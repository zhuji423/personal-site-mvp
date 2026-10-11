---
title: "[什么是deck](http://buildcloud.baidu.com/deck/)"
description: "【墙裂推荐】常用软件安装工具-deck"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🧰【必看】工欲善必先利其器\\📄 【墙裂推荐】常用软件安装工具-deck.md"
---
【墙裂推荐】常用软件安装工具-deck

# [什么是deck](http://buildcloud.baidu.com/deck/)
> * deck 是一款面向百度开发、测试环境的软件部署器，支持一键部署常用的开发软件，支持CENTOS4U3，CENTOS6U3，CENTOS7U5，CENTOS7U6等公司内部使用的主流操作系统。
> * deck的设计理念与yum, apt-get类似，均为二进制分发部署，该方式部署简单快速；不同点在于deck 支持同时部署一个软件的多个版本，每个版本同时兼容多个OS。
> 
> **详见 **[http://buildcloud.baidu.com/deck/](http://buildcloud.baidu.com/deck/)


**nodejs、go、python、git...等各种常用软件包，一行命令+几秒钟就可以完成安装**

# 安装Deck
> bash -c "$( curl -s -L -k https://bcloud-baseenv-bj.bj.bcebos.com/BaseEnv/etc/install_deck.sh )"


# 查找软件
* deck search xxxx

```
[root@xxxxxxx workspace]# deck search python
python-2.7.18 2.7.18-4
    A high-level scripting language
python-3.10.10 3.10.10-4
    A high-level scripting language
python-3.11.2 3.11.2-4
    A high-level scripting language
python-3.12.0 3.12.0-3 [installed 3.12.0-3]
    A high-level scripting language
python-3.13.0 3.13.0-4
    A high-level scripting language
python-3.14.2 3.14.2-2
    A high-level scripting language
python-3.8.16 3.8.16-5
    A high-level scripting language
python-3.9.16 3.9.16-4
    A high-level scripting language
```


# 安装软件
* deck install xxxx

```
[root@xxxxx workspace]# deck install python-3.13.0
==> Calculating dependencies....
==> Packages to be installed:
  -> python-3.13.0
==> Start installation of package python-3.13.0
  -> Downloading files for package...
  -> Downloading file https://bcloud-baseenv-bj.bj.bcebos.com/BaseEnv/artifacts/2.0/x86_64/python/3.13.0/python-3.13.0-4.tar.gz...
######################################################################## 100.0%
  -> Installing...   
  -> Calculating files...
  -> Running hook deck_post_install
==> Installation of python-3.13.0 done!
==> Installation done.
```


# 查看已安装的软件
* deck list

```
[root@xxxx workspace]# deck list
common 1.0.0-6 [installed] [using]
    A collection of base Libraries
extra 1.0.0-1 [installed] [using]
    A collection of base libraries (extra)
git-2.32.0 2.32.0-1 [installed]
    the fast distributed version control system, support git-lfs
jdk-1.8.0 1.8.0-1 [installed]
    OpenJDK Java development kit
maven-3.8.6 3.8.6-1 [installed]
    Java project management and project comprehension tool
nodejs-24.4.1 24.4.1-1 [installed]
    Evented I/O for V8 javascript
python-3.12.0 3.12.0-3 [installed]
    A high-level scripting language
python-3.13.0 3.13.0-4 [installed]
    A high-level scripting language
```
# 卸载软件
* deck remove xxx

```
[root@xxxxx workspace]# deck remove python-3.13.0
==> Start removal of package python-3.13.0
  -> Removing...
==> Package python-3.13.0 removed!
==> Done.
```

