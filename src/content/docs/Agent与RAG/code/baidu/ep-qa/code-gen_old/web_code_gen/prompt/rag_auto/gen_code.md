---
title: "目标任务Query"
description: "{{framecontext}} {{searchcontext}} {{offlinecontext}} {{rulecontext}}"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\gen_code.md"
---
{{frame_context}}
{{search_context}}
{{offline_context}}
{{rule_context}}

## 当前代码库导包格式要求
* 当前代码库：{{repo}}
* 当前代码库导包格式：`icode.baidu.com/{代码库路径}/{文件路径}`，示例如下：
```
import (
    // 其他库导包示例
    "context"
	"time"

	"icode.baidu.com/baidu/gdp/ghttp"
	
	// 当前代码库导包示例
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/service/test.go"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/request.go"
)
```

# 目标任务Query
{{query}}