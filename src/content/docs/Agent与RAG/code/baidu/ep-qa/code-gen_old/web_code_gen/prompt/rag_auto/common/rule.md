---
title: "rule"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\common\\rule.md"
---
## 生成规范
* 严格保证注释符合规范（如：导出的方法、结构体等对象必须要添加`// TestName ...`格式的注释）。
* 数据库变量&表名命名除外的变量、函数、结构体必须遵循驼峰命名规范，特别注意如HTTP、API、ID、UID、CUID等含义缩写词必须大写，示例：以`UID`为例，驼峰命名`TestUID`。