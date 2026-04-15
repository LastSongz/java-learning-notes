# CI-CD与DevSecOps

> 持续集成、持续交付与安全实践

## 流水线设计

### 核心阶段

| 阶段 | 目标时间 | 工具示例 |
|------|---------|---------|
| Build | < 2分钟 | Maven, Gradle, npm |
| Lint | < 1分钟 | ESLint, Prettier |
| Unit Tests | < 5分钟 | Jest, JUnit, PyTest |
| Security Scan | < 2分钟 | Semgrep, CodeQL |
| Deploy | < 5分钟 | ArgoCD, Jenkins |

### GitHub Actions示例

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run build

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
```

### GitOps模式

```
开发者Push/PR → Git仓库 → ArgoCD/Flux → Kubernetes集群
                              ↑
                    自动同步声明式配置
```

## IaC工具对比

| 工具 | 语言 | 模型 | 状态管理 | 适用场景 |
|------|------|------|---------|---------|
| **Terraform** | HCL | 声明式 | 远程锁定 | 运营团队 |
| **Pulumi** | Python/TS/Go | 混合 | 加密远程 | 开发团队 |
| **Ansible** | YAML | 声明式 | 无集中状态 | 配置管理 |

### Terraform示例

```hcl
terraform {
  required_version = ">= 1.5.0"
  backend "s3" {
    bucket = "myorg-terraform-state"
    key    = "prod/networking/terraform.tfstate"
  }
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
  
  name = "production-vpc"
  cidr = var.vpc_cidr
  
  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
}
```

## 测试策略

### 测试金字塔

```
        /\
       /  \      E2E (5-10%)
      /----\     集成测试 (20-30%)
     /      \
    /--------\   单元测试 (70%)
```

### TDD循环

```
RED: 写一个失败的测试
GREEN: 写最小代码通过测试
REFACTOR: 改进代码保持测试通过
```

### Contract Testing (契约测试)

```javascript
// Pact 示例
const Interaction = require('@pact-foundation/pact').Interaction;
const { eachLike, like } = require('@pact-foundation/pact').Matchers;

provider.addInteraction(
  new Interaction()
    .given('a user with id 1 exists')
    .uponReceiving('a request for user 1')
    .withRequest({
      method: 'GET',
      path: '/users/1'
    })
    .willRespondWith({
      status: 200,
      body: {
        id: like(1),
        name: like('Alice')
      }
    })
);
```

## DevSecOps

### 安全左移架构

```
开发者Push/PR → CI/CD流水线
                      │
      ┌───────────────┴─────────────────────┐
      │         安全门控 (全部必须通过)       │
      │                                        │
      │  1. Secrets扫描 (Gitleaks)    ← 30s  │
      │  2. 依赖审计 (Trivy)          ← 2m   │
      │  3. SAST (Semgrep)           ← 3-10m │
      │  4. 容器扫描 (Trivy)          ← 2m    │
      │  5. IaC扫描 (Checkov)        ← 1m    │
      └───────────────────────────────────────┘
```

### 安全工具链

| 层级 | 工具 |
|------|------|
| Pre-commit | Gitleaks, TruffleHog |
| SAST | Semgrep, CodeQL |
| SCA | Snyk, Dependabot, Trivy |
| Container | Trivy, Docker Scout |
| IaC | Checkov, tfsec |
| Policy | OPA, Sentinel |

### Secrets管理

- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Kubernetes Secrets (仅用于不敏感数据)

## DORA指标

| 指标 | 精英级 | 高 | 中 | 低 |
|------|--------|-----|-----|-----|
| **部署频率** | 多次/天 | 每天-每周 | 每周-每月 | 每月以下 |
| **变更前置时间** | < 1小时 | 1天-1周 | 1周-1月 | 1-6月 |
| **变更失败率** | 0-15% | 16-30% | 16-30% | 46-60% |
| **MTTR** | < 1小时 | < 1天 | < 1天 | > 1周 |

## 面试常考问题

### Q: DORA四指标是什么？你团队现在什么水平？
> 部署频率、变更前置时间、变更失败率、MTTR。结合自己团队实际情况回答。

### Q: IaC的state文件是什么？为什么重要？
> Terraform用state文件记录实际基础设施状态，用于规划后续变更。没有state或state损坏会导致"漂移"。

### Q: 如何防止secrets提交到代码库？
> 使用pre-commit hook (Gitleaks)、CI/CD中扫描、IDE插件提示。

### Q: TDD和测试金字塔是什么关系？
> TDD是开发方法论，测试金字塔是测试策略。TDD通常产出单元测试，配合集成测试和E2E形成金字塔。

## 实践检查清单

```markdown
- [ ] CI流水线是否在15分钟内完成？
- [ ] 是否有自动化安全扫描门控？
- [ ] 部署是否支持一键回滚？
- [ ] IaC配置是否版本控制？
- [ ] Secrets是否用专用工具管理而非写在代码里？
```

---

标签: #CI/CD #DevOps #DevSecOps #Terraform #IaC #DORA #安全
