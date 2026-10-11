---
title: "📄 获取业务线QA"
description: "地址：https://testone.baidu-int.com/api/qa/getQasByDepts 方法：POST"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 团队日历\\📄 获取业务线QA.md"
---
获取业务线QA

**功能**

> 获取业务线QA


**接口信息**

> 地址：https://testone.baidu-int.com/api/qa/getQasByDepts
> 方法：POST


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|xxxxxx|
|token|string|Token |xxxxxx|



**参数**

> 针对非必填项，不传此字段，表示不限制
|字段|类型|必填|含义|示例|
|-|-|-|-|-|
|deptIds|String|是|部门id及子方向|"222@基础,222@搜索" 或 “222”|
|type|int|否|用户类型：0：正式， 1：外包， 2：实习生，不传次参数，表示全都类型的QA|2|

**参数**

```
{
    "deptIds": "222@基础,222@搜索",
    "type": "2"
}
```


**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20250829-server-01-bcd3-53371f0f6c24",
    "owner": "wushaoshan",
    "data": [
        {
            "id": 2600,
            "username": "lixue46",
            "name": "李雪",
            "type": 2,
            "deptId": 222,
            "subDirection": "搜索",
            "superior": "zhaokairui",
            "takeTest": 1,
            "testClients": [
                "iOS",
                "Android"
            ],
            "isDeleted": 0,
            "superiorInfo": {
                "username": "zhaokairui",
                "name": "赵开瑞",
                "email": "zhaokairui@baidu.com",
                "infoflowAccount": "混子奥运选手",
                "orgChainNameCn": "移动生态事业群组/*/移动生态质量效能部/百度APP与增长质量效能组"
            },
            "qaLabelList": [
                {
                    "id": 464,
                    "type": 2,
                    "typeName": "特性标签",
                    "username": "lixue46",
                    "labelId": 1,
                    "labelName": "Android",
                    "expValue": 11,
                    "expLevel": "理解"
                },
                {
                    "id": 884,
                    "type": 2,
                    "typeName": "特性标签",
                    "username": "lixue46",
                    "labelId": 2,
                    "labelName": "iOS",
                    "expValue": 10,
                    "expLevel": "了解"
                },
                {
                    "id": 847,
                    "type": 2,
                    "typeName": "特性标签",
                    "username": "lixue46",
                    "labelId": 5,
                    "labelName": "Harmony",
                    "expValue": 4,
                    "expLevel": "了解"
                }
            ],
            "secondmentScore": 0.0
        },
        {
            "id": 2884,
            "username": "yuruiping",
            "name": "于蕊萍",
            "type": 2,
            "deptId": 222,
            "subDirection": "基础",
            "superior": "zhangkaili05",
            "takeTest": 1,
            "testClients": [
                "Harmony",
                "iOS",
                "Android"
            ],
            "isDeleted": 0,
            "superiorInfo": {
                "username": "zhangkaili05",
                "name": "张开利",
                "email": "zhangkaili05@baidu.com",
                "infoflowAccount": "karwin955",
                "orgChainNameCn": "移动生态事业群组/*/移动生态质量效能部/百度APP与增长质量效能组"
            },
            "qaLabelList": [
                {
                    "id": 617,
                    "type": 2,
                    "typeName": "特性标签",
                    "username": "yuruiping",
                    "labelId": 1,
                    "labelName": "Android",
                    "expValue": 22,
                    "expLevel": "理解"
                },
                {
                    "id": 1296,
                    "type": 2,
                    "typeName": "特性标签",
                    "username": "yuruiping",
                    "labelId": 2,
                    "labelName": "iOS",
                    "expValue": 8,
                    "expLevel": "了解"
                },
                {
                    "id": 1438,
                    "type": 2,
                    "typeName": "特性标签",
                    "username": "yuruiping",
                    "labelId": 5,
                    "labelName": "Harmony",
                    "expValue": 2,
                    "expLevel": "了解"
                }
            ],
            "secondmentScore": 0.0
        },
        {
            "id": 3131,
            "username": "youjianhao",
            "name": "游剑豪",
            "type": 2,
            "deptId": 222,
            "subDirection": "基础",
            "superior": "wangqing37",
            "takeTest": 1,
            "testClients": [],
            "isDeleted": 0,
            "superiorInfo": {
                "username": "wangqing37",
                "name": "汪清",
                "email": "wangqing37@baidu.com",
                "infoflowAccount": "被看腻的狐狸",
                "orgChainNameCn": "移动生态事业群组/*/移动生态质量效能部/百度APP与增长质量效能组"
            },
            "qaLabelList": [
                {
                    "id": 1874,
                    "type": 2,
                    "typeName": "特性标签",
                    "username": "youjianhao",
                    "labelId": 2,
                    "labelName": "iOS",
                    "expValue": 2,
                    "expLevel": "了解"
                }
            ],
            "secondmentScore": 0.0
        },
        {
            "id": 3133,
            "username": "wangmeng66",
            "name": "王萌",
            "type": 2,
            "deptId": 222,
            "subDirection": "基础",
            "superior": "zhanglu46",
            "takeTest": 1,
            "testClients": [],
            "isDeleted": 0,
            "superiorInfo": {
                "username": "zhanglu46",
                "name": "张璐",
                "email": "zhanglu46@baidu.com",
                "infoflowAccount": "初见rocky",
                "orgChainNameCn": "移动生态事业群组/*/移动生态质量效能部/百度APP与增长质量效能组"
            },
            "qaLabelList": null,
            "secondmentScore": 0.0
        }
    ]
}
```







