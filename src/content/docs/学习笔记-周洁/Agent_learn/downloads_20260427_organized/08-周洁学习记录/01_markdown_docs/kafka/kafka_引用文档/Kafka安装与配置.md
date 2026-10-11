---
title: "Kafka安装与配置"
description: "Kafka安装与配置"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\kafka\\kafka_引用文档\\Kafka安装与配置.md"
---
Kafka安装与配置

### 使用docker安装
安装docker：[Docker安装与配置](../../docker/docker_引用文档/Docker安装与配置.md)

#### 1、下载镜像
拉取zookeeper、kafka镜像

```
docker pull wurstmeister/zookeeper 
docker pull wurstmeister/kafka
```
查看镜像信息

```
docker images
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2、创建容器
##### 1）创建zookeeper容器
```
docker run -d --name zookeeper -p 2181:2181 wurstmeister/zookeeper
```
启动一个名为“zookeeper”的Docker容器，并且映射它的2181端口到本机的2181端口。

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 2）创建kafka容器
```
docker run -d --name kafka -p 9092:9092 --link zookeeper:zookeeper --env KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 --env KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 --env KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 --env KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 wurstmeister/kafka
```
* --name kafka: 设置容器的名字为“kafka”。
* -p 9092:9092: 将容器的9092端口映射到宿主机的9092端口。
* --link zookeeper:zookeeper: 连接到名为“zookeeper”的另一个Docker容器，并且在当前的容器中可以通过zookeeper这个别名来访问它。
* --env KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181: 设置环境变量，指定ZooKeeper的连接字符串，容器名:端口。
* --env KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092: 设置环境变量，指定Kafka的advertised listeners。
* --env KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092: 设置环境变量，指定Kafka的listeners。
* --env KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1: 设置环境变量，指定offsets topic的副本因子。
* wurstmeister/kafka: 使用的Docker镜像名字。

确保在运行这个命令之前ZooKeeper容器已经在运行，并且可以通过zookeeper:2181来访问

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 3）查看容器信息
```
docker ps
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 3、topic操作
##### 生产者端操作（终端1）
进入kafka容器

```
docker exec -it kafka /bin/bash
```
创建topic zjtest

```
kafka-topics.sh --create --topic zjtest --partitions 1 --replication-factor 1 --zookeeper zookeeper:2181
```
（此时另一个终端进行消费者端操作，hold……）

生产消息

```
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic zjtest
```
输入要生产的消息后回车，能看到终端2收到了输入的信息

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 消费者端操作（终端2）
进入kafka容器

```
docker exec -it kafka /bin/bash
```
消费消息

```
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic zjtest --from-beginning
```
会发现随着终端1生产消息，终端2能看到生产者终端1输入的消息

![](/personal-site-mvp/img/doc-placeholder.svg "")
完成验证，安装没问题。


