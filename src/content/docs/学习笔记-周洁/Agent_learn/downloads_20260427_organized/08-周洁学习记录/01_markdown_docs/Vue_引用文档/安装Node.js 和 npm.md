---
title: "安装Node.js 和 npm"
description: "安装Node.js 和 npm"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Vue_引用文档\\安装Node.js 和 npm.md"
---
安装Node.js 和 npm

### 1、mac
可以使用安装包或brew脚本两种安装方式

#### 安装包安装
[https://nodejs.org/zh-cn/download/prebuilt-installer](https://nodejs.org/zh-cn/download/prebuilt-installer)

![](/personal-site-mvp/img/doc-placeholder.svg "")
下载后安装

#### 验证完成
通过以下命令验证 Node.js 和 npm（Node 包管理器）已成功安装：

```
node -v
npm -v
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 2、其他安装方式
[https://nodejs.org/zh-cn/download/package-manager](https://nodejs.org/zh-cn/download/package-manager)

选择版本+系统+安装方式：

![](/personal-site-mvp/img/doc-placeholder.svg "")
执行对应的命令

### 遇到的问题
#### 1、Error: You are using macOS 11. We (and Apple) do not provide support for this old version.
![](/personal-site-mvp/img/doc-placeholder.svg "")
执行

```
xcode-select --install
```
#### 2、xcode-select: error: command line tools are already installed, use "Software Update" to install updates
执行

```
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install
```
会跳出弹窗，点同意，慢慢装就好了
