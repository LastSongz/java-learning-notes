---
title: "PostgreSQL面试速记"
created: 2026-06-24
updated: 2026-06-24
tags:
  - 分类/面试
  - 公司/Strikingly
  - 主题/PostgreSQL
  - 类型/索引
status: seed
category: database
---

# PostgreSQL 面试速记

> 这页先服务 Strikingly 笔试与面试复盘，重点不是系统讲 PostgreSQL，而是把当前会被问到的差异点讲顺。

## 当前最容易被问的点

### 主键为什么不是默认 UUID
- PostgreSQL 支持 UUID，但不是默认就用 UUID。
- Rails + PostgreSQL 常见默认主键仍是整数型，通常是 `bigint` / identity。
- 如果业务没有分布式生成主键、跨系统合并等强诉求，`bigint` 是更自然的默认选择。

### comment / migration
- PostgreSQL 支持 `COMMENT ON TABLE/COLUMN`，适合把表意图写清楚。
- 在 Rails 语境下，可以把它理解为 migration 里可维护的表结构元信息，而不只是“建完表再手工备注”。

### partial index
- `delete_flag` 这种低基数字段不适合盲目建普通单列索引。
- PostgreSQL 提供 partial index，适合“只给活跃数据建立索引”这类场景。
- 面试表达重点是“根据查询模式决定索引”，不是为了炫技而上特性。

### 唯一约束与并发防重
- 一人一票这种规则，最终仍要落到数据库唯一约束兜底。
- 应用层校验只负责更友好的返回，不能替代数据库约束。

## 和 MySQL 的表达差异

- 不要说 PostgreSQL “比 MySQL 高级很多”，这种说法没价值。
- 更稳妥的表达是：二者都能满足常规 OLTP，PostgreSQL 在类型系统、扩展能力、部分特性表达上更灵活。
- 如果你没有长期 PostgreSQL 实战，承认这个边界，比硬讲内部实现更可靠。

## 复习时优先串起来的场景

1. Strikingly 笔试里的五张核心表设计。
2. `votes.voter_id` 唯一约束保证投票幂等。
3. `candidate_pictures.position` 的唯一性与展示顺序。
4. 审计字段、软删除和索引取舍。

## 关联

- [[Strikingly笔试设计复盘]]
- [[Strikingly中级后端工程师面试复习清单]]
- [[闪卡-Strikingly面试专项]]
