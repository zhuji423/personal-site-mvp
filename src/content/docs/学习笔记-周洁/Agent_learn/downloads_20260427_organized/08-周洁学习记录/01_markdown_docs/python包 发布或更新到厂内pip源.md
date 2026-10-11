---
title: "python包 发布或更新到厂内pip源"
description: "python包 发布或更新到厂内pip源"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\python包 发布或更新到厂内pip源.md"
---
python包 发布或更新到厂内pip源

### 一、发布python包
参考文档：[用户手册](./python包 发布或更新到厂内pip源_引用文档/用户手册.md)

### 二、更新python包
#### 1、更新代码合入
代码更新后，修改setup.cfg中的版本信息

```
version = 0.2.5
```
#### 2、打包发布
合入代码时会检测版本号，若版本增加，会自动触发流水线，进行打包发布

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 3、检查最新版本
在厂内pip源查看该python库最新版本

[http://binary.irepo.baidu-int.com/ui/repos/tree/General/python_local_test/ai-test-generate/0.2.5/ai_test_generate-0.2.5-py2.py3-none-any.whl](http://binary.irepo.baidu-int.com/ui/repos/tree/General/python_local_test/ai-test-generate/0.2.5/ai_test_generate-0.2.5-py2.py3-none-any.whl)

![](/personal-site-mvp/img/doc-placeholder.svg "")
下载后改.whl后缀为.zip 解压缩 检查下有没有奇怪的账号信息被误打包进去的

![](/personal-site-mvp/img/doc-placeholder.svg "")

