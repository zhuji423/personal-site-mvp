---
title: "frame"
description: ". ├── Dockerfile ├── conf │ └── servicer │ └── servicetestral.toml // ral下游接口配置文件 ├── controller │ └── path1（ddzor包名） │ "
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_game\\depend\\frame.md"
---
.
├── Dockerfile
├── conf
│     └── servicer 
│           └── service_test_ral.toml  // ral下游接口配置文件
├── controller
│     └── path1（`ddz`or`包名`）
│           └── path2（`包名`or`子包名`）  
│                 └── 功能名.go 
├── httpserver  // 接口路由层
│     ├── path3（`包名`or`api`）
│     │     └── path4（`子包名`or`功能名`）.go  // 接口路由注册
│     └── register.go  // 接口路由配置
├── library
│     ├── constant 
│     │     ├── ...  // 模块通用常量定义
│     │     └── service.go  // 下游接口服务名称配置
│     ├── errno 
│     │     └── 包名.go  // 模块通用错误定义
│     ├── gcp // gcp通用操作，封装好的方法（该文件夹下的内容无需生成）
│     │     ├── base.go  // 读取相关的操作
│     │     └── switch.go  // 开关方法
│     └── resource
│           └── resource.go  // redis、gcp、db等操作对象定义文件
└── model
      ├── consts  
      │     ├── db
      │     │     └── 模块包占位  
      │     │           └── 包名_test_table.go  // 数据库相关业务常量定义， test_table根据输入需求命名
      │     ├── gcp
      │     │     └── 模块包占位  
      │     │           ├── base.go  // gcp前缀定义
      │     │           └── 包名.go  // gcp相关业务常量定义
      │     ├── redis
      │     │     └── 模块包占位  
      │     │           ├── base.go  // redis前缀定义
      │     │           └── 包名.go  // redis相关业务常量定义
      │     └── srv
      │           └── 模块包占位
      │                 └── 包名.go  // 其他业务相关常量定义
      ├── dao
      │     ├── db
      │     │     └── 模块包占位  // 根据接口路径层级确定，两层级时为`ddz`，三层级时为`包名`
      │     │           ├── base.go  // 数据库表名和分表配置
      │     │           └── 包名_test_table.go  // 数据库底层操作逻辑， test_table根据输入需求命名
      │     ├── gcp
      │     │     └── 模块包占位
      │     │           └── 接口路径占位  // 根据接口路径层级确定，两层级时为`包名`，三层级时为`子包名`
      │     │                 └── 功能名_test_gcp.go  // gcp底层数据操作逻辑， test_gcp根据输入需求命名
      │     └── redis
      │           └── 模块包占位
      │                 └── 包名_test_redis.go  // redis底层操作逻辑， test_redis根据输入需求命名
      ├── data  // 数据获取逻辑实现层
      │     └── 模块包占位
      │           └── 接口路径占位
      │                 ├── 基础功能名.go  // 数据获取逻辑入口
      │                 └── 功能名.go  // 数据获取逻辑实现，根据需求描述实现
      ├── ral
      │     └── 接口路径占位
      │           ├── base.go  // ral下游接口常量、结构体定义文件
      │           └── test_ral.go  // ral下游接口底层操作逻辑实现，test_ral根据输入需求命名
      ├── service  // 业务逻辑层
      │     └── 模块包占位
      │           └── 接口路径占位
      │                 ├── 基础功能名.go  // service层业务逻辑入口
      │                 └── 功能名.go  // 业务逻辑实现，根据需求描述实现
      └── types
            └── 模块包占位
                  ├── 游戏模块名
                  │     └── 接口路径占位
                  │           └── 功能名.go  // 业务逻辑中涉及到的结构体定义
                  ├── request
                  │     └── 功能名.go // 请求i定义
                  └── response
                        └── 功能名.go  // 响应体定义