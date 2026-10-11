---
title: "router"
description: "import \"net/http\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\router.md"
---
## router层
* router层代码均不要生成任何注释
### 接口注册代码，文件路径：`httpserver/path3/path4.go`
* `path3`、`path4`命名根据输入接口路径层级来确定，要求如下：
1. 当去除前缀路径后接口路径为三层级`包名/子包名/功能名`时，路径中`path3`对应`包名`,`path4`对应`子包名`
2. 当去除前缀路径后接口路径为两层级`包名/功能名`时，路径中`path3`为`api`，`path4`对应`功能名`
* 此代码不要生成任何注释
```go
package path3

import (
	"net/http"

	"icode.baidu.com/baidu/gdp/ghttp"
	
	"icode.baidu.com/baidu/searchbox/ug-game/controller/path1/path2"
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
### 配置注册接口代码，文件路径：`httpserver/register.go`
* 此代码不要生成任何注释
```go
package httpserver

import (
	"icode.baidu.com/baidu/gdp/ghttp"

	"icode.baidu.com/baidu/searchbox/ug-game/httpserver/api"
	"icode.baidu.com/baidu/searchbox/ug-game/httpserver/inner"
	"icode.baidu.com/baidu/searchbox/ug-game/httpserver/mis"
	"icode.baidu.com/baidu/searchbox/ug-game/httpserver/testing"
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