---
title: "api_router"
description: "当前是百度 APP 极速版个人中心服务业务场景，代码库接口及其路由详情如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\580\\api_router.md"
---
当前是百度 APP 极速版个人中心服务业务场景，代码库接口及其路由详情如下：

`baidu/searchbox/personal-go`是个人中心服务核心逻辑实现代码库。

- `httpserver` 包是所有接口的路由层入口：
  - `httpserver/router.go` 是接口路由入口。
  - `httpserver/personal.go` 是核心业务逻辑接口定义文件，所有个人中心业务逻辑接口均通过该文件进行路由。
  - `httpserver/metric.go` 是监控接口定义文件，监控状态、测试报警接口通过该文件进行路由。
  - `httpserver/inner` 包是内部调用接口定义包，对内服务接口均在该包下的文件进行路由。
