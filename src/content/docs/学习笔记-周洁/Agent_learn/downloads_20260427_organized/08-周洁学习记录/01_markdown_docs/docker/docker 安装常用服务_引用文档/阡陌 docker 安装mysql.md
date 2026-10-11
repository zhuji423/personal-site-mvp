---
title: "授予数据表之前，首先得有zjtest数据库"
description: "阡陌 docker 安装mysql"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\docker 安装常用服务_引用文档\\阡陌 docker 安装mysql.md"
---
阡陌 docker 安装mysql

### 1、拉取mysql镜像
官网：[https://hub.docker.com/_/mysql/tags](https://hub.docker.com/_/mysql/tags)

```
docker pull mysql:8.3.0
```
### 2、启动mysql容器实例
官网：[https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)

创建mysql目录（以~/Tool/mysql为例），并新建文件夹log、data、conf

```
docker run -p 8886:3306 --name mysql -v ~/Tool/mysql/log:/var/log/mysql -v ~/Tool/mysql/data:/var/lib/mysql -v ~/Tool/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.3.0
```
查看运行状态

```
docker ps
```
查看mysql版本

```
docker exec -it mysql mysql -V
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
root登录数据库

```
docker exec -it mysql mysql -u root -p
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
操作数据库

```
create database zjtest;  # 创建数据库
show databases;  # 查看数据库
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
退出

```
exit
```
执行后容器仍在运行

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 3、本机远程连接
```
docker exec -it mysql mysql -u root -p
```
登录数据库后执行，修改root密码并可远程连接添加远程连接

```
alter user 'root'@'%' identified with mysql_native_password by '密码';
```
刷新权限

```
flush privileges;
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
查看开发机ip

```
ifconfig
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
测试连接

![](/personal-site-mvp/img/doc-placeholder.svg "")
连接成功

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 新增用户并设置可远程连接
root登录后执行

```
create user '账户'@'%' identified by '密码';
flush privileges;
```
###### 报错2059 - Authentication plugin 'caching_sha2_password' cannot be loaded: dlopen(../Frameworks/caching_sha2_password.so, 2): image not found
![](/personal-site-mvp/img/doc-placeholder.svg "")
原因：由于目前已有的客户端连接软件还不支持Mysql8新增加的加密方式：caching_sha2_password，老的加密验证方式：mysql_native_password

解决：登陆root后执行

```
alter user '账户'@'%' identified with mysql_native_password by '密码';
flush privileges;
```
###### 报错1142 - SELECT command denied to user 'work'@'xx.xx.xx.xx' for table 'user'
![](/personal-site-mvp/img/doc-placeholder.svg "")
很多表无法访问到，点击用户报错

![](/personal-site-mvp/img/doc-placeholder.svg "")
原因：work账户没有足够的权限访问数据库表user

解决：授权，登陆root后执行

```
grant all on *.* to '账号'@'%';
flush privileges;
```
关闭连接后重新打开连接，查看用户

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 权限详解
|权限|说明|
|-|-|
|ALL, ALL PRIVILEGES|所有权限|
|SELECT|查询数据|
|INSERT|插入数据|
|UPDATE|修改数据|
|DELETE|删除数据|
|ALTER|修改表|
|DROP|删除数据库/表/视图|
|CREATE|创建数据库/表|

刚创建的账号只有

![](/personal-site-mvp/img/doc-placeholder.svg "")
A、查询用户权限

```
show grants for '账户'@'%';
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
B、授予’账号‘@’%‘，用户对zjtest数据库所有表操作权限  

先使用root登陆，再授权

```
# 授予数据表之前，首先得有zjtest数据库
grant all on zjtest.* to '账号'@'%';
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
只想授予'账号'@'%' 用户查询zjtest数据库所有表的权限，将all一替换为对应的权限：

```
grant SELECT on zjtest.* to '账号'@'%';
```
C、撤销，’账号‘@’%‘，用户对zjtest数据库的所有权限

```
revoke all on zjtest.* from '账号'@'%';
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
D、授予’账号‘@’%‘，用户所有操作权限  

```
grant all on *.* to '账号'@'%';
```

