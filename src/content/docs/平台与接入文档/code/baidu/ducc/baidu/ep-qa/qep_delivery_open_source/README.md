---
title: "README"
description: "Qep Delivery Open Source === 智能交付系统相关开源代码合集，实现跨业务共建需求等"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\README.md"
---
Qep Delivery Open Source
===
智能交付系统相关开源代码合集，实现跨业务共建需求等

整体工程目录结构
---
├── agents                      各个阶段的Agent存放位置                                                  
│   ├── base_agent.py    各阶段Agent继承的父类  
│   ├── qa_test_finish_stage_agent.py          测试完成(stage=6)阶段的处理Agent  
│   ├── qa_test_intercept_stage_agent.py     测试准出(stage=5)阶段的处理Agent  
│   ├── qa_test_stage_agent.py                     QA测试(stage=4)阶段的处理Agent  
│   ├── rd_submit_test_stage_agent.py         提测准入(stage=3)阶段的处理Agent              
│   └── rd_dev_stage_agent.py                      RD开发(stage=2)阶段的处理Agent  
├── build.sh          编译打包脚本  
├── ci.yml             代码库流水线编译配置  
├── common         一些公共的配置  
│   ├── __init__.py  
│   ├── agent_status_enum.py        Agent执行状态枚举  
│   ├── constants.py                        账号密码 接口地址等常量定义  
│   ├── kirin.py                                 麒麟工具类  
│   ├── operate_type_enum.py        操作类型枚举  
│   ├── story_stage_enum.py          需求阶段枚举：开发阶段、提测准入、测试阶段、测试准出、测试完成  
│   ├── testone_utils.py                    TestOne平台常用的数据查询获取工具类  
│   └── tool_status_enum.py           工具执行状态枚举  
├── entity                      一些实体对象定义  
│   ├── __init__.py  
│   ├── parameter.py    请求参数定义  
│   └── result.py            返回结果定义  
├── main.py                  策略执行入口  
├── requirements.txt     依赖管理  
├── run_all_unittest_case.sh                        全量执行单测Case  
├── tests                                                       单测用例管理  
│   ├── ......  
├── tools                                                       所有的工具管理  
     ├── base_tool.py                                     各工具继承的父类  
     ├── qa_test_intercept_tool.py                  QA测试准出拦截工具（自己完善策略）  
     ├── rd_submittest_intercept_tool.py        RD提测准入拦截工具（自己完善策略）  
     └── testone_builtin_tools.py                    各个TestOne内置的策略工具（可直接使用）  

维护者
---
### owners
* wangshitao(wangshitao@baidu.com)

### committers
* wangshitao(wangshitao@baidu.com)

讨论
---
百度Hi交流群：群号


[changelog]: http://icode.baidu.com/repos/baidu/ep-qa/qep_delivery_open_source/blob/master:CHANGELOG.md
