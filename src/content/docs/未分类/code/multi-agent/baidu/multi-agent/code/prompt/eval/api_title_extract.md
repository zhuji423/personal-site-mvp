---
title: "api_title_extract"
description: "请从下面的接口文档中提取所有“接口段落的标题”，每个标题通常表示一个对外接口或业务模块功能，例如“商户创建”、“支付回调”、“订单查询”等。 每条返回： - title：接口标题 - titlelinetext：标题原文 - hintlin"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\eval\\api_title_extract.md"
---
请从下面的接口文档中提取所有“接口段落的标题”，每个标题通常表示一个对外接口或业务模块功能，例如“商户创建”、“支付回调”、“订单查询”等。
每条返回：
- title：接口标题
- title_line_text：标题原文
- hint_line_text：紧随其后的接口说明/接口地址关键行

返回格式如下：
```json
返回格式：
[
  {
    "title": "商户创建",
    "title_line_text": "### 商户创建",
    "hint_line_text": "####     3.2.1 功能逻辑&流程图说明"
  },
  ...
]
```

以下是接口文档原文：
{{content}}