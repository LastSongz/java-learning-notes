---
title: "LC-07-Agent短期记忆"
created: 2026-05-29
updated: 2026-06-07
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/进阶
status: complete
prev: "[[LC-06-Agent异步调用与流式输出]]"
next: "[[LC-08-Agent长期记忆]]"
source: "https://cloud.fynote.com/share/d/jA0JAHWpQ"
---

# LC-07 Agent 短期记忆

> 短期记忆让 Agent 在同一个会话线程中记住之前的对话和临时状态，是多轮对话、任务续接和上下文感知的基础。

## 4.1 短期记忆是什么

短期记忆（Short-term Memory）也叫线程范围记忆（Thread-scoped Memory），作用范围是单个会话线程。它解决的是“当前这轮对话里刚刚发生过什么”的问题。

在 LangChain v1.x 中，短期记忆是 Agent State 的一部分，通过 checkpointer 持久化。每个会话使用 `thread_id` 隔离状态：

| 概念 | 作用 |
|------|------|
| `thread_id` | 会话线程 ID，用来区分不同用户或不同对话 |
| `AgentState` | Agent 的状态容器，默认包含 `messages` |
| `messages` | 当前线程中的对话历史 |
| `checkpointer` | 每一步执行后保存状态快照 |
| `agent.get_state(config)` | 查看某个 `thread_id` 当前保存的状态 |

短期记忆的典型场景：
- 用户说“我叫张三”，下一轮问“我叫什么？”
- 当前会话中正在查询某个订单号
- 多步骤任务执行到一半，需要在下一轮继续

## 4.2 使用 checkpointer 启用短期记忆

测试环境可以使用内存型 checkpointer：

```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

agent = create_agent(
    model=deepseek_llm,
    tools=[],
    checkpointer=checkpointer,
)

config = {"configurable": {"thread_id": "conversation_1"}}

agent.invoke(
    {"messages": [{"role": "user", "content": "你好，我叫张三"}]},
    config,
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "我叫什么名字？"}]},
    config,
)

print(response["messages"][-1].content)
```

生产环境不要只用内存存储，因为进程重启会丢失状态。应使用数据库型 checkpointer，例如 Postgres、MySQL、SQLite 等。

```python
from langgraph.checkpoint.mysql.pymysql import PyMySQLSaver

DB_URI = "mysql+pymysql://root:123456@localhost:3306/langchain_db?charset=utf8mb4"

with PyMySQLSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()
    agent = create_agent(
        model=deepseek_llm,
        tools=[],
        checkpointer=checkpointer,
    )
```

## 4.3 自定义短期记忆状态

默认 `AgentState` 主要保存 `messages`。业务系统中经常需要额外保存当前订单号、用户等级、城市、临时筛选条件等字段，这时可以扩展 `AgentState`。

```python
from langchain.agents import AgentState, create_agent
from langgraph.checkpoint.memory import InMemorySaver

class CustomerSessionState(AgentState):
    user_id: str
    current_order_id: str | None = None
    city: str | None = None

agent = create_agent(
    model=deepseek_llm,
    tools=[],
    state_schema=CustomerSessionState,
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": "user_001"}}

agent.invoke(
    {
        "messages": [{"role": "user", "content": "我想查订单 order001"}],
        "user_id": "user_001",
        "current_order_id": "order001",
    },
    config=config,
)
```

要点：
- 自定义字段必须声明在 `state_schema` 中，否则不会作为 Agent 状态管理。
- 首次调用传入状态后，后续同一 `thread_id` 可以从状态中继续读取。
- 短期记忆是会话级状态，不适合永久保存用户偏好。

## 4.4 访问和修改短期记忆

### 通过工具读取状态

工具可以通过 `ToolRuntime` 访问当前状态。`runtime` 不会暴露给模型，是运行时内部参数。

```python
from langchain_core.tools import tool
from langgraph.prebuilt import ToolRuntime

@tool
def get_current_order(runtime: ToolRuntime) -> str:
    """查询当前会话正在处理的订单号。"""
    order_id = runtime.state.get("current_order_id")
    return f"当前订单号是：{order_id or '无'}"
```

### 通过工具修改状态

工具可以返回 `Command(update=...)` 来更新 Agent 状态。

```python
from langchain_core.messages import ToolMessage
from langgraph.types import Command

@tool
def set_current_order(order_id: str, runtime: ToolRuntime) -> Command:
    """设置当前会话正在处理的订单号。"""
    return Command(
        update={
            "current_order_id": order_id,
            "messages": [
                ToolMessage(
                    content=f"已记录当前订单号：{order_id}",
                    tool_call_id=runtime.tool_call_id,
                )
            ],
        }
    )
```

### 通过中间件修改状态

`@before_model` 适合在模型调用前清理、裁剪或补充状态；`@after_model` 适合在模型调用后提取结构化结果并写入状态。

常见用法：
- 模型调用前裁剪过长消息
- 模型调用后把订单号、商品名、意图分类写入状态
- 对历史消息做摘要，避免上下文过长

## 4.5 State 和 Context 的区别

| 对比项 | State | Context |
|--------|-------|---------|
| 是否随会话变化 | 会变化 | 通常不变 |
| 是否持久化到 checkpointer | 是 | 否 |
| 典型内容 | `messages`、当前订单号、当前步骤 | 用户 ID、渠道、租户、权限 |
| 生命周期 | 跟随 `thread_id` | 单次运行传入 |
| 工具访问 | `runtime.state` | `runtime.context` |

一句话：**State 是 Agent 在当前会话里“记住的过程状态”，Context 是外部系统给这次调用的“运行背景”。**

## 4.6 长上下文处理

短期记忆如果无限保存 `messages`，很快会超过模型上下文窗口。常见处理策略：

| 策略 | 说明 | 适用场景 |
|------|------|----------|
| Trim Message | 保留最近 N 条消息 | 简单聊天、成本敏感场景 |
| Delete Message | 删除指定消息或清空历史 | 需要强制遗忘某些内容 |
| Summarize Message | 将早期对话压缩成摘要 | 长对话、客服场景 |
| Custom Strategy | 自定义过滤、归档、摘要策略 | 复杂业务系统 |

可以使用 `SummarizationMiddleware` 对长对话做摘要：

```python
from langchain.agents.middleware import SummarizationMiddleware

agent = create_agent(
    model=deepseek_llm,
    tools=[],
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model=deepseek_llm,
            summary_prompt="请总结以下对话内容：{messages}",
            trigger=("messages", 10),
            keep=("messages", 5),
        )
    ],
)
```

## 面试表达

LangChain Agent 的短期记忆是线程级的状态管理能力，核心由 `thread_id`、`AgentState` 和 checkpointer 组成。它主要解决同一会话中的上下文连续性问题，比如多轮聊天、当前任务进度、当前订单号等。生产环境中我会用数据库型 checkpointer 持久化状态，并通过 `state_schema` 扩展业务字段；如果消息过长，会用裁剪、删除或摘要策略控制上下文长度。

## 知识关联

- 上一篇：[[LC-06-Agent异步调用与流式输出]]
- 下一篇：[[LC-08-Agent长期记忆]]
- 相关：[[LC-09-Agent记忆综合案例]] — 将短期记忆放进完整客服 Agent 场景

---

*上一篇：[[LC-06-Agent异步调用与流式输出]] | 下一篇：[[LC-08-Agent长期记忆]]*
