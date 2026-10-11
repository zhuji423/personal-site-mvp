---
title: "lib64libc.so.6 version `GLIBC_2.17' not found"
description: "/lib64/libc.so.6: version GLIBC2.17' not found"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\开发机\\centos6 库&依赖升级记录_引用文档\\lib64libc.so.6 version `GLIBC_2.17' not found.md"
---
/lib64/libc.so.6: version `GLIBC_2.17' not found

1、下载 glibc-2.17.tar.gz

```
wget http://mirrors.nju.edu.cn/gnu/libc/glibc-2.17.tar.gz
```
其他版本： [http://mirrors.nju.edu.cn/gnu/libc/](http://mirrors.nju.edu.cn/gnu/libc/)

2、解压编译等操作（用 root 全权操作，最后两步用时比较久）

```
tar -zxvf glibc-2.17.tar.gz
cd glibc-2.17
mkdir build
cd build
../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin
make -j 8
make  install
```
3、查看安装结果

```
strings /lib64/libc.so.6 | grep GLIBC
```
![](../../../../_remote_images/08-周洁学习记录/local_assets/zm4avuO-Z-gl-t/image_001.bin "")

