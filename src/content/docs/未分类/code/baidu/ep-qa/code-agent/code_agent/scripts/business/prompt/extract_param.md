---
title: "extract_param"
description: "你是一个 Java 接口代码分析器，请根据以下输入完成以下任务："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\scripts\\business\\prompt\\extract_param.md"
---
你是一个 Java 接口代码分析器，请根据以下输入完成以下任务：

## 任务目标：
从输入的 Java 接口源码中，提取指定方法的入参与出参类名，并根据 import 路径生成对应的类文件路径（以 `.java` 结尾）。
项目参数根目录参考：`{{root}}`。

## 输入参数：
- 方法名: {{method_name}}
- java接口源码:
```java
{{content}}
```

## 输出要求：
以 JSON 格式输出如下结构：
{
  "request_class": "com.baidu.pa.storeb.vo.platapi.order.StoreShopOrderRequest",
  "request_path": "store-b-api/src/main/java/com/baidu/pa/storeb/vo/platapi/order/StoreShopOrderRequest.java",
  "response_class": "com.baidu.pa.storeb.vo.platapi.order.StoreShopOrderResponse",
  "response_path": "store-b-api/src/main/java/com/baidu/pa/storeb/vo/platapi/order/StoreShopOrderResponse.java"
}

## 注意：
- 如果返回类型是泛型，如 `CommonSingleResponse<StoreShopOrderResponse>`，请提取尖括号中的类型。
- 方法中可能有多个参数，请定位最后一个自定义类作为请求体（如 `StoreShopOrderRequest request`）。
- 所有路径拼接时需将包名 `com.baidu.xxx` 替换为 `store-b-api/src/main/java/com/baidu/xxx`，并加 `.java` 后缀。