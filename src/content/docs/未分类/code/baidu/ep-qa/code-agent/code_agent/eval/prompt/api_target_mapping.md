---
title: "api_target_mapping"
description: "你是一个接口映射与自动评估系统，请根据下述要求，完成接口匹配（mapping）和指标评估任务："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\eval\\prompt\\api_target_mapping.md"
---
你是一个接口映射与自动评估系统，请根据下述要求，完成接口匹配（mapping）和指标评估任务：

### 目标任务：
1. 将“生成的接口列表”中的每个接口匹配到“目标接口列表”中的一个或多个接口。
2. 每个匹配需基于以下内容进行判断：
   - 接口路径（uri）：如果是新增接口 (接口的`change_type`为`NEW`)，uri不完全一致时，含义一致也可以匹配，需要进一步考察接口功能；如果是变更接口(接口的`change_type`为`MODIFIED`) ，要求生成的uri和目标uri必须完全一致，否则不能匹配。
   - 接口名/接口功能描述（desc）：接口实现的功能需要一致；多个接口可能在target中合并实现或者拆分实现，但是如果和目标接口只有小部分功能重合，则不能匹配。
3. 输出的mapping中，每个匹配要包含以下字段
   - generated_api: 生成的接口名，列表格式，要与原文中的接口名一致
   - target_api: 目标接口名，列表格式，要与原文中的接口名一致
   - confidence: 匹配的置信度（0~1之间的小数，1为完全一致，0为完全不一致，小于0.5则认为匹配不成功）


### 输入格式：
- 生成的接口列表：
<<<GENERATED>>>
{{generated}}
<<<END>>>

- 目标接口列表：
<<<TARGET>>>
{{target}}
<<<END>>>

### 输出格式：
```json
{
  "mapping": [
    {
      "generated_api": ["商户创建&修改"],
      "target_api": ["商户创建", "商户信息修改"],
      "confidence": 0.95
    },
    {
      "generated_api": ["商户详情查询"],
      "target_api": ["查看商户详情"],
      "confidence": 0.9
    }
  ],
  "notes": [
    "有部分生成接口未在目标中找到对应（如：3.1 登录接口为新增功能）",
    "部分目标接口为通用拆分目标，由多个生成接口合并实现（如商户创建/更新合并为 saveOrUpdateMerchant）"
  ]
}
