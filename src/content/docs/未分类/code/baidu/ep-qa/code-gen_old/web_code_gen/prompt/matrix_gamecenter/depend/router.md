---
title: "router"
description: "import \"net/http\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\depend\\router.md"
---
## router层
* router层代码均不要生成任何注释
### 接口注册代码，文件路径：`servers/httpserver/router/包名.go`
* 此代码不要生成任何注释
```go
package router

import (
	"net/http"

	"icode.baidu.com/baidu/gdp/ghttp"
	
	"icode.baidu.com/baidu/searchbox/ug-gamecenter/servers/httpserver/controller/接口路径占位"
)


// 解释：`RegisterTmpRouter`中，存在`子包名`时，`Tmp`对应`子包名`，否则`Tmp`对应`包名`
func RegisterTmpRouter(router ghttp.Router) {
    /*
        参数说明：
        method  http方法，示例：http.MethodPost/http.MethodGet
        path    接口地址，接口地址中的最后的功能路径，如`包名/testFunc`，则path为`testFunc`  
        handler 业务逻辑函数，定义在controller层， 示例： test.TestFunc，存在`子包名`时，`test.`对应`包名.`，否则`test.`对应`子包名.`
    */
    router.HandleFunc(method string, path string, handler HandlerFunc)
}
```
### 配置注册接口代码，文件路径：`servers/httpserver/register.go`
* 此代码不要生成任何注释
```go
package httpserver

import (
	"icode.baidu.com/baidu/gdp/ghttp"

	myRouter "icode.baidu.com/baidu/searchbox/ug-gamecenter/servers/httpserver/router"
)


/*
    * 函数名`registerServiceTypeAPI`映射规范：
    1. 当接口路径包含`inner`、`testing`、`mis`关键词时，函数名`registerServiceTypeAPI`中的`Type`对应`Inner`或`Testing`或`MIS`，示例：接口路径包含`inner/子包名`，则函数名为`registerServiceInnerAPI`；
    2. 当接口路径不包含上述关键词时，函数名`registerServiceTypeAPI`中的`Type`对应``，即为`registerServiceAPI`。
*/
func registerServiceTypeAPI(router ghttp.Router) {
    // 解释：存在`子包名`时，`tmp`对应`子包名`，否则`tmp`对应`包名`
    tmpRouter := router.Group("/tmp")  
    // 解释：存在`子包名`时，`Tmp`对应`子包名`，否则`Tmp`对应`包名`
    myRouter.RegisterTmpRouter(tmpRouter)  
}
```