---
title: "README"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\amis_service_gen\\README.md"
---
### 项目结构
```
.
├── README.md
├── case
│   └── input_data.py         // 测试输入
├── lib
│   ├── context.py            // 定义框架透传的公共参数类
│   ├── gen_amis_schema.py    // 生成schema文件  
│   ├── gen_api.py            // 生成数据表与接口api
│   ├── gen_service_code.py   // 生成服务代码
│   ├── intent_reg.py         // 意图识别
│   └── valid_check.py        // 参数校验
├── logs                      // 日志目录
├── main.py                   // 入口文件
├── main_test.py              // 测试入口文件
├── prompt                    // prompt模板
│   ├── gen_amis_schema
│   ├── gen_api
│   ├── gen_service_code
│   ├── gen_service_code_php_tieba
│   └── intent_reg
└── utils                     // 工具类
    ├── config.py             // 配置文件
    ├── deepseek_util.py      // deepseek模型
    ├── errno_util.py         // 错误码
    ├── kirin_util.py         // kirin工具
    ├── llm_util.py           // llm模型
    ├── log.py                // 日志
    ├── parse_util.py         // 解析工具
    └── qadc_util.py          // qadc工具
```
### 接口文档
[接口文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/UCjioO60XNcLij)

### 项目文档
[项目文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/7vfH7R2e3HnyGo)

### 代码地址
https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/code-gen/tree/master