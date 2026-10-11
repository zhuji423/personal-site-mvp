---
title: "Redis Stream"
description: "Redis Stream"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\redis\\Redis Stream.md"
---
Redis Stream

### 一、介绍
Redis Stream 是 Redis 5.0 版本新增加的一种专门用来处理`消息队列`场景的高级数据结构。

![](/personal-site-mvp/img/docs-assets/image_001_34.png "")
不管是`list`还是`订阅/发布`模式，都有其弊端，比如list不能友好的重复消费，需要重复消费的话，需要程序代码去控制；而`订阅/发布模式`是一种转发消息的模式，只有订阅者在线的时候才能接收到消息，订阅者不在线期间产生的消息，就丢掉了。而Stream，有借鉴Kafka一些市面上成熟的消息队列的思想，可以消费失败重复消费，消息是持久化的。

Redis流用例的例子包括：

* 事件来源（例如，跟踪用户操作、点击等）
* 传感器监控（例如，现场设备的读数）
* 通知（例如，将每个用户通知的记录存储在单独的流中）

### 二、使用
#### 1、独立消费模式
#####  XADD **创建主题并创建消息**
创建4条消息

```
> XADD race:france * rider Castilla speed 30.2 position 1 location_id 1  # *表示希望服务器生成一个新ID，每个新ID都将单调增加
"1695880260776-0"
> XADD race:france * rider Norem speed 28.8 position 3 location_id 1
"1695880265420-0"
> XADD race:france * rider Prickett speed 29.7 position 2 location_id 1
"1695880269685-0"
> XADD race:france * rider Castilla speed 29.9 position 1 location_id 2
"1695880273970-0"
```
可视化工具查看：

![](/personal-site-mvp/img/docs-assets/image_002_27.png "")
##### XRANGE 按范围查询消息
```
> XRANGE race:france 1695876533688-0 + COUNT 2 # 读取从ID 1695876533688-0开始的两个流条目
> XRANGE race:france - +  # 两个特殊ID-和+分别意味着尽可能最小和最大的ID
> XLEN race:france  # 数据条数
(integer) 4
> XREVRANGE race:france + - COUNT 1  # 取最后一条
1) 1) "1695880273970-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "29.9"
      5) "position"
      6) "1"
      7) "location_id"
      8) "2"
```
##### **XREAD 消费消息**
```
> XREAD COUNT 2 STREAMS race:france 1695880265420-0  # 获取2条id>1695880265420-0的消息
1) 1) "race:france"
   2) 1) 1) "1695880269685-0"
         2) 1) "rider"
            2) "Prickett"
            3) "speed"
            4) "29.7"
            5) "position"
            6) "2"
            7) "location_id"
            8) "1"
      2) 1) "1695880273970-0"
         2) 1) "rider"
            2) "Castilla"
            3) "speed"
            4) "29.9"
            5) "position"
            6) "1"
            7) "location_id"
            8) "2"
```
XRED读消息时分为阻塞和非阻塞模式，使用BLOCK选项可以表示阻塞模式，需要设置阻塞时长。非阻塞模式下，读取完毕（即使没有任何消息）立即返回，而在阻塞模式下，若读取不到内容，则阻塞等待。在阻塞模型中$表示最新的id，非阻塞模型无意义。

```
> XREAD block 1000 STREAMS race:france $  # 1秒内是否有新的消息
(nil)
(1.07s)
> XREAD COUNT 2 block 1000 STREAMS race:france 1695880269685-0
1) 1) "race:france"
   2) 1) 1) "1695880273970-0"
         2) 1) "rider"
            2) "Castilla"
            3) "speed"
            4) "29.9"
            5) "position"
            6) "1"
            7) "location_id"
            8) "2"
```
典型的队列就是 XADD 配合 XREAD Block 完成。XADD负责生成消息，XREAD负责消费消息。

#### **2、消费组模式**
上边讲解的是一个消费者的模式，也是独立消费模式；Redis Stream也支持**消费组模式**，这点是借鉴了kafka的思想。当我们的生产者生产的消息过快，单个消费者的消费处理速度不能满足业务，我们就可以考虑使用消费组模式，来加快消息的处理。

多个消费者配合协作来消费同一个消息队列，比如消息队列中有10条消息，三个消费者分别消费其中的某些消息，比如消费者A消费消息1、2、5、8，消费者B消费消息4、9、10，而消费者C消费消息3、6、7。

![](/personal-site-mvp/img/docs-assets/image_003_23.png "")
##### 创建消息
创建10条消息

```
> XADD testinfo * dataid 1
"1695879616026-0"
> XADD testinfo * dataid 2
"1695879628103-0"
...
> XADD testinfo * dataid 10
"1695880012402-0"
```
可视化工具查看：

![](/personal-site-mvp/img/docs-assets/image_004_16.png "")
##### XGROUP 创建消费组
```
> XGROUP create testinfo consumerGroup 0  # $，只有到达流的新消息才会提供给组中的消费者。0，消费者组将首先消耗流历史记录中的所有消息。 
```
##### XREADGROUP 消息分发给不同消费者消费
依次分配给不同消费者来消费：消费者A消费消息1、2、5、8，消费者B消费消息4、9、10，而消费者C消费消息3、6、7。

可以进行组内消费的基本原理是，STREAM类型会为每个组记录一个**最后处理（交付）的消息ID（last_delivered_id）**，这样在组内消费时，就可以从这个值后面开始读取，保证不重复消费。

```
> XREADGROUP GROUP consumerGroup consumerA COUNT 2 STREAMS testinfo >
1) 1) "testinfo"
   2) 1) 1) "1695879616026-0"
         2) 1) "dataid"
            2) "1"
      2) 1) "1695879628103-0"
         2) 1) "dataid"
            2) "2"
> XREADGROUP GROUP consumerGroup consumerC COUNT 1 STREAMS testinfo >
1) 1) "testinfo"
   2) 1) 1) "1695879631614-0"
         2) 1) "dataid"
            2) "3"
> XREADGROUP GROUP consumerGroup consumerB COUNT 1 STREAMS testinfo >
1) 1) "testinfo"
   2) 1) 1) "1695879634817-0"
         2) 1) "dataid"
            2) "4"
```
##### XACK **消息确认**
分发了4条消息后，对其中一条1695879616026-0进行消息确认。

```
> XACK testinfo consumerGroup 1695879616026-0
(integer) 1
```
使用ack来确认消费，至此，一条消息才算被处理完毕。

##### **XPENDING** 待处理消息
```
> xpending testinfo consumerGroup> xpending testinfo consumerGroup
1) (integer) 3
2) "1695879628103-0"
3) "1695879634817-0"
4) 1) 1) "consumerA"
      2) "1"
   2) 1) "consumerB"
      2) "1"
   3) 1) "consumerC"
      2) "1"
```
表示分发的消息还有3条未确认，id范围为1695879628103-0至1695879634817-0，3个消费者各有1条未确认。

查看各已分发但未确认的消息：

```
> xpending testinfo consumerGroup - + 10
1) 1) "1695879628103-0"  # 消息id
   2) "consumerA"  # 消费者id
   3) (integer) 933111  # 未处理时常
   4) (integer) 1  # 被读取次数
2) 1) "1695879631614-0"
   2) "consumerC"
   3) (integer) 878712
   4) (integer) 1
3) 1) "1695879634817-0"
   2) "consumerB"
   3) (integer) 842116
   4) (integer) 1
```
##### XCLAIM **消息转移**
若某个消费者宕机之后，没有办法再上线了，那么就需要将该消费者Pending的消息，转移给其他的消费者处理，就是消息转移。

```
> XCLAIM testinfo consumerGroup consumerB 60000 1695879628103-0
1) 1) "1695879628103-0"
   2) 1) "dataid"
      2) "2"
```
1分钟不处理消息后，consumerB将认领1695879628103-0。

```
> xpending testinfo consumerGroup - + 10
1) 1) "1695879628103-0"
   2) "consumerB"
   3) (integer) 5234
   4) (integer) 2
2) 1) "1695879631614-0"
   2) "consumerC"
   3) (integer) 1178082
   4) (integer) 1
3) 1) "1695879634817-0"
   2) "consumerB"
   3) (integer) 1141486
   4) (integer) 1
```
##### **删除坏消息**
如果某个消息，不能被消费者处理，也就是不能被XACK，这是要长时间处于Pending列表中，即使被反复的转移给各个消费者也是如此。

此时该消息的被读取次数就会累加（上一节的例子可以看到），当累加到预设的临界值时，就认为是坏消息（也叫死信，DeadLetter，无法投递的消息）。

```
> XDEL testinfo 1695879628103-0
(integer) 1
> XACK testinfo consumerGroup 1695879628103-0  # 删除死信后需要ack确认
(integer) 1
> xpending testinfo consumerGroup - + 10
1) 1) "1695879631614-0"
   2) "consumerC"
   3) (integer) 1480328
   4) (integer) 1
2) 1) "1695879634817-0"
   2) "consumerB"
   3) (integer) 1443732
   4) (integer) 1
```
### 三、常用命令
**消息队列相关命令：**

* **XADD** - 添加消息到末尾
* XTRIM - 对流进行修剪，限制长度
* **XDEL **- 删除消息
* **XLEN** - 获取流包含的元素数量，即消息长度
* **XRANGE** - 获取消息列表，会自动过滤已经删除的消息 
* XREVRANGE - 反向获取消息列表，ID 从大到小
* **XREAD** - 以阻塞或非阻塞方式获取消息列表

**消费者组相关命令：**

* **XGROUP CREATE** - 创建消费者组
* **XREADGROUP GROUP** - 读取消费者组中的消息
* **XACK **- 将消息标记为"已处理"
* XGROUP SETID - 为消费者组设置新的最后递送消息ID
* XGROUP DELCONSUMER - 删除消费者
* XGROUP DESTROY - 删除消费者组
* **XPENDING** - 显示待处理消息的相关信息
* **XCLAIM** - 转移消息的归属权
* XINFO - 查看流和消费者组的相关信息；
* XINFO GROUPS - 打印消费者组的信息；
* XINFO STREAM - 打印流信息


