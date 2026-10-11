---
title: "kirin作为amis后端服务模板"
description: "kirin作为amis后端服务模板"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Amis\\kirin作为amis后端服务模板.md"
---
kirin作为amis后端服务模板

```
.
├── case
│   └── third_case.py  # 测试用例
├── conf
│   └── config.py  # 配置文件
├── lib
│   └── runner.py  # 运行模块，负责执行【主要开发】
├── main.py  # 主程序入口文件
├── main_test.py  # 主程序的测试文件
└── utils
    ├── error_util.py  # 错误处理
    └── log.py  # 日志记录
```


在runner中增加对应函数，在main_test中执行测试用例



[附件: demo.zip | 21.4KB | application/zip | fileId=82a85a178f574c5db51a48d1a76b1ffc]





