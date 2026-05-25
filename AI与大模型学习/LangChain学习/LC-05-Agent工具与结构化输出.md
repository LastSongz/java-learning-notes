---
title: "LC-05-Agent工具创建与结构化输出"
created: 2026-05-21
updated: 2026-05-21
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/核心
status: in-progress
prev: "[[LC-04-Agent智能体基础]]"
next: "[[LC-06-Agent异步调用与流式输出]]"
---

# LC-05 Agent 工具创建与结构化输出

> 工具（Tools）是 Agent 与外部世界交互的桥梁；结构化输出确保 Agent 返回符合预期的数据格式

## 3.4 Tools 工具

### 3.4.1 工具创建方式

LangChain 提供三种核心的工具创建方式：

#### 3.4.1.1 使用 @tool 装饰器定义工具【推荐】

最直接的方法，在函数上方添加装饰器即可：

```python
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息。"""
    return f"{city}的天气为晴朗，25°C。"
```

> 工具函数的 **docstring** 非常重要，它会被 Agent 用来理解工具的用途。参数类型注解也是必须的。

**工具定义注意事项：**
- `@tool` 默认使用函数名作为工具名，也可以用 `@tool("get_employee_info")` 显式指定名称。
- `description` 参数会覆盖函数 docstring，适合在工具描述需要更精确时使用。
- 参数名不要使用 `config` 或 `runtime`，这些属于 LangChain 内部保留字段。
- 工具描述越具体，模型越容易在正确时机调用正确工具。

#### 3.4.1.2 使用 Pydantic 模型定义工具【推荐】

当参数复杂、需要枚举值或业务逻辑验证时使用：

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from langchain.tools import tool

# 定义参数模型
class WorkOrderQuery(BaseModel):
    order_id: Optional[str] = Field(None, description="工单ID，如 TK2024001")
    status: Optional[Literal["待处理", "处理中", "已完成"]] = Field(None, description="工单状态")
    assignee: Optional[str] = Field(None, description="处理人姓名")

@tool(args_schema=WorkOrderQuery)
def query_work_order(order_id, status, assignee):
    """根据条件查询工单信息"""
    # 查询逻辑...
```

> Pydantic 模型提供强大的类型检查和数据验证。可以用 `Literal` 限定参数为固定选项，用 `Field` 设置默认值和描述。

#### 3.4.1.3 使用 JSON Schema 定义工具

适用于需要动态生成工具参数的场景：

```python
from langchain.tools import tool

json_schema = {
    "type": "object",
    "properties": {
        "category": {"type": "string", "enum": ["小说", "科技", "历史"], "description": "图书种类"},
        "keyword": {"type": "string", "description": "搜索关键词"},
    }
}

@tool(args_schema=json_schema)
def search_books(category, keyword):
    """搜索图书"""
    # 搜索逻辑...
```

#### 3.4.1.4 工具创建总结

| 方式 | 优势 | 适用场景 |
|------|------|----------|
| **@tool 装饰器** | 代码量极少，最直接 | 快速验证、参数简单的工具 |
| **Pydantic 模型** | 强类型检查、数据验证 | 参数复杂的企业内部工具 |
| **JSON Schema** | 可运行时动态生成 | 与外部系统对接、高度动态行为 |

### 3.4.2 调用工具错误处理

当 Agent 调用工具遇到异常时，可以使用 `@wrap_tool_call` 中间件优雅地捕获错误，向 LLM 返回有意义的错误信息：

```python
from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage

@wrap_tool_call
def handle_tool_errors(request, handler):
    """使用自定义消息处理工具执行错误"""
    try:
        return handler(request)
    except Exception as e:
        return ToolMessage(
            content=f"调用工具错误: 请检查输入参数并重试。({str(e)})",
            tool_call_id=request.tool_call["id"]
        )

agent = create_agent(
    model=deepseek_llm,
    tools=[get_stock_price],
    middleware=[handle_tool_errors]
)
```

> `ToolMessage` 必须传递两个核心参数：`content`（错误信息）和 `tool_call_id`（工具调用唯一标识）。

**中间件执行时机：** 用户提问 → LLM 分析并决定调用工具 → 错误处理中间件介入 → 实际工具执行 → 结果/错误返回。

## 3.5 Agent 结构化输出

### 3.5.1 结构化输出支持的策略

`create_agent` 的 `response_format` 参数控制结构化输出，常见取值有四类：

**1) ProviderStrategy** — 使用模型提供商的原生结构化输出功能。适用于 OpenAI、Anthropic Claude、xAI Grok 等支持原生结构化输出的模型。

```python
from langchain.agents.structured_output import ProviderStrategy

agent = create_agent(
    model="gpt-4o",
    response_format=ProviderStrategy(ContactInfo)
)
```

**2) ToolStrategy** — 通过创建"虚拟工具"实现结构化输出。兼容绝大多数支持工具调用的现代模型。

```python
from langchain.agents.structured_output import ToolStrategy

agent = create_agent(
    model="gpt-4o-mini",
    tools=[search_tool],
    response_format=ToolStrategy(ContactInfo)
)

result = agent.invoke({"messages": [{"role": "user", "content": "..."}]})
result["structured_response"]
# ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')
```

**3) type 直接传入** — LangChain 根据模型能力自动选择策略。

**4) None（默认）** — 不使用结构化输出。

> 版本校准：原始资料里提到“直接传入 schema 在 1.0 以上不再支持”的说法不准确。LangChain v1.x 官方文档仍支持直接传入 schema，由框架自动选择 `ProviderStrategy` 或 `ToolStrategy`。不过在生产项目中，为了行为更可控，推荐显式写 `ProviderStrategy(...)` 或 `ToolStrategy(...)`。

### 3.5.2 ToolStrategy

ToolStrategy 是最通用的策略，支持四种 Schema 定义方式：

#### 3.5.2.1 四种结构化输出 Schema

| Schema 方式 | 说明 |
|-------------|------|
| Pydantic | 强类型验证，推荐方式 |
| Dataclass | Python 标准库 dataclass |
| TypedDict | 轻量级字典类型 |
| JSON Schema | 跨语言友好 |

```python
# Pydantic Schema 示例
class AnalysisReport(BaseModel):
    sentiment: str = Field(description="情感倾向")
    score: float = Field(description="评分")

agent = create_agent(
    model=deepseek_llm,
    tools=[analyze_text],
    response_format=ToolStrategy(AnalysisReport)
)
```

#### 3.5.2.2 自定义工具消息

ToolStrategy 支持自定义工具消息格式，用于在结构化输出过程中提供更精细的控制。

#### 3.5.2.3 ToolStrategy 错误处理

可以自定义错误处理函数，在结构化输出解析失败时进行处理：

```python
def handle_parsing_error(error: Exception) -> str:
    return f"格式解析失败，请重新生成。错误：{error}"

agent = create_agent(
    model=deepseek_llm,
    response_format=ToolStrategy(ProductReview, handle_errors=handle_parsing_error)
)
```

## 关键面试考点

1. LangChain 有哪三种工具创建方式？各自的适用场景是什么？
2. `@wrap_tool_call` 中间件的执行时机是什么？
3. Agent 结构化输出的四类 `response_format` 取值是什么？各自适用于什么模型？
4. ToolStrategy 的核心原理是什么？它如何实现结构化输出？
5. ToolMessage 的两个必传参数是什么？

## 知识关联

- 上一篇：[[LC-04-Agent智能体基础]]
- 下一篇：[[LC-06-Agent异步调用与流式输出]]
- 相关：[[10-AI Agent]] — AI Agent 的理论基础

---

*上一篇：[[LC-04-Agent智能体基础]] | 下一篇：[[LC-06-Agent异步调用与流式输出]]*
