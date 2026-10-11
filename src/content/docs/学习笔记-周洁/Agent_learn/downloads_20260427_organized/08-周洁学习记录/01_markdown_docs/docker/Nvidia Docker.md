---
title: "Nvidia Docker"
description: "Nvidia Docker"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\Nvidia Docker.md"
---
Nvidia Docker

### 一、安装
[Nvidia Docker 安装与配置](./docker_引用文档/Nvidia Docker 安装与配置.md)

确保机器上安装了nvidia-device, cuda,cudnn,docker,nvidia-docker

### 二、使用镜像
#### 2.1 方法一：直接拉官方的镜像（非常不建议，看2.2）
```
sudo docker pull nvcr.io/nvidia/pytorch:23.01-py3
```
#### 2.2 方法二：根据基础镜像自己创建torch镜像（推荐）
##### 1、**从Docker Hub下载基础镜像**
进入[dockerhub](https://link.zhihu.com/?target=https%3A//hub.docker.com/)，在搜索框“nvidia/cuda”，第一个50M+download点进去，再点击“Tags”标签，搜索你需要安装的镜像版本，例如“11.8”（尽量保持宿主机的版本和镜像的驱动版本一致），右边有对应的pull指令

```
 docker pull nvidia/cuda:11.8.0-devel-ubuntu22.04
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
之后就是漫长的下载过程~

##### **2、根据镜像创建容器**
```
docker run -it -v ~/shareData:/shareData nvidia/cuda:11.8.0-devel-ubuntu22.04
```
这样就进入了容器，一个容器就相当于是一个进程，是镜像的实例化，里边包含了运行程序所需要的环境和配置环境，例如python，conda，list等等，可以在容器内执行命令，例如查看所安装的包`pip list`

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 3、**在容器内安装所需要的包**
（1）安装python3、pip

```
apt-get update
apt-get install python3
apt-get install python3-pip
```
（2）安装miniconda [阡陌虚拟机安装miniconda](./Nvidia Docker_引用文档/安装miniconda.md)

```
apt-get install wget
 wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
 sh Miniconda3-latest-Linux-x86_64.sh
```
长按回车，按要求输入yes

```
apt update
apt install vim
cd /etc/
vim bash.bashrc
```
将 export PATH=$PATH:/root/miniconda3/bin 放在文件末尾

（3）安装torch[安装GPU版pytorch](./Nvidia Docker_引用文档/安装GPU版pytorch.md)

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
（4）安装其他依赖

以[https://github.com/THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)项目为例

```
pip install -r requirements.txt
```
##### 4、更新镜像
将装好环境的容器打包为新镜像。

```
docker commit -m="update packages" -a="zhoujie19" 容器id ep:chatgml-6b
```
之后就可以直接利用该新镜像创建容器，在容器里跑代码啦~

### **三、使用容器**
shareData 里是hf上的大模型，~/zhoujie19是自己的工作目录

```
sudo docker run --name chatgml-6b-zj --gpus=all --ipc=host --ulimit memlock=-1 -p 6006:6006 -p 8500:8500 -p 8501:8501 -p 8502:8502 -v ~/shareData:/shareData -v ~/zhoujie19:/work  -v /etc/localtime:/etc/localtime:ro -itd ep:chatgml-6b /bin/bash  
```
之后的步骤就是与在本地系统命令行的操作一样

![](/personal-site-mvp/img/doc-placeholder.svg "")


常见报错的解决：[Nvidia Docker 运维](./Nvidia Docker_引用文档/Nvidia Docker 运维.md)


