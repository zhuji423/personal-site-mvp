---
title: "centos6 库&依赖升级记录"
description: "centos6 库&依赖升级记录"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\开发机\\centos6 库&依赖升级记录.md"
---
centos6 库&依赖升级记录

策略共用机： ssh work@bjyz-sys-rpm3120160421151401-036.bjyz

机子使用centos6，很多库版本较久，升级部分依赖，安装 conda 建立虚拟环境供不同同学使用

### 1、升级部分库&依赖
1、gcc 版本：[Centos6.3 升级 gcc4.4到 gcc5.1](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/ls7c_v8qOsCNr7?t=mention&mt=doc&dt=doc)

2、GLIBC只有12，缺13-17： [/lib64/libc.so.6: version `GLIBC_2.17' not found](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/zm4avuO-Z-gl-t?t=mention&mt=doc&dt=doc)

3、wget版本太低不支持 https：[centos6升级 openssl、wget](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/htQAXJ0oZWX0dz?t=mention&mt=doc&dt=doc)

4、yum centos6版本官方不支持了 换源 更新yum：[centos6 yum升级](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/KvgxmQyLMMNnCL?t=mention&mt=doc&dt=doc)

### 2、conda 安装
在work账户下安装了 anoconda，建立不同虚拟环境达到环境隔离的目的

![](../../assets/Em9fLdxsn3rCSi/image_001.bin "")

