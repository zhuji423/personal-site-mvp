---
title: "router"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\depend\\router.md"
---
## router层代码，文件路径：`httpserver/personal.go`
* 此文件追加内容即可，不要导包，示例如下：
```go
/*
    参数说明：
    method  http方法，示例：http.MethodPost/http.MethodGet
    path    接口地址，接口地址中的最后的功能路径，如`包名/test_func`，则path为`test_func`  
    handler 业务逻辑函数，定义在controller层的方法， 示例： ctl.TestFunc
*/
// 测试页面
g.HandleFunc(method string, path string, handler HandlerFunc)
```