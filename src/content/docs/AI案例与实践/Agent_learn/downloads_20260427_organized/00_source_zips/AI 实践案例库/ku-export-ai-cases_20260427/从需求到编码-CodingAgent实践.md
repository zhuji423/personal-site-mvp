---
title: "一、CodingAgent协同编码流程"
description: "从需求到编码-CodingAgent实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\从需求到编码-CodingAgent实践.md"
---
从需求到编码-CodingAgent实践

#### 🧑‍🏫 案例作者：[@贺凯](https://ku.baidu-int.com?t=mention&mt=contact&id=c8fed9d0-fce9-11f0-bf0f-416fa3f55aeb)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Ducc
#### 📒 案例概要：本文介绍了CodingAgent在复杂需求编码中的协同流程，通过撰写技术文档、拆分任务、委托CodingAgent思路、Review与编码实现，展示了AI辅助编码的高效性与准确性。强调将编码交给Agent，让人工专注于思考与创造，提升了开发效率与代码质量，是AI时代下的编码实践典范。
现阶段，CodingAgent独立完成一个复杂的需求，成功率还是有点低，但是CodingAgent按照一个整理好的任务步骤文档来编码还是相当给力的。

# 一、CodingAgent协同编码流程
[流程图]
标红的表示需要人工重点关注的。

# 二、一个实际例子
## 2.1 背景
场景：百度CC服务端开发。

需求描述：百度CC服务端是一套专为CC客户端打造的综合跟踪系统，集成了身份验证、用户交互监测和代码生成记录等功能，通过多元化存储策略和中央数据平台集成，为用户行为分析和产品迭代提供数据支持。

功能列表：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9ecb598b32cb4207b510bbcb8ce515e7&docGuid=fYxhUKrCFGsmmg "")
## 2.2 实践步骤
### 第一步：撰写技术文档
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=14ad1dab715c486dbad3ced9af4302dc&docGuid=fYxhUKrCFGsmmg "")
### 第二步：将技术文档拆分到具体的任务文件
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=13affd7e11ab43fc9a134499f711a07e&docGuid=fYxhUKrCFGsmmg "")
以“根据用户jwtToken获取modelToken接口”实现为例。

任务描述文件：

```
需要实现GetModelTokenByUserJWT接口，请将方法定义在server/controller.go中，可以参考JwtAuthentication方法的实现。
接口的请求为：
```
curl http://localhost:8080/api/rest/v1/jwt/model?accessToken=xxx
```
接口的响应为：（请将结构体定义到pkg/api/model_token.go中）
```
{
    "requestId": "123",
    "code": 200,
    "message": "success",
    "modelToken": "xxx"
}
```
接口的逻辑为：
1. 先根据accessToken从redis获取modelToken，有的话将值返回到GetModelTokenByUserJWT响应中，没有的话执行第2步。
2. 根据accessToken从redis获取username，没有的话执行第3步。
3. 调用util.ValidateAccessToken方法获取username（url、clientId、clientSecret从pkg/conf.go中获取），若data.username非空，将data.username先存入redis，再执行第4步。
4. 调用第三方接口，
```
curl --location 'https://{{modelRouter.url}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{modelRouter.authToken}}' \
--data '{
    "name": "zhangsan",
    "expired_time": -1,
    "unlimited_quota": true,
    "models": ""

}'
```
响应结果是：
```
{
    "data": {
        "key": "xxx",
        "status": 1,
        "name": "zhangsan"
    },
    "message": "",
    "success": true
}
```
若data.key非空，将data.key先存入redis，再返回到GetModelTokenByUserJWT响应中。其中modelRouter.url、modelRouter.authToken从pkg/conf.go中获取。

你的任务是：实现这个接口的逻辑，并将第4步的接口调用封装为一个方法放到pkg/util包中，文件名为model_router.go。redis相关的方法实现在pkg/cache/redis.go。http调用方法在pkg/util/http.go。业务逻辑的方法实现在server/controller.go中。配置相关方法在pkg/conf.go中。
```
### 第三步：委托CodingAgent给出任务实现思路
本示例中CodingAgent采用百度CC。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e667008a80124bb6b89d70668be7f1bd&docGuid=fYxhUKrCFGsmmg "")
### 第四步：Review CodingAgent给出的实现思路
该例子中，CodingAgent给出的实现思路没有问题，我们让它继续执行。

（ps：如果有问题的话，可以直接告诉它哪里有问题，让它进行调整）

### 第五步：允许CodingAgent根据review后的思路进行编码
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e621499cf35b4a268b114f8cf5d2e61b&docGuid=fYxhUKrCFGsmmg "")
### 第六步：Review CodingAgent生成的代码
因为在任务描述文件中已经具体告知CodingAgent如何做，所以我们可以发现CodingAgent生成的代码是符合预期的。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6357ddbbddc4ecba13a4c5be32deb15&docGuid=fYxhUKrCFGsmmg "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c63b258900e14dd2808dbaca6c7d194e&docGuid=fYxhUKrCFGsmmg "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1d7e8d4a88194a2ebac2bdd5fe15b7c2&docGuid=fYxhUKrCFGsmmg "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c76c35dd648a4b2bad4fd36749196d28&docGuid=fYxhUKrCFGsmmg "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b91a63924e9540e4bc71437859d21a74&docGuid=fYxhUKrCFGsmmg "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d824da2ba2f14d968b13974a1bb9572d&docGuid=fYxhUKrCFGsmmg "")
### 第七步：人工验证功能
这一步可以让CodingAgent直接生成测试case，自动跑。

最好再人工验证下。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=90aee675199144a98d349f00bceab487&docGuid=fYxhUKrCFGsmmg "")
# 三、最后
希望大家可以积极的拥抱CodingAgent，**将编码交给Agent，将思考和创造留给自己。**



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
