---
title: "LC-Demo手敲指南-Java与Python"
created: 2026-06-05
updated: 2026-06-07
tags:
  - 分类/langchain
  - 分类/ai
  - 类型/demo
status: in-progress
---

# LC-Demo 手敲指南：Java 与 Python

> 这份文档用于后续手敲练习。Python 版使用 LangChain；Java 版使用 LangChain4j。两者不是 API 逐行翻译，但核心概念可以对应起来。

## 0. 概念对照

| 学习点 | Python LangChain | Java LangChain4j |
|--------|------------------|------------------|
| 模型对象 | `init_chat_model` / `ChatModel` | `OpenAiChatModel` / `ChatModel` |
| 普通调用 | `llm.invoke(...)` | `model.chat(...)` |
| 消息调用 | `SystemMessage` / `HumanMessage` / `AIMessage` | `SystemMessage` / `UserMessage` / `AiMessage` |
| 流式输出 | `llm.stream(...)` | `OpenAiStreamingChatModel` / `TokenStream` |
| 批量/异步 | `batch` / `ainvoke` / `abatch` | `CompletableFuture` |
| 工具 | `@tool` | `@Tool` / `@P` |
| Agent | `create_agent(...)` | AI Service + tools，或更完整的 Agentic AI 组件 |
| 结构化输出 | Pydantic / `response_format` | Java `record` / POJO / JSON Schema |

## 1. 环境准备

### 1.1 Python

```bash
pip install -U langchain langchain-deepseek python-dotenv pydantic typing-extensions
```

建议使用环境变量保存 Key：

```bash
DEEPSEEK_API_KEY=你的key
```

### 1.2 Java

Java 版使用 LangChain4j 的 OpenAI 兼容模型接入 DeepSeek。

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-open-ai</artifactId>
    <version>1.15.1</version>
</dependency>
```

如果使用 Maven，建议同时打开 Java 编译参数 `-parameters`，这样模型能看到真实参数名；如果不打开，就更要写好 `@P` 参数描述。

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <source>17</source>
        <target>17</target>
        <compilerArgs>
            <arg>-parameters</arg>
        </compilerArgs>
    </configuration>
</plugin>
```

## 2. LC-02：模型初始化与调用

### 2.1 Python：invoke 基础调用

知识点：`invoke()` 是一次性返回完整结果，返回对象是 `AIMessage`，正文在 `.content`。

```python
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

resp = llm.invoke("用三句话解释 LangChain 是什么。")

print(type(resp))
print(resp.content)
```

### 2.2 Java：普通模型调用

知识点：Java 里最直接的调用是 `model.chat(...)`，可以类比 Python 的 `invoke()`。

```java
import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;

public class Demo01Invoke {

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        String answer = model.chat("用三句话解释 LangChain 是什么。");

        System.out.println(answer);
    }
}
```

### 2.3 Python：Messages 对话

知识点：Chat Model 的输入可以是一组带角色的消息，而不是孤立字符串。

```python
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

messages = [
    SystemMessage("你是一个 Java 面试教练，回答要简洁、有条理。"),
    HumanMessage("请用一句话解释什么是 RAG。"),
    AIMessage("RAG 是让大模型先检索外部资料，再基于资料生成答案的模式。"),
    HumanMessage("那它和普通 LLM 问答最大的区别是什么？"),
]

resp = llm.invoke(messages)
print(resp.content)
```

### 2.4 Java：Messages 对话

知识点：Java 版里用户消息叫 `UserMessage`。

```java
import dev.langchain4j.data.message.AiMessage;
import dev.langchain4j.data.message.SystemMessage;
import dev.langchain4j.data.message.UserMessage;
import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.chat.request.ChatRequest;
import dev.langchain4j.model.chat.response.ChatResponse;
import dev.langchain4j.model.openai.OpenAiChatModel;

public class Demo02Messages {

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        ChatRequest request = ChatRequest.builder()
                .messages(
                        SystemMessage.from("你是一个 Java 面试教练，回答要简洁、有条理。"),
                        UserMessage.from("请用一句话解释什么是 RAG。"),
                        AiMessage.from("RAG 是让大模型先检索外部资料，再基于资料生成答案的模式。"),
                        UserMessage.from("那它和普通 LLM 问答最大的区别是什么？")
                )
                .build();

        ChatResponse response = model.chat(request);
        System.out.println(response.aiMessage().text());
    }
}
```

### 2.5 Python：stream 流式输出

知识点：`stream()` 适合聊天页面和长文本生成。

```python
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

for chunk in llm.stream("用 100 字解释 Agent 和普通 LLM 调用的区别。"):
    print(chunk.content, end="", flush=True)

print()
```

### 2.6 Java：stream 流式输出

知识点：LangChain4j 常用 `StreamingChatModel` + `TokenStream` 做流式输出。

```java
import dev.langchain4j.model.chat.StreamingChatModel;
import dev.langchain4j.model.chat.response.ChatResponse;
import dev.langchain4j.model.openai.OpenAiStreamingChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.TokenStream;

import java.util.concurrent.CompletableFuture;

public class Demo03Stream {

    interface Assistant {
        TokenStream chat(String message);
    }

    public static void main(String[] args) {
        StreamingChatModel model = OpenAiStreamingChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        Assistant assistant = AiServices.create(Assistant.class, model);
        CompletableFuture<ChatResponse> future = new CompletableFuture<>();

        assistant.chat("用 100 字解释 Agent 和普通 LLM 调用的区别。")
                .onPartialResponse(System.out::print)
                .onCompleteResponse(future::complete)
                .onError(future::completeExceptionally)
                .start();

        future.join();
        System.out.println();
    }
}
```

### 2.7 Python：batch 批量调用

知识点：`batch()` 适合多个互不依赖的问题。

```python
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

questions = [
    "用一句话解释 invoke。",
    "用一句话解释 stream。",
    "用一句话解释 batch。",
]

responses = llm.batch(questions)

for resp in responses:
    print(resp.content)
    print("---")
```

### 2.8 Java：CompletableFuture 批量/异步

知识点：Java 里可以用 `CompletableFuture` 表达并发调用。

```java
import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;

import java.util.List;
import java.util.concurrent.CompletableFuture;

public class Demo04BatchAsync {

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        List<String> questions = List.of(
                "用一句话解释 invoke。",
                "用一句话解释 stream。",
                "用一句话解释 batch。"
        );

        List<CompletableFuture<String>> futures = questions.stream()
                .map(question -> CompletableFuture.supplyAsync(() -> model.chat(question)))
                .toList();

        futures.forEach(future -> System.out.println(future.join() + "\n---"));
    }
}
```

## 3. LC-03：结构化输出与工具调用

### 3.1 Python：Pydantic 结构化输出

知识点：Pydantic 返回对象，适合 Python 业务代码直接读取字段。

```python
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(description="电影标题")
    year: int = Field(description="上映年份")
    director: str = Field(description="导演")
    rating: float = Field(description="10分制评分")


llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

structured_llm = llm.with_structured_output(Movie)
resp = structured_llm.invoke("请介绍电影《星际穿越》。")

print(type(resp))
print(resp.title)
print(resp.year)
print(resp.director)
print(resp.rating)
```

### 3.2 Java：record 结构化输出

知识点：Java 里可以让 AI Service 方法直接返回 `record` 或 POJO。

```java
import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.UserMessage;

public class Demo05StructuredMovie {

    record Movie(String title, int year, String director, double rating) {
    }

    interface MovieExtractor {
        @UserMessage("请介绍电影《{{it}}》，并提取电影标题、上映年份、导演和10分制评分。")
        Movie extract(String movieName);
    }

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        MovieExtractor extractor = AiServices.create(MovieExtractor.class, model);
        Movie movie = extractor.extract("星际穿越");

        System.out.println(movie);
        System.out.println(movie.title());
    }
}
```

### 3.3 Python：bind_tools 只产生 tool_calls

知识点：`bind_tools` 只让模型知道工具，不会主动执行工具。

```python
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气。"""
    return f"{city}今天晴，气温 25 度，适合外出。"


llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

llm_with_tools = llm.bind_tools([get_weather])
resp = llm_with_tools.invoke("北京今天天气怎么样？")

print("content:", resp.content)
print("tool_calls:", resp.tool_calls)
```

### 3.4 Python：手动执行工具并回传模型

知识点：这是 Agent 自动循环的底层过程。

```python
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气。"""
    return f"{city}今天晴，气温 25 度，适合外出。"


llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

tools = [get_weather]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)

messages = [HumanMessage("北京今天天气怎么样？")]
ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    selected_tool = tools_by_name[tool_call["name"]]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)

final_resp = llm_with_tools.invoke(messages)
print(final_resp.content)
```

### 3.5 Java：低层工具调用心智

知识点：LangChain4j 官方也区分低层工具 API 和高层 AI Service。低层工具调用时，模型返回的是工具执行请求，开发者要执行工具并把结果回传。

实际手敲时可以先跳到下一节的 AI Service 版本；它会自动执行 `@Tool` 方法，更接近 Python 的 Agent 体验。

## 4. LC-04：Agent 基础

### 4.1 Python：create_agent 自动工具循环

知识点：`create_agent` 会自动执行工具、追加 `ToolMessage`，再让模型继续回答。

```python
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气。"""
    return f"{city}今天晴，气温 25 度，适合外出。"


llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="你是一个天气助手。用户问天气时，你应该调用工具获取天气信息。",
)

resp = agent.invoke({
    "messages": [
        {"role": "user", "content": "北京今天天气怎么样？"}
    ]
})

for msg in resp["messages"]:
    msg.pretty_print()
```

### 4.2 Java：AI Service + @Tool 自动执行工具

知识点：LangChain4j 的 AI Service 会把 `@Tool` 方法转换成工具，并在模型请求调用时自动执行。

```java
import dev.langchain4j.agent.tool.P;
import dev.langchain4j.agent.tool.Tool;
import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;
import dev.langchain4j.service.AiServices;

public class Demo06ToolsAgent {

    interface Assistant {
        String chat(String message);
    }

    static class Tools {

        @Tool("查询指定城市的天气")
        String getWeather(@P("城市名称") String city) {
            return city + "今天晴，气温 25 度，适合外出。";
        }

        @Tool("计算两个整数的和")
        int addNumbers(@P("第一个整数") int a, @P("第二个整数") int b) {
            return a + b;
        }
    }

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        Assistant assistant = AiServices.builder(Assistant.class)
                .chatModel(model)
                .tools(new Tools())
                .systemMessageProvider(id -> "你是一个助手。需要查天气时调用天气工具，需要计算时调用计算工具。")
                .build();

        String answer = assistant.chat("北京天气怎么样？顺便算一下 120 加 35。");
        System.out.println(answer);
    }
}
```

## 5. LC-05：Agent 工具与结构化输出

### 5.1 Python：Pydantic args_schema 复杂工具

知识点：复杂工具用 `args_schema` 约束参数，模型更容易生成正确参数。

```python
from typing import Optional, Literal

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from pydantic import BaseModel, Field


class WorkOrderQuery(BaseModel):
    order_id: Optional[str] = Field(None, description="工单编号，例如 TK2024001")
    status: Optional[Literal["待处理", "处理中", "已完成"]] = Field(
        None,
        description="工单状态，只能是 待处理、处理中、已完成",
    )
    assignee: Optional[str] = Field(None, description="工单处理人姓名")


@tool(args_schema=WorkOrderQuery)
def query_work_order(
    order_id: Optional[str] = None,
    status: Optional[str] = None,
    assignee: Optional[str] = None,
) -> str:
    """根据工单编号、状态或处理人查询工单信息。"""
    return (
        "查询到工单："
        f"order_id={order_id or '未指定'}, "
        f"status={status or '未指定'}, "
        f"assignee={assignee or '未指定'}"
    )


llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

agent = create_agent(
    model=llm,
    tools=[query_work_order],
    system_prompt="你是一个工单查询助手。用户查询工单时，必须调用工单查询工具。",
)

resp = agent.invoke({
    "messages": [
        {"role": "user", "content": "帮我查一下张三处理中状态的工单。"}
    ]
})

for msg in resp["messages"]:
    msg.pretty_print()
```

### 5.2 Java：复杂工具参数

知识点：Java 里可以用清晰的参数名、`@P` 描述和 `Optional` 表达可选入参。

```java
import dev.langchain4j.agent.tool.P;
import dev.langchain4j.agent.tool.Tool;
import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;
import dev.langchain4j.service.AiServices;

import java.util.Optional;

public class Demo07WorkOrderTool {

    interface WorkOrderAssistant {
        String chat(String message);
    }

    static class WorkOrderTools {

        @Tool("根据工单编号、状态或处理人查询工单信息")
        String queryWorkOrder(
                @P("工单编号，例如 TK2024001") Optional<String> orderId,
                @P("工单状态，只能是 待处理、处理中、已完成") Optional<String> status,
                @P("工单处理人姓名") Optional<String> assignee
        ) {
            return "查询到工单：orderId=%s, status=%s, assignee=%s".formatted(
                    orderId.orElse("未指定"),
                    status.orElse("未指定"),
                    assignee.orElse("未指定")
            );
        }
    }

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        WorkOrderAssistant assistant = AiServices.builder(WorkOrderAssistant.class)
                .chatModel(model)
                .tools(new WorkOrderTools())
                .systemMessageProvider(id -> "你是一个工单查询助手。用户查询工单时，必须调用工单查询工具。")
                .build();

        String answer = assistant.chat("帮我查一下张三处理中状态的工单。");
        System.out.println(answer);
    }
}
```

### 5.3 Python：Agent 结构化输出

知识点：`response_format` 让 Agent 最终返回业务对象，结果在 `structured_response` 中。

```python
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field


class InterviewFeedback(BaseModel):
    score: int = Field(description="面试回答评分，0到100")
    strengths: list[str] = Field(description="回答中的优点")
    weaknesses: list[str] = Field(description="回答中的不足")
    suggestion: str = Field(description="下一步改进建议")


llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key="你的 DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com",
)

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="你是一个 Java 面试教练。请客观评价候选人的回答。",
    response_format=ToolStrategy(InterviewFeedback),
)

resp = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": (
                "题目：HashMap 为什么线程不安全？\n"
                "我的回答：因为多线程同时 put 的时候可能会覆盖数据，"
                "扩容时也可能产生数据异常，所以并发场景应该用 ConcurrentHashMap。"
            ),
        }
    ]
})

feedback = resp["structured_response"]

print("评分:", feedback.score)
print("优点:", feedback.strengths)
print("不足:", feedback.weaknesses)
print("建议:", feedback.suggestion)
```

### 5.4 Java：AI Service 返回结构化对象

知识点：Java 里让接口方法返回 `record`，LangChain4j 会尝试把模型输出映射成 Java 对象。

```java
import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.SystemMessage;
import dev.langchain4j.service.UserMessage;

import java.util.List;

public class Demo08InterviewFeedback {

    record InterviewFeedback(
            int score,
            List<String> strengths,
            List<String> weaknesses,
            String suggestion
    ) {
    }

    interface InterviewCoach {

        @SystemMessage("你是一个 Java 面试教练。请客观评价候选人的回答，并返回结构化结果。")
        @UserMessage("""
                题目：{{question}}
                候选人回答：{{answer}}
                """)
        InterviewFeedback evaluate(String question, String answer);
    }

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com/v1")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        InterviewCoach coach = AiServices.create(InterviewCoach.class, model);

        InterviewFeedback feedback = coach.evaluate(
                "HashMap 为什么线程不安全？",
                "因为多线程同时 put 可能覆盖数据，扩容时也可能产生异常，并发场景应该用 ConcurrentHashMap。"
        );

        System.out.println("评分：" + feedback.score());
        System.out.println("优点：" + feedback.strengths());
        System.out.println("不足：" + feedback.weaknesses());
        System.out.println("建议：" + feedback.suggestion());
    }
}
```

## 6. 手敲顺序建议

先按这个顺序来，不要一口气全敲：

1. Python `invoke`
2. Java `model.chat`
3. Python Messages
4. Java Messages
5. Python `create_agent`
6. Java AI Service + `@Tool`
7. Python Pydantic 结构化输出
8. Java record 结构化输出
9. Python Pydantic `args_schema`
10. Java 复杂工具参数

## 7. 易错点

- 不要把 API Key 写进笔记或提交到 Git，尽量用环境变量。
- Python 的 `bind_tools` 不会自动执行工具，`create_agent` 才会自动管理循环。
- Java 的 `@Tool` 方法说明和 `@P` 参数说明非常重要，它们相当于给模型看的接口文档。
- 结构化输出不是 100% 不会失败，模型能力、Provider 支持和提示词都会影响稳定性。
- 多个问题只有互不依赖时才适合 batch；有前后依赖时要用 Agent、Chain 或 Graph。

## 8. 参考文档

- Python LangChain：[[LC-02-模型调用与Chat Models]]、[[LC-03-模型结构化输出与工具调用]]、[[LC-04-Agent智能体基础]]、[[LC-05-Agent工具与结构化输出]]
- LangChain4j OpenAI 集成：https://docs.langchain4j.dev/integrations/language-models/open-ai/
- LangChain4j Tools：https://docs.langchain4j.dev/tutorials/tools/
- LangChain4j Structured Outputs：https://docs.langchain4j.dev/tutorials/structured-outputs/

## 知识关联

- 导航入口：[[MOC-LangChain学习]]
- 配套章节：[[LC-02-模型调用与Chat Models]]、[[LC-03-模型结构化输出与工具调用]]、[[LC-04-Agent智能体基础]]、[[LC-05-Agent工具与结构化输出]]
