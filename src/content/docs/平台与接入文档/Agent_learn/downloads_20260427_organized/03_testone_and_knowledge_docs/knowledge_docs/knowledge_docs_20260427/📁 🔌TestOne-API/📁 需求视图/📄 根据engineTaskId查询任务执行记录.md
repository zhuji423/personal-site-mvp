---
title: "1、根据engineTaskId查询需求Agent执行记录"
description: "根据engineTaskId查询任务执行记录"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 需求视图\\📄 根据engineTaskId查询任务执行记录.md"
---
根据engineTaskId查询任务执行记录

# 1、根据engineTaskId查询需求Agent执行记录
**接口地址：**

https://testone.baidu-int.com/engine/storyAgent/getAgentExecuteRecordByEngineTaskId

**请求类型：**

GET

**Header:**

username: 个人邮箱前缀

token: 个人在TestOne平台Token (获取方式：[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken) )

**请求参数：**

|字段|类型|是否必须|含义|示例|
|-|-|-|-|-|
|engineTaskId|string|是|触发Agent调度引擎的任务ID|757af6ee-5db6-4c35-bd6c-f7f52eaaa847|

**示例代码：**

```

import requests

def get_result(engine_task_id:str):
    url = ("https://testone.baidu-int.com/engine/storyAgent/getAgentExecuteRecordByEngineTaskId"
           "?engineTaskId={}").format(engine_task_id)
    headers = {
        "username": "YOUR_NAME",
        "token": "YOUR_TOKEN",
        "Content-Type": "application/json"
    }

    response = requests.get(url=url, headers=headers).json()
    print(response)

if __name__ == '__main__':
    get_result("757af6ee-5db6-4c35-bd6c-f7f52eaaa847")
```
**返回结果：**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "9f158736-19da-4b6b-86ce-d335a53099a7",
    "data": {
        "id": 503766,
        "deptId": 26674,
        "subDirection": "工作台",
        "icafeId": "youtrack-1427",
        "stage": 4,
        "operator": "qep-testone",
        "operationType": 0,
        "agentId": 14,
        "engineTaskId": "757af6ee-5db6-4c35-bd6c-f7f52eaaa847",
        "thirdTaskId": "7067080544",  // 第三方平台(kirin)任务ID
        "isDebug": false,
        "isTest": false,
        "extData": null,
        "status": 2,          // 0: 新建  1:执行中   2:执行成功  3: 执行失败
        "message": "success",
        "highRisk": false,    // 是否高风险
        "riskSummary": "",
        "enterNextStage": false,
        "createTime": "2024-11-19 17:06:48",
        "startTime": "2024-11-19 17:06:49",
        "updateTime": "2024-11-19 17:06:51",
        "isDeleted": 0
    }
}
```

