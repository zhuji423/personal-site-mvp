---
title: "types"
description: "// data层数据结构体，示例如下： // TestData ... type TestData struct { TestName string json:\"testName\" // 测试名称 }"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\depend\\types.md"
---
## types层构体定义
### 业务逻辑相关结构体定义，文件路径：`model/types/dto/包名.go`
```go

// data层数据结构体，示例如下：
// TestData ...
type TestData struct {
    TestName string `json:"testName"`  // 测试名称
}

// redis数据结构体，示例如下：
// TestRedisData ...
type TestRedisData struct {
    TestID string `json:"testId"`  // 测试id
}

// gcp数据结构体，示例如下：
// TestGcpData ...
type TestGcpData struct {
    TestType string `json:"testType"`  // 测试类型
}
```
### 业务逻辑请求体定义，文件路径：`model/types/request/personal.go`
```go
// 请求体，示例如下：
// TestReq ...
type TestReq struct {
    TestID string `json:"testId" form:"testId" binding:"required"`  // 测试id
}
```
### 业务逻辑响应体定义，文件路径：`model/types/response/personal.go`
```go
// 响应体，示例如下：
// TestResp ...
type TestResp struct {
    TestName string `json:"testName"`  // 测试名称
}
```