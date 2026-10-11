---
title: "输入研发设计文档"
description: "请你根据输入的研发设计文档内容，提取涉及的接口信息，生成一份完整的“总体设计表格”，用于研发协作和评审。 注意：仅生成总体设计表格，禁止输出任何额外解释信息。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\trd_generator\\gen_overview.md"
---
请你根据输入的研发设计文档内容，提取涉及的接口信息，生成一份完整的“总体设计表格”，用于研发协作和评审。
注意：**仅生成总体设计表格，禁止输出任何额外解释信息**。

# 输入研发设计文档
```markdown
{{dsls}}
```


# 输出格式
* 总体设计表请使用如下格式，要求表格结构标准、字段不省略、不折行、字段说明明确、表头加粗，代码库、接口路径字段值相同的行在对应列进行合并处理，示例如下：

| **目标代码库**                                                                                                                                  | **接口名称** | **接口路径**                             | **改动类型** | **功能点概述**                                       | **关联度得分** |
|---------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------|--------------|-------------------------------------------------|-----------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)                     | 奖励信息转发 | `/baiduboxapp/basic/packet/get`           | 修改         | - 通过用户某种行为触发后，<br>后端通过 xxx 方式获取奖励信息。<br>- 最终返回统一结构供前端展示。 | 0.9       |
| [baidu/searchbox/ugact](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/ugact/tree/master)                               | 用户订单展示 | `/baiduboxapp/ugact/info/show`            | 新增         | - 新增xxx 用户信息展示内容。<br>- 内容由服务端根据策略动态返回，供页面展示与埋点。 | 0.8       |