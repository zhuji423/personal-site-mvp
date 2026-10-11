---
title: "frame"
description: ". ├── Dockerfile ├── conf │ └── servicer // 下游ral接口配置 │ └── servicetestral.toml ├── library │ ├── constant // 通用常量定义 │ │"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\depend\\frame.md"
---
.
├── Dockerfile
├── conf
│     └── servicer  // 下游ral接口配置
│           └── service_test_ral.toml
├── library
│     ├── constant  // 通用常量定义
│     │     ├── gcp.go  // gcp AppID常量配置（该文件内容无需生成）
│     │     └── service.go  // 下游ral接口名称配置
│     ├── errno
│     │     ├── common.go  // 已经定义好的基础错误码（该文件内容无需生成）
│     │     └── 包名.go  // 接口业务逻辑相关错误码配置
│     ├── gcp // gcp通用操作，封装好的方法（该文件夹下的内容无需生成）
│     │     ├── base.go  // 读取相关的操作
│     │     └── switch.go  // 开关方法
│     └── resource
│           └── resource.go  // gcp、redis、db操作对象定义
├── model
│     ├── consts  // db、gcp、redis、srv业务常量定义
│     │     ├── db
│     │     │     └── 包名_test_table.go  // 数据库相关业务常量定义， test_table根据输入需求命名
│     │     ├── gcp
│     │     │     ├── base.go  // gcp前缀常量定义
│     │     │     └── 包名.go  // gcp相关业务常量定义
│     │     ├── redis
│     │     │     ├── base.go  // redis前缀常量定义
│     │     │     └── 包名.go  // redis相关业务常量定义
│     │     └── srv
│     │           └── 包名.go  // 其他业务相关常量定义
│     ├── dao
│     │     ├── db
│     │     │     ├── base.go  // 数据库表名和分表配置
│     │     │     └── 包名_test_table.go // db数据库操作逻辑，`test_table`根据需求数据库相关描述命名
│     │     ├── gcp
│     │     │     └── 接口路径占位  // 根据接口输入层级确定，如两层级则为`包名`，如三层级则为`包名/子包名`
│     │     │           └── 功能名_test_gcp.go  // 底层gcp数据操作逻辑，`test_gcp`根据需求gcp相关描述命名
│     │     └── redis
│     │           └── 接口路径占位  
│     │                 └── 功能名_test_redis.go  // 底层redis数据操作逻辑，`test_redis`根据需求redis相关描述命名
│     ├── data
│     │     └── 接口路径占位  
│     │           ├── 基础功能名.go  // 数据获取逻辑入口
│     │           └── 功能名_test_data.go  // 数据获取逻辑实现，`test_data`根据需求数据获取相关描述命名
│     ├── ral
│     │     └── 接口路径占位  
│     │           ├── base.go // 下游ral接口常量、结构体定义
│     │           └── test_ral.go  // 下游ral接口操作逻辑，`test_ral`根据需求ral相关描述命名
│     ├── service
│     │     └── 接口路径占位  
│     │           ├── 基础功能名.go  // service层入口
│     │           └── 功能名_test_service.go  // service层业务逻辑实现，`test_service`根据需求业务逻辑相关描述命名
│     └── types
│           ├── 游戏模块名
│           │     └── 接口路径占位  
│           │           └── 功能名.go  // 业务逻辑相关结构体定义
│           ├── request
│           │     └── 接口路径占位  
│           │           └── 功能名.go  // 请求参数结构体定义
│           └── response
│                 └── 接口路径占位  
│                       └── 功能名.go  // 响应参数结构体定义
└── servers
      └── httpserver
            ├── controller
            │     └── 接口路径占位  
            │           └── 功能名.go
            ├── register.go  // 接口路由配置
            └── router
                  └── 包名.go  // 接口路由注册