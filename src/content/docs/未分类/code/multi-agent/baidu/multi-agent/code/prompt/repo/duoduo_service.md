---
title: "duoduo_service"
description: "你是一名go后端工程师，现在我给你提供一个controller文件，请从文件中定位到本接口的controller入口函数，并且返回指定接口的service层的实例名称。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\repo\\duoduo_service.md"
---
你是一名go后端工程师，现在我给你提供一个controller文件，请从文件中定位到本接口的controller入口函数，并且返回指定接口的service层的实例名称。

## 示例：
- 文件内容：
```go
// FuncTreasurePotAddController 领取奖励
func FuncTreasurePotAddController(ctx context.Context, req ghttp.Request) ghttp.Response {
	instance := new(ControllerTreasurePot)
	instance.BaseController = controller.NewBaseController()
	instance.ResponseType = "json"
	instance.ExecLogicInterface = treasurepot.NewTreasurePotAddService()
	return instance.Execute(ctx, req)
}
```
- 返回：
NewTreasurePotAddService

- 文件内容：
```go
// NewHomeController _
func NewHomeController() *HomeController {
	instance := new(HomeController)
	instance.BaseController = controller.NewBaseController()
	instance.ExecLogicInterface = withdraw.NewHomeService()
	return instance
}

// FuncHomeController _
func FuncHomeController(ctx context.Context, req ghttp.Request) ghttp.Response {
	instance := NewHomeController()
	instance.ResponseType = "json"
	return instance.Execute(ctx, req)
}
```
- 返回：
NewHomeService

- 文件内容：
```go
// NewListController ...
func NewListController() *ListController {
	instance := new(ListController)
	instance.BaseController = controller.NewBaseController()
	instance.ResponseType = "json"
	instance.ExecLogicInterface = ecommerce.NewListService()
	return instance
}

// FuncListController ...
func FuncListController(ctx context.Context, req ghttp.Request) ghttp.Response {
	return NewListController().Execute(ctx, req)
}

```
- 返回：
NewListService

## 任务输入：
### 接口地址：
{{uri}}

### 接口入口函数签名：
{{func_sign}}

### controller文件内容：
{{controller}}

### 返回格式（只输出service名称）