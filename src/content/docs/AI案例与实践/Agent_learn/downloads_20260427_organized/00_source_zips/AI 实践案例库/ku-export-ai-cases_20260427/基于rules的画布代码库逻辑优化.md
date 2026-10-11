---
title: "一、背景"
description: "基于rules的画布代码库逻辑优化"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于rules的画布代码库逻辑优化.md"
---
基于rules的画布代码库逻辑优化

#### 🧑‍🏫 案例作者：[@李昂](https://ku.baidu-int.com?t=mention&mt=contact&id=0badbfb0-fce2-11f0-bffb-11f7dd9bffc0)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了利用zulu和rules优化画布代码库的实践经验。针对B端和C端融合后存在的无效代码问题，通过设计信息类、约束类和指令类rules，指导AI进行无效代码清理，解决了人工查找繁琐且易出错的问题。同时，总结了rules应用中的注意事项，如rules数量与效果的关系、模型处理上下文能力有限等，为后续类似项目提供了宝贵经验。
# 一、背景
自由画布代码库B端和C融合拆分以后存在部分无效主站代码，需要进行无效代码优化。

优化的必要性：

* 新入职同学看到无用逻辑容易摸不清头脑。
* 开发老手等待旧逻辑执行单测流水线时间较久，开发体验不好。

# 二、使用zulu&rules规则的优化的必要性
* 人工查找麻烦，工作具有一定的重复性和逻辑性，符合AI工作的特点。
* 后续在遇到类似问题，规则可以重复利用





# 三、rules的设计
## 3.1 信息类rules
```
liang24-info-rules.mdr
code-style.mdr
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=014cbef90f3e42c19d5ca7cb42055ecf&docGuid=WhtLALrKNXVPK8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1d94df3818a54bd8b203634deed434a3&docGuid=WhtLALrKNXVPK8 "")
## 3.2 约束类rules
```
liang24-limit-rules.mdr
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=26d11767c343436a860fa3003c66d778&docGuid=WhtLALrKNXVPK8 "")
## 3.3 指令类rules
```
liang24-order-rules.mdr
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=49a5cc3579764923bfcd8ae43d8de853&docGuid=WhtLALrKNXVPK8 "")
[附件]
# 四、问题总结
1.rules并不是越多效果越好。

2.模型处理上下问能力有限，小文件还好，大文件容易被截断。

3.生成过程中容易卡死长时间无响应。

4.后端开发过程中zulu感觉适合防御性编程、搭架子、逻辑优化、单测编写等场景。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
