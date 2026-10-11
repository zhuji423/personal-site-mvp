---
title: "📄 给QA手动录入任务"
description: "给QA手动录入任务"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 团队日历\\📄 给QA手动录入任务.md"
---
给QA手动录入任务

**功能**

> 给QA分配任务和排期（手动录入任务）


**接口信息**

> 地址：https://testone.baidu-int.com/api/task/addTask
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
|deptId|Integer|是|产品线ID|26674|
|subDirection|String|是|业务方向|工作台|
|taskType|Integer|是|任务类型0："其他任务"1："模块测试"2："集成测试"3："写Case"4："值班"5："休假"6："技术Topic"7："灰度测试"|6|
|title|List|是|任务标题|测试一下|
|qa|String|是|qa中文名|吴绍山|
|qaValue|String|是|qa邮箱前缀|wushaoshan|
|testDays|Integer|是|排期时长|1|
|testStartTime|Date|是|排期开始时间|2026-01-05 10:00:00|
|testFinishTime|Date|是|排期结束时间|2026-01-06 10:00:00|
|creator|String|是|创建人|wushaoshan|
|operator|String|是|操作人|wushaoshan|

**参数**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20260310-server-03-bc41-e6f301061a11",
    "owner": "wushaoshan",
    "data": 740349
}
```


**效果**

![](/personal-site-mvp/img/doc-placeholder.svg "")





