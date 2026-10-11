---
title: "📄 根据username查询其所在部门信息"
description: "根据username查询其所在部门信息"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 团队日历\\📄 根据username查询其所在部门信息.md"
---
根据username查询其所在部门信息

**功能**

> 根据username查询其所在的部门信息


**接口信息**

> 地址：https://testone.baidu-int.com/api/qa/getQasByNames&names=${names}
> 方法：GET


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|xxxxxx|
|token|string|Token |xxxxxx|



**参数**

> 针对非必填项，不传此字段，表示不限制
|字段|类型|必填|含义|示例|
|-|-|-|-|-|
|names|String|是|用户邮箱前缀|"wushaoshan,guyouda”|



**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20250909-server-01-8a5a-416b346e71ab",
    "owner": "wushaoshan",
    "data": [
        {
            "id": 346,
            "username": "guyouda",
            "name": "顾友达",
            "type": 0,
            "deptId": 26674,
            "subDirection": "工作台",
            "superior": "wushaoshan",
            "takeTest": 0,
            "testClients": [
                "iOS",
                "Android"
            ],
            "isDeleted": 0
        },
        {
            "id": 616,
            "username": "wushaoshan",
            "name": "吴绍山",
            "type": 0,
            "deptId": 26674,
            "subDirection": "工作台",
            "superior": "nieyuxin",
            "takeTest": 1,
            "testClients": [
                "Server",
                "Android"
            ],
            "isDeleted": 0
        },
        {
            "id": 844,
            "username": "wushaoshan",
            "name": "吴绍山",
            "type": 0,
            "deptId": 26674,
            "subDirection": "精准推荐",
            "superior": "gaolizhe",
            "takeTest": 1,
            "testClients": [
                "Server",
                "Android"
            ],
            "isDeleted": 0
        },
        {
            "id": 1265,
            "username": "wushaoshan",
            "name": "吴绍山",
            "type": 0,
            "deptId": 26674,
            "subDirection": "智能交付",
            "superior": "wangshitao",
            "takeTest": 1,
            "testClients": [
                "Android",
                "Server"
            ],
            "isDeleted": 0
        }
    ]
}
```







