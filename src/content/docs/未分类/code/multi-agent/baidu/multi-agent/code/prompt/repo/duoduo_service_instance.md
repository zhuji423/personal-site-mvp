---
title: "duoduo_service_instance"
description: "你是一名go后端工程师，现在我给你提供一个service函数入口，请从函数中定位到service对象，并返回名称。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\repo\\duoduo_service_instance.md"
---
你是一名go后端工程师，现在我给你提供一个service函数入口，请从函数中定位到service对象，并返回名称。

## 示例：
- 函数内容：
```go
// NewWealthService _
func NewWealthService() ibase.ExecLogicInterface {
	instance := new(WealthService)
	return instance
}
```
- 返回：
WealthService

- 文件内容：
```go
// NewEatInfoService ...
func NewEatInfoService() *ServiceEatInfo {
	return &ServiceEatInfo{}
}
```
- 返回：
ServiceEatInfo

- 文件内容：
```go
// NewReceiveService _
func NewReceiveService() ibase.ExecLogicInterface {
	instance := new(ReceiveService)
	return instance
}
```
- 返回：
ReceiveService

## 任务输入：
### 接口地址：
{{uri}}

### 接口service层入口函数：
{{func}}

### 返回格式（只输出service名称）