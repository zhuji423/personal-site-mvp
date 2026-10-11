---
title: "api_info_str"
description: "你是一个文档结构解析专家，请从以下接口段落中提取接口元信息："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\eval\\prompt\\api_info_str.md"
---
你是一个文档结构解析专家，请从以下接口段落中提取接口元信息：

【目标输出字段】
1. name：接口名称
2. desc：接口详细功能描述描述，从原文中获取（若无则留空）
3. uri：接口地址
4. req_params：请求参数内容，JSON格式
5. resp_params：响应参数内容，采用接口文档标准结构，JSON格式
6. (`req_params`)和(`resp_params`)可能为嵌套格式，参数字段包含（参数类型、示例值、描述），用"|"隔开，如果原文档中包含参数的注释，必须保留注释写在字段中，
8. change_type：文档中如果标明了是修改接口填"MODIFIED"，否则默认填 "NEW"
9. 以上信息必须按照以下格式输出，输出前必须对原文进行解析，原文中无法找到的信息留空，不需要补充

【接口原文】
{{chunk}}

【输出格式】
```json
{
  "name": "接口名",
  "desc": "描述此接口的详细功能逻辑，变更接口需要写清内部逻辑的详细变动点（若无则留空）",
  "uri": "",
  "req_params": {
    "参数名":"类型|示例值|注释",
    "refund": "string|1000|退款金额",
  },
  "resp_params": {},
  "change_type": "NEW|MODIFIED"
}
```

