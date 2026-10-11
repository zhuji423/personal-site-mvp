---
title: "router"
description: "/ testGroup对象命名，默认为uiGroup，特殊情况如下： 1. 若接口路径包含service关键词，则命名为 serviceGroup 2. 若接口路径包含grayscale关键词，则命名为 grayscale /"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\haokan_ui\\common\\router.md"
---
## router层
* 文件路径：`routers/router.go`
* 此文件仅需生成追加内容即可，不要导包，示例如下：
```go
/*
    HandleFunc参数说明：
    method  http方法，示例：http.MethodPost/http.MethodGet
    path    接口地址：接口地址中的最后的功能路径，如`包名/testFunc`，则path为`testFunc`   
    handler 业务逻辑，执行后会返回一个 Response 对象, 定义在controllers包中， 示例： controllers.TestFunc
    middleware 中间件，可选，可以传递多个中间件
*/

/*
    `testGroup`对象命名，默认为`uiGroup`，特殊情况如下：
    1. 若接口路径包含`service`关键词，则命名为 `serviceGroup`
    2. 若接口路径包含`grayscale`关键词，则命名为 `grayscale`
*/

// 接口描述
testGroup.HandleFunc(http.MethodPost, "/testFunc", controllers.StoryTagFeed)
```