---
title: "controller"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\controller.md"
---
## controller层代码，文件路径：`controller/包名/功能名.go`
* 此文件无需生成注释
```go

import (
	"context"

	"icode.baidu.com/baidu/gdp/ghttp"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/controller"
	"icode.baidu.com/baidu/jady/ug-duoduo-video/model/service/包名"
)

// TestController ...
type TestController struct {
	controller.Controller
}

// NewTestFuncController ...
func NewTestFuncController() *TestController {
	instance := new(TestController)
	instance.BaseController = controller.NewBaseController()
	instance.ResponseType = "json"
	instance.ExecLogicInterface = 包名.NewTestFuncService()
	return instance
}

// FuncTestFuncController ...
func FuncTestFuncController(ctx context.Context, req ghttp.Request) ghttp.Response {
	return NewTestFuncController().Execute(ctx, req)
}
```