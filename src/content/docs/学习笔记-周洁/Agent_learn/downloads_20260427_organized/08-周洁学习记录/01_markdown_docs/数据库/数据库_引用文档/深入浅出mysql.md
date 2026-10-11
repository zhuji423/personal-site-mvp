---
title: "基本介绍"
description: "深入浅出mysql"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\数据库\\数据库_引用文档\\深入浅出mysql.md"
---
深入浅出mysql

# 基本介绍
**主要特点和功能：**

1. **关系型数据库：**MySQL是一种关系型数据库管理系统，它使用表来组织和存储数据。数据以行和列的形式存储在表中，并使用结构化查询语言（SQL）进行操作和管理。
2. **跨平台性：**MySQL可以在多个操作系统上运行，包括Windows、Linux、macOS等，可以适应不同的开发和部署环境。
3. **高性能：**MySQL被设计成高性能的数据库系统。它可以处理大规模数据集和高并发访问，并提供了各种优化技术来提升查询和事务处理的性能。
4. **可扩展性：**MySQL支持水平扩展和垂直扩展。水平扩展通过在多个服务器上分布数据来增加系统的容量和吞吐量。垂直扩展通过升级硬件资源（如CPU、内存）来提高单个服务器的性能。
5. **安全性：**MySQL提供了一系列安全功能来保护数据的机密性和完整性。它支持用户身份验证、访问控制、数据加密和安全传输等功能，以防止未经授权的访问和数据泄露。
6. **多种存储引擎：**MySQL支持多种存储引擎，如InnoDB、MyISAM、Memory等。每个存储引擎都有不同的特点和适用场景，可以根据应用程序的需求选择合适的存储引擎。

总之，MySQL是一种功能强大、可靠性高且易于使用的关系型数据库，被广泛使用。

# 存储引擎介绍
存储引擎负责管理数据的存储、检索和操作。它定义了数据如何在磁盘上组织、存储和访问。存储引擎决定了数据库的性能、并发性、可靠性和功能特性。

**常见引擎对比**

|**特性**|**InnoDB**|**MyISAM**|**Memory**|
|-|-|-|-|
|事务支持|支持|不支持|不支持|
|外键约束|支持|不支持|不支持|
|锁粒度|行锁|表锁|表锁|
|存储限制|64TB|256TB|存储在内存中|
|索引支持|支持|支持|支持|
|内存缓存|支持|支持|支持|
|数据缓冲区|支持|不支持|不支持|
|数据压缩|支持|支持|不支持|
|热备份|支持|支持|支持|
|恢复速度|慢|快|最快|

1. InnoDB：InnoDB是MySQL的**默认存储引擎**（5.5版本后），它提供了ACID（原子性、一致性、隔离性和持久性）事务支持。InnoDB支持行级锁定和多版本并发控制（MVCC），这使得它在高并发环境下表现出色。它还提供了外键约束、崩溃恢复能力和高可靠性。
2. MyISAM：MyISAM是MySQL最早的存储引擎之一。它具有较低的资源消耗，适用于读频繁、写较少的应用场景。MyISAM不支持事务和行级锁定，但它对全文搜索索引的支持较好。
3. Memory：Memory存储引擎将数据存储在内存中，因此读取和写入操作非常快速。它适用于临时表、缓存和其他需要快速访问的数据。然而，由于数据存储在内存中，数据库重启或服务器关闭时数据将丢失。

# 事务与隔离级别
## 事务
### 特性介绍
**原子性：**原子性指的是事务是不可分割的操作单元，要么全部执行成功，要么全部回滚到原始状态，没有中间状态。如果事务中的任何操作失败，整个事务将被回滚，所有修改将被撤销，数据库保持在一致的状态；当事务开始时，MySQL会在undo log中记录该事务所修改的行的旧版本。如果事务执行过程中遇到错误或者需要回滚，MySQL可以通过undo log中的信息将数据恢复到事务开始之前的状态，从而保证事务的原子性。

**一致性：**一致性确保事务将数据库从一个一致的状态转换为另一个一致的状态。事务的执行不会破坏数据库的完整性约束和业务规则。如果事务违反了一致性，系统将回滚事务并将数据库恢复到原始状态。

**隔离性：**隔离性指的是并发执行的事务之间应该相互隔离，每个事务的操作应该与其他事务的操作相互独立。隔离性通过使用锁机制和MVCC来防止并发事务之间的干扰和数据冲突。

**持久性：**持久性确保事务提交后，其所做的更改将永久保存在数据库中，即使在系统发生故障（如崩溃）时也是如此。数据库系统使用日志记录和恢复机制来实现持久性，以确保已提交的事务不会丢失。在commit前先写入redolog，确保commit成功，这时候即使重启也能完成数据的持久化。



## 事务隔离级别
### 隔离级别解决的问题
|**事务隔离级别下产生的问题**|**脏读**|**不可重复读**|**幻读**|
|-|-|-|-|
|读未提交（read uncommitted）|√|√|√|
|读已提交（read committed）|×|√|√|
|可重复读（repeatable read）|×|×|√|
|串行化（serializable）|×|×|×|

问题详解：

* **脏读：**读取到其他事务未提交的数据
* **不可重复读：**事务内相同的语句多次查询，获取的数据不同，eg：事务T1读取数据D1，事务T2修改数据D1，事务T1再读取数据D1出现不同结果
* **幻读：**事务内相同的语句多次查询，获取了不同条数的数据。与不可重复读类似，它发生在一个事务T1读取了范围数据，事务T2插入或删除部分数据，事务T1再次读取就会发现多了/少了一些原本不存在的数据

---

事务详解：

* **读取未提交：**最低的隔离级别，允许读取未提交的数据，可能会导致脏读、幻读、不可重复读。
* **读取已提交：**允许读取并发事务已经提交的数据，可以阻止脏读，但是幻读或不可重复读仍有可能发生。
* **可重复读：**对同一字段的多次读取结果都是一致的，除非数据是被本身事务自己所修改，可以阻止脏读和不可重复读，但幻读仍有可能发生。是mysql**默认的隔离级别**。

      PS：mysql通过其他机制在该级别下解决了幻读问题，详见4.4节。

* **串行化：**最高的隔离级别，完全服从ACID的隔离级别。所有的事务依次逐个执行，这样事务之间就完全不可能产生干扰，该级别可以防止脏读、不可重复读以及幻读。一般采用锁实现，**效率非常低**。

# 并发控制
## 数据库并发场景
1. ​ 读读：不存在线程安全问题
2. ​ 读写：有线程安全问题，可以通过MVCC解决
3. ​ 写写：有线程安全问题，只能通过加锁解决

## 锁机制
### 锁的排他性
* **共享锁（S锁）**

多个事务可以同时获得共享锁，用于并发读取数据，但是不能进行增删改操作

eg：SELECT ... LOCK IN SHARE MODE;

* **排他锁（X锁）**

只有一个事务可以获得排他锁，数据库增删改操作都是X锁

|**是否可共存**|**X锁**|**S锁**|
|-|-|-|
|X锁|否|否|
|S锁|否|是|

### 意向锁
意向锁为**表级锁**，引入意向锁是为了优化并发事务加锁判断

为什么需要意向锁：事务T1添加行锁后，事务T2需要添加表锁，这时T2需要判断是否有其他事务添加了表锁和行锁，如果没有意向锁，判断行锁需要逐行判断是否有行锁，然后再确定是否能获取表锁，效率低，有了意向锁可以直接根据意向锁判断是否可以获取锁

* **意向共享锁（IS锁）**

当事务准备在某条记录上加S锁时，需要先在表级别加一个IS锁

* **意向排他锁(IX锁)**

当事务准备在某条记录上加X锁时，需要先在表级别加一个IX锁



表级S、X锁与IS、IX共存关系：

|是否可共存|X锁|IX锁|S锁|IS锁|
|-|-|-|-|-|
|X锁|否|否|否|否|
|IX锁|否|是|否|是|
|S锁|否|否|是|是|
|IS锁|否|是|是|是|

总结：

    * X 和所有锁都冲突
    * IX 兼容 IX 和 IS
    * S 兼容 S 和 IS
    * IS 兼容 IX、S 和 IS

IX，IS是表级锁，不会和行级的X，S锁发生冲突，只会和表级的X，S发生冲突

### 行锁范围
* **记录锁（record lock）**

锁定单个索引记录，防止其他事务修改或删除该记录

* **间隙锁（gap lock）**

锁定索引范围内的间隙，防止其他事务在该范围内插入新记录，RR隔离级别下生效

* **临键锁（next-key lock）**

记录锁和间隙锁的组合，同时锁定索引记录和索引前面的间隙，范围是左开右闭，RR隔离级别下生效

注：间隙锁和临键锁存在的意义是为了防止幻读产生

**锁示例**

[流程图]
#### 行锁加锁
```
create table test_tb
(
    id   int auto_increment primary key,
    name varchar(256),
    age  int,
    index idx_age (age)
) comment 'test';
insert into test_tb (id, name, age) values (1, 'test001', 1);
insert into test_tb (id, name, age) values (10, 'test002', 10);
insert into test_tb (id, name, age) values (20, 'test003', 20);
```
**id和age索引示例：**

[流程图]
默认情况下，InnoDB在 REPEATABLE READ事务隔离级别运行，使用临键锁（next-key lock）进行索引扫描

1. 唯一索引上的等值查询，找到记录，加**记录锁；**找不到记录，向右访问到第一个不符合条件的纪录，临键锁退化为间隙锁，即对查询的值所在的**间隙加间隙锁**

eg：

1）select * from test_tb where id = 10  for update ; 

能查询到id为10的纪录，因此对10这个索引加纪录锁，锁住10

2）select * from test_tb where id = 11 for update;

不能查到11这条纪录，向右第一条不满足条件数据是20，因此锁住（10,20）间隙

2. 非唯一索引上的等值查询，找到记录，加**临键锁**，且向右访问到第一个不符合条件的纪录，加**间隙锁；**找不到记录，向右访问到第一个不符合条件的纪录，临键锁退化为间隙锁，即对查询的值所在的间隙加**间隙锁（同唯一索引）；**

eg：

1）select * from test_tb where age = 10 for update;

            * 能查询到age为10的纪录，对10加临键锁，锁住（1,10]
            * 向右访问第一个不符合条件的纪录为20，对20加间隙锁，锁住  (10,20)
            * 总结加锁范围：（1,10]，(10,20)

2）select * from test_tb where age = 11 for update;

不能查到11这条纪录，向右第一条不满足条件数据是20，因此锁住（10,20）间隙

3. 索引上的范围查询，对所有扫描到的纪录加**临键锁**，会访问到不满足条件的第一个值为止，在【小于或小于等于】条件的范围查询，该记录的索引的临键锁会退化成间隙锁

eg：

1）select * from test_tb where id > 15 or select * from test_tb where age > 15

            * 扫描到的纪录是20，对20加临键锁，锁住（10,20]
            * 向右未访问到不满足条件的数据（+∞），锁住（20，+∞）
            * 总结加锁范围（10,20]，（20，+∞）

2）select * from test_tb where id < 15 or select * from test_tb where age< 15

            * 扫描到的纪录是1、10，对1,10加临键锁，锁住（-∞,1]，（1,10]
            * 第一个不满足条件的数据是20，对20加间隙锁，锁住（10，20）
            * 总结加锁范围（-∞,1]，（1,10]，（10，20）

间隙锁目的是防止其他事务插入间隙，间隙锁可以共存，一个事务采用的间隙锁不会阻止另一个事务在同一间隙上添加间隙锁。

## mvcc
多版本并发控制，Multiversion Concurrency Control，**保留数据的多个版本**，控制多个事务之间的读写并发问题，依赖数据库**两个隐式字段、****undolog****、ReadView**（读视图）实现

### 隐式字段
1. DB_TRX_ID：最近修改事务id，记录创建这条记录或者最后一次修改该记录的事务id；
2. DB_ROLL_PTR：回滚指针，指向这条记录的上一个版本，用于配合undolog，指向上一个版本地址
3. DB_ROW_ID：隐藏的主键，如果数据表没有主键，InnoDB会自动以DB_ROW_ID产生一个聚簇索引（在mvcc中无用，此处顺带提一下这个隐式字段）

### undolog
在事务修改数据前，MySQL会保留老数据到undolog（逻辑意义上的，并不存在物理上的多条记录。真正保存的是一个反向操作，详见后文5.1.3），并且⽤隐藏字段db_trx_id、db_roll_pointer把这些不同版本的数据串联起来形成⼀个历史记录版本链，undolog的链首就是最新的历史版本记录，链尾就是最老的历史版本记录

示例：

[流程图]
### ReadView(读视图)
ReadView是事务快照读的时候产生的数据读视图

**快照读和当前读**

* 快照读：读取的快照数据（根据关联的**ReadView**判断读取数据的哪个版本），如在执行不加锁的select语句时发生，eg：select ... from tb
* 当前读：读取当前数据库数据，在执行加锁查询或者增删改时发生，eg：select ... for update,select … lock in share mode，insert、delete、update

**不同隔离级别产生ReadView时机**

* 读未提交：可以读到未提交事务修改过的记录，所以直接读取记录的最新版本，不会产生readview
* 读已提交：事务内每次select都会重新生成一个快照
* 可重复读：事务内只在第一次select的时候生成一个快照，后续select都从该快照读取
* 串行化：通过加锁方式访问数据，因此只会产生当前读，不会产生readview

**ReadView 主要包含以下几部分****：**

* m_ids：当前系统还未提交事务的id列表
* m_up_limit_id：指 m_ids 里最小的值（低水位）
* m_low_limit_id：系统拟分配给下一个事务的id（高水位，事务id的分配是递增的）
* m_creator_trx_id，创建该readView的事务的 id

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 可见性规则
在MVCC机制中，根据数据记录中的隐式字段DB_TRX_ID以及ReadView中的事务ID，完成数据的可见性控制。

1. 比较DB_TRX_ID与m_creator_trx_id

    * 等于：可见，当前事务操作数据可见（自己修改的，得认）
    * 不等于：不是当前事务，继续下一步

2. 比较DB_TRX_ID 与 m_low_limit_id

    * 大于等于：不可见，在当前readview生成时，事务还没产生，所以不可见
    * 小于：当前readview生成时，事务已产生，继续下一步

3.  比较DB_TRX_ID 与 m_up_limit_id

    * 小于：可见，在当前readview生成时，事务已提交，所以可见（当前事务开始时已提交的，得认）
    * 大于等于：当前readview生成时，事务是否已提交不确定，需进一步判断

4. 比较DB_TRX_ID是否在m_ids内

    * 不在：可见，在当前readview生成时，事务已提交，所以可见（当前事务开始时已提交的，得认）
    * 在：不可见，当前readview生成时，事务未提交

文字总结版：

一个数据版本，对于一个事务视图（readView)来说，除了事务自己的更新总是可见以外，有三种情况：

1. 版本未提交，不可见；
2. 版本已提交，但是是在视图创建后提交的，不可见；
3. 版本已提交，而且是在视图创建前提交的，可见

示例（RR事务隔离级别下）：

[流程图]


## 4.4 MySQL幻读问题的解决
mysql在可重复读隔离级别下，借助MVCC与间隙锁机制，解决幻读问题。

1. **MVCC解决快照读的幻读问题**

可重复读隔离级别，只在第一次select的时候生成一个读视图，后续select都依据该视图判断读取数据版本，因此即使其他事务做了增删操作，再次查询的时候也只会依据之前生成的读视图判断，根据上述MVCC的可见性分析，不会读取到增删的数据，以此解决幻读问题

注：如果在多次查询中产生了当前读，再次select时会重新产生一个读视图，因此也会出现幻读问题（详见4.3.4的示例分析）

2. **间隙锁解决当前读的幻读问题**

在可重复读的隔离级别下执行当前读时会产生间隙锁，其他事务在该间隙进行的增删操作就会阻塞，以此达到解决幻读的问题

示例：

[流程图]
事务T1：select * from sys_user for update;

mysql不仅会对每条记录加锁（1,10,20）还会对记录之间的间隙进行加锁((-∞,1),(1,10),(10,20),(20,+∞))，其他事务增删操作就阻塞了，因此就不会出现幻读问题

# sql执行过程
## 相关概念
### 页
MySQL 与磁盘的交互单位叫做页，页默认大小为16KB，每次MySQL 读取磁盘的时候，都会以页为单位读取数据

#### **数据页格式**
[流程图]
|**名称**|**中文名**|**占用空间大小**|**简单描述**|
|-|-|-|-|
|File Header|文件头部|38字节|页的一些通用信息|
|Page Header|页面头部|56字节|数据页专有的一些信息|
|Infimum + Supremum|最小记录和最大记录|26字节|两个虚拟的行记录|
|User Records|用户记录|不确定|实际存储的行记录内容|
|Free Space|空闲空间|不确定|页中尚未使用的空间|
|Page Directory|页面目录|不确定|页中的某些记录的相对位置|
|File Trailer|文件尾部|8字节|校验页是否完整|

#### File Header
File Header表示页的一些通用信息，占固定的38字节，由下面几部分组成的

|名称|占用空间大小|描述|
|-|-|-|
|FIL_PAGE_SPACE_OR_CHKSUM|4字节|页的校验和（checksum值）|
|FIL_PAGE_OFFSET|4字节|页号|
|FIL_PAGE_PREV|4字节|上一个页的页号|
|FIL_PAGE_NEXT|4字节|下一个页的页号|
|FIL_PAGE_LSN|8字节|页面被最后修改时对应的日志序列位置|
|FIL_PAGE_TYPE|2字节|该页的类型|
|FIL_PAGE_FILE_FLUSH_LSN|8字节|仅在系统表空间的一个页中定义，代表文件至少被刷新到了对应的LSN值|
|FIL_PAGE_ARCH_LOG_NO_OR_SPACE_ID|4字节|该页属于哪个表空间|

* FIL_PAGE_PREV、FIL_PAGE_NEXT

数据页的文件头部中记录了上一页和下一页的地址，证明叶子结点形成的是**双向链表**

* FIL_PAGE_SPACE_OR_CHKSUM校验和

用于保证页同步完整，和File Trailer的前四个字节对应

* FIL_PAGE_TYPE标识该存储页的类型

|类型名称|十六进制|描述|
|-|-|-|
|FIL_PAGE_TYPE_ALLOCATED|0x0000|最新分配，还没使用|
|FIL_PAGE_UNDO_LOG|0x0002|Undo日志页|
|FIL_PAGE_INODE|0x0003|段信息节点|
|FIL_PAGE_IBUF_FREE_LIST|0x0004|Insert Buffer空闲列表|
|FIL_PAGE_IBUF_BITMAP|0x0005|Insert Buffer位图|
|FIL_PAGE_TYPE_SYS|0x0006|系统页|
|FIL_PAGE_TYPE_TRX_SYS|0x0007|事务系统数据|
|FIL_PAGE_TYPE_FSP_HDR|0x0008|表空间头部信息|
|FIL_PAGE_TYPE_XDES|0x0009|扩展描述页|
|FIL_PAGE_TYPE_BLOB|0x000A|BLOB页|
|FIL_PAGE_INDEX|0x45BF|**索引页，也就是我们所说的数据页**|

#### Page Header
Page Header是用来记录数据页的状态信息的，由14个部分组成，共占56个字节 。由下面这些内容组成的：

|名称|占用空间大小|描述|
|-|-|-|
|PAGE_N_DIR_SLOTS|2字节|在页目录中的槽数量|
|PAGE_HEAP_TOP|2字节|还未使用的空间最小地址，也就是说从该地址之后就是Free Space|
|PAGE_N_HEAP|2字节|本页中的记录的数量（包括最小和最大记录以及标记为删除的记录）|
|PAGE_FREE|2字节|第一个已经标记为删除的记录地址（各个已删除的记录通过next_record也会组成一个单链表，这个单链表中的记录可以被重新利用）|
|PAGE_GARBAGE|2字节|已删除记录占用的字节数|
|PAGE_LAST_INSERT|2字节|最后插入记录的位置|
|PAGE_DIRECTION|2字节|记录插入的方向|
|PAGE_N_DIRECTION|2字节|一个方向连续插入的记录数量|
|PAGE_N_RECS|2字节|该页中记录的数量（不包括最小和最大记录以及被标记为删除的记录）|
|PAGE_MAX_TRX_ID|8字节|修改当前页的最大事务ID，该值仅在二级索引中定义|
|PAGE_LEVEL|2字节|当前页在B+树中所处的层级|
|PAGE_INDEX_ID|8字节|索引ID，表示当前页属于哪个索引|
|PAGE_BTR_SEG_LEAF|10字节|B+树叶子段的头部信息，仅在B+树的Root页定义|
|PAGE_BTR_SEG_TOP|10字节|B+树非叶子段的头部信息，仅在B+树的Root页定义|

#### User Records
**结构图**

[流程图]
**记录头信息**

* 预留位1：占用 1 比特，没有使用。
* 预留位2：占用 1 比特，没有使用。
* deleted_flag：占用 1 比特，标记该记录是否被删除，删除标记为1记录不会立即从磁盘上移除，是因为移除它们之后把其他的记录在磁盘上重新排列需要消耗性能，所以只是打一个**删除标记而已**，所有被删除掉的记录都会组成一个垃圾链表，在这个链表中记录占用的空间称之为可重用空间，之后如果有新记录插入到表中的话，可能把这些可重用空间覆盖掉
* min_rec_flag：占用 1 比特，在 B+ 树（后面索引会讲到）中每层非叶子节点中的最小的目录项，都会添加此标记。
* n_owned：占用4比特，一个页面中的记录被分为若干个组，每个组里有一个记录最大值，这条记录的 n_owned 就是所在组的所有记录条数，而其余记录 n_owned 都是 0
* heap_no：占用 13 比特，表示当前记录在页面堆中的相对位置
* record_type：占用 3 比特，表示当前记录的类型
    * **0是普通记录**
    * **1是 B+树非叶节点的目录项记录**
    * 2是 Infimum 记录
    * 3是 Suprememum 记录

* next_record：占用 16 比特，表示从当前记录的真实数据到下一条记录的真实数据的地址偏移量，正数往后查找，负数往前查找，eg：记录的next_record值为32，意味着从第一条记录的真实数据的地址处向后找32个字节便是下一条记录的真实数据，反之如果是-32则向前查找32个字节
    * Infimum记录的下一条记录就是本页中主键最小的用户记录
    * 未被删除的记录(deleted_flag = 0)会按照主键从小到大的顺序形成了一个单链表


#### Infimum + Supremum
Infimum和Supremum是InnoDB定义的特殊行记录，该类型记录中没有变长字段长度列表和NULL值字段列表，取而代之的分别是最小记录与最大记录，类似于链表中的头节点和尾节点，在数据查找时可以根据最大值和最小值判断数据是否在当前页

#### Free Space
尚未使用的存储空间

在开始生成页的时候，没有User Records这个部分，每当我们插入一条记录，都会从Free Space中申请一个记录大小的空间划分到User Records，当Free Space部分的空间全部被User Records替代掉之后，就意味着这个页使用完了，如果还有新的记录插入的话，就需要去申请新的页

#### Page Directory
记录在页中是按照主键值从小到大的顺序串联成为一个单向链表，因此查询也只能以头节点（Infimum）开始逐一向后查询，但是如果数据量很大，那么性能就无法保证了，针对这个问题， InnoDB采取了**类似目录**的解决方案，对页内数据进行分组，并在Page Directory中，维护了很多槽位，槽位之间从小到大排序，每个槽位指向每组中主键值最大的记录，查询时可以根据slot信息进行**二分查找**，判断数据归属于哪个组，再在组内进行查询

**分组规则**

* 对于Infimum记录所在的分组只能有1条记录。
* 对于Supremum记录所在的分组只能有1～8条记录
* 对于其他记录所在的分组只能有4～8条记录

**分组过程**

1. 将所有正常的记录（包括最大和最小记录，不包括标记为已删除的记录）划分为几个组。
2. 每个组组内最大的那条记录的头信息中的n_owned属性表示该组内共有几条记录
3. 将每个组的最后一条记录（最大的那条记录）的地址偏移量单独提取出来按顺序存储到Page Directory，这些地址偏移量被称为槽（slot）

**查询过程**

1. 通过二分法确定该记录所在的槽，并找到该槽中主键值最小的那条记录（单向链表）
2. 通过记录的 next_record 属性遍历该槽所在的组中的各个记录

注：由于slot指向的是最大值，因此我们找到符合条件slot需要向前找一位，比如slot2符合条件我们需要找到slot1，slot1最大值下一条数据即为slot2最小值

#### File Trailer
为了校验页是否完整，每个页的尾部都加了一个File Trailer部分，这个部分由8个字节组成，可以分成2个小部分

* 前4个字节代表页的校验和，与File Header中的校验和相同
* 后4字节和 File header中的 FIL_PAGE_LSN相同

这两个值与File Header中的值进行比较,看是否一致，以此来保证页的完整性

### buffer pool
缓冲池，默认大小为128M（通过innodb_buffer_pool_size配置大小通常设置为主机内存的60%，innodb_buffer_pool_instances配置缓冲池个数），缓存常用的的数据页和索引页等，在执行数据库操作时，先操作缓冲池中的数据（若缓冲池没有数据，则从磁盘加载到缓冲池），然后再以一定频率刷新到磁盘，从而减少磁盘 IO，加快处理速度

### undolog
innodb 独有，目的是为了支持事务原子性，主要作用是用于事务的回滚及MVCC控制，存储的是回滚到上一个状态执行的操作（eg:新增记录删除信息，修改记录修改前信息，删除记录写入该数据信息）

* 分类及清理机制

    1. insert undolog

新增的数据由于事务的特性，只能在当前事务中查看；因此在事务提交之后该日志会立即删除

    2. update/delete undolog

由于并发事务的存在，MVCC控制判断需要使用，因此不做删除，有专门的线程处理该日志的清理

### redolog
innodb 独有，重做日志，用于mysql服务崩溃后数据恢复。

**为什么要引入redolog：**

        在操作数据的时会先把数据页缓存到buffer pool，在buffer pool内修改，为了保证事务的持久性修改之后必须要更新到磁盘，由于数据是以页为单位进行管理，即使一点改动也需要刷新整页数据，并且一个事务很可能包含多个数据页的操作，数据页在磁盘上非连续空间，因此实时刷新磁盘效率非常低

**引入redolog后：**

        把事务在执行过程中对数据库所做的所有修改都记录到redolog，数据在buffer pool内修改完成后通过异步的方式刷新数据页到磁盘，从而提高数据库执行效率，且redolog的存在，保证了mysql服务崩溃后的数据也能进行恢复（此时buffer pool内存中的数据已经丢失），详见后续5.4章节的二阶段提交。

### binlog
binlog记录所有数据库相关的更新操作（DDL、DML）

**主要作用**

* 数据备份与恢复：可以通过备份binlog对mysql进行备份，通过读取binlog文件，使数据库恢复到特定时间点之前的状态
* 数据复制：如：主从同步

**日志格式**

有两种格式，由配置项【**binlog_format**】控制。详述如下：

* statement：记录数据库执行语句，包括函数、存储过程等，同步时只需要执行对应的sql语句及其上下文信息即可，优点：日志比较小，缺点：某些sql有状态（eg：更新一个字段为某个表最大值，id自增），会导致主从数据不一致的情况
* row：记录当前变更记录被变更成什么数据，同步时只需要修改为对应记录即可，优点：不需要记录上下文信息，不存在执行时机不同结果不同的问题，缺点：会产生大量的日志文件，占用空间大
* mixed：对能用statement记录（不会造成数据不一致的sql）采用statement记录，否则采用row记录

**示例(MIXED)：**

**create database **test_db;

![](/personal-site-mvp/img/doc-placeholder.svg "")
```
create table test_mtb
(
    id          int auto_increment primary key,
    name        varchar(256) not null comment 'name',
    age         int,
    update_time timestamp default CURRENT_TIMESTAMP
) comment 'test' charset = utf8mb4;
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
**insert into ***test_mtb *(**name**,age) **values **('test001',*55*);

![](/personal-site-mvp/img/doc-placeholder.svg "")
**update ***test_mtb ***set **age = (**select **max(age) **from **test_mtb2) **where **id = *1*;

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 查询执行过程
[流程图]
详细分析

1. **连接建立**：客户端向 MySQL 服务器发送一条查询请求，进行**身份认证、连接分配等操作**
2. **查询缓存**：接收到请求后，首先对请求进行 hash 处理并检查查询缓存，如果命中缓存，则立刻返回存储在缓存中的结果，否则进入后续流程（**注意不是buffer_pool，而是单纯查询结果的缓存，很容易失效，一般直接关闭，mysql8.0之后直接废弃了**）
3. SQL 解析：**解析器对SQL 进行解析(词法、语法、语义)**，将 SQL 转化为语法树，并传递给预处理器
4. SQL 预处理：预处理器会**验证SQL中表、字段是否存在、****将select * 中的 * 扩展为表中的各个列**
5. SQL 优化：优化器的作用就是制定一个最优的查询方案，**生成执行效率最高执行计划**
6. SQL 执行：MySQL 根据执行计划，调用**存储引擎的 API读取数据**
7. 返回结果：将结果返回给客户端，同时缓存查询结果

查询语句执行顺序

```
select 
    distinct a.name,
    count(*) cnt
from a
    left join b on a.id = b.aid
where a.name like '%test%'
group by a.name
having count(*) > 2
order by cnt desc
limit 1;
```
1. FROM：指定查询的数据源，可以是一个表、视图、子查询或表连接。在这个阶段，数据库确定要从哪些表中获取数据。
2. JOIN：根据条件a.id=b.aid 对表数据进行合并
3. WHERE：应用查询的过滤条件，筛选满足条件的记录。在这个阶段，数据库根据WHERE子句中的条件来过滤数据。
4. GROUP BY：按照指定的列对数据进行分组
5. HAVING：类似于WHERE子句，但是作用于GROUP BY后的结果集，它用于过滤分组后的数据
6. SELECT：选择要查询的列，并进行计算、聚合或转换操作
7. DISTINCT：根据指定的列对结果集进行去重，确保每行的唯一性
8. ORDER BY：对结果集进行排序，可以按照一个或多个列进行排序
9. LIMIT/OFFSET：限制结果集的数量

SQL查询语句的执行顺序是**FROM、JOIN、WHERE、GROUP BY、HAVING、SELECT、DISTINCT、ORDER BY、LIMIT/OFFSET**

## 增删改执行过程
与查询语句类似，区别在于存储引擎会写入几个日志文件

[流程图]
步骤详解

1. 前序增删改查操作（若有），一般会把最新记录放到buffer pool
2. 检测buffer pool是否有对应操作的数据，如果没有则从磁盘上读取对应数据页缓存到buffer pool（注意是整个数据页，不以记录为单位）
3. 在更新buffer pool数据之前，先写入旧数据到undolog，用于事务回滚和MVCC判断
4. 修改buffer pool内数据，此时buffer pool内数据页和磁盘不一致会标记为脏页，后续有机制把脏页刷新到磁盘
5. 写入redolog buffer pool（区别于普通buffer pool，可以简单理解为redolog的缓存），此时redolog处于**prepare阶段**
6. 刷新redolog到磁盘

 通过innodb_flush_log_at_trx_commit 参数配置，支持三种策略：

    * 0 ：设置为 0 的时候，表示每次事务提交时不进行刷盘操作，按照checkpoint操作的策略刷新（大约每秒都会刷新一次）
    * 1 ：设置为 1 的时候，表示每次事务提交时都将进行刷盘操作（默认值）
    * 2 ：设置为 2 的时候，表示每次事务提交时都只把redolog buffer 内容写入 page cache ，系统会调用 fsync 刷盘（大约每秒都会刷新一次）

除策略外，以下几种情况会刷盘

    * buffer占用超过50%时
    * MySQL正常关闭时

7. 写入binlog
8. binlog持久化完成后，通知redolog修改到**commit阶段**，此时事务已返回，执行完成
9. 异步刷新脏页数据（在buffer_pool中）到数据页（在磁盘中），触发机制：

    * redolog日志空间满的时候，会主动触发脏页刷新到磁盘中
    * buffer pool 空间满的时候，会根据淘汰算法（如LRU），淘汰一些数据页，如果淘汰的页是脏页，会先将脏页刷新到磁盘中
    * MySQL认为当前是一个空闲状态时，会对脏页刷新到磁盘中
    * MySQL正常关闭时，会将所有的脏页刷新到磁盘中

## 二阶段提交
### 为什么需要二阶段提交
假定事务新增数据D1，节点A为主节点，节点B为从节点

* 先写redolog再写binlog，写入redolog后，mysql崩溃了，服务恢复后，由于redolog写入了数据，根据redolog节点A插入数据D1，主从同步时由于binlog未写入D1，也就不会同步D1到节点B，导致主从数据不一致
* 先写binlog再写redolog，写入binlog后，mysql崩溃了，服务恢复后，由于redolog没写入数据节点A不会恢复数据D1，但是binlog有写入数据D1，因此主从同步时会把数据D1同步到节点B，导致主从数据不一致

### 引入二阶段提交后
1. redolog先写入，此时处于prepare阶段
2. binglog写入
3. redolog修改状态为commit阶段

数据库崩溃后，异常情况分析

主节点A：

* redolog的状态为commit，代表binlog也成功写入了，则提交事务
* redolog的状态为prepare，binlog中存在对应的事务信息，依旧提交事务
* redolog的状态为prepare，binlog中不存在对应的事务信息，则回滚事务

从节点B：

完全以binlog为依据，即可与主节点A保持一致

# 索引介绍
在 MySQL 中，索引是一种数据结构，用于快速查找和访问数据库表中的数据，类似于目录，可以根据索引快速定位数据

##  索引分类
**数据页内每条格式简化信息如下，后面涉及的索引结构都以图例颜色作为区分**

[流程图]
### 聚簇索引
在InnoDB中，聚簇索引是按照每张表的主键构建的一种索引方式，它是将表数据按照主键的顺序存储在磁盘上的一种方式，这种索引方式保证了行的物理存储顺序和主键的逻辑顺序相同，所以查找聚簇索引的速度非常快。数据结构是典型的B+树。

* 聚簇索引将数据行存储在索引的叶子节点中，而不是单独的数据页中。这意味着索引本身就包含数据的一部分，可以通过索引直接访问数据，而不需要额外的查找过程
* 聚簇索引只能有一个，通常是表的主键索引。因为数据行本身就是按照主键的顺序存储的，所以聚簇索引可以大大提高主键查询的性能。
* 由于数据行存储在索引中，如果表中没有主键或唯一索引，MySQL会自动生成一个隐藏的聚簇索引

**索引结构示例**

[流程图]
**数据量计算(粗略)**

**eg:**3层结构B+Tree

每页16Kb，每页数据固定占用：128b，每条数据固定占用：记录头占用5b，指针占用6b，数据页内平均6条数据产生一个slot(存放在Page Directory)，每个slot占用16b

假设id类型为int占用4b，每条数据占用800b

* 第一层：(16*1024-128)/(5+6+4)=1083，Page Directory占用：1083/6*16=2888，所以第一层(16*1024-128-2888)/(5+6+4)约为890条目录信息
* 第二层：890*890=792100条目录信息
* 第三层：792100*((16*1024-128)/800)=16095472，slot占用：20/6*16约为54，除去slot约为：16042005 条数据信息

结论：int类型主键，800b数据大小，3层结构大概可存储16042005条数据

同时可以看出，主键数据类型（如非int而为long类型）也会影响数据存储量，进而影响到查询效率

### 非聚簇索引
在InnoDB中，非主键索引都是非聚簇索引（二级索引）

* 非聚簇索引将索引和数据分开存储，索引中存储的是主键+索引列。查询时需要先通过索引查找到数据行的引用，再通过主键找到实际的数据行
* 可以有多个非聚簇索引，可以是普通索引或唯一索引
* 非聚簇索引可以提高查询效率，但在数据量很大的情况下，可能会增加额外的I/O开销，因为查询需要先访问索引，再访问数据页（也称为回表）

**索引结构示例**

[流程图]
#### 联合索引
**索引结构示例**

[流程图]
索引按照联合索引c1列先排序，第一列相同再按照第c2排序，因此索引使用时，需要遵从**最左匹配原则**

**最左匹配原则：**

最左匹配原则是指，在使用联合索引进行查询时，查询条件必须从索引的最左边的列开始，并且连续地使用索引中的列

示例：

如图c1，c2联合索引

执行select * from tb where c1=xxx;select * from tb where c1=xxx and c2 = xxxx;能使用到索引

执行select * from tb where c2=xxx;不能使用到索引

## 索引回表
当根据非聚簇索引查询的时候，会先通过该索引查询到主键，再通过主键的值进行一次查询才能获取到我们想要的数据，这个过程叫做回表，回表会增加IO次数，降低查询效率

```
eg：
表：tb，字段 id、name、age 、gender，主键id， 索引字段：age，假如用到了age索引
查询语句：select name,age from tb where age = 100
非聚簇索引叶子结点存储的不是完整数据，而是id+age，获取name字段的值需要根据id信息再遍历一遍聚簇索引(主键)，通过聚簇索引获取到name字段值，这个过程叫做回表
```
## 索引覆盖（Covering Index）
当执行查询操作时，直接通过索引树中的信息包含了所需要的字段，而不需要回表查询数据行，减少了I/O操作，可提高查询效率

```
eg：
表：tb，字段 id、name、age 、gender，主键id， 索引字段：idx_name_age（name、age），假如用到了name,age联合索引
查询语句：select age from tb where name like '张%'
非聚簇索引叶子结点存储的是id+name+age，因此可以直接获取到age字段的值，无需回表
```
## 索引下推(Index Condition Pushdown，简称ICP)
下推其实就是指将部分上层（服务层）负责的事情，交给了下层（引擎层）去处理。

在没有使用ICP的情况下，查询过程：

* 存储引擎读取索引记录
* 根据索引中的主键值，获取完整数据（回表）
* 存储引擎把记录返回给Mysql服务端，服务端再根据**完整的WHERE条件**进行筛选

使用ICP的情况下，查询过程：

* 存储引擎读取索引记录
* 判断WHERE条件部分能否用索引中的列来做检查，若可以则先行过滤：
    * 条件不满足，直接过滤掉
    * 条件满足，根据索引中的主键值，获取完整数据（回表）

* 存储引擎把记录返回给Mysql服务端，服务端再根据剩余的WHERE条件进行筛选

```
eg：
表：tb，字段 id、name、age 、gender，主键id， 索引字段：idx_name_age（name、age），假如用到了name,age联合索引
查询语句：select * from tb where name like '张%' and age = 10
未使用ICP存储引擎根据通过索引idx_name_age找到name like '张%' 的主键id，回表查询完整记录，返回给服务端，服务端再根据age=10进行筛选
使用ICP：存储引擎根据通过索引idx_name_age找到name like '张%'的索引记录 ，再继续过滤age=10的索引记录，在回表查询前过滤出符合条件的数据再回表查询完整记录
```
## 索引创建原则
* 常用的查询条件
    * 经常查询的列
    * 经常用于外联的列
    * 经常用于order by、group by、distinct的字段

* 区分度高的字段
    * 有个特殊情况：某个数据区分度不高但是某种状态能过滤掉大部分数据，如file_info的status，开始数据全为20全量跑完后，status全为50，新数据进来是20，此时20是少部分数据，走索引效率较高

* 考虑联合索引，尽量符合索引覆盖
* 过长字段创建前缀索引
* 避免在经常更新的字段创建索引
* 避免过度索引，过多的索引可能会导致增删改操作变慢，增加存储空间的使用，影响性能



# 表设计
## 遵循原则
基本原则

* 结构清晰：表名，字段命名没有歧义
* 唯一职责：一表一用，定义清晰，不存储无关信息，相关数据在一张表中
* 主键：不使用带业务意义的主键

完备性

* 完整性：保证数据的准确性与完整性，重要内容都要有记录
* 可追溯：可追溯创建人、创建时间、修改人、修改时间，删除采用逻辑删除
* 一致性原则：数据之间保持一致，尽可能避免同样的数据存储在不同表中

扩展性

* 长短分离：长文本短文本分离， 长文本存储在k-v系统中（mongo、es等）
* 冷热分离：数据量较大的表，可采用当前数据与历史数据分离

## 建表建议
1. 选择合适的数据类型
在创建表时，选择适合存储数据的最小数据类型。使用更小的数据类型可以减少存储空间，提高查询性能
2. 设计合适的主键
选择合适的主键可以提高数据访问的效率，通常使用整数类型比字符串查询效率更高（占用内存更少，索引比较数值类型比字符串更快）
3. 添加合适索引
对于常用的查询条件、连接字段、唯一属性，考虑添加索引提高数据查询效率，但是过多的索引会影响写入性能，因此需要根据实际情况适当添加
4. 适当遵循范式

遵循范式可以提高数据的一致性，但可能会增长额外的查询成本，冗余数据可以提高查询性能，但是需要维护多个表之间数据一致性，需要均衡考虑

5. 合理设置字段属性
在定义表的字段时，根据实际需求设置字段的属性，如是否允许 NULL 值、默认值、字段长度等，合理设置这些属性可以提高数据的完整性和查询性能
6. 分库和分表
如果表中的数据量非常大时，可以考虑使用分库、分表等技术来拆分数据，以提高效率



# 常见问题排查
## MySQL死锁分析
1. 执行 SHOW ENGINE INNODB STATUS 命令，查看INNODB 详细状态信息

    * 在状态信息的输出内容中，寻找 "LATEST DETECTED DEADLOCK" 一行，该行下面的内容为最近一次检测到的死锁信息，包括事务 ID、死锁查询语句、锁等待、锁持有等信息

```
------------------------
LATEST DETECTED DEADLOCK
------------------------
2024-04-19 15:11:35 0x4f20
*** (1) TRANSACTION:
TRANSACTION 3124, ACTIVE 12 sec starting index read
mysql tables in use 1, locked 1
LOCK WAIT 3 lock struct(s), heap size 1136, 2 row lock(s)
MySQL thread id 88, OS thread handle 13080, query id 7043 localhost 127.0.0.1 root statistics
/* ApplicationName=IntelliJ IDEA 2021.2 */ select * from test_tb where id = 1 for update
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 28 page no 3 n bits 80 index PRIMARY of table `test_db`.`test_tb` trx id 3124 lock_mode X locks rec but not gap waiting
Record lock, heap no 2 PHYSICAL RECORD: n_fields 5; compact format; info bits 0
 0: len 4; hex 80000001; asc     ;;
 1: len 6; hex 000000000be0; asc       ;;
 2: len 7; hex a5000001190110; asc        ;;
 3: len 7; hex 74657374303031; asc test001;;
 4: len 4; hex 80000001; asc     ;;
```
    * 在状态信息的输出内容中，查找 "TRANSACTIONS" 一节，该节下面的内容为当前所有的活跃事务信息，包括事务 ID，锁等待等信息

```
*** (2) TRANSACTION:
TRANSACTION 3123, ACTIVE 20 sec starting index read
mysql tables in use 1, locked 1
3 lock struct(s), heap size 1136, 2 row lock(s)
MySQL thread id 87, OS thread handle 20256, query id 7056 localhost 127.0.0.1 root statistics
/* ApplicationName=IntelliJ IDEA 2021.2 */ select * from test_tb where id = 10 for update
```
2. 查询 INNODB_LOCKS 和 INNODB_LOCK_WAITS 系统表，查看当前锁信息和等待信息

SELECT * FROM information_schema.INNODB_LOCKS;

SELECT * FROM information_schema.INNODB_LOCK_WAITS;

3. 查看当前事务信息

SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;

如何尽可能避免死锁

* 合理的设计索引，使业务 SQL 尽可能通过索引定位更少的行，减少锁竞争
* 调整 SQL 执行顺序， 避免 update/delete 长时间持有锁的 SQL 在事务前面
* 避免大事务，尽量将大事务拆成多个小事务来处理，小事务发生锁冲突的几率更小
* 以固定的顺序访问表和行，比如两个更新数据的事务，事务 A 更新数据的顺序为 1，2;事务 B 更新数据的顺序为 2，1，这样可能会造成死锁

## MySQL连接问题分析
###  查看最大连接数
SHOW VARIABLES LIKE 'max_connections';

### 查看当前连接数
SHOW GLOBAL STATUS LIKE 'Threads_connected';

### 查看运行中的线程列表
SHOW FULL PROCESSLIST;

可以帮助我们查看哪些sql正在执行，它们的状态已经执行了多长时间等信息

![](/personal-site-mvp/img/doc-placeholder.svg "")
* Id: 线程的唯一标识符。
* User: 执行该命令的用户名。
* Host: 用户的主机名。通常是客户端IP地址、端口号或者都有。
* db: 当前线程正在工作的数据库。如果没有选定数据库，则为NULL。
* command: 线程正在执行的命令类型

具体类型详见附件-附录.xlsx

* Time: 命令开始执行以来的秒数。对于'Sleep'命令，这是线程进入睡眠状态的时间。
* State: 显示线程的状态信息。这对找出性能问题特别有用

具体状态详见附件-附录.xlsx

* Info: 显示线程正在执行的查询。若没有查询在执行则该列为NULL。
* 如果没有 FULL 关键字， SHOW PROCESSLIST 则仅显示 Info 字段中每个语句的前 100 个字符

### 连接问题解决思路
结合以上命令，对比业务逻辑排查分析，可从以下思路进行排查

* 增加数据库最大连接数
* 修改业务逻辑，如批量数据写入合并为一个sql执行等
* 避免慢sql占用连接
* 避免长事务占用连接
* 避免锁等待占用连接

## MySQL整体效率降低排查
资源使用情况排查：

* 使用top、htop等查看服务器CPU和内存的使用情况
* 使用iostat等工具检查磁盘I/O的使用情况
* 使用df -h等命令检查磁盘空间使用情况
* 其他监控手段如普罗米修斯监控等

MySQL性能查询：

* 使用SHOW GLOBAL STATUS;查看MySQL服务器的全局状态
* 使用SHOW FULL PROCESSLIST;查看当前运行的sql，识别长时间运行的sql，排查其执行慢的原因

分析MySQL日志：

* 查看MySQL的错误日志，查看是否有系统错误
* 查看MySQL的慢SQL日志，分析是否有慢SQL导致锁竞争等问题

优化配置：

* 考虑是否需要调整表结构、索引或查询逻辑以提高性能
* 根据监控结果，调整MySQL配置参数，如innodb_buffer_pool_size、max_connections、query_cache_size等

## 慢sql排查
### EXPLAIN参数详解
示例sql表结构：

```
drop table if exists students;
CREATE TABLE students
(
    id         INT PRIMARY KEY AUTO_INCREMENT,
    student_no VARCHAR(20) NOT NULL COMMENT '学号',
    name       VARCHAR(50) NOT NULL COMMENT '姓名',
    age        INT COMMENT '年龄',
    class_id   INT COMMENT '班级ID',
    INDEX idx_name_age (name, age),
    INDEX idx_class_id (class_id),
    UNIQUE INDEX idx_student_number (student_no)
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4 COMMENT ='学生信息表';
DROP TABLE IF EXISTS classes;
CREATE TABLE classes
(
    id   INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL comment '名称',
    INDEX idx_name (name)
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4;
```
以 explain select * from sys_user 为例，得到的结果如下：

![](/personal-site-mvp/img/doc-placeholder.svg "")
下面做一个详细说明：

1. id：执行 select 语句查询的序列号，常见情况：

* id相同：执行顺序由上至下
* id不同：如果是子查询，id 的序号会递增，id 值越大优先级越高,越先被执行
* id相同不同均存在：如果 id 相同，可以认为是一组，从上往下顺序执行，在所有组中，id值越大，优先级越高，越先执行

2. select_type**：**数据读取操作的操作类型

* simple：简单的 select 查询，查询中不包含子查询或者union
* primary：查询中若包含复杂的子查询，最外层查询则被标记为primary
* subquery：在 select 或者 where 列表中包含了子查询
* dependent subquery：子查询中的第一个 SELECT， 取决于外面的查询。 即子查询依赖于外层查询的结果。
* derived：在 from 列表中包含的子查询被标记为 DERIVED（衍生表），mysql 会递归执行这些子查询，把结果放临时表中；
* union：若第二个 select 出现在 union 之后，则被标记为 union，若 union 包含在 from 子句的子查询中，外层 select 将被标记为 derived；
* union result：从 union 表（即 union 合并的结果集）中获取 select 查询的结果；
* meterialized：物化表，子查询关联查询时，子查询结果存储在物化临时表，然后根据临时表中的数据去主表匹配。
* dependent union：UNION 中的第二个或后面的查询语句，取决于外面的查询

3. table：显示的查询表名，如果查询使用了别名，那么这里显示的是别名，如果不涉及对数据表的操作可能是以下值：

* null
* <derivedN>：表示这个是临时表，后边的N就是执行计划中的 id，表示结果来自于这个查询产生
* <unionM,N>：与<derivedN>类似，也是一个临时表，表示这个结果来自于 union 查询的 id 为 M,N 的结果集
* <subqueryN>：该行是指与物化子查询该行的结果 id 的值 N

4. partitions：查询将匹配记录的分区。该值NULL用于非分区表。
5. **type：**查询时使用的索引类型，**非常重要的分析参数**

* system：系统表，只有少量数据， const 类型的特例
* const：表示通过索引一次就找到了，const 用于比较 primary key 或者 unique 索引，因为只匹配一行记录，所以很快。 如果将主键置于 where 列表中，mysql 就能将该查询转换成一个常量；

eg：EXPLAIN SELECT * FROM students WHERE id=1;

* eq_ref：唯一性索引扫描，对于每一个索引键，表中只有一条记录与之匹配，常用于主键或唯一索引扫描；此类型通常出现在多表的 join 等值查询，表示对于前表的每一个结果，都只能匹配到后表的一行结果，查询效率较高。

eg：EXPLAIN SELECT * FROM students s,classes c WHERE s.class_id=c.id;

* ref：非唯一性索引扫描，返回匹配某个单独值的所有行，本质上也是一种索引访问，所以它应该属于查找和扫描的混合体；

eg：EXPLAIN SELECT * FROM students WHERE class_id=1;

* ref_or_null：二级索引等值比较同时限定 is null 。

eg：EXPLAIN SELECT * FROM students WHERE name='张三' or name IS NULL;

* range：只检索给定范围的行，使用一个索引来选择行，key列显示使用哪个索引，一般就是在你的 where 语句中出现了 between、<、>、in 等的查询；这种范围索引扫描比全表扫描要好，因为它只需要开始于索引的某一个点，结束于另一个点，不用扫描全部索引；

eg：EXPLAIN SELECT * FROM students WHERE student_no BETWEEN 6 and 10;

* index：全索引树扫描，通过遍历索引树找出匹配数据（常见于不符合最左匹配原则索引查询）

eg：EXPLAIN SELECT name FROM students WHERE age=7;

* all：也就是全表扫描；
* index_merge：索引合并，分为intersection交集、union并集、sort union排序并集三种方式

**效果从好到差：system>const>eq_ref>ref>ref_or_null>range>index>all**

除了all之外，其他的type都使用到索引；除了index_merge之外，其他的type只会用到一个索引

6. possible_keys：查询可能使用到的索引
7. **key：查询真正使用到的索引**，上述type为index_merge时，这里可能出现两个以上的索引，其他情况只会出现一个
8. **key_len**：key_len 表示该列计算查询中使用的索引的长度，通过该值可以算出具体使用了索引中的哪些列，规则如下表所示：

|类型|描述|
|-|-|
|CHAR(n)|n 字节长度|
|VARCHAR(n)|如果是 utf8 编码，则是 3 n + 2字节;如果是 utf8mb4 编码，则是 4 n + 2 字节。|
|TINYINT|1字节|
|SMALLINT|2字节|
|MEDIUMINT|3字节|
|INT|4字节|
|BIGINT|8字节|
|DATE|3字节|
|TIMESTAMP|4字节|
|DATETIME|8字节|
|NULL|占用一个字节，如果一个字段是 NOT NULL 的， 则不占用|

9. ref：哪些列或常量被用于查找索引列（key列索引）上的值

* 如果是使用的常量等值查询，显示const
* 如果是连接查询，被驱动表的执行计划，显示驱动表的关联字段
* 如果是条件使用了表达式或者函数，或者条件列发生了内部隐式转换，这里可能显示为func
* 其他情况显示null

10. rows：估算的扫描行数
11. filtered：表示通过查询条件获取的最终记录行数占通过type字段指明的搜索方式搜索出来的记录行数的百分比
12. **Extra：额外信息**，常见信息如下：

* using filesort：说明mysql会对数据使用一个外部的索引排序，而不是按照表内的索引顺序进行读取。mysql中无法利用索引完成的排序操作称为“文件排序”。排序时无法使用到索引时，就会出现这个。常见于order by语句中，需要优化
* using index：查询时不需要回表查询，直接通过索引就可以获取查询数据，如果同时出现using where表示查询的列被索引覆盖，并且where筛选条件是索引列之一但是不是索引的前导列，意味着无法直接通过索引查找来查询到符合条件的数据
* using where：表示存储引擎返回的记录并不是所有的都满足查询条件，需要在server层进行过滤。查询条件中分为限制条件和检查条件，5.6之前，存储引擎只能根据限制条件扫描数据并返回，然后server层根据检查条件进行过滤再返回真正符合查询的数据。5.6.x之后支持ICP特性(index condition pushdown，索引下推)，可以把检查条件也下推到存储引擎层，不符合检查条件和限制条件的数据，直接不读取，这样就大大减少了存储引擎扫描的记录数量。extra列显示using index condition
* using temporary：表示使用了临时表存储中间结果，常见于order by和分组查询group by
* using join buffer（block nested loop），using join buffer（batched key accss） ：5.6.x之后的版本优化关联查询的BNL，BKA特性。主要是减少内表的循环数量以及比较顺序地扫描查询
* impossible where：where语句会导致没有符合条件的行，一般不会出现（eg：select * from students where name=‘test1’and name = ‘test2’）

进行sql优化时重点关注执行计划如下信息：

* key：查看有没有使用索引
* key_len：查看索引使用是否充分
* type：查看索引类型，至少要达到 range 级别
* extra：查看附加信息：排序、临时表、索引覆盖、索引下推等

一般情况下根据这4列就能找到索引问题

### 索引失效情况
1. 不满足最左匹配原则
2. 索引列用了函数或者计算（高版本可通过函数索引解决此问题）
3. 隐式类型转换（如数值转为字符串）
4. 使用了select *
5. like左边包含%
6. 使用or关键字，如果使用了or关键字，那么它前面和后面的字段都要加索引，不然所有的索引都会失效
7. not in关键字、not exists关键字
8. !=、<>可能导致索引失效
9. is not null

### 慢sql常见原因及优化
1. 表数据量大

* 考虑冷热数据分表
* 分库分表等技术

2. 连表过多

* 考虑拆分为多次查询一般连表不超过3个
* 考虑小表先连表之后再连主表

3. sql复杂，子查询多

* sql拆分，减少子查询

4. 未使用索引

* 针对索引失效的情况进行分析，优化sql
* 创建合适索引

5. 未使用正确索引

* 采用force index，强行指定一个索引，不推荐（后续数据分布变了mysql不能选择合适索引）
* 修改语句，引导MySQL使用我们期望的索引
* 新建一个更适合的索引，来提供给优化器，或者删除掉误用的索引

6. 回表次数多

* 索引尽量符合索引覆盖



# 附件
[附件: 附录.xlsx | 17.2KB | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | fileId=26c8029b42b24a899f5b214db6c78ec3]

