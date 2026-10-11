---
title: "gcp_consts"
description: "const // TestGcpKey 新接口gcp key配置 TestGcpKey = testPrefix + \"gcpkey\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\depend\\gcp_consts.md"
---
### gcp常量定义
* gcp常量定义需要生成两部分，第一部分是前缀常量定义，第二部分是结合前缀常量的gcp逻辑常量定义。
#### gcp前缀常量定义，文件路径：`model/consts/gcp/base.go`
* 此文件追加生成以下内容即可，不要导包，示例如下：
```go
testPrefix = basePrefix + "test_"  // 新接口前缀，`test`对应包名
```
#### 结合前缀常量的gcp逻辑常量定义，文件路径：`model/consts/gcp/包名.go`
```go
packagr gcp


const (
    // TestGcpKey 新接口gcp key配置
    TestGcpKey = testPrefix + "gcp_key" 
)
```