---
title: "📄 根据iCafeId查询流水线信息"
description: "根据iCafeId查询流水线信息"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 流水线插件相关\\📄 根据iCafeId查询流水线信息.md"
---
根据iCafeId查询流水线信息

**接口信息**

> 地址：https://testone.baidu-int.com/api/submitTestPlugin/getIpipeDataByIcafeId?icafeId=xxx
> 方法：GET


**Header**

|字段|类型|含义|示例|
|-|-|-|-|
|username|string|用户名|guyouda|
|token|string|Token |xxxxxx|



**参数**

|字段|类型|必填|含义|示例|
|-|-|-|-|-|
|icafeId|string|是|卡片ID|legal-all-3089|



**返回**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "9f1e16c9-dd1c-462e-b44e-0a92cd02f34c",
    "data": {
        "id": 68,
        "taskId": 124973,
        "codeModule": "baidu/lvlin/c-bff",
        "branch": "c-bff_1-0-137_BRANCH",
        "commitId": "db24d96a690d90d6cbf0bd183a999ca3d0aeed7a",
        "agileWorkspaceId": 393477,
        "agilePipelineId": 1364780,
        "agilePipelineBuildId": 170493978,
        "agileStageBuildId": 418534224,
        "agileJobBuildId": 637015045,
        "agileBuildNumber": 339,
        "ipipeParamData": "{\"AGILE_ICAFE_ISSUE_KEYS\":\"legal-all-3089\",\"AGILE_MODULE_NAME\":\"baidu/lvlin/c-bff\",\"AGILE_COMPILE_BRANCH\":\"c-bff_1-0-137_BRANCH\",\"AGILE_REVISION\":\"db24d96a690d90d6cbf0bd183a999ca3d0aeed7a\",\"AGILE_WORKSPACE_ID\":393477,\"AGILE_PIPELINE_ID\":1364780,\"AGILE_PIPELINE_BUILD_ID\":170493978,\"AGILE_STAGE_BUILD_ID\":418534224,\"AGILE_PIPELINE_JOB_BUILD_ID\":637015045,\"AGILE_PIPELINE_BUILD_NUMBER\":339,\"AGILE_PIPELINE_JOB_SOURCE\":\"http://console.cloud.baidu-int.com/devops/ipipe/workspaces/393477/pipeline-builds/170493978/stage-builds/418534224/task-builds/637015045/view\",\"AGILE_TRIGGER_USER\":\"yihao\"}",
        "creator": "yihao",
        "createdTime": "2024-08-28 12:39:27",
        "updateTime": "2024-08-28 12:39:27"
    }
}
```

