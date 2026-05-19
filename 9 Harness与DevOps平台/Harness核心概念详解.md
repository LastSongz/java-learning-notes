---
title: "Harness核心概念详解"
created: 2026-04-26
updated: 2026-05-19
tags:
  - 分类/devops
  - 主题/harness
  - 主题/ci-cd
  - 核心概念
  - 主题/pipeline
status: complete
category: devops
---

# Harness 核心概念详解

> 面试中需要掌握的 5 个 Harness 核心概念

---

## 1️⃣ Pipeline（流水线）

### 是什么
Pipeline 是 Harness 中定义**从代码到生产**整个交付流程的核心单元。类似 Jenkins 的 Jenkinsfile，但更现代化。

### 核心特点
- **可视化 + YAML 双模式编辑** — 不会 YAML 也能用图形界面拖拽配置
- **Pipeline-as-Code** — 所有配置可存入 Git，版本化管理
- **模板化** — 一个模板可被上百个服务复用（Morningstar 把 36,000 个 pipeline 合并为 50 个模板）

### 结构
```
Pipeline
├── Stage（阶段）
│   └── Step（步骤）
│       ├── Run（执行脚本）
│       ├── Build（构建）
│       ├── Deploy（部署）
│       └── Approval（审批门禁）
├── Variables（变量）
└── Connectors（连接器：连接云/K8s/Git 等）
```

### 与 Jenkins 的区别
| 维度 | Jenkins | Harness |
|------|---------|---------|
| 配置方式 | Groovy 脚本（Jenkinsfile）| YAML + 可视化 |
| 模板复用 | 需要写 Shared Library | 原生模板系统 |
| 多服务编排 | 困难 | 原生支持 |
| 学习曲线 | 陡峭（Groovy） | 平缓 |

---

## 2️⃣ Delegate（代理）

### 是什么
Delegate 是 Harness 安装在你环境（K8s 集群 / Docker / 服务器）中的**轻量级代理**。它是 Harness 云端控制面与你本地基础设施之间的"桥梁"。

### 工作原理
```
Harness SaaS（云端）
    ↕（加密通信）
Delegate（你的 K8s/Docker 中）
    ↕
你的基础设施（AWS/GCP/Azure/K8s/VM）
```

### 核心要点
- **Harness 本身不直接访问你的基础设施** — 所有操作通过 Delegate 执行
- **自动弹性扩缩** — 根据 pipeline 负载自动扩缩 Delegate 数量
- **安全模型** — 你的凭证（云密钥、K8s token）始终留在你的环境中，不会传到 Harness 云端
- **部署模式**：
  - **集中式** — 标准部署，统一管理
  - **分布式** — 多业务单元、网络隔离场景
  - **环境隔离** — 生产/非生产严格分离

### 面试怎么说
> "Delegate 是 Harness 在客户环境中的轻量代理，负责执行所有基础设施操作。它的好处是凭证不出环境，满足企业安全要求。"

---

## 3️⃣ Continuous Verification（持续验证 + AI 自动回滚）

### 是什么
这是 Harness 最具差异化的功能。部署完成后，Harness **自动监控应用健康状态**，如果检测到异常，**AI 自动触发回滚**。

### 工作流程
```
部署新版本
    ↓
Continuous Verification 自动采集指标
（集成 APM：Datadog / New Relic / AppDynamics / Prometheus 等）
    ↓
AI 分析：新版本是否比旧版本更差？
    ├── 正常 → 保持部署
    └── 异常 → 自动回滚到上一版本（无需人工介入）
```

### 验证方式
| 方式 | 说明 |
|------|------|
| **Auto** | AI 自动学习基线，检测异常 |
| **Threshold** | 设定阈值（如错误率 > 5% 则回滚） |
| **Canary** | 对比金丝雀版本与基线版本的指标 |
| **Manual** | 人工判断 |

### 与传统监控的区别
| 维度 | 传统监控 + 手动回滚 | Harness CV |
|------|---------------------|------------|
| 检测速度 | 分钟到小时 | **秒级** |
| 回滚触发 | 人工 on-call | **AI 自动** |
| 误判率 | 依赖经验 | ML 基线学习 |
| 与部署集成 | 割裂 | **原生一体** |

### 面试怎么说
> "Harness 的 Continuous Verification 是部署后自动监控应用健康的机制，集成 APM 工具采集指标，通过 AI 分析判断新版本是否正常，异常时自动回滚。这比传统'监控告警 → on-call 介入 → 手动回滚'的链路快得多。"

---

## 4️⃣ Canary / Blue-Green 部署策略

### Canary（金丝雀部署）

#### 是什么
先将新版本部署到**一小部分流量**（如 5%），观察指标正常后逐步扩大流量比例，直到 100% 切换。

#### Harness 中的实现
```
1. 部署新版本到 5% 的实例
2. CV 验证 → 正常？
3. 扩大到 25% → 验证
4. 扩大到 50% → 验证
5. 全量 100% → 完成
```

- 每个阶段都有 **CV 持续验证**
- 任何阶段异常 → **自动回滚**
- 流量比例和验证时长可配置

### Blue-Green（蓝绿部署）

#### 是什么
同时维护两套完全相同的环境（蓝环境和绿环境）。当前生产流量在蓝环境，新版本部署到绿环境，验证通过后**一次性切换流量**。

#### Harness 中的实现
```
1. 当前生产：Blue 环境（承载流量）
2. 部署新版本到 Green 环境
3. CV 验证 Green 环境健康
4. 切换流量：Blue → Green
5. Green 成为新生产环境
```

- 回滚极快：**只需切回 Blue 环境**
- 旧环境可保留一段时间作为快速回退

### 两者对比

| 维度 | Canary | Blue-Green |
|------|--------|------------|
| 风险暴露 | 小（逐步放量）| 一刀切 |
| 资源消耗 | 低（增量） | 高（双环境）|
| 回滚速度 | 需逐步缩容 | **秒级切回** |
| 适用场景 | 大规模微服务 | 关键业务、需要秒级回滚 |
| Harness 支持 | ✅ 原生 | ✅ 原生 |

### 面试怎么说
> "Canary 部署是逐步放量、持续验证的策略，风险可控但需要时间；Blue-Green 是双环境切换，回滚最快但资源成本高。Harness 对两种策略都有原生支持，并且每个阶段都配合 Continuous Verification 做自动健康检查。"

---

## 5️⃣ GitOps 集成

### 是什么
GitOps 是一种将 **Git 仓库作为基础设施和应用部署唯一事实来源** 的实践。Harness 与主流 GitOps 工具深度集成。

### Harness 的 GitOps 能力

| 能力 | 说明 |
|------|------|
| **ArgoCD 集成** | 集中管理多个 ArgoCD 实例 |
| **Flux 集成** | 支持 Flux 作为 GitOps 引擎 |
| **统一视图** | 一个面板看所有 GitOps 集群状态 |
| **Git 仓库同步** | 配置变更自动同步到 Git |
| **审计追踪** | 所有部署操作有完整记录 |

### 为什么 Harness + GitOps 而不是单独用 ArgoCD？

企业的痛点（Argo Sprawl）：
- 多个团队各自搭 ArgoCD → 管理混乱（Argo Sprawl）
- 缺乏统一治理和 RBAC
- 没有与 CI/测试/安全扫描联动

Harness 的解决方式：
```
ArgoCD 负责底层 GitOps 同步
Harness 负责：CI → 测试 → 安全扫描 → 触发 ArgoCD → 持续验证 → 审计
= 全链路闭环
```

### 面试怎么说
> "GitOps 的核心思想是用 Git 作为部署的唯一真相来源。Harness 与 ArgoCD/Flux 深度集成，但不仅是包一层 UI——它把 CI、测试、安全扫描、部署验证、审计全串起来，解决了企业中 ArgoCD 多实例管理混乱（Argo Sprawl）的问题。"

---

## 🔗 相关笔记

- [[Harness是什么-企业CI-CD平台]] — 平台全貌和市场背景
- [[Harness vs Jenkins对比]] — 与传统工具的核心差异
- [[Harness面试高频问题]] — 面试速查问答
