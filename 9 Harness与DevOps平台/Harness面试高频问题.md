---
title: "Harness面试高频问题"
created: 2026-04-26
updated: 2026-05-19
tags:
  - 分类/devops
  - 主题/harness
  - 分类/面试
  - 主题/ci-cd
status: complete
category: devops
---

# Harness 面试高频问题

> Q&A 格式，覆盖面试中关于 Harness 的常见问题

---

## Q1：Harness 是什么？

**Harness** 是一个 AI 驱动的现代 DevOps 平台，提供 CI（持续集成）、CD（持续部署）、安全测试、Feature Flags、云成本管理等模块。核心解决的是**从代码提交到生产部署全流程的自动化**问题，尤其面向企业级场景（治理合规、多云部署、微服务编排）。

> 加分：提一下"2025 年 Forrester Wave 评的 Leader"或"花旗银行用它把部署从几天缩到 7 分钟"。

---

## Q2：为什么你们公司选择 Harness 而不是继续用 Jenkins？

三个核心原因：

1. **维护成本** — Jenkins 需要专职团队维护插件兼容性，Harness 是低维护的 SaaS 架构
2. **治理合规** — 我们行业有审计要求，Harness 有原生的 RBAC、Policy-as-Code 和完整审计追踪
3. **部署策略** — 我们微服务多，需要 Canary 部署和 AI 自动回滚，Harness 原生支持

> 加分：提一下"Jenkins 的插件地狱"（Plugin Hell）这个说法。

---

## Q3：Harness 的 Delegate 是什么？为什么需要它？

Delegate 是安装在我们环境（K8s 集群或服务器）中的**轻量级代理**。

- Harness SaaS 不直接访问我们的基础设施，所有操作通过 Delegate 执行
- **安全优势**：凭证（云密钥、K8s token）始终留在我们环境中，不传到 Harness 云端
- 支持自动弹性扩缩，根据 pipeline 负载自动增减 Delegate 数量

> 一句话总结：**"Delegate 是 Harness 在客户环境中的安全代理，凭证不出环境。"**

---

## Q4：什么是 Continuous Verification？怎么工作的？

Continuous Verification（CV）是 Harness 最具差异化的功能：

1. 部署新版本后，CV **自动采集 APM 指标**（Datadog、New Relic、Prometheus 等）
2. AI 分析新版本是否比旧版本表现更差
3. 如果检测到异常 → **自动触发回滚**，无需人工介入
4. 验证方式有：Auto（AI 自动学习基线）、Threshold（阈值对比）、Canary（版本对比）

> 对比传统方式："监控告警 → on-call 被叫醒 → 人工判断 → 手动回滚"，CV 是秒级自动完成。

---

## Q5：Canary 部署和 Blue-Green 部署有什么区别？

| 维度 | Canary（金丝雀）| Blue-Green（蓝绿）|
|------|-----------------|-------------------|
| **方式** | 逐步放量（5% → 25% → 50% → 100%）| 双环境，一刀切换 |
| **风险** | 低（每次只暴露一小部分流量）| 切换瞬间全量暴露 |
| **回滚** | 需逐步缩容 | **秒级切回旧环境** |
| **资源** | 增量资源 | 需要双倍环境 |
| **适用** | 大规模微服务 | 关键业务、要求秒级回滚 |

> Harness 对两种策略都有原生支持，每个阶段配合 CV 做自动健康检查。

---

## Q6：Harness 怎么与 GitOps 集成？

Harness 与 **ArgoCD / Flux** 深度集成，但不仅是包一层 UI：

- 集中管理多个 ArgoCD 实例（解决 Argo Sprawl 问题）
- 提供 CI → 测试 → 安全扫描 → 触发 ArgoCD → 持续验证 → 审计的**全链路闭环**
- Git 仓库作为唯一事实来源，所有配置变更自动同步

> 解决的核心问题：企业用 ArgoCD 经常出现多团队各自搭建、管理混乱的问题，Harness 做统一治理。

---

## Q7：Harness 的 Test Intelligence 是什么？

Test Intelligence 是 Harness CI 的核心优化功能：

- **智能选择测试**：不是每次全量跑所有测试，而是根据代码变更的影响范围，只跑相关的测试
- **效果**：构建速度提升 **4-8 倍**
- 原理：通过分析代码依赖关系和测试历史数据，选择最小必要测试集

> 对比 Jenkins：每次全量跑测试，没有智能优化机制。

---

## Q8：什么是 Policy-as-Code？Harness 怎么实现的？

Policy-as-Code 是用代码（而非人工审批）来定义和执行组织策略。

Harness 集成 **OPA（Open Policy Agent）**，使用 **Rego 语言** 编写策略：

- 限制谁能部署到生产环境
- 强制所有部署必须通过安全扫描
- 要求部署前有审批流程
- 所有策略版本化管理，存入 Git

> 对比 Jenkins：没有原生 Policy-as-Code，靠插件和 Groovy 脚本勉强实现。

---

## 💡 面试加分话术

### 当被问到"你了解 Harness 吗？"
> "了解。Harness 是 AI 驱动的 DevOps 平台，核心差异化在于 Continuous Verification——部署后 AI 自动监控应用健康，异常时自动回滚。我特别关注它的 Delegate 架构，凭证不出客户环境，这对金融行业的合规很重要。"

### 当被问到"你觉得 Harness 和 Jenkins 哪个好？"
> "看场景。Jenkins 适合小团队、简单场景，开源免费但维护成本随规模指数增长。Harness 适合中大型企业，特别是有合规需求、多云部署、微服务架构的团队。很多企业从 Jenkins 迁移到 Harness，主要驱动力是维护成本、治理合规和部署效率。"

---

## 🔗 相关笔记

- [[Harness是什么-企业CI-CD平台]] — 平台全貌和市场背景
- [[Harness核心概念详解]] — 核心概念深度解释
- [[Harness vs Jenkins对比]] — 详细对比分析
- [[MOC-Java面试]] — 面试知识体系导航
