---
title: "实践简介"
description: "Coding Agent实践：使用Zulu全流程开发项目"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Coding Agent实践：使用Zulu全流程开发项目.md"
---
Coding Agent实践：使用Zulu全流程开发项目

#### 🧑‍🏫 案例作者：[@迪力亚尔·帕尔哈提](https://ku.baidu-int.com?t=mention&mt=contact&id=96bde3b0-fce6-11f0-840e-9948bb30ece8)
#### 🎬 案例场景：全流程
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了使用Coding Agent（Comate Zulu）全流程开发“易水服务端测试平台”后端服务的实践。通过制定规则和自然语言描述，Zulu自动完成了需求分析、接口设计、代码生成、编译调试等任务，实现了零手写代码的目标，显著提升了研发效率，展示了AI在软件开发中的巨大潜力。
# 实践简介
本实践由语音QA迪力亚尔·帕尔哈提贡献，聚焦于“易水服务端测试平台”的后端服务开发，该服务基于百度GDP框架构建，向平台前端和第三方提供语音测试API和数据分析能力。本次具体开发任务是构建平台前端的测试集下拉框选择功能，实现下拉展示、悬停展示描述以及选择测试集后向后端回传相关ID的功能。

实践核心亮点是充分利用Coding Agent（Comate Zulu），以“零手写代码”为目标，仅通过规则制定与自然语言描述（全程总计7句话），驱动Agent自动完成需求分析、接口设计、代码生成、编译调试、接口自测、文档撰写及代码提交等全流程开发操作。最终，全部核心功能均在智能助理主导下自动化闭环完成，显著提升了研发效率并降低了重复性开发劳动。过程中积累了如何通过规则和及时交互优化Agent行为的经验，为团队后续推广智能辅助研发提供了有益的经验教训和范例支持。

# 关键词
Comate Zulu，零代码开发，全流程自动化，规则驱动，流程闭环

# 具体实施
## **1 准备工作**
### 1.1 项目背景
* **业务目标：**基于百度GDP框架构建的“易水服务端测试平台”后端服务，主要目标是为平台前端和第三方提供API支持，实现语音测试相关的功能管理和数据分析
* **整体架构：**遵循MVC架构，项目主要实现M(model 模型层)和C(controller 控制器)的部分
    * controller 控制器: 纯业务逻辑
    * model 模型层: 纯数据操作


[流程图]
### 1.2 需求分析
* **需求描述：**用户要求平台前端新增一个测试集选择下拉框；当用户鼠标移动到某个测试集上时，显示该测试集的描述；当用户点击选择某个测试集时，将该测试集名称对应的ID发送给后端进行下一步处理

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d2aba8902a174811adf59b60386435c9&docGuid=R2zKlib9f2CbKC "")
* **协议制定：**
    * 接口请求：无
    * 接口返回：


```
[
    {
        "label": "stty_ff_awk_nhst_20221020.txt",        // 测试集名
        "value": "8accc023d35befbf15882348881c7cd5",     // 测试集ID
        "desc": ""                                       // 测试集描述
    },
    {
        "label": "stty_ff_202209_10_stress.txt",
        "value": "4e3a309dcd36fb2cef52da144b5ad2a1",
        "desc": ""
    }
]
```
* **开发方案：**对于这个需求，我决定全流程使用Comate Zulu进行开发，主打的就是**“我一行代码都不写”**

### 1.3 Zulu初始化
了解到目前Zulu支持用户使用自然语言指令来规范 Zulu 的行为，如果提前为Zulu制定好规则（Rules）能够帮助其更精准地理解并适应项目的编码偏好，例如理解项目框架和代码风格等

* **本项目构建的全局rules：**rules的建设是一个逐渐优化的过程，这里是初版。在开发过程中我发现很多可以补充在rules中的规则

```
---
description: 
globs: 
alwaysApply: true
---
## 项目概述

这是一个基于百度GDP（ Go Develop Platform ）框架构建的易水服务端测试平台的后端服务项目，提供了一系列用于平台前端和第三方调用的API。平台整体遵循MVC结构, 本项目负责实现模型（Model）和控制器（Controller）的部分。

## 项目架构

项目采用模块化设计，主要分为以下几个核心部分：

1. **控制器** (`httpserver/controller/`)
   - 负责定义接口和业务逻辑实现

2. **模型** (`model/mysql/`)
   - 负责与数据库交互, 优先基于框架内部封装的gorm实现

3. **辅助工具** (`utils/`)
   - 提供了一系列工具, 例如excel操作和数据类型转换等

4. **接口路由** (`httpserver/router.go`)
    - 遵循RESTful风格

## 开发指南

### 1. 基本开发流程

1. 接口定义和业务逻辑，放置在`httpserver/controller/`目录下。
2. 与数据库交互的部分, 放置在`model/mysql/`目录下。
3. 接口路由需要写入`httpserver/router.go`。

### 2. 代码库守则

1. 开发前先pull最新代码, pull采用rebase方式.

## 代码风格指南

1. **命名规范**
   - 使用驼峰命名法
   - 类名使用大驼峰
   - 接口名清晰表达其用途

2. **接口返回**
   - errNo: 错误码, 成功时返回0, 其他错误码参考`library/errors/error_handle.go`
   - errMsg: 错误描述, 与错误码对应
   - data: 接口有需要返回业务结果时定义
   - dataLen: 接口有需要返回data数量时定义

## 注意事项

1. 在实现新功能时，确保与现有的接口保持一致
2. 文档注释要清晰完整，包含参数说明和使用示例
```
* **参考文献：**
    * 官方文档：[https://cloud.baidu.com/doc/COMATE/s/Zm9l4agw3](https://cloud.baidu.com/doc/COMATE/s/Zm9l4agw3)
    * Zulu自动生成rules：[zulu自动生成rule文件](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/D5v7y22SAA/KM5z29xch9YBfX?t=mention&mt=doc&dt=doc)


## 2 开发流程
### 2.1 需求描述
鉴于在全局rules中已经有过项目整体的介绍和相关约束，我就直接开门见山的和Zulu描述了我此次的开发需求。可以看到甚至可以使用类似[{},{},{}]的象形描述

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1adc324373cc463cb934307cc0c9e735&docGuid=R2zKlib9f2CbKC "")
Zulu的开发过程：

* **做准备：**参考全局rules，检索已有代码，了解开发模式和已有代码

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=647de6677855452ebb17c6d3b6fc5bdd&docGuid=R2zKlib9f2CbKC "")
* **执行开发：**自主编辑文件。可以看出开发的过程逻辑清晰，先实现了M层的数据交互，之后实现了C层的业务逻辑，最后在router中给该接口完成命名

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=405dac4a68da4b6daf85db527e59c6e4&docGuid=R2zKlib9f2CbKC "")
* **汇报工作**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=586b00427e1849639f8d05b95820a06e&docGuid=R2zKlib9f2CbKC "")
### 2.2 Code Review
大模型可能会犯错，因此对于生成的代码进行code review是必要的

经过检查，我发现生成的C层代码没有按照团队习惯放在easyflow_audio_set.go，而是新增了一个文件easyflow_astp_set.go

该代码库是多个团队共同开发的，因此一般大家习惯用各自团队的名称作为前缀加以区分不同业务

> *注：此时可以在rules中新增规则 “语音团队相关的代码放在easyflow_audio_xx中”*
因此我向Zulu指出了这一点

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5a3a5fb8df534fd79e731a2bccbd69cc&docGuid=R2zKlib9f2CbKC "")
Zulu的修改过程：将自建的新文件删除，相关逻辑合并进了我指定的文件里，并做了上下文兼容

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cbf093501e3442fd95c155734f4755e9&docGuid=R2zKlib9f2CbKC "")
### 2.3 编译调试
代码开发完成，下一步就是要编译并进行调试，我在此告诉了Zulu这个项目如何编译、产物在哪、如何查看端口等相关配置以及如何启动

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c1bd69a7919246c98c60f12c4c02a103&docGuid=R2zKlib9f2CbKC "")
> *注：这部分规则也可以提前放入rules中*
Zulu的执行过程：编译 → 查看产物 → 查看端口 → 启动产物服务

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6e1d9470bf804593a298f13b2ca5d503&docGuid=R2zKlib9f2CbKC "")
这里发现服务没有启动起来，我突然想起来有一个环境变量忘记设置了，打断Zulu并告诉了他这一点

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=94bfda87f0f4480f88523866eb8154ee&docGuid=zT4f5Q48yV8PXr "")
Zulu根据提示进行了环境变量的设置和重启

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1722437302a2453884bc51e39add8cba&docGuid=zT4f5Q48yV8PXr "")
### 2.4 接口自测
**测试case1：**该case为Zulu自行执行的。默认无输入，发起请求，得到接口返回。由于当前还没有测试集上传，因此data为null符合预期

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3261b644eee94e79ab5e284b12957649&docGuid=R2zKlib9f2CbKC "")
**测试case2：**Zulu在开发过程中支持了自定义产品ID和测试集属性ID来指定某个查询范围的功能，因此我给了他一组样本参数（该范围内有测试集）来测试。可以看到按照需求预期的进行了返回

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1aa35c0a35eb4816a38371410a84b46e&docGuid=R2zKlib9f2CbKC "")
### 2.5 生成文档
开发完成后我需要写一份这个接口的说明用于和前端同学进行交接，我从以前写过的文档里复制了一份标准格式给Zulu作为参考

> *注：文档规则可以放入rules中*
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6ef3fd1649834570b106b4ea119aee59&docGuid=R2zKlib9f2CbKC "")
Zulu的回复：非常标准，可以直接复制进知识库或者icafe卡片中（带格式）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f5e76a4ef1f043658ceddbb61b2face8&docGuid=R2zKlib9f2CbKC "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aa5974142b794d3ab8dce43e5b1f68d5&docGuid=R2zKlib9f2CbKC "")
### 2.6 代码提交
接下来到了提交代码至代码库的阶段，我给Zulu大概讲了一下流程和我本次的需求卡片

> *代码库规则可以放入rules中*
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8c6dc45bbea94efa899b84328631e266&docGuid=R2zKlib9f2CbKC "")
Zulu的执行结果：按照要求进行了提交并返回了评审链接

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9c494120b6704de6bc8a364ebfeb2ef1&docGuid=R2zKlib9f2CbKC "")
# 复盘
## 模式
### 给Zulu一个机会
大模型也会出错，有时候写出来的代码有问题并不代表Zulu就不可用了，你完全可以让他自己去查问题，并自行迭代。他自己修复问题的过程有可能比你去读代码再改来的要快，不要失去耐心。

### 从对话助手到Agent的思维转变
我认为Coding Agent与普通对话大模型的区别在于是可以完成除了问答之外的各种实际操作，例如直接修改文件和终端执行指令等，嵌入式的协助我们开发，这就使得我们能够完整的在Comate中完成从需求到提交代码库的所有操作

### 可扩展性的潜力
借助MCP和插件等工具，甚至可以直接对接其他平台，例如icafe和知识库等，直接完成卡片操作和文档撰写，省去了到处跳转，完成一站式开发

同时我们可以自定义MCP接入到Comate中，实现定制化的功能，可以说潜力无穷

这里推荐一篇文档：[稳定性查询脚本MCP化接入Zulu](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/xG-SODiTDx/Zd3mOqHg3MlOTd?t=mention&mt=doc&dt=doc)

## 反模式
### 过多的记忆
我们以为做好了上述第一个接口的铺垫以后在同一窗口内继续进行第二个接口的开发会带来效果上的提升，但是就像人对话多了会忘记内容一样，Zulu会反应变慢且收到一些之前接口的干扰。

最佳的实践是将可以作为公共规则的部分提炼进Rules中，然后再新开一个窗口进行开发，会带来更好的性能和效果。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
