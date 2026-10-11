---
title: "baidu/searchbox/sbox-basic"
description: "当前是百度 APP 极速版存钱罐业务场景，代码库接口及其路由详情如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\570\\api_router.md"
---
当前是百度 APP 极速版存钱罐业务场景，代码库接口及其路由详情如下：

# baidu/searchbox/sbox-basic

代码库 `baidu/searchbox/sbox-basic` 是面向前端请求的接入层服务，在不同业务场景下职责不同，对于极速版存钱罐业务场景而言，负责接收客户端请求并调用 ug-duoduo-video 的内部接口以获取业务数据，实现逻辑处理与数据中转。

- `httpserver`包是所有接口的路由层入口：

  - `httpserver/router.go` 该文件是路由入口，所有接口的分发从该文件开始。
  - `httpserver/ddmission.go` 该文件是 duoduo 存钱罐场景对应的所有接口的定义和分发文件，路由下发到对应接口的`controller`层。

- 特殊通用接口说明：
  - `/baiduboxapp/basic/ddmission/popups`：弹窗列表接口，返回所有可展现的弹窗信息。
  - `/baiduboxapp/basic/ddmission/popup`：通用弹窗接口。
  - `/baiduboxapp/basic/ddmission/popupreceive`：通用弹窗接收接口。
  - `/baiduboxapp/basic/ddmission/taskPopup`：任务弹窗接口。
  - `/baiduboxapp/basic/ddmission/taskPopupReceive`：任务弹窗接收接口。

# baidu/jady/ug-duoduo-video

代码库 `baidu/jady/ug-duoduo-video` 是存钱罐业务的核心实现代码库，负责处理存钱罐的内部业务逻辑，并对外提供内部服务接口，供 sbox-basic 等上层服务调用。

- `httpapi` 包是所有接口的路由层入口：

  - `httpapi/router.go` 该文件是路由入口，所有接口的分发从该文件开始。
  - `httpapi/api` 目录下是所有接口的路由定义文件，路由下发到对应接口的`controller`层。

- 特殊接口说明：
  - 存钱罐页面任务相关接口（`/video/external/task/*`），通过在以下通用接口中添加任务来实现流程串通：
    - `/video/external/task/intranetRegister`：通用任务注册接口。
    - `/video/external/task/complete`：通用任务完成接口。
    - `/video/external/task/list`：通用任务列表接口，返回所有可展现的任务信息。
    - `/video/external/task/receive`：通用任务接收接口。
    - `/video/external/task/popup`：通用弹窗接口。
  - 非存钱罐页面的打卡挑战类活动相关接口（`/video/external/challenge/*`）：
    - `/video/external/challenge/list`：打卡挑战类活动列表接口。
