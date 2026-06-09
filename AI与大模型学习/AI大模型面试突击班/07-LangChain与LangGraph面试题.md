---
title: "LangChain与LangGraph面试题"
created: 2026-06-09
updated: 2026-06-09
tags:
  - 分类/ai
  - 分类/面试
  - 主题/LangChain
  - 主题/LangGraph
status: draft
category: interview
---

# 07 - LangChain 与 LangGraph 面试题

> 来源：飞书文档 `langchain与langgraph`。已打开折叠块后整理。
> 注意：资料里涉及 LangChain/LangGraph 版本变化的说法，面试前最好再按当前官方文档复核一次。

## 一、模型私有化部署怎么回答

### 面试问法

你之前的项目做过模型私有化部署吗？

### 回答要点

可以按“部署过什么模型、用什么硬件、推理框架、吞吐指标”来讲：

```
做过。受服务器算力限制，我们部署过 Qwen3-32B，也尝试过更大模型的量化版本。部署时会根据显存选择量化精度，比如 INT8；推理服务用 vLLM 暴露 OpenAI 兼容接口。硬件上使用多张 H20/A 系列 GPU，关注显存、并发、首 token 延迟和 tokens/s。
```

回答时不要硬背具体型号，关键是讲清楚：

- 模型大小和精度：7B/32B/70B/更大模型，FP16/INT8/INT4。
- 推理框架：vLLM、TGI、SGLang 等。
- 部署指标：QPS、TTFT、TPOT、tokens/s、显存占用。
- 资源约束：显存、上下文长度、KV Cache。

## 二、LangGraph 的 state、短期记忆和长期记忆

### 1. state 是什么

LangGraph 中的 state 是图运行过程中的共享状态，包含：

- 输入输出消息。
- 当前流程中间结果。
- 节点之间传递的数据。
- 工具调用结果。
- 业务字段，例如用户画像、任务状态、风险等级等。

通常可以继承 `MessagesState`，因为它已经提供了 `messages` 字段，用于保存对话消息列表。

### 2. 短期记忆

短期记忆保存单个会话内的交互数据。核心是：

- 使用 `checkpointer` 保存图执行状态。
- 每次调用图时传入 `thread_id`。
- 同一个 `thread_id` 对应同一段会话历史。

常见实现：

- 测试或本地：`InMemorySaver`。
- 需要持久化：Postgres / SQLite / Redis 等 checkpointer。

面试话术：

```
短期记忆主要靠 checkpointer 和 thread_id 实现。checkpointer 保存每一步图执行后的 state，thread_id 用来区分不同会话。用户连续对话时，只要传入同一个 thread_id，LangGraph 就能恢复前面的状态。
```

### 3. 长期记忆

长期记忆跨会话保存用户偏好、历史事实、业务数据等。可以用：

- 关系型数据库保存结构化记忆。
- 向量库保存语义记忆。
- `Store` / 自定义存储接口保存 key-value 记忆。

面试话术：

```
长期记忆不是简单把所有历史消息塞进上下文，而是把有价值的信息抽取出来，持久化到数据库或向量库中。下次用户进入新会话时，再根据 user_id 或语义检索召回相关记忆。
```

## 三、不同用户的历史信息怎么区分

核心是两个维度：

- `thread_id`：区分会话。
- `user_id`：区分用户。

短期对话历史通常按 `thread_id` 隔离；长期记忆通常按 `user_id` 或 `(user_id, namespace)` 隔离。

```text
user_id = 用户维度
thread_id = 会话维度
namespace = 记忆分类，如 profile / preference / task
```

## 四、Human-in-the-loop 怎么做

LangGraph 的人机协同主要靠三件事：

1. `interrupt()`：在关键节点暂停工作流，返回待确认信息。
2. `checkpointer`：保存暂停时的完整状态。
3. `Command(resume=...)`：人工确认后恢复执行。

面试话术：

```
我们会在高风险节点做 Human-in-the-loop，比如写操作、审批、发货、删除数据。节点里调用 interrupt 暂停图执行，把确认信息返回前端。用户确认后，再用 Command(resume=...) 恢复图执行。因为有 checkpointer，系统能从中断点继续，而不是重新跑整个流程。
```

## 五、LangGraph 每次回答多久

可以按项目体验回答：

```
普通问题一般 1 到 5 秒。为了用户体验，我们前端用流式输出，不等整个图执行完才展示。中间节点的执行状态也可以流式推给前端，比如“正在检索知识库”“正在调用订单接口”“正在生成答案”。
```

不要只说总耗时，也要拆：

- 首 token 延迟。
- 工具调用耗时。
- RAG 检索耗时。
- 多 Agent 路由耗时。
- 最终生成耗时。

## 六、LangChain 和 LangGraph 的区别

### LangChain 更适合

- 快速开发简单应用。
- 单轮问答、摘要、基础 RAG。
- 固定流程的工具调用。
- 使用 `create_agent` 快速验证需求。
- 利用现成 chain 模板快速落地。

### LangGraph 更适合

- 多步骤复杂任务。
- 条件分支、循环、重试、中断。
- 有状态多轮交互。
- 多 Agent 协作。
- 生产级、长周期、需要稳定控制的应用。

面试话术：

```
LangChain 更像上层应用开发框架，适合快速集成模型、工具、RAG 和 Agent。LangGraph 更像底层状态机和工作流编排框架，适合做有状态、可恢复、可控制的复杂 Agent 系统。简单场景用 LangChain 快，复杂生产场景我会用 LangGraph 控制流程。
```

## 七、Function Calling 怎样保证准确调用

工具定义要让模型“看得懂、选得准、参数填得对”：

- 描述清楚：工具能解决什么问题。
- 参数明确：类型、必填、可选、约束。
- 参数不要太多：复杂场景拆成多个工具。
- 提供调用示例：JSON 格式示例。
- 标注返回结构：便于模型根据工具结果继续推理。
- 工具数量过多时拆 Agent 或按场景动态加载。

## 八、条件边怎么用

条件边相当于图里的 `if-else`。

组成：

- 路由函数：接收 state，返回路由 key。
- 路径映射：把 key 映射到节点名。
- 起始节点：从哪个节点引出条件分支。

```python
def router(state):
    if state["number"] % 2 == 0:
        return "even"
    return "odd"

workflow.add_conditional_edges(
    "check_number",
    router,
    {
        "even": "process_even",
        "odd": "process_odd",
    },
)
```

## 九、多 Agent API 和思想

资料中提到三类思路：

- Supervisor：一个主管 Agent 负责任务拆解和路由，多个 Worker Agent 负责具体能力。
- Swarm：多个 Agent 去中心化协作，通过 handoff 互相转交任务。
- DeepAgents：更完整的深度任务框架，强调规划器、文件系统、子 Agent、长期任务能力。

面试中可以稳妥地说：

```
我实际更倾向 Supervisor 架构，因为它更容易控制、调试和审计。Swarm 更灵活，但生产系统里可控性差一些。复杂长期任务可以参考 DeepAgents 的规划、文件系统和子 Agent 思路。
```

## 十、LangGraph 工具调用过程

1. 定义工具：清晰描述用途，复杂参数用 Pydantic 模型。
2. 绑定工具：把工具描述交给模型。
3. 模型决策：根据用户输入判断是否调用工具。
4. 参数生成：模型输出结构化工具调用请求。
5. 执行工具：外部代码真正调用 API / 数据库 / 函数。
6. 观察结果：工具结果回填到消息上下文。
7. 继续循环：模型决定继续调用工具还是给最终答案。

需要注意：

- 网络工具要有超时和重试。
- 工具异常要捕获，并返回可理解的错误。
- 工具超过一定数量时，按业务拆分给不同 Agent。

## 十一、Function Calling 原理

Function Calling 的本质不是模型执行函数，而是模型生成结构化调用指令。

```text
用户问题
  -> 模型理解意图
  -> 模型选择函数并生成参数
  -> 外部代码执行函数
  -> 函数结果返回模型
  -> 模型继续推理或生成最终答案
```

在 LangChain 中，Tool 就是封装好的 Function；Agent 管理“思考 - 行动 - 观察”的循环。

## 十二、异步编程用在哪里

LangChain / LangGraph 开发 Agent 时，异步常见于：

- 并发调用多个工具。
- 并发检索多个知识库。
- 流式输出 token。
- 长耗时外部 API 调用。
- 多 Agent 并行执行子任务。
- Web 服务中避免阻塞请求线程。

面试话术：

```
异步不是为了炫技，而是为了减少等待。比如 RAG 可以并发查向量库和关键词索引，多工具可以并发执行，LLM 输出可以流式返回前端。这样整体延迟会比串行流程低很多。
```

## 关键要点

1. LangChain 偏快速集成，LangGraph 偏复杂有状态编排。
2. LangGraph 的记忆核心是 state + checkpointer + thread_id。
3. 长期记忆要按 user_id / namespace 隔离，不能混在短期消息里。
4. Human-in-the-loop 用 interrupt + checkpoint + resume。
5. Function Calling 是模型生成结构化调用请求，外部代码执行工具。
6. 工具多了要拆 Agent、拆 Skill 或按场景动态加载。

---

**相关笔记**：[[MOC-LangChain学习]] | [[LC-11-LangGraph状态图工作流]] | [[LC-05-Agent工具与结构化输出]] | [[08-Agent与Multi-Agent面试题]]
