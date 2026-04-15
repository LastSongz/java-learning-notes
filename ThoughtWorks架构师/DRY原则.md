# DRY原则 (Don't Repeat Yourself)

> "系统中的每条知识都必须有单一、明确、权威的表示。" — Andy Hunt & Dave Thomas

## 核心概念

DRY原则来自《The Pragmatic Programmer》，强调消除重复的知识和意图。

## 代码示例

### ❌ 反例：重复的验证逻辑

```java
public void createUser(User user) {
    if (user.name == null || user.name.isEmpty()) {
        throw new ValidationException("Name is required");
    }
    if (user.email == null || !user.email.contains("@")) {
        throw new ValidationException("Valid email is required");
    }
}

public void updateUser(User user) {
    if (user.name == null || user.name.isEmpty()) {  // 重复！
        throw new ValidationException("Name is required");
    }
    if (user.email == null || !user.email.contains("@")) {  // 重复！
        throw new ValidationException("Valid email is required");
    }
}
```

### ✅ 正例：单一知识来源

```java
public class UserValidator {
    public void validate(User user) {
        if (user.name == null || user.name.isEmpty()) {
            throw new ValidationException("Name is required");
        }
        if (user.email == null || !user.email.contains("@")) {
            throw new ValidationException("Valid email is required");
        }
    }
}

public class UserService {
    private final UserValidator validator;
    
    public void createUser(User user) {
        validator.validate(user);  // 单一来源
    }
    
    public void updateUser(User user) {
        validator.validate(user);  // 复用
    }
}
```

## DRY不仅仅是代码

> "DRY是关于知识、意图的重复。不是关于代码的重复。"

| 知识类型 | 示例 |
|---------|------|
| **业务规则** | 折扣策略、验证逻辑 |
| **数据库Schema** | 表结构定义一次 |
| **配置** | 环境特定的值 |
| **文档** | 重复代码的文档 |

## DRY vs AHA原则

| DRY | AHA (Avoid Hasty Abstractions) |
|-----|------|
| 消除重复 | 不要过早抽象 |
| 等待第三次重复 | 宁可重复也不要错误抽象 |
| 单一信息源 | 有时重复更便宜 |

---

标签: #DRY #不要重复 #抽象 #代码质量
