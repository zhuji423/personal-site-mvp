---
title: "zookeeper"
description: "zookeeper"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\RPC\\zookeeper.md"
---
zookeeper

### 简介
Zookeeper是Apache Hadoop的子项目，是一个树形的目录服务，支持变更推送，适合作为Dubbo的服务注册中心，工业强度较高，可用于生产环境，并推荐使用。

###### Zookeeper树形目录服务
![](/personal-site-mvp/img/docs-assets/image_001_32.png "")
root层次：dubbo是根节点；

service层次：service就是服务节点；【包括监控服务】

type层次：服务提供方和消费方；

URL层次：记录服务提供方的ip端口号等；

###### 流程说明
* 服务提供者provider启动时，向/dubbo/com.foo.BarService/providers目录下写入自己的URL地址；
* 服务消费者consumer启动时，订阅/dubbo/com.foo.BarService/providers目录下提供者URL地址。并向着/dubbo/com.foo.BarService/consumer目录下写入URL地址；
* 监控中心Monitor启动时，订阅/dubbo/com.foo.BarService目录下所有提供者和消费者URL

### 安装
[zookeeper安装与配置](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/BEM8oN0B-EamqI?source=137?t=mention&mt=doc&dt=doc)


