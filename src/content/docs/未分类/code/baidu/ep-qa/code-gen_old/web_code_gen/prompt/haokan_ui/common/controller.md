---
title: "controller"
description: "import \"context\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\haokan_ui\\common\\controller.md"
---
## controller层代码
* 文件路径：`controllers/test_controllers.go`
```go
package controllers

import (
	"context"

	"icode.baidu.com/baidu/go-hulk/hulk/gdp_wrapper/ghttp"
	"icode.baidu.com/baidu/haokan-go/hklib/common/ctx_util"

	"icode.baidu.com/{{repository}}/library"
	"icode.baidu.com/{{repository}}/models/request"
	"icode.baidu.com/{{repository}}/services"
)

// TestFunc ...
func TestFunc(ctx context.Context, req ghttp.Request) ghttp.Response {
    // 获取请求变量
	var param request.TestRequest
	// 请求参数校验
	if ctx_util.ShouldBind(req, &param) != nil {
		return ctx_util.CtxResponse(ctx, library.FeedParamsError, nil)
	}
	// 调用service层的逻辑处理函数
	rsp := services.TestService(ctx)
	return ctx_util.CtxResponse(ctx, ctx_util.ERR_NO_SUCCESS, rsp)
}
```