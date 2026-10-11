---
title: "1、更新或插入数据 zadd"
description: "关系型数据库管理系统（Relational Database Management System）：列+行，同一个表下数据的结构是一样的。 非关系型数据库Not only SQL：数据存储没有固定的格式，并且可以进行横向扩展。"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\数据库\\数据库_引用文档\\redis.md"
---
redis

## 一、介绍
### 非关系型数据库
传统RDBMS和NoSQL：

* 关系型数据库管理系统（Relational Database Management System）：列+行，同一个表下数据的结构是一样的。
* 非关系型数据库(Not only SQL)：数据存储没有固定的格式，并且可以进行横向扩展。

```
RDBMS
 - 组织化结构
 - 固定SQL
 - 数据和关系都存在单独的表中（行列）
 - DML（数据操作语言）、DDL（数据定义语言）等
 - 严格的一致性（ACID): 原子性、一致性、隔离性、持久性
 - 基础的事务
NoSQL
 - 不仅仅是数据 
 - 没有固定查询语言
 - 键值对存储（redis）、列存储（HBase）、文档存储（MongoDB）、图形数据库（Neo4j）
 - 最终一致性（BASE）：基本可用、软状态/柔性事务、最终一致性
```
### **Redis 是什么**
Redis 是一个开源的、使用C语言编写的、支持网络交互的、可基于内存也可持久化的Key-Value数据库。它可以用作**数据库、缓存和消息中间件；**

### 使用场景
1.排行榜TOP应用

2.Pub/Sub构建实时消息系统

3.计数器应用

4.取最新N个数据的操作

5.Uniq操作,获取某段时间所有数据排重值

### redis 如何实现高性能和高并发
* redis 是一个**内存数据库**，读写非常高效。内存的响应时间大约是 100纳秒 ，这是Redis每秒万亿级别访问的重要基础。除了开启 AOF，RDB 异步线程去持久化数据，基本没有磁盘I/O消耗，性能方面是比 mysql，oracle 快很多。
* redis 自己实现一套**简单高效的基础数据结构**：动态字符串（SDS），链表，字典，跳跃链表，整数集合和压缩列表。然后在这个基础上去实现用户能操作的对象：字符串，列表，哈希，集合，有序集合等对象。每种结构只做自己爱做的事，当然比数据库只有Table，MongogoDB只有JSON一种结构快了。
* 使用了** I/O 多路复用**去同时监控多个套接字，这是一种高效的I/O模型。
* 事件处理器是**单线执行**的，这大大减少CPU的上下文切换，和对资源锁的竞争问题，极大提高redis服务处理速度（至于为啥使用单线程，因为CPU够用了，它的性能瓶颈在内存而不是CPU）。
* Redis直接自己构建了VM 机制 ，因为一般的系统调用系统函数的话，会浪费一定的时间去移动和请求。

## 二、安装
参考：[redis安装与配置](../../redis/redis_引用文档/redis安装与配置.md)

## 三、实际应用
### 排行榜TOP应用
redis的zset可以很方便地用来实现排行榜功能。

```
import redis

board = redis.Redis(host='localhost', port=6379, password='zj1113')

# 1、更新或插入数据 zadd
N = 10
for i in range(1, N):
    board.zadd('top10', {'usr%s' % i: i * 100})

# 2、获取某个区间(排名)榜单数据 zrange、zrevrange
top10 = board.zrange('top10', 0, -1, withscores=True)  # zrevrange从大到小，zrange从小到大
print('获取排行榜: %s' % top10)
# 获取排行榜: [(b'usr1', 100.0), (b'usr2', 200.0), (b'usr3', 300.0), (b'usr4', 400.0), (b'usr5', 500.0), (b'usr6', 600.0), (b'usr7', 700.0), (b'usr8', 800.0), (b'usr9', 900.0)]

# 3、获取某范围内积分的榜单 zrangebyscore、zrevrangebyscore
rangebyscore = board.zrevrangebyscore('top10', 400, 200, withscores=True, score_cast_func=int)  # 注意：大值在前，小值在后
print('获取排行榜: %s' % rangebyscore)
# 获取排行榜: [(b'usr4', 400), (b'usr3', 300), (b'usr2', 200)]

# 4、获取用户排名 zrank、zrevrank
rank = board.zrank('top10', 'usr2')
print('获取用户排名: %s' % rank)  # 获取用户排名: 1

# 5、获取用户分数 zscore
score = board.zscore('top10', 'usr5')
print('获取用户分数: %s' % score)  # 获取用户分数: 500.0

# 6、更新用户分数 zadd、zincrby
board.zadd('top10', {'usr1': 120})
print(board.zscore('top10', 'usr1'))  # 120.0
board.zincrby('top10', 20, 'usr1')  # 在原基础上增加20
print(board.zscore('top10', 'usr1'))  # 140.0

# 7、数量统计 zcard、zcount
cards = board.zcard('top10')  
print('榜单数量: %s' % cards)  # 榜单数量: 9
counts = board.zcount('top10', 600, 700)
print('区间范围榜单数量: %s' % counts)  # 区间范围榜单数量: 2

# 8、删除元素 zrem、zremrangebyrank、zremrangebyscore
# 删除元素
board.zrem('top10', 'usr1')  
print(board.zrange('top10', 0, -1))  # [b'usr2', b'usr3', b'usr4', b'usr5', b'usr6', b'usr7', b'usr8', b'usr9']
# 批量删除min到max区间内元素
board.zremrangebyrank('top10', 1, 2)  
print(board.zrange('top10', 0, -1))  # [b'usr2', b'usr5', b'usr6', b'usr7', b'usr8', b'usr9']
# 批量删除minscore到maxscore分数区间内元素
board.zremrangebyscore('top10', 700, 800,)  
print(board.zrange('top10', 0, -1))  # [b'usr2', b'usr5', b'usr6', b'usr9']
# 批量删除整张表
board.zremrangebyrank('top10', 0, -1)  
print(board.zrange('top10', 0, -1))  # []
```
### Pub/Sub构建实时消息系统
使用Redis的订阅功能来快速获取最新实时数据。

Redis的订阅功能使用“发布/订阅”模式，即发布者向通道发布消息，订阅者订阅通道并接收发布者发送的消息。当发布者向通道发布消息时，所有订阅该通道的订阅者都能够接收到该消息。这一功能最明显的用法就是用作实时消息系统，比如普通的即时聊天，群聊等功能。

```
import datetime
import time
import redis
import threading

r = redis.Redis(host='localhost', port=6379, password='zj1113')


def subscribe():
    """ 订阅 """
    pubsub = r.pubsub()
    pubsub.subscribe('channel1', 'channel2')
    for item in pubsub.listen():
        if item['type'] == 'message':
            print('Get message from %s: message = %s, @%s' % (item['channel'], item['data'], datetime.datetime.now()))


subscribe_thread = threading.Thread(target=subscribe)
subscribe_thread.start()

for i in range(3):
    r.publish('channel1', 'meg #%s!' % i)
    time.sleep(1)

for i in range(2):
    r.publish('channel2', 'meg #%s!' % i)
    time.sleep(0.5)

```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 计数器应用
统计服务运行次数。

```
import redis

cache = redis.Redis(host='localhost', port=6379)
res = cache.incr('hits')
print(res)
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 4、取最新N个数据的操作
将最新的10条评论的ID放在Redis的List集合里面

```
import redis

r = redis.Redis(host='localhost', port=6379, password='zj1113')
N = 10
# 把当前登录人添加到链表里
for i in range(12):
    ret = r.lpush("last10", i)
# 保持链表只有N位
r.ltrim("last10", 0, N-1)
# 获得前N个最新登陆的用户Id列表
last_login_list = r.lrange("last10", 0, N-1)
print(last_login_list)
# [b'11', b'10', b'9', b'8', b'7', b'6', b'5', b'4', b'3', b'2']
```
## 四、数据类型与常用命令
详细命令参考：[https://redis.io/commands/](https://redis.io/commands/)

### Strings
Redis字符串存储字节序列，包括文本、序列化对象和二进制数组。

通常用于缓存，但它们支持额外的功能，允许实现计数器并执行按位操作。

默认情况下，单个Redis字符串的最大值为512 MB。

|**方法**|**说明**|**特性**|
|-|-|-|
|**set**|设置key对应的的值为String类型的value|   |
|**get**|获取对应key对应的String的值，如果不存在返回nil|   |
|**setnx**|设置可以为对应的值为String类型的value，如果key存在返回0不覆盖，不存在返回1|nx的意思为not exist。**对实现锁很有用。**|
|setex|置key对应的值为String类型的value，并指定此键值对应的有效期SETEX key seconds value|例：setex mykey 10 你好|
|setrange|设置key的value的子字符串|setrange key 位置 替换的内容如果替换内容没有原value长,则原value剩余的内容将被保留|
|**mset**|一次设置多个key的值，成功返回ok，失败返回0，要成功都成功，要不成功全部失败|mset key1 内容一 key2 内容二|
|msetnx|一次设置多个key的值，成功返回ok，失败返回0，不覆盖已经存在的值，要成功都成功，要失败都失败|   |
|**getset**|设置key的值并返回key的旧值|getset key newValuse|
|getrange|获取key对应的value子字符串|getrange key 0 5 //获取前6个字符|
|mget|批量获取|mget key1 key2 key3 //没有设置则返回空|
|**incr**|对key的值做增加操作,并返回新的值|   +1。**命令将字符串值解析为整数，将其增加一个，最后将获取的值设置为新值。**|
|incrby|对可以的value加指定的值|key如果不存在会设置key并value为0incrby key1 5 //对key1的值加5|
|decr|对key的值做减减操作|    -1|
|decrby|对key的值减去指定值|   |
|append|给指定key的字符串追加value，返回新的字符串长度|   |
|strlen|取指定key的value值的长度|   |

### Lists
Redis的list是每个子元素都是String类型的双向链表，可以通过push和pop操作从列表的头部或者尾部添加或者删除元素，这样List即可以作为栈，也可以作为队列。  一个列表最多可以包含 232 - 1 个元素 (4294967295, 每个列表超过40亿个元素)。

Redis列表经常用于：

* 实现堆栈和队列
* 为后台工作者系统构建队列管理

将列表视为队列（先进先出）：

```
r.lpush("bikes:repairs", "bike:1")  # >>> 1
r.lpush("bikes:repairs", "bike:2")  # >>> 2
r.rpop("bikes:repairs")  # >>> bike:1
r.rpop("bikes:repairs")  # >>> bike:2
```
将列表视为堆栈（先进后出）：

```
r.lpush("bikes:repairs", "bike:1")  # >>> 1
r.lpush("bikes:repairs", "bike:2")  # >>> 2
r.lpop("bikes:repairs")  # >>> bike:2
r.lpop("bikes:repairs")  # >>> bike:1
```
|**方法**|**说明**|**特性**|
|-|-|-|
|**lpush**|在key所对应的list头部添加一个元素|l的意思是left，视为头部|
|**rpush**|在key说对应的list尾部添加一个元素|r的意思是right，视为尾部|
|lrange|显示list里面的内容|lrange 0 -1 //全部显示|
|linsert|在key对应的list|linsert mylist before one myvalue|
|lset|设置list中指定下标元素的值|lset mylist index myvalue|
|lrem|从key对应的list中删除n个和value相同的元素,结果返回影响元素的个数，n<0从尾部开始删除，n=0全删除|lrem mylist count "value"|
|**ltrim**|保留指定key范围内的数据，返回ok成功|ltrim mylist 0 3 //0-3是保留的范围|
|**lpop**|从list的头部删除一个元素，并返回该删除的元素||
|**rpop**|从list的尾部弹出一个元素，并返回该删除的元素||
|rpoplpush|从第一个list的尾部元素异常元素并添加到第二个list的头部|rpoplpush mylistA mylistB|
|lindex|返回list位置的元素|lindex mylist 3|
|**llen**|返回list中元素的个数|llen mylist|

### Sets
Redis集合是唯一字符串（成员）的无序集合。集合对象的编码可以是 intset 或者 hashtable。

Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。

Redis集合可用来：

* 跟踪唯一项目（例如，跟踪访问给定博客文章的所有唯一IP地址）。
* 表示关系（例如，具有给定角色的所有用户的集合）。
* 执行共同的集合操作，如交叉、联合和差异。

|**方法**|**说明**|**特性**|
|-|-|-|
|**sadd**|向名称为key的set中添加元素，返回影响元素的个数，0为失败，1为成功|sadd myset value|
|smembers|查看集合中所有的成员|smebers myset|
|**srem**|删除集合的一个元素|srem myset two|
|spop|随机返回并删除set中一个元素|spop myset|
|sdiff|返回所有set与第一个set的差集|sdiff myset1 myset2|
|sdiffstore|比较差集并且存储到另一个set中，返回1代表成功|sdiffstore setstoreSet mySet1 myset2|
|**sinter**|返回所有给定集合的交集|sinter myset1 mysert2 //1集合和2集合的交集|
|sinterstore|返回给定集合的交集并存储到另一个集合|sinterstore desset myset1 myset2 //存到desset集合中|
|sunion|返回所有给定集合的并集|sunion set1 set2|
|sunionstore|返回所有的并集并且存储到另一个集合中，返回影响的元素个数|sunionstore destSet myset1 myset2|
|smove|把第一个集合的元素移动到第二个集合中|smove myset myset 你好|
|**scard**|返回集合中元素的个数|scard myset1|
|**sismember**|测试某个元素是否在集合中，返回0是不是，大于0是存在|sismember mykey1 你好|
|srandmember|随机返回个集合中的元素|srandmemeber myset1|

### Hashs
它是一个String类型的field和value的映射表。可以用来表示基本对象和存储计数器的分组等。hash 特别适合用于存储对象。

```
res1 = r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)
r.hget("bike:1", "price")  # >>> '4972'
r.hincrby("bike:1", "price", 100)  # >>> 5072
r.hmget("bike:1", ["model", "price"])  # >>> ['Deimos', '4972']
r.hgetall("bike:1")  # >>> {'model': 'Deimos', 'brand': 'Ergonom', 'type': 'Enduro bikes', 'price': '4972'}
```
|**方法**|**说明**|**特性**|
|-|-|-|
|**hset**|设置一个hash 的field为指定值，如果key不存在则先创建|hset tab ke1 val1|
|**hget**|获取某个hash的某个field值|hget tab ke1|
|hsetnx|类似string只是操作的是hash|   |
|hmset|批量设置hash的内容|   |
|**hmget**|获取hash表的全部key值|Hmget key field1 field2|
|**hincrby**|给hash表的某个字段增加值|   |
|hexists|判断hash表中某个key是否存在|   |
|hlen|返回hash表中的key数量|   |
|hdel|删除指定hash表的某个键值对|   |
|hkeys|返回hash表中所有的key|    |
|hvals|返回hash表中所有的value|   |
|hgetall| 获取hash表中所有key和value|   |

### Sorted Sets
和Sets相比，Sorted Sets增加了一个权重参数score，使得集合中的元素能够按score进行有序排列。

排序集的一些用例包括：

* 排行榜。例如，可以使用排序集来轻松维护大型在线游戏中最高分的有序列表。
* 速率限制器。特别是，可以使用排序集来构建滑动窗口速率限制器，以防止过多的API请求。

|**方法**|**说明**|**特性**|
|-|-|-|
|**zadd**|向zset中添加元素member，score 用于排序，如果元素存在，则更新其顺序,返回0代表没添加成功|ZADD key score memberzadd myset 3 itim|
|**zrange**|取出集合中的元素|zrange myset 0 -1 withscores//显示序号by index|
|**zrem**|删除名称为key的zset中的元素member|zrem myset itim|
|zincrby|修改元素的排序，如果元素不存在则添加该元素，且排序的score值为增加值|zincrby myzset score itim|
|**zrank**|返回元素在集合中的排序位置，就是索引值|zrank myzset itim //itim在集合中的位置|
|zrevrank|返回从大到小的排序索引值，就是逆序位置|zrevrangk myzset itim//逆序的位置|
|zrevrange|返回集合中从大到小排序（降序）的，索引start到end的所有元素|zrevrange myzset 0 -1 //逆序后的元素|
|**zrangebyscore**|根据排序索引的scores来返回元素|zrangebyscore myzset 1 3 withscores//|
|zcount|返回集合中给定区间的数量|zcount myzset 2 4 //集合中2-4索引元素的个数|
|zcard|返回集合中所有元素的个数|zcard myzset //返回所有元素的个数|
|zremrangebyrank|删除集合中排序在给定区间的所有元素(按索引删除)|zremrangebyrank myzset 2 3 //|
|zremrangebyscore|删除集合中在给定排序区间的元素 (按顺序删除)||

### Streams
Redis Stream 是 Redis 5.0 版本新增加的一种专门用来处理`消息队列`场景的高级数据结构。

参考：[Redis Stream](../../redis/redis_引用文档/Redis Stream.md)

## 五、详细分析
### 1、具体实现
#### 持久化
单机式Redis存在以下问题，因此需要Redis集群化来解决这些问题：

* 数据丢失问题：数据持久化
* 并发问题：搭建主从集群，实现读写分离
* 存储能力问题：搭建分片集群，利用插槽机制实现动态扩容
* 故障恢复问题：利用哨兵，实现健康检测和动态恢复

Redis 具有持久化功能，设置以**快照**或**操作日志**的形式将数据持久化到磁盘。Redis 提供了 RDB 和 AOF 两种持久化方式，默认开启的是RDB，如果需要AOF，需要手动修改配置文件进行开启。

* **RDB：**是一种对Redis存在内存中的数据周期性的持久化机制，将内存中的数据以快照的形式硬盘，实质上是fork了一个子进程在执行数据存储，采用的是二进制压缩的存储模式。
* **AOF：**是以文本日志的形式记录Redis的每一个写入、删除请求（查询请求不处理），它是以追加的方式（append-only）写入，没有磁盘寻址的开销，所以写入速度非常快（类似mysql的binlog）。

##### RDB（Redis Database Backup file ）持久化
Redis数据快照，简单来说就是把内存中的所有数据都记录到磁盘中。当Redis实例故障重启后，从磁盘读取**快照文件**，恢复数据。

1. **save命令：**通过在 redis-cli 客户端中执行 save 命令可立即进行一次持久化保存。save 命令在执行期间会**阻塞 redis-server 进程**，直至持久化过程完毕。而在 redis-server 进程阻塞期间，Redis不能处理任何读写请求，无法对外提供服务。线上禁止使用
2. **bgsave命令：**通过在 redis-cli 客户端中执行 bgsave 命令可立即进行一次持久化保存。不同于 save 命 令的是，正如该命令的名称一样，background save，**后台运行 save**。bgsave 命令会使服务器进程 redis-server 会fork一个子进程，由该子进程负责完成保存过程。在子进程进行保存过程中，不会阻塞 redis-server 进程对客户端读写请求的处理。
3. **触发RDB条件：**除以上2个命令手动触发外，Redis会根据设置信息自动调用bgsave命令执行。配置在/etc/redis/redis.conf中，900秒内如果至少有一个key被修改，则执行bgsave，如果是save ""表示禁用RDB。通过 lastsave 命令可以查看最近一次执行持久化的时间，返回一个时间戳。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**bgsave实现原理：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### AOF（Append Only File ）持久化 
与RDB相对的，AOF并不是直接将数据存入磁盘进行持久化保存，而是通过将每一个写命令记录在AOF文件中实现持久化。就很类似于Mysql的Binlog日志，记录的是具体的语句操作。

其刷盘频率通过redis.conf文件进行配置：

```
# 表示每执行一次写命令，立即记录到AOF文件
appendfsync always 
# 写命令执行完先放入AOF缓冲区，然后表示每隔1秒将缓冲区数据写到AOF文件，是默认方案
appendfsync everysec 
# 写命令执行完先放入AOF缓冲区，由操作系统决定何时将缓冲区内容写回磁盘
appendfsync no
```
**实现原理：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### **适用场景及如何选择**
RDB适合做冷备，AOF适合做热备。

在生产环境中，通常是冷备和热备一起上，RDB中bgsave做全量持久化，AOF做增量持久化，在redis重启的时候，使用rdb持久化的文件重新构建内存，再使用aof恢复最近操作数据，从而实现完整的服务到重启之前的状态。

（单独用**RDB**会丢失很多数据，你单独用**AOF**，数据恢复没**RDB**来的快，所以在生产环境中，第一时间用**RDB**恢复，然后**AOF**做数据补全，冷备热备一起上。）

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 主从同步
单点部署的服务无论服务本身设计的多完美，只要服务所在的机器宕掉了，都是白扯。

在要求高可用性的系统设计上，都会遵守一个核心准则：冗余。也就是说某个节点挂掉后，还有其他节点可以继续提供服务。对 存储系统 设计冗余要考虑如何保证 数据的一致性（所有节点的数据要一致）。

如果冗余节点也可以接收写请求，那在数据同步的问题上将变得非常复杂，所以，存储系统的冗余节点一般有两种使用方法，以此保证所有的写请求只发生在一个节点，只要将变更的数据同步到冗余节点即可：

1. 只作为一个数据备份，**不接收任何读写请求**；
2. 采用读写分离模式，冗余节点可以**接收读请求，但不处理写请求**。

Redis 采用** 一主多从** 的方式提供冗余副本，同时主从节点采用 **读写分离方式**，不仅可以保证数据一致性，从节点还可以分担主节点的负载（读请求可以在从节点处理）。

```
#  执行该命令的节点自动成为从节点
replicaof ip port
```
##### 全量同步
主从第一次建立连接时，会执行全量同步，将master节点的所有数据都拷贝给slave节点。

在同步的过程中，需要用到上文提到的RDB文件。通过bgsave生成RDB时，是子进程复制出的数据进行存盘，但如果此时主线程趁此时进行写数据，那这些新的数据会在此时通过repl_baklog记录bgsave期间的所有命令，再发给slave进行补充，保证数据的完整。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**如何知道是第一次建立连接？**

* **Replication Id：**简称replid，是数据集的标记，id一致则说明是同一数据集。每一个master都有唯一的replid，slave则会继承master节点的replid。这个id如果不同，说明是第一次。
* **offset：**偏移量，随着记录在repl_baklog中的数据增多而逐渐增大。slave完成同步时也会记录当前同步的offset。如果slave的offset小于master的offset，说明slave数据落后于master，需要更新。

至此，主从节点已经完成同步，在此之后，主节点会与从节点之间维护一个长连接，用来同步后续主节点的数据操作，即 **基于长连接的命令传播**。

比如网络只是闪断了一下，其实主从节点数据之间的差异可能很小很小，再次执行全量同步固然可以解决数据一致性问题，但是属实有点浪费。所以在 Redis 2.8 以后，主从节点采用 增量同步 的方式来实现同步。

##### 增量同步
当主从的Replication Id相同时，我们可以理解为，此时slave数据集至少是master的子集了。主从数据剩余部分具体相差多少可以通过offset偏移量来进行记录。

repl_baklog中会记录Redis处理过的命令日志及offset，包括master当前的offset，和slave已经拷贝到的offset。每次在第二阶段，master就去发送：从 已经拷贝过的offset开始 到 当前offset的数据，如图所示：

![](/personal-site-mvp/img/doc-placeholder.svg "")
 repl_baklog这个文件是一个固定大小的数组，只不过数组是环形，也就是说角标到达数组末尾后，会再次从0开始读写，这样数组头部的数据就会被覆盖（绿色部分已经同步了，因此master可以直接覆盖也无妨）。但是如果slave宕机过久，导致master把尚未同步的红色部分覆盖了（即，红色超过了一整圈）：例如下图，此时只能全量同步了。 

一般可以用以下方法来预估该值：

**repl_backlog_size **= (主节点写入命令速度 * 操作大小 - 主从节点间网络传输命令速度 * 操作大小) * 2

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 全量同步和增量同步区别
* 全量同步：master将完整内存数据生成RDB，发送RDB到slave。后续命令则记录在repl_baklog，逐个发送给slave。
* 增量同步：slave提交自己的offset到master，master获取repl_baklog中从offset之后的命令给slave

**什么时候执行全量同步：**

slave节点第一次连接master节点时

slave节点断开时间太久，repl_baklog中的offset已经被覆盖时

**什么时候执行增量同步：**

slave节点断开又恢复，并且在repl_baklog中能找到offset时

#### 缓存清理
##### 过期键**清除策略**
Redis对于过期键有三种清除策略：

* **被动删除：**设置一个key过期时间后，当该key过期了，不会马上从内存中删除，当对其 读/写一个已经过期的key时，会触发惰性删除策略，直接删除掉这个过期key；
* **主动删除：**由于惰性删除策略无法保证冷数据被及时删掉，所以Redis会定期主动淘汰一批已过期的key 
* **缓存淘汰策略：**当前已用内存超过maxmemory限定时，触发主动清理策略当REDIS运行在主从模式时，只有主结点才会执行被动和主动这两种过期删除策略，然后把删除操作”del key”同步到从结点。

##### **最大内存淘汰策略**
　当前已用内存超过redis.cnf配置文件中  **# maxmemory <bytes> **限定时，会触发主动清理策略根据自身业务类型，选好redis.cnf配置文件中 **maxmemory-policy (最大内存淘汰策略)**，设置好过期时间。如果不设置最大内存， 当 Redis 内存超出物理内存限制时，内存的数据会开始和磁盘产生频繁的交换 (swap)，会让 Redis 的性能急剧下降。

配置说明：

(1). LRU means Least Recently Used: 最近最少使用

(2). LFU means Least Frequently Used: 最不经常使用（表示按最近的访问频率进行淘汰，它比 LRU 更加精准地表示了一个 key 被访问的热度）

```
# 第一类：检测易失数据（可能会过期的数据集server.db[i].expires ），已设置过期时间的数据集
volatile-lru：挑选最近最少使用的数据淘汰
volatile-lfu：挑选最近使用次数最少的数据淘汰
volatile-ttl：挑选将要过期的数据淘汰
volatile-random：任意选择数据淘汰 
# 第二类：检测全库数据（所有数据集server.db[i].dict ）
allkeys-lru：挑选最近最少使用的数据淘汰
allkeys-lfu：：挑选最近使用次数最少的数据淘汰
allkeys-random：任意选择数据淘汰，相当于随机 
# 第三类：放弃数据驱逐
noeviction：不会剔除任何数据，拒绝所有写入操作并返回客户端错误信息"(error)OOM command not allowed when used memory"，此时Redis只响应读操作。
```
### 2、一些功能
#### 慢查询分析
慢查询日志就是系统在命令执行前后计算每条命令的执行时间，当超过预设阀值，就将这条命令的相关信息（例如：发生时间，耗时，命令的详细信息）记录下来。客户端超时不一定慢查询，但慢查询是客户端超时的一个可能因素。慢查询是一个先进先出的队列，和两个配置相关：slowlog-log-slower-than（阈值）、slowlog-max-len（长度）。

使用config set命令将slowlog-log-slower-than设置为20000微秒，slowlog-max-len设置为1000：

```
config set slowlog-log-slower-than 20000
config set slowlog-max-len 1000
config rewrite
```
如果要Redis将配置持久化到本地配置文件，需要执行config rewrite命令。

```
slowlog get [n]  # 查看慢查询队列
slowlog len  # 获取慢查询队列长度
slowlog reset  # 清空慢查询队列
```
**有什么用：**

如：公司好多项目用这一个redis实例，最近公司发现，redis响应非常慢，通过排查它的 慢查询-->排查出一些慢命令，找到对应的执行项目--->位置，避免再执行这些命令了。

#### Pipeline（流水线）机制
将一批命令，批量打包，在redis服务端批量计算(执行)，然后把结果批量返回。

```
import redis
pool = redis.ConnectionPool(host="10.211.55.4", port=6379)
r = redis.Redis(connection_pool=pool)
# 创建pipeline
pipe = r.pipeline(transaction=True)
# 开启事务
pipe.multi()
pipe.set("name", "lqz")
# 其他代码，可能出异常
pipe.set("role", "nb")
pipe.execute()  # 事务的执行
```
#### 事务与 Lua
[Redis篇：事务和lua脚本的使用](https://zhuanlan.zhihu.com/p/436011931?t=mention&mt=doc&dt=sdk)

#### Bitmaps
位图是一种特殊的散列表。

申请一个大小为1亿、布尔类型（true或者false）的数组。将这1千万个整数作为数组下标，将对应的数组值设置成true。很多语言中提供的布尔类型，大小是1个字节的，并不能节省太多内存空间。实际上，表示true和false，只需要一个二进制位（bit）就可以了。

```
# 操作比特位
set hello big  #放入key为hello 值为big的字符串
getbit hello 0 #取位图的第0个位置，返回0
getbit hello 1 #取位图的第1个位置，返回1 
# 设置比特位
etbit hello 7 1 #把hello的第7个位置设为1 这样，big就变成了cig
# 获取指定字节范围内，有几个1
bitcount key 0 3   # 数字指的是字节
```
**使用场景：**独立用户统计

假设有1亿用户，假设5千万活跃--->统计日活，使用集合大约需要200m，使用bitmap位图大约需要12m内存，如果活跃用户量少，不适合用bitmap。

#### HyperLogLog
基于HyperLogLog算法：极小的空间完成独立数量统计。跟集合很像，但是占的内存空间很小，百万级别独立用户统计，百万条数据只占15k，错误率 0.81%，无法取出单条数据，只能统计个数。

```
# 增加值
pfadd uuids "uuid1" "uuid2" "uuid3" "uuid4"   
# 统计个数
pfcount uuids  
```
使用场景：

* 爬虫去重
* 黑白名单
* 垃圾邮件过滤
* 独立用户统计
    * 有个用户登录，就把用户id放到HyperLogLog中
    * 最后只需要统计一下 个数  就能统计出今天的活跃人数


#### 发布订阅
Redis的订阅功能使用“发布/订阅”模式，即发布者向通道发布消息，订阅者订阅通道并接收发布者发送的消息。当发布者向通道发布消息时，所有订阅该通道的订阅者都能够接收到该消息。

**发布订阅和消息队列的区别：**发布订阅，订阅者都能收到，消息队列有个抢的过程，只有一个抢到。

使用详情见第三部分实际应用2.Pub/Sub构建实时消息系统

#### GEO
GEO（地理信息定位）：存储经纬度，计算两地距离，范围等。geo本质是zset类型。

```
# 存储经纬度
geoadd cities:locations 116.28 39.55 beijing 
geoadd cities:locations 117.12 39.08 tianjin
geoadd cities:locations 114.29 38.02 shijiazhuang
geoadd cities:locations 118.01 39.38 tangshan
geoadd cities:locations 115.29 38.51 baoding

# 计算两个地理位置的距离
geodist cities:locations beijing tianjin km

# 计算北京方圆 150km内的城市
georadiusbymember cities:locations beijing 90 km
```
### 3、知识拓展
#### 缓存与数据库同步策略
#### 分布式锁
#### 关于集群



