---
title: "param_target_mapping"
description: "你是一个接口参数结构比对分析器，请对以下生成接口和目标接口的参数结构进行逐字段的匹配与准确性评估："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\eval\\prompt\\param_target_mapping.md"
---
你是一个接口参数结构比对分析器，请对以下生成接口和目标接口的参数结构进行逐字段的匹配与准确性评估：

### 目标任务：
请对 生成接口参数 与 目标接口参数 进行结构化字段对比，考虑嵌套的字段结构，输出以下内容：
1. request_matching: 生成的接口请求参数和目标接口请求参数的字段对齐情况
2. response_matching: 生成的接口响应参数和目标接口响应参数的字段对齐情况

## 字段对齐结果：
1. generated_field: 生成的接口字段
2. target_field: 目标接口字段
3. match_type: 匹配的类型，包括以下几种类型：
  - exact: 字段完全匹配
  - partial: 字段名称不同或者嵌套结构不同，但是字段的含义和类型一致(Id类型的字段要求不能混淆)；
  - missing: 缺失字段，生成接口中没有的字段
  - extra: 多余字段，目标接口中没有的字段

### 输入格式：
输入为标准的openapi参数格式
- 生成的接口列表：
<<<GENERATED>>>
{{generated}}
<<<END>>>

- 目标接口列表：
<<<TARGET>>>
{{target}}
<<<END>>>


## 输出格式
```json
{
  "request_matching":[
    {
      "generated_field": "shopId",
      "target_field": "shopId",
      "match_type": "exact" // 可为 exact | partial | missing | extra
    },
    {
      "generated_field": "companyInfo",
      "target_field": "companyVo",
      "match_type": "partial"
    }
],
"response_matching":[
    {
      "generated_field": "shopId",
      "target_field": "shopId",
      "match_type": "exact" // 可为 exact | partial | missing | extra
    },
    {
      "generated_field": "companyInfo",
      "target_field": "companyVo",
      "match_type": "partial"
    }
]
}
```