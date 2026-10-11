---
title: "当前代码库"
description: "- bootstrap：应用入口 - bootstrap：服务初始化 - servers：HTTP服务器 - httpserver：业务服务 - middleware：中间件 - router：路由,api定义的地方 - controlle"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\baidu_searchbox_userauthorize.md"
---
# 当前代码库
baidu/searchbox/userauthorize这是一个对游戏中心和斗地主提供策略服务的代码库，支持以下几种功能：
- 目标人群判断
- 任务策略服务
- 人群策略服务

## 项目结构
userauthorize/
  ├── main.go                   # 应用入口
  ├── bootstrap/                # 服务初始化
  ├── servers/                  # HTTP服务器
  │   ├── httpserver/             # 业务服务
  │   │   ├── middleware/           # 中间件
  │   │   ├── router/               # 路由,api定义的地方
  │   │   └── controller/           # 控制器
  │   └── adminserver/            # 管理服务
  ├── services/                 # 业务服务层
  │   ├── task/                   # 任务策略服务
  │   └── crowd/                  # 人群策略服务
  ├── model/                    # 数据模型层
  │   ├── dao/                    # 数据访问对象
  │   └── service/                # 授权/任务判断
  │       └───authorize/             # 目标人群判断
  ├── library/                   # 公共库（常量、错误码、工具）
  └── conf_online/              # 线上配置

- bootstrap：应用入口
- bootstrap：服务初始化
- servers：HTTP服务器
  - httpserver：业务服务
    - middleware：中间件
    - router：路由,api定义的地方
    - controller：控制器
  - adminserver：管理服务
- services：业务服务层
  - task：任务策略服务
  - crowd：人群策略服务
- model：数据模型层
  - dao：数据访问对象
  - service：授权/任务判断
    - authorize：目标人群判断
- library：公共库（常量、错误码、工具）
- conf_online：线上配置

## 依赖方向
  - 严格遵循依赖方向：router -> controller → service → services
  - 请求处理链： 请求 → 中间件(日志/指标/超时/公参) → Router → Controller → Service → Response
  - 禁止循环依赖
  - 上层模块不能依赖于下层模块实现细节，应通过接口进行依赖
  - 可以参照代码库中ral的请求方式