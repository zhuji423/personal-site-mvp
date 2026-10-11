---
title: "ral"
description: "/ DESCRIPTION 测试服务 /"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\haokan\\baidu_haokan-go_hklib\\ral.md"
---
## 涉及到ral第三方下游服务数据获取，需严格按照以下步骤生成：
1. 在指定`conf/ral_conf/ral_env`包路径下进行下游服务配置，其中`test`服务命名需根据需求描述自定义，示例如下：
* 文件路径：`conf/ral_conf/ral_env/test_service.go`
```go
/*
 * Copyright(C) 2025 Baidu Inc. All Rights Reserved.
 * Author: Fall (weizongqun@baidu.com)
 * Date: 2025-04-14
 * File: test_service.go
 */

/*
 * DESCRIPTION
 *   测试服务
 */

package ral_env

const TestService = `
Name = "test_service"
ConnTimeOut     = 200
ReadTimeOut     = 800
WriteTimeOut    = 800
Retry           = 1
Protocol = "http"
Converter = "form"
[Strategy]
Name="LocalityAware"
[Strategy.LocalityAware]
SlidingWindowPeriod = 60

[Resource.BNS]
BNSName = "group.cms-web.SUPERPAGE.cn"
EnableSmartBNS = true
`
```
2. 在指定`client`包路径下，参考补充检索知识生成需求描述涉及到的完整ral下游第三方服务数据操作相关逻辑代码；