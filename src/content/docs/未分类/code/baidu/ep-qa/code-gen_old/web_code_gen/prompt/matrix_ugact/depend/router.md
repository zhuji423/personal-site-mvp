---
title: "router"
description: "import \"net/http\" \"icode.baidu.com/baidu/gdp/ghttp\" \"icode.baidu.com/baidu/searchbox/ugact/controller/包名\""
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\router.md"
---
## router层，需根据需求进行接口注册和路径配置
### router注册代码，文件路径：`router/包名.go`
* 注意此文件无需生成注释
```go
package router

import (
    "net/http"
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/searchbox/ugact/controller/包名"
)

// HandleFunc参数说明：
//  method  http方法，示例：http.MethodPost/http.MethodGet
//  path    接口地址：`controller/包名/test_func.go`路径下需要用到的接口文件名，示例："/test_func"    
//  handler 业务逻辑，执行后会返回一个 Response 对象, 定义在ctl中， 示例： ctl.TestFunc

// 需求输入接口路径包含`baiduboxapp/ugact/`时，需注册外部接口，示例如下：
// registerTestRouter，其中Test对应包名
func registerTestRouter(r ghttp.Router) {
    ctl := 包名.NewController()
    r.HandleFunc(method string, path string, handler HandlerFunc)
}

// 需求输入接口路径包含`inner/`时，需注册内网接口，示例如下：
// registerInnerTestRouter，其中Test对应包名
func registerInnerTestRouter(r ghttp.Router) {
    ctl := 包名.NewController()
    r.HandleFunc(method string, path string, handler HandlerFunc)
}
```  
### 注册的router路径配置代码，文件路径：`router/router.go`
```go
// 需求输入接口路径包含`baiduboxapp/ugact/`时，需配置外部接口路径，示例如下：
func registerPublicAPI(router ghttp.Router) {
    // registerTestRouter 其中`Test`对应包名
    registerTestRouter(router.Group("/包名")) 
}

// 需求输入接口路径含`inner/`关键词时，需配置内网接口路径，示例如下：
func registerInnerAPI(router ghttp.Router) {
    // registerInnerTestRouter 其中`Test`对应包名
    registerInnerTestRouter(router.Group("/包名"))  
}
```