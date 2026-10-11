---
title: "service_types"
description: "// TestRes ... type TestRes struct { // 账户类型 TestAccountType string json:\"testAccountType\" }"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\service_types.md"
---
#### 框架&service层用到的结构体、常量等，文件路径：`service/包名/types/功能名.go`
* 结构体命名为大驼峰，对应变量定义格式为：大驼峰 变量类型 `json:"小驼峰" form:"小驼峰" 
* 注意结构体、常量定义均需生成对应注释
```go
// TestReq ...
type TestReq struct {
    // 成员变量注释示例：测试ID
    TestID   int    `json:"testID" form:"testID" binding:"required"`
}

// TestRes ...
type TestRes struct {
    // 账户类型
    TestAccountType       string       `json:"testAccountType"`
}
```