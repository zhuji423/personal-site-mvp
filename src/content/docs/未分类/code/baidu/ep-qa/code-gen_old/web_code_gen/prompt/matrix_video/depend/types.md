---
title: "types"
description: "// TestFuncResp ... type TestFuncResp struct { TestKey string form:\"testKey\" json:\"testKey\" // 测试key }"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\types.md"
---
### data层数据获取相关结构体定义文件，文件路径：`model/data/types/包名_功能名.go
* 此文件定义结构体及变量，必须一一对应生成注释
* 数据库相关表结构、结构体不要在当前文件定义
```go
package types

// TestFuncResp ...
type TestFuncResp struct {
    TestKey string `form:"testKey" json:"testKey"`  // 测试key
}
```