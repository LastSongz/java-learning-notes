# DDD领域驱动设计

> 通过领域专家与技术团队的协作，将复杂业务领域建模为清晰的结构

## 核心概念

```
┌─────────────────────────────────────────────────────────────┐
│                    DDD分层架构                                 │
├─────────────────────────────────────────────────────────────┤
│  战略设计                                                      │
│  ├── 限界上下文 (Bounded Context)                            │
│  ├── 通用语言 (Ubiquitous Language)                          │
│  └── 上下文映射 (Context Mapping)                            │
├─────────────────────────────────────────────────────────────┤
│  战术设计                                                      │
│  ├── 实体 (Entity)                                          │
│  ├── 值对象 (Value Object)                                  │
│  ├── 聚合 (Aggregate)                                       │
│  ├── 领域事件 (Domain Event)                                 │
│  └── 仓储 (Repository)                                       │
└─────────────────────────────────────────────────────────────┘
```

## 战略设计

### Bounded Context (限界上下文)

> "DDD通过将大型系统划分为不同的限界上下文来处理大型模型，并明确其相互关系。" — Martin Fowler

```
┌─────────────────────────────────────────────────────────────┐
│                    电商系统                                     │
├─────────────────────┬─────────────────────┬─────────────────┤
│    订单上下文        │     库存上下文        │    客户上下文     │
│   (Order Context)   │  (Inventory Context) │ (Customer)      │
├─────────────────────┼─────────────────────┼─────────────────┤
│ Order, LineItem     │ Stock, Warehouse     │ Customer, Address│
│ OrderService        │ InventoryService     │ CustomerService  │
└─────────────────────┴─────────────────────┴─────────────────┘
```

**识别限界上下文的信号**：
- 同一术语在不同团队有不同含义
- 不同团队自然负责不同部分
- 不同服务拥有不同数据

### Context Mapping Patterns

| 模式 | 描述 | 适用场景 |
|------|------|---------|
| **Shared Kernel** | 团队共享部分领域模型 | 紧密协作的团队 |
| **Customer-Supplier** | 上下游提供-消费关系 | 明确的上下游关系 |
| **Conformist** | 放弃自己的模型，采用上游模型 | 无法控制上游时 |
| **Anticorruption Layer** | 转换层保护自己的模型 | 集成外部/遗留系统 |

## 战术设计

### Entity vs Value Object

| 特征 | Entity | Value Object |
|------|--------|--------------|
| **身份** | 有唯一标识 | 无身份 |
| **相等性** | 基于ID | 基于属性值 |
| **可变性** | 通常可变 | 不可变 |
| **生命周期** | 独立跟踪 | 附属于实体 |

```typescript
// Entity - 有唯一身份
class User extends Entity<UserProps> {
    constructor(props: CreateUserProps) {
        super({ id: props.id, props });
    }
}

// Value Object - 无身份，由属性定义相等性
class Address extends ValueObject<AddressProps> {
    constructor(props: AddressProps) {
        super(props);
    }
    get city(): string { return this.props.city; }
}
```

### Aggregate (聚合)

> "聚合是一组可以视为单个单元的领域对象。外部引用只能指向聚合根。"

```typescript
// 聚合根 - 外部只能通过根访问内部对象
class Order extends AggregateRoot<OrderProps> {
    private readonly lineItems: OrderLineItem[] = [];
    
    public addLineItem(item: OrderLineItem) {
        // 业务规则在此执行
        this.lineItems.push(item);
    }
}

order.addLineItem(item);      // ✅ 正确
order.lineItems.push(item);  // ❌ 禁止！
```

### Domain Events (领域事件)

```typescript
class OrderPlacedEvent extends DomainEvent {
    constructor(props: { aggregateId: string; orderTotal: Money; customerId: string }) {
        super(props);
    }
}

class Order extends AggregateRoot<OrderProps> {
    addEvent(domainEvent: DomainEvent) {
        this._domainEvents.push(domainEvent);
    }
}
```

### Repository (仓储)

```typescript
interface OrderRepository {
    insert(order: Order): Promise<void>;
    findById(id: string): Promise<Option<Order>>;
    findAll(): Promise<Order[]>;
    delete(order: Order): Promise<boolean>;
}

class MySQLOrderRepository implements OrderRepository {
    async insert(order: Order): Promise<void> { /* MySQL实现 */ }
    async findById(id: string): Promise<Option<Order>> { /* MySQL实现 */ }
}
```

## 决策框架

```
领域复杂吗？
├── 否 → 考虑事务脚本或简单CRUD
└── 是 → 跨多个团队吗？
    ├── 否 → 单个限界上下文，应用战术DDD
    └── 是 → 多个限界上下文，先应用战略DDD
```

## 面试常考问题

### Q: 聚合根的作用是什么？为什么外部不能直接访问聚合内对象？
> 聚合根保证聚合内的一致性约束。如果外部直接修改内部对象，可能破坏业务规则。通常通过聚合根暴露的方法来操作。

### Q: 实体和值对象的本质区别是什么？
> 身份是本质区别。实体有生命周期追踪（比如订单取消后重新下单还是同一个订单），值对象无身份（如地址相同就相等）。

### Q: 什么时候不用DDD？
> 当领域非常简单（如CRUD为主的系统）或单一团队维护时，传统分层可能更简单高效。

---

标签: #DDD #领域驱动设计 #限界上下文 #实体 #聚合 #领域事件
