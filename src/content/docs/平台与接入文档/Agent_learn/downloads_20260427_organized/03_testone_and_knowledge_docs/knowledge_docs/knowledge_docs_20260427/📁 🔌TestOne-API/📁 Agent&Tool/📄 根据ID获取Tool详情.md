---
title: "!/usr/bin/python3"
description: "根据ID获取Tool详情"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 Agent&Tool\\📄 根据ID获取Tool详情.md"
---
根据ID获取Tool详情

**功能**

> 查询业务需求卡片列表


**接口信息**

> 地址：https://testone.baidu-int.com/engine/storyAgent/getToolById
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
|id|string|是|Tool Id|ace343da7e82947d1f481f76fe3a986b|

```
curl --location 'https://testone.baidu-int.com/engine/storyAgent/getToolById' \
--header 'username: YOUR_NAME' \
--header 'token: YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "id":"ace343da7e82947d1f481f76fe3a986b"
}'
```
```
# !/usr/bin/python3

# -*- coding: utf-8 -*-

"""
@author: GuYouda
@date:   2024/11/20
@desc:   
"""
import json

import requests


def sample():
    url = "https://testone.baidu-int.com/engine/storyAgent/getToolById"
    headers = {
        'username': YOUR_NAME,
        'token': YOUR_TOKEN,
        'Content-Type': 'application/json'
    }

    data = {
        "id": "ace343da7e82947d1f481f76fe3a986b"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.text)


if __name__ == '__main__':
    sample()

```


**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "18ac4dde-6303-4346-9fab-40a8710dc6b3",
    "data": {
        "id": "ace343da7e82947d1f481f76fe3a986b",
        "type": 3,
        "owner": "chenlei10,liuquanhong,qiaohuanyu",
        "name": "QAMate-脑图用例工具",
        "description": "使用AI生成技术，实现迭代需求的脑图用例自动化生成，并提供用例的签章、签章数据查询功能，给业务准出提供数据支撑",
        "instruction": "<p><span style=\"color: rgb(28, 29, 31);\">from qep_delivery_tools import BrainCaseGenerateTool</span></p><p><span style=\"color: rgb(28, 29, 31);\">tool = BrainCaseGenerateTool(ak, sk, case_info, generation, callback, sign)</span></p><p>tool_result = tool.execute(self.parameter)</p>",
        "documentUrl": "",
        "serviceUrl": "",
        "isAsync": true,
        "timeout": 60,
        "isSelfRunning": false,
        "createTime": "2024-05-22 11:14:56",
        "createUser": "louhanqiong",
        "updateTime": "2024-06-11 16:47:14",
        "updateUser": "louhanqiong",
        "isDeleted": 0,
        "isCommon": 1,
        "deptParamTemplet": null,
        "deployTime": "2024-09-10 19:39:38"
    }
}
```







