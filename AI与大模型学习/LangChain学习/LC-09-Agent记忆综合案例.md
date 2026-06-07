---
title: "LC-09-Agent记忆综合案例"
created: 2026-05-29
updated: 2026-06-07
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/实战
status: complete
prev: "[[LC-08-Agent长期记忆]]"
next: "[[LC-10-RAG检索增强生成实战]]"
source: "https://cloud.fynote.com/share/d/jA0JAHWpQ"
---

# LC-09 Agent 记忆综合案例

> 综合案例的重点不是把代码背下来，而是理解一个真实客服 Agent 如何同时使用短期记忆、长期记忆、工具调用、摘要和错误处理。

## 5.5 电商客服助手目标

原始资料中的综合案例是一个智能电商客服助手，核心能力包括：

- 记住当前会话状态：用户正在查询哪个订单
- 记住长期偏好：用户喜欢的商品类型、品牌、具体商品
- 处理多轮复杂对话：对过长消息做摘要
- 调用工具：查询用户信息、查询订单、更新偏好、推荐商品
- 捕获工具异常：返回友好提示而不是直接报错
- 流式输出：让客服回复过程可观察

这类案例非常适合面试，因为它能把 Agent、Tools、Memory、Middleware、Streaming 串起来。

## 系统结构

```text
用户输入
  -> Agent
      -> Short-term Memory: 当前订单号、会话消息、临时状态
      -> Long-term Memory: 用户偏好、历史行为
      -> Tools: 查询订单、更新偏好、推荐商品
      -> Middleware: 摘要、工具错误处理
      -> Streaming: 实时输出模型和工具步骤
```

## 核心组件拆解

### Context：调用背景

Context 是外部系统传给本次调用的稳定背景信息，比如用户 ID、访问渠道、租户 ID。

```python
from pydantic import BaseModel, Field

class UserContext(BaseModel):
    user_id: str = Field(description="用户唯一标识")
    channel: str = Field(description="咨询渠道，如 Web、APP、小程序")
```

在实际项目中，如果直接传 Pydantic 对象给 `context` 出现序列化警告，可以改成传普通字典，或统一在项目层做序列化处理。

### State：当前会话状态

State 保存会话中动态变化的内容，比如当前正在查询的订单号。

```python
from langchain.agents import AgentState

class CustomerSessionState(AgentState):
    current_order_id: str | None = None
```

### Checkpointer：短期记忆

短期记忆负责保存同一个 `thread_id` 内的状态。

```python
from langgraph.checkpoint.mysql.pymysql import PyMySQLSaver

checkpointer = PyMySQLSaver.from_conn_string(DB_URI)
```

测试环境可以用 `InMemorySaver`，生产环境建议用数据库型 checkpointer。

### Store：长期记忆

长期记忆负责保存跨线程的用户偏好。

```python
from langgraph.store.mysql.pymysql import PyMySQLStore

store = PyMySQLStore.from_conn_string(DB_URI)
```

工具可以通过 `runtime.store.put(...)` 写入偏好，通过 `runtime.store.search(...)` 读取偏好。

### Tools：业务动作

案例中的工具可以拆成四类：

| 工具 | 作用 |
|------|------|
| `get_user_info` | 读取 context 和 state，返回用户当前信息 |
| `query_order_status` | 查询订单，并把当前订单号写入短期状态 |
| `update_user_preference` | 把用户偏好写入长期记忆 |
| `get_recommendation` | 结合当前订单和长期偏好做推荐 |

查询订单时，如果要同时返回工具消息并更新状态，可以返回 `Command(update=...)`。

## Agent 创建思路

```python
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, wrap_tool_call

agent = create_agent(
    model=deepseek_llm,
    tools=[
        get_user_info,
        query_order_status,
        update_user_preference,
        get_recommendation,
    ],
    system_prompt="你是一个智能电商客服助手...",
    checkpointer=checkpointer,
    store=store,
    state_schema=CustomerSessionState,
    context_schema=UserContext,
    middleware=[
        SummarizationMiddleware(
            model=deepseek_llm,
            summary_prompt="请总结以下对话内容：{messages}",
            trigger=("messages", 10),
            keep=("messages", 5),
        ),
        handle_tool_errors,
    ],
)
```

## 运行逻辑

同一个 `thread_id` 下：

```text
用户：查询订单 order001
Agent：调用 query_order_status
工具：返回订单状态，并把 current_order_id 写入 State
用户：给我推荐一些商品
Agent：读取 State 中的 current_order_id，同时读取 Store 中的长期偏好
工具：返回个性化推荐
```

切换新的 `thread_id` 后：

```text
短期记忆：当前订单号等会话状态不共享
长期记忆：用户偏好仍可按 user_id 读取
```

## 实战注意事项

- `thread_id` 用来区分会话，不要把它当成用户 ID。
- 用户长期偏好应保存在 Store 中，namespace 建议包含用户 ID 和业务域。
- 工具写状态时，要保证返回的 `ToolMessage` 带有正确的 `tool_call_id`。
- 长对话必须考虑摘要或裁剪，否则成本和质量都会下降。
- 生产环境中不要盲目保存所有对话内容，长期记忆要有权限、过期和删除策略。
- 原始资料中用 MySQL 同时保存 checkpointer 和 store，这个思路适合本地演示；真实项目可以按基础设施选择 Postgres、Redis、MySQL 或云数据库。

## 面试表达

我做 Agent 记忆设计时会把记忆分成两层：短期记忆和长期记忆。短期记忆通过 checkpointer 按 `thread_id` 保存当前会话状态，比如对话历史和当前订单号；长期记忆通过 store 按 `namespace + key` 保存跨会话的用户偏好。以电商客服为例，用户当前查询的订单号属于短期状态，用户长期喜欢的品牌和商品类型属于长期记忆。Agent 通过工具读写这些状态，再结合摘要中间件控制长上下文，最终实现可持续、多轮、个性化的客服体验。

## 知识关联

- 上一篇：[[LC-08-Agent长期记忆]]
- 下一篇：[[LC-10-RAG检索增强生成实战]]
- 相关：[[MOC-LangChain学习]] — 返回学习总导航

---

*上一篇：[[LC-08-Agent长期记忆]] | 下一篇：[[LC-10-RAG检索增强生成实战]]*
