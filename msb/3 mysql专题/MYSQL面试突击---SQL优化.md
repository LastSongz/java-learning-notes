---
title: "MYSQL面试突击-SQL优化"
created: 2026-05-19
updated: 2026-05-19
tags:
  - 分类/数据库
  - 分类/面试
  - 主题/sql优化
status: complete
category: database
---

# MYSQL面试突击---SQL优化

### 优化案例1：

#### 业务背景：

假定在某电商平台中，商品列表页日均访问量100万+，用户每次访问会查询商品基本信息+分类信息

有一个核心查询场景：根据分类ID筛选商品，按照销量降序、创建时间降序，显示商品ID，商品名称、售价、销量、分类名称，支持分页查询，每页20条

#### 产生问题：

在某些促销活动中，商品列表加载耗时过长，用户投诉卡顿，后台监控显示mysql查询耗时过高，具体耗时多少可以根据项目的需求来进行设定，在下面的文档中，我会把本机执行的时间截图显示

#### 具体数据表：

商品表：

```sql
CREATE TABLE `product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '商品ID（主键）',
  `product_name` varchar(255) NOT NULL COMMENT '商品名称',
  `category_id` bigint(20) NOT NULL COMMENT '分类ID（关联category表）',
  `price` decimal(10,2) NOT NULL COMMENT '商品售价',
  `stock` int(11) NOT NULL DEFAULT 0 COMMENT '库存',
  `sales` int(11) NOT NULL DEFAULT 0 COMMENT '累计销量',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态（1-上架，0-下架）',
  `remark` varchar(500) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='商品表';
```

商品分类表：

```sql
CREATE TABLE `category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '分类ID（主键）',
  `category_name` varchar(100) NOT NULL COMMENT '分类名称',
  `parent_id` bigint(20) NOT NULL DEFAULT 0 COMMENT '父分类ID（0-一级分类）',
  `sort` int(11) NOT NULL DEFAULT 0 COMMENT '排序权重',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='商品分类表';
```

插入商品分类表的数据

```sql
INSERT INTO `category` (category_name, parent_id, sort) VALUES 
-- 一级分类（parent_id=0），sort 1-10
('电子产品', 0, 1),('家用电器', 0, 2),('服饰鞋帽', 0, 3),('美妆护肤', 0, 4),('食品生鲜', 0, 5),
('家居日用', 0, 6),('运动户外', 0, 7),('母婴用品', 0, 8),('数码配件', 0, 9),('图书音像', 0, 10),
-- 二级分类：电子产品（parent_id=1），sort 11-14
('手机', 1, 11),('电脑', 1, 12),('平板', 1, 13),('智能设备', 1, 14),
-- 二级分类：家用电器（parent_id=2），sort 15-18
('冰箱', 2, 15),('洗衣机', 2, 16),('空调', 2, 17),('电视', 2, 18),
-- 二级分类：服饰鞋帽（parent_id=3），sort 19-22
('男装', 3, 19),('女装', 3, 20),('鞋子', 3, 21),('帽子', 3, 22),
-- 二级分类：美妆护肤（parent_id=4），sort 23-26
('护肤品', 4, 23),('彩妆', 4, 24),('香水', 4, 25),('美妆工具', 4, 26),
-- 二级分类：食品生鲜（parent_id=5），sort 27-30
('零食', 5, 27),('生鲜', 5, 28),('粮油', 5, 29),('饮料', 5, 30),
-- 二级分类：家居日用（parent_id=6），sort 31-34
('厨具', 6, 31),('家纺', 6, 32),('清洁用品', 6, 33),('收纳用品', 6, 34),
-- 二级分类：运动户外（parent_id=7），sort 35-38
('运动服饰', 7, 35),('健身器材', 7, 36),('户外装备', 7, 37),('球类运动', 7, 38),
-- 二级分类：母婴用品（parent_id=8），sort 39-42
('婴儿奶粉', 8, 39),('婴儿服饰', 8, 40),('玩具', 8, 41),('母婴洗护', 8, 42),
-- 二级分类：数码配件（parent_id=9），sort 43-46
('手机壳', 9, 43),('充电器', 9, 44),('耳机', 9, 45),('数据线', 9, 46),
-- 二级分类：图书音像（parent_id=10），sort 47-50
('小说', 10, 47),('教材', 10, 48),('杂志', 10, 49),('音像制品', 10, 50);
```

插入商品表的数据：商品表的数据较多，所以需要通过mysql函数来生成，直接粘贴执行即可，因为数据较多，可能会耗费的时间较久，

```sql
-- 存储过程：生成100万条商品数据
DELIMITER //
CREATE PROCEDURE generate_product_data()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 1000000 DO
    INSERT INTO `product` (product_name, category_id, price, stock, sales, create_time, update_time, status)
    VALUES (
      CONCAT('测试商品', i), -- 商品名称
      FLOOR(1 + RAND() * 50), -- 随机关联50个分类
      ROUND(10 + RAND() * 999, 2), -- 售价10-1009.99元
      FLOOR(10 + RAND() * 990), -- 库存10-1000
      FLOOR(0 + RAND() * 10000), -- 销量0-10000
      DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 365) DAY), -- 创建时间随机1年内
      DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 30) DAY), -- 更新时间随机30天内
      1 -- 状态上架
    );
    SET i = i + 1;
  END WHILE;
END //
DELIMITER ;

-- 执行存储过程生成数据
CALL generate_product_data();
```

#### **查询需求：**

查询分类ID=2（手机分类）的商品，按销量降序、创建时间降序，分页显示第1页（20条）

```sql
SELECT 
  p.id, p.product_name, p.price, p.sales, c.category_name
FROM 
  product p
LEFT JOIN 
  category c ON p.category_id = c.id
WHERE 
  p.status = 1 AND p.category_id = 2
ORDER BY 
  p.sales DESC, p.create_time DESC
LIMIT 0, 20;
```

执行结果如下：

![1772443811427](image\1772443811427.png)

执行计划如下：

![1772443870232](image\1772443870232.png)

执行计划分析：

1、product表的type是ALL，说明进行了全表扫描，没有使用索引

2、extra字段显示using filesort，说明mysql无法利用索引完成排序，只能在内存或者磁盘中对结果集进行排序，排序耗时较高

根据分析可以看到查询条件（category_id,status）和排序字段（sales，create_time）均未建立索引，导致全表扫描+文件排序，查询效率极低，在并发访问的高峰期会拖慢整个数据库

#### 优化手段：

根据查询条件→排序条件→查询字段的顺序，建立联合索引

```sql
-- 说明：1. 筛选字段放前面，排序字段放后面；2. 排序字段统一按业务需求设为DESC，避免MySQL排序反转；3. 覆盖查询字段（id是主键，自动包含在索引中，无需额外添加）
CREATE INDEX idx_product_status_category_sales_create ON product (status, category_id, sales DESC, create_time DESC);
```

添加索引之后，执行语句不变，结果如下：

![1772444946331](image\1772444946331.png)

由于category表数据量较小，同时商品必然归属于某个分类，所以也可以将left join改成inner join，可以减少关联开销

```sql
-- 优化后SQL
SELECT 
  p.id, p.product_name, p.price, p.sales, c.category_name
FROM 
  product p
INNER JOIN 
  category c ON p.category_id = c.id
WHERE 
  p.status = 1 AND p.category_id = 2
ORDER BY 
  p.sales DESC, p.create_time DESC
LIMIT 0, 20;
```

执行结果如下：

![1772445076897](image\1772445076897.png)

**注意：**

**1、上述演示的结果均在我本机检测，而且是单请求下，所以查询的耗时可能并不是很明显，如果是并发环境会更加明显**

**2、上述耗时时间和执行计划在不同的mysql版本的时候可能会有一些差异，大家了解这样的优化思路，然后转换成自己的业务场景，面试的时候合理表述即可**

### 优化案例2：

#### 业务背景：

在某外卖平台，后台管理系统需查询用户订单明细

核心场景是根据订单创建时间范围，查询订单ID，订单金额，用户姓名、手机号、收获地址、订单状态、支持分页，日均查询量5万+，其中批量导出订单时（一次性查询1000+条）耗时极高

#### 产生问题：

批量导出订单时，查询耗时很长，甚至出现超时报错

#### 具体数据表：

订单表：

```sql
CREATE TABLE `order_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '订单ID（主键）',
  `order_no` varchar(50) NOT NULL COMMENT '订单编号（唯一）',
  `user_id` bigint(20) NOT NULL COMMENT '用户ID（关联user表）',
  `amount` decimal(10,2) NOT NULL COMMENT '订单金额',
  `status` tinyint(1) NOT NULL COMMENT '订单状态（1-待支付，2-已支付，3-已取消，4-已完成）',
  `address` varchar(500) NOT NULL COMMENT '收货地址',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `pay_time` datetime DEFAULT NULL COMMENT '支付时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_order_no` (`order_no`) -- 订单编号唯一索引
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单表';
```

用户表：

```sql
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '用户ID（主键）',
  `username` varchar(100) NOT NULL COMMENT '用户姓名',
  `phone` varchar(20) NOT NULL COMMENT '手机号（唯一）',
  `password` varchar(100) NOT NULL COMMENT '加密密码',
  `register_time` datetime NOT NULL COMMENT '注册时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
```

插入用户表的数据：

```sql
DELIMITER //
CREATE PROCEDURE generate_user_data()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 1000000 DO
    INSERT INTO `user` (username, phone, password, register_time)
    VALUES (
      CONCAT('用户', i),
      -- 调整：用i拼接手机号，确保唯一（避免随机数重复导致唯一键冲突）
      -- 格式：138 + 8位数字（i补前导0，确保8位，避免手机号长度不一致）
      CONCAT('138', LPAD(i, 8, '0')), 
      MD5(CONCAT('123456', i)), -- 加密密码（仍关联i，保证唯一）
      DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 730) DAY) -- 注册时间2年内
    );
    SET i = i + 1;
  END WHILE;
END //
DELIMITER ;
CALL generate_user_data();
```

插入订单表的数据：

```sql
DELIMITER //

CREATE PROCEDURE generate_order_data_fast()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE batch_size INT DEFAULT 1000;          -- 每批插入行数
    DECLARE total_rows INT DEFAULT 5000000;       -- 总行数
    DECLARE max_batch INT DEFAULT CEIL(total_rows / batch_size);
    DECLARE current_batch INT DEFAULT 1;
    DECLARE start_id INT;
    DECLARE end_id INT;
    DECLARE date_prefix VARCHAR(20);
    
    -- 获取固定的日期前缀（例如 ORDER20250303）
    SET date_prefix = CONCAT('ORDER', DATE_FORMAT(NOW(), '%Y%m%d'));
    
    -- 开启事务（MySQL 默认自动提交，这里显式控制）
    START TRANSACTION;
    
    WHILE current_batch <= max_batch DO
        -- 计算当前批次的行号范围
        SET start_id = (current_batch - 1) * batch_size + 1;
        SET end_id = LEAST(current_batch * batch_size, total_rows);
        
        -- 构建批量 INSERT 语句
        SET @insert_sql = 'INSERT INTO `order_info` 
            (order_no, user_id, amount, status, address, create_time, pay_time) VALUES ';
        
        -- 拼接多行数据
        SET @values = '';
        SET @j = start_id;
        WHILE @j <= end_id DO
            -- 生成唯一的订单号（前缀 + 8位序号）
            SET @order_no = CONCAT(date_prefix, LPAD(@j, 8, '0'));
            
            -- 随机数据：用户ID(1-100万)，金额(10.00-210.00)，状态(1-4)
            SET @user_id = FLOOR(1 + RAND() * 1000000);
            SET @amount = ROUND(10 + RAND() * 200, 2);
            SET @status = FLOOR(1 + RAND() * 4);
            SET @address = CONCAT('北京市海淀区XX街道', FLOOR(100 + RAND() * 900), '号');
            
            -- 创建时间：过去365天内的随机时间
            SET @create_time = DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 365) DAY);
            
            -- 支付时间：70%概率有支付时间（创建时间之后1小时内随机），30%为NULL
            IF FLOOR(RAND() * 10) > 2 THEN
                SET @pay_time = DATE_ADD(@create_time, INTERVAL FLOOR(RAND() * 3600) SECOND);
            ELSE
                SET @pay_time = NULL;
            END IF;
            
            -- 拼接一行数据
            SET @row = CONCAT(
                '(\'', @order_no, '\',',
                @user_id, ',',
                @amount, ',',
                @status, ',\'',
                @address, '\',\'',
                DATE_FORMAT(@create_time, '%Y-%m-%d %H:%i:%s'), '\','
            );
            
            IF @pay_time IS NULL THEN
                SET @row = CONCAT(@row, 'NULL)');
            ELSE
                SET @row = CONCAT(@row, '\'', DATE_FORMAT(@pay_time, '%Y-%m-%d %H:%i:%s'), '\')');
            END IF;
            
            -- 逗号分隔（最后一行不加逗号）
            IF @values = '' THEN
                SET @values = @row;
            ELSE
                SET @values = CONCAT(@values, ',', @row);
            END IF;
            
            SET @j = @j + 1;
        END WHILE;
        
        -- 组合完整的 INSERT 语句并执行
        SET @final_sql = CONCAT(@insert_sql, @values);
        PREPARE stmt FROM @final_sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
        
        -- 每批提交一次事务
        COMMIT;
        
        -- 开始下一批事务
        START TRANSACTION;
        
        SET current_batch = current_batch + 1;
    END WHILE;
    
    -- 最终提交（确保最后一批提交）
    COMMIT;
END //

DELIMITER ;

-- 调用存储过程
CALL generate_order_data_fast();
```

#### 查询需求：

批量导出场景，查询1个月内的订单，1000条

```sql
SELECT 
  o.id, o.order_no, o.amount, o.status, o.address, o.create_time,
  u.username, u.phone
FROM 
  order_info o
LEFT JOIN 
  user u ON o.user_id = u.id
WHERE 
  o.create_time BETWEEN '2026-01-01 00:00:00' AND '2026-01-31 23:59:59'
ORDER BY 
  o.create_time DESC
LIMIT 0, 1000;
```

执行结果如下：![1772547194942](image\1772547194942.png)

执行计划如下：

![1772547248994](image\1772547248994.png)

执行计划分析：

1、order_info表的type为ALL，全表扫描500万数据，未使用索引

2、extra显示using filesort，排序耗时极高

3、user表关联效率正常，使用eq_ref，主键索引，但订单表全表扫描导致整体耗时飙升

批量查询1000条数据的时候，mysql需要先扫描500万数据，筛选出符合条件的，在排序，最后取1000条，中间过程占用大量的内存和IO

#### 优化手段：

1、创建订单表时间索引，解决全表扫描的问题

查询条件是create_time字段，排序字段也是create_time，建立create_time的索引，同时覆盖关联字段和查询字段，避免回表

```sql
CREATE INDEX idx_order_create_user ON order_info (create_time DESC, user_id, amount, status, address, order_no);
```

2、用户表建立覆盖索引

关联时需要查询user表的username和phone，建立user_id+username+phone的覆盖索引，避免用户表回表

```
CREATE INDEX idx_user_id_name_phone ON user (id, username, phone);
```

3、业务上订单表必然属于某个用户，可以将left join换成inner join，减少无数据扫描

```sql
-- 优化后SQL（分批次查询示例，第1批）
SELECT 
  o.id, o.order_no, o.amount, o.status, o.address, o.create_time,
  u.username, u.phone
FROM 
  order_info o
INNER JOIN 
  user u ON o.user_id = u.id
WHERE 
  o.create_time BETWEEN '2026-01-01 00:00:00' AND '2026-01-31 23:59:59'
ORDER BY 
  o.create_time DESC
LIMIT 0, 200;
```

执行效果如下：

![1772547878114](image\1772547878114.png)

执行计划如下：

![1772547920764](image\1772547920764.png)

### 优化案例3：

#### 业务背景：

某会员系统，每月月底需要批量更新所有用户的积分（根据当月消费金额计算：积分=消费金额x1）

核心场景：更新user_score表中所有用户的积分，关联order_info表统计当月消费金额，用户总量超100万，每月订单量500万+

#### 产生问题：

每月月底执行批量更新时，耗时很长，期间数据库CPU占用率高达90%，其他业务出现卡顿，甚至无法正常访问

#### 具体数据表：

用户积分表：

```sql
CREATE TABLE `user_score` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_id` bigint(20) NOT NULL COMMENT '用户ID（关联user表，唯一）',
  `total_score` int(11) NOT NULL DEFAULT 0 COMMENT '总积分',
  `month_score` int(11) NOT NULL DEFAULT 0 COMMENT '当月积分',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_user_id` (`user_id`) -- 用户ID唯一索引
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户积分表';
```

订单表：

在案例二中已经有了订单表，此案例中沿用优化案例二中的订单表，数据不需要做任何的变化

插入用户积分表数据：

```sql
DELIMITER //
CREATE PROCEDURE generate_user_score_data()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 1000000 DO
    INSERT INTO `user_score` (user_id, total_score, month_score, update_time)
    VALUES (
      i, -- 关联user表的user_id（1-100万）
      FLOOR(0 + RAND() * 10000), -- 历史总积分0-10000
      0, -- 当月积分初始为0
      DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 30) DAY) -- 上次更新时间
    );
    SET i = i + 1;
  END WHILE;
END //
DELIMITER ;
CALL generate_user_score_data();
```

#### 查询需求：

更新2026年1月所有用户的当月积分和总积分，总积分=原总积分+当月积分

```sql
UPDATE 
  user_score us
INNER JOIN (
  -- 子查询：统计每个用户1月份已完成订单的总金额（取整）
  SELECT 
    user_id, 
    FLOOR(SUM(amount)) AS month_score 
  FROM 
    order_info 
  WHERE 
    status = 4 
    AND create_time BETWEEN '2026-01-01 00:00:00' AND '2026-01-31 23:59:59'
  GROUP BY 
    user_id
) o ON us.user_id = o.user_id
SET 
  us.month_score = o.month_score,
  us.total_score = us.total_score + o.month_score,
  us.update_time = NOW();
```

执行结果如下：

![image-20260304130419910](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20260304130419910.png)

子查询执行计划如下：

![image-20260304122357482](image\image-20260304122357482.png)

通过执行计划可以分析：

1、子查询进行的是全表扫描，没有用到索引，耗时较久

2、使用了临时表和文件排序，效率极低

总结分析，子查询全表扫描，效率极低，同时批量更新100万的数据，可能会对其他业务进行阻塞，而且在执行批量更新过程中，会占用大量的CPU和IO资源

#### 优化手段：

1、优化子查询，建立联合索引

```sql
CREATE INDEX idx_order_status_create_user_amount ON order_info (status, create_time, user_id, amount);
```

添加索引之后，执行时长有所降低：

![image-20260304122721598](image\image-20260304122721598.png)

![image-20260304122741022](image\image-20260304122741022.png)

执行计划显示子查询也用到了索引，但是时长还是无法接受，

调整user_score表索引，给update_time字段建立索引，方便后续查询最新的更新积分数据

```
CREATE INDEX idx_user_score_update_time ON user_score (update_time DESC);
```

执行结果如下：

![image-20260304123137958](image\image-20260304123137958.png)

时间又有所降低，但是时长还是较长，因此进行批量更新操作：

```sql
-- 编写存储过程，分批次更新（进一步优化，将耗时压缩至3秒内，兼容所有MySQL版本）
DELIMITER //
-- 先删除已存在的存储过程，避免重复创建报错
DROP PROCEDURE IF EXISTS batch_update_user_score;
CREATE PROCEDURE batch_update_user_score()
BEGIN
  -- 变量声明（规范顺序，避免语法冲突）
  DECLARE start_id BIGINT DEFAULT 1;    -- 起始user_id（1开始，匹配用户表user_id范围）
  DECLARE end_id BIGINT DEFAULT 15000; -- 优化：批次提升至15000条，减少批次数量（从100批→67批）
  DECLARE max_user_id BIGINT;          -- 最大user_id，用于控制循环结束

  -- 临时表优化：添加ROW_FORMAT=COMPACT，减少内存占用；主键索引保留，提升关联效率
  DROP TEMPORARY TABLE IF EXISTS temp_user_score;
  CREATE TEMPORARY TABLE IF NOT EXISTS temp_user_score (
    user_id BIGINT NOT NULL,
    month_score INT NOT NULL,
    PRIMARY KEY (user_id)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

  -- 子查询优化：结合订单表索引，添加ORDER BY user_id，避免临时表排序，提升插入效率
  INSERT INTO temp_user_score (user_id, month_score)
  SELECT 
    user_id, 
    FLOOR(SUM(amount)) AS month_score 
  FROM 
    order_info 
  WHERE 
    status = 4 
    AND create_time BETWEEN '2026-01-01 00:00:00' AND '2026-01-31 23:59:59'
  GROUP BY 
    user_id
  ORDER BY 
    user_id; -- 贴合临时表主键顺序，减少插入时的索引排序开销

  -- 处理无数据场景，避免max_user_id为NULL导致循环异常
  SELECT IFNULL(MAX(user_id), 0) INTO max_user_id FROM user_score;

  -- 分批次更新优化：关闭自动提交，批量提交事务，减少事务日志写入开销
  SET autocommit = 0;
  WHILE start_id <= max_user_id DO
    -- 关联临时表更新，ON条件优化，明确关联逻辑，提升执行效率
    UPDATE 
      user_score us
    INNER JOIN temp_user_score t 
      ON us.user_id = t.user_id 
      AND us.user_id BETWEEN start_id AND end_id -- 限定批次user_id范围，兼容所有MySQL版本
    SET 
      us.month_score = t.month_score,
      us.total_score = us.total_score + t.month_score,
      us.update_time = NOW();

    -- 推进批次（自动适配下一批，避免遗漏）
    SET start_id = end_id + 1;
    SET end_id = end_id + 15000;
  END WHILE;
  -- 批量提交所有事务，减少日志写入次数
  COMMIT;
  -- 恢复自动提交，避免影响后续数据库操作
  SET autocommit = 1;

  -- 删除临时表，释放数据库资源
  DROP TEMPORARY TABLE IF EXISTS temp_user_score;
END //
DELIMITER ;

-- 执行分批次更新（优化后耗时可压缩至3秒内，语法无错，可直接执行）
CALL batch_update_user_score();
```

执行结果如下：![image-20260304132254681](image\image-20260304132254681.png)