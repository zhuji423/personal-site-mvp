---
title: "安装containerd.io"
description: "Docker安装与配置"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\docker_引用文档\\Docker安装与配置.md"
---
Docker安装与配置

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 一、安装
### ubuntu 22.04 安装docker
更新系统软件包：

```
sudo apt update
sudo apt upgrade
```
安装所需的依赖包，以允许APT使用HTTPS：

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
添加Docker官方的GPG密钥：

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
添加Docker存储库：

```
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
更新软件包索引：

```
sudo apt update
```
安装Docker引擎：

```
sudo apt install docker-ce docker-ce-cli containerd.io
```
验证Docker是否成功安装并运行：

```
docker version
```


注：过程中遇到这个提示直接回车就行

![](/personal-site-mvp/img/doc-placeholder.svg "")
### ubuntu 16.04 安装docker
旧版本（如ubuntu16）推荐离线安装

#### 1、完全卸载
1、判断当前的Ubantu16.04系统中是否已经安装过curl和docker

![](/personal-site-mvp/img/doc-placeholder.svg "")
2、删除软件以及安装时自动安装的所有包

```
sudo apt-get autoremove docker docker-ce docker-engine  docker.io  containerd runc -y
```
3、查看docker中其他没有卸载的包

```
dpkg -l | grep docker
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
4、卸载没有删除的docker相关插件

```
sudo apt remove --purge docker-ce -y
sudo apt remove --purge docker-ce-cli -y
```
5、删除docker的相关配置&目录

```
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
sudo rm -rf /var/run/docker*
```
6、确认docker卸载完毕

```
which docker
```
#### 2、离线安装
离线安装地址： [https://download.docker.com/linux/ubuntu/dists/xenial/pool/stable/amd64/](https://download.docker.com/linux/ubuntu/dists/xenial/pool/stable/amd64/)

1、下载containerd.io、docker-ce

```
wget https://download.docker.com/linux/ubuntu/dists/xenial/pool/stable/amd64/containerd.io_1.4.6-1_amd64.deb
wget https://download.docker.com/linux/ubuntu/dists/xenial/pool/stable/amd64/docker-ce-cli_20.10.7~3-0~ubuntu-xenial_amd64.deb
wget https://download.docker.com/linux/ubuntu/dists/xenial/pool/stable/amd64/docker-ce_20.10.7~3-0~ubuntu-xenial_amd64.deb
```
2、按顺序安装

```
dpkg -i containerd.io_1.4.6-1_amd64.deb
dpkg -i docker-ce-cli_20.10.7~3-0~ubuntu-xenial_amd64.deb
dpkg -i docker-ce_20.10.7~3-0~ubuntu-xenial_amd64.deb
```
#### 3、安装成功
```
docker --version
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 可能遇到的依赖问题
1、【报错docker-ce-cli依赖】16.04以上的docker-ce最新版本安装时报错：docker-ce depends on docker-ce-cli 

解决：再去其下载目录下载docker-ce-cli进行安装。

2、【报错libseccomp2依赖】Depends: libseccomp2 (>= 2.3.0) but 2.2.3-3ubuntu3 is to be installed Recommends: aufs-tools but it is not going to be installed

```
apt-get install -y libltdl7 libseccomp2
```
3、【报错libsystemd-journal0依赖】docker-ce depends on libltdl7 (>= 2.4.2); however:Package libltdl7 is not installed.docker-ce depends on libsystemd-journal0 (>= 201); however:Package libsystemd-journal0 is not installed.

```
apt-get install -y libltdl7 libsystemd-journal0
```
### Mac 安装Docker
这里因为使用许可的问题，没有用Docker DeskTop，采用的colima+docker方案

[安装Homebrew](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/KoRWp8X1bneN3T?source=137?t=mention&mt=doc&dt=doc)使用brew安装：

```
brew install docker docker-compose colima
```
时间比较久，耐心等待。

安装完成之后，启动colima：

```
colima start
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
启动成功之后，再执行docker命令，就可以看到可以正确执行了

```
docker -v  # 查看版本
docker ps  # 查看容器
docker run -p 8300:3000 --name attu -d zilliz/attu:latest   # 创建容器
```
### CentOS 7 安装 Docker
##### 在线安装
```
sudo yum update -y
```
安装所需的依赖包

```
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```
添加 Docker 的官方仓库

```
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```
安装 Docker CE（社区版）

```
sudo yum install -y docker-ce docker-ce-cli containerd.io
```
安装完成后，启动 Docker 服务并设置为开机自启。

```
sudo systemctl start docker
sudo systemctl enable docker
```
验证安装

```
sudo docker --version
```
运行一个测试容器

```
sudo docker run hello-world
```
##### 离线安装
```
# 安装containerd.io
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.4.6-3.1.el7.x86_64.rpm
yum install -y container-selinux
rpm -i containerd.io-1.4.6-3.1.el7.x86_64.rpm

# 安装docker-ce-cli
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-scan-plugin-0.9.0-3.el7.x86_64.rpm
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-cli-20.10.9-3.el7.x86_64.rpm
rpm -i docker-ce-cli-20.10.9-3.el7.x86_64.rpm docker-scan-plugin-0.9.0-3.el7.x86_64.rpm

# 安装docker-ce
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-rootless-extras-20.10.9-3.el7.x86_64.rpm
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-20.10.9-3.el7.x86_64.rpm
yum install -y fuse-overlayfs slirp4netns
rpm -i docker-ce-20.10.9-3.el7.x86_64.rpm docker-ce-rootless-extras-20.10.9-3.el7.x86_64.rpm

# 验证
docker --version
# Docker version 20.10.9, build c2ea9bc
```
## 二、docker-compose 升级到V2（非必需）
1、查看版本

```
docker-compose --version   
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
若显示未安装，使用apt  install docker-compose先进行安装

2、下载docker-compose V2 的可执行文件： [docker-compose-Linux-x86_64](https://github.com/docker/compose/releases/latest/download/docker-compose-Linux-x86_64)

3、替换原有的

```
mv docker-compose-linux-x86_64 docker-compose
chmod +x docker-compose
whereis docker-compose  # /usr/bin/docker-compose
mv /usr/bin/docker-compose /usr/bin/docker-compose.bak  # 备份一下原有的脚本
mv ./docker-compose /usr/bin/  # 将当前目录的docker-compose拷贝到/usr/bin 目录下
docker-compose --version 
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
使用可参考：[Docker Compose](../Docker Compose.md)

## 三、权限问题
### 1、permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock
sudo docker ps -a 命令正常，但是不加sudo就会报错

![](/personal-site-mvp/img/doc-placeholder.svg "")
1、添加docker group

```
sudo groupadd docker
```
如果docker组已经存在，可能会出现如下提示：groupadd: group ‘docker’ already exists

2、将用户’username’加到docker group中

```
sudo usermod -aG docker {username}
```
-aG：-a在-G存在的情况下，增加次要用户组的支持，而不是修改当前用户组。

3、修改

```
sudo chmod 666 /var/run/docker.sock
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")



