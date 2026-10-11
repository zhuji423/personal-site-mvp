---
title: "阡陌 docker 安装zookeeper、kafka"
description: "阡陌 docker 安装zookeeper、kafka"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\docker 安装常用服务_引用文档\\阡陌 docker 安装zookeeper、kafka.md"
---
阡陌 docker 安装zookeeper、kafka

### 1、下载镜像
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
docker run -d --name zookeeper -p 8888:2181 wurstmeister/zookeeper
```
启动一个名为“zookeeper”的Docker容器，并且映射它的2181端口到本机的8888端口。

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 2）创建kafka容器
```
docker run -d --name kafka -p 8889:9092 --link zookeeper:zookeeper --env KAFKA_ZOOKEEPER_CONNECT=zookeeper:8888 --env KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:8889 --env KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 --env KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 wurstmeister/kafka
```
* --name kafka: 设置容器的名字为“kafka”。
* -p 8889:9092: 将容器的9092端口映射到宿主机的8889端口。
* --link zookeeper:zookeeper: 连接到名为“zookeeper”的另一个Docker容器，并且在当前的容器中可以通过zookeeper这个别名来访问它。
* --env KAFKA_ZOOKEEPER_CONNECT=zookeeper:8888: 设置了Kafka的ZooKeeper连接地址，以便Kafka能够与ZooKeeper协调器进行通信。
* --env KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:8889: 设置了Kafka容器要公开的监听地址和端口。
* --env KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092: 设置了Kafka的监听器。它允许Kafka容器接受来自任何主机的连接，0.0.0.0表示所有可用的网络接口。
* --env KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1: 设置环境变量，指定offsets topic的副本因子。
* wurstmeister/kafka: 使用的Docker镜像名字。

确保在运行这个命令之前ZooKeeper容器已经在运行，并且可以通过zookeeper:2181来访问

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 3）查看容器信息
```
docker ps
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 3、设置权限
#### 4、使用

