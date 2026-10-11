---
title: "gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码："
description: "你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码： {{requirement}} gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码： {{contr"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_ugact\\gen_code.md"
---
你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码：
{{requirement}}
# gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码：
{{controller}}
{{router}}
## 业务逻辑代码
{{service}}
{{service_types}}
{{gcp}}
{{data}}
{{data_types}}
{{resource}}
{{ral}}
### 错误码配置，文件路径：`library/errno/包名.go`
* 注意常量等生成时需要生成对应注释
```go
package errno

var (
    ErrTest = newCodeError(10000, "测试错误")  // 测试错误
)
```
# gdp框架项目结构参考（仅供参考理解，项目结构无需生成输出）：
{{frame}}

# 生成要求:
## 特别注意，controller层的 入参: context.Context和ghttp.Request，  出参: ghttp.Response
## 示例代码中testXXX代表示例名，需要根据需求改成实际的名字， 如TestFile.go需要根据描述改成相关的File名, Test变量也需要响应修改
## gcp Fetch函数中的 T 为GCP配置的完整结构体
## 包名、功能名根据需求自定义，如果需求中指定，优先按照指定的名字
## 请深入解析需求描述中的接口逻辑，参照示例指定项目结构，不要生成示例，根据理解逐步在相应层级的文件中尽可能完整地生成需求对应逻辑代码
## 所有文件必须采用小写、下划线的方式进行命名
## 所有变量、函数、结构体均必须参照示例遵循对应的驼峰命名方式（db数据库变量&表名命名除外），特别注意缩写词如http、api、id、uid、cuid等在命名时必须大写，示例：以`uid`为例，驼峰命名`TestUID`
## 注意所有生成的结构体及其变量、常量必须生成一对一对应的注释，其中导出的函数、结构体必须采用`//方法名 ...`、`//结构体名 ...`的方式进行注释

# 输出要求
    给出生成的代码，以及文件路径
    写全代码，禁止省略代码

# 输出格式参考如下：
文件路径：`具体文件路径`
```go
```