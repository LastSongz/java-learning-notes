---
tags: #redis #mq #中间件 #面试 #运达
---

# 中间件专题：Redis 与 MQ

> 本笔记为运达公司面试专项准备，系统整合 Redis 缓存与消息队列核心知识点

---

## 一、Redis 五大数据结构及底层编码

Redis 之所以高性能，很大程度上得益于其高效的数据结构实现。Redis 5.0 版本前提供了五大基本数据结构，5.0 后又新增了 Stream，下面逐一解析。

### 1.1 String（字符串）

String 是 Redis 最基本的数据结构，采用 **SDS（Simple Dynamic String）** 实现，相比 C 原生字符串具有以下优势：

- **O(1) 复杂度获取字符串长度**（C 字符串需要遍历）
- **防止缓冲区溢出**（自动扩展空间）
- **减少修改时的内存重分配**（空间预分配、惰性释放）

**底层编码有三种形式**：

| 编码 | 存储形式 | 触发条件 |
|------|----------|----------|
| int | 64位整数 | 存储的是整数且值在 8 字节范围内 |
| embstr | embstr 编码的 SDS | 字符串长度 ≤ 44 字节 |
| raw | raw 编码的 SDS | 字符串长度 > 44 字节 |

> 为什么是 44 字节？Redis 对象头（sdshdr + redisObject）共 56 字节，jemalloc 以 64 字节为边界分配，44 + 56 = 120，恰好跨过 64 字节边界，所以 44 是 embstr 的上限。

**典型应用场景**：缓存 JSON 序列化对象、分布式锁的 value、计数器、Session 共享。

### 1.2 List（列表）

List 在 Redis 3.2 之前使用 **ziplist（压缩列表）** 或 **linkedlist（双向链表）** 两种实现，3.2 后统一使用 **quicklist**。

**quicklist 本质是 ziplist + linkedlist 的组合**：

- 每个 quicklist 节点是一个 ziplist
- ziplist 节点过多时自动转换为 linkedlist
- 兼顾内存效率和插入删除性能

**3.2 版本引入 listpack 替代 ziplist**，主要解决了 ziplist 级联更新的问题。listpack 通过将 entry 长度存储在 entry 自身而非前一个 entry 中，避免了连锁更新。

**典型应用场景**：消息队列（简单场景）、最新消息列表、粉丝列表（需分页时慎用）。

### 1.3 Hash（哈希）

Hash 采用 **ziplist** 或 **hashtable** 两种编码：

**转换条件**（两个条件满足任意一个即转换）：

| 条件 | 阈值 |
|------|------|
| 字段数量 | > 512 |
| 单个字段 value 长度 | > 64 字节 |

**hashtable 实现**：
- 字典（dict）结构，包含两个哈希表
- 渐进式 rehash，避免阻塞
- 采用链地址法解决哈希冲突

**典型应用场景**：存储对象属性（如用户信息）、购物车商品列表。

### 1.4 Set（集合）

Set 采用 **intset** 或 **hashtable** 两种编码：

**转换条件**：
- 所有元素都是整数
- 元素数量 ≤ 512

**intset（整数集合）**：
- 连续内存存储，内存效率高
- 支持升级：int16_t → int32_t → int64_t
- 不支持降级

**典型应用场景**：标签系统、去重、抽奖、好友关系（求交集/并集）。

### 1.5 ZSet（有序集合）

ZSet 是 Redis 最复杂的数据结构，采用 **ziplist** 或 **skiplist + hashtable** 两种实现：

**转换条件**：
- 元素数量 ≤ 128
- 单个元素长度 ≤ 64 字节

**skiplist（跳表）实现**：
- 多层索引结构，查找时间复杂度 O(logN)
- 配合 hashtable 实现 O(1) 查找 member 对应的 score
- 相比平衡树实现更简单，插入效率更高

**典型应用场景**：排行榜、延时队列（score 为执行时间戳）、权重队列。

### 1.6 补充数据结构

除五大基本类型外，Redis 还提供了以下高级数据结构：

| 数据结构 | 加入版本 | 说明 | 典型应用 |
|----------|----------|------|----------|
| Stream | 5.0 | 消息队列，支持消费者组 | 替代 List 的消息队列 |
| HyperLogLog | 2.8 | 基数统计 | UV 统计 |
| Bitmap | 2.2 | 位图 | 签到、活跃用户统计 |
| GEO | 3.2 | 地理位置 | 附近的人、滴滴打车 |

**Stream 特别说明**：
- 类似于 Kafka 的消费者组模型
- 支持 ACK 确认、PENDING 列表、消息 ID 可自定义
- 适合实现可靠消息队列

---

## 二、Redis 缓存三大问题

缓存的使用带来了三大经典问题，这是面试中的高频考点。

### 2.1 缓存穿透

**问题描述**：查询一个不存在的数据，由于缓存和数据库都不存在，每次请求都会打到数据库。

**危害**：大量不存在的数据请求会击垮数据库。

**解决方案**：

**方案一：缓存空值**
```
# 当查询数据库也为空时，缓存一个空值
if (db.query(key) == null) {
    redis.setex(key, 5分钟, "");
}
```
- 优点：实现简单
- 缺点：空值也占用缓存空间，需要设置较短 TTL

**方案二：布隆过滤器（推荐）**
- 使用 Redis 的 bitmap 或独立布隆过滤器组件
- 将所有存在的 key 存入布隆过滤器
- 查询前先检查布隆过滤器，存在的 key 才查缓存和数据库
- 优点：空间效率高，性能好
- 缺点：存在误判（false positive），不存在可能被误判为存在

**方案三：增强参数校验**
- 对请求参数进行基础校验
- 拦截明显恶意的无效请求

### 2.2 缓存击穿

**问题描述**：某个热点 Key 过期瞬间，大量请求同时涌入，直接打到数据库。

**解决方案**：

**方案一：互斥锁（分布式锁）**
```java
String value = redis.get(key);
if (value == null) {
    // setnx 加锁
    if (redis.setnx(lockKey, "1", 10, TimeUnit.SECONDS)) {
        // 查数据库并写入缓存
        value = db.query(key);
        redis.setex(key, expireTime, value);
        redis.del(lockKey);
    } else {
        // 等待后重试
        Thread.sleep(50);
        return redis.get(key);
    }
}
```
- 优点：保证一致性
- 缺点：性能有所下降

**方案二：逻辑过期（不设置 TTL）**
- key 永不过期，但 value 中包含逻辑过期时间字段
- 查询时检查逻辑过期时间
- 如果已过期，则开启异步线程更新缓存，同时返回旧数据
- 优点：用户体验好，旧数据仍可用
- 缺点：数据一致性稍差

### 2.3 缓存雪崩

**问题描述**：大量 Key 同时过期，或缓存服务宕机，导致大量请求打到数据库。

**解决方案**：

**方案一：过期时间加随机值**
```java
// 原：expireTime = 3600;
// 改：expireTime = 3600 + random.nextInt(300);
redis.set(key, value, expireTime + ThreadLocalRandom.current().nextInt(300));
```

**方案二：多级缓存**
- L1 本地缓存（如 Caffeine） + L2 Redis + 数据库
- 本地缓存作为缓冲区，减轻 Redis 压力

**方案三：熔断降级**
- 使用 Sentinel 或 Hystrix 实现熔断
- 缓存不可用时走数据库降级逻辑

**方案四：构建高可用 Redis 集群**
- Sentinel 哨兵模式
- Cluster 集群模式

**方案五：请求限流**
- 对数据库请求进行限流
- 保护数据库不被击垮

---

## 三、Redis 持久化

Redis 支持两种持久化机制：RDB 和 AOF，各有优劣，也可混合使用。

### 3.1 RDB（Redis Database）

**原理**：定时对内存数据进行快照，生成dump.rdb文件。

**触发方式**：
- **定时触发**：配置 `save 900 1`（900秒内至少1个key变化则触发）
- **手动触发**：`BGSAVE`（后台异步）或 `SAVE`（同步，会阻塞）
- **shutdown 时自动触发**

**实现机制**：
- fork 子进程（Copy-On-Write机制）
- 子进程遍历内存数据写入 RDB 文件
- 父进程继续处理请求

**优缺点**：

| 优点 | 缺点 |
|------|------|
| 恢复速度快 | 可能丢失最近一次快照后的数据 |
| 文件紧凑（压缩） | fork 子进程消耗内存 |
| 适合备份/灾难恢复 | 频繁 fork 影响响应时间 |

### 3.2 AOF（Append Only File）

**原理**：将所有写命令追加到 AOF 文件末尾。

**刷盘策略**（通过 `appendfsync` 配置）：

| 策略 | 效率 | 安全性 |
|------|------|--------|
| always | 最慢 | 最高（每条命令都刷盘） |
| everysec | 较快 | 较高（每秒刷盘，最多丢1秒数据） |
| no | 最快 | 最低（依赖操作系统） |

**AOF 重写（bgrewriteaof）**：
- 合并重复命令，减小 AOF 文件体积
- 例如：`SADD key a b c` + `SADD key d e` → `SADD key a b c d e`
- 触发机制：文件大小比上次重写后的体积大于100%时自动触发

### 3.3 RDB + AOF 混合持久化（4.0+）

**工作原理**：
- RDB 快照内容 + AOF 重写期间的增量命令
- 兼顾恢复速度和数据的完整性
- 恢复时先加载 RDB，再应用 AOF 增量

**配置**：`aof-use-rdb-preamble yes`

**推荐策略**：RDB 定时备份 + AOF everysec 刷盘，适用于大多数场景。

---

## 四、Redis 高可用

Redis 高可用方案从简单到复杂分为：主从复制、哨兵模式、集群模式。

### 4.1 主从复制

**架构**：一主多从，主库负责写，从库负责读。

**同步流程**：

**1. 全量同步（PSYNC）**
```
从库 → 主库：PSYNC ? -1
主库 → 从库：FULLRESYNC {runId} {offset}
主库 → 从库：（BGSAVE + 发送 RDB 文件）
从库 → 主库：REPLCONF ACK {offset}
```

触发条件：
- 从库首次连接主库
- 从库短点（offset 不在 repl_backlog 范围内）

**2. 增量同步**
- 主库将写命令追加到 repl_backlog 缓冲区
- 从库通过 `REPLCONF ACK` 汇报已接收的 offset
- 主库只发送缺失的部分

**repl_backlog 配置**：
- `repl-backlog-size 1mb`：缓冲区大小
- 缓冲区是环形，覆盖太久会导致同步失败

**工作原理**：
- 主库 fork 子进程生成 RDB，同时将新命令写入缓冲区
- RDB 发送完毕后，主库把缓冲区内容发给从库

### 4.2 哨兵（Sentinel）模式

**哨兵职责**：
1. **监控**：检测主库和从库是否正常运行
2. **通知**：故障时发送告警
3. **自动故障转移**：从从库中选举新主库
4. **提供配置**：告诉客户端新的主库地址

**故障转移流程**：
1. 主观下线（sdown）：单个哨兵认为主库 down
2. 客观下线（odown）：多数哨兵认为主库 down
3. 选举领头哨兵（Raft 协议）：得票超过半数者当选
4. 领头哨兵从从库中选出新主库（优先级 + offset + runId）
5. 领头哨兵让其他从库执行 `replicaof` 指向新主库
6. 旧主库恢复后降级为从库

**选主规则**：
- 优先级 `replica-priority` 最高的
- offset 最新的（数据最完整）
- runId 最小的（最早启动）

### 4.3 集群（Cluster）模式

**架构**：16384 个槽位分布在多个节点上。

**核心概念**：
- **槽位（slot）**：16384 个，键通过 CRC16(key) % 16384 映射到槽位
- **Gossip 协议**：节点间通过 Gossip 协议通信，传播集群状态
- **ASK/MOVED 重定向**：客户端请求到错误节点时，返回重定向指令

**数据存储**：
- 每个主节点负责一部分槽位
- 每个主节点可以有多个从节点（副本）
- 从节点复制主节点数据，提供故障转移

**集群特点**：
- 数据分区存储，支持横向扩展
- 不支持跨槽位的批量操作（如 mget）
- 支持动态添加/删除节点

**为什么不采用一致性哈希**：
- 一致性哈希只有顺时针第一个节点负责数据，容易出现数据倾斜
- 16384 槽位是 2^14，既能保证节点均匀分布，又不会产生过多心跳包

---

## 五、Redis 多级缓存架构

结合用户简历中提到的多级缓存实践经验，本节详解生产环境中的缓存架构设计。

### 5.1 经典架构：Caffeine + Redis

**L1 本地缓存（Caffeine）**：
- 进程内缓存，访问延迟 < 1μs
- 基于 LinkedHashMap 实现，采用 W-TinyLFU 淘汰算法
- 适合存储热点数据（访问频率极高的数据）

**L2 分布式缓存（Redis）**：
- 跨进程共享
- 支持集群部署，高可用

**查询流程**：
```
请求 → L1 Caffeine（命中直接返回）
        ↓ 未命中
     L2 Redis（命中写入L1并返回）
        ↓ 未命中
     数据库（写入Redis + 写入L1）
```

### 5.2 数据一致性保障

**Cache Aside 模式（标准模式）**：
```
读：cache hit → 直接返回
    cache miss → 查数据库 → 写缓存 → 返回

写：更新数据库 → 删除缓存（而非更新缓存）
```

> 为什么是删除缓存而非更新？避免并发时的数据不一致。

**主动失效 + MQ 广播**：
- 写请求完成数据库更新后，发送 MQ 消息
- 各服务节点订阅 MQ，收到消息后删除本地缓存
- 适合多实例部署场景

**Canal 监听 Binlog**：
- MySQL 开启 binlog
- Canal 模拟 slave 订阅 binlog
- 数据变更时自动删除/更新 Redis 缓存
- 适合对数据一致性要求较高的场景

### 5.3 热点 Key 探测与防御

**热点 Key 发现**：
- Redis 4.0+ 提供 `hotkeys` 命令
- 使用 `redis-cli --hotkeys` 定期扫描
- 客户端埋点统计

**热点 Key 解决方案**：
- **本地缓存**：热点 key 存入 JVM 堆缓存
- **热点 Key 备份**：对热点 key 追加随机后缀，路由到不同实例
- **读写分离**：读请求走从库，写请求走主库

---

## 六、Redis 其他高频问题

### 6.1 Redis 为什么这么快

**1. 内存操作**
- 所有数据存储在内存
- 内存访问速度 ns 级（纳秒）

**2. 单线程模型**
- 避免上下文切换开销
- 避免锁竞争
- 单线程不等于慢，Redis QPS 可达 10万+

> 注意：Redis 6.0 后 IO 读写变为多线程，但命令执行仍是单线程。

**3. IO 多路复用（epoll）**
- 使用 epoll 实现 IO 多路复用
- 单线程同时监听多个 socket 事件
- 事件驱动，非阻塞 I/O

**4. 高效数据结构**
- 各种数据结构针对不同场景优化
- O(1) 复杂度的基本操作

### 6.2 Redis 6.0 多线程

**多线程只用于 IO 读写**：
- 主线程负责协议解析
- IO 线程负责 socket 读写
- 命令执行仍在主线程

**配置**：
```
io-threads 4  # IO线程数，建议 N-1（留一个给主线程）
io-threads-do-reads yes
```

**性能提升**：多核机器上可提升约 3 倍 QPS。

### 6.3 分布式锁（Redisson）

Redisson 是最流行的 Redis 分布式锁实现。

**核心特性**：

**1. 看门狗机制（Watchdog）**
- 默认锁 TTL 为 30 秒
- 看门狗每 10 秒检查锁是否还在持有
- 如果是，自动续期到 30 秒
- 防止业务执行时间超过 TTL 导致锁自动释放

**2. 可重入锁**
- 同一线程可多次获取同一把锁
- 通过 ThreadLocal 存储重入计数
- 释放时计数归零才真正删除 key

**3. RedLock 算法**
- 向 N 个独立 Redis 节点获取锁
- 超过半数节点成功才视为获取成功
- 需要处理节点故障和时钟漂移

**基本用法**：
```java
RLock lock = redisson.getLock("myLock");
try {
    lock.lock();
    // 业务逻辑
} finally {
    lock.unlock();
}
```

### 6.4 Pipeline vs Lua 脚本

**Pipeline**：
- 客户端批量发送命令
- 服务端按顺序执行
- 减少网络往返次数（RTT）
- 适用于批量读取/写入

**Lua 脚本**：
- 服务端原子执行脚本
- 脚本内容整体编译执行
- 适用于需要原子性的复杂逻辑
- Redis 保证脚本执行不被中断

**区别**：
| 维度 | Pipeline | Lua |
|------|----------|-----|
| 原子性 | 非原子，命令独立执行 | 原子执行 |
| 网络 | 批量 RTT | 单次 RTT |
| 适用场景 | 批量操作 | 需要原子性的操作 |

---

## 七、消息队列核心问题

### 7.1 为什么要用 MQ

**1. 解耦**
- 生产者和消费者解耦
- 新增消费者无需修改生产者
- 系统间通过消息契约通信

**2. 异步**
- 同步调用 → 异步消息
- 减少响应时间
- 例如：下单后发优惠券，只需发消息，异步处理

**3. 削峰**
- 流量洪峰时，MQ 作为缓冲区
- 消费者按自己的速度处理
- 保护下游系统不被击垮

### 7.2 如何保证消息不丢失

消息丢失发生在三个环节，需要三重保障：

**1. 生产者 → Broker**

**方案一：确认机制（Publisher Confirm）**
- 生产者发送消息后等待 Broker 确认
- 未收到确认则重试

**方案二：事务消息（RocketMQ）**
- 发送消息和本地事务绑定
- 提交/回滚二阶段提交

**2. Broker 自身**

**持久化**：
- 刷盘策略：同步刷盘（always）保证不丢
- 副本机制：多副本存储
- Broker 配置多盘（RAID）进一步保障

**3. Broker → 消费者**

**手动 ACK**：
```java
consumer.registerMessageListener((MessageListenerConcurrently) (msgs, context) -> {
    try {
        // 业务处理
        return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
    } catch (Exception e) {
        return ConsumeConcurrentlyStatus.RECONSUME_LATER; // 重试
    }
});
```
- 手动返回成功才确认
- 处理失败返回重试，Broker 会重新投递

### 7.3 如何保证消息有序

**场景**：下单流程需要依次经过：创建订单 → 扣减库存 → 扣减余额 → 物流

**解决方案**：

**1. 同一业务 Key 路由到同一 Queue**
```java
// 使用订单ID作为sharding key
producer.send(message, new MessageQueueSelector() {
    @Override
    public MessageQueue select(List<MessageQueue> mqs, Message msg, Object arg) {
        String orderId = (String) arg;
        int index = orderId.hashCode() % mqs.size();
        return mqs.get(index);
    }
}, orderId);
```

**2. 单线程消费**
- 同一 Queue 只用一个消费者
- 保证消息按顺序处理

**注意**：消息积压时，有序性和性能需要权衡。

### 7.4 如何保证消息幂等

消息重复消费是常见问题，需要消费者实现幂等。

**方案一：唯一业务ID + 防重表**
```java
// 使用订单ID作为幂等Key
if (redis.exists("dedup:" + orderId)) {
    return; // 重复消费，直接返回
}
redis.setex("dedup:" + orderId, 24小时, "1");
// 业务处理...
```

**方案二：数据库唯一约束**
- 利用数据库唯一索引
- 重复插入会报错，自动去重

**方案三：Redis setnx**
- 原子性保证
- key 过期时间防止永久占用

### 7.5 消息积压处理

**问题表现**：消费速度 < 生产速度，消息在队列中堆积。

**解决方案**：

**1. 紧急扩容消费者**
- 增加消费者实例
- 注意：RabbitMQ 需要新建消费者，Kafka 可用 Consumer Group 扩展

**2. 临时 Queue 扩容**
- 新建临时 Queue 分担压力
- 上线新消费者实例

**3. 消费端批量消费**
- 一次拉取多条消息（Kafka 可配置 fetch.max.bytes）
- 本地批量处理后再 ACK

**4. 跳过不重要的消息**
- 消费端设置超时跳过
- 先处理重要消息

**5. 丢弃（最后手段）**
- 积压太多时，直接丢弃
- 后续补偿处理

**预防措施**：
- 监控队列深度
- 提前报警
- 生产端限流

---

## 八、三大 MQ 对比

### 8.1 核心对比

| 维度 | RocketMQ | Kafka | RabbitMQ |
|------|----------|-------|----------|
| **定位** | 金融/电商级 | 大数据/日志 | 企业级通用 |
| **事务消息** | 原生支持（半消息） | 不支持 | 插件实现 |
| **吞吐量** | 10万级 | 百万级 | 万级 |
| **延迟** | ms 级 | ms 级（高吞吐时） | μs 级（低吞吐） |
| **顺序消息** | 支持（单 Queue 有序） | 支持（Partition 内） | 不支持 |
| **消息回溯** | 支持（按时间戳/offset） | 支持（按 offset） | 不支持 |
| **单机吞吐量** | 10万 QPS | 100万 QPS | 1万 QPS |
| **单机队列数** | 万级 | 千级 | 万级 |
| **消息堆积能力** | 强 | 极强 | 一般 |
| **单消息大小** | MB 级 | KB 级（推荐） | MB 级 |
| **消费模式** | 集群/广播 | 集群 | 集群/广播 |

### 8.2 选型建议

**选择 RocketMQ**：
- 电商交易场景
- 需要事务消息
- 金融支付相关
- 需要消息回溯

**选择 Kafka**：
- 日志收集、大数据实时计算
- 超高吞吐量需求
- 消息积压场景
- 消息审计需求

**选择 RabbitMQ**：
- 中小规模项目
- 需要灵活路由（Exchange）
- 消息延迟探测
- 学习成本低的场景

---

## 九、RocketMQ 深度解析

### 9.1 架构设计

```
                    ┌─────────────────────────────────────┐
                    │              NameServer             │
                    │  (集群各节点间无数据同步，各节点独立)  │
                    └─────────────────────────────────────┘
                                    ▲
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│    Broker     │          │    Broker     │          │    Broker     │
│  (Master)     │          │  (Master)     │          │  (Master)     │
│  写 + 读      │          │  写 + 读      │          │  写 + 读      │
└───────────────┘          └───────────────┘          └───────────────┘
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│   Broker      │          │   Broker      │          │   Broker      │
│  (Slave)      │          │  (Slave)      │          │  (Slave)      │
│  读           │          │  读           │          │  读           │
└───────────────┘          └───────────────┘          └───────────────┘
```

**核心组件**：

**1. NameServer**
- 服务注册中心
- 各 Broker 定期向所有 NameServer 注册
- Producer/Consumer 从 NameServer 获取路由信息
- 无状态，集群间无数据同步

**2. Broker**
- 消息存储和转发
- 分 Master 和 Slave
- Master 负责读写，Slave 仅读
- 支持同步双写（高可用）和异步复制

**3. Producer**
- 消息生产者
- 从 NameServer 获取 Broker 地址
- 支持多种负载均衡策略

**4. Consumer**
- 消息消费者
- 集群消费（多实例分摊）
- 广播消费（所有实例都消费）

### 9.2 事务消息原理

RocketMQ 事务消息实现半消息机制，保证本地事务和消息发送的一致性。

**流程**：

```
┌────────┐      ┌────────┐      ┌────────┐      ┌────────┐
│Producer│      │ Broker │      │Producer│      │ Broker │
└───┬────┘      └───┬────┘      └───┬────┘      └───┬────┘
    │                │                │                │
    │  1.发送半消息    │                │                │
    │───────────────>│                │                │
    │  2.ACK         │                │                │
    │<───────────────│                │                │
    │                │                │                │
    │  3.执行本地事务  │                │                │
    │  (扣款/库存)    │                │                │
    │                │                │                │
    │  4.提交/回滚    │                │                │
    │───────────────>│                │                │
    │                │                │                │
    │  (如无响应)     │                │                │
    │  6.回查         │                │                │
    │<───────────────│                │                │
    │                │                │                │
    │                │        5.投递消息到Consumer    │
    │                │<────────────────│                │
```

**详细步骤**：

**1. 发送半消息**
- 发送的消息对消费者不可见
- 类似于预扣款/预占库存

**2. 执行本地事务**
- 执行业务逻辑（创建订单、扣减库存）
- 根据结果决定提交还是回滚

**3. 提交/回滚**
- 提交：半消息变为正常消息，投递给消费者
- 回滚：删除半消息

**4. 回查机制**
- 如果 Producer 长时间未响应
- Broker 向 Producer 查询事务状态
- Producer 提供查询接口查询本地事务结果

**应用场景**：
- 分布式事务：下单 + 扣库存
- 账户扣款 + 消息发送
- 任何需要本地事务和消息一致性保障的场景

### 9.3 消息重试与死信队列

**消息重试**：

**触发条件**：
- 消费者返回 `RECONSUME_LATER`
- 消费者返回 null 或抛异常
- 消息处理超时

**重试机制**：
- 最大重试次数：16 次（可配置）
- 重试间隔：阶梯式（1s, 5s, 10s, 30s, 1m, 2m...）
- 超过最大次数进入死信队列

**死信队列（Dead Letter Queue）**：
- 存储无法正常消费的消息
- 单独 Topic，不影响主流程
- 可人工干预处理
- 保留 3 天（可配置）

**消费幂等**：
- RocketMQ 不保证消息不重复
- 消费者必须实现幂等处理
- 使用业务唯一 ID 去重

---

## 十、Kafka 深度解析

### 10.1 核心概念

```
┌─────────────────────────────────────────────────────────────────┐
│                         Kafka Cluster                           │
│                                                                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                        │
│  │ Broker1 │  │ Broker2 │  │ Broker3 │   ← 3台Broker           │
│  │(Leader) │  │(Follower)│  │(Follower)│                        │
│  └─────────┘  └─────────┘  └─────────┘                        │
│                                                                 │
│  Topic: ORDER_TOPIC (3 Partition, 3 Replica)                    │
│  ┌──────────────┬──────────────┬──────────────┐                │
│  │ Partition-0  │ Partition-1  │ Partition-2  │                │
│  │ Leader: B1   │ Leader: B2  │ Leader: B3   │                │
│  └──────────────┴──────────────┴──────────────┘                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

Consumer Group: ORDER_CONSUMER_GROUP
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Consumer-1  │  │ Consumer-2  │  │ Consumer-3  │
│ 消费P0,P1   │  │ 消费P2,P0   │  │ 消费P1,P2   │
└─────────────┘  └─────────────┘  └─────────────┘
```

**核心概念解释**：

| 概念 | 说明 |
|------|------|
| Broker | Kafka 服务节点，一个集群包含多个 Broker |
| Topic | 消息主题，逻辑分类 |
| Partition | 分区，物理存储，实现并行消费 |
| Replica | 分区副本，保证高可用 |
| Producer | 生产者，消息发送方 |
| Consumer | 消费者，消息读取方 |
| Consumer Group | 消费者组，实现负载均衡消费 |

### 10.2 Kafka 高性能原因

**1. 顺序写磁盘**
- 写入数据追加到文件末尾
- 磁盘顺序写入速度可达 600MB/s
- 接近内存随机访问速度

**2. 零拷贝（sendfile）**
```
传统方式：磁盘 → 内核缓冲区 → 用户缓冲区 → 内核Socket缓冲区 → 网络
零拷贝：  磁盘 → 内核缓冲区 → 网络
```
- 使用 Linux sendfile 系统调用
- 减少 2 次 CPU 拷贝
- 配合 DMA irect Memory Access

**3. 页缓存（Page Cache）**
- 操作系统将空闲内存作为磁盘缓存
- 写入先到页缓存，后异步刷盘
- 读取先查页缓存，未命中再读磁盘

**4. 批量压缩**
- 多条消息一起压缩
- 减少网络传输量
- 支持多种压缩算法（LZ4, Snappy, Gzip）

**5. 批量发送**
- Producer 积累消息后批量发送
- 减少网络请求次数
- 可配置 batch.size 和 linger.ms

### 10.3 ISR 机制

**ISR（In-Sync Replicas）** 是 Kafka 实现高可用的核心机制。

**定义**：与 Leader 保持同步的副本集合

**判定标准**：副本的leo（log end offset）追赶上 leader的hw（high watermark）

**触发条件**：
- Follower 持续从 Leader 拉取消息
- 延迟时间 < replica.lag.time.max.ms
- 延迟消息数 < replica.lag.max.messages

**作用**：
- 只有 ISR 内的副本有资格被选为新 Leader
- 保证消息不丢失
- 权衡了可用性和一致性

**举例**：
- Topic 配置 3 副本
- ISR = {0, 1}，副本2 落后太多被踢出 ISR
- 此时如果 Leader 宕机，只从 {0, 1} 中选新 Leader

**可靠性配置**：
```properties
# 确保消息写入 ISR 中所有副本
acks = all

# 副本间同步等待时间
replica.lag.time.max.ms = 30000

# 允许的最大延迟
replica.lag.max.messages = 40000
```

---

## 十一、面试高频速查

### Q1: 为什么选 RocketMQ 而不是 Kafka？

**参考答案**：

RocketMQ 和 Kafka 的定位不同：

**选择 RocketMQ 的场景**：
1. **需要事务消息**：RocketMQ 原生支持，Kafka 不支持
2. **电商交易场景**：订单、支付等业务需要强一致性
3. **需要消息回溯**：按时间戳/offset 重新消费
4. **延迟消息**：RocketMQ 支持定时/延时消息
5. **中小规模项目**：运维简单，文档完善

**Kafka 的优势场景**：
1. **大数据实时计算**：Flink、Spark 生态完美对接
2. **日志收集**：超高吞吐量，消息堆积能力强
3. **用户行为分析**：海量埋点数据

**运达项目场景建议**：如果涉及交易、订单等核心链路，推荐 RocketMQ；如果主要是数据同步、日志处理，Kafka 更合适。

---

### Q2: 消息积压了怎么处理？

**参考答案**：

**紧急处理**：
1. **快速扩容消费者**：增加 Consumer 实例，Kafka 可直接加入 Consumer Group
2. **临时新建 Queue**：RabbitMQ 可快速扩容 Queue 和消费者
3. **批量消费优化**：增加每次拉取数量，本地批量处理

**治本方案**：
1. **分析积压原因**：
   - 消费者挂了？重启
   - 消费者逻辑太慢？优化代码
   - 生产速度太快？限流
2. **监控预警**：提前发现积压趋势
3. **消费端优化**：异步处理、批量操作、并行消费

**预防措施**：
- 设置消息积压监控
- 阈值报警
- 定期压测

---

### Q3: 如何保证消息的精确一次消费（Exactly-Once）？

**参考答案**：

**三种语义对比**：

| 语义 | 说明 | 可能丢消息 | 可能重复 |
|------|------|----------|---------|
| At Most Once | 最多一次 | 可能 | 可能 |
| At Least Once | 至少一次 | 不可能 | 可能 |
| Exactly Once | 精确一次 | 不可能 | 不可能 |

**实现方案**：

**1. 事务消息（RocketMQ）**
```
半消息 → 执行本地事务 → 提交/回滚 → 消费者 ACK
```
- Producer 端保证发送不丢失
- 需要消费者实现幂等

**2. 幂等消费者**
```java
// 方案1：Redis 防重
if (redis.setnx("msg:dedup:" + msgId, "1", 24h)) {
    // 处理消息
}

// 方案2：数据库唯一索引
// 消息处理表加唯一索引，重复插入会报错
```

**3. Kafka 事务（Exactly-Once Semantics）**
```properties
enable.idempotence = true
transactional.id = "producer-1"
```
- Producer 发送消息开启事务
- 消费端开启事务，自动提交 offset

**最佳实践**：
- 业务端实现幂等（最可靠）
- RocketMQ 事务消息 + 消费者幂等
- 不依赖 MQ 本身保证幂等

---

### Q4: RocketMQ 的事务消息原理？

**参考答案**：

**核心思想**：半消息（Half Message）+ 本地事务 + 事务回查

**执行流程**：

```
1. Producer 发送半消息到 Broker（此时消息对 Consumer 不可见）

2. Producer 执行本地事务
   - 创建订单、扣减库存等
   - 根据成功/失败决定提交/回滚

3. 提交半消息
   - 成功：消息变为正常，可被消费
   - 失败：删除半消息

4. 如果 Producer 长时间未响应
   - Broker 向 Producer 发送回查请求
   - Producer 查询本地事务状态
   - 根据状态决定提交/回滚
```

**应用场景**：
- 分布式事务：下单 + 扣库存 + 扣余额
- 需要本地事务和消息一致性

**代码示例**：
```java
@Transactional
public void createOrder(OrderDTO order) {
    // 1. 创建订单
    orderService.create(order);

    // 2. 发送事务消息
    TransactionMQProducer producer = ...;
    producer.sendMessageInTransaction(message, new LocalTransactionExecuter() {
        @Override
        public LocalTransactionState executeLocalTransactionBranch(Message msg, Object arg) {
            // 本地事务已在上一步执行，这里返回提交
            return LocalTransactionState.COMMIT_MESSAGE;
        }
    }, null);
}
```

---

### Q5: Kafka 为什么这么快？

**参考答案**：

**1. 顺序写磁盘**
- 消息追加到分区文件末尾
- 顺序写入速度接近内存
- 写入 QPS 可达 600MB/s

**2. 零拷贝技术**
- 使用 sendfile 系统调用
- 数据从磁盘直接到网卡，跳过用户态
- 减少 CPU 上下文切换和拷贝次数

**3. 页缓存（Page Cache）**
- 利用操作系统内存作为缓存
- 写入先到页缓存，异步刷盘
- 读取优先查缓存

**4. 批量处理**
- Producer 批量发送消息
- Consumer 批量拉取
- 减少网络请求次数

**5. 压缩**
- 多消息合并压缩
- 减少网络传输量
- 支持 LZ4、Snappy、Gzip

**6. 稀疏索引**
- 消息不建立稠密索引
- 基于 offset 定位
- 查找效率 O(1)

**一句话总结**：Kafka 通过顺序写、零拷贝、页缓存、批量处理等技术，实现了磁盘的高效读写，兼顾了持久化和性能。

---

### Q6: Redis 和数据库双写一致性怎么保证？

**参考答案**：

**三种策略对比**：

| 策略 | 一致性 | 性能 | 实现复杂度 |
|------|--------|------|-----------|
| 先写缓存，再写数据库 | 差 | 高 | 低 |
| 先写数据库，再写缓存 | 较差 | 高 | 低 |
| 先删缓存，再写数据库 | 较好 | 中 | 中 |
| 延迟双删 | 好 | 中 | 中 |
| Canal 监听 Binlog | 最好 | 低 | 高 |

**1. Cache Aside（推荐）**
```
读：cache hit → 返回
    cache miss → 读DB → 写cache → 返回

写：更新DB → 删除cache（不是更新cache）
```

**2. 延迟双删**
```java
// 1. 删除缓存
redis.del(key);

// 2. 更新数据库
db.update(key, value);

// 3. 延迟N毫秒后再删一次（处理并发问题）
Thread.sleep(N);
redis.del(key);
```

**3. Canal 方案**
- MySQL 开启 binlog
- Canal 模拟 slave 订阅
- 数据变更自动删除/更新 Redis

**结合 MQ 广播失效**：
```
服务A 更新数据库 → 发送 MQ 消息 → 
服务B/服务C 收到消息 → 删除各自本地缓存
```

**最佳实践**：
- 强一致性场景：Canal + 多级缓存
- 最终一致性场景：Cache Aside + MQ 广播失效
- 避免并发问题：延迟双删

---

## 附录

### 附录A：Redis 常用配置

```properties
# 内存相关
maxmemory 2gb
maxmemory-policy allkeys-lru

# RDB 持久化
save 900 1
save 300 10
save 60 10000

# AOF 持久化
appendonly yes
appendfsync everysec
aof-use-rdb-preamble yes

# 集群
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 15000
```

### 附录B：Kafka 常用命令

```bash
# 创建 Topic
kafka-topics.sh --create --topic my-topic --partitions 3 --replication-factor 2 --bootstrap-server localhost:9092

# 查看 Topic 列表
kafka-topics.sh --list --bootstrap-server localhost:9092

# 查看消费者组
kafka-consumer-groups.sh --list --bootstrap-server localhost:9092

# 重置 offset
kafka-consumer-groups.sh --reset-offsets --group my-group --topic my-topic --to-earliest --execute --bootstrap-server localhost:9092

# 查看 Topic 详情
kafka-topics.sh --describe --topic my-topic --bootstrap-server localhost:9092
```

### 附录C：RocketMQ 常用命令

```bash
# 启动 NameServer
mqnamesrv.cmd

# 启动 Broker
mqbroker.cmd -n localhost:9876

# 创建 Topic
mqadmin updateTopic -n localhost:9876 -t my-topic -c DefaultCluster

# 查看消费堆积
mqadmin consumerProgress -n localhost:9876 -g my-consumer-group

# 查看 Topic 路由
mqadmin topicRoute -n localhost:9876 -t my-topic
```

---

## 关联笔记

- [[简历知识点总结]]
- [[运达面试专区]]
- [[MVCC多版本并发控制]]

## 参考资源

- [[MOC-Java面试]]

---

*文档更新时间：2026年4月*
*整理：Sisyphus-Junior*
