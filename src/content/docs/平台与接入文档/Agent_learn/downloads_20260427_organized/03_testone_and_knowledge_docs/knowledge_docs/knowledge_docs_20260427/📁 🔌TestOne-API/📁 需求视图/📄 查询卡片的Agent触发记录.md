---
title: "📄 查询卡片的Agent触发记录"
description: "查询卡片的Agent触发记录"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 需求视图\\📄 查询卡片的Agent触发记录.md"
---
查询卡片的Agent触发记录

**功能**

> 查询卡片的详细信息


**接口信息**

> 地址：https://testone.baidu-int.com/engine/storyAgent/getAgentExecuteRecordByIcafeId
> 方法：GET


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|YOUR_NAME|
|token|string|Token |YOUR_TOKEN|



**参数**

|字段|类型|必填|含义|示例|
|-|-|-|-|-|
|icafeId|string|是|卡片ID|bjhpm-23583|
|stage|int|是|阶段ID|4|



**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "18022346-71bb-486f-a61d-83ec69684670",
    "data": [
        {
            "id": 320318,
            "deptId": 27084,
            "subDirection": "百家号",
            "icafeId": "bjhpm-23583",
            "stage": 4,
            "operator": "qep-testone",
            "operationType": 0,
            "agentId": 123,
            "engineTaskId": "4b4bdf0b-ec4f-4054-92cb-5730d42e6b1c",
            "thirdTaskId": "6890594909",
            "isDebug": false,
            "isTest": false,
            "extData": null,
            "status": 2,
            "message": "success",
            "highRisk": true,
            "riskSummary": "风险洞察存在高风险情况，按照提示信息进行解除",
            "enterNextStage": false,
            "createTime": "2024-09-20 16:24:03",
            "startTime": "2024-09-20 16:24:20",
            "updateTime": "2024-09-20 16:24:39",
            "isDeleted": 0
        },
        {
            "id": 320317,
            "deptId": 27084,
            "subDirection": "百家号",
            "icafeId": "bjhpm-23583",
            "stage": 4,
            "operator": "qep-testone",
            "operationType": 0,
            "agentId": 123,
            "engineTaskId": "3edd2eca-fafa-48eb-aee9-c078c10ad442",
            "thirdTaskId": "6890594789",
            "isDebug": false,
            "isTest": false,
            "extData": null,
            "status": 2,
            "message": "success",
            "highRisk": true,
            "riskSummary": "风险洞察存在高风险情况，按照提示信息进行解除",
            "enterNextStage": false,
            "createTime": "2024-09-20 16:24:02",
            "startTime": "2024-09-20 16:24:19",
            "updateTime": "2024-09-20 16:24:27",
            "isDeleted": 0
        }
    ]
}
```

