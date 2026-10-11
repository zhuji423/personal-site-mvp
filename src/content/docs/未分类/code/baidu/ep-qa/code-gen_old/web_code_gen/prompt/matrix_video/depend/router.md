---
title: "router"
description: "// 当未指定接口类型时，默认为duoduo是，路由配置方式示例如下： func InitDuoDuor ghttp.Router { r = r.Group\"/video\", middlewares.SetAppNamefalse //d"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\router.md"
---
## router层代码，文件路径：`httpapi/api/接口类型.go`
* `接口类型`根据输入接口路径解析，当接口路径未指定`接口类型`时，默认为`duoduo`
* 此文件无需生成注释
* 此文件仅需生成追加内容即可，不要导包，示例如下：
```go
import (
    "icode.baidu.com/baidu/jady/ug-duoduo-video/controller/包名"
)

// 当未指定接口类型时，默认为duoduo是，路由配置方式示例如下：
func InitDuoDuo(r ghttp.Router) {
	r = r.Group("/video", middlewares.SetAppName(false)) //duoduo ==> video
    {
        testRouter := r.Group("/包名")
        /*
            HandleFunc参数说明：
            method  http方法，示例：http.MethodPost/http.MethodGet
            path    接口地址：接口地址中的最后的功能路径，如`包名/testFunc`，则path为`testFunc`   
            handler 业务逻辑，执行后会返回一个 Response 对象, 定义在test包中， 示例： test.TestFunc
            middleware 中间件，可选，可以传递多个中间件
        */
        testRouter.HandleFunc(method string, path string,  handler HandlerFunc, middleware ...Middleware)
    }
}

// 当未指定接口类型为`test`时，路由配置方式示例如下：
func InitTest(r ghttp.Router) {
	testRouter := r.Group("/video/test", middlewares.SetAppName(true), middlewares.IsInner(), middlewares.SendMessage)
	// 测试接口
	{
		testRouter.HandleFunc("GET,POST", "/testFunc", test.FuncTestFuncController)
    }
}
```