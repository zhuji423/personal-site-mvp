---
title: "rule"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\matrix\\sub_common\\rule.md"
---
## service层、data层、dao层等层生成的导出方法需在对应层交互入口文件添加导出方法声明。
## 深入理解分析controller、service、data、dao等层导包&函数调用链路信息，明确对应层用到的`Newxxx`初始化对象是否已完成定义：
* 若已完成定义，直接通过`层级.Newxxx()`获取初始化对象即可；
* 否则，若未定义，需要生成对应层`Newxxx`初始化对象的定义代码；