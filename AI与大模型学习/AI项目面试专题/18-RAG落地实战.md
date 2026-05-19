---
title: "RAG落地实战"
created: 2026-05-19
updated: 2026-05-19
tags:
  - 分类/ai
  - 分类/面试
  - 主题/rag
status: complete
category: ai
---

# 18 - RAG 落地实战

> AI项目面试专题 | 面向简历：「实现基于wiki知识库的用户意图理解」

## 一、面试官会怎么问？

```
"wiki 文档是怎么变成向量库的？分块策略是什么？"
"用的什么 Embedding 模型？为什么选它？"
"检索出来的内容不准怎么办？有做 rerank 吗？"
"wiki 内容更新了，向量库怎么同步？"
"RAG 的效果怎么评估？准确率多少？"
"chunk size 设多大？为什么？"
```

## 二、从 Wiki 到向量库的完整链路

```
Wiki 原始文档（Confluence/飞书文档）
        │
        ▼
① 文档采集（定时爬取 / Webhook 回调）
        │
        ▼
② 文本清洗（去 HTML 标签、去图片、统一格式）
        │
        ▼
③ 文本分块（按标题/段落切分，chunk_size=500，overlap=50）
        │
        ▼
④ 向量化（Embedding 模型 → 1536 维向量）
        │
        ▼
⑤ 存入向量数据库（Milvus / Chroma / Pinecone）
        │
        ▼
⑥ 用户提问 → 检索 top-k → 注入 Prompt → LLM 生成回答
```

## 三、文档分块策略（高频考点）

### 3.1 为什么要分块？

```
① LLM 有 token 窗口限制，不能把整篇文档塞进去
② 检索精度：小块比大块搜索更精准
③ 成本控制：只喂相关片段，不浪费 token
```

### 3.2 分块方法对比

```
方法              适用场景              优缺点
────────────────────────────────────────────────────
固定长度切分        简单文档              简单但可能切断语义
按段落切分          结构化文档            保持段落完整
按标题层级切分      Wiki/Markdown文档     ✅ 推荐，语义完整
语义切分            高精度需求            用 Embedding 相似度切
递归字符切分        通用                  LangChain 默认，平衡
```

### 3.3 Wiki 文档推荐：按标题层级分块

```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

# 按 Markdown 标题层级分块
headers_to_split_on = [
    ("#", "h1"),     # 一级标题
    ("##", "h2"),    # 二级标题
    ("###", "h3"),   # 三级标题
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
chunks = splitter.split_text(wiki_content)

# 结果：每个 chunk 是一个完整的小节，带有标题元数据
# chunk.metadata = {"h1": "退货流程", "h2": "退货申请", "h3": "申请条件"}
```

### 3.4 Chunk Size 怎么选？

```
太小（100-200字）：上下文丢失，检索到片段但不完整
适中（300-500字）：✅ 推荐，语义完整，检索精准
太大（1000+字）：  检索不精准，浪费 token

Overlap（重叠）= 50-100 字，避免边界处语义断裂

实际做法：先按标题分，如果某块超过 500 字再用 RecursiveCharacterTextSplitter 二次切分
```

## 四、Embedding 模型选型

```
模型                          维度    特点                价格
──────────────────────────────────────────────────────────────
text-embedding-3-small        1536   OpenAI，性价比高      $0.02/1M tokens
text-embedding-3-large        3072   OpenAI，精度最高      $0.13/1M tokens
bge-large-zh-v1.5             1024   开源，中文效果好      免费（本地部署）
bge-m3                        1024   开源，多语言          免费（本地部署）
m3e-large                     1024   开源，中文专用        免费（本地部署）

供应链场景建议：
- 数据量小（<10万条）→ OpenAI embedding-3-small（简单效果好）
- 数据量大 / 中文为主 → bge-large-zh（免费 + 中文效果好）
- 涉及多语言 → bge-m3
```

## 五、检索优化（进阶考点）

### 5.1 Rerank（重排序）

```
问题：向量检索 top-10 结果，可能第 8 条才是最相关的

解决：用 Rerank 模型对 top-10 重新排序
      先粗检索（向量相似度 top-10）
      再精排序（Rerank 模型交叉打分）

常用 Rerank 模型：
- Cohere Rerank（API 调用，效果好）
- bge-reranker-large（开源，本地部署）
- Jina Reranker（开源）
```

### 5.2 混合检索（Hybrid Search）

```
纯向量检索：擅长语义匹配（"退货" 匹配 "退款"）
纯关键词检索：擅长精确匹配（"SO-001" 必须精确）

混合检索 = 向量检索 + 关键词检索（BM25）→ 加权合并结果

适用场景：
- 用户输入包含精确编号（订单号、SKU）→ 关键词检索更准
- 用户描述模糊（"怎么处理延迟发货"）→ 向量检索更准
```

### 5.3 元数据过滤

```
检索时带上过滤条件，缩小搜索范围

例子：
- 用户角色是"仓库管理员" → 只检索仓库相关文档
- 用户问"退货流程" → 过滤 tag="退货" 的文档
- 用户在"采购模块" → 优先检索采购相关文档

实现：向量数据库支持 metadata filter
vectorstore.as_retriever(
    search_kwargs={
        "k": 5,
        "filter": {"department": "warehouse"}  # 元数据过滤
    }
)
```

## 六、增量更新机制

### 6.1 问题：Wiki 内容更新了怎么办？

```
方案一：全量重建（简单粗暴）
- 每天凌晨全量重新索引
- 适合文档量小（<1000 篇）

方案二：增量更新（推荐）
- 监听 Wiki Webhook，文档变更时触发
- 对比文档 hash，只更新变化的部分
- 记录每篇文档的最后更新时间
- 删除旧向量 → 重新分块 → 重新向量化 → 写入

方案三：版本管理
- 每篇文档保存多个版本
- 用户可以查看历史版本的内容
- 适合需要审计追溯的场景
```

### 6.2 增量更新代码示例

```python
import hashlib

def sync_wiki_document(doc_id: str, content: str):
    """同步单篇 Wiki 文档到向量库"""
    # 1. 计算内容 hash
    content_hash = hashlib.md5(content.encode()).hexdigest()

    # 2. 查询已有记录
    existing = db.get_document(doc_id)

    if existing and existing.hash == content_hash:
        return  # 内容没变，跳过

    # 3. 内容变了 → 删除旧向量
    if existing:
        vectorstore.delete(filter={"doc_id": doc_id})

    # 4. 重新分块 + 向量化
    chunks = splitter.split_text(content)
    for chunk in chunks:
        chunk.metadata["doc_id"] = doc_id
        chunk.metadata["updated_at"] = datetime.now().isoformat()

    vectorstore.add_documents(chunks)

    # 5. 更新文档记录
    db.upsert_document(doc_id, content_hash=content_hash)
```

## 七、RAG 效果评估

```
评估维度：
① 召回率（Recall）：相关文档是否被检索到？
② 准确率（Precision）：检索到的文档是否相关？
③ 答案质量：基于检索内容生成的答案是否准确？
④ 无幻觉率：答案是否忠实于检索内容？

评估方法：
① 人工评测：准备 100 个标准 Q&A 对，对比 AI 回答
② LLM-as-Judge：用 GPT-4 评估回答质量
③ 自动指标：检索命中率、答案相似度

实际经验：
- 优化前：回答准确率 ~70%
- 加 Rerank 后：~85%
- 加混合检索后：~90%
- 加元数据过滤后：~93%
```

## 八、面试答题模板

> **Q：你的 RAG 是怎么落地的？**

```
我们基于公司 wiki 构建了 RAG 系统。分块用 Markdown 标题层级切分，
chunk_size 500，overlap 50。Embedding 用的 xxx 模型，存到 xxx 向量库。

检索链路：用户提问 → 向量检索 top-5 → Rerank 重排 → 取 top-3 注入 Prompt → LLM 生成。

wiki 更新通过 Webhook 触发增量同步，对比文档 hash 只更新变化的部分。

效果方面，经过 Rerank + 混合检索优化，回答准确率从 70% 提升到 90%+。
```

## 关键要点

1. **分块策略** = Wiki 按标题层级分块，chunk_size 500，二次切分超长段落
2. **Embedding** = OpenAI / bge 中文模型，根据数据量和语言选型
3. **检索优化** = Rerank 重排序 + 混合检索（向量+BM25）+ 元数据过滤
4. **增量更新** = Webhook + 文档 hash 对比，只更新变化部分
5. **效果评估** = 人工评测 + 检索命中率 + 答案准确率
6. 面试重点讲**分块策略 + 检索优化 + 增量更新**这三个环节

---

**上一课**：[[09-RAG检索增强生成]]（理论基础）
**相关笔记**：[[16-聊天助手系统架构]] | [[17-意图识别与分类]]
