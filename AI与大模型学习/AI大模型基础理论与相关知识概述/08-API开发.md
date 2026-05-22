---
title: "API开发"
created: 2026-05-19
updated: 2026-05-19
tags:
  - 分类/ai
status: complete
category: ai
---

# 08 - API 开发

> 第三阶段 · 第2课 | 2026-05-06

## API 调用本质

```
你的代码 ── HTTP请求(JSON) ──→ 大模型服务
你的代码 ←─ HTTP响应(JSON) ── 大模型服务
```

## 最简示例（OpenAI）

```python
from openai import OpenAI

client = OpenAI(api_key="sk-xxxxxxxxxxxx")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "用一句话解释什么是AI"}]
)

print(response.choices[0].message.content)
```

## 请求体结构

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "你是一个资深Java开发工程师"},    # 系统指令
        {"role": "user", "content": "HashMap和ConcurrentHashMap区别？"},  # 用户提问
        {"role": "assistant", "content": "HashMap是线程不安全的..."},      # 模型历史回复
        {"role": "user", "content": "性能差距有多大？"},                   # 继续提问
    ],
    temperature=0.7,    # 温度
    max_tokens=500,     # 最大生成 Token 数
    top_p=0.9,          # Top-P 采样
)
```

### 三种角色

| role | 含义 | 类比 |
|------|------|------|
| system | 系统指令，设定行为规则 | Prompt 中的角色设定 |
| user | 用户说的话 | 你的提问 |
| assistant | 模型之前的回复 | 对话历史 |

> [!important] 模型没有记忆
> 每次请求都是独立的，必须自己维护对话历史，每次把完整历史发过去。

## 响应体结构

```python
response.choices[0].message.content   # 回复内容
response.model                        # 使用的模型
response.usage.prompt_tokens          # 输入 Token 数
response.usage.completion_tokens      # 输出 Token 数
response.usage.total_tokens           # 总 Token 数
response.choices[0].finish_reason     # "stop"正常结束 / "length"被截断
```

## 多轮对话

```python
messages = [
    {"role": "system", "content": "你是Java面试教练"}
]

# 第1轮
messages.append({"role": "user", "content": "开始面试，主题是JVM"})
response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
reply = response.choices[0].message.content
messages.append({"role": "assistant", "content": reply})

# 第2轮
messages.append({"role": "user", "content": "JVM有类加载、运行时数据区等子系统"})
response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
reply = response.choices[0].message.content
messages.append({"role": "assistant", "content": reply})
```

## 流式输出（Streaming）

```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "写一首关于编程的诗"}],
    stream=True
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
```

## 费用计算

```
GPT-4o-mini（参考价）：
  输入：$0.15 / 1M Token
  输出：$0.60 / 1M Token

费用 = 输入Token数/1000000 × 输入单价 + 输出Token数/1000000 × 输出单价
1M Token ≈ 75万汉字
注意：多轮对话历史越长，输入 Token 越多，费用累积
```

## 国产模型 API（兼容 OpenAI 接口）

```python
# 通义千问（阿里）
client = OpenAI(
    api_key="sk-xxxxxxxx",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# DeepSeek
client = OpenAI(
    api_key="sk-xxxxxxxx",
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"
```

> 只需改 base_url 和 model，代码几乎不用动。

## 错误处理

```python
from openai import OpenAI, APIError, RateLimitError, APITimeoutError

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "你好"}],
        timeout=30
    )
except RateLimitError:
    print("请求太快，稍后重试")
except APITimeoutError:
    print("请求超时")
except APIError as e:
    print(f"API错误: {e}")
```

## 关键要点

1. API 调用 = 发 JSON 请求，收 JSON 响应
2. messages 三种角色：system / user / assistant
3. 模型没有记忆 → 每次带完整对话历史
4. 流式输出 stream=True → 逐 Token 返回
5. 国产模型兼容 OpenAI 接口 → 改 base_url 即可
6. 费用 = 输入Token×单价 + 输出Token×单价
7. 生产环境必须有错误处理

---

**上一课**：[[07-Prompt Engineering]]
**下一课**：[[09-RAG检索增强生成]]
