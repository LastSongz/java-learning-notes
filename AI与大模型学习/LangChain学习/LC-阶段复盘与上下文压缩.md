---
title: "LC-阶段复盘与上下文压缩"
created: 2026-07-12
updated: 2026-07-12
tags:
  - 分类/langchain
  - 分类/ai
  - 类型/复盘
status: in-progress
---

# LC 阶段复盘与上下文压缩

> 这份笔记用于压缩学习上下文：后续继续学习时，优先从这里恢复主线，不需要回看完整对话。

## 当前学习进度

已完成主线：

```text
LC-01 LangChain 概述与核心架构
LC-02 模型调用与 Chat Models
LC-03 模型结构化输出与工具调用
LC-04 Agent 智能体基础
LC-05 Agent 工具与结构化输出
LC-06 Agent 异步调用与流式输出
LC-07 Agent 短期记忆
LC-08 Agent 长期记忆
LC-09 Agent 记忆综合案例
LC-10 RAG 检索增强生成实战：已学到 Prompt 约束与 sources，下一步是检索质量优化
```

配套手敲 Demo 入口：[[LC-Demo手敲指南-Java与Python]]

## 总体知识地图

LangChain 不是单纯的大模型 API 封装，而是一套大模型应用开发框架：

```text
Model：统一调用大模型
Prompt：组织输入和约束行为
Structured Output：让模型结果可解析
Tool：连接外部动作和业务系统
Agent：自动管理工具调用和多轮执行循环
Memory：保存会话状态和长期偏好
RAG：连接外部知识库
LangGraph：复杂状态图和工作流编排
LangSmith：调试、追踪、评测和监控
```

核心学习主线：

```text
模型调用
-> 结构化输出
-> 工具调用
-> Agent 自动循环
-> Agent 工具工程化
-> Agent 异步与流式输出
-> Agent 短期/长期记忆
-> RAG 知识库问答
```

## LC-01：LangChain 核心认知

普通 LLM 调用：

```text
用户问题 -> LLM -> 文本回答
```

LangChain 应用：

```text
用户问题
-> Prompt
-> Model
-> Tool / RAG
-> Agent / LangGraph
-> Structured Output
-> 业务结果
```

关键理解：

- LangChain 解决的是大模型应用工程化问题，不只是调用模型。
- Tool 扩展模型行动能力，RAG 扩展模型知识来源，Agent 负责围绕目标做决策和执行。
- LangGraph 是复杂 Agent 和工作流的底层编排能力。

## LC-02：模型调用与 Chat Models

Chat Model 的输入输出：

```text
messages -> AIMessage
```

常见消息：

```text
SystemMessage：规则、身份、背景
HumanMessage / UserMessage：用户输入
AIMessage：模型回复，也可能包含 tool_calls
ToolMessage：工具执行结果
```

四类调用：

```text
invoke：同步调用，一次性返回完整结果
stream：流式输出，适合聊天页面和长文本生成
batch：批量处理多个互不依赖的问题
async / ainvoke：异步非阻塞，适合 Web 服务和高并发
```

工程判断：

```text
普通后台任务 -> invoke
聊天页面打字机效果 -> stream
批量生成题目/摘要 -> batch
高并发 Web 接口 -> async / ainvoke / abatch
```

## LC-03：结构化输出与工具调用

结构化输出解决的问题：

```text
自然语言输出不稳定，程序难以解析
```

目标是把模型输出变成：

```json
{
  "intent": "refund",
  "order_id": "A123",
  "confidence": 0.91
}
```

三种结构定义：

```text
Pydantic：Python 项目推荐，强类型，返回对象
TypedDict：轻量，返回 dict
JSON Schema：跨语言标准，适合接口协议
```

`with_structured_output` 和 Output Parser：

```text
with_structured_output：更现代，直接让模型按 schema 返回结构化结果
Output Parser：通过 Prompt 要求模型输出 JSON，再解析，兼容性更强
```

`bind_tools` 的关键点：

```text
bind_tools 只是把工具 schema 告诉模型
模型返回 tool_calls
程序员要自己执行工具、追加 ToolMessage、再调用模型
```

## LC-04：Agent 智能体基础

Agent 的工程定义：

```text
Agent = LLM + Tools + Prompt + 执行循环 + 消息状态
```

`bind_tools` 与 `create_agent` 区别：

```text
bind_tools：
只让模型产生 tool_calls，不自动执行工具

create_agent：
自动执行工具调用，追加 ToolMessage，并让模型继续推理直到最终回答
```

ReAct 循环：

```text
Reasoning：推理，判断下一步做什么
Acting：行动，调用工具或生成最终回答
Observation：观察，读取工具返回结果
```

Agent 输入使用 `{"messages": [...]}`，因为它维护的是完整消息状态，而不是一句孤立文本。

## LC-05：Agent 工具与结构化输出

好工具需要：

```text
工具名清楚
参数名清楚
参数类型完整
docstring / description 明确说明用途和调用时机
职责单一
```

工具创建方式：

```text
@tool：
简单工具，参数少，适合查天气、计算、按 ID 查询

Pydantic args_schema：
复杂参数，强校验，适合工单、订单、报表等企业工具

JSON Schema：
动态工具定义、跨系统、平台化场景
```

Agent 结构化输出：

```python
response_format=ToolStrategy(InterviewFeedback)
```

最终结果：

```python
resp["structured_response"]
```

核心理解：

```text
Tool Calling 让模型连接外部能力
Structured Output 让最终结果进入业务系统
```

## LC-06：Agent 异步调用与流式输出

异步调用：

```text
ainvoke 只有在多个任务并发调度时才明显提升整体效率
```

错误示例：

```text
for 循环里逐个 await：仍然接近串行
```

正确思路：

```python
tasks = [query_city(city) for city in cities]
results = await asyncio.gather(*tasks)
```

常用流模式：

```text
updates：看 Agent 每一步做了什么
messages：看模型 token 输出，适合打字机效果
custom：工具或节点主动输出业务进度
```

工程判断：

```text
调试 Agent 执行过程 -> stream_mode="updates"
聊天页面逐字输出 -> stream_mode="messages"
长任务进度条 -> stream_mode="custom"
```

## LC-07：Agent 短期记忆

短期记忆解决：

```text
同一个会话里，Agent 怎么记住刚发生过什么
```

核心组件：

```text
thread_id：会话线程 ID，用于隔离不同会话
AgentState：Agent 当前状态，默认包含 messages
checkpointer：保存和恢复状态快照
messages：会话历史消息
```

关键表达：

```text
短期记忆通过 checkpointer 按 thread_id 保存会话状态。
同一个 thread_id 可以恢复上下文，不同 thread_id 互相隔离。
```

适合放短期记忆：

```text
当前订单号
当前任务步骤
当前城市
当前筛选条件
同一会话的对话历史
```

## LC-08：Agent 长期记忆

长期记忆解决：

```text
跨会话记住用户偏好、稳定事实和可复用经验
```

核心组件：

```text
Store：长期记忆存储
namespace：记忆命名空间，通常包含 user_id 和业务域
key：某条记忆的唯一标识
value：JSON 文档
runtime.store：工具中读写长期记忆的入口
```

短期记忆和长期记忆区别：

```text
短期记忆：thread_id + checkpointer + state
长期记忆：namespace + key + store
```

重要边界：

```text
user_id 不是 thread_id
一个 user_id 可以有多个 thread_id
```

适合长期保存：

```text
用户明确表达的偏好
稳定事实
长期有价值的信息
可复用任务经验
```

不适合长期保存：

```text
一次性闲聊
临时查询参数
敏感信息
未经确认的模型猜测
真实订单/支付/审计记录，这些应该放业务数据库
```

## LC-09：Agent 记忆综合案例

电商客服 Agent 的分层：

```text
Context：外部系统传入的背景，如 user_id、权限、渠道
State：当前会话动态状态，如 current_order_id
Store：跨会话长期记忆，如 favorite_brand
Tools：查询订单、保存偏好、读取偏好、推荐商品
Agent：调度工具、读写状态、生成回答
```

核心边界：

```text
当前订单号 -> State
用户长期偏好 -> Store
用户 ID / 权限 -> Context
真实业务记录 -> 业务数据库
```

面试表达：

```text
我会把 Agent 记忆分为短期状态和长期记忆。短期状态通过 checkpointer 按 thread_id 保存，用于同一会话内任务续接；长期记忆通过 store 按 user_id 和业务 namespace 保存，用于跨会话个性化。Context 由外部系统传入，表示本次调用的用户身份、权限和渠道。
```

## LC-10：RAG 检索增强生成实战

当前已学到：

```text
RAG 基本链路
文档切分、Embedding、Vector Store、Retriever
Prompt 约束、sources 引用、资料不足时拒答
```

RAG 不是让模型永久记住更多知识，而是在用户提问时：

```text
从外部知识库动态检索相关资料
把资料作为 context 交给模型
让模型基于资料生成答案
```

标准链路：

```text
Load -> Split -> Embed -> Store -> Retrieve -> Prompt -> Generate -> Sources
```

索引阶段：

```text
文档加载
清洗
切分 chunk
Embedding 向量化
存入 Vector Store
```

问答阶段：

```text
用户提问
Retriever 检索相关 chunk
组装 context + question
Prompt 约束模型只基于资料回答
LLM 生成答案
返回 sources
```

关键组件：

```text
Embedding Model：把文本转换成语义向量
Vector Store：保存向量并支持相似度搜索
Retriever：输入问题，返回相关 Document 列表
top_k：返回最相关的前 K 个 chunk
```

切分要点：

```text
整篇文档向量化会导致语义混杂、检索不精准、噪声过多。
chunk_size 太小会导致上下文不足，太大会导致语义混杂。
chunk_overlap 用于避免关键信息刚好被切分边界截断。
```

RAG Prompt 关键约束：

```text
只根据资料回答
资料没有答案就明确说没有找到
不要编造
最好返回引用来源 sources
```

## 当前上下文压缩摘要

后续继续学习时，只需要带着下面这段即可：

```text
我们已经完成 LangChain LC-01 到 LC-09，并学习 LC-10 RAG 到 Prompt 约束和 sources。

已掌握：
1. LangChain 是大模型应用开发框架，不只是 API 封装。
2. Chat Model 基于 messages，核心调用有 invoke、stream、batch、async。
3. 结构化输出让模型结果变成对象、dict 或 JSON，方便进入业务系统。
4. bind_tools 只产生 tool_calls，create_agent 会自动执行工具并追加 ToolMessage。
5. Agent 基于 ReAct 循环：Reasoning、Acting、Observation。
6. 工具 docstring、参数类型和 args_schema 会直接影响 Agent 是否正确调用工具。
7. Agent 流式输出常用 updates、messages、custom。
8. 短期记忆：thread_id + checkpointer + state，保存当前会话状态。
9. 长期记忆：namespace + key + store，保存跨会话用户偏好。
10. Context 是外部调用背景，State 是当前会话状态，Store 是长期记忆。
11. RAG 是 Load -> Split -> Embed -> Store -> Retrieve -> Prompt -> Generate -> Sources 的完整链路。
12. RAG Prompt 要求模型只基于资料回答，资料不足时拒答，并尽量返回 sources。

下一步继续 LC-10：RAG 检索质量优化，包括 metadata filter、rerank、hybrid search、query rewrite、引用与置信度。
```

## 下一步学习入口

继续：RAG 检索质量优化

要回答的问题：

```text
为什么检索结果不准？
metadata filter 解决什么？
rerank 为什么能提升相关性？
hybrid search 为什么要结合关键词和向量？
query rewrite 在什么场景下有用？
RAG 怎么评估答案是否可信？
```
