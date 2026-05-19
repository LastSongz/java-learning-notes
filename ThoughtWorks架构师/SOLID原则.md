---
title: "SOLID原则"
created: 2026-05-19
updated: 2026-05-19
tags:
  - 分类/架构
  - 主题/solid
status: complete
category: java
---

# SOLID原则

> Robert C. Martin 提出的五个软件设计原则

## 五大原则

### 1. SRP - 单一职责原则
> "每个软件模块应该只有一个且只有一个需要变更的原因。"

```java
// ❌ 反例：多个职责混合
public class Employee {
    public Money calculatePay() { }      // HR/财务职责
    public void save() { }               // 数据库职责
    public String reportHours() { }      // 审计职责
}

// ✅ 正例：职责分离
public class PayCalculator { }           // 只负责薪酬计算
public class EmployeeRepository { }      // 只负责数据持久化
public class HoursReporter { }           // 只负责报表
```

### 2. OCP - 开闭原则
> "软件实体应该对扩展开放，对修改关闭。"

```java
// ❌ 反例：添加新形状需要修改现有代码
public double calculateArea(Object shape) {
    if (shape instanceof Circle) { /* ... */ }
    else if (shape instanceof Rectangle) { /* ... */ }
    else if (shape instanceof Triangle) { /* 必须修改 */ }
    return 0;
}

// ✅ 正例：扩展无需修改
public interface Shape {
    double calculateArea();
}

public class Circle implements Shape { /* ... */ }
public class Rectangle implements Shape { /* ... */ }
// 新增Triangle只需创建新类，无需修改现有代码
```

### 3. LSP - 里氏替换原则
> "子类型必须能够替换其基类型而不破坏程序。"

```java
// ❌ 反例：Square继承Rectangle违反了LSP
public class Square extends Rectangle {
    @Override
    public void setWidth(int width) {
        this.width = width;
        this.height = width;  // 修改width同时也修改height
    }
}

// 调用方期望宽高独立，但Square不符合预期
Rectangle rect = new Square();
rect.setWidth(5);
rect.setHeight(10);
rect.getArea();  // 期望50，实际100！

// ✅ 正例：分开层次
public interface Quadrilateral { int getArea(); }
public class Rectangle implements Quadrilateral { }
public class Square implements Quadrilateral { }
```

### 4. ISP - 接口隔离原则
> "客户端不应该被迫依赖它不使用的接口。"

```java
// ❌ 反例：胖接口
public interface Machine {
    void print(Document d);
    void scan(Document d);
    void fax(Document d);
    void staple(Document d);
}

public class SimplePrinter implements Machine {
    public void scan(Document d) { throw new NotSupportedException(); }
    public void fax(Document d) { throw new NotSupportedException(); }
}

// ✅ 正例：按职责拆分为小接口
public interface Printable { void print(Document d); }
public interface Scannable { void scan(Document d); }
public interface Faxable { void fax(Document d); }

public class SimplePrinter implements Printable { }
public class OfficePrinter implements Printable, Scannable, Faxable { }
```

### 5. DIP - 依赖反转原则
> "高层模块不应该依赖低层模块，两者都应该依赖抽象。"

```java
// ❌ 反例：高层直接依赖低层
public class OrderProcessor {
    private MySQLOrderRepository repository = new MySQLOrderRepository();
    private SendGridEmailService emailService = new SendGridEmailService();
}

// ✅ 正例：依赖抽象（接口）
public interface OrderRepository { void save(Order order); }
public interface EmailService { void sendConfirmation(Order order); }

public class OrderProcessor {
    private final OrderRepository repository;
    private final EmailService emailService;
    
    public OrderProcessor(OrderRepository repository, EmailService emailService) {
        this.repository = repository;
        this.emailService = emailService;
    }
}

// 低层实现接口
public class MySQLOrderRepository implements OrderRepository { /* ... */ }
public class PostgreSQLOrderRepository implements OrderRepository { /* ... */ }
```

## 快速参考

| 原则 | 核心问题 | 自检问题 |
|------|---------|---------|
| **SRP** | 单一职责 | 这个类只有一个原因需要变更吗？ |
| **OCP** | 对扩展开放 | 能添加功能而不改变现有代码吗？ |
| **LSP** | 可替换性 | 子类替换基类后行为一致吗？ |
| **ISP** | 接口专注 | 客户端被迫依赖无用方法吗？ |
| **DIP** | 依赖抽象 | 业务逻辑依赖具体实现吗？ |

## 面试常考问题

### Q: 举例说明你如何在项目中应用SOLID？
> 结合实际项目经验，举例说明。比如："订单服务原本是个2000行的类，我按SRP拆成了OrderService、OrderValidator、OrderRepository..."

### Q: SOLID五个原则哪个最重要？
> 没有标准答案。可以说DIP是其他原则的基础，因为一旦依赖抽象，很多设计决策会更清晰。

### Q: 违背LSP有什么实际风险？
> 可能导致运行时异常、计算结果错误，或需要大量条件判断。

---

标签: #SOLID #单一职责 #开闭原则 #里氏替换 #接口隔离 #依赖反转
