---
title: "当前代码库"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\baidu_uts-strategy_incentiveauthorize.md"
---
# 当前代码库
baidu/uts-strategy/incentiveauthorize这是一个存钱罐业务目标人群服务实现代码库，主要提供对内部服务，实现存钱罐目标人群识别能力，供ug_duoduo和sbox-basic服务调用
- **相关的目录层级及文件**
strategyies/incentiveauthorize: 目录，请注意，存钱罐目标服务逻辑在该目录下：
  - baiduboxlite_control.go: 极速版目标服务的人群判定的主要代码逻辑文件，方法入口是ProcessAppID2 
  - baiduboxlite_xx.go：以`baiduboxlite_`为前缀的文件，是极速版存钱罐目标人群服务相关的代码文件，其他前缀的不是 
  - constant.go: 常量定义文件 
  - dataprovider.go: 数据转换层，例如DMP转换成字段 
  - strategy.go：结构定义文件 
  - util.go：工具类和方法