---
title: "📄 根据业务线获取绑定的icafe空间信息"
description: "根据业务线获取绑定的icafe空间信息"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 业务线相关\\📄 根据业务线获取绑定的icafe空间信息.md"
---
根据业务线获取绑定的icafe空间信息

## 1、根据业务线获取绑定的icafe空间信息


**接口信息**

> 地址：https://testone.baidu-int.com/api/conf/demandSpace/get
> 方法：POST


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|guyouda|
|token|string|Token |xxxxxx|

**参数**

```
{
    // deptId、subDirection、space不能都为空
    "deptId": 26674  // 产品线ID
    // "subDirection": "工作台"  // 业务方向
    //"space":"youtrack", // icafe空间
    //"cardType":"Story"  // 卡片类型
}
```
**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20260209-server-01-9797-b8bd495ff26c",
    "owner": "wushaoshan",
    "data": [
        {
            "id": 131,
            "deptId": 26674,
            "subDirection": "精准推荐",
            "space": "youtrack",
            "cardType": "Feature",
            "taskType": 1,
            "depDirectionExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"所属计划\",\"containMapping\":[\"精准推荐线上\"],\"direction\":\"26674@精准推荐\"}}",
            "clientExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"标题\",\"validClients\":[\"Android\",\"iOS\",\"Server\",\"Web\",\"FE\"],\"defaultClient\":\"\"}}",
            "versionExtractConf": "{\"MULTI_REGEX\":{\"rules\":[{\"type\":\"VERSION\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\"\"},{\"type\":\"VERSION\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\".0\"},{\"type\":\"CYCLE\",\"field\":\"所属计划\",\"regex\":\"\\\\d+年\\\\d+月\",\"prefix\":\"\",\"postfix\":\"\"}],\"defaultVersion\":{\"type\":\"CYCLE\",\"time\":\"QUARTER\",\"field\":\"创建时间\"}}}",
            "rd": "RD负责人",
            "qa": "QA负责人",
            "devDays": "估算工时",
            "testDays": "",
            "testStartTime": "计划启动测试（QA填）",
            "testFinishTime": "计划测试完成（QA填）",
            "priority": "",
            "isRdTest": "是否免测",
            "submitTestTime": "计划提测日期",
            "otherFieldList": [],
            "creator": "gaolizhe",
            "operator": "",
            "createdTime": "2023-08-16 14:39:29",
            "updateTime": "2025-06-16 21:36:21",
            "isDeleted": 0,
            "onlineTime": "",
            "deliveryType": "{\"defaultDeliveryType\":0,\"fieldConfList\":[{\"propertyName\":\"是否大项目\",\"value\":\"是\",\"deliveryType\":3}]}",
            "deptName": "TestOne@精准推荐"
        },
        {
            "id": 136,
            "deptId": 26674,
            "subDirection": "工作台",
            "space": "youtrack",
            "cardType": "Story",
            "taskType": 1,
            "depDirectionExtractConf": "{\"MULTI_FIELD_RULE\":{\"fieldContain\":[{\"fieldName\":\"所属计划\",\"fieldValue\":[\"TestOne线上\"]}],\"fieldExclude\":[{\"fieldName\":\"是否需要提测\",\"fieldValue\":[\"否\",\"NULL\"]}]}}",
            "clientExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"标题\",\"validClients\":[\"Android\",\"iOS\",\"Server\",\"Web\",\"鸿蒙\"],\"defaultClient\":\"\"}}",
            "versionExtractConf": "{\"MULTI_REGEX\":{\"rules\":[{\"type\":\"VERSION\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\"\"},{\"type\":\"VERSION\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\".0\"},{\"type\":\"CYCLE\",\"field\":\"所属计划\",\"regex\":\"wss测试\",\"prefix\":\"\",\"postfix\":\"\"},{\"type\":\"CYCLE\",\"field\":\"所属计划\",\"regex\":\"\\\\d+年\\\\d+月\",\"prefix\":\"\",\"postfix\":\"\"}],\"defaultVersion\":{\"type\":\"CYCLE\",\"time\":\"QUARTER\",\"field\":\"创建时间\"}}}",
            "rd": "RD负责人",
            "qa": "QA负责人",
            "devDays": "估算工时",
            "testDays": "测试工时（QA填）",
            "testStartTime": "计划启动测试（QA填）",
            "testFinishTime": "计划测试完成（QA填）",
            "priority": "",
            "isRdTest": "是否免测",
            "submitTestTime": "计划提测日期",
            "otherFieldList": [
                "关注人"
            ],
            "creator": "gaolizhe",
            "operator": "wushaoshan",
            "createdTime": "2023-08-16 14:39:29",
            "updateTime": "2025-08-20 13:36:48",
            "isDeleted": 0,
            "onlineTime": "计划上线日期",
            "deliveryType": "{\"defaultDeliveryType\":1,\"fieldConfList\":[{\"propertyName\":\"QA负责人\",\"value\":\"ai_testone\",\"deliveryType\":4}]}",
            "deptName": "TestOne@工作台"
        },
        {
            "id": 310,
            "deptId": 26674,
            "subDirection": "智能交付",
            "space": "megqaend",
            "cardType": "Story",
            "taskType": 1,
            "depDirectionExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"所属计划\",\"containMapping\":[\"智能交付\"],\"direction\":\"26674@智能交付\"}}",
            "clientExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"标题\",\"validClients\":[\"Android\",\"iOS\",\"Server\",\"Web\",\"FE\"],\"defaultClient\":\"Server\"}}",
            "versionExtractConf": "{\"MULTI_REGEX\":{\"rules\":[{\"type\":\"CYCLE\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\\\\.\\\\d+~\\\\d+\\\\.\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\"\"}],\"defaultVersion\":{\"type\":\"CYCLE\",\"time\":\"QUARTER\",\"field\":\"创建时间\"}}}",
            "rd": "负责人",
            "qa": "验收人",
            "devDays": "估算工时",
            "testDays": "实际工时",
            "testStartTime": "开始时间",
            "testFinishTime": "结束时间",
            "priority": "唯一优先级",
            "isRdTest": "",
            "submitTestTime": "开始时间",
            "otherFieldList": [],
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-04-18 19:11:45",
            "updateTime": "2024-05-14 14:59:30",
            "isDeleted": 0,
            "onlineTime": "",
            "deliveryType": null,
            "deptName": "TestOne@智能交付"
        },
        {
            "id": 311,
            "deptId": 26674,
            "subDirection": "智能交付",
            "space": "megqaend",
            "cardType": "Feature",
            "taskType": 1,
            "depDirectionExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"所属计划\",\"containMapping\":[\"智能交付\"],\"direction\":\"26674@智能交付\"}}",
            "clientExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"标题\",\"validClients\":[\"Android\",\"iOS\",\"Server\",\"Web\",\"FE\"],\"defaultClient\":\"Server\"}}",
            "versionExtractConf": "{\"MULTI_REGEX\":{\"rules\":[{\"type\":\"CYCLE\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\\\\.\\\\d+~\\\\d+\\\\.\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\"\"}],\"defaultVersion\":{\"type\":\"CYCLE\",\"time\":\"QUARTER\",\"field\":\"创建时间\"}}}",
            "rd": "负责人",
            "qa": "验收人",
            "devDays": "估算工时",
            "testDays": "",
            "testStartTime": "开始时间",
            "testFinishTime": "结束时间",
            "priority": "唯一优先级",
            "isRdTest": "",
            "submitTestTime": "开始时间",
            "otherFieldList": [],
            "creator": "wushaoshan",
            "operator": "wushaoshan",
            "createdTime": "2024-04-18 19:24:27",
            "updateTime": "2024-10-15 19:49:20",
            "isDeleted": 0,
            "onlineTime": "",
            "deliveryType": null,
            "deptName": "TestOne@智能交付"
        },
        {
            "id": 377,
            "deptId": 26674,
            "subDirection": "工作台",
            "space": "youtrack",
            "cardType": "Feature",
            "taskType": 1,
            "depDirectionExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"所属计划\",\"containMapping\":[\"TestOne线上\"],\"direction\":\"26674@工作台\"}}",
            "clientExtractConf": "{\"FIELD_CONTAIN\":{\"field\":\"标题\",\"validClients\":[\"Android\",\"iOS\",\"Server\",\"Web\",\"鸿蒙\"],\"defaultClient\":\"\"}}",
            "versionExtractConf": "{\"MULTI_REGEX\":{\"rules\":[{\"type\":\"VERSION\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\"\"},{\"type\":\"VERSION\",\"field\":\"所属计划\",\"regex\":\"\\\\d+\\\\.\\\\d+\",\"prefix\":\"\",\"postfix\":\".0\"},{\"type\":\"CYCLE\",\"field\":\"所属计划\",\"regex\":\"wss测试\",\"prefix\":\"\",\"postfix\":\"\"}],\"defaultVersion\":{\"type\":\"CYCLE\",\"time\":\"QUARTER\",\"field\":\"创建时间\"}}}",
            "rd": "RD负责人",
            "qa": "QA负责人",
            "devDays": "估算工时",
            "testDays": "",
            "testStartTime": "计划启动测试（QA填）",
            "testFinishTime": "计划测试完成（QA填）",
            "priority": "",
            "isRdTest": "是否免测",
            "submitTestTime": "计划提测日期",
            "otherFieldList": [],
            "creator": "gaolizhe",
            "operator": "",
            "createdTime": "2024-05-30 10:17:37",
            "updateTime": "2024-11-08 13:15:53",
            "isDeleted": 0,
            "onlineTime": "",
            "deliveryType": null,
            "deptName": "TestOne@工作台"
        }
    ]
}
```
## 
