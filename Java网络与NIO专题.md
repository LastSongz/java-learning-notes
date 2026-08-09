---
title: "Java网络与NIO专题"
created: 2026-07-19
updated: 2026-08-09
tags:
  - 分类/java
  - 主题/网络
  - 主题/nio
  - 类型/索引
status: seed
category: network
---

# Java 网络与 NIO 专题

> 这页先作为高级 Java 补强中的网络入口，承接 TCP、HTTP、NIO、Netty 和 SSE 相关知识，避免学习计划里的链接悬空。

## 先抓住的主线

1. 先理解连接是怎么建立、保持和关闭的。
2. 再理解 Java 如何从阻塞 IO 走到 NIO / 事件驱动。
3. 最后把这些机制落到 Netty、Redis、MQ、SSE 这类真实系统上。

## 这一专题建议覆盖的块

### 协议与连接
- TCP 三次握手、四次挥手、TIME_WAIT、KeepAlive
- HTTP/1.1 长连接、HTTP/2、多路复用
- SSE 和 WebSocket 的适用边界

### Java IO 模型
- BIO、NIO、AIO 的差异
- `Buffer`、`Channel`、`Selector`、直接内存
- 阻塞模型为什么会卡线程，事件驱动为什么能抗高并发连接

### Netty 与工程化表达
- Reactor 模型、EventLoop、ChannelPipeline、Handler
- 粘包拆包、背压、零拷贝
- 如何用项目里的流式输出和消息系统解释这些概念

## 可以和现有笔记串起来的地方

- 并发主线：[[java并发编程]]
- JVM 与内存：[[JVM内存结构]]
- AI 流式输出案例：[[16-聊天助手系统架构]]
- 学习总导航：[[MOC-Java学习]]

## 现有资料落点

- JVM 里的直接内存、堆外内存和 NIO 使用场景：[[JVM内存结构]]
- Redis / MQ 为什么快、零拷贝和事件驱动能怎么讲：[[中间件专题-Redis与MQ]]
- AI 助手里的 SSE 流式返回，可以拿来解释长连接和线程占用：[[16-聊天助手系统架构]]
- 补强计划里的本周目标和口述要求：[[能力差距分析/高级Java开发工程师补强学习计划]]

## 建议的整理顺序

1. 先用 [[JVM内存结构]] 把直接内存、堆外内存、GC 不可见区域补齐。
2. 再围绕 Buffer / Channel / Selector 把 BIO、NIO、Reactor 讲成一条链。
3. 最后回到 [[16-聊天助手系统架构]] 和 [[中间件专题-Redis与MQ]]，把 SSE、Redis、MQ 的高并发连接表达串起来。

## 面试回答时可以这样组织

- 先说“这是在解决大量连接和线程成本的问题”。
- 再讲 NIO / Reactor 如何把一个线程从“等 IO”改成“处理就绪事件”。
- 最后补一句你项目里哪个接口或链路最能体现这个模型，比如 SSE 长连接或消息消费。

## 后续补充清单

- [ ] BIO / NIO / AIO 对比图
- [ ] Reactor 三种线程模型
- [ ] SSE vs WebSocket 的项目表达
- [ ] Netty 常见面试问答

## 关联

- [[能力差距分析/高级Java开发工程师补强学习计划]]
- [[MOC-Java学习]]
- [[面试问题记录]]
