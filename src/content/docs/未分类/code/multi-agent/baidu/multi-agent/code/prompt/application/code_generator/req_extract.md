---
title: "req_extract"
description: "你是一名资深后端研发工程师，请根据给出的需求文档，提取出相关的标题"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\req_extract.md"
---
你是一名资深后端研发工程师，请根据给出的需求文档，提取出相关的标题

<Requirements Document>
{{trd_content}}
</Requirements Document>

返回格式参考（内容根据实际需求替换）：
```json
[
    "需求背景",
    "改动点",
    "XX状态查询接口（修改）",
    "XX奖励发放接口（修改）",
    "/baiduboxapp/ug-gamecenter/sdk/user/login",
    "数据库设计"
]
```

要求：
1. 分析文档中涉及**{{icode_path}}**代码库的内容标题，返回对应的标题
2. 只关注对应代码库的子章节，包括
    - 接口设计详情中并没有涉及**{{icode_path}}**下的接口
    - 存储设计下的相关内容章节
3. 只返回标题名称列表，请保持原样，便于后续的使用正则匹配提取文本段落