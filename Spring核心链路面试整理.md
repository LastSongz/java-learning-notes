---
title: "Spring核心链路面试整理"
created: 2026-07-19
updated: 2026-07-19
tags:
  - 分类/java
  - 主题/spring
  - 主题/框架源码
  - 类型/索引
status: seed
category: spring
---

# Spring 核心链路面试整理

> 这页先把 Spring / Spring Boot / MyBatis 的高频追问串成一条面试主线，方便后续从 `msb` 原始材料沉淀成自己的表达。

## 面试里的主线顺序

1. Bean 是怎么被定义、创建和注入的。
2. 请求是怎么从 Web 层一路走到 Service / DAO 的。
3. AOP、事务、自动装配分别在链路里做了什么增强。

## 当前应优先整理的专题

### 容器与生命周期
- BeanDefinition、BeanFactory、ApplicationContext
- Bean 生命周期、后置处理器、循环依赖

### AOP 与事务
- JDK 动态代理、CGLIB、切点和通知
- `@Transactional` 的生效原理与失效场景
- 自调用、异常处理、传播行为和隔离级别

### Web 与持久层
- DispatcherServlet、HandlerMapping、HandlerAdapter
- Interceptor、参数绑定、异常处理
- MyBatis 的 `#` / `$`、Executor、缓存、插件机制

## 对照现有笔记

- 框架原始材料：[[msb/核心框架源码常见问题（上）]]
- 框架原始材料：[[msb/核心框架源码常见问题（下）]]
- 总导航：[[MOC-Java学习]]
- 项目场景：[[简历面试备战/03-项目二-权限管理]]

## 整理时的表达要求

- 不要只抄源码概念，要能回答“这个机制解决了什么问题”。
- 每个点最好补一个项目落点，例如拦截器、事务边界或权限校验。
- 面试里优先讲调用链，再补源码细节，避免一上来陷在类名里。

## 后续补充清单

- [ ] Bean 生命周期流程图
- [ ] 循环依赖为什么只解决部分场景
- [ ] 请求链路从 Controller 到数据库的口述稿
- [ ] 事务失效案例与规避方式

## 关联

- [[能力差距分析/高级Java开发工程师补强学习计划]]
- [[MOC-Java学习]]
- [[架构能力与工程实践面试清单]]
