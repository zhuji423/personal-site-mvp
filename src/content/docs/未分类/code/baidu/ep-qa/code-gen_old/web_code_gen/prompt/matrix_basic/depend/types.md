---
title: "types"
description: "// TestReq 请求体 type TestReq struct { TestId json:\"testId\" form:\"testId\" binding:\"required\" // 测试Id } 接口返回体定义，文件路径：model/"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_basic\\depend\\types.md"
---
## types层结构体定义
### 接口请求体定义，文件路径：`model/types/request/包名.go`
* 此文件中结构体、变量均需要一对一生成对应注释
```go
package request

// TestReq 请求体
type TestReq struct {
	TestId `json:"testId" form:"testId" binding:"required"`  // 测试Id
}
```
### 接口返回体定义，文件路径：`model/types/response/包名.go`
* 此文件中结构体、变量均需要一对一生成对应注释
```go
// TestResp 响应体
type TestResp struct {
	TestData `json:"testData" form:"testData"`  // 测试数据
}
```
### 接口业务逻辑相关结构体定义，文件路径：`model/types/结构体模块名/包名/功能名.go
* 此文件中结构体、变量均需要一对一生成对应注释
```go
package 包名

// TestServiceData 业务数据结构体
type TestServiceData struct {
	TestServiceData `json:"testServiceData" form:"testServiceData"`  // 测试业务数据
}
```