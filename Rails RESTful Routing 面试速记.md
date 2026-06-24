---
title: "Rails RESTful Routing 面试速记"
created: 2026-06-24
updated: 2026-06-24
tags:
  - 分类/面试
  - 公司/Strikingly
  - 主题/Rails
  - 主题/API设计
  - 类型/索引
status: seed
category: interview
---

# Rails RESTful Routing 面试速记

> 这页只抓面试最容易被追问的几个路由约定，先保证能把笔试设计和接口命名讲顺。

## 核心原则

- URL 表示资源，HTTP Method 表示动作。
- 资源路径通常使用小写下划线复数，例如 `/phone_verification_codes`。
- 能用名词资源，就不要退回到动作式路径，例如 `/sign_up`、`/voteCandidate`。

## 高频例子

### 注册

```http
POST /voters
```

- 含义：创建一个 `voter` 资源。
- 面试表达：注册不是特殊魔法动作，本质就是创建投票者。

### 登录/登出

```http
POST /session
DELETE /session
```

- 当前用户会话通常是单数资源，所以常见写法是 `resource :session`。
- 重点不是死记 DSL，而是知道“当前会话”通常没有集合语义。

### 候选人和照片

```http
GET /candidates
GET /candidates/:id
GET /candidates/:candidate_id/pictures
```

- 候选人照片是一对多关系，通常挂在候选人资源下。
- 如果只是展示图片 URL，可以不一定暴露复杂路由，但建模要能讲清。

## 和 Spring MVC 的类比

- Spring MVC 更常见的是手写 `@GetMapping("/users/{id}")` 这类路径。
- Rails 把资源约定做得更强，面试里可以说它“默认鼓励 RESTful 风格”。
- 两边本质都在做资源暴露和请求分发，只是代码组织方式不同。

## 面试不要踩的坑

- 不要把 RESTful 简化成“只是 URL 好看”。
- 不要把 `resources`、`resource` 的单复数差异讲错。
- 不要把动作式路径说成“绝对不能用”；更稳妥的说法是“常规 CRUD 资源更推荐 RESTful 命名”。

## 关联

- [[Ruby与Rails面试速记]]
- [[Strikingly笔试设计复盘]]
- [[闪卡-Strikingly面试专项]]
