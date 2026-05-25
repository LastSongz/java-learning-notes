---
title: "LC-02-模型初始化与调用"
created: 2026-05-21
updated: 2026-05-21
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/入门
status: in-progress
prev: "[[LC-01-LangChain概述与核心架构]]"
next: "[[LC-03-模型结构化输出与工具调用]]"
---

# LC-02 Models 模型 — 初始化与调用

> LangChain 支持所有主流模型提供商，包括 OpenAI、Anthropic、Google、Azure、AWS Bedrock 等

LangChain 中使用模型可以单独使用或者在 Agent 中使用，无论哪种方式都要进行模型初始化。本节重点讲解单独使用模型的初始化与调用方式。

支持的模型完整列表：https://docs.langchain.com/oss/python/integrations/providers/all_providers

## 2.1 模型初始化

LangChain 中初始化模型主要有两种方式：**Model Class 直接初始化**和 **`init_chat_model` 统一初始化**。

### 2.1.1 Model Class 方式初始化模型

最直接的方式，根据模型提供商导入对应的类并实例化。

**1) 安装必要依赖**

```bash
conda activate langchain_v1.2

pip install langchain-openai==1.1.6
pip install langchain-anthropic==1.3.1
pip install langchain-deepseek==1.0.1
pip install langchain-ollama==1.0.1
pip install langchain-community==0.4.1  # ChatHunyuan、ChatTongyi、ChatZhipuAI
pip install tencentcloud-sdk-python==3.1.28  # ChatHunyuan
pip install dashscope==1.25.6  # ChatTongyi
pip install pyjwt==2.10.1  # ChatZhipuAI
```

**2) 在 `.env` 中配置 API_KEY 和 BASE_URL**

```env
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_BASE_URL=https://api.deepseek.com
OPENAI_API_KEY=sk-...
OPENAI_BASE_URL=https://api.openai.com/v1
ANTHROPIC_API_KEY=sk-...
ANTHROPIC_BASE_URL=https://api.anthropic.com
```

**3) 在 `my_llm.py` 中创建各模型对象**

```python
from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatHunyuan, ChatTongyi, ChatZhipuAI
from langchain_deepseek import ChatDeepSeek
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from env_utils import (DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL,
                       OPENAI_API_KEY, OPENAI_BASE_URL,
                       ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL)

# DeepSeek
deepseek_llm = ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,  # 注意：这里是 api_base，不是 base_url
    model="deepseek-chat",
)

# OpenAI
openai_llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    model="gpt-4",
)

# Anthropic
anthropic_llm = ChatAnthropic(
    api_key=ANTHROPIC_API_KEY,
    base_url=ANTHROPIC_BASE_URL,
    model="claude-3-5-haiku-latest",
)

# Ollama（本地模型）
ollama_llm = ChatOllama(
    base_url="http://192.168.1.106:11434",
    model="deepseek-r1:1.5b",
)
```

> 注意：使用不同的模型传入的参数名称可能不同，可以参考对应的源码。

**ChatOpenAI 的扩展使用**：如果模型供应商兼容 OpenAI 标准接口，即使 LangChain 没有对应的专用类，也可以直接用 `ChatOpenAI` 连接：

```python
# 通过 ChatOpenAI 连接 DeepSeek
deepseek_llm2 = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    model="deepseek-chat",
)

# 通过 ChatOpenAI 连接通义千问
tongyi_llm2 = ChatOpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL,
    model="qwen-plus",
)
```

**各模型 LangChain 使用文档：**

| 模型供应商 | 文档链接 |
|-----------|---------|
| OpenAI | https://docs.langchain.com/oss/python/integrations/chat/openai |
| Anthropic | https://docs.langchain.com/oss/python/integrations/chat/anthropic |
| DeepSeek | https://docs.langchain.com/oss/python/integrations/chat/deepseek |
| Ollama | https://docs.langchain.com/oss/python/integrations/chat/ollama |
| 腾讯混元 | https://docs.langchain.com/oss/python/integrations/chat/tencent_hunyuan |
| 通义千问 | https://docs.langchain.com/oss/python/integrations/chat/tongyi |
| 智谱AI | https://docs.langchain.com/oss/python/integrations/chat/zhipuai |

### 2.1.2 init_chat_model 初始化模型【推荐】

`init_chat_model` 是 LangChain v1.0 后推出的统一初始化方法，像一个**智能工厂**，传入 `model`（模型）、`model_provider`（模型提供商）、`api_key`、`base_url` 参数即可自动创建对应的模型实例。初始化后，调用方式与 Model Class 完全一致。

`model_provider` 常见参数：`openai`、`anthropic`、`deepseek`、`ollama`。如果模型供应商没有对应的 provider 但支持标准 OpenAI 访问，可以设置 `model_provider="openai"`。

新版文档也支持把供应商写进 `model` 字符串中，例如 `init_chat_model("deepseek:deepseek-chat")`、`init_chat_model("openai:gpt-4o")`。如果供应商是固定的，使用 `provider:model` 形式更直观；如果供应商和模型名需要从配置动态读取，继续使用 `model` + `model_provider` 两个参数更方便。

```python
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

# DeepSeek
deepseek_llm: BaseChatModel = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

# OpenAI
openai_llm = init_chat_model(
    model="gpt-4",
    model_provider="openai",
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
)

# 通义千问（通过 OpenAI 兼容接口）
tongyi_llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL,
)
```

**推荐使用 `init_chat_model` 的原因：**
- 参数格式统一，不同模型提供商使用同一套参数
- 通过 `model_provider` 自动选择对应的模型类
- 切换模型只需修改参数，代码改动最小

### 2.1.3 模型初始化参数解释

Model Class 和 `init_chat_model` 共同的参数：

| 参数 | 类型 | 描述 |
|------|------|------|
| `model` | string | 指定要使用的模型标识符 |
| `api_key` | string | 用于身份验证的 API 密钥，建议通过环境变量设置 |
| `base_url` | string | 指定 API 端点 |
| `temperature` | number | 控制输出随机性，越低越确定保守，越高越多样有创意 |
| `max_tokens` | number | 限制模型响应的最大令牌数 |
| `timeout` | number | 等待模型响应的最大时间（秒） |
| `max_retries` | number | 请求失败时的最大重试次数 |

> `model_provider` 是 `init_chat_model` 中指定模型供应商的参数，Model Class 初始化不需要。

**关于 Token 的常识：**

Token 并非简单的"字"或"词"，而是大模型通过分词器将输入文本拆分后的最小语义单元。不同模型采用不同的分词算法，同一段文本在不同模型中的 Token 数量可能不同。

- 英文 Token 估算：1 个 Token 约对应 0.75 个英文单词或 4 个字符
- 中文 Token 估算：1 个汉字通常对应 1~2 个 Token

## 2.2 模型调用

LangChain 提供了几种核心的调用方式：`invoke()`、`stream()`、`batch()` 及其异步版本。

| 核心方法 | 主要特点 | 适用场景 |
|----------|----------|----------|
| `invoke()` | 阻塞式，一次性返回完整结果 | 简单问答、无需实时反馈的场景 |
| `ainvoke()` | 非阻塞，提高系统吞吐量 | 高并发 Web 应用、IO 密集型任务 |
| `stream()` | 流式输出，实时返回每个 token | 聊天机器人、长文本生成 |
| `astream()` | 非阻塞流式输出 | 高并发 Web 应用 |
| `batch()` | 批量处理多个输入 | 需要同时处理大量请求的场景 |
| `abatch()` | 非阻塞批量处理 | 高并发 Web 应用 |

### 2.2.1 Invoke 调用模型

`invoke()` 是最直接、最常用的调用方法，阻塞式工作——等待模型完全生成响应后一次性返回。支持三种输入形式：

**1) 单条消息**

最简单的方式，直接传入问题或指令：

```python
resp = deepseek_llm.invoke("请介绍一下你自己")
print(resp.content)
```

**2) 消息列表（字典格式）**

通过 `role` 字段指定角色（system、user、assistant）：

```python
conversation = [
    {"role": "system", "content": "你是一个有帮助的助手，可以将汉语翻译成英语。"},
    {"role": "user", "content": "翻译: 我喜欢编程"},
    {"role": "assistant", "content": "I love programming."},
    {"role": "user", "content": "翻译: 我喜欢大模型"}
]
resp = deepseek_llm.invoke(conversation)
print(resp.content)  # 输出: I like large models.
```

**3) 消息列表（消息对象格式）【推荐】**

使用 LangChain 内置的消息类，类型更安全，功能更丰富：

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

conversation = [
    SystemMessage("你是一个有帮助的助手，可以将汉语翻译成英语。"),
    HumanMessage("翻译: 我喜欢编程"),
    AIMessage("I love programming."),
    HumanMessage("翻译: 我喜欢大模型")
]
resp = deepseek_llm.invoke(conversation)
print(resp.content)  # 输出: I like large models.
```

**四种消息类型：**

| 消息类型 | 说明 |
|----------|------|
| `SystemMessage` | 为模型设定角色、行为准则和上下文背景，像给 AI 的工作说明书 |
| `HumanMessage` | 代表用户输入，可包含文本或多模态内容（图片、音频等） |
| `AIMessage` | 代表模型的输出，包括生成文本、工具调用、元数据等 |
| `ToolMessage` | 将工具执行结果返回给模型，让模型基于结果继续生成回复 |

> `ChatModel.invoke()` 返回的是 `AIMessage` 对象，需要通过 `.content` 属性获取文本内容。

### 2.2.2 流式调用模型

`stream()` 返回一个迭代器，逐块（Chunk）实时输出结果：

```python
from typing import Iterator
from langchain_core.messages import AIMessageChunk

resp: Iterator[AIMessageChunk] = deepseek_llm.stream("使用20个字给我介绍什么是大模型？")
for chunk in resp:
    print(chunk.content, end="|", flush=True)
```

> `stream()` 立即返回迭代器，逐个产生 `AIMessageChunk` 对象。每个块包含输出内容的一部分，拼接后的最终效果与 `invoke()` 一致。

### 2.2.3 批量调用模型

将多个独立请求集合成一个批次并行发送，大幅减少网络往返开销和等待时间。

**batch() — 按顺序返回**

等待所有请求处理完毕，按原始输入顺序返回结果列表：

```python
from langchain_core.runnables.utils import Output

responses: list[Output] = deepseek_llm.batch([
    "为什么鹦鹉的羽毛是彩色的？",
    "飞机是如何飞行的？",
    "什么是量子计算？"
])
for response in responses:
    print(response.content)
```

**batch_as_completed() — 按完成顺序返回**

每个请求完成后立即 yield 结果，结果可能乱序，但包含索引信息：

```python
from typing import Iterator

responses = deepseek_llm.batch_as_completed([
    "为什么鹦鹉的羽毛是彩色的？",
    "飞机是如何飞行的？",
    "什么是量子计算？"
])
for response in responses:
    # response 是元组：(索引, 输出)
    print(f"第 {response[0]} 个问题回答完毕: {response[1].content}")
```

**控制并发数**：通过 `RunnableConfig` 的 `max_concurrency` 参数限制最大并行数：

```python
model.batch(
    large_list_of_inputs,
    config={"max_concurrency": 5}
)
```

### 2.2.4 异步调用模型

异步方法（`ainvoke`、`astream`、`abatch`）与同步版本相比的优势：
- **避免阻塞主线程**：异步方法让应用在等待 API 响应时保持响应性
- **优化资源利用**：减少空闲等待时间，更高效地利用系统资源

```python
import asyncio

async def demo_async_invoke():
    print("程序开始...")

    # 创建异步任务，让模型请求真正开始执行
    async_task = asyncio.create_task(
        llm.ainvoke("用一句话解释人工智能。")
    )

    # 同时执行其他任务
    for i in range(3):
        await asyncio.sleep(1)
        print(f">>> 正在执行第{i + 1}个任务...")

    # 需要结果时再 await
    response = await async_task
    print(f">>> 模型返回: {response.content}")

asyncio.run(demo_async_invoke())
```

> 注意：`llm.ainvoke(...)` 本身返回的是协程对象。只有 `await` 它，或用 `asyncio.create_task(...)` 把它调度成任务后，请求才会真正并发执行。

异步流式调用使用 `async for`：

```python
async def demo_async_stream():
    async for chunk in llm.astream("请解释机器学习的基本概念。"):
        if hasattr(chunk, 'content'):
            print(chunk.content, end="", flush=True)
```

异步批量调用：

```python
async def demo_async_batch():
    questions = ["用一句话说明深度学习与传统机器学习的区别"]
    responses = await llm.abatch(questions)
    for response in responses:
        print(response.content)
```

## 关键面试考点

1. `init_chat_model` 和 Model Class 有什么区别？为什么推荐前者？
2. LangChain 的四种消息类型是什么？各有什么作用？
3. `batch()` 和 `batch_as_completed()` 的区别是什么？
4. 同步调用和异步调用的区别？什么场景下应该使用异步？
5. Token 和字的关系是什么？

## 知识关联

- 上一篇：[[LC-01-LangChain概述与核心架构]]
- 下一篇：[[LC-03-模型结构化输出与工具调用]]
- 相关：[[08-API开发]] — API 调用的底层原理

---

*上一篇：[[LC-01-LangChain概述与核心架构]] | 下一篇：[[LC-03-模型结构化输出与工具调用]]*
