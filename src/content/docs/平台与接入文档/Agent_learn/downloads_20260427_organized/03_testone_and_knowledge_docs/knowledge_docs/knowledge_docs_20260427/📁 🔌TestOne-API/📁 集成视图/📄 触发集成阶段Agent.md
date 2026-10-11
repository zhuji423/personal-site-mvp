---
title: "📄 触发集成阶段Agent"
description: "触发集成阶段Agent"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 集成视图\\📄 触发集成阶段Agent.md"
---
触发集成阶段Agent

**接口地址：**

https://testone.baidu-int.com/api/testCard/openApi/triggerIntegratedAgent

**请求类型：**

POST

**Header:**

username: 个人邮箱前缀

token: 个人在TestOne平台Token (获取方式：[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken) )

**请求参数：**

|字段|类型|是否必须|含义|示例|
|-|-|-|-|-|
|deptId|int|是|业务线ID|550|
|subDirection|string|是|子方向|Feed|
|client|string|是|端类型AndroidiOSHarmonyServerWeb|Android|
|version|string|是|版本号|13.76.0|
|stage|int|是|阶段：8: 集成准入9：新需求回归10：集成ET11：核心用例回归12：集成准出|12|

**参数示例:**

```
{
    "deptId": 26674,
    "subDirection": "工作台",
    "stage": 8,
    "client": "Android",
    "version": "14.0.1"
}
```
**示例代码：**

```
import requests
import json

def trigger():
    url = "https://testone.baidu-int.com/api/testCard/openApi/triggerIntegratedAgent"
    data = {
                "deptId": 26674,
                "subDirection": "工作台",
                "stage": 8,
                "client": "Android",
                "version": "14.0.1"
            }
    headers = {
        "username": TESTONE_USERNAME,
        "token": TESTONE_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(url=url, data=json.dumps(data, ensure_ascii=False).encode("utf-8"),
                             headers=headers).json()
    print(response)

```
**返回结果：**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "7fb6738d-c421-4508-ac0f-d3f5b16b4b21",
    "owner": "guyouda",
    "data": {
        "cardIds": "youtrack-1464,youtrack-1465,youtrack-1475,youtrack-1487",
        "stage": 8,
        "dimensionId": 6766,
        "engineTaskId": "39b96855-9844-41ef-b0a4-97c039d4f7d0",
        "agentStatus": 1,  // 触发成功，Agent执行中
        "deptId": 26674,
        "subDirection": "工作台"
    }
}
```

