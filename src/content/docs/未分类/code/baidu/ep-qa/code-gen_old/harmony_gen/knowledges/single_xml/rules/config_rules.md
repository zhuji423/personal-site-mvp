---
title: "config_rules"
description: "1. 配置命名&内容转换： 注意：若数值变量命名或数值中存在dp关键词，需注意变量名或数值中dp到vp关键词的转换 不含dp关键词的变量名直接映射即可 2. 配置文件的输出路径，需根据输入路径产生对应变化： 常规转换到对应场景的base文件"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\harmony_gen\\knowledges\\single_xml\\rules\\config_rules.md"
---
1. 配置命名&内容转换：
* 注意：若数值变量命名或数值中存在`dp`关键词，需注意变量名或数值中`dp`到`vp`关键词的转换
* 不含`dp`关键词的变量名直接映射即可
2. 配置文件的输出路径，需根据输入路径产生对应变化： 
* 常规转换到对应场景的`base`文件路径下，如：`test-template/src/main/res/values/strings.xml`->`entry/src/main/resources/base/element/test_template_string.json`
* 若输入路径中带`night`、`dark`等代表夜间的关键词，则转换到对应场景的`dark`文件路径下，如：`test-styles/src/main/res/values-night/dimens.xml`->`entry/src/main/resources/dark/element/test_styles_dimen.json`