---
tags: #java #集合框架 #面试 #运达 #高频考点
---

# HashMap 与 ConcurrentHashMap

Java 集合框架中，HashMap 和 ConcurrentHashMap 是使用频率最高的键值对存储结构。本文深入剖析两者底层原理、线程安全问题及面试高频考点。

---

## 一、HashMap 核心原理

### 1.1 底层数据结构

JDK8 及之后的 HashMap 采用**数组 + 链表 + 红黑树**的组合结构：

- **数组**：主干的哈希表，每个位置称为桶（bucket）
- **链表**：解决哈希冲突，相同 hash 值的元素以链表形式存储
- **红黑树**：当链表长度达到阈值时转换为红黑树，提升查询效率从 O(n) 到 O(log n)

```
数组索引 [0] [1] [2] [3] [4] ... [n]
           ↓   ↓   ↓
         链表或红黑树
```

### 1.2 关键参数解析

| 参数 | 默认值 | 说明 |
|------|--------|------|
| INITIAL_CAPACITY | 16 | 初始数组容量，必须是 2 的幂次 |
| LOAD_FACTOR | 0.75 | 负载因子，size > capacity × loadFactor 时扩容 |
| TREEIFY_THRESHOLD | 8 | 链表树化阈值，链表长度 ≥ 8 时转为红黑树 |
| UNTREEIFY_THRESHOLD | 6 | 红黑树反树化阈值，节点数 ≤ 6 时转回链表 |
| MIN_TREEIFY_CAPACITY | 64 | 树化的最小数组容量，数组 < 64 时优先扩容而非树化 |

### 1.3 容量为什么必须是 2 的幂次

这是 HashMap 设计中的精髓，核心目的是**用位运算替代耗时的取模运算**。

**数学原理**：

- 当 length = 2^n 时，`hash % length` 等价于 `hash & (length - 1)`
- 例如：length = 16 = 2^4，`hash % 16` 等价于 `hash & 15`

**性能差异**：

- 取模运算（%）：涉及除法，CPU 周期长
- 位与运算（&）：纯位操作，几个时钟周期完成

**均匀散列保证**：
length - 1 的二进制形式是全 1（如 15 = 1111），与 hash 进行 & 运算时，每一位都有机会参与，结果分布均匀。

```
hash:     10110011 11010101 01110010 10101010
length-1: 00000000 00000000 00000000 00001111  (15)
------------------------------------------------
result:   00000000 00000000 00000000 10101010  (低位决定桶位置)
```

### 1.4 hash 扰动函数

```java
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
```

**为什么需要扰动？**

key.hashCode() 返回的 32 位整数，高位 bit 的信息在取模时可能被丢弃。例如数组容量 16 时，只有低 4 位参与运算。

**扰动函数做了什么？**

将 hashCode 的高 16 位与低 16 位进行异或运算，让高位特征混合到低位，从而**让所有 bit 位都参与运算，减少碰撞**。

```
原始 hashCode: 10110011 11010101 01110010 10101010
高 16 位:     10110011 11010101
低 16 位:     01110010 10101010
异或结果:     11000001 00100111 01110010 10101010
```

### 1.5 put 流程详解

put 方法的执行流程如下：

```
1. 计算 key 的 hash 值（扰动函数处理）
   ↓
2. 通过 (n-1) & hash 定位桶位置
   ↓
3. 判断该桶是否为空
   ├── 空桶：直接创建 Node 插入
   └── 非空桶：继续判断
   ↓
4. 桶不为空，判断 key 是否相同（hash 相等 && equals 为 true）
   ├── 相同：覆盖旧 value
   └── 不同：继续遍历
   ↓
5. 当前桶结构是链表还是红黑树？
   ├── 链表：遍历到尾节点，追加新 Node
   │         若链表长度 ≥ 8，转下一步判断
   └── 红黑树：调用树插入方法
   ↓
6. 链表长度 ≥ 8 且数组容量 ≥ 64？
   ├── 是：链表转换为红黑树
   └── 否：触发 resize() 扩容
   ↓
7. 检查是否需要扩容（size > threshold）
   └── 是：调用 resize() 扩容
```

**代码核心逻辑**：

```java
public V put(K key, V value) {
    return putVal(hash(key), key, value, false, true);
}

final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
               boolean evict) {
    Node<K,V>[] tab; Node<K,V> p; int n, i;
    // 1. 首次put时延迟初始化
    if ((tab = table) == null || (n = tab.length) == 0)
        n = (tab = resize()).length;
    
    // 2. 定位桶，空则直接插入
    if ((p = tab[i = (n - 1) & hash]) == null)
        tab[i] = newNode(hash, key, value, null);
    else {
        Node<K,V> e; K k;
        // 3. key 已存在，覆盖value
        if (p.hash == hash && ((k = p.key) == key || key.equals(k)))
            e = p;
        // 4. 红黑树结构
        else if (p instanceof TreeNode)
            e = ((TreeNode<K,V>) p).putTreeVal(this, tab, hash, key, value);
        // 5. 链表结构
        else {
            for (int binCount = 0; ; ++binCount) {
                if ((e = p.next) == null) {
                    p.next = newNode(hash, key, value, null);
                    // 链表长度达到阈值，尝试树化
                    if (binCount >= TREEIFY_THRESHOLD - 1)
                        treeifyBin(tab, hash);
                    break;
                }
                // 找到相同key，覆盖
                if (e.hash == hash && ((k = e.key) == key || key.equals(k)))
                    break;
                p = e;
            }
        }
        // 覆盖value
        if (e != null) {
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
        }
    }
    ++modCount;
    if (++size > threshold)
        resize();
    afterNodeInsertion(evict);
    return null;
}
```

### 1.6 扩容机制（resize）

**触发条件**：

```java
if (++size > threshold)  // threshold = capacity × loadFactor
    resize();
```

**扩容规则**：

- 新容量 = 旧容量 × 2（始终保持 2 的幂次）
- 新阈值 = 新容量 × 负载因子

**JDK8 扩容优化：无需重新计算 hash**

这是 JDK8 对扩容算法的重大优化。传统方式需要对每个元素重新计算 hash，而 JDK8 只需要判断 `(e.hash & oldCap) == 0`。

原理：
- oldCap 是 2 的幂次（如 16 = 10000）
- oldCap - 1 的最高位为 1（如 15 = 01111）
- `e.hash & oldCap` 的结果要么是 0，要么是 oldCap 本身
- 结果为 0：元素留在原位置
- 结果为 oldCap：元素移动到 原位置 + oldCap

```
示例：oldCap = 16

元素A: hash = 43 (0b101011)
       43 & 16 = 0   → 留在原位置 index = 11

元素B: hash = 59 (0b111011)
       59 & 16 = 16  → 移动到 index = 11 + 16 = 27
```

**为什么先插入再扩容？**

HashMap 采用**先插入后扩容**的策略，目的是避免无意义的扩容。如果插入后 size 没超过阈值，就不需要扩容。比起先扩容再插入，再判断是否需要回退，这种方式更简单高效。

---

## 二、HashMap 线程不安全

HashMap 不是线程安全的，在并发环境下会出现严重问题。

### 2.1 JDK7 扩容死循环（头插法导致）

JDK7 中，扩容时使用**头插法**转移链表元素。并发扩容时，多个线程可能将链表指针改写，形成环形链表。

**死循环形成过程**：

```
初始状态：数组桶 → 链表 A → B → C

线程A开始扩容，遍历到A节点：
  next = A.next  (指向B)
  A.next = newTable[index]  (null)
  newTable[index] = A
  当前节点 = B

线程B也在扩容，抢占了同一个桶：
  next = B.next  (指向C)
  B.next = newTable[index]  (指向A)
  newTable[index] = B
  当前节点 = C

线程A继续执行，处理B：
  next = C.next  (null)
  C.next = newTable[index]  (指向B)
  newTable[index] = C
  当前节点 = null，遍历结束

线程B继续执行，处理C：
  next = C.next  (指向B，形成环！)
  ...

问题：获取元素时，遍历陷入死循环，CPU 100%
```

**核心问题**：头插法会**反转链表顺序**。当两个线程同时遍历同一个桶并重建链表时，指针交错导致成环。

### 2.2 JDK8 数据覆盖问题（尾插法改进）

JDK8 改为**尾插法**，解决了死循环问题，但仍有线程安全问题：

```java
// JDK8 尾插法
if ((e = p.next) == null) {
    p.next = newNode(hash, key, value, null);  // 追加到尾部
    break;
}
```

**并发覆盖场景**：

```
线程A和线程B同时put "key1" -> "valueA" 和 "key1" -> "valueB"

1. 线程A和B都计算得到相同的桶位置
2. 桶为空，线程A CAS插入 Node(key1, valueA)
3. 线程B也发现桶为空，CAS插入 Node(key1, valueB) 覆盖了A的节点
4. 结果：valueB覆盖了valueA，线程A的put结果丢失
```

**Fail-Fast 机制**：

HashMap 内部维护 `modCount` 字段，每次增删改操作都会递增。当迭代器遍历时，会检查 `modCount` 是否被修改过：

```java
final Node<K,V> nextNode() {
    Node<K,V>[] t;
    int i, expectedModCount = modCount;  // 记录期望值
    if ((e = next) == null || e == (p = next = t[i = index]))
        throw new ConcurrentModificationException();
    if (modCount != expectedModCount)    // 被修改则抛出异常
        throw new ConcurrentModificationException();
    return e;
}
```

并发修改时，另一个线程会触发 `ConcurrentModificationException`。

### 2.3 为什么不用 HashMap 做并发共享

1. **数据覆盖**：并发 put 可能导致后写入的数据覆盖先写入的
2. **死循环**：JDK7 扩容时链表成环导致死循环
3. **Fail-Fast**：迭代时检测到并发修改会抛异常
4. **可见性**：没有同步机制，其他线程可能看不到最新值

---

## 三、ConcurrentHashMap

### 3.1 JDK7 实现：Segment 分段锁

JDK7 采用**Segment 分段锁**机制实现线程安全：

**数据结构**：

```java
public class ConcurrentHashMap<K, V> {
    // Segment 数组，每个 Segment 是一个小型的 HashMap
    final Segment<K,V>[] segments;
    
    static final class Segment<K,V> extends ReentrantLock 
                                      implements Serializable {
        transient volatile HashEntry<K,V>[] table;
        transient int count;           // 元素数量
        transient int modCount;        // 修改计数
        transient int threshold;       // 扩容阈值
        final float loadFactor;        // 负载因子
    }
    
    static final class HashEntry<K,V> {
        final int hash;
        final K key;
        volatile V value;
        final HashEntry<K,V> next;
    }
}
```

**并发度**：

- 默认 16 个 Segment
- 并发度 = Segment 数量，即最多 16 个线程同时操作

**操作逻辑**：

| 操作 | 锁粒度 | 说明 |
|------|--------|------|
| get | 无锁 | value 和 next 都是 volatile，保证可见性 |
| put | Segment 锁 | 锁住对应 Segment，在其内部数组操作 |
| size | Segment 锁 | 锁所有 Segment，累加 count |

**put 操作流程**：

```java
public V put(K key, V value) {
    Segment<K,V> s;
    if (value == null) throw new NullPointerException();
    int hash = hash(key);
    int j = (hash >>> segmentShift) & (segmentMask);  // 定位Segment
    s = (Segment<K,V>)UNSAFE.getObjectVolatile(segments, u);
    if (s == null) {
        s = Segment<K,V> ensureSegment(j);  // 延迟初始化
    }
    return s.put(key, hash, value, false);  // 在Segment内加锁put
}
```

### 3.2 JDK8 实现：CAS + synchronized

JDK8 废弃了 Segment，改为**CAS + synchronized**实现，进一步提升并发度。

**数据结构**：

```java
public class ConcurrentHashMap<K, V> {
    transient volatile Node<K,V>[] table;
    
    static final class Node<K,V> {
        final int hash;
        final K key;
        volatile V value;
        volatile Node<K,V> next;
    }
    
    // 红黑树节点
    static final class TreeNode<K,V> extends Node<K,V> {
        TreeNode<K,V> parent;
        TreeNode<K,V> left;
        TreeNode<K,V> right;
        boolean red;
    }
}
```

**put 操作流程**：

```
1. 计算 key 的 hash 值
   ↓
2. 定位桶位置 table[(n-1) & hash]
   ↓
3. 判断该桶是否为空
   ├── 空桶：CAS 插入新 Node
   │         CAS 成功 → 插入完成
   │         CAS 失败（竞争）→ 说明其他线程已插入，转下一步
   └── 非空桶：继续
   ↓
4. 桶不为空，synchronized 锁住桶的头节点
   ↓
5. 判断桶结构
   ├── 链表：遍历查找或追加到尾部
   └── 红黑树：调用树插入方法
   ↓
6. 插入后检查是否需要树化
   ↓
7. 检查是否需要扩容
```

**核心代码**：

```java
final V putVal(K key, V value, boolean onlyIfAbsent) {
    if (key == null || value == null) throw new NullPointerException();
    int hash = spread(key.hashCode());
    int binCount = 0;
    
    for (Node<K,V>[] tab = table;;) {
        Node<K,V> f; int n, i, fh;
        // 延迟初始化
        if (tab == null || (n = tab.length) == 0)
            tab = table = initTable();
        // CAS 插入空桶
        else if ((f = tabAt(tab, i = (n - 1) & hash)) == null) {
            if (casTabAt(tab, i, null, new Node<K,V>(hash, key, value, null)))
                break;
        }
        // 发现正在扩容，帮助扩容
        else if ((fh = f.hash) == MOVED)
            tab = helpTransfer(tab, f);
        // 桶已有元素，synchronized 加锁
        else {
            V oldVal = null;
            synchronized (f) {
                if (tabAt(tab, i) == f) {
                    if (fh >= 0) {
                        binCount = 1;
                        for (Node<K,V> e = f;; ++binCount) {
                            K ek;
                            if (e.hash == hash &&
                                ((ek = e.key) == key || key.equals(ek))) {
                                oldVal = e.value;
                                if (!onlyIfAbsent)
                                    e.value = value;
                                break;
                            }
                            Node<K,V> pred = e;
                            if ((e = e.next) == null) {
                                pred.next = new Node<K,V>(hash, key, value, null);
                                break;
                            }
                        }
                    }
                    // 红黑树插入
                    else if (f instanceof TreeNode) {
                        TreeNode<K,V> t;
                        oldVal = ((TreeNode<K,V>)f).putTreeVal(this, tab, hash, key, value);
                    }
                }
            }
            if (binCount != 0) {
                if (binCount >= TREEIFY_THRESHOLD)
                    treeifyBin(tab, i);
                if (oldVal != null)
                    return oldVal;
                break;
            }
        }
    }
    addCount(1L, binCount);
    return null;
}
```

**为什么 JDK8 用 synchronized 而不是 ReentrantLock？**

1. **JVM 优化**：synchronized 在 JDK6 后引入了锁升级机制（偏向锁 → 轻量级锁 → 重量级锁），在大多数场景下性能已经很优秀
2. **API 简洁**：不需要手动释放锁，减少错误
3. **内存占用**：synchronized 的轻量级锁使用对象头 Mark Word，比 ReentrantLock 的 AQS 更轻量

### 3.3 get 操作无锁原理

ConcurrentHashMap 的 get 操作完全无锁且线程安全，依赖以下机制：

```java
static final class Node<K,V> {
    volatile V value;      // volatile 保证可见性
    volatile Node<K,V> next;  // volatile 保证可见性
}

public V get(Object key) {
    Node<K,V>[] tab; Node<K,V> e, p; int n, eh; K ek;
    int h = spread(key.hashCode());
    if ((tab = table) != null && (n = tab.length) > 0 &&
        (e = tabAt(tab, (n - 1) & h)) != null) {
        // 头节点 hash 匹配
        if ((eh = e.hash) == h) {
            if ((ek = e.key) == key || key.equals(ek))
                return e.value;
        }
        // 树结构
        else if (eh < 0) {
            p = e.find(h, key);
            return p != null ? p.value : null;
        }
        // 链表结构
        while ((e = e.next) != null) {
            if (e.hash == h &&
                ((ek = e.key) == key || key.equals(ek)))
                return e.value;
        }
    }
    return null;
}
```

**volatile 保证**：
- Node 的 value 和 next 用 volatile 修饰
- 任何线程对 value/next 的修改，对其他线程立即可见
- 结合 CAS 操作，确保读取到最新数据

### 3.4 多线程并发扩容

JDK8 的 ConcurrentHashMap 支持**多线程并发扩容**，这是 JDK7 做不到的。

**transfer 方法核心逻辑**：

```java
private final void transfer(Node<K,V>[] tab, Node<K,V>[] nextTab) {
    int n = tab.length, stride;
    // 每个线程处理的桶数量，最少16个
    stride = (n >>> 3) / NCPU * 3;  // 约 n/8/3
    if (stride < MIN_TRANSFER_STRIDE)
        stride = MIN_TRANSFER_STRIDE;
    
    // 初始化新数组
    if (nextTab == null) {
        nextTab = new Node<?,?>[n << 1];
        nextTable = nextTab;
        transferIndex = n;  // 标识进度
    }
    
    // 分配任务：每个线程从 transferIndex 处向前处理 stride 个桶
    for (int i = 0, nextIndex = transferIndex;;) {
        int bound;
        if (--i < bound || --nextIndex >= 0) {
            // 分配 [nextIndex-stride+1, nextIndex] 范围的桶给当前线程
        }
        // 所有桶处理完成
        if (i < 0 || nextIndex < 0 || transferIndex == 0) {
            nextTable = null;
            table = nextTab;
            return;
        }
    }
}
```

**任务分配机制**：
- transferIndex 记录当前未处理的桶位置
- 每个线程认领一段桶区间进行处理
- 处理完的桶标记为 ForwardingNode，表示已迁移

### 3.5 size() 的分段计数

ConcurrentHashMap 的 size() 不是简单地遍历计数，而是采用**分段累加**机制，类似 LongAdder：

```java
public int size() {
    long sum = 0;
    // 累加 baseCount
    sum = baseCount;
    // 累加 CounterCell[] 中的分段计数
    if (cellsBusy == 0) {
        Cell[] c = counterCells;
        if (c != null) {
            for (Cell cell : c) {
                if (cell != null)
                    sum += cell.value;
            }
        }
    }
    return (sum >= Integer.MAX_VALUE) ? Integer.MAX_VALUE : (int) sum;
}
```

**为什么不用 synchronized 锁住所有桶？**

因为 size() 是读多写少场景，如果为每次 size() 都锁住整个数组，会严重影响并发性能。分段计数让大部分场景下 size() 可以无锁执行。

### 3.6 JDK7 vs JDK8 对比

| 维度 | JDK7 | JDK8 |
|------|------|------|
| 数据结构 | Segment[] + HashEntry[] | Node[] + 链表/红黑树 |
| 锁粒度 | Segment 级别（最小 1） | 桶级别（最小 1） |
| 锁类型 | ReentrantLock（显式锁） | CAS + synchronized（内置锁） |
| 并发度 | 固定（默认 16） | 动态（与桶数量相关） |
| 查询复杂度 | O(n/m)，n 为元素数，m 为 Segment 数 | 链表 O(n)，红黑树 O(log n) |
| 扩容 | 单线程扩容 | 多线程并发扩容 |
| null 支持 | key/value 都不允许为 null | key/value 都不允许为 null |
| 死循环问题 | JDK7 扩容有死循环风险 | 无死循环 |

---

## 四、HashMap vs ConcurrentHashMap vs Hashtable vs Collections.synchronizedMap

| 特性 | HashMap | ConcurrentHashMap | Hashtable | Collections.synchronizedMap |
|------|---------|-------------------|-----------|------------------------------|
| 线程安全 | 否 | 是 | 是 | 是 |
| 并发度 | 无锁 | 高（桶级锁） | 低（全表锁） | 低（全表锁） |
| key/value null | 都允许 | 都不允许 | 都不允许 | 都不允许 |
| 底层结构 | 数组+链表+红黑树 | 数组+链表+红黑树 | 数组+链表 | 装饰器模式，内部持有一个 HashMap |
| 迭代安全性 | Fail-Fast | 安全迭代 | Fail-Fast | Fail-Fast |
| 锁类型 | 无 | CAS + synchronized | synchronized | synchronized |
| 首次 put 性能 | 快 | 可能涉及初始化竞争 | 慢（直接加锁） | 慢（直接加锁） |
| 适用场景 | 单线程或缓存 | 高并发场景 | 不推荐使用 | 不推荐使用 |
| 引入版本 | JDK1.2 | JDK1.5（JDK7 Segments，JDK8 全新实现） | JDK1.0 | JDK1.2 |

**为什么 ConcurrentHashMap 不允许 null？**

这是一个经典的设计问题。主要原因是**二义性**：

```java
// 场景：获取一个不存在的 key 对应的 value
V value = map.get(key);  // 返回 null

// 问题：无法判断是 key 不存在，还是 key 存在但 value 为 null
if (value == null) {
    // 二义性：是 key 不存在？还是 value 本来就是 null？
}
```

在并发环境下，这个问题更严重：

```
线程A执行：map.put(key, null)  // 期望将 key 的 value 设为 null
线程B执行：map.get(key)         // 返回 null，无法区分"不存在"和"值为null"
```

Hashtable 和 ConcurrentHashMap 选择**不允许 null 值**来消除这种歧义。

---

## 五、红黑树基础

### 5.1 为什么选择红黑树

**阈值为什么是 8？**

HashMap 选择链表长度 ≥ 8 时树化，背后有概率学的支撑。根据泊松分布，链表长度达到 k 的概率为：

```
P(X = k) = λ^k * e^(-λ) / k!
其中 λ ≈ 0.5（负载因子 0.75 下的平均链表长度）
```

计算结果：
- P(8) ≈ 0.00000003（约一亿分之三）
- P(7) ≈ 0.0000002

即链表长度达到 8 的概率**极低**，设置阈值为 8 可以避免对短链表进行不必要的树化（树化有额外开销）。

**为什么选红黑树而不是 AVL？**

| 对比维度 | 红黑树 | AVL |
|---------|--------|-----|
| 平衡标准 | 近似平衡（最长路径 ≤ 2×最短路径） | 严格平衡（左右子树高度差 ≤ 1） |
| 查找性能 | O(log n) | O(log n)，理论上稍快 |
| 插入性能 | 最多旋转 2 次 | 最多旋转 O(log n) 次 |
| 删除性能 | 最多旋转 3 次 | 最多旋转 O(log n) 次 |
| 适用场景 | 插入/删除频繁 | 查询频繁 |

Java 选择红黑树的原因是**插入和删除性能更好**。在 HashMap 场景中，频繁的 put 操作会导致链表节点的增删，红黑树更合适。

### 5.2 树化与反树化

**树化条件**（同时满足）：
1. 链表长度 ≥ 8
2. 数组容量 ≥ 64

```java
final void treeifyBin(Node<K,V>[] tab, int hash) {
    int n, index; Node<K,V> e;
    if (tab == null || (n = tab.length) < MIN_TREEIFY_CAPACITY)
        resize();  // 容量 < 64，优先扩容
    else if ((e = tabAt(tab, index = (n - 1) & hash)) != null) {
        // 构建红黑树
        TreeNode<K,V> hd = null, tl = null;
        do {
            TreeNode<K,V> p = new TreeNode<>(hash, e.key, e.value, null);
            if (tl == null) hd = p;
            else {
                p.prev = tl;
                tl.next = p;
            }
            tl = p;
        } while ((e = e.next) != null);
        tabAt(tab, index, hd);
    }
}
```

**反树化条件**：
- 红黑树节点数 ≤ 6 时，转回链表
- 反树化阈值设置为 6，与树化阈值 8 之间的"缓冲区"避免频繁切换

---

## 六、面试高频速查

### Q: HashMap 的 key 可以为 null 吗？ConcurrentHashMap 呢？为什么？

**HashMap**：key 和 value 都可以为 null。

**ConcurrentHashMap**：key 和 value 都不允许为 null。

**原因**：ConcurrentHashMap 禁止 null 是为了消除二义性。在并发环境下，无法区分 `get(key) == null` 是因为 key 不存在，还是因为 key 存在但 value 就是 null。Hashtable 也不允许 null 也是同样的原因。

---

### Q: HashMap 扩容时元素怎么迁移的？

JDK8 采用了高效的迁移策略：

1. **新容量 = 旧容量 × 2**，保持 2 的幂次
2. **不需要重新计算 hash**，通过 `(e.hash & oldCap) == 0` 判断位置
   - 结果为 0：元素留在原位置（index 不变）
   - 结果为 oldCap：元素移动到原位置 + oldCap（index + oldCap）
3. **使用尾插法**，避免链表成环

JDK7 使用头插法，且需要重新计算每个元素的 hash（因为容量变化了），这是 JDK7 并发扩容死循环的根本原因。

---

### Q: 为什么 ConcurrentHashMap 不允许 null key/value？

主要原因是**二义性问题**：

```java
V v = concurrentHashMap.get(key);
if (v == null) {
    // 无法判断：key 不存在？还是 key 对应的 value 本身就是 null？
}
```

这种二义性在单线程环境下可以通过额外标志位解决，但在并发环境下会导致竞态条件。

此外，null 值在 ConcurrentHashMap 的语义设计中也表示"未找到"或"计算中"，不允许用户显式存储 null 可以避免混淆。

---

### Q: HashMap 和 Hashtable 区别？

| 区别 | HashMap | Hashtable |
|------|---------|-----------|
| 线程安全 | 否 | 是（每个操作都加 synchronized） |
| 性能 | 高（无锁） | 低（全局锁） |
| key/value null | 都允许 | 都不允许 |
| 迭代器 | Fail-Fast | Fail-Fast |
| 底层结构 | 数组+链表+红黑树（JDK8） | 数组+链表 |
| 初始容量 | 16 | 11 |
| 扩容策略 | 容量 × 2 | 容量 × 2 + 1 |
| 同步方式 | 无 | synchronized |
| 引入版本 | JDK1.2 | JDK1.0 |

**建议**：Hashtable 是遗留类，已不推荐使用。需要线程安全时用 ConcurrentHashMap。

---

### Q: HashMap 的负载因子为什么是 0.75？

负载因子决定 HashMap 在什么时机扩容，本质是**时间与空间的平衡**：

**负载因子太小（如 0.5）**：
- 优点：冲突减少，查询效率高
- 缺点：空间浪费严重，数组利用率低

**负载因子太大（如 1.0）**：
- 优点：空间利用率高
- 缺点：冲突增多，链表/红黑树变长，查询性能下降

**0.75 的选择依据**：
- 空间利用率和查询性能的折中
- 在 put 操作触发扩容前，有足够的空间
- 根据泊松分布，0.75 时链表长度的期望值约为 0.5，树化阈值 8 几乎不可能达到

---

### Q: JDK8 HashMap 为什么用尾插法替代头插法？

**JDK7 头插法的问题**：

```java
// JDK7 扩容代码
e.next = newTable[i];
newTable[i] = e;
```

头插法会**反转链表顺序**。在并发扩容时：
1. 线程 A 遍历链表，A → B → C
2. 线程 A 将 A 头插到新数组
3. 线程 B 也遍历同一个链表（此时链表可能已被线程 A 修改）
4. 指针交错导致链表成环

**JDK8 尾插法**：

```java
// JDK8 扩容代码
e.next = null;
tail.next = e;
tail = e;
```

尾插法**保持链表顺序**，不会反转。配合 `(e.hash & oldCap) == 0` 的位置判断，即使多线程并发扩容，也不会出现成环问题。

**注意**：JDK8 的 ConcurrentHashMap 扩容仍然支持多线程并发，但不会死循环。

---

## 关联笔记

- [[锁机制与并发原语]]
- [[简历知识点总结]]
- [[运达面试专区]]

## 参考资源

- [[MOC-Java面试]]
