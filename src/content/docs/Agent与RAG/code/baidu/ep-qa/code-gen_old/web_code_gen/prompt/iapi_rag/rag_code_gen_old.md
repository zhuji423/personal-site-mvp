---
title: "需要你根据`用户需求`生成符合输出要求的gdp框架接口代码"
description: "下面是一些可参考的文件路径以及代码： <files {{filecodes}} </files"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\iapi_rag\\rag_code_gen_old.md"
---
# 需要你根据`用户需求`生成符合输出要求的gdp框架接口代码
可参考的接口注册写法，其中业务逻辑省略：
<struct>
{{struct_codes}}
</struct>

下面是一些可参考的文件路径以及代码：
<files>
{{file_codes}}
</files>

不要引入无关代码，请简洁回答

# 输出要求
 - 给出生成的代码，以及文件路径
 - 写全代码，禁止省略代码
 - 不要生成需求无关注释内容

## 代码规范
 - 所有方法、结构体、变量均必须参照示例遵循对应的驼峰命名方式，特别注意缩写词如`http`、`api`、`id`、`uid`、`cuid`等在命名时必须大写，示例：以`testuid`为例，驼峰命名`TestUID`

# 用户需求：
## 需要你根据用户需求生成gdp框架接口代码（依次生成router层、controller层、types层、service层代码）：
若接口描述为空，业务逻辑省略
若代码逻辑简单，service层代码可不实现
{{req}}