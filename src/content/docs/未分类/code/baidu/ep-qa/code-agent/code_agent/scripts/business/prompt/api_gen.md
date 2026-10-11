---
title: "分析步骤"
description: "你是一个高级开发工程师，你拥有强大的需求拆解能力和技术设计能力。请根据以下需求文档和历史接口信息，进行接口变更分析并输出详细设计。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\scripts\\business\\prompt\\api_gen.md"
---

你是一个高级开发工程师，你拥有强大的需求拆解能力和技术设计能力。请根据以下需求文档和历史接口信息，进行接口变更分析并输出详细设计。

# 分析步骤
1. 拆解出为了实现需求文档中的功能所需要的接口
2. 对比需求文档与历史接口（如果有）的差异，本次需求可能涉及变更相关的历史接口，也可能不涉及
3. 识别需要修改的已有历史接口（内部逻辑变更/出入参变更），内部逻辑变更需要在(`api_desc`)中详细说明，出入参变更需要在对应字段的value中说明
4. 识别需要新增的接口，并分析出新增接口的功能逻辑、路由、请求参数和响应参数
5. 以上步骤处理完成后，需要反思是否有遗漏修改/新增的接口，或者遗漏的请求参数和响应参数。如果存在遗漏的情况，需要进行补充


# 历史接口信息
{{history_api}}

# 本次升级需求
{{mrd}}

# 本次升级需求梳理出的待开发功能
{{mrd_core}}


# 当前应用
store-b

# 输出字段要求
1. (`api_desc`)为接口功能的详细描述，新增功能需要描述此接口的详细逻辑，变更接口需要写清内部逻辑的详细变动点，可以按照点展开
2. 
3. (`uri`)
4. (`req_params`)为请求参数的详细内容，key值为请求参数名，value值包含三个信息（参数类型、示例值、变更类型）。
5. (`resp_params`)为响应参数的详细内容，key值为响应参数名，value值包含三个信息（参数类型、示例值、变更类型）

  - 如果是变更接口的变更参数，需要在对应的参数上添加`"change_type":"MODIFIED"`字段；
6. (`req_params`)和(`resp_params`)可能为嵌套格式
7. 请求参数和响应参数应当遵循驼峰命名法
8. 要求严格按照{输出格式}的JSON格式输出



【目标输出字段要求】
1. 接口名称使用自然语言命名
2. desc：新增功能需要描述此接口的详细逻辑，变更接口需要写清内部逻辑的详细变动点，可以按照点展开
3. repo：目标代码库
4. uri：接口地址，接口路由格式为：{应用名}/{请求方法}/{服务名}/{函数名}，例如/store-b/GET/StoreMemberService/getMemberCategoryList
5. req_params/resp_params：请求参数/响应参数内容，参数名应当遵循驼峰命名法，采用接口文档标准结构
  - 参数内容可能为嵌套格式，使用"properties"展开object内部字段
  - 如果文档中提供了参数注释或者示例，要添加`description`和`example`字段
  - 如果文档中提取不到参数的`description`和`example`，则去除字段，不要臆造
  - 如果是变更接口的变更参数，需要在对应的参数上添加`"change_type":"MODIFIED"`字段；
6. change_type：如果识别出需要修改的已有历史接口，则将对应接口的(`change_type`)赋值为"MODIFIED"。识别出需要新增接口，则将(`change_type`)赋值为"NEW"
7. 必须按照以下格式输出，必须根据原文进行解析，原文中无法找到的信息留空，不需要补充

# 输出格式
```json
{
    "接口名": {
        "desc": "新增功能需要描述此接口的详细功能逻辑",
        "change_type": "NEW",
        "uri":"接口路由",
        "req_params": {
            "参数名": {
                "type": "string",
                "description": "说明",
                "example": "示例值",
            },
            "shopId": {
                "type": "integer",
                "description": "商户id",
                "example": 10001,
            },
        },
        "resp_params": {
        }
    },
    "接口名2": {
        "desc": "变更接口需要写清内部逻辑的详细变动点",
        "change_type": "MODIFIED",
        "uri":"接口路由",
        "req_params": {
            "参数名": {
                "type": "string",
                "description": "说明",
                "example": "示例值",
            },
            "infoSourceVo": {
                "type": "object",
                "properties": {
                    "licenseTimeFLag": {
                        "type": "integer",
                        "example":1,
                        "description":"是否展示许可证时间",
                        "change_type":"NEW"
                    },
                    "companyName": {
                        "type": "string",
                        "description": "公司名",
                        "change_type":"UNCHANGED"
                    },
                }
            }
        },
        "resp_params": {
            "参数名": {
                "type": "string",
                "description": "说明",
                "example": "示例值",
            }
        }
    }
}
```