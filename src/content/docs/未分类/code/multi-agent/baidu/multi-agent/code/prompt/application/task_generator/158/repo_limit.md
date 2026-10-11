---
title: "模块限制"
description: "以下是存钱罐策略方向代码仓库的代码目录和文件限制，请在 理解代码仓库、设计需求方案、生成代码时严格参照，禁止使用、修改不相关的代码和文件："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\158\\repo_limit.md"
---
以下是存钱罐策略方向代码仓库的代码目录和文件限制，请在 理解代码仓库、设计需求方案、生成代码时严格参照，禁止使用、修改不相关的代码和文件：

# 模块限制
1. `baidu/explorer/jst`:
   * library/consts：目录 
     * arm_uts_jst.go：文件，包含实验管理相关的amis配置key 
   * uts/incentivetasksystem：目录，请注意，存钱罐策略内容主要在该目录下 
     * video_act_xxx.go：以`video_act_`为前缀的文件，是存钱罐业务相关文件，其他的不是，请注意区分
2. `baidu/uts-strategy/incentiveauthorize`:
   * strategyies/incentiveauthorize: 目录，请注意，存钱罐目标服务逻辑在该目录下
         1. baiduboxlite_control.go: 极速版目标服务的人群判定的主要代码逻辑文件，方法入口是ProcessAppID2
         2. baiduboxlite_xx.go：以`baiduboxlite_`为前缀的文件，是极速版存钱罐目标人群服务相关的代码文件，其他前缀的不是
         3. constant.go: 常量定义文件
         4. dataprovider.go: 数据转换层，例如DMP转换成字段
         5. strategy.go：结构定义文件
         6. util.go：工具类和方法