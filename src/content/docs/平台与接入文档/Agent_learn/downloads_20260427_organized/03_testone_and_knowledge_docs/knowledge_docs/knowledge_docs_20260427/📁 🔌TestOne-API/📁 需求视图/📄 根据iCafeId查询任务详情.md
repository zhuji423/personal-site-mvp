---
title: "1、单个需求卡片查询"
description: "根据iCafeId查询任务详情"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 需求视图\\📄 根据iCafeId查询任务详情.md"
---
根据iCafeId查询任务详情

# 1、单个需求卡片查询
**接口信息**

> 地址：https://testone.baidu-int.com/api/task/getTaskByIcafeId?icafeId=xxx
> 方法：GET


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|浏览器打开[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken)链接获取|
|token|string|Token |浏览器打开[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken)链接获取|



**参数**

|字段|类型|必填|含义|示例|
|-|-|-|-|-|
|icafeId|string|是|卡片ID|routine00-22800|



**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "c248348c-2a3f-43ac-aa75-c57ab45175c3",
    "owner": "wushaoshan",
    "data": {
        "id": 165855,
        "deptId": 222,
        "subDirection": "基础",
        "taskType": 1,
        "taskLabel": "",
        "client": "iOS",
        "version": "13.74.0",
        "customVersion": "13.74.0",
        "title": "【iOS】【产品】【用增】主版任务系统户全局计时器能力迭代优化-支持对非金币人群下发",
        "status": "已上车",   // iCafe状态
        "icafeId": "routine00-22800",
        "icafeCardType": "Story",
        "icafeParentCard": "routine00-22158",
        "icafePlan": "随版需求/V13.74版本",
        "groupId": "0",
        "rd": "赵晓昆",
        "rdValue": "zhaoxiaokun01",
        "devDays": 13.0,
        "submitTestTime": "2024-11-04 23:00:00",
        "onlineTime": null,
        "qa": "郝国鼎",
        "qaValue": "v_haoguoding",
        "testDays": 3.0,
        "testStartTime": "2024-11-06 10:00:00",
        "testFinishTime": "2024-11-08 18:00:00",
        "caseIds": "16585645",
        "testType": 0,  // 测试类型：0表示未标识，等于1标识非自主测试，等于2标识自主测试
        "testReason": "", // 测试类型判断原因
        "createdTime": "2024-10-16 14:29:55",
        "cardCreatedTime": "2024-10-16 14:29:55",
        "creator": "zhaoxiaokun01",
        "updateTime": "2024-11-10 12:25:41",
        "operator": "bdmobile",
        "assignTaskId": -7021574464,
        "assignReason": "",
        "assignDetail": "",
        "secondmentFormId": "",
        "extInfo": "",
        "isDeleted": 0,
        "dimensionStatus": "准出通过",  // TestOne状态
        "showcaseStatus": "",
        "showcaseRemark": "",
        "deliveryType": 1,            // 0:需求交付视图，1:集成交付视图，2:联调交付视图，3:自定义交付视图，4:AIQA交付视图
        "customId": null,
        "currentStage": {
            "code": 5,
            "enumName": "SYS_TEST_ACCURACY_STAGE",
            "desc": "测试准出阶段",
            "detail": "测试准出阶段"
        },
        "hostInfo": {
            "versionType": "VERSION",
            "host": "百度APP",
            "hostAppCode": "1",
            "hostVersion": "13.74.0"
        }
    }
}
```
# 2、批量需求卡片查询接口
**接口信息**

> 地址：https://testone.baidu-int.com/api/task/getTaskByIcafeIds?icafeIds=xxx
> 方法：GET


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|浏览器打开[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken)链接获取|
|token|string|Token |浏览器打开[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken)链接获取|



**参数**

|字段|类型|必填|含义|示例|备注|
|-|-|-|-|-|-|
|icafeIds|string|是|卡片ID|routine00-18638,routine00-18624|一次性查询最多100张卡片|



**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20250801-server-02-947e-3ac65e2a7f07",
    "owner": "wushaoshan",
    "data": [
        {
            "id": 29574,
            "deptId": 222,
            "subDirection": "基础",
            "taskType": 1,
            "taskLabel": "",
            "client": "Android",
            "version": "13.53.5",
            "customVersion": null,
            "title": "【Android】收藏历史网页视频更新提醒屏蔽版权库及地域",
            "status": "已上线",
            "icafeId": "routine00-18624",
            "icafeCardType": "Story",
            "icafeParentCard": "routine00-18402",
            "icafePlan": "随版需求/V13.53.5版本",
            "groupId": "0",
            "rd": "党学义",
            "rdValue": "dangxueyi",
            "devDays": 5.0,
            "submitTestTime": "2024-03-12 23:08:08",
            "onlineTime": null,
            "qa": "张广厚,张松涛",
            "qaValue": "v_zhangguanghou,v_zhangsongtao",
            "testDays": 1.0,
            "testStartTime": "2024-03-18 00:00:00",
            "testFinishTime": "2024-03-18 20:00:00",
            "caseIds": "41101",
            "testType": 0,
            "testReason": "",
            "createdTime": "2024-03-07 14:09:55",
            "cardCreatedTime": "2024-03-07 14:09:55",
            "creator": "dangxueyi",
            "updateTime": "2024-10-30 12:03:01",
            "operator": "v_zhangsongtao",
            "assignTaskId": 0,
            "assignReason": "",
            "assignDetail": "",
            "secondmentFormId": "",
            "extInfo": "",
            "isDeleted": 0,
            "dimensionStatus": "准出通过",
            "showcaseStatus": "",
            "showcaseRemark": "",
            "deliveryType": 0,     // 0:需求交付视图，1:集成交付视图，2:联调交付视图，3:自定义交付视图，4:AIQA交付视图
            "customId": null,
            "currentStage": {
                "code": 5,
                "enumName": "SYS_TEST_ACCURACY_STAGE",
                "desc": "测试准出阶段",
                "detail": "测试准出阶段"
            },
            "hostInfo": {
                "versionType": "VERSION",
                "host": "百度APP",
                "hostAppCode": "1",
                "hostVersion": "13.53.5"
            }
        },
        {
            "id": 29983,
            "deptId": 222,
            "subDirection": "基础",
            "taskType": 1,
            "taskLabel": "",
            "client": "Android",
            "version": "13.53.0",
            "customVersion": null,
            "title": "【Android】第三方清单隐私协议链接更新",
            "status": "已上线",
            "icafeId": "routine00-18638",
            "icafeCardType": "Story",
            "icafeParentCard": "routine00-18619",
            "icafePlan": "随版需求/V13.53版本",
            "groupId": "0",
            "rd": "孟凡雷",
            "rdValue": "mengfanlei",
            "devDays": 2.0,
            "submitTestTime": "2024-03-11 20:00:00",
            "onlineTime": null,
            "qa": "吴超",
            "qaValue": "v_wuchao04",
            "testDays": 1.0,
            "testStartTime": null,
            "testFinishTime": null,
            "caseIds": null,
            "testType": 2,
            "testReason": "自主测试-模型判断",
            "createdTime": "2024-03-08 14:38:06",
            "cardCreatedTime": "2024-03-08 14:38:06",
            "creator": "mengfanlei",
            "updateTime": "2024-10-30 12:03:02",
            "operator": "huangdaxin",
            "assignTaskId": 0,
            "assignReason": "",
            "assignDetail": "",
            "secondmentFormId": "",
            "extInfo": "",
            "isDeleted": 0,
            "dimensionStatus": "测试中",
            "showcaseStatus": "",
            "showcaseRemark": "",
            "deliveryType": 0,
            "customId": null,
            "currentStage": {
                "code": 4,
                "enumName": "SYS_TEST_STAGE",
                "desc": "测试阶段",
                "detail": "测试阶段"
            },
            "hostInfo": {
                "versionType": "VERSION",
                "host": "百度APP",
                "hostAppCode": "1",
                "hostVersion": "13.53.0"
            }
        }
    ]
}
```
