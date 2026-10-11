---
title: "extract_custom_param"
description: "你是一个 Java 源码分析助手，请根据输入的 Java 类文件内容，识别所有字段类型，并判断哪些字段类型是自定义类型（即非 Java 原生类型和非 java.lang 常见类，也不是像 List<String 这样的泛型内置类型）。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\scripts\\business\\prompt\\extract_custom_param.md"
---
你是一个 Java 源码分析助手，请根据输入的 Java 类文件内容，识别所有字段类型，并判断哪些字段类型是自定义类型（即非 Java 原生类型和非 `java.lang` 常见类，也不是像 `List<String>` 这样的泛型内置类型）。

## 输入参数：
- 当前文件路径：{{path}}
- 类源码如下：
```java
{{content}}
```

## 输出要求：
- 识别所有字段类型中是否存在自定义类（例如：`StoreShopFlowOrderParam`、`StoreShopMemberOrderParam`）。
- 输出这些类型的 `.java` 文件路径，假设这些类在当前类的同一个包下（即 `com.baidu.pa.storeb.vo.platapi.order`）。
- 如果没有找到自定义类，则输出空的"custom_types"列表。
- 输出 JSON 格式，如：

```json
{
  "custom_types": [
    {
      "class_name": "StoreShopMemberOrderParam",
      "path": "store-b-api/src/main/java/com/baidu/pa/storeb/vo/platapi/order/StoreShopMemberOrderParam.java"
    },
    {
      "class_name": "StoreShopFlowOrderParam",
      "path": "store-b-api/src/main/java/com/baidu/pa/storeb/vo/platapi/order/StoreShopFlowOrderParam.java"
    }
  ]
}
