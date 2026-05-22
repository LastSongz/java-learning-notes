---
title: "LC-01-LangChain概述与核心架构"
created: 2026-05-21
updated: 2026-05-21
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/入门
status: in-progress
prev: "[[MOC-LangChain学习]]"
next: "[[LC-02-模型调用与Chat Models]]"
---

# LC-01 LangChain 概述与核心架构

> LangChain 是一个用于开发由大语言模型（LLM）驱动的应用程序的开源框架，它并非仅是对模型 API 的简单封装，而是提供了预构建的智能体（Agent）架构和丰富的工具集成，使开发者无需从零搭建复杂的集成架构，就能快速构建基于 LLM 的高级应用。

## 1.1 LangChain 的由来

LangChain 这一开源框架诞生于 **2022 年 10 月**，由哈佛大学的 **Harrison Chase**（哈里森·蔡斯）创建。其名称来源于 "Language"（语言模型）和 "Chain"（链式连接）的组合，体现了核心设计理念——将大语言模型与其他计算资源和数据源以链式方式连接，构建出功能更加强大的 AI 应用。

### 为什么需要 LangChain

LangChain 的诞生源于一个关键洞察：单一的大语言模型虽然能力强大，但在实际应用场景中存在明显局限。

LLM 的固有局限：
- **知识受限于训练数据**：无法获取训练时点之后的信息
- **无法与外部系统交互**：不能直接操作数据库、调用 API
- **不具备状态保持能力**：难以进行连贯的多轮对话

所以要构建真正实用的 AI 应用，必须将大语言模型与外部工具、数据源和记忆机制有机结合，这就是 LangChain 的设计初衷。

### 框架演进

2024 年是 LangChain 架构重大变革的一年。随着开发者从构建原型转向生产环境部署，对更精细工作流控制的需求日益增长。LangChain 团队推出了 **LangGraph** 作为底层智能体编排框架，并将原有的链和智能体标记为弃用，转而采用基于 LangGraph 构建的统一智能体抽象。

**2025 年 10 月 20 日**，LangChain 团队正式发布 **LangChain v1.0.0** 与 **LangGraph v1.0.0**，标志着框架的成熟和标准化，为企业级 AI 应用提供了稳定基础。

### 文档资源

| 资源 | 地址 |
|------|------|
| 英文文档 | https://docs.langchain.com/oss/python/langchain/overview |
| 中文文档 | https://docs.langchain.org.cn/oss/python/langchain/overview |

## 1.2 LangChain 核心特点

LangChain 作为一个成熟的大模型应用开发框架，具备如下核心特点：

### 1) 统一的模型接口

LangChain 通过统一的 API 抽象层，解决了不同模型提供商接口各异的问题。各大模型提供商（如 OpenAI、Anthropic、Google 等）都有独特的 API 接口、参数规范和响应格式。LangChain 通过标准化模型交互接口，使开发者可以**无缝切换不同模型而无需重写大量代码**。

这一特性不仅降低了技术锁定风险，还使得开发者能够轻松利用最新最先进的模型，加速实验和创新周期。

### 2) 模块化架构

LangChain 采用高度模块化架构，将复杂的大模型应用分解为可复用的构建块。核心组件包括模型（Models）、提示模板（Prompts）、记忆（Memory）、链（Chains）、智能体（Agents）和工具（Tools）等。这种设计使开发者可以**像搭积木一样组合各种功能**，快速构建符合特定需求的 AI 应用。

组件的可组合性体现在 **LangChain 表达式语言（LCEL）** 中，它允许开发者通过管道操作符（`|`）将多个组件连接成复杂的工作流。例如，一个简单的检索增强生成流程可以通过组合检索器、提示模板和 LLM 来实现。这种声明式的工作流定义方式不仅代码简洁，而且天然支持**流式输出、异步调用和并行执行**等高级特性，显著提升了开发效率和运行时性能。

### 3) 智能体与工具调用

智能体是 LangChain 最强大的特性之一，它将大语言模型从被动的文本生成器转变为能够主动决策和执行任务的智能系统。智能体的核心思想是使用 LLM 作为"大脑"，通过**观察-思考-行动的循环**来动态决定如何解决用户问题。

LangChain 智能体支持丰富的外部工具集成，包括搜索引擎、数据库、API 接口等。工具是标准的函数接口，包含**名称、描述和执行函数**三个基本要素。智能体通过分析用户查询，自动选择适当的工具，执行后根据结果决定下一步行动，直至问题解决。这种机制极大地扩展了大模型的能力边界，使其能够处理需要实时数据或具体操作的任务。

### 4) 记忆管理机制

LangChain 的记忆系统使大模型应用能够保持对话状态和历史上下文，实现了真正有意义的多轮交互。记忆机制解决了纯 LLM 应用的无状态性问题，通过维护短期和长期记忆，使 AI 应用能够参考之前的对话内容，提供更加连贯和个性化的体验。

记忆系统的**分层架构**支持不同存储后端（内存、文件、数据库）和检索策略。开发者可以根据应用需求选择适当的记忆类型，如客服系统可能需要长期记忆用户偏好，而数据查询应用可能只需短期记忆当前会话上下文。这种灵活的记忆管理是构建高质量对话应用的关键。

## 1.3 LangChain 使用场景

### 1) 检索增强生成（RAG）

检索增强生成是 LangChain 最经典的应用场景，解决了大模型**知识滞后和幻觉**问题。RAG 系统通过将外部知识源（文档、数据库等）向量化存储，在生成答案前先检索相关信息，使模型能够基于最新、最相关的数据生成回答。

### 2) Agent 智能体构建

智能体应用将大语言模型作为推理引擎，使其能够自主规划并执行复杂任务。智能体通过分析用户目标，动态选择和执行适当的工具，逐步推进任务完成。

典型应用：
- **智能旅行规划**：依次调用航班查询、酒店预订、景点推荐等工具，生成完整行程
- **市场调研**：自动搜索行业报告、分析数据并生成简报
- **数据分析**：连接数据库，根据自然语言查询生成 SQL 并执行分析

### 3) 对话系统与聊天机器人

LangChain 为构建上下文感知的对话系统提供了完整支持。通过记忆管理系统，对话应用能够保持多轮对话的连贯性，记住用户偏好和历史交互。

对话系统可以集成外部工具和知识源，提供超越通用聊天机器人的专业服务：
- **电商客服机器人**：连接订单数据库，提供个性化推荐和售后支持
- **教育助手**：结合教材内容，解答学生的学习问题

### 4) 数据连接与处理

LangChain 强大的数据连接能力使大模型能够与各种数据源和结构化数据交互，包括从非结构化文档中提取信息、查询数据库、分析数据等任务。

典型应用：
- 从 PDF 合同中自动提取关键信息（各方、金额、条款）
- 将自然语言转换为 SQL 查询数据库
- 基于 Excel 数据生成趋势分析和报告

### 5) 内容生成与自动化写作

LangChain 优化了结构化内容生成流程，通过提示模板和输出解析器确保生成内容符合特定格式和质量要求。

典型应用：
- **周报生成工具**：从业务系统提取数据，按固定格式生成报告
- **法律文书生成**：基于模板和用户输入，产出符合规范的法律文件

### 6) 多模态应用开发

随着多模态模型的发展，LangChain 也扩展了对多种媒体类型的支持。多模态应用可以处理图像、音频、视频等非文本数据，结合语言模型的推理能力，实现更丰富的交互体验。

典型应用：
- **图像分析系统**：用户上传图片，调用图像识别 API 生成描述，再让 LLM 基于描述回答问题
- **语音交互系统**：将用户语音转换为文本，处理后再将答案转换为语音输出

## 1.4 LangChain 快速上手

### 1.4.1 Python 环境准备

LangChain 1.2 版本要求 Python 版本为 **3.10+** 以上，本课程使用 Python **3.13.11** 版本，使用 Anaconda 管理环境：

```bash
# 创建名为 langchain_v1.2 的环境，指定 Python 版本
conda create --name langchain_v1.2 python=3.13.11

# 查看已安装的 python 环境
conda env list

# 切换到某 python 环境
conda activate langchain_v1.2

# 退出当前 python 环境
conda deactivate

# 删除已有的 python 环境
conda remove --name langchain_v1.2 --all
```

### 1.4.2 创建项目及配置
**在 IDEA 中创建 Langchainv12Project 项目并指定 python 环境为 `langchain_v1.2`：**

![[images/ch01-idea-project-setup.png]]

**1) 安装必要依赖**

```bash
# 切换 conda 环境
conda activate langchain_v1.2

# 安装依赖（使用清华镜像源加速）
python -m pip install langchain==1.2.0 langchain-deepseek==1.0.1 dotenv==0.9.9 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

> 说明：`langchain-deepseek` 是使用 DeepSeek 大模型的必要依赖；`dotenv` 是从项目根目录 `.env` 文件中加载自定义环境变量的必要依赖。

**2) 创建 `.env` 文件**

在项目根目录下创建 `.env` 文件，配置大模型的 API_KEY 和 BASE_URL：

```env
DEEPSEEK_API_KEY=sk-xxxx
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

**3) 创建 `env_utils.py` 文件**

通过 dotenv 加载并获取 `.env` 文件中配置的环境变量：

```python
import os
from dotenv import load_dotenv

# override=True 确保 .env 文件优先
load_dotenv(override=True)

# 从环境变量读取配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
```

**4) 创建 `my_llm.py` 文件**

集中管理各种大模型的创建，方便在项目中复用：

```python
from langchain_deepseek import ChatDeepSeek
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

# 创建 DeepSeek LLM
deepseek_llm = ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,
    model="deepseek-chat",
)
```

### 1.4.3 快速上手案例 — Agent 查询天气

使用 LangChain 创建 Agent，该 Agent 可以调用查询天气工具进行天气查询（天气查询工具通过代码模拟生成）：

```python
from langchain.agents import create_agent
from my_llm import deepseek_llm


def get_weather(city: str) -> str:
    """获取给定城市的天气。"""
    # 模拟天气查询
    return f"{city} 天气晴朗！"


# 创建 Agent
agent = create_agent(
    model=deepseek_llm,
    tools=[get_weather],
    system_prompt="你是一个助手，你可以查询城市的天气。",
)

# 调用 Agent
resp = agent.invoke(
    {"messages": [{"role": "user", "content": "查询北京的天气"}]}
)

print(resp)
```

**运行结果解析：**

Agent 的执行过程是一个**多步交互循环**：

1. `HumanMessage` — 用户发送请求："查询北京的天气"
2. `AIMessage`（含 tool_calls） — LLM 决定调用 `get_weather` 工具，参数为 `{"city": "北京"}`
3. `ToolMessage` — 工具执行返回结果："北京 天气晴朗！"
4. `AIMessage`（最终回复） — LLM 根据工具结果生成自然语言回答："根据查询结果，北京今天的天气是晴朗的！"

这个案例展示了 LangChain Agent 的核心工作模式：**LLM 作为大脑，自主决策调用工具，最终生成人类可读的回答**。

## 核心架构概览

```
LangChain 架构层次
├── Model I/O（模型输入输出）
│   ├── Prompts - 提示词模板管理与优化
│   ├── LLMs / Chat Models - 模型调用接口
│   └── Output Parsers - 输出结果解析
├── Retrieval（检索）
│   ├── Document Loaders - 文档加载器
│   ├── Text Splitters - 文本分割器
│   ├── Vector Stores - 向量数据库
│   └── Retrievers - 检索器
├── Chains（链）
│   ├── LCEL（LangChain Expression Language）
│   └── 通用链与专用链
├── Agents（智能代理）
│   ├── Tools - 工具定义
│   ├── Agent Types - 代理类型
│   └── Executor - 执行器
├── Memory（记忆）
│   ├── 短期记忆
│   └── 长期记忆
└── Callbacks（回调）
    └── 日志、监控与可观测性
```

## 生态工具

| 工具 | 用途 |
|------|------|
| LangChain | 核心框架 |
| LangGraph | 状态图工作流编排（v1.0 后为底层智能体编排框架） |
| LangSmith | 调试、测试与监控平台 |
| LangServe | 将 Chain 部署为 REST API |

## 与相关概念的关系

- LangChain 是 [[09-RAG检索增强生成|RAG]] 的主流实现框架之一
- LangChain Agent 是 [[10-AI Agent|AI Agent]] 概念的工程化落地
- LangChain 的 Chain 概念与 [[15-AI工作流|AI工作流]] 编排思想一致
- 在 [[18-RAG落地实战]] 和 [[19-微组件与工具调用设计]] 中有实际应用

## 关键面试考点

1. LangChain 解决了什么问题？为什么要用它而不是直接调 API？
2. LangChain 的核心特点有哪些？分别解决什么痛点？
3. LangChain 的名称由来？其核心设计理念是什么？
4. LCEL 是什么？管道操作符 `|` 的作用是什么？
5. LangChain v1.0 和 LangGraph v1.0 的发布意味着什么？
6. Agent 的工作模式是什么？工具的三个基本要素是什么？

## 学习资源

- [LangChain 英文文档](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain 中文文档](https://docs.langchain.org.cn/oss/python/langchain/overview)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)

---

*上一篇：[[MOC-LangChain学习]] | 下一篇：[[LC-02-模型调用与Chat Models]]*
