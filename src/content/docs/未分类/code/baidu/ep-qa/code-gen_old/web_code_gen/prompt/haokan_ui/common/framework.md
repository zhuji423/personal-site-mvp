---
title: "framework"
description: ". ├── Dockerfile ├── Makefile ├── README.md ├── bootstrap │ ├── dao │ │ ├── mysql.go │ │ ├── redis.go │ │ └── sndb.go │ "
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\haokan_ui\\common\\framework.md"
---
.
├── Dockerfile
├── Makefile
├── README.md
├── bootstrap
│   ├── dao
│   │   ├── mysql.go
│   │   ├── redis.go
│   │   └── sndb.go
│   ├── hklogger
│   │   └── logger.go
│   └── init.go
├── ci.yml
├── conf
│   ├── ral
│   │   └── services
│   │       ├── ral_config_test.toml    // ral下游接口配置文件
│   │       ├── mysql_test.toml
│   │       ├── redis_test.toml
│   │       └── sndb_test.toml
├── controllers
│   └── haokan_test.go      // 
├── models
│   ├── constant
│   ├── dto
│   ├── request
│   │   └── request_test.go
│   └── response
│       └── response_test.go
├── routers
│   └── router.go
└── services                // 业务逻辑层
    └── services_test.go    // service层业务逻辑入口，相关

    