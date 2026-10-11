---
title: "阡陌 docker 安装redis"
description: "阡陌 docker 安装redis"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\docker 安装常用服务_引用文档\\阡陌 docker 安装redis.md"
---
阡陌 docker 安装redis

### 1、下载配置文件
创建自己的redis目录，如~/Tool/redis，并新建文件夹conf、data。在conf中下载配置文件：[redis.conf](http://download.redis.io/redis-stable/redis.conf)

```
cd conf/
wget http://download.redis.io/redis-stable/redis.conf
```
### 2、启动redis容器实例
```
docker run -p 8887:6379 --name redis -v ~/Tool/redis/data:/data -v ~/Tool/redis/conf:/etc/redis/redis.conf -d redis:6.0.6 redis-server /etc/redis/redis.conf --appendonly yes --requirepass 123456
```
密码设定的123456，服务端口为8887。

运行后查看状态：

![](/personal-site-mvp/img/doc-placeholder.svg "")
查看redis版本

```
docker exec -it redis redis-server -v
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
登录数据库

```
docker exec -it redis redis-cli
```
直接操作会报错(error) NOAUTH Authentication required. 需要输入'auth 密码'

![](/personal-site-mvp/img/doc-placeholder.svg "")
退出exit，执行后容器仍在运行

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 3、本机远程连接
```
redis-cli -h [ip] -p [端口]
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
在mac上连没问题

### 4、修改密码
Redis本身并没有普通账号权限的概念，所有的连接都是通过密码进行认证的。

在Redis中，修改密码通常涉及两种情况：一种是修改配置文件中的密码，另一种是在运行时通过命令动态修改。

1. 修改配置文件中的密码：

Redis的配置文件`redis.conf`。在配置文件中找到`requirepass`指令，如果它已经被设置了，可以直接修改这个值来更改密码。如果没有设置，可以在`redis.conf`文件中添加或修改以下行：

```
requirepass 密码
```
然后，重启Redis服务以使更改生效。

2. 运行时动态修改密码：

如果想在不重启Redis服务的情况下更改密码，可以使用`CONFIG SET`命令。

```
CONFIG SET requirepass "密码"
```
注意，使用`CONFIG SET`修改密码不会更改配置文件中的密码，它只会影响当前运行的Redis实例。重启后，将会恢复为配置文件中的密码设置。

### 可能遇到的问题
1、启动失败

![](/personal-site-mvp/img/doc-placeholder.svg "")
机子太旧最新版本不支持，别用redis:latest了，换成6.0或者5.0






