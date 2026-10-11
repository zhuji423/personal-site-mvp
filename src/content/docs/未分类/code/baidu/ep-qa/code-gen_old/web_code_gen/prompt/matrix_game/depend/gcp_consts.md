---
title: "gcp_consts"
description: "const // TestGcpKey ... TestGcpKey = testPrefix + \"gcpkey\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\gcp_consts.md"
---
### gcp常量定义
* gcp常量定义分为两部分，第一部分为前缀常量定义，第二部分为逻辑相关常量定义
#### gcp前缀常量定义，文件路径：`model/consts/gcp/模块包占位/base.go`
* 此文件生成以下追加内容即可，不要导包，示例如下：
```go
testPrefix = basePrefix + "test_"  // 新接口前缀，`test`对应包名
```
#### gcp逻辑相关常量定义，文件路径：`model/consts/gcp/模块包占位/包名.go`
```go
packagr gcp


const (
    // TestGcpKey ...
    TestGcpKey = testPrefix + "gcp_key" 
)
```