---
title: "LC-08-Agent长期记忆"
created: 2026-05-29
updated: 2026-06-07
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/进阶
status: complete
prev: "[[LC-07-Agent短期记忆]]"
next: "[[LC-09-Agent记忆综合案例]]"
source: "https://cloud.fynote.com/share/d/jA0JAHWpQ"
---

# LC-08 Agent 长期记忆

> 长期记忆让 Agent 跨会话保存和召回用户偏好、事实、历史行为和经验规则，是个性化 AI 应用的基础。

## 5.1 长期记忆是什么

长期记忆（Long-term Memory）解决的是“跨会话还要记住什么”的问题。它不绑定某个 `thread_id`，而是存储在 LangGraph Store 中，通过 `namespace + key` 组织。

| 概念 | 作用 |
|------|------|
| Store | 长期记忆存储组件 |
| namespace | 记忆命名空间，通常包含用户 ID、业务域 |
| key | 某条记忆的唯一标识 |
| value | JSON 文档，存储用户事实、偏好、规则等 |
| `runtime.store` | 工具中读写长期记忆的入口 |

长期记忆的典型内容：
- 用户身份信息
- 用户偏好，如喜欢什么颜色、品牌、商品类型
- 历史行为，如常买什么、常问什么
- 系统经验，如某类问题的处理规则

## 5.2 Store 基本使用

测试环境可以使用 `InMemoryStore`：

```python
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()

namespace = ("user_123", "preferences")

store.put(
    namespace,
    "favorite_color",
    {"category": "color", "value": "蓝色"},
)

memory = store.get(namespace, "favorite_color")
print(memory.value)

results = store.search(namespace)
for item in results:
    print(item.key, item.value)
```

生产环境应使用数据库型 Store，例如 Postgres 或 MySQL，避免进程重启后丢失长期记忆。

## 5.3 在 Agent 中使用长期记忆

创建 Agent 时传入 `store`，工具中通过 `ToolRuntime` 访问 `runtime.store`。

```python
from langchain.agents import create_agent
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()

agent = create_agent(
    model=deepseek_llm,
    tools=[],
    store=store,
)
```

读取长期记忆的工具：

```python
from langchain_core.tools import tool
from langgraph.prebuilt import ToolRuntime

@tool
def get_user_preferences(runtime: ToolRuntime) -> str:
    """读取用户长期偏好。"""
    user_id = runtime.context.user_id
    namespace = (user_id, "preferences")
    memories = runtime.store.search(namespace)

    if not memories:
        return "暂无长期偏好记录。"

    return "\n".join(str(item.value) for item in memories)
```

写入长期记忆的工具：

```python
import uuid

@tool
def save_user_preference(category: str, value: str, runtime: ToolRuntime) -> str:
    """保存用户长期偏好。"""
    user_id = runtime.context.user_id
    namespace = (user_id, "preferences")
    key = str(uuid.uuid4())

    runtime.store.put(
        namespace,
        key,
        {"category": category, "value": value},
    )

    return f"已保存偏好：{category} = {value}"
```

## 5.4 短期记忆和长期记忆区别

| 对比维度 | 短期记忆 | 长期记忆 |
|----------|----------|----------|
| 作用域 | 单个线程 / 会话 | 跨线程 / 跨会话 |
| 核心标识 | `thread_id` | `namespace + key` |
| 管理组件 | Checkpointer | Store |
| 主要内容 | 对话历史、当前任务状态 | 用户偏好、事实、经验规则 |
| 生命周期 | 随会话存在，可过期清理 | 长期保存，除非显式删除 |
| 访问方式 | `runtime.state` / `agent.get_state()` | `runtime.store` |
| 典型场景 | 记住本轮对话刚说过什么 | 记住用户长期喜欢什么 |

最容易混淆的点：**用户 ID 不是 thread_id。** 同一个用户可以有多个会话线程，短期记忆只在某个线程中连续；长期记忆应该按用户或组织维度保存，供多个线程共享。

## 5.5 记忆设计建议

长期记忆不应该什么都存。比较合理的存储对象是：
- 用户明确表达的偏好
- 多次交互中稳定出现的事实
- 可复用的任务经验
- 对后续回答有长期价值的业务信息

不适合长期保存：
- 一次性闲聊
- 临时查询参数
- 敏感信息或不该持久化的数据
- 没有确认过的模型猜测

企业项目中建议把长期记忆写入做成工具或服务层能力，并加入权限、过期、审计和删除机制。

## 面试表达

LangChain 的长期记忆基于 LangGraph Store，核心是用 `namespace + key` 保存 JSON 文档。它和短期记忆不同，短期记忆跟 `thread_id` 绑定，用 checkpointer 保存会话状态；长期记忆跨线程存在，用 store 保存用户偏好、事实和经验规则。在项目中，我会让工具通过 `runtime.store` 读写长期记忆，并用用户 ID、业务域作为 namespace，避免把一次性上下文和长期偏好混在一起。

## 知识关联

- 上一篇：[[LC-07-Agent短期记忆]]
- 下一篇：[[LC-09-Agent记忆综合案例]]
- 相关：[[LC-09-Agent记忆综合案例]] — 查看短期记忆与长期记忆如何组合使用

---

*上一篇：[[LC-07-Agent短期记忆]] | 下一篇：[[LC-09-Agent记忆综合案例]]*
