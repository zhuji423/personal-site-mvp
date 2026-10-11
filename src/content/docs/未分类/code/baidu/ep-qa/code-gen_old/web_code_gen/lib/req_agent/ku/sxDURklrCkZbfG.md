---
title: "1  项目详情"
description: "【影视频道】继续看小窗"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\lib\\req_agent\\ku\\sxDURklrCkZbfG.md"
---
【影视频道】继续看小窗

# 1  项目详情
[[ailite-28828] 【非随】影视频道-继续看小窗](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-28828/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)

# 2 需求
**背景**

现已验证回访对于提升端留存有重要作用，个人中心【最近播放卡片】有展用户实验数据，端次留+0.09%，端次留量+0.15%，ctr 10.5%，现计划于极速版内搭建整体回访框架，此需求为影视频道场景内新增回访入口

**收益**

端次留+0.05%，影视时长+xx分钟

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1a1147cecd6c4453b648e3a3cb4ebec5&docGuid=sxDURklrCkZbfG "")
# 3 沟通地图
## 内部
|    角色|    接口人|备注|
|-|-|-|
|   PM|     @王琪||
|   SRD|   @潘超毅 ||
|FE|    @唐豪健||
|SQA|    ||
|CRQ|||
## 模块拆分
|接口内容|备注|
|-|-|
|首页-home接口||
### 接口文档
1. **影视频道首页**
接口地址：/baiduboxapp/basic/movieChannel/home

请求类型：GET

参数：公参&cookie

结果返回：

```
{
    "data":{
       "config":{
           "smallWindowSwitch":1     //小窗开关
       }
        "diamond":[],
        "history":{}
        "television":{},
        "movie":{},
        "recommend":{}
    }
}
```
# 4 详细设计
[流程图]
## 4.1 存储设计
### 4.1.1 GCP
```
// key:movie_channel_experiment
{
  "isDiamond": false,
  "isHistory": true,
  "isMovie": true,
  "isRecommend": true,
  "isTelevision": true,
  "isHistoryRec": true,
  // 新增小窗开关
  "isSmallWindow": true
}
```
# 上线流程
1. GCP配置上线
2. 业务代码上线（sbox-basic）