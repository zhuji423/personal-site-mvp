---
title: "Docker"
description: "runc 是一个 Linux 命令行工具，用于根据 OCI容器运行时规范 创建和运行容器。 containerd 是一个守护程序，它管理容器生命周期，提供了在一个节点上执行容器和管理镜像的最小功能集。 Docker架构./kuassets/"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\01_docker_docs\\Docker文档导出_2026-04-27\\Docker教程.md"
---
# Docker

### 一、介绍
#### Docker的主要作用
起到一个"容器"（代码+环境）的作用，解决了软件跨环境迁移导致的版本不兼容等问题。使用沙箱机制，相互之间没有任何接口，且性能开销极低。

#### Docker的架构
**Docker** 使用 `Google` 公司推出的 Go 语言 进行开发实现，基于 `Linux` 内核的 cgroup，namespace，以及 OverlayFS类的 Union FS 等技术，对进程进行封装隔离，属于 操作系统层面的虚拟化技术。由于隔离的进程独立于宿主和其它的隔离的进程，因此也称其为容器。最初实现是基于 LXC，从 `0.7` 版本以后开始去除 `LXC`，转而使用自行开发的 libcontainer，从 `1.11` 版本开始，则进一步演进为使用 runC 和 containerd。

> `runc` 是一个 Linux 命令行工具，用于根据 OCI容器运行时规范 创建和运行容器。
> `containerd` 是一个守护程序，它管理容器生命周期，提供了在一个节点上执行容器和管理镜像的最小功能集。
![Docker架构](/personal-site-mvp/img/doc-placeholder.svg "")

#### **Docker** 和传统虚拟化方式的不同
传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整操作系统，在该系统上再运行所需应用进程；而容器内的应用进程直接运行于宿主的内核，容器内没有自己的内核，而且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便。

|特性|容器|虚拟机|
|-|-|-|
|启动|秒级|分钟级|
|硬盘使用|一般为 `MB`|一般为 `GB`|
|性能|接近原生|弱于|
|系统支持量|单机支持上千个容器|一般几十个|

Docker的优点：

* **更高效的利用系统资源：**容器不需要进行硬件虚拟以及运行完整操作系统等额外开销，Docker 对系统资源的利用率更高。无论是应用执行速度、内存损耗或者文件存储速度，都要比传统虚拟机技术更高效。
* **更快速的启动时间：** Docker 容器应用，由于直接运行于宿主内核，无需启动完整的操作系统，因此可以做到秒级、甚至毫秒级的启动时间，大大节约了开发、测试、部署的时间。
* **一致的运行环境：** Docker 的镜像提供了除内核外完整的运行时环境，确保了应用运行环境一致性。
* **更轻松的迁移：**用户可以很轻易的将在一个平台上运行的应用，迁移到另一个平台上，而不用担心运行环境的变化导致应用无法正常运行的情况。
* **复用更为容易：**Docker使用的分层存储以及镜像的技术，使得应用重复部分的复用更为容易。此外，Docker 团队同各个开源项目团队一起维护了一大批高质量的官方镜像，既可以直接在生产环境使用，又可以作为基础进一步定制，大大的降低了应用服务的镜像制作成本。

#### Docker的构成
##### **镜像（image）**
Docker镜像，相当于一个root文件系统。镜像相当于java中的一个类，是一个模板，一个镜像可以生成多个容器。(镜像是一种轻量级的，可执行的独立软件包，用来打包软件运行环境和基于环境开发的软件，它包含运行某个软件的所需的所有内容，包括代码，运行时，库，环境变量和配置文件。)

**分层存储：**镜像构建时，会一层层构建，前一层是后一层的基础。每一层构建完就不会再发生改变，后一层上的任何改变只发生在自己这一层。比如，删除前一层文件的操作，实际不是真的删除前一层的文件，而是仅在当前层标记为该文件已删除。在最终容器运行的时候，虽然不会看到这个文件，但是实际上该文件会一直跟随镜像。分层存储的特征还使得镜像的复用、定制变的更为容易。甚至可以用之前构建好的镜像作为基础层，然后进一步添加新的层，以定制自己所需的内容，构建新的镜像。

##### **容器（container）**
镜像和容器的关系就像是类与对象的关系一样，镜像是静态的定义，容器是镜像运行时的实体，容器可以被创建，启动，停止，删除，暂停等。（Docker利用容器独立运行一个或一组应用。容器时是镜像创建的运行实例。可以把容器看成一个简易版本的linux的运行环境，包括运行在里面的应用程序。Docker启动是秒级的。容器只保留了内核，把硬件，网络，打印机等不相关的统统去除了，所以运行快。）

##### **仓库（repository）**
仓库可以看成是一个代码控制中心，用来保存镜像。

### 二、安装
****[Docker安装与配置](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/7PuxE-aNhJtAA0?t=mention&mt=doc&dt=doc)

[Nvidia Docker 安装与配置](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/kgred7mOxl40B9?t=mention&mt=doc&dt=doc)

### 三、常用命令
#### 基本命令
```
# 查看镜像
docker images

# 查看所有状态容器
docker ps -a

# 查看docker消耗的资源状态
docker stats

# run 指令  执行①检测本地有没有该镜像（没有的话直接到docker hub上下载) ②create(将镜像创建为容器)+ start将创建好的容器运行起来
docker run hello-world

# 查看docker信息
docker info

# 查看docker版本命令
docker version
```
![Docker版本](/personal-site-mvp/img/doc-placeholder.svg "")
![Docker信息](/personal-site-mvp/img/doc-placeholder.svg "")

#### 镜像操作
```
# 搜索镜像（公共仓库）
docker search centos:7

# 下载镜像
docker pull centos:7
docker pull nginx

# 查看镜像列表
docker images

# 获取镜像信息 格式：docker inspect  镜像ID
docker inspect eb4a57159180

# 添加镜像标签 格式：docker tag 名称:[旧标签] 新名称:[新标签]
docker tag nginx:latest nginx:zj

# 删除镜像 docker rmi是docker rm image的简写
docker rmi nginx:zj

# 批量删除所有镜像 注：docker images -q 可以加载镜像id
docker rmi `docker images -q`

# 批量删除nginx镜像
docker rmi `docker images|grep "nginx"`

# 导出镜像  格式：docker save -o 存储文件名 存储的镜像
docker save -o nginx_v1 nginx:latest
docker save -o centos_v1 centos:7

# 导入镜像，可以异地导入，但是必须要有docker引擎，并且版本不可以差太多 格式：docker load < 存出的文件
docker load < nginx_v1
dokcer load < centos_v1

# 批量把镜像打包成haha.tar压缩包（但修改名称的镜像包打包不了）
docker save $(docker images | grep -v REPOSITORY | awk 'BEGIN{OFS=":";ORS=" "}{print $1,$2}') -o haha.tar
```
![镜像操作1](/personal-site-mvp/img/doc-placeholder.svg "")
![镜像操作2](/personal-site-mvp/img/doc-placeholder.svg "")

#### 容器操作
```
# 查看所有状态容器
docker ps -a

# 创建容器 格式：docker create [选项] 镜像 注：新创建的容器默认处于停止状态，不运行任何程序，需要在其中发起一个进程来启动容器。
# 常用选项：
# -i：让容器的输入保持打开
# -t：让 Docker 分配一个伪终端
docker create -it nginx:latest /bin/bash

# 启动容器 格式：docker start 容器的ID/名称
docker start 98da3509dca9

# 启动容器（一次性执行） 加 -d 选项让 Docker 容器以守护形式在后台运行。并且容器所运行的程序不能结束。
docker run --name web1 -itd nginx:latest /bin/bash
docker run --name test1 centos:7 /usr/bin/bash -c ls /   # 执行后退出
docker run --name web2 -d centos:7 /bin/bash -c "while true;do echo hello;done"  # 执行后不退出，以守护进程方式执行持续性任务

# 查看容器ip地址  格式：docker inspect 容器id
docker inspect fa0b5f062c62

# 进入容器 格式：docker exec -it 容器ID/名称 /bin/bash 注：容器必须先运行
# 方式1：使用run进入，可以使用ctrl+d退出，直接退出终端
docker run -it centos:7 /bin/bash
# 方式2：想永久性进入，退出后还是运行状态，用docker exec
docker exec -it 2484876fddd2 /bin/bash

# 容器导出/导入
# 导出格式：docker export 容器ID/名称 > 文件名
docker export heuristic_montalcini > centos_v1
# 导入格式：cat 文件名 | docker import – 镜像名称:标签  注：导入后会生成镜像，但不会创建容器
docker import centos_v1  centos:v1
cat centos_v1 |docker import - centos:v2

# 删除容器  格式：docker rm [-f] 容器ID/名称
# 不能删除运行状态的容器，只能-f强制删除，或者先停止再删除
docker rm web1
# 基于名称匹配的方式删除
docker rm -f web3
# 删除所有运行状态的容器
docker rm -f `docker ps -q`
# 删除所有容器
docker rm -f `docker ps -aq`
# 有选择性的批量删除 （正则匹配）
docker ps -a | awk ' {print "docker rm "$1}' | bash
```
![容器操作1](/personal-site-mvp/img/doc-placeholder.svg "")
![容器操作2](/personal-site-mvp/img/doc-placeholder.svg "")
![容器操作3](/personal-site-mvp/img/doc-placeholder.svg "")
![容器操作4](/personal-site-mvp/img/doc-placeholder.svg "")
![容器操作5](/personal-site-mvp/img/doc-placeholder.svg "")
![容器操作6](/personal-site-mvp/img/doc-placeholder.svg "")

#### 数据管理
##### 挂在本地目录
```
# 挂在本地目录 宿主机的/data1目录挂载到容器的/data2目录
docker run -it -v ~/data1:/data2 centos:7 /bin/bash
```
![数据挂载1](/personal-site-mvp/img/doc-placeholder.svg "")
![数据挂载2](/personal-site-mvp/img/doc-placeholder.svg "")

##### 数据卷
启动多个容器实例，并且共享同一个数据卷，复用性和扩展性较强

```
# 创建一个自定义容器卷 volumes：默认位于/var/lib/docker/volumes目录中
docker volume create zj-vol
# 查看所有容器卷
docker volume ls
# 查看指定容器卷详情信息
docker volume inspect zj-vol

# 创建使用数据卷的容器
docker run -itd  -v zj-vol:/shareddata centos:7

# 删除数据卷 需要先删掉使用数据卷的容器
docker volume rm zj-vol
```
![数据卷1](/personal-site-mvp/img/doc-placeholder.svg "")
![数据卷2](/personal-site-mvp/img/doc-placeholder.svg "")
![数据卷3](/personal-site-mvp/img/doc-placeholder.svg "")

### 四、进阶操作
#### Docker仓库
待补充

#### Dockerfile
待补充

#### 集群管理与编排
参考：[容器管理](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/mrlSFU0lgFNCxP?source=137?t=mention&mt=doc&dt=doc)

中文教程： [https://yeasy.gitbook.io/docker_practice/](https://yeasy.gitbook.io/docker_practice/)