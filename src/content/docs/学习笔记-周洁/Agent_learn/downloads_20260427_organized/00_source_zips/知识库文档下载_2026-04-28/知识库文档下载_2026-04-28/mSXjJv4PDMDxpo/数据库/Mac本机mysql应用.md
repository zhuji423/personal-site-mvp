---
title: "Mac本机mysql应用"
description: "Mac本机mysql应用"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\数据库\\Mac本机mysql应用.md"
---
Mac本机mysql应用

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 
## 1、安装mysql
下载 [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/) ，选择dmg文件下载。选择不登录,直接下载即可。

下载完成后双击打开。

![](../../assets/56Q5-DVq3WxEuZ/image_001.bin "")
一路确定。

## 2、开启MySQL服务
进入系统偏好设置，点击MySQL

![](../../assets/56Q5-DVq3WxEuZ/image_002.bin "")
显示

![](../../assets/56Q5-DVq3WxEuZ/image_003.bin "")
原因：Mac版本10.14.6，mysql版本8.0.25，mac版本与mysql不兼容

解决：换回mysql版本5.7.30，[https://downloads.mysql.com/archives/community/](https://downloads.mysql.com/archives/community/) ，下载安装包

![](../../assets/56Q5-DVq3WxEuZ/image_004.bin "")
卸载已有的：

```
(base) appledeMacBook-Pro:~ zhoujie19$ cd ~
(base) appledeMacBook-Pro:~ zhoujie19$ open /usr
(base) appledeMacBook-Pro:~ zhoujie19$ sudo rm /usr/local/mysql
Password:
(base) appledeMacBook-Pro:~ zhoujie19$ sudo rm -rf /usr/local/mysql*
(base) appledeMacBook-Pro:~ zhoujie19$ sudo rm -rf /Library/StartupItems/MySQLCOM
(base) appledeMacBook-Pro:~ zhoujie19$ sudo rm -rf /Library/PreferencePanes/My*
(base) appledeMacBook-Pro:~ zhoujie19$ rm -rf ~/Library/PreferencePanes/My*
(base) appledeMacBook-Pro:~ zhoujie19$ sudo rm -rf /Library/Receipts/mysql*
(base) appledeMacBook-Pro:~ zhoujie19$ sudo rm -rf /Library/Receipts/MySQL*
(base) appledeMacBook-Pro:~ zhoujie19$ sudo rm -rf /var/db/receipts/com.mysql.*
```
![](../../assets/56Q5-DVq3WxEuZ/image_005.bin "")
此时，系统偏好设置里mysql图标消失

重新安装mysql版本5.7.30

一路确定，区别在于当弹出一个MYSQL Installer提示框的时候一定打开备忘录复制粘贴记下弹出框的密码。

![](../../assets/56Q5-DVq3WxEuZ/image_006.bin "")
进入系统偏好设置，点击MySQL

![](../../assets/56Q5-DVq3WxEuZ/image_007.bin "")
开启MySQL服务，点击按钮

![](../../assets/56Q5-DVq3WxEuZ/image_008.bin "")
打开后界面上红色的部分会变成绿色的running。

![](../../assets/56Q5-DVq3WxEuZ/image_009.bin "")
## 3、配置路径
```
vim ~/.bash_profile
```
加入

```
PATH=$PATH:/usr/local/mysql/bin
```
使配置生效：

```
source ~/.bash_profile
```
## 4、登录并修改密码
```
mysql -u root -p
```
登陆，输入之前保存的密码

![](../../assets/56Q5-DVq3WxEuZ/image_010.bin "")
修改密码

```
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('zhoujie1113');
```
![](../../assets/56Q5-DVq3WxEuZ/image_011.bin "")
## 5、数据库操作
创建数据库ZjtestDatabase并查看

![](../../assets/56Q5-DVq3WxEuZ/image_012.bin "")
使用数据库，新建数据表user并查看数据表

![](../../assets/56Q5-DVq3WxEuZ/image_013.bin "")
插入一条数据并查看

![](../../assets/56Q5-DVq3WxEuZ/image_014.bin "")
## 6、使用Navicat Premium进行数据库管理
安装: [https://blog.csdn.net/qq_42445719/article/details/104115462](https://blog.csdn.net/qq_42445719/article/details/104115462)

Navicat Premium基本使用: [https://www.cnblogs.com/heqiyoujing/p/9374227.html](https://www.cnblogs.com/heqiyoujing/p/9374227.html)
