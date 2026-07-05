---
title: "Rails RESTful Routing 面试速记"
created: 2026-06-24
updated: 2026-07-05
tags:
  - 分类/面试
  - 主题/Rails
  - 主题/API设计
  - 类型/索引
status: seed
category: interview
---

# Rails RESTful Routing 面试速记

> 这页只抓面试最容易被追问的几个路由约定，先保证能把资源建模和接口命名讲顺。

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
- 面试表达：注册不是特殊魔法动作，本质就是创建一个用户侧资源。

### 登录 / 登出

```http
POST /session
DELETE /session
```

- 当前用户会话通常是单数资源，所以常见写法是 `resource :session`。
- 重点不是死记 DSL，而是知道“当前会话”通常没有集合语义。

### 一对多子资源

```http
GET /candidates
GET /candidates/:id
GET /candidates/:candidate_id/pictures
```

- 子资源天然挂在父资源下时，这种设计更容易解释建模关系。
- 就算实际项目不暴露完整子路由，也要能说明父子关系和查询边界。

## 资源建模时常见的面试解释

- “注册为什么不是 `/sign_up`？”：因为注册本质是创建资源，动作由 `POST` 表达。
- “为什么是 `resource :session` 而不是 `resources :sessions`？”：因为当前用户会话通常是唯一资源。
- “为什么照片不直接平铺在主表里？”：因为一对多关系单独建模更自然，后续扩展和位置管理也更清楚。

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
- [[PostgreSQL面试速记]]
- [[MOC-Java面试]]