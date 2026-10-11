---
title: "1、触发接口"
description: "触发需求卡片各阶段Agent接口"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 需求视图\\📄 触发需求卡片各阶段Agent接口.md"
---
触发需求卡片各阶段Agent接口

# 1、触发接口
**接口地址：**

https://testone.baidu-int.com/api/testCard/stageAgent/triggerAgent

**请求类型：**

POST

**Header:**

username: 个人邮箱前缀

token: 个人在TestOne平台Token (获取方式：[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken) )

**请求参数：**

|字段|类型|是否必须|含义|示例|
|-|-|-|-|-|
|icafeId|string|是|icafe卡片ID|youtrack-898|
|stage|int|是|阶段：1：需求阶段2：开发阶段3：准入阶段4：测试阶段5：准出阶段6：完成阶段7：联调阶段|4|
|operator|string|否|如果不指定，默认使用接口header里面的username作为操作人否则以指定的用户作为操作人。|guyouda|
|toolId|string|否|工具IDnull: 全量出发Agent，完整执行其他: 定向执行某一个工具|null|
|extData|anyType|否|扩展参数，类型不限。控制好长度，不超过256||



**参数示例:**

```
{
    "icafeId": "youtrack-898",
    "stage": 4,
}
```


**示例代码：**

```
import requests
import json

def trigger():
    url = "https://testone.baidu-int.com/api/testCard/stageAgent/triggerAgent"
    data = {
        "icafeId": "youtrack-898",
        "stage": 4,
    }
    headers = {
        "username": TESTONE_USERNAME,
        "token": TESTONE_TOKEN,
        "Content-Type":"application/json"
    }

    response = requests.post(url=url, data=json.dumps(data, ensure_ascii=False).encode("utf-8"),
                             headers=headers).json()
    print(response)

```


**返回结果：**

> 关注code字段即可，code=0表示触发成功，其他失败，失败原因参考： msg字段
```
// 触发成功
{
    "code": 0,
    "msg": "success",
    "requestId": "b253e22c-0d77-4ba5-949d-45514d5541b4",
    "data": {
        "cardIds": "youtrack-898",
        "stage": 4,
        "dimensionId": 49212,
        "dimensionType": 0,
        "engineTaskId": "335d932f-5278-4203-aa80-20526337c172",
        "agentStatus": 1,
        "deptId": 26674,
        "subDirection": "工作台"
    }
}
```
常见失败原因：

* 已经超过对应阶段，不允许再触发。

```
{
    "code": 626,
    "msg": "当前状态不允许触发agent 用户: guyouda 在需求视图视图下手动触发了 提测准入阶段的agent, 当前状态为: 待测试, 不允许触发agent! cardIds: youtrack-898",
    "requestId": "a82f122f-3504-447f-a5ab-b22d1de7647c",
    "data": null
}
```
* 卡片不存在

```
{
    "code": 400,
    "msg": "参数校验错误: 卡片暂未接入TestOne平台",
    "requestId": "58e3f438-1850-4499-ab76-382e634c5ae9",
    "data": null
}
```


# 2、如何判断Agent是否执行完成
根据接口返回的 data.engineTaskId字段，调用此接口查询执行结果。

由于Agent执行耗时不一定，如果需要轮询等待Agent执行结果。建议轮询间隔时长不低于  5s

[根据engineTaskId查询任务执行记录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/w6ivGjCkEn3gEf#anchor-8e874ca0-a679-11ef-8065-0dfd28d127d8?t=mention&mt=doc&dt=doc)


