---
title: "router"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\matrix\\baidu_searchbox_sbox-basic\\router.md"
---
## router层涉及到`inner`接口添加路由配置时，需要通过`innerRouter`替换`basicRouter`实现注册接口添加配置，**仅生成新增添加语句即可**，innerRouter定义如下：
```go
innerRouter := router.Group("/baiduboxapp/basic")
```
- 生成示例：
* 步骤：添加inner注册接口配置
* 文件名：`httpserver/router.go`
```go
registerTask(innerRouter.Group("/test"))  // 注册接口添加示例配置
```