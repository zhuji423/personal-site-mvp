---
title: "redis安装与配置"
description: "redis安装与配置"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\redis\\redis_引用文档\\redis安装与配置.md"
---
redis安装与配置

### 一、Ubuntu 安装 redis 
#### 1.1 安装 redis
Ubuntu 16.04 默认源中的 Redis 版本是3.0版本，不是最新版，要安装5.0以上版本看第二部分

1、使用apt-get安装

```
apt-get install redis-server
```
2、安装完后查看redis状态

```
service redis status 
```
 running说明安装完成后已经自动启动了服务

![](/personal-site-mvp/img/doc-placeholder.svg "")
3、查看配置文件地址

```
whereis redis
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
配置文件地址为/etc/redis

#### 1.2 配置 redis
1、远程连接

通过netstat -talnp查看，6379只运行本地访问。默认情况下，Redis服务器不允许远程访问，只允许本机访问，所以需要设置打开远程访问的功能。

![](/personal-site-mvp/img/doc-placeholder.svg "")
在redis配置文件（/etc/redis/redis.conf）中注释bind 127.0.0.1这行

![](/personal-site-mvp/img/doc-placeholder.svg "")
2、 修改密码

找到#   requirepass foobared这一行，将注释符号#去掉，将后面修改成自己的密码，如zj1113

![](/personal-site-mvp/img/doc-placeholder.svg "")
3、重启服务

```
/etc/init.d/redis-server restart
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
```
/etc/init.d/redis-server start     #启动
/etc/init.d/redis-server stop      #关闭
/etc/init.d/redis-server restart   #重启
```
#### 1.3 连接 redis
Redis提供了一个命令行界面（CLI）可以用来连接Redis服务器。

1) 如果Redis安装在本地

```
redis-cli
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
2) 如果Redis未安装在本地

需要提供服务器的IP地址和端口号，例如：

```
redis-cli -h 10.24.5.81 -p 6379
```
### 二、Ubuntu redis 升级至5.0
Ubuntu 16.04 默认源中的 Redis 版本是3.0版本不是最新版，可以用镜像源ppa方式安装5.0以上版本

```
apt-get install software-properties-common -y
add-apt-repository ppa:chris-lea/redis-server -y  # 添加源
apt-get update && sudo apt-get install redis-server -y  # 安装
redis-server -v
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
卸载：

```
apt-get remove redis-server
rm /etc/redis/redis.conf
rm -rf /var/lib/redis/
```
### 三、Mac 安装 redis
1、安装

```
brew install redis
```
2、启动\关闭客户端

```
brew services start redis  # 启动
brew services info redis  # 查看信息
brew services stop redi  # 关闭
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 四、docker 安装 redis
[阡陌 docker 安装redis](../../docker/docker 安装常用服务_引用文档/阡陌 docker 安装redis.md)

### 



