---
title: "交互时序"
description: "当前是百度 APP 极速版存钱罐业务，需求围绕当前场景展开，该业务场景 策略方向 开发主要包含以下3个代码库："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\158\\repo_role.md"
---
当前是百度 APP 极速版存钱罐业务，需求围绕当前场景展开，该业务场景 策略方向 开发主要包含以下3个代码库：

1. 代码库 `baidu/explorer/jst` 是存钱罐策略服务代码库，主要用来下发任务或者活动的奖励策略，策略包含数值、类型、人群、活跃度等； 该库是多业务共用库，请注意"模块范围"小节的业务文件范围
2. 代码库 `baidu/uts-strategy/incentiveauthorize` 是存钱罐目标人群服务代码库，主要用来判断用户是否存钱罐目标用户，只有目标用户才能参与存钱罐活动；该库是多业务共用库，请注意"模块范围"小结的业务文件范围
3. 代码库 `baidu/mainline/dd-video` 是存钱罐的模型代码库，主要用来构建模型，涉及到模型的训练和推理，并提供交付结果


# 交互时序
可能存在的交互时序
→ Server发送请求至jst
→ Server发送请求至incentiveauthorize