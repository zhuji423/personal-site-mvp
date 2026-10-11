---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "dodo 拯救我的日常"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\dodo 拯救我的日常.md"
---
dodo 拯救我的日常

#### 🧑‍🏫 案例作者：[@杨轶男](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：其他、办公
#### 🔧 使用工具：dodo
#### 📒 案例概要：dodo支持自动化OKR/SLA巡检、AI编程辅助、需求闭环处理及群消息感知，提升开发效率。




## OKR review 
[https://okr.baidu-int.com/pages/review.html](https://okr.baidu-int.com/pages/review.html)

拿我的账号登陆这个网站就能看到我所有的周报，并参考上传的文件，然后在下面这个网页填写okr review保存：



[https://okr.baidu-int.com/pages/weekly.html](https://okr.baidu-int.com/pages/weekly.html)

保存前让我确认

[轶男：dodo 拯救 Q 末打工 P 人](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/esHF4uSRzd/6K2eSXQk2Ih-3K?t=mention&mt=doc&dt=doc)

[2026 年 Q1 OKR Review 报告](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/nK_k8495fV/jyBoEwD64bRx6z?t=mention&mt=doc&dt=doc)





## 定时任务 -- sentry 日志巡检
[http://sentry.network-product.baidu-int.com/organizations/network-product/issues/](http://sentry.network-product.baidu-int.com/organizations/network-product/issues/)  地址是 BSP 项目记录 sentry 日志的地址

请每天 11:10 整理过去 24 小时的错误日志事件，要求分项目统计每种异常事件的数量

![效果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1c395e2156784c4fafc7d9f39677aa0b&docGuid=YPfU9wQC2AvhKh "效果")
定时任务生成后可在 web 端编辑

[https://dodo.baidu-int.com/space/540/task/34107](https://dodo.baidu-int.com/space/540/task/34107)





## 定时任务 -- AI 咨询推送
GitHub 上的「Awesome‑xxx」是社区公认的高质量分类合集，适合系统选型。

1. Awesome AI Coding（最全面）

地址：[https://github.com/TomGranot/awesome-ai-coding](https://github.com/TomGranot/awesome-ai-coding)
分类：IDE 插件、独立 AI IDE、代码生成、开源工具、CLI、企业方案等
收录：Copilot、Cursor、Continue、Tabnine、Amazon Q、Supermaven 等全主流工具

每天读取相关咨询 10:50 生成日报推送

![效果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=43baebd9612346bda926632b4c3fac5a&docGuid=YPfU9wQC2AvhKh "效果")
![生成报告](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8a663e21fbb2453d8067b32e8fa35126&docGuid=YPfU9wQC2AvhKh "生成报告")




## 拆卡片
我要实现知识库 [2. 作业管理](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/41FsefhkDo/lrfamHdefwPJ-_?t=mention&mt=doc&dt=doc) 子目录下的接口功能，请帮我在 [NP-SPRINT-BSP/2026-02TH](https://console.cloud.baidu-int.com/devops/icafe/space/bsp/planbox/1106414/issue?viewId=144721?t=mention&mt=doc&dt=sdk) 空间 2026-02TH 迭代中建立卡片

1. 一个接口建立一个 Story 父卡片 + 一个 Task 子卡片

2. Story 父卡片标题要求 [标准运维] 开头、所属服务 选择 标准运维、任务类型 选择 研发任务

3. Task 子卡片 任务类型 选择 研发任务、所属服务 选择 标准运维、是否免测 选择 否、所属模块 选择 脚本执行

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1f5c313f65704dc1917cb9d0189a3ef1&docGuid=YPfU9wQC2AvhKh "")
[dodo内置DevOps Skill Changelog -- 20260322](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/esHF4uSRzd/UGZde-wXtL7DVP?t=mention&mt=doc&dt=doc)





## SLA 巡检
你是不是还在为每周手动扒拉sugar数据而费劲？！—— 交给dodo

[https://sugar.baidu-int.com/dataPortalShare/datahub?menu=m_m024uo5x263jt](https://sugar.baidu-int.com/dataPortalShare/datahub?menu=m_m024uo5x263jt) BGW SLA 指标

[https://sugar.baidu-int.com/dataPortalShare/datahub?menu=m_m024uo5x263jt](https://sugar.baidu-int.com/dataPortalShare/datahub?menu=m_m024uo5x263jt) BigNAT SLA 指标

合格指标阈值是同地域 SLA 99.95%以上，若有连续少量的丢包也算异常



请根据页面返回下拉框中遍历所有的集群指标，分析昨天 2026.03.26 网关服务质量







## 需求闭环
写代码写到头秃，想尝试些新方案？！—— 交给dodo

* 把你的需求或 bug 甩给 dodo，它能帮你分析需求、写代码、提交评审、跑流水线，一条龙服务~
    * 解放双手等级：⭐⭐⭐（前期还是要告知代码库信息等，后面就不用啦）
    * 风险指数：⭐⭐（代码都给你看，改不改你说了算）
    * 注意事项：⭐（记得检查 commit message 哦）
    * tips：可以直接丢 iCafe 卡片链接，dodo 自动识别需求帮你干活！（在啥基础知识都知道的情况下）


[https://dodo.baidu-int.com/space/540/task/36094](https://dodo.baidu-int.com/space/540/task/36094)





## 群消息感知
* **群消息感知能力优化，支持收集群内其他机器人消息**
    * 可用于报警、数据分析等场景


![分析效果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=25a7673f47ec47fe85dfea3e2ef07c72&docGuid=YPfU9wQC2AvhKh "分析效果")




## 排障
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8b8f90b1cf184c94aca118fef103dd49&docGuid=YPfU9wQC2AvhKh "")
错误日志：[http://sentry.network-product.baidu-int.com/organizations/network-product/issues/4895/?project=11&referrer=webhooks_plugin](http://sentry.network-product.baidu-int.com/organizations/network-product/issues/4895/?project=11&referrer=webhooks_plugin)  结合代码库 [https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bs-platform/detection/tree/master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bs-platform/detection/tree/master) 帮我分析错误原因

[https://dodo.baidu-int.com/space/540/task/36094](https://dodo.baidu-int.com/space/540/task/36094)：错误分析报告

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
