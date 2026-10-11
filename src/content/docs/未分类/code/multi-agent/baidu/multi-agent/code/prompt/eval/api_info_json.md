---
title: "api_info_json"
description: "你是一个文档结构解析专家，请从以下接口段落中提取接口元信息："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\eval\\api_info_json.md"
---
你是一个文档结构解析专家，请从以下接口段落中提取接口元信息：

【目标输出字段要求】
1. name：接口名称
2. desc：接口详细功能描述描述，从原文中获取（若无则留空）
3. uri：接口地址
4. req_params/resp_params：请求参数/响应参数内容，采用接口文档标准结构，JSON格式
  - 参数内容可能为嵌套格式，使用"properties"展开object内部字段
  - 如果文档中提供了参数注释或者示例，要添加`description`和`example`字段
  - 如果文档中提取不到参数的`description`和`example`，则去除字段，不要臆造
  - 如果是变更接口的变更参数，需要在对应的参数上添加`"change_type":"MODIFIED"`字段；
7. change_type：文档中如果标明了是修改接口填"MODIFIED"，否则默认填 "NEW"
8. 必须按照以下格式输出，必须根据原文进行解析，原文中无法找到的信息留空，不需要补充

【接口原文】
{{chunk}}

【输出格式】
```json
{
  "接口名称": {
    "desc": "新增接口要描述此接口的详细功能逻辑，变更接口需要写清内部逻辑的详细变动点（若无则留空）",
    "uri": "",
    "repo": "接口所在代码库",
    "req_params": {
      "参数名": {
        "type": "string",
        "description": "说明",
        "example": "示例值",
        "required": true, //如果为必填字段则为true，否则不需要此字段
        "change_type": "MODIFIED" //只有变更接口的变更字段为MODIFIED，否则不需要此字段
      },
      "shopId": {
        "type": "integer",
        "description": "商户id",
        "example": 10001,
      },
    },
    "resp_params": {
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
          },
          "companyName": {
            "type": "string",
            "description": "公司名",
          },
        }
      }
    },
    "change_type": "NEW|MODIFIED"
  }
}
```