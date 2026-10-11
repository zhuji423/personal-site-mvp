---
title: "Nvidia Docker 安装与配置"
description: "Nvidia Docker 安装与配置"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\docker_引用文档\\Nvidia Docker 安装与配置.md"
---
Nvidia Docker 安装与配置

### 一、Ubuntu 安装Nvidia Docker
#### 1、安装docker
原生的Docker不支持使用GPU, 而Nvidia-Docker是一个可以使用GPU的docker.

Nvidia-Docker 是在docker上做了一层封装，通过nvidia-docker-plugin，然后调用到docker上，其最终实现的还是在docker的启动命令上携带一些必要的参数。因**此在安装nvidia-docker之前，还是需要安装docker的**。

[Docker安装与配置](./Docker安装与配置.md)

#### 2、环境依赖
```
GNU/Linux x86_64 with kernel version > 3.10
Docker >= 1.12
NVIDIA GPU with Architecture > Fermi (2.1)
NVIDIA drivers ~= 361.93 (untested on older versions)
```
kernel version:  5.19.0

![](/personal-site-mvp/img/doc-placeholder.svg "")
Docker: 24.0.2

![](/personal-site-mvp/img/doc-placeholder.svg "")
CUDA Version: 11.8， NVIDIA-SMI 520.61.05

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 3、卸载已有的nvidia-docker 1.0
```
docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
sudo apt-get purge nvidia-docker
```
#### 4、安装version 2.0
设置稳定版的库源/GPG密钥

```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```
更新

```
sudo apt-get update
```
安装

```
 sudo apt-get install -y nvidia-docker2
```
启动

```
sudo systemctl restart docker
```
试一下能用不

```
sudo docker run --rm --gpus all nvidia/cuda:11.2.0-base-ubuntu18.04 nvidia-smi
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
nvidia-docker与docker操作类似，使用方法参考： [docker](../README.md)



### 二、Centos7 安装Nvidia Docker
#### 1、安装 Docker
[Docker安装与配置](./Docker安装与配置.md)

#### 2、安装 NVIDIA Container Toolkit 
NVIDIA Container Toolkit 允许 Docker 容器使用宿主机的 GPU。

1. 添加 NVIDIA Container Toolkit 的仓库：

```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
```
2. 安装 NVIDIA Container Toolkit：

```
yum install -y nvidia-docker2
```
3. 配置 Docker 以使用 NVIDIA Container Toolkit：

```
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```
验证 NVIDIA Container Toolkit 是否正确安装并配置：

```
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

