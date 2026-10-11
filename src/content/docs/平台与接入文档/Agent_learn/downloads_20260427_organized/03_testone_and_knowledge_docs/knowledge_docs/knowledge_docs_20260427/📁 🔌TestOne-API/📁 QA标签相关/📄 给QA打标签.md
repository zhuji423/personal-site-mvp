---
title: "📄 给QA打标签"
description: "地址：https://testone.baidu-int.com/api/qaLabel/mark 方法：POST"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 QA标签相关\\📄 给QA打标签.md"
---
给QA打标签

**功能**

> 给QA打标签


**接口信息**

> 地址：https://testone.baidu-int.com/api/qaLabel/mark
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
    "username":"wushaoshan", // 多个用户，使用英文逗号分隔
    "labelId":9,
    "labelName":"工作台", // labelName和labelId 二选一，两个都填以labelId为准
    "expValue":1
}
```


**返回**

```
// 成功返回
{
    "code": 0,
    "msg": "success",
    "requestId": "b2337cba-9921-4ba7-b7a8-28cec40fcc55",
    "owner": "wushaoshan",
    "data": true
}

// 参数错误
{
    "code": 400,
    "msg": "参数校验错误: 标签[900]不存在，请检查参数",
    "requestId": "daa56fc1-d67a-44c8-a27f-434d7d0cbba3",
    "owner": "wushaoshan",
    "data": null
}
{
    "code": 400,
    "msg": "校验失败:labelId：labelId不能为空!, ",
    "requestId": "7fa51db7-6775-4cc6-8474-b139f2136b4e",
    "owner": "wushaoshan",
    "data": null
}
```







