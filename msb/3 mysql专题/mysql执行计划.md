# mysql执行计划

​       在企业的应用场景中，为了知道优化SQL语句的执行，需要查看SQL语句的具体执行过程，以加快SQL语句的执行效率。

​       可以使用explain+SQL语句来模拟优化器执行SQL查询语句，从而知道mysql是如何处理sql语句的。

​	   官网地址：https://dev.mysql.com/doc/refman/8.0/en/explain-output.html

### 1、执行计划中包含的信息

|    Column     |                    Meaning                     |
| :-----------: | :--------------------------------------------: |
|      id       |            The `SELECT` identifier             |
|  select_type  |               The `SELECT` type                |
|     table     |          The table for the output row          |
|  partitions   |            The matching partitions             |
|     type      |                 The join type                  |
| possible_keys |         The possible indexes to choose         |
|      key      |           The index actually chosen            |
|    key_len    |          The length of the chosen key          |
|      ref      |       The columns compared to the index        |
|     rows      |        Estimate of rows to be examined         |
|   filtered    | Percentage of rows filtered by table condition |
|     extra     |             Additional information             |

**id**

select查询的序列号，包含一组数字，表示查询中执行select子句或者操作表的顺序

id号分为三种情况：

​		1、如果id相同，那么执行顺序从上到下

```sql
explain select * from emp e join dept d on e.deptno = d.deptno join salgrade sg on e.sal between sg.losal and sg.hisal;
```

​		2、如果id不同，如果是子查询，id的序号会递增，id值越大优先级越高，越先被执行

```sql
explain select * from emp e where e.deptno in (select d.deptno from dept d where d.dname = 'SALES');
```

​		3、id相同和不同的，同时存在：相同的可以认为是一组，从上往下顺序执行，在所有组中，id值越大，优先级越高，越先执行

```sql
explain select * from emp e join dept d on e.deptno = d.deptno join salgrade sg on e.sal between sg.losal and sg.hisal where e.deptno in (select d.deptno from dept d where d.dname = 'SALES');
```

**select_type**

主要表明mysql在执行查询的时候，每个select子句属于什么类型，详细的类型如下：

| `select_type` Value  |                           Meaning                            |
| :------------------: | :----------------------------------------------------------: |
|        SIMPLE        |        Simple SELECT (not using UNION or subqueries)         |
|       PRIMARY        |                       Outermost SELECT                       |
|        UNION         |         Second or later SELECT statement in a UNION          |
|   DEPENDENT UNION    | Second or later SELECT statement in a UNION, dependent on outer query |
|     UNION RESULT     |                      Result of a UNION.                      |
|       SUBQUERY       |                   First SELECT in subquery                   |
|  DEPENDENT SUBQUERY  |      First SELECT in subquery, dependent on outer query      |
|       DERIVED        |                        Derived table                         |
|  DEPENDENT DERIVED   |           Derived table dependent on another table           |
|     MATERIALIZED     |                    Materialized subquery                     |
| UNCACHEABLE SUBQUERY | A subquery for which the result cannot be cached and must be re-evaluated for each row of the outer query |
|  UNCACHEABLE UNION   | The second or later select in a UNION that belongs to an uncacheable subquery (see UNCACHEABLE SUBQUERY) |

```sql
--sample:简单的查询，不使用union或者子查询
explain select * from emp;

--primary:当查询中包含子查询或者union的时候，最外层的select会被标记为primary
explain select * from emp where sal > (select avg(sal) from emp) ;

--union:在使用union组合多个查询结构的时候，第一个select是primary，后续的select都是union
explain select * from emp where deptno = 10 union select * from emp where sal >2000;

--dependent union:当union出现在子查询中，并且该子查询的每行结果都需要根据外层查询的当前行重新执行时，后续的select会被标记为dependent union，通常发生在相关子查询中使用了union
explain select * from emp e where e.empno  in ( select empno from emp where deptno = 10 union select empno from emp where sal >2000)

--union result:这是一个特殊的select_type,这个并不是一个真正的select语句，而是代表从union操作中检索结果的步骤
explain select * from emp where deptno = 10 union select * from emp where sal >2000;

--subquery:当子查询不是相关子查询（即不依赖外层查询），且出现在where、from等子句中时，该子查询的select_type为subquery
explain select * from emp where sal > (select avg(sal) from emp) ;

--dependent subquery:子查询引用了外层表的列，导致子查询需要为外层查询的每一行重新执行
EXPLAIN SELECT ename, sal FROM emp e WHERE sal > (SELECT AVG(sal) FROM emp e2 WHERE e2.deptno = e.deptno);

--DERIVED: 当一个子查询出现在from子句中，作为一个临时表，该子查询的select_type为derived
EXPLAIN SELECT * FROM (SELECT deptno, AVG(sal) avg_sal FROM emp GROUP BY deptno) AS dept_avg;

--dependent derived：这是mysql8新增的类型，指派生表（from子句中的子查询）依赖于外部查询的某个表。通常出现在使用LATERAL语法或者某些特殊情况下，派生表需要根据外层表的每一行进行计算
EXPLAIN SELECT d.deptno, d.dname, e.ename, e.sal FROM dept d LEFT JOIN LATERAL ( SELECT ename, sal FROM emp WHERE deptno = d.deptno ORDER BY sal DESC LIMIT 1) e ON true;

--materialized subquery：当优化器决定将子查询的结果物化（即生成一个临时表并缓存结果）时，该子查询的select_type为materialized subquery，这通常发生在非相关子查询中，并且物化器认为物化可以提升性能
--未演示出对应的案例

--UNCACHEABLE SUBQUERY：无法被缓存且必须为外层查询的每一行重新评估的子查询，子查询的结果不能缓存，通常因为子查询中包含用户变量，某些函数或者引用了外层表中的某些无法确定的值，每次执行都需要重新计算
 explain select * from emp where empno = (select empno from emp where deptno=@@sort_buffer_size);
 
--uncacheable union:属于一个不可缓存子查询的union中的第二个或者之后的select，当union出现在一个uncacheable subquery中，并且是union的后续部分时，这些后续的select会被标记为uncacheable union
explain select * from emp where empno = (select empno from emp where ename='SMITH' union select empno from emp where deptno=@@sort_buffer_size);
```

**table**

对应行正在访问哪一个表，表名或者别名，可能是临时表或者union合并结果集
		1、如果是具体的表名，则表明从实际的物理表中获取数据，当然也可以是表的别名

​		2、表名是derivedN的形式，表示使用了id为N的查询产生的衍生表

​		3、当有union result的时候，表名是union n1,n2等的形式，n1,n2表示参与union的id

**type**

type显示的是连接类型，访问类型表示我是以何种方式去访问我们的数据，最容易想的是全表扫描，直接暴力的遍历一张表去寻找需要的数据，效率非常低下，访问的类型有很多，效率从最好到最坏依次是：

system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > range > index > ALL 

一般情况下，得保证查询至少达到range级别，最好能达到ref

```sql
--all:全表扫描，一般情况下出现这样的sql语句而且数据量比较大的话那么就需要进行优化。
explain select * from emp;

--index：全索引扫描，即遍历整个索引树，通常发生在两种情况，查询使用了覆盖索引或者需要按索引顺序读取数据
explain  select empno from emp;

--range：表示利用索引查询的时候限制了范围，在指定范围内进行查询，这样避免了index的全索引扫描，适用的操作符： =, <>, >, >=, <, <=, IS NULL, BETWEEN, LIKE, or IN() 
explain select * from emp where empno between 7000 and 7500;

--index_subquery：与unique_subquery类似，但子查询使用的是普通索引，没演示出效果

--unique_subquery:子查询使用主键或者唯一键进行in查询优化，mysql会将该子查询视为一个唯一键查询，然后对外层表逐行匹配
SET optimizer_switch = 'semijoin=off,materialization=off';
EXPLAIN
SELECT * FROM emp
WHERE deptno IN (SELECT deptno FROM dept WHERE dname = 'SALES'); 

--index_merge：索引合并优化，查询使用多个索引，然后将结果合并
EXPLAIN SELECT * FROM emp WHERE empno = 7369 OR deptno = 20;

--ref_or_null：类似于ref，但mysql会额外搜索包含null值的行
alter table emp add index idx_name(ename)
EXPLAIN SELECT * FROM emp WHERE ename = 'SMITH' OR ename IS NULL;

--ref：使用了非唯一性索引或者唯一索引的前缀进行等值匹配，可能返回多行数据
 create index idx_3 on emp(deptno);
 explain select * from emp e,dept d where e.deptno =d.deptno;

--eq_ref ：使用唯一性索引进行数据查找
EXPLAIN SELECT e.ename, d.dname FROM emp e, dept d WHERE e.deptno = d.deptno;

--const：这个表至多有一个匹配行，
explain select * from emp where empno = 7369;
 
--system：表只有一行记录（等于系统表），这是const类型的特例，平时不会出现
```

 **possible_keys** 

​        显示可能应用在这张表中的索引，一个或多个，查询涉及到的字段上若存在索引，则该索引将被列出，但不一定被查询实际使用

```sql
explain select * from emp,dept where emp.deptno = dept.deptno and emp.deptno = 10;
```

**key**

​		实际使用的索引，如果为null，则没有使用索引，查询中若使用了覆盖索引，则该索引和查询的select字段重叠。

```sql
explain select * from emp,dept where emp.deptno = dept.deptno and emp.deptno = 10;
```

**key_len**

表示索引中使用的字节数，可以通过key_len计算查询中使用的索引长度，在不损失精度的情况下长度越短越好。

```sql
explain select * from emp,dept where emp.deptno = dept.deptno and emp.deptno = 10;
```

**ref**

表示具体的查询条件，显示了key列引用的索引在查找值时，是与什么进行比较的

```sql
explain select * from emp,dept where emp.deptno = dept.deptno and emp.deptno = 10;
```

**rows**

根据表的统计信息及索引使用情况，大致估算出找出所需记录需要读取的行数，此参数很重要，直接反应的sql找了多少数据，在完成目的的情况下越少越好

```sql
explain select * from emp;
```

**extra**

包含额外的信息。

```sql
--using filesort:说明mysql无法利用索引进行排序，只能利用排序算法进行排序，会消耗额外的位置
explain select * from emp order by sal;

--using temporary:建立临时表来保存中间结果，查询完成之后把临时表删除
explain select ename,count(*) from emp where deptno = 10 group by ename;

--using index:这个表示当前的查询时覆盖索引的，直接从索引中读取数据，而不用访问数据表。如果同时出现using where 表名索引被用来执行索引键值的查找，如果没有，表面索引被用来读取数据，而不是真的查找
explain select deptno,count(*) from emp group by deptno limit 10;

--using where:表示mysql的server在存储引擎返回记录的时候，再次应用where条件进行过滤，通常发生在无法通过索引直接过滤所有条件的时候
EXPLAIN SELECT * FROM dept WHERE dname = 'SALES';

--using index condition:表示使用索引下推
alter table emp add index idx_deptno_sal(deptno,sal);
EXPLAIN SELECT * FROM emp WHERE deptno = 30 AND sal > 2000;
```

