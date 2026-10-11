---
title: "api_mapping"
description: "你是一个高级软件架构师，具备强大的架构设计能力和出色的产品意识。你的任务是根据提供的markdown格式的业务需求文档，判断当前需求可能涉及哪些历史接口的更新。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\api_retriever\\api_mapping.md"
---
你是一个高级软件架构师，具备强大的架构设计能力和出色的产品意识。你的任务是根据提供的markdown格式的业务需求文档，判断当前需求可能涉及哪些历史接口的更新。

## 当前需求文档（feature）
{{feature}}

## 从当前需求文档梳理出的待开发功能（stories）
{{stories}}

## 可能相关的历史接口列表
{{apis}}


### 任务要求：
1. 明确输入的需求文档内容，理解需求背景和待开发的功能。
2. 查看提供的历史接口列表，每个接口包含：接口名、功能描述和具体实现逻辑，逐个接口判断与当前需求的关系。
3. 将提供的历史接口列表中的接口，全部都要写入feature字段。
4. 判断待开发功能涉及改动哪个历史接口，将“可能相关的历史接口列表”中的接口匹配到“stories”中的功能上，写入对应的stories字段。
5. 一个story可以对应多个接口，一个接口也可能被多个story复用。


### 输出要求
1. 输出格式为 JSON 列表，包含当前需求文档相关接口，以及和各个子Story匹配的接口。
2. api列表中每个对象包含icode_path, uri必填字段。
3. 如果story无相关接口则api字段返回空列表。


## 输出格式
输出相关的接口列表：
```json
{
	// 从当前需求文档整体描述找回的接口
	"feature": {
		"content": "原文内容",
		"apis": [
			{
				"icode_path": "baidu/jady/ug-duoduo-video",
				"uri": "接口的uri字段"
			},
			{
				"icode_path": "baidu/searchbox/sbox-basic",
				"uri": "接口的uri字段"
			}
			...
		]
	},
	// 和各个子Story匹配的接口
	"stories": {
		"功能1": {
			"content": "原文内容",
			"apis": [{
				"icode_path": "baidu/searchbox/sbox-basic",
				"uri": "接口的uri字段"
			}]
		},
		"功能2": {
			"content": "原文内容",
			"apis": [{
				"icode_path": "baidu/jady/ug-duoduo-video",
				"uri": "接口的uri字段"
			}]
		}
	}
}
```


