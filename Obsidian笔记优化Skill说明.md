---
title: "Obsidian 笔记优化 Skill"
tags:
  - 分类/工具
created: 2026-05-19
updated: 2026-05-19
---

# Obsidian 笔记优化 Skill

> 本文件是一个可被 Claude 使用的 Skill 定义，用于全面优化 Obsidian 笔记。

## 功能模块

### 模块 A：格式与元数据统一

给所有笔记添加规范的 front matter，包含 title、created、updated、tags、status、category 字段。

### 模块 B：双向链接补充

分析笔记内容，在关键知识点处添加 `[[]]` 链接，建立知识网络。

### 模块 C：标签体系整理

规范标签命名，去重，建立层级标签结构（如 `#分类/java`、`#主题/jvm`、`#状态/待复习`）。

### 模块 D：知识卡片生成（Spaced Repetition）

从笔记内容提取问答，生成兼容 obsidian-spaced-repetition 插件的闪卡文件，按知识分类生成 8 个闪卡文件。

### 模块 E：对话转笔记

在其他对话中完成学习或研究后，将对话内容整理为结构化的 Obsidian 笔记，自动匹配存放目录、添加 front matter、双向链接、更新 MOC。

### 模块 F：全部执行

按 A → C → B → D → G 的顺序依次执行所有优化。

### 模块 G：推送到 GitHub（自动）

每次优化操作完成后自动执行 git commit 和 git push，提交信息根据执行的模块自动生成。

## 闪卡分类

| 闪卡文件 | 覆盖内容 |
|----------|----------|
| `闪卡-Java基础.md` | Java 语法、集合、异常、IO |
| `闪卡-JVM.md` | 内存结构、GC、调优 |
| `闪卡-并发编程.md` | 线程、锁、JUC |
| `闪卡-数据库.md` | MySQL、索引、事务、MVCC |
| `闪卡-中间件.md` | Redis、MQ、Netty |
| `闪卡-Spring.md` | IoC、AOP、循环依赖 |
| `闪卡-AI与大模型.md` | Transformer、RAG、微调 |
| `闪卡-面试高频.md` | 跨领域面试高频题 |

## 使用方式

在 Claude 对话中说以下任何一句话即可触发：

**笔记优化类：**
- "优化我的 Obsidian 笔记"
- "给我的 Java 笔记统一格式"
- "从 AI 笔记中提取闪卡"
- "整理标签"
- "全面优化"

**对话转笔记类：**
- "把这个对话的内容整理成笔记"
- "我们刚讨论的 XX 保存到笔记里"
- "把刚才学的内容写进笔记"

**Git 推送会在每次操作后自动执行，不需要额外提醒。**
