---
title: "1、使用场景"
description: "API触发创建任务&执行任务"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🤖如流&ducc&skills&沙箱开发接入指南\\📄 API触发创建任务&执行任务.md"
---
API触发创建任务&执行任务

# 1、使用场景
不依赖人工去TestOne平台或者如流主动触发，直接使用API调用的方式和业务的流水线&线上服务等集成起来，实现无缝的自动唤醒AiAgent干活。



# 2、相关接口
## 2.1、创建任务并执行
**请求：**

* taskName: 任务名 （摘要）
* taskTarget: 任务目标，需要让Agent给你干啥 （输入框的query）
* aiWorkerId: 数字员工ID（TestOne平台注册以后可在列表页查看）

```
curl --location 'https://testone.baidu-int.com/aiqa/task/createCommonTask' \
--header 'username: TESTONE_USERNAME' \
--header 'token: TESTONE_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "taskName": "问题xxx排查",
    "taskTarget": "查下这个问题， requestId:20260413-engine-01-9d24-13646e4670eb",
    "aiWorkerId": 37
}'
```


**返回：**

* id: 本次执行记录的ID
* taskIndex: 任务唯一索引，基于此可以得到任务链接 https://testone.baidu-int.com/aiAgent/task?taskIndex={taskIndex}
* thirdTaskId: 调用的自己的Agent返回的一个请求Id, 方便自己基于此排查问题
* timeout： 超时时间

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20260414-engine-00-bfaf-9b1a179bc673",
    "data": {
        "id": 577604,
        "operator": "guyouda",
        "operateType": 1,
        "detail": {
            "description": "查下这个问题， requestId:20260413-engine-01-9d24-13646e4670eb"
        },
        "taskId": "main_6443f924-0944-4620-87c7-dfd032d06eb8",
        "status": 1,
        "debug": false,
        "sugList": [],
        "timeout": "2026-04-14 11:42:33",
        "thirdTaskId": "2e1d7de7764840788d92f3c4a39b2964", 
        "createTime": "2026-04-14 10:42:33",
        "updateTime": "2026-04-14 10:42:33",
        "createUser": "guyouda",
        "updateUser": "qep-testone",
        "taskIndex": "abdea740-d3d6-4fb8-ae31-xxx",
    }
}
```
## 2.2、触发任务继续执行
**请求：**

* taskIndex:  已有任务的taskIndex
* operateType:  query触发，固定为1
* detail: 详细内容
    * description: query具体内容


```
curl --location 'https://testone.baidu-int.com/aiqa/task/executeCommonTask' \
--header 'username: TESTONE_USERNAME' \
--header 'token: TESTONE_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "taskIndex": "abdea740-d3d6-4fb8-ae31-xxxx",
    "operateType": 1,
    "detail": {
        "description": "hello"
    }
}'
```


**返回：**

* id：本次执行记录的ID
* thirdTaskId: 调用的自己的Agent返回的一个请求Id, 方便自己基于此排查问题
* timeout： 超时时间

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20260414-engine-02-8b3a-f9c11575190b",
    "data": {
        "id": 577735,
        "operator": "guyouda",
        "operateType": 1,
        "detail": {
            "description": "hello"
        },
        "taskId": "main_6443f924-0944-4620-87c7-dfd032d06eb8",
        "status": 1,
        "debug": false,
        "sugList": [],
        "timeout": "2026-04-14 12:00:58",
        "thirdTaskId": "444f4ddcf96d408fa0a701d1c8f68714",
        "createTime": "2026-04-14 11:00:58",
        "updateTime": "2026-04-14 11:00:58",
        "createUser": "guyouda",
        "updateUser": "qep-testone"
    }
}
```


## 2.3、获取执行状态
> 由于上述创建或者触发继续执行，都是异步。触发完以后需要知道本次触发什么时候执行完毕（新建/执行中/成功/失败/超时）
**请求：**

* id: 本次执行记录的ID
* operateType:  query触发，固定为1
* detail: 详细内容
    * description: query具体内容


```
curl --location 'https://testone.baidu-int.com/aiqa/task/getByRecordId' \
--header 'username: TESTONE_USERNAME' \
--header 'token: TESTONE_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "id": 577735
}'
```


**返回：**

* id：本次执行记录的ID
* status: 执行状态
    * 0：新建
    * 1：执行中
    * 2：成功
    * 3：失败
    * 4：超时关闭


```
{
    "code": 0,
    "msg": "success",
    "requestId": "20260421-engine-01-aea6-6e1cf47acd7e",
    "data": {
        "id": 577735,
        "operator": "guyouda",
        "operateType": 1,
        "detail": {
            "description": "hello"
        },
        "taskId": "main_6443f924-0944-4620-87c7-dfd032d06eb8",
        "status": 2,
        "debug": false,
        "sugList": [],
        "timeout": "2026-04-14 12:00:58",
        "thirdTaskId": "444f4ddcf96d408fa0a701d1c8f68714",
        "createTime": "2026-04-14 11:00:58",
        "updateTime": "2026-04-14 11:01:12",
        "createUser": "guyouda",
        "updateUser": "qep-testone"
    }
}
```
