---
title: "Harness是什么-企业CI-CD平台"
created: 2026-04-26
updated: 2026-05-19
tags:
  - 分类/devops
  - 主题/harness
  - 主题/ci-cd
  - 平台
  - 面试准备
status: complete
category: devops
---

# Harness 是什么？— 企业级 CI/CD 平台

## 一句话定义

**Harness** 是一个 **AI 驱动的现代 DevOps 平台**，核心功能是自动化软件的**构建、测试、安全和部署**全流程，尤其面向企业级场景（治理合规、多云部署、微服务编排）。

---

## 📊 市场地位（2025-2026 数据）

| 指标 | 数据 |
|------|------|
| 公司估值 | **55 亿美元** |
| 年收入 (ARR) | **2.5 亿美元+**，年增长 **50%+** |
| 企业客户数 | **1,000+** |
| 年部署量 | **1.28 亿次** |
| 员工规模 | 1,000-9,999 人 |
| 行业评级 | Gartner Magic Quadrant **Leader**（连续 2 年）|
| 行业评级 | Forrester Wave DevOps Platforms **Leader**（2025 Q2）|
| Fortune 荣誉 | 2026 全美最具创新力公司 |

### CI/CD 工具市场份额对比

| 工具 | 采用率 | 趋势 |
|------|--------|------|
| GitHub Actions | 33% | 稳定，中小团队首选 |
| Jenkins | 28% | ⬇ 年下降 8% |
| GitLab CI | 19% | 稳定 |
| **Harness** | 增长最快 | ⬆ **企业级市场增速第一** |

---

## 🏗️ 平台核心模块

| 模块 | 作用 | 亮点 |
|------|------|------|
| **CI（持续集成）** | 自动构建和测试 | Test Intelligence 可提速构建 **4-8 倍** |
| **CD（持续部署）** | 自动化发布到多云/多区域 | 无脚本部署，原生 Canary/Blue-Green |
| **Feature Flags** | 功能开关、灰度发布 | 精细的流量控制 |
| **STO（安全测试）** | 安全扫描编排 | SBOM、镜像签名、漏洞去重与优先级排序 |
| **Cloud Cost Management** | 云成本监控和优化 | AI 驱动的 FinOps，已管理 **28 亿美元** 云支出 |
| **IaC** | 基础设施即代码 | Terraform 自动化 |
| **Chaos Engineering** | 混沌工程 | 系统韧性测试 |

---

## 🏢 知名企业客户案例

### 金融行业（合规刚需）
| 公司 | 成果 |
|------|------|
| **花旗银行 (Citi)** | 20,000 工程师，部署时间 **几天 → 7 分钟** |
| **Experian** | 发布频率提升 **50 倍** |
| **澳洲国民银行 (NAB)** | 构建失败率降低 **67%** |
| **Swedbank** | Feature Flags 实现更频繁部署 |

### 航空 / 零售 / 科技
| 公司 | 成果 |
|------|------|
| **United Airlines** | 部署速度提升 **75%**，微服务转型 |
| **Morningstar** | 合规模板化，开发者自助服务 |
| **Ulta Beauty** | 部署量提升 **50 倍** |
| **Twilio** | 快速产品实验 |

### 成本节省案例
| 公司 | 节省金额 |
|------|----------|
| **Raisin**（从 Jenkins 迁移） | 年省 **52.5 万美元** |
| **MakerBot**（替换 Spinnaker） | 省 **27.5 万美元** |
| **The Warehouse Group** | 交付周期 **120 小时 → 1 小时**（99% 缩减）|

---

## 🌏 为什么越来越多招聘要求 Harness？

### 根本原因：Jenkins 在衰退，企业在集体迁移

1. **Jenkins 维护成本爆炸** — 大企业需要 2-5 个工程师专门维护 Jenkins
2. **合规治理需求** — 金融/医疗行业的审计追踪、策略管控，Jenkins 原生不支持
3. **AI 驱动的 DevOps** — Harness 的 AI 自动回滚、智能测试选择是竞品没有的
4. **多云/微服务复杂性** — 企业微服务架构越复杂，越需要平台化交付
5. **平台工程趋势** — 从"工具拼装"走向"平台化交付"

### 什么样的公司会要求 Harness？

| 公司类型 | 原因 |
|----------|------|
| 外企 / 跨国大厂 | 合规治理、多云、总部统一平台 |
| 金融 / 银行 | 审计追踪、安全扫描、策略管控 |
| 大中型互联网公司 | 微服务规模大、Jenkins 维护成本高 |
| DevOps 平台团队 | 内部开发者平台，标准化交付流水线 |
| Jenkins 迁移期企业 | 需要"懂两边"的人 |

> 💡 **看到招聘要求 Harness → 该公司工程成熟度不低**，至少是中大型企业或重视 DevOps 的团队。

---

## 📚 认证体系

Harness 提供**免费**的 Developer 级别认证：

| 级别 | 费用 | 说明 |
|------|------|------|
| **Developer** | **免费** | 90 分钟在线考试 |
| Administrator | $50 | 配置与管理 |
| Architect | 付费 | 架构级设计 |

> 💡 建议去 [Harness University](https://university.harness.io/) 免费考一个 Developer 认证，直接写在简历上。
考试已完成：
证书：
repo
https://verify.skilljar.com/c/43z7s9m5zart
CI
https://verify.skilljar.com/c/34omcaoe8e27
CD
https://verify.skilljar.com/c/yv5xh7ekon4g

---

## 🔗 相关笔记

- [[Harness核心概念详解]] — 深入理解 Pipeline、Delegate 等核心概念
- [[Harness vs Jenkins对比]] — 为什么要从 Jenkins 迁移
- [[Harness面试高频问题]] — 面试速查问答
