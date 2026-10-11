---
title: "centos6 yum升级"
description: "centos6 yum升级"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\开发机\\centos6 库&依赖升级记录_引用文档\\centos6 yum升级.md"
---
centos6 yum升级

1. 备份本地yum源

```
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo_bak 
```
 2.获取阿里yum源配置文件

```
 wget -O /etc/yum.repos.d/CentOS-Base.repo  
```
3.清理缓存

```
yum clean all
```
4.更新cache

```
 yum makecache 
```
5.更新yum

```
 yum -y update 
```

