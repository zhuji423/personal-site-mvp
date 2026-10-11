---
title: "derive 配置派生的值文件"
description: "使用配置派生功能，可以实现一份配置在不同的环境（如机房）实际生效的配置值不同，如下述 IDC 字段， 在 tucheng 机房值为 tc，在 nanjing 机房值为 nj。"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\code_trans\\myapp\\conf_online\\derive\\README.md"
---
# derive 配置派生的值文件

使用配置派生功能，可以实现一份配置在不同的环境（如机房）实际生效的配置值不同，如下述 IDC 字段，
在 tucheng 机房值为 `tc`，在 nanjing 机房值为 `nj`。

gdp/conf@v1.22.0 开始内置支持配置派生功能，如：
```toml
IDC = "<$idc$>"
```
即在配置文件中使用 `<$idc$>` 这种语法来引用读取派生的变量。  

注意事项：
1. 一般情况下，一个机房对应一个配置目录，`default` 为最终兜底默认配置。  
2. 上线前，请按照实际部署情况补齐配置文件和目录。


更多内容详见文档：http://gdp.baidu-int.com/api/baidu/gdp/conf/
