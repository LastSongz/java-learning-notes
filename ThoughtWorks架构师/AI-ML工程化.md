# AI-ML工程化

> 将机器学习模型可靠地部署到生产环境

## MLOps vs LLMOps

| 维度 | 传统MLOps | LLMOps |
|------|----------|--------|
| 输入 | 结构化数据 | 自然语言Prompt |
| 监控 | 统计漂移 | 幻觉、Token成本 |
| 版本控制 | 模型权重 | Prompt + 权重 |
| 评估 | 标准指标 | LLM-as-Judge、人工反馈 |

## MLOps生命周期

```
┌─────────────────────────────────────────────────────────────────┐
│                    MLOps 7阶段生命周期                              │
├─────────────────────────────────────────────────────────────────┤
│  Data Management → Experimentation → Model Management              │
│        ↓                   ↓                 ↓                     │
│  Deployment → Monitoring → Continuous Training → Governance       │
└─────────────────────────────────────────────────────────────────┘
```

| 阶段 | 描述 |
|------|------|
| **Data Management** | 数据收集、验证、版本管理 (DVC, lakeFS) |
| **Experimentation** | 模型开发、超参调优、实验跟踪 (MLflow, W&B) |
| **Model Management** | 版本控制、注册表 |
| **Deployment** | CI/CD流水线、部署策略 |
| **Monitoring** | 性能跟踪、漂移检测、告警 |
| **Continuous Training** | 自动重训练和模型更新 |
| **Governance** | 合规、审计、可解释性 |

### 三版本锁定

每个生产模型应锁定三个版本：

```json
{
  "model_version": "churn-v2.4",
  "code_version": "git:abc123",
  "data_version": "dvc:data/v2.4",
  "feature_version": "feast:customer_features/v3",
  "trained_at": "2026-02-10T03:00:00Z"
}
```

### MLOps成熟度模型

| 级别 | 特征 |
|------|------|
| **0** | 无MLOps - 手动流程 |
| **1** | DevOps但无MLOps - 自动化构建测试 |
| **2** | 自动化训练 - Pipeline自动化 |
| **3** | 自动化部署 - CI/CD for ML |
| **4** | 全MLOps - 策略驱动、自动化运营 |

## 模型部署策略

### 策略对比

| 策略 | 风险 | 成本 | 验证速度 | 用户影响 |
|------|------|------|---------|---------|
| **Shadow Mode** | 最低 | 2x计算 | 慢 | 无 |
| **Canary** | 低 | 中等 | 中等 | 小% |
| **A/B Testing** | 中等 | 中等 | 快 | 受控% |
| **Blue/Green** | 中 | 2x基础设施 | 即时 | 无 |

### Shadow Mode

```
用户请求 → 生产模型(v1) ──→ 响应
         └→ 影子模型(v2) ──→ 仅记录比较
```

**适用**：重大变更前的验证，无用户影响

### Canary部署

```
0% → 1% → 5% → 20% → 50% → 100%
     (每阶段监控错误率、延迟、业务指标)
```

**适用**：渐进式风险降低

### Blue-Green部署

两套相同环境，即时切换流量，零停机。

## LLMOps

### RAG架构

```
用户查询 → Embedding → 向量搜索 → Top-K文档
                                      ↓
                              Prompt模板 + 检索内容
                                      ↓
                              LLM (GPT-4, Claude, Gemini)
                                      ↓
                              响应 + 引用
```

**适用场景**：
- 知识频繁变化
- 需要可验证的响应
- 大知识库（无法fit在context中）
- 幻觉不可接受

### RAG vs Fine-tuning

| 场景 | 方案 |
|------|------|
| 知识频繁变化 | RAG |
| 需要可验证的响应 | RAG |
| 领域特定行为 | Fine-tuning |
| 小型模型，成本敏感 | Fine-tuning |
| 最佳质量 | Hybrid (RAG + Fine-tuning) |

### Fine-tuning方法对比

| 方法 | 更新参数 | 显存需求 | 速度 | 适用场景 |
|------|---------|---------|------|---------|
| **Full Fine-tune** | 所有 | 高 | 慢 | 完全控制 |
| **LoRA** | 仅适配器 | 低 | 快 | 大多数场景 |
| **QLoRA** | 适配器(4-bit) | 非常低 | 中 | 消费级GPU |

### 三大云AI平台对比

| 能力 | AWS SageMaker | Azure ML | Google Vertex AI |
|------|--------------|----------|-----------------|
| **AutoML** | Autopilot | Automated ML | AutoML Tables |
| **ML流水线** | SageMaker Pipelines | Azure ML Pipelines | Vertex Pipelines |
| **生成式AI** | Bedrock (独立) | Azure OpenAI | Gemini, Model Garden |
| **合规认证** | 100+ | 90+ | 100+ |

## 面试常考问题

### Q: RAG和Fine-tuning怎么选？
> 知识变化频繁、需要可验证性 → RAG；领域特定行为、低成本部署小型模型 → Fine-tuning。

### Q: MLOps和传统DevOps有什么区别？
> ML多了数据版本管理、模型版本管理、模型监控（漂移检测）、自动重训练等环节。

### Q: 什么是模型漂移？怎么检测？
> 模型预测质量随时间下降，通常因为数据分布变化。检测方法：监控预测分布、ground truth回传、定期评估。

### Q: Shadow Mode部署是什么原理？
> 用户请求同时打到新旧模型，但只返回新模型结果给用户，旧模型结果只记录用于比较。

## 实践检查清单

```markdown
- [ ] 模型是否有版本锁定（code/data/feature三版本）？
- [ ] 是否有模型性能监控和告警？
- [ ] 是否有数据漂移检测机制？
- [ ] 模型更新是否有CI/CD流水线自动化？
- [ ] LLM应用是否有Guardrails防止有害输出？
```

---

标签: #MLOps #LLMOps #AI工程化 #机器学习 #RAG #模型部署
