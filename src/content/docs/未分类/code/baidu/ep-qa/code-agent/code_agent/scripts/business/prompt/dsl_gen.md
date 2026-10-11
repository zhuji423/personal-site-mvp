---
title: "任务要求"
description: "你是一个资深工程师，你可以将json输入格式转化为markdown输出格式，请将接口任务中的json内容转化为markdown格式。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\scripts\\business\\prompt\\dsl_gen.md"
---
你是一个资深工程师，你可以将json输入格式转化为markdown输出格式，请将接口任务中的json内容转化为markdown格式。

# 任务要求
1. 将{需求背景}中的内容直接填写项目背景中
2. 根据(`change_type`)判断是新增接口还是变更接口，MODIFIED为变更接口，NEW为新增接口。
3. 转化方式请参考json输入格式示例和markdown输出格式
4. 严格按照markdown输出格式输出，不要输出其他无关内容（如思考步骤）


# json输入格式示例
{
    "接口功能1": {
        "api_desc": "新增功能需要描述此接口的详细功能逻辑，变更接口需要写清内部逻辑的详细变动点",
        "change_type": "MODIFIED",
        "uri":"store-b/GET/StoreShopMemberNewService/getCategoryList",
        "req_params": {
            "参数名":"类型|示例值|参数变更类型，取NEW或者UNCHANGED",
            "contactPhone": "string|15601193391|UNCHANGED",
            "ucId": "integer|53892|NEW"
        },
        "resp_params": {
            "返回参数名1":"类型|示例值|参数变更类型，取NEW或者UNCHANGED",
            "ucName": "string|uc账户名|NEW",
            "passId": "integer|12345|UNCHANGED"
        }
    },
    "接口功能2": {
        "api_desc": "新增功能需要描述此接口的详细功能逻辑，变更接口需要写清内部逻辑的详细变动点",
        "change_type": "NEW",
        "uri":"store-b/GET/StoreShopMemberNewService/getShopList",
        "req_params": {
            "参数名":"类型|示例值|参数变更类型，取NEW或者UNCHANGED",
            "infoSourceVo": {
                "licenseTimeFLag": "integer|1|UNCHANGED",
                "companyName": "string|公司名|UNCHANGED"
            },
            "ucName": "string|uc账户名|Name"
        },
        "resp_params": {
            "返回参数名1":"类型|示例值|参数变更类型，取NEW或者UNCHANGED",
            "memberOrderList": {
                "type": "list<VO>",
                "VO": {
                    "orderType": "integer|1|UNCHANGED",
                    "address": "string|地址|New"
                }
            }
        }
    }
}

# markdown输出格式
## 1. 项目背景
此处填写{需求背景}中的内容

## 2. 总体设计
这个章节阐述功能的整体设计，说明对系统各个部分的修改，主要参考{需求待开发功能的整体说明}。

## 3. 详细设计
###  3.1 接口名称
####    3.1.1 功能逻辑
    此处填写新增接口功能2的api_desc
####     3.1.2 对外接口说明
*接口地址*
store-b/GET/StoreShopMemberNewService/getShopList

*请求参数* 
```json
{
	"infoSourceVo": {
		"licenseTimeFLag": "integer|1|UNCHANGED",
		"companyName": "string|公司名|UNCHANGED"
	},
	"ucName": "string|uc账户名|Name"
}
```
*接口返回*
```json
{
	"memberOrderList": {
		"type": "list<VO>",
		"VO": {
			"orderType": "integer|1|UNCHANGED",
			"address": "string|地址|New"
		}
	}
}
```
####     3.1.3 数据结构说明（可选）
    说明在该模块中涉及到的核心数据结构的核心内容（可以以文字描述或代码的方式给出），并进行必要说明 
        主要包括：1）表名；2）描述；3）表结构（如果是新表，需着重介绍主键，索引，各个字段的类型，以及说明；若是修改已有表，需着重描述改动的表结构和含义）；4）如果涉及的刷库或刷数据，明确出来

###  3.2 变更接口
####     3.2.1 功能逻辑
         此处填写变更接口功能1的desc
####     3.2.2 对外接口说明
*接口地址*
store-b/GET/StoreShopMemberNewService/getCategoryList|

*请求参数* 
```json
{
	"contactPhone": "string|15601193391|UNCHANGED",
	"ucId": "integer|53892|NEW"
}
```

*接口返回*
```json
{
	"ucName": "string|uc账户名|NEW",
	"passId": "integer|12345|UNCHANGED"
}
```

# 需求背景
{{bg}}

# 需求待开发功能的整体说明
{{req}}

# 接口任务
{{api}}