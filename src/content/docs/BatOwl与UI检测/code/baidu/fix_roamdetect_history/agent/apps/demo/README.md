---
title: "智能执行策略共建demo"
description: "demo: 以业务名命名的目录 autocasegeneratedemo.py: 主执行流程，命名规则是autocasegenerate{业务名}.py afterall.py: 整份用例级别的后置清理可选，如果业务目录没有该文件则会调用默"
date: "2026-10-11"
category: "BatOwl与UI检测"
source: "F:\\百度工作\\01_code\\code\\baidu\\fix_roamdetect_history\\agent\\apps\\demo\\README.md"
---
# 智能执行策略共建demo

## 注意事项
1. 共建时先建立一个名为coop_{module_id}的分支，切勿在master分支开发

## 代码结构
```
demo
 ├── README.md
 ├── autocase_generate_demo.py
 ├── after_all.py
 ├── before_all.py
 ├── after_all
 ├── autocase_kb_engine
 ├── autocase_step_generate
 ├── automated_judgement
 ├── before_all
 ├── before_one
 ├── case_organize
 ├── execute_generate_plan
 ├── execute_quality_assessment
 ├── generate_process_reflect
 ├── generate_process_summary
 ├── manualcase_quality_assessment
 ├── optimize_manual_case_for_execute
 └── special_step_generate
 
demo: 以业务名命名的目录
autocase_generate_demo.py: 主执行流程，命名规则是autocase_generate_{业务名}.py
after_all.py: 整份用例级别的后置清理(可选)，如果业务目录没有该文件则会调用默认after_all
before_all.py: 整份用例级别的前置准备(可选)，如果业务目录没有该文件则会调用默认before_all
after_all: after_all.py实现相关的代码存放目录
autocase_kb_engine: 智能执行策略知识库
autocase_step_generate: 智能执行策略步骤生成，生成下一步操作
automated_judgement: 判断是否可自动化
before_one: 每个用例执行前的前置准备
before_all: before_all.py实现相关的代码存放目录
case_organize: 用例组织目录，用于存放不同的用例组织策略（例如全组合）
execute_generate_plan: 根据生成的下一步操作解析为QAMate步骤格式，并在设备执行
execute_quality_assessment: 整体校验，判断整个执行流程是否完成测试要求，用于最后签章的依据
generate_process_reflect：一步操作执行后对效果的反思
generate_process_summary：执行流程总结，判断有没有执行结束
manualcase_quality_assessment: 手动测试用例质量评估，低质量用例直接过滤不生成
optimize_manual_case_for_execute: 根据当前截图、业务场景知识，优化手动测试用例，增加用例的可读性
special_step_generate: 特殊步骤生成，例如实验命中

```


