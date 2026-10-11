---
title: "docker 安装常用服务"
description: "docker 安装常用服务"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\docker\\docker 安装常用服务.md"
---
docker 安装常用服务

## 一、docker中创建容器的两种方式
### 交互式方式创建容器
交互式方式创建容器是指在容器内部启动一个交互式会话，类似于在终端中登录到一个虚拟机。可以直接与容器进行交互，并在容器内部执行命令。

```
docker run -it --name <container_name> <image_name> /bin/bash
```
创建成功之后，进入到容器里，进行终端操作，`exit` 退出交互模式，docker容器会停止运行。

![](/personal-site-mvp/img/docs-assets/image_001_26.png "")
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
![](/personal-site-mvp/img/docs-assets/image_002_20.png "")
与容器交互

```
docker exec -it <container_name> /bin/bash
```


## 二、安装常用服务
* **Milvus**

[Milvus安装与配置（及可视化界面attu）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/tczZM1HF3pSKLc?source=137?t=mention&mt=doc&dt=doc)

* **Mysql**

[阡陌 docker 安装mysql](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/5R4PVa85mC9-yx?source=137?t=mention&mt=doc&dt=doc)

* **Redis**

[阡陌 docker 安装redis](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/keDs-w2wMfKaFI?source=137?t=mention&mt=doc&dt=doc)

其他：

[阡陌 docker 安装zookeeper、kafka](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/lSgHMEB2kZJv10?source=137?t=mention&mt=doc&dt=doc)
