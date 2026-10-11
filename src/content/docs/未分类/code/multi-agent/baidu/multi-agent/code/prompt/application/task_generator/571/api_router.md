---
title: "api_router"
description: "当前是百度 APP 极速版游戏中心业务场景，代码库接口及其路由详情如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\571\\api_router.md"
---
当前是百度 APP 极速版游戏中心业务场景，代码库接口及其路由详情如下：

`baidu/searchbox/ug-gamecenter` 这是一个对前端提供服务的代码库，提供一系列的接口支撑游戏中心和多个游戏的服务。

- `servers/httpserver` 包是所有接口的路由层入口：
  - `servers/httpserver/register.go` 是接口注册文件。
  - `servers/httpserver/router.go` 是接口路由入口。
  - `servers/httpserver/router` 包是所有接口的路由定义文件，路由下发到对应接口的`controller`层。
