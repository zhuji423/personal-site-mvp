---
title: "Centos6.3 升级 gcc4.4到 gcc5.1"
description: "Centos6.3 升级 gcc4.4到 gcc5.1"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\开发机\\centos6 库&依赖升级记录_引用文档\\Centos6.3 升级 gcc4.4到 gcc5.1.md"
---
Centos6.3 升级 gcc4.4到 gcc5.1

1、当前版本

Centos版本

```
cat /etc/issue
```
gcc 版本

```
gcc --version
```
![](../../../../_remote_images/08-周洁学习记录/local_assets/ls7c_v8qOsCNr7/image_001.bin "")
2、下载gcc安装包

（1）去[中科大开源的gcc镜像列表](http://mirrors.ustc.edu.cn/gnu/gcc/)中查找需要的版本，在root下执行

```

```
（2）解压

```
tar xvf gcc-5.1.0.tar.bz2 -C /usr/local/src
```
将其解压到指定目录/usr/local/src下

```
cd /usr/local/src/gcc-5.1.0
```
（3）安装依赖

```
./contrib/download_prerequisites
```
3、编译 gcc

```
./configure --prefix=/usr/local/gcc-5.1.0 --disable-multilib --enable-languages=c,c++,java
make  
make install
```
执行make命令这一过程耗费的时间非常多

重启后查看 gcc 版本
