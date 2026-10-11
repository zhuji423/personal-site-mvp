---
title: "api_router"
description: "当前是百度 APP 极速版社群私域服务业务场景，代码库接口及其路由详情如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\573\\api_router.md"
---
当前是百度 APP 极速版社群私域服务业务场景，代码库接口及其路由详情如下：

`baidu/searchbox/wechat-group-operations`是社群服务核心逻辑实现代码库。

- `servers/httpserver`包是所有接口的路由层入口：
  - `servers/httpserver/router.go` 该文件是路由入口，所有接口的分发从该文件开始，路由下发到对应接口的`controller`层。
