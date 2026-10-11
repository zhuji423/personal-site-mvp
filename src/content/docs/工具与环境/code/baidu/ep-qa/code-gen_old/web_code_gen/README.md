---
title: "README"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\README.md"
---
### 项目结构
```
.
├── README.md
├── case                      // 测试输入    
│   ├── amis_page.py
│   ├── business_op.py
│   ├── dianshang_restful.py
│   ├── feed_gr.py
│   ├── public_gdp.py
│   ├── tieba_crontask.py
│   └── tieba_third.py
├── conf                      // 配置文件
│   ├── conf.py
│   └── dianshang_restful_modules
├── lib                       // 子功能实现
│   ├── amis_page
│   │   ├── gen_amis_schema.py
│   │   ├── gen_api.py
│   │   ├── gen_service_code.py
│   │   └── intent_reg.py
│   ├── tieba_third
│   │   ├── gen_encry.py
│   │   ├── gen_third.py
│   │   └── intent_reg.py
│   ├── dianshang_restful
│   │   ├── gen_restful.py
│   │   └── intent_reg.py
│   ├── feed_gr
│   │   ├── gen_api.py
│   │   └── intent_reg.py
│   ├── context.py            // 定义框架透传的公共参数类
│   ├── gen_base.py           // 生成子功能基类
│   ├── gen_public.py         // 通用生成实现
│   ├── put_data_to_qadc.py   // 数据入库
│   └── valid_check.py
├── logs                      // 日志目录
├── main.py                   // 入口文件
├── main_test.py              // 测试入口文件
├── runner.py                 // 执行主控基类
├── runner                    // 执行主控实现
│   ├── amis_page_main.py
│   ├── tieba_third_main.py
│   ├── dianshang_restful_main.py
│   ├── feed_gr_main.py
│   └── public_main.py        // 通用生成主控
├── prompt                    // prompt模板
│   ├── amis_page
│   │   ├── gen_amis_schema
│   │   ├── gen_api
│   │   ├── gen_service_code
│   │   ├── gen_service_code_php_tieba
│   │   └── intent_reg
│   ├── tieba_third
│   │   ├── gen_encry
│   │   ├── gen_third
│   │   └── intent_reg
│   ├── dianshang_restful
│   │   ├── gen_restful
│   │   └── intent_reg
│   ├── feed_gr
│   │   ├── gen_api
│   │   └── intent_reg
│   ├── gen_crontask
│   ├── gen_fea
│   └── gen_gdp
└── utils                     // 工具类
    ├── config.py             // 配置文件
    ├── deepseek_util.py      // deepseek模型
    ├── errno_util.py         // 错误码
    ├── file_util.py          // 文件工具
    ├── kirin_util.py         // kirin工具
    ├── llm_util.py           // llm模型
    ├── log.py                // 日志
    ├── parse_util.py         // 解析工具
    ├── qadc_util.py          // qadc工具
    └── upload_model.py       // 上传模型到bos
```

### 接口文档
[接口文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/UCjioO60XNcLij)


### 代码地址
https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/code-gen/tree/master