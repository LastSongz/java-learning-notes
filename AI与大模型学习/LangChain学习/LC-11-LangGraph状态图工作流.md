---
title: "LC-11-LangGraph状态图工作流"
created: 2026-06-08
updated: 2026-06-08
tags:
  - 分类/langchain
  - 分类/ai
  - 难度/实战
status: seed
prev: "[[LC-10-RAG检索增强生成实战]]"
next: "[[LC-12-LangChain项目实战]]"
---

# LC-11 LangGraph 状态图工作流

> 这篇先作为学习入口和整理占位，后续围绕 LangGraph 的状态图建模、节点编排、条件分支和人工介入等能力补充正式内容。

## 学习目标

- 理解 LangGraph 和 LangChain Agent 的关系，以及为什么复杂流程要显式建图
- 串起 State、Node、Edge、Router、Checkpoint 这些核心概念
- 能用状态图视角描述多步骤 Agent / Workflow 的执行路径和中断恢复

## 与现有笔记的关系

- 前置知识：[[15-AI工作流]]、[[LC-04-Agent智能体基础]]、[[LC-10-RAG检索增强生成实战]]
- 上一篇：[[LC-10-RAG检索增强生成实战]]
- 下一篇：[[LC-12-LangChain项目实战]]
- 导航入口：[[MOC-LangChain学习]]

## 计划补充的内容

1. LangGraph 为什么出现，以及它和传统 Chain / Agent 封装的边界
2. StateGraph、节点函数、条件边、循环边的基本组织方式
3. Checkpoint、人工介入、中断恢复如何落到真实工作流
4. 常见工作流模式：顺序编排、路由分发、并行汇总、人工审核
5. 面试表达：如何说明 LangGraph 适合解决的复杂流程问题

## 当前整理说明

这篇笔记目前先保留目录入口，避免 `MOC-LangChain学习` 中的 LC-11 链接悬空。等后续开始 LangGraph 学习时，再按现有 LangChain 笔记风格扩充为正式内容。

## 知识关联

- 上一篇：[[LC-10-RAG检索增强生成实战]]
- 下一篇：[[LC-12-LangChain项目实战]]
- 相关：[[15-AI工作流]] — 先复习工作流编排的通用视角

---

*上一篇：[[LC-10-RAG检索增强生成实战]] | 下一篇：[[LC-12-LangChain项目实战]]*
