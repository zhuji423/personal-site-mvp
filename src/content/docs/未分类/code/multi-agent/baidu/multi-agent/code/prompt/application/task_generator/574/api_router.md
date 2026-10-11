---
title: "api_router"
description: "当前是百度 APP 极速版斗地主游戏业务场景，代码库接口及其路由详情如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\574\\api_router.md"
---
当前是百度 APP 极速版斗地主游戏业务场景，代码库接口及其路由详情如下：

`baidu/searchbox/wechat-group-operations`是斗地主游戏服务核心逻辑实现代码库。

- `httpserver` 包是所有接口的路由层入口：
  - `httpserver/register.go` 是接口注册文件。
  - `httpserver/router.go` 是接口路由入口。
  - `httpserver/api` 包是核心接口定义包，所有核心业务逻辑接口均通过该包下的文件进行路由。
  - `httpserver/inner` 包是内部调用接口定义包，对内服务接口均在该包下的文件进行路由。
  - `httpserver/mis` 包是 amis 相关配置服务调用接口定义包，amis 相关数据操作接口均在该包下的文件进行路由。
  - `httpserver/testing` 包是干预、测试服务调用接口定义包，干预接口均在该包下的文件进行路由。
