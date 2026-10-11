---
title: "frame"
description: ". └── Dockerfile ├── conf │ └── servicer // 下游http接口相关配置 │ └── servicetestfunc.toml // 下游接口相关配置，根据下游接口名进行命名 ├── library "
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\depend\\frame.md"
---
.
└── Dockerfile
    ├── conf  
    │   └── servicer  // 下游http接口相关配置
    │       └── service_test_func.toml  // 下游接口相关配置，根据下游接口名进行命名
    ├── library
    │   ├── gcp  // gcp通用操作，封装好的方法
    │   │   ├── switch.go  // 开关相关的操作
    │   │   └── fetch.go //读取相关的操作
    │   ├── resource  
    │   │   └── resource.go // mysql、redis等数据操作对象定义
    │   ├── errno
    │   │   └── 包名.go  // 错误码定义
    │   └── constant  // 常量配置
    │       ├── service.go  // 下游http接口服务名称配置文件
    │       └── gcp.go // gcp相关常量配置
    ├── controller
    │   └── 包名    // 包名根据需求自定义，如果需求中指定，优先按照指定的名字
    │       └── 功能名.go   // 根据输入接口路径确定
    ├── router
    │   ├── router.go  // 内部、外部接口配置
    │   └── 包名.go  // 内部、外部接口定义
    ├── repository
    │   └── test_pkg // 下游http数据获取函数、结构体独立定义，根据下游接口进行命名
    │       ├── test_file.go  // 下游http数据获取函数定义，根据要获取的数据描述命名
    │       └── types.go  // 下游http接口结构体定义
    └── service
        └── 包名 // 包名根据需求自定义，如果需求中指定，优先按照指定的名字
            ├── 功能名.go  // 业务逻辑入口文件，功能名根据需求自定义
            ├── constructor.go  // service类定义和初始化
            ├── contract.go  // service层相关接口类
            ├── data // 业务逻辑具体实现
            │   └── 功能名  // 功能名根据需求自定义，如果需求中指定，优先按照指定的名字
            │       ├── constructor.go  // data类定义和初始化
            │       ├── contract.go  // data层相关接口类
            │       ├── types.go  // 数据获取逻辑相关结构体定义
            │       └── test_file.go  // 数据获取逻辑具体实现，文件根据需求要获取的数据命名
            └──types  // 定义框架、业务逻辑相关结构体
                └── 功能名.go