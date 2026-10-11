---
title: "/user/用户名"
description: "HDFS分布式文件系统"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\hadoop\\hadoop_引用文档\\HDFS分布式文件系统.md"
---
HDFS分布式文件系统

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间

分布式文件系统解决的问题就是大数据存储。它们是横跨在多台计算机上的存储系统。分布式文件系统在大数据时代有着广泛的应用前景，它们为存储和处理超大规模数据提供所需的扩展能力。



## HDFS组成
HDFS使用Master和Slave结构对集群进行管理。一般一个 HDFS 集群只有一个 Namenode 和一定数目的Datanode 组成。Namenode 是 HDFS 集群主节点，Datanode 是 HDFS 集群从节点，两种角色各司其职，共同协调完成分布式的文件存储服务。

![](../../../../_remote_images/08-周洁学习记录/local_assets/rdUmKd9ssWYP5c/image_001.bin "")
HDFS集群包括，NameNode和DataNode以及Secondary Namenode。

* NameNode负责管理整个文件系统的元数据，以及每一个路径（文件）所对应的数据块信息。
* DataNode 负责管理用户的文件数据块，每一个数据块都可以在多个datanode上存储多个副本。
* Secondary NameNode用来监控HDFS状态的辅助后台程序，每隔一段时间获取HDFS元数据的快照。最主要作用是辅助namenode管理元数据信息

## HDFS分块存储
hdfs将所有的文件全部抽象成为block块来进行存储，不管文件大小，全部一视同仁都是以block块的统一大小和形式进行存储，方便我们的分布式文件系统对文件的管理

所有的文件都是以block块的方式存放在HDFS文件系统当中，在Hadoop1当中，文件的block块默认大小是64M，Hadoop2当中，文件的block块大小默认是128M，block块的大小可以通过hdfs-site.xml当中的配置文件进行指定

一个文件100M，上传到HDFS占用几个快？一个块128M，剩余的28M怎么办？

数据超过128M，便进行切分，如果没有超过128M，就不用切分，有多少算多少，不足128M的也是一个快。这个快的大小就是100M，没有剩余28M这个概念。

**抽象成数据块的好处**

1.一个文件有可能大于集群中任意一个磁盘20T/128 = xxx块，这些block块属于一个文件 2.使用块抽象而不是文件,可以简化存储子系统。 3.块非常适合用于数据备份进而提供数据容错能力和可用性。

**块缓存：**通常DataNode从磁盘中读取块，但对于访问频繁的文件，其对应的块可能被显示的缓存在DataNode的内存中，以堆外块缓存的形式存在。默认情况下，一个块仅缓存在一个DataNode的内存中，当然可以针对每个文件配置DataNode的数量。作业调度器通过在缓存块的DataNode上运行任务，可以利用块缓存的优势提高读操作的性能。

## HDFS副本机制
HDFS视硬件错误为常态，硬件服务器随时有可能发生故障。 为了容错，文件的所有 block 都会有副本。每个文件的 block 大小和副本系数都是可配置的。应用程序可以指定某个文件的副本数目。副本系数可以在文件创建的时候指定，也可以在之后改变。 数据副本默认保存三个副本，可以更改副本数以提高数据的安全性，在hdfs-site.xml当中修改以下配置属性，即可更改文件的副本数。

Hadoop2.7.2副本节点选择 第一个副本在client所处的节点上。如果客户端在集群外，随机选一个。 第二个副本和第一个副本位于相同机架，随机节点。 第三个副本位于不同机架，随机节点。

![](../../../../_remote_images/08-周洁学习记录/local_assets/rdUmKd9ssWYP5c/image_002.bin "")
## Namenode 功能
* Namenode 负责维护整个hdfs文件系统的目录树结构，以及每一个文件所对应的 block 块信息（block 的id，及所在的datanode 服务器）。
* 确定指定的文件块到具体的Datanode结点的映射关系。在客户端与数据节点之间共享数据。
* 管理Datanode结点的状态报告，包括Datanode结点的健康状态报告和其所在结点上数据块状态报告，以便能够及时处理失效的数据结点。

![](../../../../_remote_images/08-周洁学习记录/local_assets/rdUmKd9ssWYP5c/image_003.bin "")
## Datanode功能
* 文件的各个 block 的具体存储管理由 datanode 节点承担。每一个 block 都可以在多个datanode 上。Datanode 需要定时向 Namenode 汇报自己持有的 block信息。存储多个副本（副本数量也可以通过参数设置dfs.replication，默认是 3）。
* 向Namenode结点报告状态。每个Datanode结点会周期性地向Namenode发送心跳信号和文件块状态报告。心跳是每3秒一次，心跳返回结果带有namenode给该datanode的命令如复制块数据到另一台机器，或删除某个数据块。如果超过10分钟没有收到某个datanode的心跳，则认为该节点不可用。DataNode启动后向namenode注册，通过后，周期性（1小时）的向namenode上报所有的块信息。
* 执行数据的流水线复制。当文件系统客户端从Namenode服务器进程获取到要进行复制的数据块列表后，完成文件块及其块副本的流水线复制。一个数据块在datanode上以文件形式存储在磁盘上，包括两个文件，一个是数据本身，一个是元数据包括数据块的长度，块数据的校验和，以及时间戳。

## hdfs文件系统基本操作
### 新建目录
```
# /user/用户名
$ hadoop fs -mkdir /user/hadoop
```
### 上传文件到分布式文件系统
准备Shakespeare.txt放在本地的默认工作目录，即`/home/hadoop，`默认也会放到远程的工作目录，即 [hdfs://localhost/user/hadoop/](hdfs://localhost/user/hadoop/)

```
# 第1种
$ hadoop fs -copyFromLocal shakespeare.txt shakespeare.txt
# 第2种 表明绝对路径
$ hadoop fs -put /home/hadoop/shakespeare.txt hdfs://localhost/user/hadoop/shakespeare.txt
```
### **查看文件列表**
```
$ hadoop fs -ls <path> #这里是绝对路径，从/user开始
$ hadoop fs -ls .  #查看主目录，即/user/hadoop
```
### 查看文件内容
远程文件可能非常大，不是整个读过来，而是通过less 或者 more，通过管道传输

```
$ hadoop fs -cat shakespeare.txt | less
$ hadoop fs -tail shakespeare.txt | less #查看最后1000个字节
```
### 获取文件到本地
```
$ hadoop fs -get shakespeare.txt ./shakespeare.from-remote.txt
```
### 获取指定路径包含的目录数，文件数，字节数
```
$ hadoop fs -count /user
```
### 获取指定路径使用的空间字节数
```
$ hadoop fs -du -h /user
```
### 修改文件权限
```
$ hadoop fs -chmod 664 shakespeare.txt
```
其他基本上和本地文件操作类似,可以用以下命令查询用法

```
$ hadoop fs help
```
## 设计特点
* 大数据文件
* 文件分块存储：HDFS会将一个完整的大文件平均分块存储到不同计算器上，它的意义在于读取文件时可以从多个主机读取不同区块的文件，多主机读取比单主机读取效率要高得多。
* 硬件故障：HDFS认为所有计算机都可能会出问题，为了防止某个主机失效读取不到该主机的块文件，它将同一个文件块副本分配到其它某几个主机上，如果其中一台主机失效，可以迅速找另一块副本取文件。
* 流式数据访问：HDFS的构建思路是这样的：一次写入，多次读取是最高效的访问模式。每次数据分析都涉及该数据集的大部分数据甚至全部，因此读取整个数据集的时间延迟比读取第一条记录的时间延迟更重要。
* 廉价硬件：Hadoop并不需要运行在昂贵可靠的硬件上，它是设计运行在商用硬件的集群上的。因此对于庞大的集群来说，节点故障的几率还是非常高的。HDFS遇到上述故障时，被设计成能够继续运行且不让用户察觉到明显的中断。
* 低时间延迟的数据访问：要求低时间延迟数据访问的应用，不适合在HDFS上运行。HDFS是为高数据吞吐量应用优化的，这可能会以高时间延迟为代价。
* 大量的小文件：由于namenode将文件系统的元数据存储在内存中，所以因此该文件系统能够存储的文件总数受限于namenode的内存容量

## 优点
* **高吞吐量访问，高效性**：HDFS的每个block分布在不同的rack上，在用户访问时，HDFS会计算使用最近和访问量最小的服务器给用户提供。由于block在不同的rack上都有备份，所以不再是单数据访问，所以速度和效率是非常快的。另外HDFS可以并行从服务器集群中读写，增加了文件读写的访问带宽。
* **高容错性，可靠性**：上面简单的介绍了一下高度容错。系统故障是不可避免的，如何做到故障之后的数据恢复和容错处理是至关重要的。HDFS通过多方面保证数据的可靠性，自动将数据多份复制并且分布到物理位置的不同服务器上，并且能够自动将失败的任务重新分配。数据校验功能、后台的连续自检数据一致性功能，都为高容错提供了可能。
* **容量扩充**：因为HDFS的block信息存放到namenode上，文件的block分布到datanode上，当扩充的时候，仅仅添加datanode数量，系统可以在不停止服务的情况下做扩充，不需要人工干预。分布式存储和分布式计算是在集群节点完成的，所以可以扩展至更过的集群结点。
* **低成本**：hadoop本身是运行在普通PC服务器组成的集群中进行大数据的分发及处理工作的，这些集群是可以支持上千个结点的。


