---
title: "1、背景"
description: "通用知识库API代理接口"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 知识库文档相关\\📄 通用知识库API代理接口.md"
---
通用知识库API代理接口

# 1、背景
知识库的API访问依赖有前提：

* 申请数字员工
* 知识库后台给对应数字员工开通API访问权限
* 提供需要访问对应API的BNS或者IP白名单，仅限给定白名单机器可访问
* 数字员工有对应的知识库/知识本/文档的权限



对于绝大部分业务，满足以上所有要求的成本过大，而且每个业务都需要重复建设，为了降低MEG各业务QA日常交付流程建设中对知识库数据的依赖成本，再此统一提供相关的API代理服务。

* 用户仅需给公共的数字员工  ai_qepku@baidu.com 这个账号加权限以后，就可以访问相关的文档



警告：

* 业务知识库文档严格控制权限，不建议整个知识库加权限。
* 建议将需求相关的文档添加权限即可，非必要情况下不要给管理权限或者编辑权限
* 建议将需求文档放到一个统一的知识本下规范管理，方便权限控制
* **平台会定期统计关注相关接口的访问情况，请按需使用，如有不合理的异常访问，将会进行通报并封禁对应访问用户的相关权限**



# 2、接口信息
```
curl --location 'https://testone.baidu-int.com/api/ku/proxy' \
--header 'username: USERNAME' \
--header 'token: TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "uri": "/v1/doc/queryUserPermission",   // 需要访问的API
    "body": {                               // 对应API的请求参数
        "docGuid": "IItZU3fzkxj3UR",
        "usernames": [
            "guyouda",
            "renxuejian"
        ]
    }
}'

# 返回
{
    "code": 0,
    "msg": "success",
    "requestId": "20251113-server-02-b738-a0b8ed023dfd",
    "owner": "guyouda",
    "data": {               // 知识库API的原始返回，具体数据结构字段含义参考知识库相关API
        "returnCode": 200,
        "returnMessage": "OK",
        "traceId": "643993167685628928",
        "result": {
            "docGuid": "IItZU3fzkxj3UR",
            "permissionDetails": [
                {
                    "username": "guyouda",
                    "canRead": true,
                    "canUpdate": true
                },
                {
                    "username": "renxuejian",
                    "canRead": false,
                    "canUpdate": false
                }
            ]
        }
    }
}
```


# 附
知识库开放API： [知识库开放API](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/HnMHxrpxmXO2Ih?t=mention&mt=doc&dt=doc)
