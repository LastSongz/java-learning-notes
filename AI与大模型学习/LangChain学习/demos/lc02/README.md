# LC-02 Demo：模型初始化与调用

这些 demo 配套 `LC-02-模型调用与Chat Models.md`，用于在 IDE 中实际体验 `init_chat_model`、`invoke`、`stream`、`batch`、`async`。

## 1. 安装依赖

```bash
pip install -U langchain langchain-deepseek python-dotenv
```

如果你使用 OpenAI：

```bash
pip install -U langchain langchain-openai python-dotenv
```

## 2. 配置环境变量

复制 `.env.example` 为 `.env`，填入自己的 API Key。

```bash
copy .env.example .env
```

默认使用 DeepSeek：

```env
LANGCHAIN_MODEL_PROVIDER=deepseek
LANGCHAIN_MODEL=deepseek-chat
DEEPSEEK_API_KEY=sk-your-api-key
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

## 3. 运行顺序

建议按这个顺序运行：

```bash
python 01_invoke_basic.py
python 02_messages_conversation.py
python 03_stream_output.py
python 04_batch_calls.py
python 05_async_calls.py
```

## 4. 学习重点

- `invoke()`：一次性拿到完整结果
- `stream()`：边生成边返回，适合聊天界面
- `batch()`：多个互相独立的问题并发处理
- `ainvoke()`：异步调用，适合 Web 服务和高并发场景
- `SystemMessage` / `HumanMessage` / `AIMessage`：Chat Model 的消息结构
