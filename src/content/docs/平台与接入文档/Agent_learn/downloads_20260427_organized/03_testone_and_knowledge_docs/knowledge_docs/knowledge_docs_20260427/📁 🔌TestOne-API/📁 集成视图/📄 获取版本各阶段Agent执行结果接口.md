---
title: "📄 获取版本各阶段Agent执行结果接口"
description: "获取版本各阶段Agent执行结果接口"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 集成视图\\📄 获取版本各阶段Agent执行结果接口.md"
---
获取版本各阶段Agent执行结果接口

**接口地址：**

https://testone.baidu-int.com/engine/integrationAgent/executeResult/getAgentExecuteResult

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
    "deptId": 550,
    "subDirection": "Feed",
    "stage": 12,
    "client": "Android",
    "version": "13.76.0"
}
```
**示例代码：**

```
import requests
import json

def trigger():
    url = "https://testone.baidu-int.com/engine/integrationAgent/executeResult/getAgentExecuteResults"
    data = {
        "deptId": 550,
        "subDirection": "Feed",
        "stage": 12,
        "client": "Android",
        "version": "13.76.0"
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
    "requestId": "8c8d6981-35bc-4435-8194-779836a523ee",
    "data": {
        "agentConf": {
            "id": 115,
            "name": "百度APP客户端-集成准出阶段",
            "description": "百度APP客户端-集成准出阶段",
            "stage": 12,
            "customStageId": null,
            "url": "http://kirin.baidu-int.com/api/tool/213816",
            "isKirinApi": true,
            "isAsync": true,
            "requestHeader": null,
            "timeout": 600,
            "owner": "wangzhongyang",
            "createTime": null,
            "createUser": null,
            "updateTime": null,
            "updateUser": null,
            "deployTime": null,
            "isDeleted": null,
            "isRelease": null
        },
        "agentExecuteRecord": {
            "id": 27631,
            "deptId": 550,
            "subDirection": "Feed",
            "client": "Android",
            "version": "13.76.0",
            "host": "",
            "hostVersion": "",
            "stage": 12,
            "agentId": 115,
            "engineTaskId": "3af0250b-d249-49f4-b223-6ccc8a4f7ec0",
            "thirdTaskId": "7088769598",
            "operator": "tanzengjie",
            "operationType": 1,
            "icafeIdList": null,
            "isDebug": false,
            "isTest": false,
            "status": 2,
            "message": "success",
            "highRisk": true,
            "riskSummary": "集成后变更函数覆盖率 50% 不符合准出条件，其中变更函数数量 2 覆盖函数数量 1 ; 未完成用例签章, 需签章用例数 1033,已签章或跳过用例数 168, 当前签章比例 17%",
            "enterNextStage": false,
            "createTime": "2024-11-26 15:19:57",
            "updateTime": "2024-11-26 15:20:42",
            "isDeleted": false,
            "name": "百度APP客户端-集成准出阶段",
            "description": "百度APP客户端-集成准出阶段",
            "owner": "wangzhongyang",
            "isKirinApi": true,
            "url": "http://kirin.baidu-int.com/api/tool/213816",
            "isAsync": true,
            "timeout": 600
        },
        "agentHintMessage": "",
        "riskSummary": {
            "highRisk": true,
            "summary": "集成后变更函数覆盖率 50% 不符合准出条件，其中变更函数数量 2 覆盖函数数量 1 ; 未完成用例签章, 需签章用例数 1033,已签章或跳过用例数 168, 当前签章比例 17%",
            "highRiskList": [
                {
                    "toolId": "e46678487b3a46be8e3b510e7004d408",
                    "title": "百度APP客户端-集成准出拦截策略",
                    "summary": "集成后变更函数覆盖率 50% 不符合准出条件，其中变更函数数量 2 覆盖函数数量 1 ; 未完成用例签章, 需签章用例数 1033,已签章或跳过用例数 168, 当前签章比例 17%",
                    "message": "如有疑问，请联系工具负责同学 <a href=\"baidu://message?id=w1210321016\"> <img src=\"https://eefe.baidu-int.com/avatars/wangzhongyang\" style=\"width: 18px; height: 18px;border-radius: 50%; vertical-align: middle\"> 王中阳 </a>  确认原因"
                }
            ]
        },
        "toolResults": [
            {
                "id": 1271784,
                "status": 2,
                "message": "success",
                "engineTaskId": null,
                "highRisk": true,
                "riskSummary": "集成后变更函数覆盖率 50% 不符合准出条件，其中变更函数数量 2 覆盖函数数量 1 ; 未完成用例签章, 需签章用例数 1033,已签章或跳过用例数 168, 当前签章比例 17%",
                "toolInfo": {
                    "id": "e46678487b3a46be8e3b510e7004d408",
                    "type": 4,
                    "owner": "wangzhongyang",
                    "name": "百度APP客户端-集成准出拦截策略",
                    "description": "百度APP客户端-集成准出拦截策略",
                    "instruction": null,
                    "documentUrl": "",
                    "serviceUrl": null,
                    "isAsync": null,
                    "timeout": null,
                    "isSelfRunning": null,
                    "createTime": null,
                    "createUser": null,
                    "updateTime": null,
                    "updateUser": null,
                    "isDeleted": null,
                    "isCommon": 0,
                    "deptParamTemplet": null,
                    "deployTime": null
                },
                "componentInfo": {
                    "componentId": 106,
                    "componentOperateConfig": {
                        "expand": true,
                        "enableRefresh": true,
                        "labelConfig": null
                    },
                    "componentData": {
                        "taskId": 7088769598,
                        "highRisk": true,
                        "riskSummary": "集成后变更函数覆盖率 50% 不符合准出条件，其中变更函数数量 2 覆盖函数数量 1 ; 未完成用例签章, 需签章用例数 1033,已签章或跳过用例数 168, 当前签章比例 17%",
                        "detail": "集成后变更函数覆盖率 50% 不符合准出条件，其中变更函数数量 2 覆盖函数数量 1 ; 未完成用例签章, 需签章用例数 1033,已签章或跳过用例数 168, 当前签章比例 17%",
                        "score": 0,
                        "url": ""
                    }
                },
                "userLabeledData": {
                    "isCorrect": null,
                    "inputText": null,
                    "selectedItems": null
                },
                "createTime": "2024-11-26 15:20:42",
                "updateTime": "2024-11-26 15:20:42"
            }
        ]
    }
}
```

