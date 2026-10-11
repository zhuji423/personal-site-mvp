---
title: "需求：对不合理需求say no"
description: "人生苦短，我用AI Coding"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\人生苦短，我用AI Coding.md"
---
人生苦短，我用AI Coding

#### 🧑‍🏫 案例作者：[@王爱超](https://ku.baidu-int.com?t=mention&mt=contact&id=9226aeb0-fcee-11f0-8001-672082fcaae3)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了利用AI Coding提升研发效率的实践，包括通过AI快速定位业务逻辑代码及其背景、利用编码规范Rules提升代码规范性和可控性、以及通过Rules简化重复开发动作。强调AI Coding让人从繁琐的基础工作中解放出来，聚焦创造性设计，同时指出AI工具需持续优化以适应更广泛的应用场景。


# 需求：对不合理需求say no
## 痛点
日常产品需求分析或者排查问题时，经常需要定位某一个细小的业务功能是什么时候有的，当时的业务背景是什么。如果不熟悉相关代码，需要花很大精力找到相关业务逻辑的代码，再查看git提交记录和注释，找到需求卡片，进一步找到当时的MRD。可以利用AI输入业务逻辑查找代码位置，进一步找到git记录、需求卡片和MRD，并分析得到业务背景。

## 解法
```
请帮我根据一个目标业务逻辑找到相关的业务背景，也就是为什么要有该业务逻辑。

# 具体步骤
1. 找到实现该业务逻辑的代码。
2. 找到具体代码的git blame。
3. 如果相关代码的git blame有多个提交，则从comment中推测最相关的一次提交。
4. 从该次提交的comment开头提取icafe卡片编号。
5. 如果icafe卡片有父卡片，则找到父卡片，直到最上级的父卡片。
6. 从最上级的icafe卡片的内容中寻找目标业务逻辑的业务背景。
7. 如果icafe卡片中没有具体解释，而是有知识库文档链接，则访问知识库文档，寻找目标业务逻辑的业务背景。

# 目标业务逻辑
xxxxxxxxx

# 代码入口
xxxxxxxxx
```
## 调试case
[https://console.cloud.baidu-int.com/comatestack/share/3708?token=4a972696](https://console.cloud.baidu-int.com/comatestack/share/3708?token=4a972696)

## 下一步
具备通用性，可以成为Agent产品，但需要优化

* 步骤可以更精确，使执行效果更稳定
* 主要的代码入口可以单独固化为rules，作为背景知识



## 


# 开发：跟不规范代码说byebye
## 痛点
客户端定期发版、铺渠道，代码改动的敏捷性较低，因此对代码的规范性和可控性有更高要求。此前，规范性和可控性的评估基本依赖人工CR判断，难免问题漏出，不可依赖，而现在，可以借助IDE集成的AI Coding能力提升可靠性和效率。



## 解法
1. 基于知识库MCP，产出编码规范Rules；
2. 基于代码仓库结构简洁Rules，定位新增代码；
3. 基于编码规范Rules 与 代码开关控制Rules，判断开关规范；
4. 输出不规范代码；
5. 基于规范与代码变更，修复变更代码，生成patch。

```
# Prompt1：产出编码规范

读取知识库链接`https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/GTYswyYRrG/xknNaPaxBGrH3d`指向的文档，以markdown的形式输出一份完整的Kotlin编码规范Rules。

# Prompt2：修改不规范代码

客户端代码有既定的代码规范，按照如下步骤帮我检查新增代码是否符合规范要求，一定要聚焦新增代码，忽略已经commit的代码！！！
1.根据 #ad-business-structure.mdr  ，找到所有ad_business仓库中未git add和未git commit的代码变更；
2.根据编码规范 #kotlin-code-style.mdr  ，判断步骤1中找到的新增代码是否符合规范要求；
3.根据新增代码开关控制规范 #new-code-control.mdr ，判断步骤1中找到的新增代码是否符合规范要求；
4.以表格形式逐个输出2、3中找到的不符合规范的代码改动，给出代码位置跳转链接，给出与规范的差距；
5.针对2、3中的不规范代码，在代码文件中生成改动patch，修复不规范代码。
```
![1.git查找代码diff](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fa64a057c0324188ae39be241512385a&docGuid=99pkERhgApi8ml "1.git查找代码diff")
![2.代码审查](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6571b5d6519f4b53a8d637b31f1fb479&docGuid=99pkERhgApi8ml "2.代码审查")
![3.代码审查总结](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=011c23d32fd540a49a9562867503fb64&docGuid=99pkERhgApi8ml "3.代码审查总结")
![4.详细问题分析](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a56d904b75dc410ba495b160dbfc99af&docGuid=99pkERhgApi8ml "4.详细问题分析")
![5.生成修复代码patch](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a566d109a7d14f5fb415df15e41fad63&docGuid=99pkERhgApi8ml "5.生成修复代码patch")
![6.再次检查新增代码并总结](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b606e475b13c4cb69866eb82d9821f67&docGuid=99pkERhgApi8ml "6.再次检查新增代码并总结")
![生成代码1](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7eea6822123b4c18b738ed249b530922&docGuid=99pkERhgApi8ml "生成代码1")
![生成代码2](http://bj.bcebos.com/rte-file/kuResource/4bce1fd75a894fce986fc1e487357107 "生成代码2")
![生成代码3](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=310d3a8d508b4caca74e290bff1ace87&docGuid=99pkERhgApi8ml "生成代码3")
![生成代码4](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=21621140259243d5b43bce93d8e6cf7c&docGuid=99pkERhgApi8ml "生成代码4")
![生成代码5](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=28ca32936a064696b4950e77a6897d75&docGuid=99pkERhgApi8ml "生成代码5")
![生成代码6](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc2cb3c07e084e42aa2298de377c8bb4&docGuid=99pkERhgApi8ml "生成代码6")
![生成代码7](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1011d833147f41e5ba946cf4227744b1&docGuid=99pkERhgApi8ml "生成代码7")
[https://console.cloud.baidu-int.com/comatestack/share/3709?token=2aecf7d8](https://console.cloud.baidu-int.com/comatestack/share/3709?token=2aecf7d8)

## 下一步
支持所有百度代码规范。



# 运行：Everything ku can play
## 痛点
图灵数据流算子，每个算子都有不同的模版，并提供了使用手册。开发时，每次新增算子的时候需要根据文档搭建本地的环境，重复工作比较多。

## 解法
平台手册，转化成Rules，简化重复动作，提升工作效率。

```
1. 读取 https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MUyZ7Y-BGz/a0bhydzuze/doIzFcyYEAQ_j7 , 分析构建一个本地任务执行算子环境模版的流程

2. 基于总结的流程，逐个进行细化，并生成一个rules用于构建本地任务执行算子环境模板

3. 在test下生成1212目录，并应用 #local-task-operator-template.mdr

4. 演示一下执行效果
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=efe6ba4809684d778c54f60bd8080b11&docGuid=99pkERhgApi8ml "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aeeb0c4eaf0440399c104c35dc836d40&docGuid=99pkERhgApi8ml "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=029294f8eea34b7e9f72e9ffa371234f&docGuid=99pkERhgApi8ml "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=13bc864ff4bd45bfb6f4eae3aa2d8b54&docGuid=99pkERhgApi8ml "")
## 下一步
落地点：除了平台的一些规范、模版、部署环境等等，个人的一些开发环境、开发习惯等等，都可以转换成Rules进行发布，自动化执行，提升人效。

依赖：MCP支持的系统越多，AI coding的能力也就越来越强大。



***人生苦短*****，我*****用AI Coding***



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
