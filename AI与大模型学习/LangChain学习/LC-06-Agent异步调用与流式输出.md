---
title: "LC-06-Agent异步调用与流式输出"
created: 2026-05-21
updated: 2026-06-07
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/进阶
status: in-progress
prev: "[[LC-05-Agent工具与结构化输出]]"
next: "[[LC-07-Agent短期记忆]]"
---

# LC-06 Agent 异步调用与流式输出

> 异步调用提升 Agent 并发性能；流式输出实现实时交互体验

## 3.6 Agent 异步调用

Agent 的异步调用（`ainvoke`、`astream`、`abatch`）与模型的异步调用原理一致，但在 Agent 场景下价值更大——因为 Agent 通常涉及多轮推理和多次工具调用。需要注意的是，只有把多个任务并发调度起来，异步才会明显减少整体等待时间；单纯在 `for` 循环中逐个 `await`，本质上仍然是顺序执行。

```python
import asyncio

async def query_city_info(agent, city):
    """异步查询单个城市信息"""
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": f"查询{city}的天气和景点信息"}]}
    )
    return result

async def main():
    # 顺序异步查询多个城市
    cities = ["北京", "上海"]
    for city in cities:
        result = await query_city_info(agent, city)
        print(f"\n## {city}信息")
        print(result["messages"][-1].content)

    # 北京到上海交通信息
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "从北京到上海的交通方式有哪些？"}]}
    )
    print(f"\n## 北京到上海交通信息")
    print(result["messages"][-1].content)

asyncio.run(main())
```

**并发查询多个城市：**

```python
async def main_parallel():
    cities = ["北京", "上海", "广州"]
    tasks = [query_city_info(agent, city) for city in cities]
    results = await asyncio.gather(*tasks)

    for city, result in zip(cities, results):
        print(f"\n## {city}信息")
        print(result["messages"][-1].content)

asyncio.run(main_parallel())
```

## 3.7 Agent 流式输出及模式

### 3.7.1 Agent 流式输出

Agent 的流式输出通过 `agent.stream()` 方法实现，它返回一个迭代器，可以在 Agent 执行过程中实时获取中间结果：

```python
# 创建客户服务 Agent
agent = create_agent(
    model=deepseek_llm,
    tools=[query_customer_data, check_order_history, get_current_promotions]
)

# 流式输出
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "查询客户 CUST123456 的信息"}]},
    stream_mode="updates"  # 指定输出模式
):
    print(chunk)
```

### 3.7.2 流式输出模式

LangChain Agent 提供 7 种流式输出模式，通过 `stream_mode` 参数指定：

#### 3.7.2.1 values 模式

每个步骤执行后输出**完整的状态信息**：

```python
for chunk in agent.stream(
    {"messages": [...]},
    stream_mode="values"
):
    print(chunk)
```

#### 3.7.2.2 updates 模式（默认）

每个步骤执行后只输出**增量更新**的内容：

```python
for chunk in agent.stream(
    {"messages": [...]},
    stream_mode="updates"
):
    print(chunk)
```

#### 3.7.2.3 messages 模式

输出流式返回的 **Token 以及相关元数据**（如来自哪个节点 model/tool），适合实现类似 ChatGPT 的打字机效果：

```python
for chunk in agent.stream(
    {"messages": [...]},
    stream_mode="messages"
):
    print(chunk)
```

#### 3.7.2.4 tasks 模式

输出当前 task 任务信息，包含任务的结果和错误信息：

```python
for chunk in agent.stream(
    {"messages": [...]},
    stream_mode="tasks"
):
    print(chunk)
```

#### 3.7.2.5 debug 模式

与 tasks 模式类似，但额外输出任务步骤、时间戳、task 类型等信息，用于调试：

```python
for chunk in agent.stream(
    {"messages": [...]},
    stream_mode="debug"
):
    print(chunk)
```

#### 3.7.2.6 checkpoints 模式

当检查点（checkpoint）被创建时触发输出，输出包含检查点中的状态。用于需要状态持久化、工作流恢复或分布式执行跟踪的高级场景：

```python
from langgraph.checkpoint.memory import InMemorySaver

# 创建内存检查点存储
checkpointer = InMemorySaver()

agent = create_agent(
    model=deepseek_llm,
    tools=[...],
    checkpointer=checkpointer
)

# 创建唯一的会话 ID
thread_id = "session-001"
config = {"configurable": {"thread_id": thread_id}}

for chunk in agent.stream(
    {"messages": [...]},
    config=config,
    stream_mode="checkpoints"
):
    print(chunk)
```

#### 3.7.2.7 custom 模式

通过 `get_stream_writer` 在工具或节点内部**自定义发送的数据**，用于输出业务逻辑相关的进度信息：

```python
from langgraph.config import get_stream_writer

@tool
def generate_sales_report() -> str:
    """生成销售报告"""
    writer = get_stream_writer()
    writer({"type": "进度", "message": "开始生成销售报告..."})
    # 报告生成逻辑...
    writer({"type": "进度", "message": "销售报告生成完成"})
    return "销售报告: ..."
```

### 3.7.3 流式输出模式总结

| 模式 | 输出内容 | 使用场景 |
|------|----------|----------|
| **values** | 每步执行后的完整状态信息 | 需要获取每一步完整状态、状态持久化 |
| **updates（默认）** | 每步增量更新的内容 | 监控 Agent 执行进度 |
| **messages** | 流式返回的 Token 及元数据 | ChatGPT 打字机效果、实时交互 |
| **tasks** | 当前 task 信息（结果/错误） | 监控任务生命周期 |
| **debug** | 比 tasks 多输出步骤、时间戳 | 调试、详细监控 |
| **checkpoints** | 检查点创建时的状态 | 状态持久化、工作流恢复 |
| **custom** | 自定义业务数据 | 进度信息、自定义日志 |

**选择建议：**
- 实时对话交互 → `messages` 模式
- 观察 Agent 思考与执行步骤 → `updates` 模式
- 查看每一步状态 → `values` / `tasks` / `debug` 模式
- 工具执行时输出自定义日志 → `custom` 模式

**模式可组合使用：**

```python
for stream_mode, chunk in agent.stream(
    {"messages": [...]},
    stream_mode=["tasks", "updates"]  # 组合多个模式
):
    print(f"模式: {stream_mode}, 数据: {chunk}")
```

> 多模式组合时，迭代器返回的是 `(stream_mode, chunk)` 元组，`stream_mode` 是当前模式名称，`chunk` 是该模式的结果。

## 关键面试考点

1. Agent 异步调用有什么优势？在什么场景下使用？
2. Agent 流式输出的 7 种模式分别是什么？各自的特点？
3. 实现类似 ChatGPT 的打字机效果应该用哪种模式？
4. 流式输出模式如何组合使用？返回的数据格式是什么？
5. `get_stream_writer` 的作用是什么？

## 知识关联

- 上一篇：[[LC-05-Agent工具与结构化输出]]
- 下一篇：[[LC-07-Agent短期记忆]]
- 相关：[[LC-02-模型调用与Chat Models]] — 模型的异步调用基础

---

*上一篇：[[LC-05-Agent工具与结构化输出]] | 下一篇：[[LC-07-Agent短期记忆]]*
