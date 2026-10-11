---
title: "📄 获取需求卡片各阶段Agent执行结果接口"
description: "获取需求卡片各阶段Agent执行结果接口"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 需求视图\\📄 获取需求卡片各阶段Agent执行结果接口.md"
---
获取需求卡片各阶段Agent执行结果接口

**接口地址：**

https://testone.baidu-int.com/engine/storyAgent/executeResult/getAgentToolResults

**请求类型：**

POST

**Header:**

username: 个人邮箱前缀

token: 个人在TestOne平台Token (获取方式：[https://testone.baidu-int.com/api/getToken](https://testone.baidu-int.com/api/getToken) )

**请求参数：**

|字段|类型|是否必须|含义|示例|
|-|-|-|-|-|
|icafeIdList|list(str)|是|icafe卡片ID列表|["youtrack-975"]|
|stage|int|是|阶段：1: 需求阶段2：开发阶段3：准入阶段4：测试阶段5：准出阶段6：完成阶段7：联调阶段|4|

**参数示例:**

```
{
    "icafeIdList": ["youtrack-975"],
    "stage": 2 
}
```
**示例代码：**

```
import requests
import json

def trigger():
    url = "https://testone.baidu-int.com/engine/storyAgent/executeResult/getAgentToolResults"
    data = {
        "icafeIdList": ["youtrack-975"],
        "stage": 4,
    }
    headers = {
        "username": TESTONE_USERNAME,
        "token": TESTONE_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(url=url, data=json.dumps(data, ensure_ascii=False).encode("utf-8"),
                             headers=headers).json()
    print(response)

```
**返回结果：**

```
{
    "code": 0,
    "msg": "success",
    "requestId": "bef9c32a-3bc5-4d6b-bc5f-12d7b5d78c77",
    "data": [
        {
            "icafeId": "youtrack-1294",
            "agentConf": {                             // agent配置参数
                "id": 14,
                "name": "内部测试Agent-需求测试阶段",
                "description": "测试使用",
                "stage": 4,
                "customStageId": null,
                "url": null,
                "isKirinApi": true,
                "isAsync": false,
                "requestHeader": null,
                "timeout": 60,
                "owner": "guyouda,chenwei57",
                "createTime": null,
                "createUser": null,
                "updateTime": null,
                "updateUser": null,
                "deployTime": null,
                "isDeleted": null,
                "isRelease": null
            },
            "agentExecuteRecord": {                     // agent执行结果
                "id": 338698,
                "deptId": 26674,
                "subDirection": "工作台",
                "icafeId": "youtrack-1294",
                "stage": 4,
                "operator": "qep-testone",
                "operationType": 0,
                "agentId": 14,
                "engineTaskId": "104bf272-fd4e-414a-9b75-eb74b0dbfce8",
                "thirdTaskId": "6911533611",
                "isDebug": false,
                "isTest": false,
                "extData": "",
                "status": 2,
                "message": "success",
                "highRisk": true,
                "riskSummary": "风险洞察存在高风险情况，按照提示信息进行解除",
                "enterNextStage": false,
                "createTime": "2024-09-26 20:10:50",
                "startTime": "2024-09-26 20:10:51",
                "updateTime": "2024-09-26 20:10:53",
                "isDeleted": 0,
                "name": "内部测试Agent-需求测试阶段",
                "description": "测试使用",
                "owner": "guyouda,chenwei57",
                "isKirinApi": true,
                "isAsync": false,
                "timeout": 60
            },
            "agentHintMessage": "",
            "riskSummary": {                               //  高风险的tool集合
                "icafeId": "youtrack-1294",
                "highRisk": true,
                "summary": "风险洞察存在高风险情况，按照提示信息进行解除",
                "highRiskList": [
                    {
                        "toolId": "ff29c2165ba40004401d40dbde8d56d9",
                        "title": "【平台测试】自主测试风险",
                        "summary": "高风险",
                        "message": "如有疑问，请联系工具负责同学 <a href=\"baidu://message?id=GuYouda\"> <img src=\"https://eefe.baidu-int.com/avatars/guyouda\" style=\"width: 18px; height: 18px;border-radius: 50%; vertical-align: middle\"> 顾友达 </a>  确认原因"
                    },
                    {
                        "toolId": "d7e059d9563107353b49901db7bf3c99",
                        "title": "【平台测试】高风险Bug",
                        "summary": " 因为xxxxx，需求高风险",
                        "message": "如有疑问，请联系工具负责同学 <a href=\"baidu://message?id=GuYouda\"> <img src=\"https://eefe.baidu-int.com/avatars/guyouda\" style=\"width: 18px; height: 18px;border-radius: 50%; vertical-align: middle\"> 顾友达 </a>  确认原因"
                    }
                ]
            },
            "toolResults": [                               // 每个tool最新的执行结果集合
                {
                    "id": 800755,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "d26611c5c11c6c2ea78cc93d8b56c48f",
                        "type": 2,
                        "owner": "guyouda,louhanqiong",
                        "name": "内部自测-混合组件Demo",
                        "description": "内部自测-混合组件Demo",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": false,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 107,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": [
                            {
                                "subTitle": "子组件xxx",
                                "componentId": 103,
                                "componentOperateConfig": {
                                    "expand": true,
                                    "enableRefresh": false,
                                    "labelConfig": null
                                },
                                "componentData": "这是一个富文本组件</br> <font color='red'>红色的文字; </font> <font>超链接：</font><a href='https://console.cloud.baidu-int.com' target='_blank'>点我打开</a>"
                            },
                            {
                                "subTitle": "子组件123",
                                "componentId": 100,
                                "componentOperateConfig": {
                                    "expand": true,
                                    "enableRefresh": false,
                                    "labelConfig": null
                                },
                                "componentData": {
                                    "head": [
                                        {
                                            "dataIndex": "kirin_task_id",
                                            "title": "麒麟任务ID",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "type": "TEXT",
                                            "width": 100
                                        },
                                        {
                                            "dataIndex": "engine_task_id",
                                            "title": "引擎任务ID",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "type": "TEXT",
                                            "width": 150
                                        },
                                        {
                                            "dataIndex": "icafe_rich_text",
                                            "title": "富文本",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "type": "RICH_TEXT",
                                            "width": 300
                                        },
                                        {
                                            "dataIndex": "icafe_url_blank",
                                            "title": "超链-新页面",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "type": "URL",
                                            "width": null
                                        },
                                        {
                                            "dataIndex": "icafe_url_popup",
                                            "title": "超链-弹窗",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "type": "URL",
                                            "width": null
                                        }
                                    ],
                                    "body": [
                                        {
                                            "kirin_task_id": 12345,
                                            "engine_task_id": "xxx-xxx",
                                            "icafe_rich_text": "<font color='green'>绿色的文字</font>",
                                            "icafe_url_blank": {
                                                "name": "链接-新页面打开",
                                                "url": "https://console.cloud.baidu-int.com",
                                                "target": "_blank"
                                            },
                                            "icafe_url_popup": {
                                                "name": "链接-浮层打开",
                                                "url": "https://console.cloud.baidu-int.com",
                                                "target": "_popup"
                                            }
                                        },
                                        {
                                            "kirin_task_id": 56789,
                                            "engine_task_id": "yyy-yyy",
                                            "icafe_rich_text": "<font color='red'>红色的文字;  </font> <font>超链接:</font><a href='https://console.cloud.baidu-int.com' target='_blank'>点我打开</a>",
                                            "icafe_url_blank": {
                                                "name": "链接-新页面打开",
                                                "url": "https://console.cloud.baidu-int.com",
                                                "target": "_blank"
                                            },
                                            "icafe_url_popup": {
                                                "name": "链接-浮层打开",
                                                "url": "https://console.cloud.baidu-int.com",
                                                "target": "_popup"
                                            }
                                        }
                                    ],
                                    "pageSize": 5,
                                    "showOptions": false
                                }
                            },
                            {
                                "subTitle": "子组件ahjsgd",
                                "componentId": 101,
                                "componentOperateConfig": {
                                    "expand": false,
                                    "enableRefresh": false,
                                    "labelConfig": null
                                },
                                "componentData": [
                                    "列表1",
                                    "列表2"
                                ]
                            },
                            {
                                "subTitle": "子组件hhhh",
                                "componentId": 105,
                                "componentOperateConfig": {
                                    "expand": true,
                                    "enableRefresh": false,
                                    "labelConfig": null
                                },
                                "componentData": [
                                    {
                                        "name": "链接A",
                                        "url": "https://ku.baidu-int.com/d/NzwrklmOjkeBeQ"
                                    },
                                    {
                                        "name": "链接B",
                                        "url": "https://ku.baidu-int.com/d/NzwrklmOjkeBeQ"
                                    }
                                ]
                            },
                            {
                                "subTitle": "子组件fck",
                                "componentId": 106,
                                "componentOperateConfig": {
                                    "expand": true,
                                    "enableRefresh": false,
                                    "labelConfig": null
                                },
                                "componentData": {
                                    "taskId": 12345,
                                    "highRisk": true,
                                    "riskSummary": "风险概要",
                                    "detail": "风险详情",
                                    "score": 59,
                                    "url": "http://testone.baidu-int.com"
                                }
                            }
                        ]
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:50",
                    "updateTime": "2024-09-26 20:10:50"
                },
                {
                    "id": 800756,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "01b82eb75363e86049b50271214e11dd",
                        "type": 3,
                        "owner": "louhanqiong,guyouda",
                        "name": "QaMate测试用例",
                        "description": "用于支持需求关联QAMate测试用例以及展示关联的测试用例结果",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 1,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 203,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": null
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:50",
                    "updateTime": "2024-09-26 20:10:50"
                },
                {
                    "id": 800757,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "79d1c973c8a0fb160bad40674410153b",
                        "type": 3,
                        "owner": "guyouda",
                        "name": "需求Bug列表",
                        "description": "新增Bug，需求对应的Bug列表",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 1,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 208,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": null
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:50",
                    "updateTime": "2024-09-26 20:10:50"
                },
                {
                    "id": 800758,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "db2d10e9ec391c8682e2ec495962f70e",
                        "type": 3,
                        "owner": "lirui42,wushaoshan",
                        "name": "客户端函数覆盖率",
                        "description": "客户端Android&iOS函数覆盖率工具",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 1,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 202,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": null
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:50",
                    "updateTime": "2024-09-26 20:10:50"
                },
                {
                    "id": 800759,
                    "status": 2,
                    "message": "success",
                    "highRisk": true,
                    "riskSummary": " 因为xxxxx，需求高风险",
                    "toolInfo": {
                        "id": "d7e059d9563107353b49901db7bf3c99",
                        "type": 1,
                        "owner": "guyouda",
                        "name": "【平台测试】高风险Bug",
                        "description": "展示需求相关的高风险Bug列表",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 103,
                        "componentOperateConfig": {
                            "expand": false,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": "\n        需求关联的卡片如下:<br>\n        <table border=\"1\" cellspacing=\"0\" bordercolor=\"gray\">\n        <thead><col style='width: 15%;text-align: center;'>\n            <tr>\n                <th>空间</th>\n                <th>序号</th>\n                <th>链接</th>\n            </tr>\n        </thead>\n        <tbody>\n            \n        </tbody>\n        </table>\n        "
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:51",
                    "updateTime": "2024-09-26 20:10:51"
                },
                {
                    "id": 800760,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "ff834fe511f472304aaa5a74b6607f38",
                        "type": 3,
                        "owner": "guyouda",
                        "name": "iPipe流水线任务",
                        "description": "需求对应的iPipe流水线执行结果",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 1,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 207,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": null
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:51",
                    "updateTime": "2024-09-26 20:10:51"
                },
                {
                    "id": 800761,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "cf7290942ac1e5358e943ab649928622",
                        "type": 3,
                        "owner": "guyouda",
                        "name": "【平台测试】URL内嵌",
                        "description": "测试URL内嵌",
                        "instruction": null,
                        "documentUrl": "https://amis.baidu.com/groups/my?perPage=24&page=1",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 105,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": [
                            {
                                "name": "内嵌页面",
                                "url": "https://console.cloud.baidu-int.com/devops/ipipe/workspaces/175037/pipeline-builds/162456162/view"
                            }
                        ]
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:51",
                    "updateTime": "2024-09-26 20:10:51"
                },
                {
                    "id": 800762,
                    "status": 2,
                    "message": "success",
                    "highRisk": true,
                    "riskSummary": "高风险",
                    "toolInfo": {
                        "id": "ff29c2165ba40004401d40dbde8d56d9",
                        "type": 2,
                        "owner": "guyouda",
                        "name": "【平台测试】自主测试风险",
                        "description": "需求RD自主测试风险识别工具(质量度模型工具)",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 106,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": true,
                            "labelConfig": {
                                "type": "SINGLE_SELECT",
                                "value": {
                                    "right": [],
                                    "wrong": [
                                        "函数已覆盖，第三方平台问题",
                                        "Case已签章，策略问题"
                                    ]
                                }
                            }
                        },
                        "componentData": {
                            "taskId": 6911533611,
                            "highRisk": true,
                            "riskSummary": "高风险",
                            "detail": "\n                    需求<font color='red' style=\"font-weight:bold;\">改动高风险代码模块</font>，\n                    请联系RD讨论回归范围。 如有疑问，请联系 <a href='baidu://message?id=GuYouda'>guyouda \n                    <img src='https://eefe.baidu-int.com/avatars/guyouda' \n                        style='width: 18px; height: 18px; border-radius: 50%; vertical-align: middle'>\n                    </a><br>\n                    改动的高风险代码如下：<br>\n                    <table border=\"1\" cellspacing=\"0\" bordercolor=\"gray\">\n                        <thead><col style='width: 30%;text-align: center;'>\n                            <col style='width: 10%;text-align: center;'>\n                            <col style='width: 10%;text-align: center;'>\n                                <tr>\n                                    <th>代码库</th>\n                                    <th>变更函数</th>\n                                    <th>CR地址</th>\n                                    <th>风险详情</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                            <tr>\n                                <td>baidu/baiduapp-android/search</td>\n                                <td>pay()</td>\n                                <td><a href=\"https://console.cloud.baidu-int.com\">查看详情</a></td>\n                                <td>改动支付模块，请重点关注支付相关逻辑</td>\n                            </tr>\n                            <tr>\n                                <td>baidu/baiduapp-android/video</td>\n                                <td>videoPlay()</td>\n                                <td><a href=\"https://console.cloud.baidu-int.com\">查看详情</a></td>\n                                <td>改动底层播放函数，请重点关注各类型的视频播放效果</td>\n                            </tr>\n                        </tbody>\n                    </table>\t\n            ",
                            "score": 38.8,
                            "url": ""
                        }
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:51",
                    "updateTime": "2024-09-26 20:10:51"
                },
                {
                    "id": 800764,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "质量度模型结果为低风险",
                    "toolInfo": {
                        "id": "43190d1a1e962882652973baf4f978a2",
                        "type": 2,
                        "owner": "shixue01",
                        "name": "自主测试风险分析模型",
                        "description": "需求自主测试风险分析策略（石雪），判断需求是否可以流转为RD自主测试",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 1,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 106,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": {
                            "taskId": 6911533647,
                            "highRisk": false,
                            "riskSummary": "质量度模型结果为低风险",
                            "detail": "命中1条规则，判断为低风险: (1) 实验需求：需求标题命中【实验】<table border='' cellspacing='0' bordercolor='gray'><thead><col style='width: 25%;text-align: center;'><col style='width: 15%;text-align: center;'><col style='width: 45%;text-align: center;'><col style='width: 15%;text-align: center;'><tr><th>特征字段名</th><th>特征的风险贡献分数</th><th>特征名</th><th>原始值</th></tr></thead><tbody></tbody></table>",
                            "score": 0,
                            "url": "http://amis.baidu.com/group/quality_risk_report/index?product_id=26674&relation_id=youtrack-1294&stage=1&relation_type=Story&"
                        }
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:52",
                    "updateTime": "2024-09-26 20:10:52"
                },
                {
                    "id": 800765,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "fea7d4b0e45360c2daf6c2199804ab34",
                        "type": 1,
                        "owner": "louhanqiong",
                        "name": "【平台测试】需求变更代码库",
                        "description": "获取需求变更的代码库以及对应的分支、CR等信息",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 103,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": "\n            需求<font color='red' style=\"font-weight:bold;\">改动高风险代码模块</font>，请联系RD讨论回归范围。 如有疑问，请联系 \n            <a href='baidu://message?id=GuYouda'>guyouda \n                <img src='https://eefe.baidu-int.com/avatars/guyouda' \n                style='width: 18px; height: 18px; border-radius: 50%; vertical-align: middle'>\n            </a><br>\n            改动的高风险代码如下：<br>\n            <table border=\"1\" cellspacing=\"0\" bordercolor=\"gray\"><thead><col style='width: 30%;text-align: center;'><col style='width: 10%;text-align: center;'><col style='width: 10%;text-align: center;'><tr><th>代码库</th><th>变更函数</th><th>CR地址</th><th>风险详情</th></tr></thead>\n        <tbody>\n        <tr><td>baidu/baiduapp-android/search</td><td>pay()</td><td><a href=\"https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_engine/reviews/111119927/files/base...latest/delivery-engine-common/pom.xml\">查看详情</a></td><td>改动支付模块，请重点关注支付相关逻辑</td></tr>\n        <tr><td>baidu/baiduapp-android/video</td><td>videoPlay()</td><td><a href=\"https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_engine/reviews/111119927/files/base...latest/delivery-engine-common/pom.xml\">查看详情</a></td><td>改动底层播放函数，请重点关注各类型的视频播放效果</td></tr>\n        </tbody>\n        </table>\t\n            "
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:52",
                    "updateTime": "2024-09-26 20:10:52"
                },
                {
                    "id": 800766,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "b222c3e5ae18f9b8cb55fba6312baaeb",
                        "type": 1,
                        "owner": "guyouda",
                        "name": "【平台测试】ICafe数据",
                        "description": "获取一些业务自定义的，非平台公共的iCafe卡片字段数据",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 101,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": true,
                            "labelConfig": null
                        },
                        "componentData": [
                            "第一行数据",
                            "第二行数据",
                            "第三行数据"
                        ]
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:52",
                    "updateTime": "2024-09-26 20:10:52"
                },
                {
                    "id": 800767,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "2a7e57307d377520c285306741d449ca",
                        "type": 3,
                        "owner": "guyouda",
                        "name": "【平台测试】表单提交工具",
                        "description": "测试用户自定义下发表单组件，提交能力",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 102,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": {
                            "formList": [
                                {
                                    "name": "xxx",
                                    "displayValue": "文字",
                                    "required": true,
                                    "type": "TEXT",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": 2,
                                    "maxLength": 10,
                                    "defaultValue": "不可修改的文字",
                                    "tip": "不可编辑",
                                    "disabled": true
                                },
                                {
                                    "name": "name",
                                    "displayValue": "文本输入",
                                    "required": true,
                                    "type": "TEXT",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": 2,
                                    "maxLength": 10,
                                    "defaultValue": "",
                                    "tip": "想填啥，你自己说了算，叫什么自己决定",
                                    "disabled": false
                                },
                                {
                                    "name": "age",
                                    "displayValue": "数字输入",
                                    "required": true,
                                    "type": "DIGITAL",
                                    "selectItems": [],
                                    "min": 20,
                                    "max": 100,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": 30,
                                    "tip": "请输入年龄，最小20  最大100",
                                    "disabled": false
                                },
                                {
                                    "name": "gender",
                                    "displayValue": "单选输入",
                                    "required": true,
                                    "type": "SINGLE_SELECT",
                                    "selectItems": [
                                        "男",
                                        "女"
                                    ],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": [
                                        "男"
                                    ],
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "skills",
                                    "displayValue": "多选输入",
                                    "required": true,
                                    "type": "MULTI_SELECT",
                                    "selectItems": [
                                        "Android",
                                        "iOS",
                                        "Web",
                                        "Server"
                                    ],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": [
                                        "Android",
                                        "iOS"
                                    ],
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "languages",
                                    "displayValue": "多选-非必填",
                                    "required": false,
                                    "type": "MULTI_SELECT",
                                    "selectItems": [
                                        "汉语",
                                        "英语",
                                        "日语",
                                        "法语"
                                    ],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": [
                                        "汉语",
                                        "英语"
                                    ],
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "date",
                                    "displayValue": "日期",
                                    "required": true,
                                    "type": "DATE",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": "",
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "datetime",
                                    "displayValue": "时间",
                                    "required": true,
                                    "type": "DATE_TIME",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": "2024-01-01 01:01:01",
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "users",
                                    "displayValue": "用户",
                                    "required": true,
                                    "type": "USER_SELECT",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": [
                                        "guyouda",
                                        "wangshitao"
                                    ],
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "description",
                                    "displayValue": "其他详细描述",
                                    "required": false,
                                    "type": "RICH_TEXT",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": "",
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "codeInfo",
                                    "displayValue": "表格输入",
                                    "required": true,
                                    "type": "TABLE",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": [
                                        {
                                            "text": "默认文本",
                                            "digital": 3.5,
                                            "singleSelect": [],
                                            "multiSelect": []
                                        },
                                        {
                                            "text": "默认文本1",
                                            "digital": 0,
                                            "singleSelect": [
                                                "单选B"
                                            ],
                                            "multiSelect": [
                                                "多选1",
                                                "多选4"
                                            ]
                                        }
                                    ],
                                    "tip": "",
                                    "disabled": false,
                                    "head": [
                                        {
                                            "dataIndex": "text",
                                            "title": "文本",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "edit": true,
                                            "tip": "输入提示",
                                            "width": null,
                                            "type": "TEXT",
                                            "selectItems": []
                                        },
                                        {
                                            "dataIndex": "digital",
                                            "title": "数字",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "edit": true,
                                            "tip": "",
                                            "width": null,
                                            "type": "DIGITAL",
                                            "selectItems": []
                                        },
                                        {
                                            "dataIndex": "singleSelect",
                                            "title": "单选",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "edit": true,
                                            "tip": "",
                                            "width": null,
                                            "type": "SINGLE_SELECT",
                                            "selectItems": [
                                                "单选A",
                                                "单选B",
                                                "单选C"
                                            ]
                                        },
                                        {
                                            "dataIndex": "multiSelect",
                                            "title": "多选",
                                            "copyable": false,
                                            "ellipsis": true,
                                            "edit": true,
                                            "tip": "",
                                            "width": null,
                                            "type": "MULTI_SELECT",
                                            "selectItems": [
                                                "多选1",
                                                "多选2",
                                                "多选3",
                                                "多选4"
                                            ]
                                        }
                                    ],
                                    "addLine": true
                                }
                            ],
                            "strategyId": 30010
                        }
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:52",
                    "updateTime": "2024-09-26 20:10:52"
                },
                {
                    "id": 800768,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "617c2f83ec48f3298e59e4bd12e987d0",
                        "type": 3,
                        "owner": "guyouda",
                        "name": "【平台测试】测试环境部署",
                        "description": "测试环境部署",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 104,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": {
                            "envStrategy": 123,
                            "formList": [
                                {
                                    "name": "name",
                                    "displayValue": "环境名字",
                                    "required": true,
                                    "type": "TEXT",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": "需求xxx的测试环境",
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "envId",
                                    "displayValue": "环境ID(如果填写则复用)",
                                    "required": false,
                                    "type": "DIGITAL",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": null,
                                    "tip": "",
                                    "disabled": false
                                },
                                {
                                    "name": "codeInfo",
                                    "displayValue": "代码信息",
                                    "required": true,
                                    "type": "TABLE",
                                    "selectItems": [],
                                    "min": null,
                                    "max": null,
                                    "minLength": null,
                                    "maxLength": null,
                                    "defaultValue": [
                                        {
                                            "module": "baidu/ep-qa/testone-server1",
                                            "branch": "master",
                                            "pipelineName": null,
                                            "eks": "是"
                                        },
                                        {
                                            "module": "baidu/ep-qa/testone-server2",
                                            "branch": "master2",
                                            "pipelineName": "ChangePipeline",
                                            "eks": "是"
                                        }
                                    ],
                                    "tip": "",
                                    "disabled": false,
                                    "head": [
                                        {
                                            "dataIndex": "module",
                                            "title": "模块",
                                            "copyable": true,
                                            "ellipsis": false,
                                            "edit": true,
                                            "tip": "",
                                            "width": null,
                                            "type": "TEXT",
                                            "selectItems": []
                                        },
                                        {
                                            "dataIndex": "branch",
                                            "title": "分支",
                                            "copyable": true,
                                            "ellipsis": false,
                                            "edit": true,
                                            "tip": "",
                                            "width": null,
                                            "type": "TEXT",
                                            "selectItems": []
                                        },
                                        {
                                            "dataIndex": "pipelineName",
                                            "title": "流水线名称",
                                            "copyable": true,
                                            "ellipsis": false,
                                            "edit": true,
                                            "tip": "",
                                            "width": null,
                                            "type": "TEXT",
                                            "selectItems": []
                                        },
                                        {
                                            "dataIndex": "eks",
                                            "title": "是否使用eks",
                                            "copyable": true,
                                            "ellipsis": true,
                                            "edit": true,
                                            "tip": "",
                                            "width": null,
                                            "type": "SINGLE_SELECT",
                                            "selectItems": [
                                                "是",
                                                "否"
                                            ]
                                        }
                                    ],
                                    "addLine": true
                                }
                            ]
                        }
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:52",
                    "updateTime": "2024-09-26 20:10:52"
                },
                {
                    "id": 800769,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "bb099112caa629c133f3abd54e573664",
                        "type": 3,
                        "owner": "chenlei10,liuquanhong",
                        "name": "回归用例推荐",
                        "description": "匹配代码diff和回归用例录制信息，推荐与代码diff相关的回归用例，用于测试核心功能是否存在异常",
                        "instruction": null,
                        "documentUrl": "",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 1,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 212,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": null
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:52",
                    "updateTime": "2024-09-26 20:10:52"
                },
                {
                    "id": 800770,
                    "status": 2,
                    "message": "success",
                    "highRisk": false,
                    "riskSummary": "",
                    "toolInfo": {
                        "id": "e828962531a9b63025074cf66bcfb62a",
                        "type": 1,
                        "owner": "guyouda",
                        "name": "需求定制信息展示",
                        "description": "用于展示一些平台不支持的业务定制字段",
                        "instruction": null,
                        "documentUrl": "https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/NzwrklmOjkeBeQ",
                        "serviceUrl": "",
                        "isAsync": true,
                        "timeout": 60,
                        "isSelfRunning": false,
                        "createTime": null,
                        "createUser": null,
                        "updateTime": null,
                        "updateUser": null,
                        "isDeleted": null,
                        "isCommon": 0,
                        "deptParamTemplet": null,
                        "deployTime": null
                    },
                    "componentInfo": {
                        "componentId": 100,
                        "componentOperateConfig": {
                            "expand": true,
                            "enableRefresh": false,
                            "labelConfig": null
                        },
                        "componentData": {
                            "head": [
                                {
                                    "dataIndex": "kirin_task_id",
                                    "title": "麒麟任务ID",
                                    "copyable": false,
                                    "ellipsis": true,
                                    "type": "TEXT",
                                    "width": 100
                                },
                                {
                                    "dataIndex": "engine_task_id",
                                    "title": "引擎任务ID",
                                    "copyable": false,
                                    "ellipsis": true,
                                    "type": "TEXT",
                                    "width": 150
                                },
                                {
                                    "dataIndex": "icafe_rich_text",
                                    "title": "富文本",
                                    "copyable": false,
                                    "ellipsis": true,
                                    "type": "RICH_TEXT",
                                    "width": 300
                                },
                                {
                                    "dataIndex": "icafe_url_blank",
                                    "title": "超链-新页面",
                                    "copyable": false,
                                    "ellipsis": true,
                                    "type": "URL",
                                    "width": null
                                },
                                {
                                    "dataIndex": "icafe_url_popup",
                                    "title": "超链-弹窗",
                                    "copyable": false,
                                    "ellipsis": true,
                                    "type": "URL",
                                    "width": null
                                }
                            ],
                            "body": [
                                {
                                    "kirin_task_id": 12345,
                                    "engine_task_id": "xxx-xxx",
                                    "icafe_rich_text": "<font color='green'>绿色的文字</font>",
                                    "icafe_url_blank": {
                                        "name": "链接-新页面打开",
                                        "url": "https://console.cloud.baidu-int.com",
                                        "target": "_blank"
                                    },
                                    "icafe_url_popup": {
                                        "name": "链接-浮层打开",
                                        "url": "https://console.cloud.baidu-int.com",
                                        "target": "_popup"
                                    }
                                },
                                {
                                    "kirin_task_id": 56789,
                                    "engine_task_id": "yyy-yyy",
                                    "icafe_rich_text": "<font color='red'>红色的文字;  </font> <font>超链接：</font><a href='https://console.cloud.baidu-int.com' target='_blank'>点我打开</a>",
                                    "icafe_url_blank": {
                                        "name": "链接-新页面打开",
                                        "url": "https://console.cloud.baidu-int.com",
                                        "target": "_blank"
                                    },
                                    "icafe_url_popup": {
                                        "name": "链接-浮层打开",
                                        "url": "https://console.cloud.baidu-int.com",
                                        "target": "_popup"
                                    }
                                }
                            ],
                            "pageSize": 5,
                            "showOptions": false
                        }
                    },
                    "userLabeledData": {
                        "isCorrect": null,
                        "inputText": null,
                        "selectedItems": null
                    },
                    "createTime": "2024-09-26 20:10:53",
                    "updateTime": "2024-09-26 20:10:53"
                }
            ]
        }
    ]
}
```

