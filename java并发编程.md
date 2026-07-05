---
title: "java并发编程"
created: 2026-04-11
updated: 2026-07-05
tags:
  - 分类/java
  - 分类/面试
  - 主题/并发
  - 类型/索引
status: seed
category: concurrency
---

# Java 并发编程

> 这页作为并发主题的总入口，承接 `[[MOC-Java面试]]`、`[[MOC-Java学习]]` 等导航中的并发链接，避免落到空白页。

## 并发面试的主线

- 先讲清线程和任务模型：进程、线程、线程切换、线程安全问题。
- 再讲同步原语：`synchronized`、`volatile`、CAS、AQS、`ReentrantLock`。
- 然后扩展到线程池、并发容器、锁优化、性能排查。
- 最后把知识点落到真实系统：高并发接口、任务堆积、线程池隔离、幂等与重试。

## 题型地图

### 线程基础
- `start()` 和 `run()` 的区别
- `sleep()`、`wait()`、`join()`、`yield()` 的使用场景
- 线程状态流转与常见阻塞原因

### 同步与可见性
- `synchronized` 锁升级过程
- `volatile` 的可见性和指令重排
- CAS、ABA、AQS、`ReentrantLock`、`Condition`

### 线程池与任务治理
- 核心参数：核心线程数、最大线程数、队列、拒绝策略
- 常见问题：线程池打满、任务堆积、上下游超时传染
- 实战表达：为什么不能直接 `Executors.newFixedThreadPool(...)`

### 并发容器与数据结构
- `ConcurrentHashMap` 的线程安全实现
- `CopyOnWriteArrayList`、阻塞队列的适用场景
- 读写锁、分段思想、LongAdder

## 深入阅读入口

- 锁与底层原语：[[锁机制与并发原语]]
- 集合与并发容器：[[HashMap与ConcurrentHashMap]]
- JVM 与线上排查：[[JVM内存结构]]
- 总导航：[[MOC-Java面试]]

## 面试表达建议

- 回答并发题时，不要只背定义，尽量补一句“这个问题在线上会造成什么后果”。
- 讲线程池时，顺带说明你如何根据接口类型、超时和下游依赖做隔离。
- 讲锁时，把“为什么需要它”“竞争激烈时的代价”“替代方案”一起说清楚。

## 关联

- [[MOC-Java学习]]
- [[MOC-Java面试]]
- [[面试问题记录]]
