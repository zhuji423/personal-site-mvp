---
title: "python包 发布或更新到厂内pip源"
description: "python包 发布或更新到厂内pip源"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\python包 发布或更新到厂内pip源.md"
---
python包 发布或更新到厂内pip源

### 一、发布python包
参考文档：[用户手册](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/tjIp17bwPd/CHf1I_vIs4/EN9D1w9QpX-6Xs?t=mention&mt=doc&dt=doc)

### 二、更新python包
#### 1、更新代码合入
代码更新后，修改setup.cfg中的版本信息

```
version = 0.2.5
```
#### 2、打包发布
合入代码时会检测版本号，若版本增加，会自动触发流水线，进行打包发布

![](/personal-site-mvp/img/docs-assets/image_001_1.png "")
#### 3、检查最新版本
在厂内pip源查看该python库最新版本

[http://binary.irepo.baidu-int.com/ui/repos/tree/General/python_local_test/ai-test-generate/0.2.5/ai_test_generate-0.2.5-py2.py3-none-any.whl](http://binary.irepo.baidu-int.com/ui/repos/tree/General/python_local_test/ai-test-generate/0.2.5/ai_test_generate-0.2.5-py2.py3-none-any.whl)

![](/personal-site-mvp/img/docs-assets/image_002_1.png "")
下载后改.whl后缀为.zip 解压缩 检查下有没有奇怪的账号信息被误打包进去的

![](/personal-site-mvp/img/docs-assets/image_003_1.png "")

