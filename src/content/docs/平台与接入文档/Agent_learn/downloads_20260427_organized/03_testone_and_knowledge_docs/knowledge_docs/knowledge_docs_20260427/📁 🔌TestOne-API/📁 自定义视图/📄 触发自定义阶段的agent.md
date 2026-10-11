---
title: "一、 接口"
description: "触发自定义阶段的agent"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 自定义视图\\📄 触发自定义阶段的agent.md"
---
触发自定义阶段的agent

# 一、 接口
|**地址**|/api/customView/openAPi/triggerAgent|
|-|-|
|**请求方式**|POST|
|**content-type**|application/json|
|**权限**|None|
|**header**|username: 个人邮箱前缀token: 个人在TestOne平台Token (获取方式：[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken) )|
|**请求参数**|{
    "customVersion": "youtrack-1354",
    "customStageId": "13",
    "isRelease": 0
}|
|**返回结果**|{
    "code": 0,
    "msg": "success",
    "requestId": "b6fed612-6199-4f0b-acf3-a86d2f64688d",
    "data": {
        "cardIds": "youtrack-1354",
        "engineTaskId": "9aaccad1-06f7-47c3-9ef2-a564376e5f8e",
        "agentStatus": 1
    }
}|


