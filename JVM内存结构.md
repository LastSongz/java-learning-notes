---
title: "JVM 内存结构"
created: 2026-04-11
updated: 2026-05-19
tags:
  - 分类/jvm
  - 分类/java
  - 分类/面试
  - 运达
status: complete
category: jvm
---

# JVM 内存结构

> 8年经验面试速查，[[运达面试专区]]专版。核心知识点全覆盖，适合快速回忆和深度理解。

---

## 一、JVM 运行时数据区

运行时数据区是 JVM 内存管理的根基，分为线程私有和线程共享两大类。

### 1.1 程序计数器（PC Register）

线程私有，每个线程独立拥有。

唯一不会产生 OutOfMemoryError 的区域。

作用：字节码行号指示器，线程恢复执行时从此位置继续。

```java
// 典型场景：分支、循环、异常处理、线程切换
public class Example {
    public int method(int x) {
        if (x > 0) {        // PC 记录这个位置
            return x * 2;
        } else {
            return -x;      // 或者这个位置
        }
    }
}
```

执行 Native 方法时，计数器为空（Undefined）。

### 1.2 虚拟机栈（VM Stack）

线程私有，生命周期与线程相同。

每个方法调用创建一个栈帧（Stack Frame），方法完成时栈帧出栈。

#### 栈帧结构

| 组成部分 | 作用 |
|----------|------|
| 局部变量表 | 存放方法参数和局部变量，容量编译时确定 |
| 操作数栈 | 方法执行时的临时操作空间，先进后出 |
| 动态链接 | 解析符号引用为直接引用 |
| 方法返回地址 | 方法退出后需要恢复的执行位置 |

#### 两种错误

| 错误类型 | 原因 | 场景 |
|----------|------|------|
| StackOverflowError | 栈深度超过限制 | 递归调用没有正确退出条件 |
| OutOfMemoryError | 无法申请足够内存 | 创建大量线程，每个占用大量栈空间 |

```java
// StackOverflowError 示例
public class StackOverflow {
    public static void recursion() {
        recursion(); // 无限递归，栈深度不断增加
    }
    public static void main(String[] args) {
        recursion();
    }
}
```

-Xss 参数控制栈大小，默认 1MB。

### 1.3 本地方法栈（Native Method Stack）

为 JVM 执行 Native 方法服务。

与虚拟机栈类似，但服务于 Native 代码。

HotSpot 虚拟机将两者合并实现。

### 1.4 堆（Heap）

所有线程共享，GC 的主要战场。

用于存放对象实例和数组。

#### 分代结构（JDK8+）

```
堆
├── 年轻代（Young Generation）
│   ├── Eden 区（伊甸园区）
│   ├── Survivor 0（From 区）
│   └── Survivor 1（To 区）
└── 老年代（Old Generation）
```

#### 分代比例（默认）

| 参数 | 默认值 | 说明 |
|------|--------|------|
| NewRatio | 2 | 老年代/年轻代 = 2:1 |
| SurvivorRatio | 8 | Eden/Survivor = 8:1 |
| MaxNewSize | - | 年轻代最大大小 |

#### 对象分配流程

```
1. 检查 TLAB（Thread Local Allocation Buffer）
   └─ 是 → 在 TLAB 分配，失败则走步骤2
2. 在 Eden 区分配
   └─ 成功 → 完成
   └─ 失败 → 触发 Minor GC
3. Minor GC 后再次尝试 Eden 分配
   └─ 成功 → 完成
   └─ 失败 → 尝试 Survivor 区
4.  Survivor 区分配
   └─ 成功 → 对象年龄+1
   └─ 失败 → 对象进入老年代
5. 老年代分配
   └─ 成功 → 完成
   └─ 失败 → 触发 Full GC
6. Full GC 后仍失败 → OOM
```

#### TLAB 机制

线程本地分配缓冲，解决多线程分配对象时的竞争问题。

每个线程在 Eden 区拥有自己的 TLAB 空间。

```java
// -XX:+UseTLAB 开启（默认开启）
// -XX:TLABSize 设置大小
// -XX:+ResizeTLAB 动态调整
```

### 1.5 元空间（Metaspace）

JDK 8 及之后使用，替代了 JDK 7 及之前的永久代。

#### 存储内容

- 类元数据（类的结构信息）
- 字段信息
- 方法信息
- 构造器/方法字节码
- 常量池
- 即时编译器优化信息

#### 为什么用元空间替代永久代

| 对比项 | 永久代 | 元空间 |
|--------|--------|--------|
| 位置 | 堆内（受堆大小限制） | 本地内存（堆外） |
| 大小 | 固定，难以调整 | 动态增长，受物理内存限制 |
| Full GC | 触发 Full GC 才能回收 | 使用 MetaspaceSize 触发 GC |
| 调优 | PermGenSize | MaxMetaspaceSize |

#### Metaspace OOM 排查

```bash
# 监控
jstat -gcutil <pid> 1000

# 导出堆信息
jmap -dump:format=b,file=heap.hprof <pid>

# 查看类加载统计
jstat -class <pid>

# Metaspace 相关参数
-XX:MaxMetaspaceSize=256m      # 最大元空间
-XX:MetaspaceSize=128m         # 初始阈值
-XX:MinMetaspaceFreeRatio=40   # 最小空闲比例
-XX:MaxMetaspaceFreeRatio=70   # 最大空闲比例
```

### 1.6 直接内存（Direct Memory）

不属于 JVM 运行时数据区，是堆外内存。

NIO 的 ByteBuffer 使用直接内存，避免 Java 堆和本地堆之间数据复制。

```java
// 直接内存分配示例
ByteBuffer buffer = ByteBuffer.allocateDirect(1024 * 1024 * 100); // 100MB 直接内存
```

#### 常见使用场景

- Netty 高性能网络框架
- RocksDB 等本地存储
- 大文件读写

#### 常见问题

不受堆大小限制，但受物理内存和 -XX:MaxDirectMemorySize 限制。

如果忘记设置，可能导致物理内存耗尽。

### 1.7 运行时数据区总结

```
┌─────────────────────────────────────────────────────────────┐
│                        运行时数据区                          │
├─────────────────────────────────────────────────────────────┤
│  线程私有                                                   │
│  ├─ 程序计数器        ─ 唯一不会 OOM                        │
│  ├─ 虚拟机栈          ─ 栈帧（局部变量表、操作数栈、动态链接）│
│  └─ 本地方法栈        ─ Native 方法服务                      │
├─────────────────────────────────────────────────────────────┤
│  线程共享                                                   │
│  ├─ 堆                ─ 对象分配、GC 主要区域                │
│  ├─ 元空间            ─ 类元数据（JDK8+）                    │
│  └─ 直接内存          ─ NIO 使用，堆外内存                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、JMM（Java Memory Model）内存模型

JMM 是 JDK 5 引入的规范，定义了程序中各个变量的访问规则。

### 2.1 主内存 vs 工作内存

| 概念 | 说明 |
|------|------|
| 主内存 | 所有变量存储的位置，对应堆内存 |
| 工作内存 | 线程私有的内存区域，存储主内存副本 |

```
线程A                      线程B
┌────────┐                ┌────────┐
│ 工作内存 │←→ 主内存 ←→│ 工作内存 │
└────────┘                └────────┘
```

线程间通信通过主内存传递。

### 2.2 三大特性

#### 可见性（Visibility）

一个线程对共享变量的修改，其他线程能立即看到。

```java
// 可见性问题示例
public class VisibilityDemo {
    private static boolean flag = true; // 共享变量
    
    public static void main(String[] args) throws InterruptedException {
        new Thread(() -> {
            while (flag) {
                // 可能永远看不到 flag 的变化
            }
        }).start();
        
        Thread.sleep(1000);
        flag = false; // 主线程修改
    }
}
// 解决方案：使用 volatile 或 synchronized
```

#### 原子性（Atomicity）

一个操作要么全部执行，要么全部不执行。

```java
// 原子性问题示例
private static int count = 0;

// count++ 不是原子操作（读取→修改→写入）
// 解决方案：AtomicInteger, synchronized, ReentrantLock
```

#### 有序性（Ordering）

程序执行顺序按代码顺序，但在多线程下可能发生指令重排。

```java
// 有序性问题示例
int a = 0;
int b = 0;
int c = 0;
// 可能被重排为 b = 0; c = 0; a = 0;
// 单线程没问题，多线程可能出问题
```

### 2.3 happens-before 规则

定义了两个操作之间的偏序关系，满足则保证可见性和有序性。

#### 8条核心规则

1. **程序顺序规则**：同一个线程中，前面的操作 happens-before 后面的操作
2. **解锁规则**：unlock 操作 happens-before 后续对同一个锁的 lock
3. **[[锁机制与并发原语]] 写规则**：volatile 写 happens-before 后续对同一个变量的 read
4. **线程 start 规则**：线程.start() happens-before 该线程的任何操作
5. **线程终止规则**：线程的所有操作 happens-before 其他线程检测到该线程终止
6. **中断规则**：线程.interrupt() happens-before 被中断线程检测到中断
7. **对象终结规则**：构造函数结束 happens-before finalize()
8. **传递性**：A happens-before B，B happens-before C，则 A happens-before C

### 2.4 内存屏障（Memory Barrier）

#### 四种屏障类型

| 屏障类型 | 说明 |
|----------|------|
| LoadLoad | 确保前面的 Load 先执行完再执行后面的 Load |
| StoreStore | 确保前面的 Store 刷新到主内存后再执行后面的 Store |
| LoadStore | 确保前面的 Load 执行完再执行后面的 Store |
| StoreLoad | 确保前面的 Store 刷新到主内存后，再执行后面的 Load |

#### volatile 底层实现

```java
// volatile 变量的读写
public volatile int value;

// 写操作：StoreStore + StoreLoad
// 读操作：LoadLoad + LoadStore
```

StoreLoad 是最重的屏障，跨越它后面的所有读写操作。

### 2.5 JMM 与运行时数据区关系

```
JMM 抽象模型                     运行时数据区
┌─────────────────┐            ┌─────────────────┐
│   主内存        │ ←───────→  │   堆（对象）     │
└─────────────────┘            └─────────────────┘
┌─────────────────┐            ┌─────────────────┐
│   工作内存      │ ←───────→  │   虚拟机栈       │
└─────────────────┘            │   （局部变量）    │
                               └─────────────────┘
```

---

## 三、对象内存布局

### 3.1 对象头（Header）

#### Mark Word（标记字）

32位/64位系统大小不同，记录对象运行时数据。

| 状态 | Mark Word 内容（32位） |
|------|----------------------|
| 无锁 | 对象哈希码 + 分代年龄 + 偏向标志(0) + 锁标志(01) |
| 偏向锁 | 线程ID + Epoch + 分代年龄 + 偏向标志(1) + 锁标志(01) |
| 轻量级锁 | 指向栈中锁记录的指针 + 锁标志(00) |
| 重量级锁 | 指向互斥量指针 + 锁标志(10) |
| GC 标记 | 空 + 锁标志(11) |

```java
// Mark Word 内容变化示意
对象刚创建 → 无锁状态（偏向标志=0，锁标志=01）
第一次被线程访问 → 膨胀为偏向锁（线程ID存储在Mark Word）
有竞争发生 → 膨胀为轻量级锁（指向栈中锁记录）
竞争加剧 → 膨胀为重量级锁（指向互斥量）
```

#### 类型指针（ Klass Pointer）

指向方法区中类元数据的指针，JVM 通过它确定对象类型。

开启压缩指针（-XX:+UseCompressedClassPointers）后为 32 位。

#### 数组长度（Array Length）

如果对象是数组，对象头中包含数组长度。

普通对象没有这个部分。

### 3.2 实例数据（Instance Data）

父类定义的字段在子类前面。

相同宽度的字段会分配在一起。

```java
class Parent {
    int x;           // 4字节
    long y;          // 8字节（可能需要对齐）
}

class Child extends Parent {
    int z;           // 4字节
}
// 字段顺序可能影响内存占用
```

### 3.3 对齐填充（Padding）

对象大小必须是 8 字节的整数倍。

不足时通过对齐填充补齐。

```java
// 计算对象大小
class Example {
    byte a;        // 1字节 + 3字节填充 = 4
    int b;         // 4字节
    byte c;        // 1字节 + 3字节填充 = 4
    // 总大小 = 12 + 8(对象头) = 20 → 填充到 24
}
// HotSpot 中对象头 = 8字节（普通对象）
```

### 3.4 对象内存布局图示

```
┌────────────────────────────────────────┐
│           对象头（Header）              │
│  ├─ Mark Word      (8字节，32位系统)   │
│  ├─ Klass Pointer (4字节，压缩)        │
│  └─ Array Length  (若有数组)           │
├────────────────────────────────────────┤
│           实例数据（Instance Data）    │
│  ├─ 父类字段                           │
│  └─ 子类字段                           │
├────────────────────────────────────────┤
│           对齐填充（Padding）           │
└────────────────────────────────────────┘
```

---

## 四、GC 调优核心概念

### 4.1 对象存活判定

#### 引用计数法

给对象添加引用计数器，引用+1，失效-1。

优点：简单高效。

缺点：无法解决循环引用问题。

```java
// 循环引用示例
Object A = new Object(); // refCount = 1
Object B = new Object(); // refCount = 1
A.ref = B;              // B.refCount = 2
B.ref = A;              // A.refCount = 2
A = null;               // A.refCount = 1
B = null;               // B.refCount = 1
// A 和 B 相互引用，但已经不可达
// 引用计数法无法回收，JVM 不采用
```

#### 可达性分析（Reachability Analysis）

从 GC Roots 向下搜索，标记不可达对象。

##### 常见 GC Roots

- 虚拟机栈（栈帧中本地变量表）中引用的对象
- 方法区中静态属性引用的对象
- 方法区中常量引用的对象
- 本地方法栈中 JNI（Native 方法）引用的对象
- 内部引用（ClassLoder、异常对象等）
- 所有被 synchronized 持有的对象

### 4.2 垃圾收集算法

#### 标记-清除（Mark-Sweep）

两个阶段：标记存活对象，清除未标记对象。

缺点：产生内存碎片，大对象分配困难。

```
清理前          清理后
████        ██
  ███    ██      ██
    █████    ███
  ██          ██
   内存碎片    空间不连续
```

#### 标记-复制（Mark-Copy）

将内存分为两半，每次只用一半。

存活对象复制到另一半，然后清理整区。

优点：没有内存碎片。

缺点：可用内存减半。

```
原始内存          复制后
┌─────────┐      ┌─────────┐
│ 存活对象 │ →   │ 存活对象 │
├─────────┤      └─────────┘
│ 可回收   │      │   空    │
└─────────┘      └─────────┘
```

#### 标记-整理（Mark-Compact）

标记存活对象，整理到一端，然后清理边界外内存。

优点：没有内存碎片，利用率高。

缺点：整理过程有性能开销。

```
整理前          整理后
████        ████████
  ███    ██
    █████
  ██
```

#### 分代收集（Generational Collection）

根据对象生命周期不同采用不同算法。

年轻代：对象存活率低，用标记-复制。

老年代：对象存活率高，用标记-整理。

### 4.3 常见垃圾收集器

#### 各代收集器对应

```
年轻代                    老年代
─────────                ─────────
Serial                   Serial Old
Parallel Scavenge        Parallel Old
ParNew                   CMS
                        G1
                        ZGC (JDK11+)
```

#### 收集器对比

| 收集器 | 线程 | 目标 | 内存占用 | 特点 |
|--------|------|------|----------|------|
| Serial | 单 | 响应时间短 | - | Client 模式默认，简单高效 |
| Serial Old | 单 | 响应时间短 | - | Serial 老年代版本 |
| ParNew | 多 | 响应时间短 | - | 多线程版 Serial，是 CMS 默认年轻代 |
| Parallel Scavenge | 多 | 吞吐量 | - | 吞吐量优先，CPU 利用率高 |
| Parallel Old | 多 | 吞吐量 | - | Parallel Scavenge 老年代版 |
| CMS | 多 | 响应时间短 | 老年代 | 并发收集，低停顿 |
| G1 | 多 | 响应时间短 | 全堆 | 区域化内存布局，可预测停顿 |
| ZGC | 多 | 响应时间短 | 全堆 | 着色指针，并发标记，极低停顿 |
| Shenandoah | 多 | 响应时间短 | 全堆 | 转发指针，无需重连 |

#### CMS 收集器流程

```
1. 初始标记（Initial Mark）
   └─ 标记 GC Roots 直接关联的对象，Stop The World

2. 并发标记（Concurrent Mark）
   └─ 遍历对象图，耗时最长，不停顿

3. 重新标记（Remark）
   └─ 修正并发期间变动的对象，Stop The World

4. 并发清除（Concurrent Sweep）
   └─ 清理死亡对象，不停顿
```

CMS 缺点：对 CPU 敏感，无法处理浮动垃圾（Concurrent Mode Failure），产生内存碎片。

#### G1 收集器

Garbage First，面向服务端的收集器。

将堆划分为多个大小相等的 Region（1MB~32MB）。

```
┌──────────────────────────────────────────┐
│                  G1 Heap                  │
├────┬────┬────┬────┬────┬────┬────┬────┤
│ E  │ S  │ O  │ O  │ E  │ S  │ O  │ O  │
│ Eden│Surv│Old │Old │Eden│Surv│Old │Old │
├────┴────┴────┴────┴────┴────┴────┴────┤
│        Humongous（大对象专用Region）      │
└──────────────────────────────────────────┘
```

G1 特点：

- 区域化内存布局，避免内存碎片
- 可预测停顿（-XX:MaxGCPauseMillis 默认200ms）
- 优先回收价值最大的 Region（垃圾最多的）
- Mixed GC 可同时回收年轻代和老年代

#### G1 vs CMS 深度对比

| 对比项 | G1 | CMS |
|--------|----|----|
| 内存模型 | Region 分区，整体连续 | 老年代连续空间 |
| 碎片问题 | 整理后几乎无碎片 | 产生内存碎片 |
| 停顿时间 | 可预测，通过参数控制 | 不确定，浮动垃圾多时频繁 Full GC |
| 适用范围 | 全堆，适合大内存（JDK9+默认） | 老年代，反应式低停顿 |
| 并发阶段 | 并发标记和并发清理都有 | 并发标记和并发清理都有 |
| 写屏障 | Columbia | Update CMS |
| 复杂度和调优 | 相对复杂 | 相对简单 |
| 老年代处理 | Mixed GC | Full GC |

### 4.4 Full GC 频繁排查思路

#### 常见原因

1. 老年代空间不足
2. 元空间不足
3. 分配担保失败
4. CMS GC 失败（Concurrent Mode Failure）
5. 老年代碎片化严重

#### MAT 工具排查流程

```bash
# 1. 导出堆转储
jmap -dump:format=b,file=heap.hprof <pid>

# 2. 打开 MAT 分析
# 导入 heap.hprof 文件

# 3. Dominator Tree 分析
# 找出占用内存最大的对象链

# 4. 查找 GC Roots
# 找到不可回收的对象

# 5. 常见问题模式
# - 静态集合持有大量对象
# - 连接池未关闭
# - 缓存未清理
# - 监听器未注销
```

```java
// 常见内存泄漏示例
public class MemoryLeak {
    // 静态集合持有对象引用，不清理导致内存泄漏
    private static List<Object> cache = new ArrayList<>();
    
    public void add(Object obj) {
        cache.add(obj); // 只增不减，内存持续增长
    }
}
```

---

## 五、面试高频速查（Q&A 格式）

### Q: 所有的对象都在堆上分配吗？

不是。JVM 通过逃逸分析（Escape Analysis）优化。

逃逸分析判断对象的作用域是否逃出方法。

#### 栈上分配（Stack Allocation）

如果对象没有逃逸出方法，可以栈上分配。

```java
public void method() {
    Object obj = new Object();
    // 只有方法内部使用，没有逃逸
    // JIT 可能直接在栈上分配，方法结束自动回收
}
```

#### 标量替换（Scalar Replacement）

如果对象可以拆解为原始类型（标量），则不创建对象，直接使用字段。

```java
// 标量替换示例
public class ScalarReplacement {
    static class Point {
        int x;
        int y;
    }
    
    public static void main(String[] args) {
        Point p = new Point();
        p.x = 1;
        p.y = 2;
        // 编译器可能替换为直接使用 int x = 1; int y = 2;
        // 不创建 Point 对象
    }
}
```

#### 相关参数

```bash
# 开启逃逸分析（JDK8 默认开启）
-XX:+DoEscapeAnalysis

# 开启标量替换（JDK8 默认开启）
-XX:+EliminateAllocations

# 查看分配情况
-XX:+PrintGC
```

### Q: 为什么要有 Survivor 区？

减少对象直接进入老年代，降低 Full GC 频率。

#### 工作原理

1. 对象在 Eden 区分配
2. Minor GC 后，存活对象复制到 Survivor 0
3. 下一次 Minor GC，Eden + Survivor 0 一起清理，存活对象复制到 Survivor 1
4. 年龄达到阈值（默认15，-XX:MaxTenuringThreshold）后进入老年代

#### 为什么需要两个 Survivor 区

解决复制算法空间效率问题。

使用复制收集时，将可用内存分为两块，每次只用一块。

Survivor 区采用两半交替使用策略，避免空间浪费。

```
Minor GC 前:
┌──────┬──────┬─────────────────┐
│ Eden │ S0   │       老年代     │
└──────┴──────┴─────────────────┘

Minor GC 后（存活对象复制到 S1）:
┌──────┬──────┬─────────────────┐
│ 空   │ S1   │       老年代     │
└──────┴──────┴─────────────────┘
```

### Q: G1 收集器的 Region 有什么用？

Region 是 G1 将堆内存划分的基本单位。

#### 核心作用

1. **区域化管理**：将堆分为多个大小相等的 Region，每个Region独立管理
2. **化整为零**：将整堆回收分解为多个 Region 的小规模回收
3. **价值优先**：优先回收垃圾最多的 Region（Garbage First）
4. **灵活性**：根据回收时间目标动态调整回收区域

#### 大对象（Humongous Objects）

大于 Region 一半的对象称为大对象。

- 存储在连续 Humongous Region 中
- 跨 Region 存储
- 回收优先级最低

### Q: 线上 CPU 100% 怎么排查？

#### 排查步骤

```bash
# 1. top 查看整体 CPU 使用情况
top

# 2. 找到 Java 进程的高 CPU 线程
top -Hp <pid>

# 3. 获取线程 ID（十进制）转换为十六进制
printf "%x\n" <thread-id>

# 4. jstack 打印线程堆栈
jstack <pid> > thread_dump.log

# 5. 在堆栈文件中搜索线程 ID
# 找到对应线程的堆栈信息
```

#### 示例

```bash
# 定位高 CPU 线程
top -Hp 12345

# 假设找到线程 ID 12346，转换为十六进制
printf "%x\n" 12346
# 输出: 303a

# 查看堆栈
jstack 12345 | grep -A 20 "nid=0x303a"
```

#### 常见原因

- 死循环
- 频繁 GC
- 正则表达式匹配（回溯）
- 序列化/反序列化
- 加密解密计算

### Q: OOM 排查全流程？

#### 常见 OOM 类型

| OOM 类型 | 原因 |
|----------|------|
| Java heap space | 对象分配超过堆大小 |
| Metaspace | 类元数据超过元空间 |
| Direct buffer memory | 直接内存不足 |
| unable to create new native thread | 线程数超过限制 |
| GC overhead limit exceeded | GC 时间和回收比例超限 |

#### 排查流程

```bash
# 1. 添加 JVM 参数，OOM 时生成堆转储
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/path/to/dump.hprof

# 2. 手动导出（发现问题后）
jmap -dump:format=b,file=dump.hprof <pid>

# 3. 分析堆转储
# 使用 MAT / JProfiler / async-profiler

# 4. MAT 分析步骤
# - 打开 dump 文件
# - Histogram 查看对象数量和大小
# - Dominator Tree 查看内存占用分布
# - Top Consumers 找最大对象
# - Path from GC Roots 找引用链
```

```java
// 常见 OOM 场景示例
public class OOMExample {
    // 场景1：内存泄漏
    private static List<byte[]> leak = new ArrayList<>();
    public void memoryLeak() {
        leak.add(new byte[1024 * 1024]); // 只增不减
    }
    
    // 场景2：老年代分配大对象
    public void bigObject() {
        // 超过 Survivor 区承受范围，直接进入老年代
        // 老年代无法容纳时 OOM
    }
}
```

### Q: 什么是内存泄漏？和内存溢出的区别？

#### 内存泄漏（Memory Leak）

程序运行过程中不断分配内存，但不再使用的对象无法被回收。

长周期对象持有短周期对象的引用，导致短周期对象无法回收。

```java
// 内存泄漏示例
public class MemoryLeakExample {
    private static List<Object> list = new ArrayList<>();
    
    public void leak() {
        Object obj = new Object();
        list.add(obj);
        // obj 不再使用，但 list 持有引用，永远无法回收
        // 只有 list 被清理时才能释放
    }
}
```

#### 内存溢出（OutOfMemoryError）

程序申请的内存超过系统能提供的内存。

可以是内存泄漏导致，也可以是业务确实需要大内存。

#### 区别

| 对比项 | 内存泄漏 | 内存溢出 |
|--------|----------|----------|
| 原因 | 引用未释放 | 内存确实不够 |
| 表现 | 内存持续增长 | 无法分配内存 |
| 解决方案 | 找到泄漏源，释放引用 | 调大内存或优化使用 |
| 关系 | 泄漏可能导致溢出 | 不一定由泄漏引起 |

---

## 关联笔记

关联笔记: [[