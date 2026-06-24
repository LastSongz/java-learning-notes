---
title: "Strikingly笔试设计复盘"
created: 2026-06-24
updated: 2026-06-24
tags:
  - 分类/面试
  - 公司/Strikingly
  - 主题/系统设计
  - 类型/索引
status: seed
category: interview
---

# Strikingly 笔试设计复盘

> 这页作为投票系统笔试题的总入口，先把表设计、路由和并发防重这些高频追问串起来。

## 题目主线

- 一个 `voter` 只能投一次票。
- 每个 `candidate` 有 20 张照片，需要稳定展示顺序。
- 注册、登录、投票都需要能解释清楚资源建模和接口设计。
- 面试官更关心“你为什么这么设计”，不只是表名写出来了没有。

## 五张核心表

1. `voters`
2. `phone_verification_codes`
3. `candidates`
4. `candidate_pictures`
5. `votes`

## 必须讲顺的设计点

### 为什么照片单独建表
- 一对多关系更自然。
- 20 个字段平铺在 `candidates` 里扩展性差。
- 需要 `position` 表达稳定展示顺序。

### 为什么保留 position
- 插入顺序不一定等于展示顺序。
- 后续替换图片时，位置语义更稳定。
- 可用 `candidate_id + position` 约束同一位置不重复。

### 一人一票怎么兜底
- 前端禁用按钮只是体验层防重。
- 后端最终靠 `votes.voter_id` 唯一约束。
- 并发场景下一条成功、一条失败，是预期结果。

### 为什么可以不建数据库外键
- 这是工程取舍，不是不会建。
- 可以保留模型层关联语义，把完整性更多放到应用层校验、索引和事务控制里。
- 适合顺带聊批量导入、数据修复、迁移复杂度这些现实问题。

## 接口命名主线

- 注册：`POST /voters`
- 登录：`POST /session`
- 投票：围绕 `votes` 资源设计，不要默认写成动作式 API

## 深入阅读入口

- [[Rails RESTful Routing 面试速记]]
- [[PostgreSQL面试速记]]
- [[闪卡-Strikingly面试专项]]

## 关联

- [[Strikingly中级后端工程师面试复习清单]]
- [[MOC-Java面试]]
