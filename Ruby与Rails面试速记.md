---
title: "Ruby与Rails面试速记"
created: 2026-06-24
updated: 2026-06-24
tags:
  - 分类/面试
  - 公司/Strikingly
  - 主题/Ruby
  - 主题/Rails
  - 类型/索引
status: seed
category: interview
---

# Ruby 与 Rails 面试速记

> 这页先作为 Strikingly 面试专项里的 Ruby/Rails 顶层入口，避免清单和闪卡跳到空白页。

## 这页怎么用

- 目标不是把自己包装成 Rails 老手，而是证明你知道 Rails 的基本抽象，并能把 Java Web 后端经验迁移过去。
- 面试里优先讲“职责、约定、工程问题”，少讲零散语法点。
- 遇到细节追问时，再跳到更细的子页展开。

## 迁移主线

### Rails MVC
- Model 负责数据和业务约束。
- Controller 负责请求入口、参数接收、调用模型或服务。
- View 在典型前后端分离场景里存在感比传统服务端渲染弱，但仍是 Rails 体系的一部分。
- 和 Spring MVC 类比时，不要硬说一一对应，更稳妥的说法是“都在解决 Web 请求分层，但约定和生态不同”。

### Active Record
- Active Record 同时承载数据访问和一部分领域约束。
- 常见关注点：`validation`、`association`、`scope`、`counter_cache`。
- 面试里要讲清：应用层校验提供友好反馈，数据库约束负责最终兜底。

### Migration 与路由
- Migration 是表结构演进记录，不只是“建表脚本”。
- Rails 倾向 RESTful Routing：URL 表示资源，HTTP Method 表示动作。
- 资源命名、单复数、下划线风格是 Rails 的基础约定。

## 先记住的几个表达

- “我过去主栈是 Java，但后端核心能力并不只绑定某一门语言，业务建模、数据一致性、接口设计、性能与稳定性这些问题在 Ruby/Rails 场景里同样成立。”
- “Rails 的约定比 Spring 更强，所以我准备时重点先抓 MVC、Active Record、Migration 和 RESTful Routing 这几条主线。”
- “我不会假装有多年 Rails 实战，但会明确说明自己已经补了哪些概念、能迁移哪些工程经验。”

## 深入阅读入口

- [[Rails RESTful Routing 面试速记]]
- [[Ruby基础语法面试速记]]
- [[Strikingly中级后端工程师面试复习清单]]
- [[闪卡-Strikingly面试专项]]

## 关联

- [[MOC-Java面试]]
- [[Strikingly面试动机与反问]]
