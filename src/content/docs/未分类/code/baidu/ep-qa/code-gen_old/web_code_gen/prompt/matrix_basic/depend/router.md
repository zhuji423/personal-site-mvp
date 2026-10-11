---
title: "router"
description: "import \"net/http\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_basic\\depend\\router.md"
---
## router层
### 接口路由注册，文件路径：`httpserver/包名.go`
```go
package httpserver

import (
	"net/http"

	"icode.baidu.com/baidu/gdp/ghttp"

	"icode.baidu.com/baidu/searchbox/sbox-basic/controller/包名"
)

// 注意当接口路径为包含`inner/`的内部接口时，注册函数名需加入Inner关键词，即`registerInnerTestFunc`
func registerTestFunc(router ghttp.Router) {
    ctl := 包名.NewController()
    /*
        HandleFunc参数说明：
        method  http方法，示例：http.MethodPost/http.MethodGet
        path    接口地址：接口地址中的最后的功能路径，如`包名/testFunc`，则path为`testFunc`   
        handler 业务逻辑，执行后会返回一个 Response 对象, 示例： ctl.TestFunc
    */
	router.HandleFunc(method string, path string, handler HandlerFunc)
}
```
### 注册接口路由配置，文件路径：`httpserver/router.go`
* 此文件仅需追加生成内容即可，不要导包，示例如下：
```go
// 注册路径配置函数
func httpRouter(ser *ghttp.DefaultServer) ghttp.Router {
    // ...
    
    // 常规接口注册配置，示例如下：
    // basicRouter := router.Group("/baiduboxapp/basic")
	// {
    //    registerTestFunc(basicRouter.Group("/包名"))
    // }
    
    // 内部接口注册配置，示例如下：
    // innerRouter := router.Group("/inner")
	// {
    //    registerInnerTestFunc(innerRouter)
    // }
}
```