---
title: "MYSQL面试突击-事务与锁"
created: 2026-05-19
updated: 2026-05-19
tags:
  - 分类/数据库
  - 分类/面试
  - 主题/事务
  - 主题/锁与并发
status: complete
category: database
---

# MYSQL面试突击---事务与锁

### 1、什么是 MySQL 事务？事务的核心作用是什么？

核心回答：事务是数据库中一组**不可分割的操作集合**，要么全部执行成功（提交），要么全部执行失败（回滚）；核心作用是保证多步操作的**数据一致性和完整性**（如转账、订单创建等场景，避免部分操作成功导致数据异常）。

### 2、事务的 ACID 特性分别指什么？MySQL 如何保证这四大特性？

- **A（Atomicity，原子性）**：事务是最小执行单元，要么全成，要么全败；由**undo log（回滚日志）** 保证（记录操作的反向逻辑，回滚时执行反向操作恢复数据）。
- **C（Consistency，一致性）**：事务执行前后，数据库从一个一致状态到另一个一致状态（如转账前后总金额不变）；由原子性、隔离性、持久性共同保证，同时依赖业务逻辑校验。
- **I（Isolation，隔离性）**：多个并发事务之间相互隔离，互不干扰；由**[[MVCC多版本并发控制]]（多版本并发控制）+ 锁机制** 保证。
- **D（Durability，持久性）**：事务提交后，修改永久保存，即使数据库崩溃也不会丢失；由**redo log（重做日志）** 保证（先写日志再异步刷盘）。

### 3、数据库事务的隔离级别有哪些？

SQL 标准定义 4 个隔离级别（从低到高）：

- 读未提交（Read Uncommitted）：能读取到其他事务**未提交**的数据；

- 读已提交（Read Committed）：只能读取到其他事务**已提交**的数据；

- 可重复读（Repeatable Read，RR）：同一事务内多次读取同一数据，结果一致；

- 串行化（Serializable）：最高级别，事务串行执行，完全避免并发问题。

  MySQL 差异：InnoDB 默认隔离级别是RR，且通过 Next-Key Lock 解决了 SQL 标准中 RR 级别仍存在的 “幻读” 问题。

### 4、各种隔离级别会出现什么异常情况

| 隔离级别          | 脏读 | 不可重复  读 | 幻读 |
| ----------------- | ---- | ------------ | ---- |
| READ- UNCOMMITTED | √    | √            | √    |
| READ-COMMITTED    | ×    | √            | √    |
| REPEATABLE- READ  | ×    | ×            | √    |
| SERIALIZABLE      | ×    | ×            | ×    |

### 5、什么是幻读，如何解决？

事务A按照一定条件进行数据读取，期间事务B插入了相同搜索条件的新数据，事务A再次按照原先条件进行读取时，发现了事务B新插入的数据称之为幻读。

```sql
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB ;

INSERT into user VALUES (1,'1',20),(5,'5',20),(15,'15',30),(20,'20',30);
```

假设有如下业务场景：

| 时间 | 事务1                                                        | 事务2                                       |
| ---- | ------------------------------------------------------------ | ------------------------------------------- |
|      | begin；                                                      |                                             |
| T1   | select * from user where age = 20;2个结果                    |                                             |
| T2   |                                                              | insert into user values(25,'25',20);commit; |
| T3   | select * from user where age =20;2个结果                     |                                             |
| T4   | update user set name='00' where age =20;此时看到影响的行数为3 |                                             |
| T5   | select * from user where age =20;三个结果                    |                                             |

执行流程如下：

1、T1时刻读取年龄为20 的数据，事务1拿到了2条记录

2、T2时刻另一个事务插入一条新的记录，年龄也是20 

3、T3时刻，事务1再次读取年龄为20的数据，发现还是2条记录，事务2插入的数据并没有影响到事务1的事务读取

4、T4时刻，事务1修改年龄为20的数据，发现结果变成了三条，修改了三条数据

5、T5时刻，事务1再次读取年龄为20的数据，发现结果有三条，第三条数据就是事务2插入的数据，此时就产生了幻读情况

此时大家需要思考一个问题，在当下场景里，为什么没有解决幻读问题？

其实通过前面的分析，大家应该知道了快照读和当前读，一般情况下select * from ....where ...是快照读，不会加锁，而 for update,lock in share mode,update,delete都属于当前读，**如果事务中都是用快照读，那么不会产生幻读的问题，但是快照读和当前读一起使用的时候就会产生幻读**。

如果都是当前读的话，如何解决幻读问题呢？

```sql
truncate table user;
INSERT into user VALUES (1,'1',20),(5,'5',20),(15,'15',30),(20,'20',30);
```

| 时间 | 事务1                                        | 事务2                                                |
| ---- | -------------------------------------------- | ---------------------------------------------------- |
|      | begin;                                       |                                                      |
| T1   | select * from user where age =20 for update; |                                                      |
| T2   |                                              | insert into user values(25,'25',20);此时会阻塞等待锁 |
| T3   | select * from user where age =20 for update; |                                                      |

此时，可以看到事务2被阻塞了，需要等待事务1提交事务之后才能完成，其实本质上来说采用的是间隙锁的机制解决幻读问题。

### 6、mysql的原子性的底层实现原理是什么？

mysql事务原子性的核心目标是保证事务内所有的操作要么全部执行成功提交，要么任意一步失败之后要回滚到最开始的状态，而这个目标的实现，需要依赖于innodb存储引擎的undolog（回滚日志）

首先要明确，undolog并不是记录数据的最终状态，而是记录数据修改操作的反向逻辑，这个反向逻辑并不是SQL语句，而是记录之前的旧的历史数据，相当于给每一步操作都做了一个可恢复的快照，为后续可能得回滚操作提供数据依据

undolog是一种逻辑日志，它记录的事如何恢复到操作前的状态，而不是数据页的物理变化，比如执行如下SQL：

update user set balance  = 900 where id = 1;(原来的值是1000)

undolog中不会记录balance最终的值是1000，而是会记录，id=1的数据行原始的数据结果值为1000

如果执行了一个delete的操作，比如delete from user id = 1

undolog中会记录id=1的数据的所有数据字段，而不是记录一条insert操作

这种逻辑记录的优势是体积小，回顾效率高，且不依赖于数据页的物理存储结构

针对于mysql的三种基本操作，insert，delete，update，undolog记录的策略是不同的，要确保回滚的时候能够精准的进行恢复：

**insert**：undolog中仅记录插入记录的主键值，因为插入的记录是全新的，回滚时只需要根据主键值就可以执行delete操作，就能删除这条新增的记录，恢复到之前的状态，所以此时是需要记录其他的数据信息的，效率比较高

**update**：undolog中记录被更新的字段的历史数据，回滚的时候，直接将字段值还原为undolog中记录的旧值即可，不需要记录其他没有更新的字段

**delete**：undolog中记录被删除记录的完整数据，因为删除后记录会被标记为删除状态，回滚时需要根据这些完整行记录执行insert操作，将被删除的记录重新插入到数据表中，恢复删除前的状态

---

mysql8版本之前，undolog的数据是存储在innodb的共享表空间的，有一个文件叫做ibdata1,而在8版本之后，undolog存储在独立的undo表空间中

undolog并不会无限增长，是会进行清除的，undolog的清除跟事务紧密相关

事务提交后，undolog并不会立刻删除，原因是undolog除了作为回滚操作的需要之外，还要给MVCC提供历史数据的支持，所以并不会立刻删除

undolog删除的操作是mysql的一个线程来执行的，叫做purge

purge有自己的规则，会定期的进行undolog的日志清除，此处不需要详细了解

### 7、MVCC的底层实现机制是什么？

详情看mvcc文件夹

### 8、mysql的持久性的实现原理是什么？

事务持久性的核心目标是事务一旦成功，对数据的修改就是永久性的，即使后续发生数据库崩溃，服务器宕机等异常情况，已经提交的数据也不会丢失

实现这一目标的核心底层机制是依赖于innodb存储引擎的redolog，同时需要配合WAL（write ahead log）预写日志的思想

redolog是一种物理日志，它记录的是数据页的物理修改，比如哪个数据页，哪个偏移量，修改了什么内容，在物理层面的修改而不是逻辑层面的修改，比如你更新了id=1的数据结构值，那么redolog在进行记录的时候会记录某个表的第多少页数据，偏移量100的位置数值从100改为200

这种物理记录的优势是，恢复数据的时候速度非常快，因为innodb会根据redolog中物理地址直接定位到数据，然后进行数据的修改，不需要进行SQL语句的解析，索引的数据查找

redolog中的存储是分为两部分存储的，分别是内存缓冲+磁盘的持久化操作，这种方式既能够保证性能，也可以保证数据的安全性

内存层面：log buffer的区域，主要用来缓存数据，redolog在记录的时候会优先写入log buffer中，这是内存的操作，速度非常快，可以避免每次写操作都直接操作磁盘，提成数据库的写入性能

磁盘层面：存储redolog的文件叫做ib_logfile,innodb默认在数据目录下生成2个循环使用的日志文件（ib_logfile0,ib_logfile1）,这是redolog的最终持久化存储，redolog采用循环写的方式，当日志写满一个文件之后，会切换到另外一个文件中，这个文件的切换操作由innodb来完成，用户不需要干预

如果2个文件都写满的话，会触发checkpoint的机制，清理掉已经不需要的日志文件，再从头开始进行写入

事务执行过程中，对于数据的修改操作，会先写入redolog中（先写入内存中的logbuffer，再按照需要刷写到磁盘的ib_logile中），然后再修改内存中的缓存池中的数据，最后在合适的时机，由innodb异步将缓冲池的数据刷写到磁盘的数据文件中

![img](image\redolog)

redolog中有一个非常重要的参数：innodb_flush_log_at_trx_commit，这个参数可以确定redolog的刷盘机制

1：事务提交的时候，立即将logbuffer中的redolog同步刷写到磁盘中，并调用操作系统的fsync（）函数确保数据落盘，这是最安全的配置，即使立刻发生宕机，已经提交的事务数据也不会丢失，完全符合持久化的要求，但是性能层面有损耗

0：事务提交的时候，不刷盘，仅仅将redolog留在log buffer中，由innodb后台线程来控制每秒刷盘一次，性能最高，但是安全性最差，如果宕机，那么会丢失最近1秒内的数据

2：事务提交的时候，将log buffer中的redolog写入操作系统的OS buffer中，由操作系统每秒将文件缓存中的数据刷写到磁盘，性能介于0和1之间，安全性比0高，但是比1低，如果操作系统宕机，那么仍然会丢失1秒的数据

在进行时机的参数选择的过程中，绝大部分场景还是选择参数为1的情况，要尽可能的保证数据的安全

![image-20260304213310567](image\image-20260304213310567.png)

### 9、什么是redolog和binlog的两阶段提交

redolog是innodb存储引擎专属的物理日志，记录的是哪个数据页在哪个偏移量上进行了什么样的修改，核心 作用的保证事务的持久性，用于mysql崩溃之后的快速数据恢复

binlog是mysql 服务器层面的二进制日志文件，文件有三种格式，分别是statement，row，mixed，核心作用是主从复制和数据备份恢复

那么为什么会出现两阶段提交呢？其实非常简单，因为两种日志位于不同的层次，当进行对应的SQL操作的时候都会进行日志的记录，那么先写谁，后写谁就会成为问题，因此引入了两阶段提交

所谓的两阶段提交就是将一个事务的提交过程拆分为准备阶段和提交阶段两个步骤，报缺redolog和binlog的日志原子性，要么两者都完整的持久化到磁盘中，要么两者都不持久化，不会出现一个成功，一个失败的情况，这种机制是为了保证数据一致性而存在的

完整的执行过程：

1、当开启事务之后，执行SQL语句，会记录对应的redolog，此时redolog位于log buffer，持久化要根据参数来判定，然后修改buffer pool中的数据，然后再记录binlog，同样，binlog的持久化也是由参数来配置的

2、执行commit指令之后，innodb存储引擎会将当前事务的log buffer中的redolog进行持久化操作，此时redolog中记录了数据修改相关的信息，此时的日志状态为prepare，而不是 commit，这步骤完成之后，binlog日志也开始进行对应的持久化操作

3、当mysql的server将当前事务的binlog持久化成功之后，会向innodb存储引擎发送提交确认的消息，innodb收到之后，会将之前的prepare状态的redolog文件修改为commit状态，

4、innodb可以释放对应的资源，向客户端返回事务执行成功的响应，整个事务提交流程结束

至于为什么需要给日志添加状态来保证数据一致性，可以通过反证法的方式来验证

（1）先写binlog，然后再写redolog

假设binlog已经成功刷盘，但是redolog还没有来得及刷盘，此时mysql突然崩溃了，重启之后，innodb存储引擎因为没有对应的redolog记录，会将事务回滚，数据保持一致，但是binlog中已经有了这条事务的执行记录，在进行主从复制的过程中，从库就会执行这条binlog日志，导致从库的数据比主库多一条记录，主从的数据不一致了

（2）先写redolog，再写binlog

假设redolog已经成功刷盘，binlog还没有刷盘，mysql崩溃之后，重启，innodb引擎通过redolog进行数据恢复的时候，该事务会被提交，数据生效，但是binlog中并没有这条记录，主从复制的时候也不会同步这条数据，那么就会出现主库有，从库没有的情况，主从数据不一致了

通过对redolog添加状态的方式就可以解决这个问题，如何进行崩溃的恢复呢？

当mysql崩溃重启之后，innodb引擎会自动触发崩溃恢复的流程，核心是扫描redolog，根据redolog的状态和对应binlog的完整性，来决定事务的最终走向，从而确保数据的一致性

1、redolog中没有记录，或者只有部分记录，没有prepare标记，说明事务还没有开始，直接回滚即可，没有数据一致性的问题

2、redolog的状态是prepare，但是找不到对应的完整binlog，说明准别阶段完成，但是提交阶段没有完成，此时会回滚事务，保证redolog和binlog数据一致

3、redolog为prepare状态，能够找到与之匹配的binlog日志，说明binlog已经刷盘，只是还没有来得及修改redolog的状态为commit，此时innodb会自动完成commit操作，恢复事务，确保数据一致

### 10、mysql中有哪些锁？

innodb的锁体系是围绕高并发和数据一致性来设计的，核心以行锁为主，同时配套表级锁，意向锁还有针对于行锁的细分锁（记录锁，间隙锁，临键锁），当然还有特殊场景的自增锁

首先从锁的粒度来进行拆分的话，innodb支持表级锁和行级锁，其中行级锁是innodb区别于myisam的核心优势，也是支持高并发系统的关键

#### 表锁

表锁可以分为共享读锁和排他写锁，innodb并不会默认优先使用表级锁，只有在特殊场景下才会触发，比如执行SQL语句lock tables .... read/write，还有就是在执行DDL语句的时候会触发表锁，阻塞所有其他线程对该表进行DDL操作

表级锁的特点是粒度大，加锁开销小，速度快，不会出现死锁的情况，但是并发性能差，适合低并发、全表操作的场景

#### 意向锁

意向锁是mysql为了协调表级锁和行级锁，引入的特殊的标记锁，可以分为共享读锁和排他写锁，可以根据意向锁快速的判断表中是否存在行锁，避免全表扫描检查行锁

这里有个关键的锁兼容规则，意向锁之间相互兼容，以为他们只是进行标记操作，不会影响彼此，还有就是意向锁和表级锁之间是互斥的原则，只有表共享锁与意向锁兼容，其他的都是排斥的

#### 行级锁

行级锁是支撑mysql高并发的核心，粒度细，并发性能好，但是加锁的开销相对较大，可能会出现死锁的情况

行级锁又可以做细粒度的拆分，分为记录锁，间隙锁，临键锁

##### 记录锁

锁定的是索引上的某一条具体的记录，不存在间隙，在RR和RC隔离级别下都存在，典型的场景就是使用唯一索引

##### 间隙锁

锁定的事两个索引记录之间的间隙，或者索引记录之前或者之后的空白区间，他不锁定具体的行记录，只是阻止其他事务在间隙之间插入新数据，核心的目的是为了避免幻读，需要主要的是间隙锁仅在RR隔离级别下存在，RC隔离级别是不存在，而且间隙锁之间相关兼容，多个事务可以同时锁定同一个间隙，因为他的表示防止插入，而不是修改已有的数据

##### 临键锁

临键锁是innodb存储引擎在RR隔离级别下的默认行锁算法，是记录锁+间隙锁的组合，锁定的是一个左开右闭的索引区间，默认情况下，innodb对非唯一索引的等值查询、所有范围查询都会触发临键锁

#### 自增锁

这是innodb针对自增列的特殊表级锁，目的是为了保证自增只的唯一性和连续性，他有三种锁模式，分别是连续模式，交错模式，传统模式，当然我们在日常使用的时候不需要关心它锁的模式是什么，知道有自增锁即可

#### 总结：

mysql中支持的锁的类型是比较多的，主要是目标是为了保证效率和一致性，在工作中可以根据业务的需要来合理的设置锁：select ... lock in share mode，select ... for update

### 11、mysql中的加锁情况

参考mysql中的加锁情况文档

### 12、什么是乐观锁，什么是悲观锁？

无论是乐观锁还是悲观锁，都是为了解决并发冲突问题，只不过两者的假设不同：

- 悲观锁：假设一定会出现冲突，提前加锁阻止其他操作，避免冲突
- 乐观锁：假设大概率不会发生冲突，全程不加锁，只在最后更新时验证是否冲突

#### 悲观锁：

悲观锁认为并发操作中数据冲突是必然的，因此在整个数据处理过程中，会将目标数据锁定，阻止其他事务对该数据的修改，直到当前事务完成并释放锁。

在mysql的innodb存储引擎中，悲观锁主要是通过行级锁实现的：

- 排他锁：select ... for update,加锁之后其他事务无法读取、修改该数据
- 共享锁：select ... lock in share mode,加锁后其他事务可以读取数据但是无法修改数据

悲观锁适用于并发冲突概率高、数据一致性要求极高的场景（如金融交易、库存扣减、订单支付），在这种模式下冲突处理简单，能100%保证数据一致性，无需业务层进行额外的处理，但是加锁会导致其他事务阻塞等待，并发性能低，甚至会出现死锁

#### 乐观锁：

乐观锁认为并发操作中数据冲突是小概率事件，因此全程不进行加锁操作，仅在**更新数据的最后一刻**，检查数据是否被其他事务修改过：若未被修改则更新成功，若已被修改则放弃更新（或重试）

在mysql的innodb存储引擎中，乐观锁主要是通过版本标识来实现的，最常用的就是添加版本号字段，给表中添加version字段，更新的时候需要对比版本号

乐观锁适用于并发冲突概率低、追求高并发性能的场景（如电商商品详情页更新、用户资料修改、点赞 / 收藏），在这种模式下全程无锁，无阻塞，并发性能极高，不会出现死锁，但是冲突之后需要业务层进行处理，比如重试或者提示，高冲突场景下重试次数多，性能反而会下降

### 13、什么是死锁，如何解决死锁

死锁本质是多事务（通常是2个及以上）在并发执行的时候，互相持有对方需要的锁资源，且都拒绝释放自己持有的锁，导致所有的事务都陷入永久阻塞，无法推进的僵局，此时没有任何一个事务能继续执行，也无法自动解决，必须依赖外部干预才能够打破僵局

案例演示：

```sql
-- 创建测试表（必须用InnoDB引擎，支持行锁和事务）
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id` INT UNSIGNED NOT NULL PRIMARY KEY COMMENT '账户ID',
  `balance` DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '余额'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='账户表';

-- 插入2条测试数据
INSERT INTO `account` (id, balance) VALUES (1, 1000.00), (2, 1000.00);
```

按照下述图片的执行步骤执行：

![image-20260305112540064](image\image-20260305112540064.png)

运行之后出现死锁情况，死锁日志如下所示：

![image-20260305112707433](image\image-20260305112707433.png)

![image-20260305112735330](image\image-20260305112735330.png)

上图展示的是死锁的日志，正常情况下在执行show engine innodb status\G的时候会保留最后一次的死锁日志记录，如果线上环境中经常出现死锁，建议打开如下参数，此时会将死锁的日志打印在errorlog文件中：

```sql
SET GLOBAL innodb_print_all_deadlocks = 1;
```

下面我们来分析下这个死锁日志：

```
*** (1) TRANSACTION:
TRANSACTION 2507, ACTIVE 46 sec starting index read
mysql tables in use 1, locked 1
LOCK WAIT 3 lock struct(s), heap size 1128, 2 row lock(s)
MySQL thread id 8, OS thread handle 140008889452288, query id 215 localhost root statistics
select * from account where id = 2 for update
```

通过这段信息我们可以知道在执行select * from account where id = 2 for update的语句的时候触发了锁等待

```
*** (1) HOLDS THE LOCK(S):
RECORD LOCKS space id 16 page no 4 n bits 72 index PRIMARY of table `locktest`.`account` trx id 2507 lock_mode X locks rec but not gap
Record lock, heap no 2 PHYSICAL RECORD: n_fields 4; compact format; info bits 0
 0: len 4; hex 00000001; asc     ;;
 1: len 6; hex 0000000009c6; asc       ;;
 2: len 7; hex 82000000c20110; asc        ;;
 3: len 5; hex 800003e800; asc      ;;
```

通过这块的信息我们可以知道此事务持有的锁是主键索引上的记录锁，0: len 4; hex 00000001; asc     ;;表示持有的锁是id=1的锁

```
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 16 page no 4 n bits 72 index PRIMARY of table `locktest`.`account` trx id 2507 lock_mode X locks rec but not gap waiting
Record lock, heap no 3 PHYSICAL RECORD: n_fields 4; compact format; info bits 0
 0: len 4; hex 00000002; asc     ;;
 1: len 6; hex 0000000009c6; asc       ;;
 2: len 7; hex 82000000c2011d; asc        ;;
 3: len 5; hex 800003e800; asc      ;;
```

通过这块信息我们可以知道此事务在等待记录锁， 0: len 4; hex 00000002; asc     ;;表示等待的是id=2的记录锁

```
*** (2) TRANSACTION:
TRANSACTION 2508, ACTIVE 33 sec starting index read
mysql tables in use 1, locked 1
LOCK WAIT 3 lock struct(s), heap size 1128, 2 row lock(s)
MySQL thread id 9, OS thread handle 140008556136192, query id 216 localhost root statistics
select * from account where id = 1 for update
```

通过这段信息我们可以知道在执行select * from account where id = 1 for update的语句的时候触发了锁等待

```
*** (2) HOLDS THE LOCK(S):
RECORD LOCKS space id 16 page no 4 n bits 72 index PRIMARY of table `locktest`.`account` trx id 2508 lock_mode X locks rec but not gap
Record lock, heap no 3 PHYSICAL RECORD: n_fields 4; compact format; info bits 0
 0: len 4; hex 00000002; asc     ;;
 1: len 6; hex 0000000009c6; asc       ;;
 2: len 7; hex 82000000c2011d; asc        ;;
 3: len 5; hex 800003e800; asc      ;;
```

通过这段信息我们可以知道此事务持有的锁是主键索引上的记录锁，0: len 4; hex 00000002; asc     ;;表示持有的锁是id=2的锁

```
*** (2) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 16 page no 4 n bits 72 index PRIMARY of table `locktest`.`account` trx id 2508 lock_mode X locks rec but not gap waiting
Record lock, heap no 2 PHYSICAL RECORD: n_fields 4; compact format; info bits 0
 0: len 4; hex 00000001; asc     ;;
 1: len 6; hex 0000000009c6; asc       ;;
 2: len 7; hex 82000000c20110; asc        ;;
 3: len 5; hex 800003e800; asc      ;;
```

通过这块信息我们可以知道此事务在等待记录锁，0: len 4; hex 00000001; asc     ;;表示等待的事id=1的记录锁

因为相互之间彼此持有了对方需要的资源，所以判断死锁，然后进行回滚，回滚的是事务2

```
*** WE ROLL BACK TRANSACTION (2)
```

想要解决死锁的问题，有几种常用的手段：

1、固定加锁的顺序，所有的事务按照id升序的方式来加锁：

```sql
SELECT * FROM account WHERE id = 1 FOR UPDATE; -- 先锁小ID
SELECT * FROM account WHERE id = 2 FOR UPDATE; -- 再锁大ID
COMMIT;
```

2、缩短锁持有的时间，尽量避免长事务，我们的事务1时间是46秒，事务2时间是33秒，在生产环境中要尽量避免长事务

3、如果在生产环境中，定位到具体的阻塞情况的话，那么找到对应的线程ID，直接kill，可以通过如下命令找到线程ID

```sql
show processlist;
```

