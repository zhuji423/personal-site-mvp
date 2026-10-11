---
title: "📄 给QA分配需求卡片和排期"
description: "给QA分配需求卡片和排期"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 团队日历\\📄 给QA分配需求卡片和排期.md"
---
给QA分配需求卡片和排期

**功能**

> 给QA分配需求卡片和排期（模块测试任务分配）


**接口信息**

> 地址：https://testone.baidu-int.com/api/task/assignIcafeToUser
> 方法：POST


**Header**

|字段|类型|含义|获取方式|
|-|-|-|-|
|username|string|用户名|浏览器打开[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken)链接获取|
|token|string|Token |浏览器打开[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken)链接获取|



**参数**

> 针对非必填项，不传此字段，表示不限制
|字段|类型|必填|含义|示例|
|-|-|-|-|-|
|icafeId|List|是|需求卡片ID|"youtrack-1744"|
|startDateTime|Date|是|排期开始时间|"2025-12-01 02:00:00"|
|endDateTime|Date|是|排期结束时间|"2025-12-02 23:59:59"|
|qaList|List|是|QA人员|["zhangtao77"]|
|assignReason|String|否|分配原因|“QA借调”|

**参数**

```
{
    "icafeId":"youtrack-1744",
    "startDateTime":"2025-12-01 02:00:00",
    "endDateTime":"2025-12-02 23:59:59",
    "qaList":[
        "zhangtao77"
    ],
    "assignReason":"QA借调"
}
```


**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20251201-server-01-9256-1d4d223c8671",
    "owner": "wushaoshan",
    "data": true
}
```
```
{
    "code": 400,
    "msg": "参数校验错误: 卡片[youtrack-1744555]未导入TestOne!",
    "requestId": "20251201-server-01-9a8c-ff10c49b5dce",
    "owner": "wushaoshan",
    "data": null
}
```


**效果**

![](/personal-site-mvp/img/doc-placeholder.svg "")





