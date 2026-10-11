---
title: "frame"
description: ". ├── Dockerfile ├── conf │ └── servicer │ └── servicetestral.toml // ral第三方下游接口配置文件 ├── controller │ └── personal │ └──"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_personal\\depend\\frame.md"
---
.
├── Dockerfile
├── conf
│    └── servicer
│         └── service_test_ral.toml  // ral第三方下游接口配置文件
├── controller
│    └── personal
│         └── 包名.go  // controller层
├── httpserver
│    └── personal.go  // router层
├── library
│    ├── constant
│    │    ├── gcp.go  // gcp常量配置
│    │    ├── service.go  // ral第三方下游接口名称配置
│    │    └── personal.go  // 业务逻辑相关常量配置
│    ├── errno
│    │    └── personal.go  // 业务逻辑相关错误码配置
│    ├── gcp
│    │    └── fetch.go  // gcp通用操作，封装好的方法（无需生成）
│    └── resource
│         └── resource.go  // 数据操作对象定义
└──  model
     ├── dao
     │    ├── gcp
     │    │    └── personal
     │    │         └── test_gcp.go  // dao层gcp底层数据操作逻辑实现，文件根据需求命名
     │    ├── redis
     │    │    └── personal
     │    │         └── test_redis.go  // dao层redis底层数据操作逻辑实现，文件根据需求命名
     │    ├── 数据库包名
     │    │    └── test_mysql.go // dao层mysql底层数据操作逻辑实现，文件根据需求命名
     │    └── 第三方下游接口包名
     │         └── test_ral.go  // dao层ral第三方下游接口数据操作逻辑实现，文件根据需求命名
     ├── data
     │    └── 包名
     │         └── 功能名.go  // data层数据获取逻辑实现，文件根据需求命名
     ├── service
     │    └── personal
     │         └── 包名.go  // service层业务逻辑实现，文件根据需求命名
     └── types
          ├── dto
          │    └── 包名.go  // 业务逻辑相关结构体定义
          ├── request
          │    └── personal.go  // 业务逻辑相关请求结构体定义
          └── response
               └── personal.go  // 业务逻辑相关响应结构体定义