---
title: "types"
description: "// TestReq 测试请求体 type TestReq struct { TestType string json:\"testType\" form:\"testType\" binding:\"required\" // 测试类型 } 响应结构"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\types.md"
---
## 结构体定义
* 结构体及变量定义均需根据需求生成对应注释
### 请求结构体定义，文件路径：`model/types/模块包占位/request/接口路径占位/功能名.go`
* 此文件结构体、变量等必须生成注释
```go
package 包名or子包名


// TestReq 测试请求体
type TestReq struct {
    TestType  string `json:"testType" form:"testType" binding:"required"`  // 测试类型
}
```
### 响应结构体定义，文件路径：`model/types/模块包占位/response/接口路径占位/功能名.go`
* 此文件结构体、变量等必须生成注释
```go
package 包名or子包名

// TestResp 测试响应体
type TestResp struct {
    ExistData *ExistData `json:"existData"`  // 现有数据
    NewData  *NewData  `json:"newData"`   // 新数据
}


// ExistData 现有数据结构
type ExistData struct {
    TestUID   int64  `json:"testUId"`       // 测试UID
    TestUser string `json:"testUser"`    // 测试用户名称
}

// NewData 新数据结构
type NewData struct {
    TestPID   int64  `json:"testPId"`       // 测试PID
    TestName string `json:"testName"`    // 测试名称
}
```
### 业务逻辑框架相关结构体定义，文件路径：`model/types/模块包占位/游戏模块名/接口路径占位/功能名.go`
* 特别注意，数据库表相关结构体不要在此文件定义，在dao层中已经完成了定义
* 此文件结构体、变量等必须生成注释
```go
package 包名or子包名

// TestParams 测试函数参数结构体
type TestParams struct {
    TestUID   int64  `json:"testUId"`       // 测试UID
    TestType string `json:"testType"`    // 测试类型
}

// TestData service层测试函数返回结构体
type TestData struct {
    TestParam string `json:"testParam"`       // 测试参数
}

// TestDBData 测试函数返回结构体
type TestDBData struct {
    TestDBParam string `json:"testDBParam"`       // 测试参数
}
```