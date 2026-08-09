---
title: "Java服务云原生交付入门"
created: 2026-07-19
updated: 2026-08-09
tags:
  - 分类/java
  - 主题/云原生
  - 主题/交付
  - 类型/索引
status: seed
category: delivery
---

# Java 服务云原生交付入门

> 这页先把 Java 服务从代码提交到部署上线的主线串起来，后续逐步补齐 Docker、K8s、发布策略和 CI/CD 视角下的后端表达。

## 先理解的一条交付链

1. 代码提交后先经过构建、测试和制品产出。
2. 然后把应用打成镜像，并注入配置、密钥和运行参数。
3. 最后进入部署、灰度、回滚和运行监控。

## 这一专题要补的块

### 容器与镜像
- Dockerfile 分层、基础镜像、JAR 包构建
- 环境变量、配置管理、镜像体积控制

### K8s 运行视角
- Pod、Deployment、Service、ConfigMap、Secret、Ingress
- `livenessProbe` / `readinessProbe`
- 滚动发布、蓝绿、金丝雀、回滚

### CI/CD 与交付治理
- Build、Test、Image、Scan、Deploy
- DORA 四指标
- Java 服务上线前后需要关注的验证点

## 与现有笔记的关系

- DevOps 导航：[[MOC-Harness与DevOps]]
- 平台工具对比：[[Harness vs Jenkins对比]]
- 平台概念总览：[[Harness是什么-企业CI-CD平台]]
- 核心概念：[[Harness核心概念详解]]
- Java 总导航：[[MOC-Java学习]]
- AI / DevOps 交叉话题：[[定时任务驱动AI-Coding]]

## 建议先挂回来的资料

- 先用 [[Harness是什么-企业CI-CD平台]] 建立“从代码到部署”的平台全景。
- 再看 [[Harness核心概念详解]]，把 Pipeline、Delegate、持续验证和 GitOps 这些词挂到交付链上。
- 对比思路补到 [[Harness vs Jenkins对比]]，方便回答“为什么企业要从 Jenkins 迁移”。
- 如果要把 AI Agent 放进交付链，可回看 [[定时任务驱动AI-Coding]] 里的 CI/CD 类比。

## 建议的整理顺序

1. 先把 Build -> Test -> Image -> Deploy -> Verify -> Rollback 讲顺。
2. 再把 Docker / K8s / 探针 / 灰度发布这些运行时概念挂进去。
3. 最后用 Harness / Jenkins 对比补上治理、审计、DORA 指标和回滚表达。

## 面试里建议怎么说

- 不必把自己包装成 K8s 专家，但要能讲清 Java 服务怎么被构建、部署、探活和回滚。
- 回答时优先讲后端视角：配置、依赖、启动、健康检查、资源限制、发布验证。
- 如果没做过生产集群，也可以结合本地 Docker Compose 和平台学习路线说明理解框架。

## 后续补充清单

- [ ] Spring Boot 服务 Dockerfile 模板
- [ ] Deployment / Service / Ingress 速记
- [ ] 健康检查与灰度发布表达
- [ ] CI/CD 面试问答

## 关联

- [[能力差距分析/高级Java开发工程师补强学习计划]]
- [[MOC-Java学习]]
- [[MOC-Harness与DevOps]]
