---
title: "📄 根据业务线+时间查询走TestOne提测插件的代码库"
description: "根据业务线+时间查询走TestOne提测插件的代码库"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 流水线插件相关\\📄 根据业务线+时间查询走TestOne提测插件的代码库.md"
---
根据业务线+时间查询走TestOne提测插件的代码库

**前提：使用了TestOne流水线提测插件**

**接口信息**

> 地址：https://testone.baidu-int.com/api/submitTestPlugin/getTaskIpipeData
> 方法：POST


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|guyouda|
|token|string|Token |xxxxxx|



**参数**

```
{
    "deptId":551,
    "subDirection":"产研服务端",
    "startDate":"2025-07-12",
    "endDate":"2025-07-13"
}
```


**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20250721-server-02-87e7-bc727892bfdd",
    "owner": "wushaoshan",
    "data": [
        {
            "codeRepo": "baidu/mms-voice/assistant-ui-go",
            "branch": "master",
            "icafeId2IpipeUrl": {
                "AI-search-550": "http://console.cloud.baidu-int.com/devops/ipipe/workspaces/391662/pipeline-builds/211918306/stage-builds/512160810/task-builds/799193983/view"
            }
        },
        {
            "codeRepo": "baidu/ps-se-go/search-uigo",
            "branch": "master",
            "icafeId2IpipeUrl": {
                "U-search-12861": "http://console.cloud.baidu-int.com/devops/ipipe/workspaces/363852/pipeline-builds/211864253/stage-builds/512136729/task-builds/799154455/view"
            }
        }
    ]
}
```

