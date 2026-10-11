---
title: "Milvus安装与配置（及可视化界面attu）"
description: "Milvus安装与配置（及可视化界面attu）"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\docker 安装常用服务_引用文档\\Milvus安装与配置（及可视化界面attu）.md"
---
Milvus安装与配置（及可视化界面attu）

官方文档参考：[https://milvus.io/docs/install_standalone-docker.md](https://milvus.io/docs/install_standalone-docker.md)

需要先安装docker>=19.03，且docker-compose 升级到V2，参考：[Docker安装与配置](../docker_引用文档/Docker安装与配置.md)。

### 1、CPU版本Milvus (单机模式，docker安装)
#### 下载配置文件
新建目录milvus，下载配置文件[milvus-standalone-docker-compose.yml](https://github.com/milvus-io/milvus/releases/download/v2.3.0/milvus-standalone-docker-compose.yml)并重命名为docker-compose.yml

#### 启动Milvus容器
在 docker-compose.yml 同目录执行

```
 sudo docker-compose up -d
```
根据docker-compose.yml拉取镜像并启动容器，-d表示后台执行。

#### **确认 Milvus 运行状态**
```
sudo docker ps -a  # 查看所有容器
```
 可以看到除了milvus standalone服务之外还有两个依赖容器minio、etcd

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 停止Milvus容器
```
sudo docker-compose stop
```
#### 开启Milvus容器
```
sudo docker-compose start
```
#### 停止并删除Milvus容器
```
sudo docker-compose down
```
 删除包括容器和网络。后附加-v 同时删除附加的卷，相当于rm -rf  volumes。

更多详情可参考：[Docker Compose](../Docker Compose.md)

### 2、GPU版本Milvus (单机模式，docker安装)
> Milvus 2.3 正式支持 NVIDIA A100
> Milvus GPU 版本目前仅支持单个 Milvus 进程单个显卡，Milvus GPU 版本默认使用 device 0 显卡。如果需要使用多卡，可以通过启动多个 Milvus 进程或者容器，然后配合 CUDA_VISIBLE_DEVICES 环境变量来实现多卡部署。
安装gpu docker，参考：[Nvidia Docker 安装与配置](../docker_引用文档/Nvidia Docker 安装与配置.md)

#### 下载配置文件
下载配置文件[milvus-standalone-docker-compose-gpu.yml](https://github.com/milvus-io/milvus/releases/download/v2.3.0/milvus-standalone-docker-compose-gpu.yml)并重命名为docker-compose.yml

#### 启动Milvus容器
在 docker-compose.yml 同目录执行

```
 sudo docker-compose up -d
```
#### **确认 Milvus 运行状态**
```
sudo docker ps -a  # 查看所有容器
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 停止Milvus容器
```
sudo docker-compose stop
```
#### 开启Milvus容器
```
sudo docker-compose start
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 停止并删除Milvus容器
```
sudo docker-compose down
```
 删除包括容器和网络。后附加-v 同时删除附加的卷，相当于rm -rf  volumes。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 3、使用 Milvus （milvus python SDK与milvus_cli）
注意：当前的milvus是在虚拟机里面安装的，从虚拟机里面通过ip和端口是可以直接连接milvus的，但是如果想从物理机上连接milvus,需要保证虚拟机和物理机在同一个网段上。

```
sudo docker port milvus-standalone 19530/tcp  # milvus默认19530端口
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
此时milvus服务地址为ip:19530，可以直接访问到milvus。记住{milvus服务地址}后面界面连接也会用到

#### 1）milvus python SDK
参考：[向量数据库](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/tnDu7it7iMHJtP?t=mention&mt=doc&dt=doc)

安装milvus python sdk

```
pip install pymilvus
```
运行程序 python3 hello_milvus.py 连接milvus并创建collections

[附件: hello_milvus.py | 7.2KB | text/x-python-script | fileId=1fa1b653accc412484ba1e7e5d2d5e1d]
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2）milvus_cli (好久不维护了，建议用attu)
安装

```
pip install milvus-cli
```
运行 milvus_cli

```
connect  # 直接连接 带账号密码的是connect -t {username}:{password}
list collections  # 查看collections列表
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 4、可视化界面attu
attu只能部署到本机或直连的物理机，不要部署在需要跳板机的阡陌机子上。milvus没有要求，无论阡陌机子还是直连物理机都是可以的。

简单来说就是attu只是一个通过{milvus服务地址}链接milvus的界面工具，可以不和milvus部署在同一个机子上。

#### 安装 （必须直连，不通过跳板机）
创建attu容器并运行，得到{attu服务地址} 192.168.1.1:3000

```
docker run --network=host --name attu -d zilliz/attu:latest 
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 本机访问界面
在mac上连接attu服务地址  ssh -N -L localhost:{attu服务地址} {attu机器}

```
ssh -N -L localhost:8837:192.168.1.1:3000 star@172.18.12.141
```
浏览器打开localhost:8837

![](/personal-site-mvp/img/doc-placeholder.svg "")


手动填{milvus服务地址}，点击连接

![](/personal-site-mvp/img/doc-placeholder.svg "")
[attu使用指南](https://github.com/zilliztech/attu/blob/main/doc/zh-CN/attu.md)

### 5、修改配置（以设置密码为例子）
官方提供的docker安装milvus默认是没有密码的，但是在项目中为了安全性需要设置密码。

##### 修改配置文件
进入容器当中操作

```
docker exec -it {容器} /bin/bash
```
配置文件在configs/milvus.yaml

编辑milvus.yaml，可以查找关键词authorizationEnabled

改为authorizationEnabled: true后保存，之后登陆需使用默认账号密码root Milvus

![](/personal-site-mvp/img/doc-placeholder.svg "")
ctr+d退出容器，退出后还是运行状态

![](/personal-site-mvp/img/doc-placeholder.svg "")
可以使用以下命令下载配置文件到本机，慢慢查看配置的构成

```
docker cp milvus-standalone:/milvus/configs/milvus.yaml /root/milvus/configs/milvus.yaml
```
##### 重启容器
在 docker-compose.yml 同目录执行

```
sudo docker-compose stop  # 关闭
sudo docker-compose start  # 启动
```
##### 已设置密码，修改登录方式
pysdk:

```
connections.connect(
    host='',
    port='19530',
    user='root',
    password='Milvus',
)
```
attu:

![](/personal-site-mvp/img/doc-placeholder.svg "")
进入attu里可以通过界面修改root密码或者创建新用户

### 6、pass部署
部署依赖的一些环境放在厂内公有服务上：

* 依赖的**kv存储服务**etcd可以放在厂内的潘多拉服务
* 依赖的**对象存储服务**minio可以放在厂内的bos服务
* 其他：消息队列厂内pulsar、组件容器化部署（8个组件）eks



### 7、mac快速部署
1、安装docker 

参考[Docker安装与配置](../docker_引用文档/Docker安装与配置.md)第五部分

2、运行

新建目录milvus，下载配置文件：

[附件: docker-compose.yml | 1.9KB | application/x-yaml | fileId=b76c0c07b3a34ea0b3f7e25ff3aff004]
和官方相比，只是新增了attu容器，都在本地机子的话，不如直接写在同一个compose里就好了

![](/personal-site-mvp/img/doc-placeholder.svg "")
执行：

```
docker-compose up -d
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
3、图形界面

浏览器打开localhost:3000，点击连接

![](/personal-site-mvp/img/doc-placeholder.svg "")



