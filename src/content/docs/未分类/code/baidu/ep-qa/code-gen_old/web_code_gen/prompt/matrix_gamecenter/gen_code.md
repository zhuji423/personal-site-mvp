---
title: "目标"
description: "const TestName = \"xxx\" // 业务逻辑实现过程中涉及到的常量定义 {{mysqlconsts}} {{redisconsts}} {{gcpconsts}} {{errno}} gdp框架项目结构参考（仅供参考理解，项"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\matrix_gamecenter\\gen_code.md"
---
# 目标
你是一个go语言开发工程师，你需要基于gdp框架，采用MVC模式，深入解析需求描述的内容，按步骤生成对应完整的逻辑代码：
``` 
{{requirement}}
```
{{name_rules}}

# gdp框架代码示例，请解析需求内容，参考代码示例层级顺序生成对应代码：
* 请深入解析需求描述中的接口逻辑，参照示例指定项目结构，根据理解逐步在相应层级的文件中尽可能完整地生成逻辑代码
{{controller}}
{{router}}
{{service}}
{{data}}
## 底层数据操作逻辑
* 根据需求进行解析，仅生成需要用到的对应底层数据操作逻辑和相关配置代码，不需要生成的部分跳过即可
{{resource}}
### dao层（db、redis、gcp相关底层数据操作）
{{mysql}}
{{gcp}}
{{redis}}
{{ral}}
{{types}}
## 常量定义
* 请根据需求解析，生成需求要用到的对应的常量定义文件，不要生成无关文件
* 所有生成的常量定义需根据需求生成对应的注释信息
### 业务相关常量定义，文件路径：`model/consts/srv/包名.go`
* 此文件必须生成注释
```go
package srv

const (
    TestName = "xxx"  // 业务逻辑实现过程中涉及到的常量定义
)
```
{{mysql_consts}}
{{redis_consts}}
{{gcp_consts}}
{{errno}}
# gdp框架项目结构参考（仅供参考理解，项目结构无需生成输出）：
{{frame}}
                  
{{name_rules}}

# 生成要求:
## 特别注意，controller层的 入参: context.Context和ghttp.Request，  出参: ghttp.Response
## 示例代码中testXXX代表示例名，文件名、方法名等需要根据需求改成实际的名字， 如TestFile.go需要根据描述改成相关的File名, Test变量也需要响应修改
## gcp Fetch函数中的 T 为GCP配置的完整结构体
## 接口路径占位、包名、基础功能名、功能名等根据需求要求自定义，如果需求中指定，优先按照指定的名字，`游戏模块名`默认是`dto`，若指定则按指定命名
## 请深入解析需求描述中的接口逻辑，参照示例指定项目结构，不要生成示例，根据理解逐步在相应层级的文件中尽可能完整地生成需求对应逻辑代码
## 特别注意缩写词如http、api、id、uid、cuid等在命名时必须大写，示例：以`uid`为例，驼峰命名`TestUID`
## 注意所有生成的结构体及其变量、常量必须生成一对一对应的注释，其中要导出的方法、结构体必须采用`//方法名 ...`、`//结构体名 ...`的方式进行注释

# 输出要求：
    给出生成的代码，以及文件路径
    写全代码，禁止省略代码

# 输出格式参考如下：
文件路径：`具体文件路径`
```go
```