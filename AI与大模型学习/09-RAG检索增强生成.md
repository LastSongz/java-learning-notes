# 09 - RAG（检索增强生成）

> 第三阶段 · 第3课 | 2026-05-06

## 为什么需要 RAG？

大模型不知道：
- 你公司的内部文档
- 你数据库里的业务数据
- 训练截止日期之后的事

RAG = 让大模型基于你的私有数据回答问题。

## 核心思路

```
不用 RAG：用户提问 → 直接给模型 → 瞎编或说不知道
用 RAG：  用户提问 → 检索相关资料 → 资料+问题一起给模型 → 基于资料回答

类比：开卷考试（翻参考书再答题）
```

## 六步流程

```
① 加载文档（Loading）      → 把资料读进来
② 文本分块（Splitting）     → 把长文档切成小段
③ 向量化（Embedding）       → 每段文字变成向量
④ 存入向量数据库（Storing）  → 存起来方便搜索
⑤ 检索相关内容（Retrieving）→ 找最相关的几段
⑥ 生成回答（Generating）    → 相关内容+问题给模型
```

## 代码实现（LangChain）

### 加载 + 分块

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ① 加载
loader = PyPDFLoader("company_policy.pdf")
documents = loader.load()

# ② 分块
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # 每块最多500字符
    chunk_overlap=50      # 相邻块重叠50字符
)
chunks = splitter.split_documents(documents)
```

### 向量化 + 存储

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./db"
)
```

### 检索 + 生成

```python
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", "根据以下参考资料回答。如果资料中没有相关信息，请说'根据现有资料无法回答'。\n\n参考资料：{context}"),
    ("user", "{input}")
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(
    vectorstore.as_retriever(search_kwargs={"k": 3}),
    question_answer_chain
)

response = rag_chain.invoke({"input": "公司年假有几天？"})
print(response["answer"])
```

## 向量数据库

```
Chrom    → 轻量，适合入门
FAISS    → Facebook 开源，纯本地，快
Pinecone → 云服务，适合生产
Milvus   → 国产，大规模部署

核心能力：输入向量 → 快速找到最相似的 N 个向量 → 返回对应文本
```

## RAG vs 微调 vs 纯 Prompt

```
                纯 Prompt        RAG             微调
──────────────────────────────────────────────────────
知识更新        靠手写           随时更新数据库     需重新训练
私有数据        放不进去         ✅ 完美支持       可以但不灵活
实现难度        最简单           中等              最难
成本            最低             中等              最高
回答可溯源      ❌               ✅ 能看到出处      ❌
适合场景        简单问答         知识库、客服       改变模型行为风格
```

## 关键要点

1. RAG = 让模型基于私有数据回答问题
2. 核心思路 = 检索资料 + 基于资料生成（开卷考试）
3. 六步 = 加载 → 分块 → 向量化 → 存储 → 检索 → 生成
4. 分块 = 精确搜索 + 不超窗口
5. 向量数据库 = 存向量、找相似
6. 企业 AI 首选 RAG（便宜、灵活、可溯源）

---

**上一课**：[[08-API开发]]
**下一课**：[[10-AI Agent]]
