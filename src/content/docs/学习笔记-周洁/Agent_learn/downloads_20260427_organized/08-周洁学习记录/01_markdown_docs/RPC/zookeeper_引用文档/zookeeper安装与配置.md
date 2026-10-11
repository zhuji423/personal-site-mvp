---
title: "zookeeper安装与配置"
description: "zookeeper安装与配置"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\RPC\\zookeeper_引用文档\\zookeeper安装与配置.md"
---
zookeeper安装与配置

#### 单机环境安装Zookeeper(Linux)
下载Zookeeper，网址是：[https://archive.apache.org/dist/zookeeper](https://archive.apache.org/dist/zookeeper) 

传到开发机上，解压，在zookeeper目录下下建立`log`文件夹和`data`文件夹用于存放日志和数据

```
root@kongdefu:~/Tool# cd zookeeper-3.4.6/
root@kongdefu:~/Tool/zookeeper-3.4.6# ls
bin          dist-maven       LICENSE.txt           src
build.xml    docs             NOTICE.txt            zookeeper-3.4.6.jar
CHANGES.txt  ivysettings.xml  README_packaging.txt  zookeeper-3.4.6.jar.asc
conf         ivy.xml          README.txt            zookeeper-3.4.6.jar.md5
contrib      lib              recipes               zookeeper-3.4.6.jar.sha1
root@kongdefu:~/Tool/zookeeper-3.4.6# mkdir data
root@kongdefu:~/Tool/zookeeper-3.4.6# mkdir log
```
由于Zookeeper运行需要一个zoo.cfg的配置文件，在conf目录下没有conf.xml文件，所以进入`conf`目录，复制一份`zoo_sample.cfg`取名为`zoo.cfg`

```
root@kongdefu:~/Tool/zookeeper-3.4.6# cd conf
root@kongdefu:~/Tool/zookeeper-3.4.6/conf# ls
configuration.xsl  log4j.properties  zoo_sample.cfg
root@kongdefu:~/Tool/zookeeper-3.4.6/conf# cp zoo_sample.cfg zoo.cfg
root@kongdefu:~/Tool/zookeeper-3.4.6/conf# ls
configuration.xsl  log4j.properties  zoo.cfg  zoo_sample.cfg
```
vi zoo.cfg修改配置文件

![](/personal-site-mvp/img/doc-placeholder.svg "")
配置好了后进入bin目录输入 **./zkServer.sh start** 启动zookeeper

![](/personal-site-mvp/img/doc-placeholder.svg "")
**./zkServer.sh stop **关闭zookeeper

**jps**  列出正在运行的虚拟机进程,并显示虚拟机执行主类，启动后**有QuorumPeerMain进程**才算成功启动。

没有QuorumPeerMain进程的原因：你下载使用的zk是未编译的[apache-zookeeper-3.8.0.tar.gz](https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0.tar.gz), 自zk3.5.5版本以后，已编译的jar包，尾部有bin，应该使用的是[apache-zookeeper-3.8.0-bin.tar.gz](https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz)。

没有成功的话，看看 zookeeper-3.4.6/zookeeper.out 或 zookeeper-3.4.6/logs/zookeeper.out 中报错信息

![正确的启动](/personal-site-mvp/img/doc-placeholder.svg "正确的启动")
**./zkCli.sh** 启动成功后连接zookeeper

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 基本的操作命令
1. ls /： 使用 ls 命令来查看当前 ZooKeeper 中所包含的内容

2.  ls2 /： 查看当前节点数据并能看到更新次数等数据

3. 创建文件，并设置初始内容： create /zj "zjzj" 创建一个新的znode节点“ zj ”以及与它关联的字符串"zjzj"

4. 获取文件内容： get /zj 确认新创建的znode节点是否包含我们所创建的"zjzj"字符串

5. 修改文件内容： set /zj "zjzjzj" 对 zj 所关联的字符串"zjzj"进行设置,修改为"zjzjzj"

6. 删除文件： delete /zj 将刚才创建的 znode 删除；rmr /zj 删除节点和他的子节点

7. 退出客户端： quit

8. 帮助命令： help 

```
[zk: localhost:2181(CONNECTED) 6] ls /
[zookeeper]
[zk: localhost:2181(CONNECTED) 7] create /zj "zjzj"
Created /zj
[zk: localhost:2181(CONNECTED) 8] ls /
[zj, zookeeper]
[zk: localhost:2181(CONNECTED) 9] get /zj
"zjzj"
cZxid = 0x4
ctime = Thu Feb 16 10:49:44 CST 2023
mZxid = 0x4
mtime = Thu Feb 16 10:49:44 CST 2023
pZxid = 0x4
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 6
numChildren = 0
[zk: localhost:2181(CONNECTED) 10] set /zj "zjzjzj"
cZxid = 0x4
ctime = Thu Feb 16 10:49:44 CST 2023
mZxid = 0x5
mtime = Thu Feb 16 10:50:23 CST 2023
pZxid = 0x4
cversion = 0
dataVersion = 1
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
[zk: localhost:2181(CONNECTED) 11] get /zj
"zjzjzj"
cZxid = 0x4
ctime = Thu Feb 16 10:49:44 CST 2023
mZxid = 0x5
mtime = Thu Feb 16 10:50:23 CST 2023
pZxid = 0x4
cversion = 0
dataVersion = 1
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 8
numChildren = 0
[zk: localhost:2181(CONNECTED) 12]
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 搭建集群环境Zookeeper
参考：[https://blog.csdn.net/qq_45950109/article/details/115430962](https://blog.csdn.net/qq_45950109/article/details/115430962)


