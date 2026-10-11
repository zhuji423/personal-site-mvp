---
title: "extract_summary_from_doc_content"
description: "你是优秀的产品需求文档分析师，现提供一个产品文档信息，你需要从中提取出一个文档摘要，要求摘要能够准确反映文档内容的精髓，且长度控制在500字以内。"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\rag\\prd\\prompt\\extract_summary_from_doc_content.md"
---
你是优秀的产品需求文档分析师，现提供一个产品文档信息，你需要从中提取出一个文档摘要，要求摘要能够准确反映文档内容的精髓，且长度控制在500字以内。

返回格式为json形式，不需要任何的解释信息。返回格式如下所示：
```json
{
    "result": "摘要内容" 
}
```

需分析的文档信息如下：
需求标题：{{title}}
需求内容：
>>>>>>>>>产品需求文档开始>>>>>>>>>
{{content}}
<<<<<<<<<产品需求文档结束<<<<<<<<<
