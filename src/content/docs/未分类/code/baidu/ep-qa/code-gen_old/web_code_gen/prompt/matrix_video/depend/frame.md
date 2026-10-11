---
title: "frame"
description: ". ├── BCLOUD ├── components │ └── miscache │ └── loader.go // mis页面数据脚手架逻辑 ├── conf │ └── servicer │ └── servicetestral."
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_video\\depend\\frame.md"
---
.
├── BCLOUD
├── components
│    └── miscache
│         └── loader.go  // mis页面数据脚手架逻辑
├── conf
│    └── servicer
│         └── service_test_ral.toml  // ral配置文件
├── controller
│    ├── base.go // controller层入口
│    └── 包名
│         └── 功能名.go
├── httpapi
│    └── api
│         └── 接口类型.go  // 接口路由注册&配置
├── library
│    ├── consts
│    │    ├── service_name.go  // ral下游接口服务名称配置
│    │    └── ... // 通用常量定义
│    ├── gtask
│    │    └── ... // 通用并行数据获取方法定义
│    ├── ibase
│    │    └── ... // 通用工具包定义
│    ├── ierrno
│    │    └── ... // 通用错误码定义
│    ├── mis
│    │    ├── consts.go  // mis页面数据相关常量配置
│    │    ├── struct_smaple.go  // mis页面数据获取实验页面配置
│    │    ├── struct.go  // 新增mis页面配置
│    │    └── struct_test_mis.go  // 新增mis页面定义
│    └── store
│         └── redis
│              └── redis.go  // 封装好的redis操作逻辑
├── model
│    ├── dao
│    │    └── test_table.go  // 数据库底层操作逻辑
│    ├── data
│    │    ├── consts
│    │    │    ├── duoduo_redis_key.go  // 数据库redis key常量配置
│    │    │    └── 包名_功能名.go  // 数据操作相关常量配置
│    │    ├── sample
│    │    │    └── sample.go  // mis实验页面数据加载逻辑
│    │    ├── types
│    │    │    └── 包名_功能名.go  // data层数据获取相关结构体定义
│    │    ├── common
│    │    │    └── mis_ltcache.go  // mis页面数据操作相关函数封装
│    │    └── 包名
│    │         ├── 功能名_base.go  // data层数据获取逻辑入口封装
│    │         └── 功能名.go  // data层数据获取逻辑
│    └── service
│         └── 包名
│              └── 功能名.go
└── thirdparty  // 第三方下游接口数据获取
     └── 下游接口包名  // 从第三方接口路径解析命名
         ├── consts.go  // ral常量配置
         ├── type.go  // ral相关结构体定义
         └── test_ral.go  // ral下游接口底层数据操作逻辑