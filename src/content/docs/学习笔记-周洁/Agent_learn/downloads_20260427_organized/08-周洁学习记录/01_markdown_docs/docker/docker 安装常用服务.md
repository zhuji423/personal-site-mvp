---
title: "docker 安装常用服务"
description: "docker 安装常用服务"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\docker 安装常用服务.md"
---
docker 安装常用服务

## 一、docker中创建容器的两种方式
### 交互式方式创建容器
交互式方式创建容器是指在容器内部启动一个交互式会话，类似于在终端中登录到一个虚拟机。可以直接与容器进行交互，并在容器内部执行命令。

```
docker run -it --name <container_name> <image_name> /bin/bash
```
创建成功之后，进入到容器里，进行终端操作，`exit` 退出交互模式，docker容器会停止运行。

![](/personal-site-mvp/img/doc-placeholder.svg "")
启动容器

```
docker start <container_name>
```
与容器交互

```
docker exec -it <container_name> /bin/bash
```


### 守护式方式创建容器
守护式方式创建容器是指在后台运行容器，无需进入容器内部进行交互。这种方式适用于长期运行的服务或应用程序。

```
docker run -id --name=mycentos4 centos:7
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
与容器交互

```
docker exec -it <container_name> /bin/bash
```


## 二、安装常用服务
* **Milvus**

[Milvus安装与配置（及可视化界面attu）](./docker 安装常用服务_引用文档/Milvus安装与配置（及可视化界面attu）.md)

* **Mysql**

[阡陌 docker 安装mysql](./docker 安装常用服务_引用文档/阡陌 docker 安装mysql.md)

* **Redis**

[阡陌 docker 安装redis](./docker 安装常用服务_引用文档/阡陌 docker 安装redis.md)

其他：

[阡陌 docker 安装zookeeper、kafka](./docker 安装常用服务_引用文档/阡陌 docker 安装zookeeper、kafka.md)
