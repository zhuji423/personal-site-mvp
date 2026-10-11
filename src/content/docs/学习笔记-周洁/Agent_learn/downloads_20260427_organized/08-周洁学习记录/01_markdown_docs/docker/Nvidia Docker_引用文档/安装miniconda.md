---
title: "安装miniconda"
description: "安装miniconda"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\Nvidia Docker_引用文档\\安装miniconda.md"
---
安装miniconda

### **对于pip、conda、anaconda和miniconda的区别**
* conda是一个包和环境管理工具，它不仅能管理包，还能隔离和管理不同python版本的环境。类似管理nodejs环境的nvm工具。
* anaconda和miniconda都是conda的一种发行版。只是包含的包不同。
* anaconda包含了conda、python等180多个科学包及其依赖项，体格比较大。但很多东西你未必用到，所以才有mini版。
* miniconda是最小的conda安装环境，只有conda+python+pip+zlib和一些其他常用的包，体格非常迷你。
* pip也叫包管理器，和conda的区别是，pip只管理python的包，而conda可以安装所有语言的包。而且conda可以管理python环境，pip不行。

注意：miniconda所有的操作命令皆在命令行中完成，没有GUI界面。而anaconda是有界面的。

### 安装
官网：[Miniconda — Conda documentation](https://docs.conda.io/en/latest/miniconda.html)

找到对应系统、Python版本下载

#### linux安装
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
#后续根据提示选择安装路径或添加到环境变量即可
```
一直回车，输入2次yes

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
第二次yes如果忘了输直接回车选了默认的不修改环境变量，就重新运行

```
 sh Miniconda3-latest-Linux-x86_64.sh -u  # 加-u表示覆盖已安装的
```
这次别忘了根据提示输2次yes

刚安装完需要重启下终端，这时conda命令就能用了

![](/personal-site-mvp/img/doc-placeholder.svg "")
安装后修改源，下载速度大幅提升：[修改conda源、pip源](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/kZvpzgCdEZtlxn?t=mention&mt=doc&dt=doc)


