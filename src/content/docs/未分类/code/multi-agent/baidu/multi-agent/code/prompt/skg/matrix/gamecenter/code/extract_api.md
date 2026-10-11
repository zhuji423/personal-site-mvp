---
title: "extract_api"
description: "你是 go 语言软件开发工程师，需要分析项目中暴露出的接口信息。该项目为 go web 项目，暴露接口信息以类似 Router.go 的方式呈现。现提供路由文件，请分析出该文件中包含的接口信息，以 JSON 形式进行分返回。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\skg\\matrix\\gamecenter\\code\\extract_api.md"
---
你是 go 语言软件开发工程师，需要分析项目中暴露出的接口信息。该项目为 go web 项目，暴露接口信息以类似 Router.go 的方式呈现。现提供路由文件，请分析出该文件中包含的接口信息，以 JSON 形式进行分返回。

提取要求：
* 需求从文件中提取接口功能点及具体的子接口信息，比如提现接口功能，包含提现记录接口、提现接口、重试接口等
* 接口功能点在代码中往往定义了一个 ***Router 对象，子接口使用 ***Router.HandleFunc() 方式进行定义
* 产出的接口功能点的名称为名词形式，可以从注释信息或者包含的子接口信息中归纳出来，样式为 XXX 功能接口
* 产出的子接口的 uri 路径需要为全路径信息，比如接口功能点对应的 uri 为 /withdraw，提现记录接口定义为***Router.HandleFunc("GET,POST", "withdrawRecordApi")，则提现记录接口的 uri 为 /withdraw/withdrawRecordApi
* 存在接口功能点本身就是 api 操作的情况,此时 api_group_api 和 api_operation_uri 内容是一样的

术语描述:
* cb是callback的缩写，表示回调
* cny活动指的是新年活动
* ad是Advertisement的缩写，表示广告

返回格式要求：
```json
[
    {
        "api_group_name": "接口功能点名称",
        "api_group_description": "接口功能描述",
        "api_group_api": "api_group对应的路径，比如/withdraw",
        "api_operations": [
            {
                "api_operation_name": "api 操作的名称",
                "api_operation_description": "api 操作的功能描述信息",
                "api_operation_uri": "api 操作的全路径 uri 信息，比如/withdraw/withdrawRecordApi"
            }
        ]
    }
]
```

请按照上述要求，一步步思考，分析下面的代码，给出最终的结果。

go 代码为：
```go
{{go_router_code}}
```