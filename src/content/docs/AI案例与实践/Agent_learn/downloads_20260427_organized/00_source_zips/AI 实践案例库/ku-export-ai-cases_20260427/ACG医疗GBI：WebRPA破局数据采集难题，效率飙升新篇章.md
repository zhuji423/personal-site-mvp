---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "ACG医疗GBI：WebRPA破局数据采集难题，效率飙升新篇章"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\ACG医疗GBI：WebRPA破局数据采集难题，效率飙升新篇章.md"
---
ACG医疗GBI：WebRPA破局数据采集难题，效率飙升新篇章

#### 🧑‍🏫 案例作者：[@郭静](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：知识加工、工作流自动化、信息洞察
#### 🔧 使用工具：AI Spider WebRPA
#### 📒 案例概要：ACG医疗GBI应用WebRPA技术，自动化采集药企财报、知网论文、卫健委执业医师资格及药企会议信息，将手动转为自动，显著提升数据效率与质量。年化节省人力总计约1697人天，赋能SOURCE、METRIX等核心数据库，支撑GBI约22.4%至18%的收入，突破人工采集瓶颈，强化数据交付与维护能力。
**<项目背景>**

ACG医疗GBI作为面向TOB药企的数据提供商，需从公开渠道采集大量的数据数信息，因验证码技术壁垒、附件上传下载等卡点影响，导致数据采集高度依赖人工，一定程度上影响了项目交付效率及数据库数据有效性建设维护，同时人工采集监测的低效方法，也占用了业务大量人力

**<项目目标>**

基于 Web RPA 的自动化技术突破验证码壁垒，实现了卫健委执业医师资格、药企会议数据、财报数据、知网论文数据自动化采集，提升业务数据采集效率，助力业务完善 METRIX（医疗服务研究人员数据库）及 SOURCE（全球药品数据库）等核心数据

收益：

##### 收益：
**<定量目标>**

突破验证码壁垒，利用附件下载上传等特色能力，实现了卫健委执业医师资格、药企会议数据、财报数据、知网论文4个任务场景的数据自动化采集

**<定性目标>**

为ACG医疗44.4%的收入提供数据赋能，年度预计节省业务人力成本447人天/年

**业务背景：**ACG GBI是中国医疗信息数据提供商（一站式数据库平台），主要面向TOB药企客户提供数据咨询服务，覆盖95%头部MNC药企；其数据采集范围涵盖海量公开渠道信息。受数据网站验证码、附件上传下载等卡点影响，目前只能通过人工采集监测，消耗人力大，且一定程度上影响了项目交付效率及数据库数据有效性建设维护，急需自动化能力，突破目前数据监测瓶颈，节省人力投入。

**部门：**智能云事业群组/*/医疗产品部/医疗GBI研发组

**解决方案：**

* **GBI财报自动化采集监测**

基于WebRPA自动化能力，实现药企财报数据由“手动采集→自动获取”的范式改变，提升数据采集效率，年化节省人力104人天/年，完善SOURCE(全球药品数据库)药品/公司板块核心数据**，为GBI22.4%的收入提供赋**

收益：预计节省人力104人天/年（2人天*52周/年）

![RPA流程图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b48edb99ca554a1e89f914c21303c745&docGuid=JYw7kgoirymDs8 "RPA流程图")
![财报信息选择](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=35346ab99f0841219dbc443ec28a60bf&docGuid=JYw7kgoirymDs8 "财报信息选择")
![财报附件下载](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=51f938a8760e47bb9b14d6e458de6597&docGuid=JYw7kgoirymDs8 "财报附件下载")
![财报附件业务系统上传](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=02dc8d2b60024a319729a7a43e6505b3&docGuid=JYw7kgoirymDs8 "财报附件业务系统上传")
* **GBI知网论文自动化补采**

基于Web RPA自动化能力，实现了知网论文由“手动采集→自动获取”的范式改变，提升数据采集效率及质量，年化节省人力123人天/年，完善METRIX（医疗服务研究人员数据库）核心数据，**为GBI18%的收入提供赋能**

收益：预计节省123人天（1640条*3min*12月）

![RPA流程图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f3d6a1a661f84254895e4ff194731be3&docGuid=JYw7kgoirymDs8 "RPA流程图")
![首次验证码](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2ee08ad807e541aaa134a3cc6baaa413&docGuid=JYw7kgoirymDs8 "首次验证码")
![二次验证码](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0a12cbe2b76a4922bc98ccea65434d1d&docGuid=JYw7kgoirymDs8 "二次验证码")
![论文内容监测](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e7a3cf00af944eccb8752c05ccd3beb2&docGuid=JYw7kgoirymDs8 "论文内容监测")
* **GBI卫健委执业医师资格自动化监测**

基于Web RPA自动化能力，实现卫健委网站执业医师资格数据由“手动采集”到“自动获取”的范式转变。提升数据采集效率，年化节省人力1350人天/年。**医师资格监测为GBI 18%的收入提供赋能**

收益：

1、项目交付：预计节省100人天/年（10人天/千项目*10）

2、GBI标准数据库有效性信息更新：1250人天（60w*1min），如果不做数据有效性更新会牺牲数据质量

![RPA流程图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7565b6b7a958430f9de243f88aedbea6&docGuid=JYw7kgoirymDs8 "RPA流程图")
![医师信息填写验证](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7aabd21a5a434c1cb6acdc821bf74151&docGuid=JYw7kgoirymDs8 "医师信息填写验证")
![医师信息监测](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2782747d5e8a41c696bc9a12b791febb&docGuid=JYw7kgoirymDs8 "医师信息监测")
* **GBI药企会议信息自动化获取：9.17已上线**

基于Web RTA自动化能力通过搜狗微信渠道进行信息采集，实现了药企会议信息从“手动采集”到“自动获取”的范式改变，提升GBI会议信息采集效率，降低了人力成本，并增强METRIX（医疗服务研究人员数据库）产品的核心数据能力。同时，通过持续获取医学领域最新学术会议信息，能够及时追踪研究者的前沿动态，帮助企业客户更精准地把控目标客户的活跃度与观念变化；也助力业务提升非订阅项目交付效率（客户临时数据需求/售前POC）。药企会议数据监测将为GBI 18%的收入提供赋能

收益：预计节省120人天/年（10天/月*12月）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cb7810a9dddc4fdf991d28d3bdfbdf80&docGuid=XwNj4aAcQ3TM8B "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bade99adc78f4bed8992e5c3dc9c0cfb&docGuid=5W0lRGiYDEU68l "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
