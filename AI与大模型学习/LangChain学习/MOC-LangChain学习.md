---
title: "MOC-LangChain学习"
created: 2026-05-21
updated: 2026-06-08
tags:
  - 类型/moc
  - 分类/ai
  - 分类/langchain
status: in-progress
category: langchain
---

# LangChain 学习导航

> LangChain 是构建 LLM 应用的主流框架，掌握它是大模型应用开发工程师的核心技能

## 整理口径

本目录由原始课程资料整理而来：第1章 LangChain 介绍、第2章 Models 模型、第3章 Agent 智能体、第4~5章 Agent 记忆。整理时没有逐字搬运原文，而是按学习路径拆成本地笔记，并补充 LangChain v1.x / LangGraph 口径下更准确的理解。

详细对照见：[[资料对照-原始文档与本地笔记]]

配套手敲练习见：[[LC-Demo手敲指南-Java与Python]]

## 前置知识

| 主题 | 说明 |
|------|------|
| [[07-Prompt Engineering]] | 提示词工程，LangChain 的 Prompt 模板基础 |
| [[08-API开发]] | LLM API 调用方式 |
| [[09-RAG检索增强生成]] | RAG 原理，LangChain 的核心应用场景 |
| [[10-AI Agent]] | Agent 概念，LangChain Agent 的理论基础 |
| [[15-AI工作流]] | AI 工作流编排，与 LangGraph 相关 |

## 学习路线

### 第一阶段：入门与核心概念
| 编号 | 主题 | 状态 |
|------|------|------|
| LC-01 | [[LC-01-LangChain概述与核心架构]] | ✅ 已完成 |

### 第二阶段：Models 模型
| 编号 | 主题 | 状态 |
|------|------|------|
| LC-02 | [[LC-02-模型调用与Chat Models]] | ✅ 已完成 |
| LC-03 | [[LC-03-模型结构化输出与工具调用]] | ✅ 已完成 |

### 第三阶段：Agent 智能体
| 编号 | 主题 | 状态 |
|------|------|------|
| LC-04 | [[LC-04-Agent智能体基础]] | ✅ 已完成 |
| LC-05 | [[LC-05-Agent工具与结构化输出]] | ✅ 已完成 |
| LC-06 | [[LC-06-Agent异步调用与流式输出]] | ✅ 已完成 |

### 第四阶段：Agent 记忆

| 编号 | 主题 | 状态 |
|------|------|------|
| LC-07 | [[LC-07-Agent短期记忆]] | ✅ 已整理 |
| LC-08 | [[LC-08-Agent长期记忆]] | ✅ 已整理 |
| LC-09 | [[LC-09-Agent记忆综合案例]] | ✅ 已整理 |

### 第五阶段：RAG 与 LangGraph 实战
| 编号 | 主题 | 状态 |
|------|------|------|
| LC-10 | [[LC-10-RAG检索增强生成实战]] | 📝 已建索引 |
| LC-11 | [[LC-11-LangGraph状态图工作流]] | 📝 已建索引 |
| LC-12 | [[LC-12-LangChain项目实战]] | 📝 已建索引 |

## 相关面试题
- [[18-RAG落地实战]]
- [[19-微组件与工具调用设计]]
- [[21-AI项目面试话术]]

## 原始资料来源

| 章节 | 原始链接 | 对应本地笔记 |
|------|----------|--------------|
| 第1章 LangChain介绍 | https://cloud.fynote.com/share/d/IyAJ0qZI0 | [[LC-01-LangChain概述与核心架构]] |
| 第2章 Models 模型 | https://cloud.fynote.com/share/d/GyAJGYW66 | [[LC-02-模型调用与Chat Models]]、[[LC-03-模型结构化输出与工具调用]] |
| 第3章 Agent 智能体 | https://cloud.fynote.com/share/d/AyWXMhzG | [[LC-04-Agent智能体基础]]、[[LC-05-Agent工具与结构化输出]]、[[LC-06-Agent异步调用与流式输出]] |
| 第4~5章 Agent 记忆 | https://cloud.fynote.com/share/d/jA0JAHWpQ | [[LC-07-Agent短期记忆]]、[[LC-08-Agent长期记忆]]、[[LC-09-Agent记忆综合案例]] |
