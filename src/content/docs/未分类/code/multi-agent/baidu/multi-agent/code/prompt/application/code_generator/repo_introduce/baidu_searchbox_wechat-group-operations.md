---
title: "当前代码库"
description: "一、配置相关目录 conf/ 开发环境配置 confonline/ 生产环境配置 confshangyang/ 商鞅的配置"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\baidu_searchbox_wechat-group-operations.md"
---
# 当前代码库
baidu/searchbox/wechat-group-operations

一、配置相关目录
* conf/  开发环境配置
* conf_online/  生产环境配置
* conf_shangyang/  商鞅的配置

二、源代码与业务逻辑目录
核心业务代码、数据模型、工具库等。
1. 入口与初始化
* main.go  程序入口文件，启动服务。
* bootstrap/  初始化组件（如日志、缓存、服务注册），关键文件 bootstrap.go 包含 initLoggers（日志初始化）、initComponent（组件初始化）等函数。

2. 核心业务逻辑
* model/  数据模型与业务服务，包含： - dao/：数据库访问层（如 wx_robot_group.go 操作机器人群组数据）； - data/：常量、结构体定义（如 wechatgroup/group.go 群数据模型）； - service/：业务服务实现（如 wxgroup/ 微信群操作、qywx/ 企业微信接口封装）。
* servers/  服务端实现，如 httpserver/ 存放 HTTP 接口控制器（controller/tools.go）和路由配置。

3. 通用工具库
* library/

  公共组件与工具，包含： - cache/：缓存相关（如 storage.go 内存缓存实现）； - store/：数据存储（redis/、mysql/ 客户端封装）； - ibase/：API 上下文、响应处理等基础框架； - util/：字符串、时间等通用工具函数。
* components/

定制组件，如 gredis/（Redis 扩展）、miscache/（缓存组件）。
三、工具与脚本目录
* script/

 业务脚本，如 wx_group_task/ 包含微信群定时任务（wx_group_handle_task.go）、群人数统计等脚本。
* cmd/

子功能模块编译脚本（build.sh），编译产出存放于 bin/。
* develop/

开发环境辅助工具（如 main.go 可能用于本地调试）。
* Makefile

工程编译、测试、打包脚本，支持 make package（打包线上环境）、make test（单元测试）等命令。