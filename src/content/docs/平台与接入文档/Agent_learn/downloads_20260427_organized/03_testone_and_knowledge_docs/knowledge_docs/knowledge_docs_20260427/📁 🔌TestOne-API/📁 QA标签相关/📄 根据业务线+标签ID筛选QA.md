---
title: "📄 根据业务线+标签ID筛选QA"
description: "根据业务线+标签ID筛选QA"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 QA标签相关\\📄 根据业务线+标签ID筛选QA.md"
---
根据业务线+标签ID筛选QA

**功能**

> 根据业务线+标签ID筛选QA


**接口信息**

> 地址：https://testone.baidu-int.com/api/qa/getQasByDepts
> 方法：POST


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|Content-Type|string||application/json|
|username|string|用户名|xxxxxx|
|token|string|Token |xxxxxx|



**参数**



```
{
    "deptIds": "26674@工作台,26674@智能交付",  // 必填，产品线
    "type": 0,   // 0：正式, 1：外包, 2：实习生 非必填，不填查询全部类型的人员
    "labelIds": [ // 非必填
        0,
        1,
        2
    ]
}
```


**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "ad64efa6-de01-4cb0-90cd-b3d128a0ecee",
    "owner": "wushaoshan",
    "data": [
        {
            "id": 616,
            "username": "wushaoshan",
            "name": "吴绍山",
            "type": 0,
            "deptId": 26674,
            "subDirection": "工作台",
            "superior": "mazhe",
            "takeTest": 1,
            "testClients": [
                "Server",
                "Android"
            ],
            "isDeleted": 0,
            "superiorInfo": {
                "username": "mazhe",
                "name": "马喆",
                "email": "mazhe@baidu.com",
                "infoflowAccount": "mazhe0801",
                "orgChainNameCn": "移动生态事业群组/*/移动生态质量效能部/推荐质量效能组"
            },
            "qaLabelList": [
                {
                    "id": 1,
                    "type": 0,
                    "username": "wushaoshan",
                    "labelId": 1,
                    "labelName": "TestOne平台",
                    "expValue": 200,
                    "expLevel": "运用"
                },
                {
                    "id": 2,
                    "type": 0,
                    "username": "wushaoshan",
                    "labelId": 2,
                    "labelName": "QAMate平台",
                    "expValue": 100,
                    "expLevel": "掌握"
                }
            ],
            "secondmentScore": 0.0
        }
    ]
}
```







