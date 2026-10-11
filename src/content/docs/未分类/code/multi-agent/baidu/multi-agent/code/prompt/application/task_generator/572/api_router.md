---
title: "api_router"
description: "当前是百度 APP 极速版基础业务场景，代码库接口及其路由详情如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\572\\api_router.md"
---
当前是百度 APP 极速版基础业务场景，代码库接口及其路由详情如下：

`baidu/searchbox/sbox-basic`这是一个对端提供服务的接入服务代码库，提供一系列的接口支撑多个业务，基础方向的核心业务逻辑均实现在该代码库。

- `httpserver`包是所有接口的路由层入口：
  - `httpserver/router.go` 该文件是路由入口，所有接口的分发从该文件开始。
