---
title: "ubuntu16开发机mysql应用"
description: "ubuntu16开发机mysql应用"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\数据库\\ubuntu16开发机mysql应用.md"
---
ubuntu16开发机mysql应用

### 1、安装
```
sudo apt-get install mysql-server
```
输入两次初始密码

```
sudo apt install mysql-client
```
```
sudo apt install libmysqlclient-dev
```
查看版本信息

```
mysql -V
```
### 2、登录
```
mysql -u root -p
```
输入密码

![](../../assets/3tqYdtaRl7YodO/image_001.bin "")
退出mysql服务

```
exit
```
修改密码

```
use mysql;
update user set authentication_string='' where user='123456';
```
创建数据库robot-talk并查看

```
create database robot_talk;
show databases;
```
![](../../assets/3tqYdtaRl7YodO/image_002.bin "")
### 3、设置mysql允许远程访问
```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```
![](../../assets/3tqYdtaRl7YodO/image_003.bin "")
注释掉bind-address = 127.0.0.1

![](../../assets/3tqYdtaRl7YodO/image_004.bin "")
登录 mysql 后，授权(授权给远程任何电脑登录数据库)

mysql5：

```
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '密码' WITH GRANT OPTION;
```
mysql8：

```
update user set host = '%' where user ='root';
```
刷新配置信息

```
flush privileges;
```
退出mysql服务后重启mysql

```
service mysql restart
```
### 4、Navicat Premium 验证连接
![](../../assets/3tqYdtaRl7YodO/image_005.bin "")
连接成功

### 注：root密码忘了怎么办
```
sudo vim /etc/mysql/debian.cnf 
```
里面有 debian-sys-maint 的 密码

```
mysql -u debian-sys-maint -p
```
输入密码就登进来了，重新改密码

```
use mysql;
update user set authentication_string='' where user='123456';
```




[mysql常用知识汇总](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/8RjZbDh3rp/-0wwJm-WRVjMzo?t=mention&mt=doc&dt=doc)
