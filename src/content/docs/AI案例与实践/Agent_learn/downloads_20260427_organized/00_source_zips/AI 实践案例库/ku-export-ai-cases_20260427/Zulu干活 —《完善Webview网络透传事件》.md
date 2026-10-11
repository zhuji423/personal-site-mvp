---
title: "开发需求"
description: "Zulu干活 —《完善Webview网络透传事件》"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Zulu干活 —《完善Webview网络透传事件》.md"
---
Zulu干活 —《完善Webview网络透传事件》

#### 🧑‍🏫 案例作者：[@慕海龙](https://ku.baidu-int.com?t=mention&mt=contact&id=106a2030-fceb-11f0-97c4-75d489407df4)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文记录了使用Zulu快速完成Webview网络透传事件开发需求的过程。通过明确业务需求，逐步调整Prompt，最终实现在特定条件下（authorization为true）自动添加plugin-version header的功能。体现了Zulu在敏捷开发中的高效性和灵活性，同时强调了清晰Prompt的重要性。
# 开发需求
侧边栏WebView通过插件才能请求网络，技术设计之前已经协定好通过http方式请求，如果需要header信息，WebView传业务header即可，WebView侧边栏需要拉取一个slash列表，需要插件请求后端时加一个**plugin-version**header，那开发需求就是在正确的地方塞一下这个header。

# ⚡目标
根据开发需求，快速识别出是否为Zulu开发场景。Zulu开发场景下，写Prompt+Zulu执行3分钟闪电⚡完成开发需求

# 执行
#### 直接输入业务需求
```
帮我完成一个业务开发小需求，如下：
插件接收侧边栏WebView的PassthroughRequest事件时，如果需要使用header头则需要插件额外再添加一对header键值，key=plugin-version表示插件版本，value需要你从项目里寻找调用。请帮我实现这个需求，开发完成后不需要你验证，我手动验证即可
```
  

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c8672d9cf0e24d398cfd07531b559945&docGuid=sVHKqVOSyvXVlp "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=931ad2d4411e4356b3543bfddbcc0a52&docGuid=sVHKqVOSyvXVlp "")
基本上给实现了，位置找的没问题，http请求时确实塞了个header，但我想要的是仅在PassthroughRequest事件有header的时候才塞



#### 继续输入诉求
```
我放弃了你的修改，原因是你这个实现无论在什么情况下都给我额外补充了这个header，我业务诉求是仅在PassthroughRequest事件使用了header情况下才额外补充这个header
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b68831fbbeb748aeacc7dcc01419049f&docGuid=sVHKqVOSyvXVlp "")
它确实完完全全在按着我的描述来实现，此时我发现自己交代的东西不对！

#### 矫正自己的描述，再次输入诉求
```
我还是没采纳，仅在authorization为true的时候塞一下这个header
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=205731fea6b64e1b8df34b333c33e238&docGuid=sVHKqVOSyvXVlp "")
正确实现，美中不足的是没完善自动import。

# 事后诸葛亮再玩一遍
这次要把业务诉求一次性交代清楚，争取一次就完美实现

```
帮我完成一个业务开发小需求，如下：
插件接收侧边栏WebView的PassthroughRequest事件时，仅在透传字段**authorization为true**的时候塞一下这个header，key=plugin-version表示插件版本，value需要你从项目里寻找调用。请帮我实现这个需求，注意开发完后检查一下import情况，如需导入import请帮我导入，开发完成后不需要你验证，我手动验证即可
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a3dbc252e2c944559b0342807122dade&docGuid=sVHKqVOSyvXVlp "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=607a26a85fff43798e6be90ff1405c10&docGuid=sVHKqVOSyvXVlp "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b2ba5b415ebf473c8ab8f042a208bd40&docGuid=sVHKqVOSyvXVlp "")
完美的实现了！

# **📌 **快速总结
这种及时需求是可以让Zulu做敏捷实现的，Zulu&Claude4.5做需求基本上指哪打哪，由于我一味的寻求敏捷🚀完成，Prompt写的不够用心🚨，导致我额外补充两次诉求，所以Prompt要写清楚自己想要的，别指望模型90°转弯式的理解你的所求。

#### **✨本次使用经验碎块**
* 关键词加粗有助于模型感知
* Zulu做业务开发，正常情况下不会做import



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
