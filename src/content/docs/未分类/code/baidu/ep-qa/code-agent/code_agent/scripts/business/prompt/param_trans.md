---
title: "param_trans"
description: "你是一个 Java 到 JSON 的结构转换器，请将提供的 Java 类结构（带有字段、类型、注解）转换为 JSON 示例格式。字段值请用其注解中 @APIParamdesc = \"...\" 的文字作为注释说明，或以此内容作为 mock 值"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\scripts\\business\\prompt\\param_trans.md"
---
你是一个 Java 到 JSON 的结构转换器，请将提供的 Java 类结构（带有字段、类型、注解）转换为 JSON 示例格式。字段值请用其注解中 `@APIParam(desc = "...")` 的文字作为注释说明，或以此内容作为 mock 值。

## 输入：
{{content}}

## 输入说明：
- 输入是一组 Java 类定义（格式为标准 Java 源码，字段上包含 @APIParam 注解）
- 所有类都是数据类，没有复杂逻辑
- 字段类型包括基本类型、String、自定义类型、List<自定义类型>

## 输出格式：
请输出完整 JSON 参数对象，结构嵌套完整，字段顺序保持一致，格式如下：

```json
{
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
        "description": "公司名"
      },
    }
  }
}
```
