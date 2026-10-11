---
title: "升级 openssl1.1.1"
description: "升级 openssl1.1.1"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\开发机\\centos6 库&依赖升级记录_引用文档\\升级 openssl1.1.1.md"
---
升级 openssl1.1.1

问题：tlsv1 alert protocol version,需要升级openssl、wget

![](../../../../_remote_images/08-周洁学习记录/local_assets/htQAXJ0oZWX0dz/image_001.bin "")
### 一、升级 openssl到1.1.1
1、下载

换个机子下载 https://www.openssl.org/source/openssl-1.1.1q.tar.gz 传到 centos6机子上

2、安装

```
tar -xzf openssl-1.1.1q.tar.gz
cd openssl-1.1.1q
./config --prefix=/usr/local/openssl
./config -t
make
make install
```
3、替换老版本

查看路径\版本

```
which openssl
openssl version
```
查看所需要的动态链接库

```
cd /usr/local
ldd /usr/local/openssl/bin/openssl
```
替换旧的

```
mv /usr/bin/openssl /usr/bin/openssl.old
ln -s /usr/local/openssl/bin/openssl /usr/bin

mv /usr/include/openssl /usr/include/openssl.old
ln -s /usr/local/openssl/include/openssl /usr/include

cd /usr/lib64
mv libssl.so.6 libssl.so.6.old
ln -s /usr/local/openssl/lib/libssl.so libssl.so.6
mv libcrypto.so.6 libcrypto.so.6.old
ln -s /usr/local/openssl/lib/libcrypto.so libcrypto.so.6
```
![](../../../../_remote_images/08-周洁学习记录/local_assets/htQAXJ0oZWX0dz/image_002.bin "")
###  二、升级 wget
直接升级 yum 就可以用了




