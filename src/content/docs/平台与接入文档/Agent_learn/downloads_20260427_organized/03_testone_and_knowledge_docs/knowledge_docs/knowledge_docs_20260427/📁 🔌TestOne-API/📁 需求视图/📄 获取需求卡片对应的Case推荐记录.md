---
title: "📄 获取需求卡片对应的Case推荐记录"
description: "获取需求卡片对应的Case推荐记录"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 需求视图\\📄 获取需求卡片对应的Case推荐记录.md"
---
获取需求卡片对应的Case推荐记录

**接口地址：**

https://testone.baidu-int.com/api/testCard/regressCase/getStoryRecommendRecord

**请求类型：**

GET

**Header:**

username: 个人邮箱前缀

token: 个人在TestOne平台Token (获取方式：[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken) )

**请求参数：**

|字段|类型|是否必须|含义|示例|
|-|-|-|-|-|
|icafeId|string|是|iCafe卡片ID|tieba02-13562|

```
curl --location 'https://testone.baidu-int.com/api/testCard/regressCase/getStoryRecommendRecord?icafeId=tieba02-13562' \
--header 'username: YOUR_NAME' \
--header 'token: YOUR_TOKEN'
```
**示例代码：**

```

import requests

def get_result(icafe_id:str):
    url = ("https://testone.baidu-int.com/api/testCard/regressCase/getStoryRecommendRecord"
           "?icafeId={}").format(icafe_id)
    headers = {
        "username": "YOUR_NAME",
        "token": "YOUR_TOKEN",
        "Content-Type": "application/json"
    }

    response = requests.get(url=url, headers=headers).json()
    print(response)

if __name__ == '__main__':
    get_result("tieba02-13562")
```
**返回结果：**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "e24e75f3-e400-4830-957d-378802d59b39",
    "data": [
        {
            "dimensionType": 0,
            "dimensionId": 155526,
            "recommendType": 3,
            "precisionTaskId": 118,      // 精准任务ID
            "precisionTaskStatus": "完成",
            "lazyoneTaskId": -1,
            "precisionTaskCreateTime": "2024-11-25 21:59:46",
            "lazyoneTaskCreateTime": null,
            "os": "Android",
            "precisionTaskUser": "mayongchao",
            "lazyoneTaskUser": null,
            "versionId": 0,
            "precisionTaskMsg": null,
            "spaceId": 8,
            "osType": 0,
            "planId": 3101,
            "regressTaskId": 23544
        },
        {
            "dimensionType": 0,
            "dimensionId": 155526,
            "recommendType": 3,
            "precisionTaskId": 105,    // 精准任务ID
            "precisionTaskStatus": "进行中",
            "lazyoneTaskId": -1,
            "precisionTaskCreateTime": "2024-11-21 15:35:11",
            "lazyoneTaskCreateTime": null,
            "os": "Android",
            "precisionTaskUser": "mayongchao",
            "lazyoneTaskUser": null,
            "versionId": 0,
            "precisionTaskMsg": null,
            "spaceId": 8,
            "osType": 0,
            "planId": 0,
            "regressTaskId": 23368
        }
    ]
}
```




如何根据精准任务ID查询推荐出来的Case详情？

参考：
