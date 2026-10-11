---
title: "centos6 库&依赖升级记录"
description: "centos6 库&依赖升级记录"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\开发机\\centos6 库&依赖升级记录.md"
---
centos6 库&依赖升级记录

策略共用机： ssh work@bjyz-sys-rpm3120160421151401-036.bjyz

机子使用centos6，很多库版本较久，升级部分依赖，安装 conda 建立虚拟环境供不同同学使用

### 1、升级部分库&依赖
1、gcc 版本：[Centos6.3 升级 gcc4.4到 gcc5.1](./centos6 库&依赖升级记录_引用文档/Centos6.3 升级 gcc4.4到 gcc5.1.md)

2、GLIBC只有12，缺13-17： [/lib64/libc.so.6: version `GLIBC_2.17' not found](./centos6 库&依赖升级记录_引用文档/lib64libc.so.6 version `GLIBC_2.17' not found.md)

3、wget版本太低不支持 https：[centos6升级 openssl、wget](./centos6 库&依赖升级记录_引用文档/升级 openssl1.1.1.md)

4、yum centos6版本官方不支持了 换源 更新yum：[centos6 yum升级](./centos6 库&依赖升级记录_引用文档/centos6 yum升级.md)

### 2、conda 安装
在work账户下安装了 anoconda，建立不同虚拟环境达到环境隔离的目的

![](../../../_remote_images/08-周洁学习记录/local_assets/Em9fLdxsn3rCSi/image_001.bin "")

