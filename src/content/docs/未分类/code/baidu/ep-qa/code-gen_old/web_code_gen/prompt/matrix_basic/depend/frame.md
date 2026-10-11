---
title: "frame"
description: ". ├── Dockerfile ├── conf │ └── servicer │ └── servicetestral.toml // ral下游服务配置 ├── controller │ └── 包名 // 包名根据需求输入解析，优先"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_basic\\depend\\frame.md"
---
.
├── Dockerfile
├── conf
│    └── servicer
│         └── service_test_ral.toml  // ral下游服务配置
├── controller
│    └── 包名  // `包名`根据需求输入解析，优先根据指定命名，否则从接口路径后缀中提取解析`包名/功能名`
│        └── 功能名.go  // `功能名`根据需求输入解析，优先根据指定命名，否则从接口路径后缀中提取解析`包名/功能名`
├── httpserver
│    ├── 包名.go  // 接口注册
│    └── router.go  // 注册接口配置
├── library
│    ├── constant
│    │    ├── ...  // 其他通用常量配置
│    │    ├── service.go  // ral下游接口服务名配置
│    │    └── 包名.go  // 接口特定常量配置
│    ├── errno
│    │    └── 包名.go  // 接口错误码设置
│    ├── gcp // gcp通用操作，封装好的方法
│    │     ├── gcp.go  // 读取相关的操作
│    │     └── switch.go  // 开关方法
│    ├── errors // 通用错误码
│    │    └── basic_error.go  
│    └── resource
│         └── resource.go // 数据操作对象定义
└── model
     ├── dao
     │    ├── mission
     │    │    └── service.go  // ral交互入口
     │    ├── db
     │    │    └── test_table.go  // db数据库的底层操作逻辑
     │    ├── redis
     │    │    ├── service.go  // redis数据操作相关方法配置
     │    │    └── test_redis.go  // redis数据操作底层逻辑
     │    └── 包名
     │         ├── 功能名.go  // dao层数据操作入口
     │         └── test_ral.go  // ral数据操作相关底层逻辑
     ├── data
     │    └── 包名
     │         ├── 功能名_base.go
     │         └── 功能名.go
     ├── service
     │    ├── ddmission
     │    │    └── service.go  // service层交互入口
     │    └── 包名
     │         ├── 功能名_base.go
     │         └── 功能名.go
     └── types
         ├── 结构体模块名（默认为`dto`）
         │    └── 包名
         │         └── 功能名.go
         ├── request
         │    └── 包名.go
         └── response