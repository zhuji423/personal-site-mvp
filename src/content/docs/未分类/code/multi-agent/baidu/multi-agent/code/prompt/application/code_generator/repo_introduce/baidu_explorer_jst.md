---
title: "当前代码库"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\baidu_explorer_jst.md"
---
# 当前代码库
baidu/explorer/jst这是一个存钱罐业务策略实现代码库，主要提供对内部服务，实现存钱罐业务策略逻辑，供ug_duoduo服务调用
- **相关的目录层级及文件**
  - uts:
    - incentivetasksystem: 极速版存钱罐&任务系统的策略代码文件夹，不同的业务以不同的文件名前缀区分，存钱罐业务以video_act_为前缀
      - video_act_main.go: 存钱罐任务的主入口，支持以下功能：1）根据任务ID来分发到不同的业务策略 2）从dmp转换数据 3）参数定义和转发
  - library:工具层，主要封装通用的工具方法，提供给业务调用。
    - consts：amis需求实验项的key定义，根据不同的key获取不同的实验配置
- 使用建议：
  - 没有在上面列举出来的位置，即为非存钱罐业务，请不要变更