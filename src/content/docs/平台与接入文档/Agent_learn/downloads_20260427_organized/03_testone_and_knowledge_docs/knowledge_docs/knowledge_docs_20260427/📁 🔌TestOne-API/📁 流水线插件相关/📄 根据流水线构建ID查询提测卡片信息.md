---
title: "📄 根据流水线构建ID查询提测卡片信息"
description: "根据流水线构建ID查询提测卡片信息"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 流水线插件相关\\📄 根据流水线构建ID查询提测卡片信息.md"
---
根据流水线构建ID查询提测卡片信息

**接口信息**

> 地址：https://testone.baidu-int.com/api/submitTestPlugin/getIpipeDataByPipelineBuildId?pipelineBuildId=xxx
> 方法：GET


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|guyouda|
|token|string|Token |xxxxxx|



**参数**

|字段|类型|必填|含义|示例|
|-|-|-|-|-|
|pipelineBuildId|string|是|流水线构建ID|214116976|



**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "20250730-server-00-a683-19e4f5b47d83",
    "owner": "wushaoshan",
    "data": [
        {
            "task": {
                "id": 477404,
                "deptId": 26677,
                "subDirection": "newapp服务端",
                "taskType": 1,
                "taskLabel": "",
                "client": "Web",
                "version": "2025.Q3",
                "customVersion": null,
                "deliveryType": 0,
                "title": "【策略】newapp社区部分二级tab视频资源放开可分发的限制",
                "status": "已上线",
                "icafeId": "newapp-00-18904",
                "icafeCardType": "Story",
                "icafeParentCard": "",
                "icafePlan": "未计划",
                "groupId": 0,
                "rd": "李淑婷",
                "rdValue": "lishuting01",
                "devDays": 2.0,
                "submitTestTime": null,
                "onlineTime": null,
                "qa": "付笑",
                "qaValue": "fuxiao03",
                "testDays": 0.0,
                "testStartTime": null,
                "testFinishTime": null,
                "testType": 2,
                "testReason": "自主测试-人工判断",
                "createdTime": "2025-07-29 14:10:16",
                "creator": "lishuting01",
                "cardCreatedTime": "2025-07-29 14:10:17",
                "cardFirstTestFinishTime": "2025-07-30 14:47:13",
                "updateTime": "2025-07-30 15:41:46",
                "operator": "lishuting01",
                "assignTaskId": 0,
                "assignReason": "",
                "assignDetail": "",
                "secondmentFormId": "",
                "extInfo": "",
                "isDeleted": 0,
                "dimensionStatus": "测试完成",
                "showcaseStatus": "",
                "showcaseRemark": ""
            },
            "taskIpipeData": {
                "id": 9294,
                "deptId": 26677,
                "subDirection": "newapp服务端",
                "taskId": 477404,
                "pluginType": 0,
                "codeModule": "baidu/feed-q/newapp",
                "branch": "newapp_1-0-187_BRANCH",
                "commitId": "f0596190c0bed3f5772b1f08fd1adb5396622a0b",
                "agileWorkspaceId": 406761,
                "agilePipelineId": 2264153,
                "agilePipelineBuildId": 214116976,
                "agileStageBuildId": 517405147,
                "agileJobBuildId": 808324940,
                "agileBuildNumber": 25,
                "ipipeParamData": "{\"AGILE_ICAFE_ISSUE_KEYS\":\"newapp-00-18904\",\"submitTestIcafeIds\":null,\"AGILE_MODULE_NAME\":\"baidu/feed-q/newapp\",\"AGILE_COMPILE_BRANCH\":\"newapp_1-0-187_BRANCH\",\"AGILE_REVISION\":\"f0596190c0bed3f5772b1f08fd1adb5396622a0b\",\"AGILE_WORKSPACE_ID\":406761,\"AGILE_PIPELINE_ID\":2264153,\"AGILE_PIPELINE_BUILD_ID\":214116976,\"AGILE_STAGE_BUILD_ID\":517405147,\"AGILE_PIPELINE_JOB_BUILD_ID\":808324940,\"AGILE_PIPELINE_BUILD_NUMBER\":25,\"AGILE_PIPELINE_JOB_SOURCE\":\"http://console.cloud.baidu-int.com/devops/ipipe/workspaces/406761/pipeline-builds/214116976/stage-builds/517405147/task-builds/808324940/view\",\"AGILE_TRIGGER_USER\":\"lishuting01\",\"AGILE_PRODUCT_HTTP_URL\":\"https://irepo.baidu-int.com/rest/prod/v3/baidu/feed-q/newapp/nodes/84052675/files?access_token=eyJhbGciOiJFUzI1NiIsImtpZCI6Ik5CR0E6VEZaUTpHSFBKOkpRT1E6SEw3WTozM04yOkNIREM6UTNYVjpUSFJFOjZDU0Y6N09BTDpRUkxRIn0.eyJqdGwiOiJmZDQ2Zjc5OC1hMzNlLTRhMWEtOTA1NS0yNmUyMzA0MWNiZDEiLCJpc3MiOiJpcmVwby5iYWlkdS1pbnQuY29tIiwic3ViIjoibGlzaHV0aW5nMDEiLCJpYXQiOjE3NTM4NTc3NDIwNzAsImV4cCI6MTc1Mzg2NDk0MjA3MCwiYXVkIjoicGx1Z2luLWNlbnRlciIsImJucyI6W10sImlwIjpbXSwiYWNjZXNzIjpbeyJ0eXBlIjoibm9kZSIsIm5hbWUiOiJlMWYzZDMzOTBmMGU0YzMwYTM1OTQ4YjFkM2FiMDkzMCIsImFjdGlvbnMiOlsiZG93bmxvYWQiXX0seyJ0eXBlIjoibm9kZSIsIm5hbWUiOiI4NDA1MjY3NSIsImFjdGlvbnMiOlsiZG93bmxvYWQiXX1dfQ.mjs0IOU5bs8-9cIwvBqGYAHtnEkG4C1XY8m2b7Uz0tF-3XxEsLv9Fpl4tCJAoxlsxbglA8NKr7fv-R2yi0MPCQ\",\"AGILE_COVERAGE_PRODUCT_HTTP_URL\":\"\"}",
                "creator": "lishuting01",
                "createdTime": "2025-07-30 14:42:22",
                "updateTime": "2025-07-30 14:42:22"
            }
        }
    ]
}
```

