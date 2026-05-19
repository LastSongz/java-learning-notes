---
title: "ThoughtWorks架构师MOC"
created: 2026-05-19
updated: 2026-05-19
tags:
  - 分类/架构
  - 类型/moc
status: complete
category: java
---

# ThoughtWorks架构师 - 知识地图 (MOC)

> 本笔记库涵盖ThoughtWorks高级技术架构师岗位要求的所有核心技术栈

---

## 📚 知识模块

### [[架构设计原则]]
- [[SOLID原则]] - 单一职责、开闭、里氏替换、接口隔离、依赖反转
- [[DRY原则]] - 不要重复自己
> **面试高频**: SOLID各原则的"自检问题"是口头解释高频题

### [[DDD领域驱动设计]]
- 战略设计 - 限界上下文、通用语言、上下文映射
- 战术设计 - 实体、值对象、聚合、领域事件、仓储
> **面试高频**: "聚合根的作用是什么？"

### [[微服务架构模式]]
- 弹性模式 - 熔断器、隔板、重试、降级
- 分布式事务 - Saga、Outbox、2PC
- 数据与通信模式 - CQRS、事件溯源、API Gateway
> **面试高频**: "为什么不用2PC？Saga怎么实现？"

### [[云原生与容器化]]
- Docker - 容器、镜像、最佳实践
- Kubernetes - Pod、Service、Deployment
- Service Mesh - Istio、Linkerd
> **面试高频**: "K8s的rolling update原理？Service Mesh解决什么问题？"

### [[AI-ML工程化]]
- MLOps生命周期 - 数据管理、实验跟踪、模型注册
- 模型部署策略 - Shadow Mode、Canary、Blue-Green
- LLMOps - RAG、Fine-tuning、云AI平台
> **面试高频**: "RAG和Fine-tuning怎么选？"

### [[CI-CD与DevSecOps]]
- 流水线设计 - GitHub Actions、GitLab CI
- IaC工具 - Terraform、Pulumi、Ansible
- DevSecOps安全实践 - SAST、DAST、DORA指标
> **面试高频**: "DORA四指标是什么？你团队现在什么水平？"

### [[数据库与缓存]]
- MySQL - InnoDB、索引、查询优化
- PostgreSQL - JSONB、[[MVCC多版本并发控制]]、索引类型
- Redis - 数据结构、缓存模式、持久化
> **面试高频**: "MVCC是怎么实现的？Redis持久化选哪个？"

### [[高并发处理]]
- 连接池 - psycopg2、HikariCP
- 主从复制与读写分离
- 一致性模型
> **面试高频**: "连接池大小怎么设？主从复制延迟怎么处理？"

---

## 🗺️ 学习路径

```
建议学习顺序：

1. 编程基础 → 2. 架构原则 → 3. DDD → 4. 微服务 → 5. 云原生
     ↓              ↓            ↓           ↓           ↓
  Java/Go       SOLID/DRY    战略设计    弹性模式    Docker/K8s
                                     ↓
                               战术设计
                                     ↓
                               Saga/CQRS
```

---

## 💡 核心技术决策

| 场景 | 选择 |
|------|------|
| 微服务间事务 | [[微服务架构模式#Saga]] vs 2PC |
| 数据一致性要求高 | 强一致 vs [[高并发处理#最终一致]] |
| ML模型部署 | [[AI-ML工程化#RAG]] vs Fine-tuning |
| 容器编排 | [[云原生与容器化#Docker]] vs 直接K8s |
| IaC工具选择 | Terraform vs Pulumi vs Ansible |

---

## 📖 参考资源

### 书籍
- 《Clean Code》 - Robert C. Martin
- 《Clean Architecture》 - Robert C. Martin  
- 《Domain-Driven Design》 - Eric Evans
- 《Building Microservices》 - Sam Newman

### 官方文档
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Resilience4j](https://resilience4j.io/)
- [Terraform](https://www.terraform.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Redis Documentation](https://redis.io/documentation)

### 研究报告
- [DORA Research](https://www.devops-research.com/) - 工程技术效能
- [Martin Fowler's Bliki](https://martinfowler.com/bliki/) - 架构模式

---

标签: #ThoughtWorks #架构师 #技术栈 #学习笔记 #面试准备
