# 10 - AI Agent

> 第三阶段 · 第4课 | 2026-05-06

## Agent 和普通聊天的区别

```
普通聊天：给建议，不干活
Agent：调 API、查数据库、执行操作，真的帮你完成任务
```

## 四个核心组件

```
大脑（LLM）：理解意图、做决策、规划步骤
工具（Tools）：搜索引擎、数据库、API、代码执行器
记忆（Memory）：短期记忆（对话历史）+ 长期记忆（知识库）
规划（Planning）：复杂任务拆成步骤，按顺序执行
```

## Function Calling（工具调用）

这是 Agent 最关键的能力：模型决定调用哪个函数，你执行后把结果喂回去。

### 完整流程

```python
from openai import OpenAI
import json

client = OpenAI(api_key="sk-xxxxxxxx")

# 1. 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名"}
                },
                "required": ["city"]
            }
        }
    }
]

# 2. 用户提问（传入工具列表）
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "北京天气怎么样？"}],
    tools=tools
)

# 3. 模型决定调用工具（不会真的执行！）
message = response.choices[0].message
# message.tool_calls → [get_weather(city="北京")]

# 4. 你执行函数，把结果发回模型
def get_weather(city):
    return {"city": city, "weather": "晴天", "temp": "25°C"}

tool_results = []
for tc in message.tool_calls:
    args = json.loads(tc.function.arguments)
    result = get_weather(**args)
    tool_results.append({
        "tool_call_id": tc.id,
        "role": "tool",
        "content": json.dumps(result, ensure_ascii=False)
    })

# 5. 把结果发回，模型生成最终回答
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "北京天气怎么样？"},
        message,
        *tool_results
    ],
    tools=tools
)
print(response.choices[0].message.content)
```

> [!important] 关键理解
> 模型不直接执行工具！它只做决策（"我要调 get_weather(city=北京)"），你负责执行并把结果喂回去。

## Agent 核心循环

```
思考 → 行动（调工具）→ 观察（看结果）→ 再思考 → ... → 最终回答
```

## ReAct 模式（Reason + Act）

```
用户: "2024奥运会在哪？那里天气怎么样？"

Thought: 先查奥运会地点
Action: search("2024奥运会举办地")
Observation: 法国巴黎

Thought: 知道地点了，查天气
Action: get_weather(city="巴黎")
Observation: 多云 18°C

Thought: 信息齐全了
Answer: 2024奥运会在巴黎，今天多云18°C

→ 重复 Thought → Action → Observation 直到任务完成
```

## Agent 框架

```
LangChain   → 最流行，生态丰富，适合入门
LangGraph   → LangChain 升级版，复杂多步 Agent
AutoGen     → 微软出品，多 Agent 协作
Dify        → 可视化搭建，低代码
Coze（扣子） → 字节跳动，免费好上手
```

## LangChain 搭建 Agent 示例

```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气"""
    return {"北京": "晴天 25°C", "上海": "多云 22°C"}.get(city, "未找到")

@tool
def calculate(expression: str) -> str:
    """计算数学表达式"""
    return str(eval(expression))

llm = ChatOpenAI(model="gpt-4o-mini")
tools = [get_weather, calculate]
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个助手，可以使用工具帮助用户。"),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({"input": "北京天气怎么样？比上海热多少？"})
print(result["output"])
```

## 关键要点

1. **Agent** = LLM + 工具 + 记忆 + 规划，能自主完成任务
2. **Function Calling** = 模型决策调什么函数，你执行后喂回结果
3. **核心循环** = 思考 → 行动 → 观察 → 再思考
4. **ReAct** = Reason + Act，经典推理框架
5. 模型只决策不执行，你负责执行
6. LangChain / Dify / Coze 等框架简化 Agent 开发

---

**上一课**：[[09-RAG检索增强生成]]
**下一课**：[[11-数据准备]]
