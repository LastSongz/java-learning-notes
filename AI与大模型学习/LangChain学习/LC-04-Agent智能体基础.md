---
title: "LC-04-Agent智能体基础"
created: 2026-05-21
updated: 2026-05-21
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/核心
status: in-progress
prev: "[[LC-03-模型结构化输出与工具调用]]"
next: "[[LC-05-Agent工具与结构化输出]]"
---

# LC-04 Agent 智能体基础

> Agent 是 LangChain 的高级组件，通过将 LLM 与外部工具结合，构建能够自主推理并执行复杂任务的智能系统

## 3.1 Agent 介绍

### 3.1.1 什么是 Agent

在 LangChain 框架中，Agent（智能体）是一个高级组件，它通过将大型语言模型（LLM）与一系列外部工具（Tools）相结合，构建了一个能够**自主推理并执行复杂任务**的智能系统。其核心思想是利用 LLM 作为推理引擎（Reasoning Engine），让模型能够动态地决定为解决用户问题所需采取的行动序列，包括选择何种工具、以何种顺序调用，并迭代地处理工具返回的结果，直至任务完成。

简单来说，一个 Agent 不再仅仅是生成文本的模型，而是一个具备**"思考-行动-观察"循环**的自主工作者。当用户提出一个复杂需求时，Agent 会像人类一样，先理解任务、规划步骤、使用合适的工具（如搜索网络、查询数据库、执行计算）获取信息，最后综合所有信息给出最终答案。

### 3.1.2 Agent 原理与执行流程

Agent 的核心工作原理遵循 **ReAct（Reasoning + Acting，推理+行动）框架**，即在一个循环中交替进行推理和行动，这个过程会涉及到模型、工具、记忆、中间件等核心组件。

以下是一个具体的 ReAct 循环示例，演示 Agent 如何解决"找出当前最流行的无线耳机并检查库存"的任务：

**1) 输入解析与初始推理**

**输入**：用户查询："找出当前最流行的无线耳机并检查库存"。

**推理**：LLM 分析任务后认为："要找出'最流行'的产品，需要最新的市场信息，我应该先使用搜索工具。"

**2) 第一次行动与观察**

**行动**：Agent 调用 `search_products` 工具，参数为 "wireless headphones"。

**观察**：工具返回结果："找到5款匹配产品。Top结果：WH-1000XM5, ..."

**3) 迭代推理**

**推理**：LLM 根据搜索结果分析："WH-1000XM5 是排名第一的型号。现在需要确认其库存状态才能回答用户问题。"

**4) 第二次行动与观察**

**行动**：Agent 调用 `check_inventory` 工具，参数为 "WH-1000XM5"。

**观察**：工具返回："产品 WH-1000XM5：库存10件。"

**5) 最终输出**

**推理**：LLM 综合所有信息后认为："已获得所需信息，可以生成最终答案。"

**行动**：模型生成最终答案，不再调用工具。

### 3.1.3 LLM、LLM 工具调用与 Agent 区别

| 对比角度 | LLM | LLM+工具调用 | Agent |
|----------|-----|-------------|-------|
| **本质定位** | 文本生成器，基于训练数据生成连贯文本 | 增强型 LLM，通过函数调用扩展能力边界 | 具备规划和执行能力的智能系统，以任务闭环为目标 |
| **核心功能** | 语言理解、文本生成、知识问答 | 基础工具调用、实时数据获取、简单操作执行 | 多步规划、工具编排、状态管理、错误恢复 |
| **工作模式** | 单次交互，静态响应 | 单轮"请求-调用-响应" | 多轮"感知-规划-执行-反馈"循环（ReAct） |
| **系统架构** | 单一模型接口 | 模型+工具绑定+手动执行循环 | LLM+规划+记忆+工具使用+防护措施 |
| **状态管理** | 需外部维护状态 | 需外部维护状态 | 内置记忆系统，支持短期/长期状态管理 |
| **错误处理** | 失败即终止，无自动恢复 | 失败即终止，无自动恢复 | 支持重试、回滚等恢复机制 |

## 3.2 Agent 创建与调用

在 LangChain 1.2 中，`create_agent` API 是构建智能体的核心方式。它通过将语言模型与工具相结合，创建能够自主决策并执行复杂任务的系统。

### 3.2.1 Agent 创建方式

模型是 Agent 的"大脑"，负责决策和推理。LangChain 支持两种模型配置方式：

#### 3.2.1.1 静态模型

静态模型在 Agent 创建时一次性配置，在整个执行过程中保持不变。这是最简单、最常用的方法。

```python
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.graph.state import CompiledStateGraph

@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息。"""
    return f"{city}的天气为晴朗，25°C。"

# 通过模型实例创建，可精细控制参数
deepseek_llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

agent: CompiledStateGraph = create_agent(deepseek_llm, tools=[get_weather])

resp: dict = agent.invoke({"messages": [{"role": "user", "content": "查询北京的天气"}]})
```

> 注意：`create_agent` 返回的是 `CompiledStateGraph` 类型，它内部基于 LangGraph 构建了一个执行图（Graph）。`agent.invoke` 的参数格式固定为 `{"messages": [{"role": "...", "content": "..."}]}`。

#### 3.2.1.2 动态模型

动态模型允许在运行时根据对话状态或上下文智能地选择不同模型，通过**中间件机制**实现。对于优化成本和处理不同复杂度的任务非常有用。

```python
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse

# 定义两个模型：基础版和高级版
basic_model = init_chat_model(model="deepseek-chat", ...)
advanced_model = init_chat_model(model="qwen-plus", ...)

# 定义动态模型选择中间件
@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """根据对话消息数动态选择模型"""
    message_count = len(request.state["messages"])

    if message_count >= 3:
        model = advanced_model  # 复杂对话用高级模型
    else:
        model = basic_model     # 简单对话用基础模型

    return handler(request.override(model=model))

# 创建 Agent，并传入动态模型选择中间件
agent = create_agent(
    model=basic_model,
    tools=[get_current_location, get_weather],
    middleware=[dynamic_model_selection]  # 挂载中间件
)
```

> `@wrap_model_call` 标记的方法会在 Agent 推理循环的每个 LLM 调用前触发。`request` 封装了当前调用的所有请求信息，`handler` 是后续处理链的回调。

### 3.2.2 Agent 调用

`invoke` 是 Agent 最基本的同步调用方法。`invoke` 中传入的 `{"messages": [...]}` 对应 `input` 参数，每条消息包含 `role`（如 "user"、"assistant"、"system"、"tool"）和 `content`。

**在消息中加入 system 角色来约束 Agent 行为：**

```python
resp = agent.invoke({
    "messages": [
        {"role": "system", "content": "你是一个天气查询助手，只回答天气相关的问题。"},
        {"role": "user", "content": "100加上50等于多少？"}
    ]
})
```

**格式化输出消息：**

```python
for msg in resp["messages"]:
    msg.pretty_print()
```

> `pretty_print()` 是 LangChain 消息对象自带的方法，用于美化打印消息内容和元数据。

## 3.3 提示词（Prompt）

在 LangChain 中，提示词为 Agent 提供了任务背景、行为准则和操作指南。通过 `system_prompt` 参数设置，它本质上定义了 Agent 的"角色"和"使命"。

### 3.3.1 基础提示词设置

在 `create_agent` 时传入 `system_prompt` 参数，可以是 `str` 或 `SystemMessage` 类型：

```python
from langchain_core.messages import SystemMessage

agent = create_agent(
    model=deepseek_llm,
    tools=[add_numbers],
    # 方式一：字符串
    # system_prompt="你是一个数学助手，可以实现两数相加。"
    # 方式二：SystemMessage 对象
    system_prompt=SystemMessage(content="你是一个数学助手，可以实现两数相加。")
)
```

### 3.3.2 动态提示词设置

对于需要根据运行时上下文调整提示词的高级场景，可以使用**中间件（Middleware）**实现动态提示词。通过 `@dynamic_prompt` 装饰器创建中间件，根据上下文生成不同的系统提示。

**核心思路：**

1. 定义运行时上下文的数据结构（`TypedDict`）
2. 使用 `@dynamic_prompt` 装饰器定义中间件函数
3. 在 `create_agent` 时挂载中间件
4. 在 `agent.invoke` 时传入 `context` 数据

```python
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from typing import TypedDict

# 定义上下文结构
class AgentContext(TypedDict):
    query_type: str  # 'normal' 或 'vip'

# 动态提示词中间件
@dynamic_prompt
def dynamic_support_prompt(request: ModelRequest) -> str:
    query_type = request.runtime.context.get("query_type", "normal")

    if query_type == "vip":
        return "你是一名高级支持专员，请深度分析问题并提供专业方案..."
    else:
        return "你是一线客服助手，请快速响应并简洁友好地回答..."
```

**使用时传入 context：**

```python
agent = create_agent(
    model=deepseek_llm,
    tools=[query_order_info, search_faq],
    middleware=[dynamic_support_prompt],
    context_schema=AgentContext  # 关联上下文 schema
)

# 普通用户模式
result = agent.invoke(
    {"messages": [{"role": "user", "content": "物品坏了怎么办？"}]},
    context={"query_type": "normal"}
)

# VIP 用户模式
result = agent.invoke(
    {"messages": [{"role": "user", "content": "物品坏了怎么办？"}]},
    context={"query_type": "vip"}
)
```

> `context_schema` 参数的作用是声明运行时上下文有哪些数据字段，确保 `invoke` 时传入的 `context` 数据符合定义。

## 关键面试考点

1. 什么是 Agent？它与普通 LLM 调用的区别是什么？
2. ReAct 框架的工作原理是什么？请描述一个完整的循环过程。
3. `create_agent` 的返回类型是什么？它的内部实现基于什么？
4. 静态模型和动态模型的区别是什么？动态模型通过什么机制实现？
5. 基础提示词和动态提示词的区别？动态提示词适用于什么场景？

## 知识关联

- 上一篇：[[LC-03-模型结构化输出与工具调用]]
- 下一篇：[[LC-05-Agent工具与结构化输出]]
- 相关：[[10-AI Agent]] — AI Agent 的理论基础

---

*上一篇：[[LC-03-模型结构化输出与工具调用]] | 下一篇：[[LC-05-Agent工具与结构化输出]]*
