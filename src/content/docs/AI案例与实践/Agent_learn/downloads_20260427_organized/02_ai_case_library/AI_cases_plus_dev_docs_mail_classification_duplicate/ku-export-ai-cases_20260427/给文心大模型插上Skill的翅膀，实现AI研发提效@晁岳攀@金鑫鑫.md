---
title: "Example with default OpenAI model (gpt-4o)"
description: "给文心大模型插上Skill的翅膀，实现AI研发提效@晁岳攀@金鑫鑫"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\给文心大模型插上Skill的翅膀，实现AI研发提效@晁岳攀@金鑫鑫.md"
---
给文心大模型插上Skill的翅膀，实现AI研发提效@晁岳攀@金鑫鑫

#### 🧑‍🏫 案例作者：[@晁岳攀](https://ku.baidu-int.com?t=mention&mt=contact&id=6b05c720-fce0-11f0-9a90-9763fae61c54)[@金鑫鑫](https://ku.baidu-int.com?t=mention&mt=contact&id=6d879000-fce0-11f0-9a90-9763fae61c54)
#### 🎬 案例场景：开发
#### 🔧 使用工具：其他
#### 📒 案例概要：本文介绍Claude Skills功能扩展机制及goskills库的应用。Claude Skills允许用户通过包含指令、脚本和资源的文件夹为Claude添加自定义能力，采用渐进式披露设计提升效率。goskills库将此能力扩展到文心、千问等其他大模型，可解析SKILL.md获取元数据和指令。文章以生成MySQL建表SQL技能为例，展示如何开发技能并通过skill-runner调用执行，输出符合规范的建表语句。这为AI研发提效提供了新思路，实现一次开发、反复使用的技能复用模式。
### 创作者简介——[@晁岳攀](https://ku.baidu-int.com?t=mention&mt=contact&id=4497ad90-ca79-11f0-83a0-7f7b019483f2)[@金鑫鑫](https://ku.baidu-int.com?t=mention&mt=contact&id=4785f3e0-ca79-11f0-83a0-7f7b019483f2)
Hi. 大家好，我们是『智能体研究社』的成员。

『智能体研究社』是厂内对AI应用和智能体有浓厚兴趣的同学自发组织的学习社团，也欢迎你的加入。我们会跟进业界对AI应用的最新进展、分享AI在产品的实际应用，组织学习和开发AI开源项目等。 交流和合作可联系[@晁岳攀](https://ku.baidu-int.com?t=mention&mt=contact&id=576d08f0-ca85-11f0-83a0-7f7b019483f2)

**欢迎星标本文、评论区点赞、投币、留言** [🔍点击此处了解更多AI+社区](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)** **[👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)

[文档目录]
Claude Skills (技能) 是 Anthropic 推出的一种功能扩展机制,允许用户为 Claude 添加自定义的能力和工具。Claude 可以使用技能来提升其执行特定任务的表现。技能是包含指令、脚本和资源的文件夹，Claude 在需要时可以加载它们。

Claude 只会在和任务有相关性时才会访问特定的技能。使用技能时，Claude 在处理专业任务（如创建电子表格和演示文稿 ）方面表现更佳，就像我们常说的『专业的人干专业的事』



在处理任务时，Claude 会扫描所有可用技能以找到相关匹配项。当找到匹配项时，它仅加载所需的最小信息和文件——这既保证了 Claude 的快速响应，又能够访问专业领域的知识。



使用MCP工具时， Claude处理任务都会把MCP的信息附加到请求消息中，这会导致每次调用上下文都非常的庞大，但是技能就不一样，Claude 调用特定的技能的时候，它仅加载所需的最小信息和文件——这既保证了 Claude 的快速响应，又能够访问专业领域的知识。



技能具有以下的优点

* 易于开发和维护：开发者只需要编写SKILL.md文件和相关的脚本即可
* 可组合：技能可以堆叠使用。Claude 会自动识别所需的技能并协调它们的使用。
* 高效：仅在需要时加载所需内容。
* 强大：技能可以包含可执行代码，用于任务，而传统编程比令牌生成更可靠。



网上已经有很多的文章介绍它了，我们这篇文章就不赘述了。 Claude 官方还列出了技能的优点，被我从上面的列表中删除了，它是：

* 可移植：技能在所有地方都使用相同的格式。**一次构建，可在 Claude 应用、Claude Code 和 API 中跨平台使用**。



这一条对于Claude (背后的 **Anthropic 公司**)来说的确是个好特性，但是对于其他大语言模型来说，就不是那么好了。技能这么好的一个功能却不能被其他大模型使用，只能局限于Claude生态圈，这是很大的一个遗憾。



技能能不能结合其他大模型使用？一个星期前我们不得不说： **不能！**，但是转机来了。

## 连通其他大语言模型的桥梁 -  goskills 库
Claude在国外使用广泛，但是基于创始人以及他们公司对待中国的态度等众所周知的原因，在国内并没有得到广泛应用，主要还是一些开发者眼馋他的代码能力。



上周出现了一个可以将技能应用到其他大语言模型(兼容open API): [https://github.com/smallnest/goskills](https://github.com/smallnest/goskills), 彻底解决了我们的痛点，现在我们可以轻轻松松的使用文心 + 技能进行AI提效了。



goskills 是一个Go语言的库和工具，它实现了下面的功能：

* 解析 `SKILL.md` ，获取它的元数据和指令
* 抽取 YAML 头信息到Go结构体 `SkillMeta`
* 捕获技能的markdown信息
* 发现 `scripts/`, `references/`, and `assets/`等技能的资源目录



同时，它还提供了两个工具：

* skill-cli: 一个inspector工具，可以透视技能目录和技能
* skill-runner: 一个可以调用技能的 agent



你可以使用下面的命令导入这个库：

```
go get github.com/smallnest/goskills
```


### 作为库使用
 goskills作为库，提供了两个重要的函数：

* ParseSkillPackage： 解析单个的技能
* ParseSkillPackages：解析某个文件夹下的多个技能



让我们分别介绍它们。

#### ParseSkillPackage：解析单个技能
下面是一个如何使用 `ParseSkillPackage` 库中的 `goskills` 函数来解析某个技能目录的示例。在goskills的examples/skill目录中，有Claude官方提供的一些技能，让我们尝试解析 artifacts-builder 这个技能：

```
package main

import (
    "fmt"
    "log"

    "github.com/smallnest/goskills"
)

func main() {
    // 要解析的技能的目录
    skillDirectory := "./examples/skills/artifacts-builder"

    skillPackage, err := goskills.ParseSkillPackage(skillDirectory)
    if err != nil {
        log.Fatalf("Failed to parse skill package: %v", err)
    }

    // 解析到的技能的信息
    fmt.Printf("Successfully Parsed Skill: %s\n", skillPackage.Meta.Name)
    // ... and so on
}
```
#### ParseSkillPackages：解析技能集合
要在目录及其子目录中查找并解析所有有效的技能包，您可以使用 `ParseSkillPackages` 函数。它递归地扫描给定路径，识别所有包含 `SKILL.md` 文件的目录，并返回一个成功解析的 `*SkillPackage` 对象切片。



```
package main

import (
    "fmt"
    "log"

    "github.com/smallnest/goskills"
)

func main() {
    // 包含技能的目录
    skillsRootDirectory := "./examples/skills"

    packages, err := goskills.ParseSkillPackages(skillsRootDirectory)
    if err != nil {
        log.Fatalf("Failed to parse skill packages: %v", err)
    }

    fmt.Printf("Found %d skill(s):\n", len(packages))
    for _, pkg := range packages {
        fmt.Printf("- Path: %s, Name: %s\n", pkg.Path, pkg.Meta.Name)
    }
}
```




### 命令行工具


goskills 提供两个独立的命令行工具。



#### 技能审查员 ( `goskills-cli` )
这个工具位于 `cmd/skill-cli` ，该工具帮助您检查和管理本地 Claude 技能。

您可以从项目根目录构建可执行文件：

```
go build -o goskills-cli ./cmd/skill-cli
```


以下是 `goskills-cli` 可用的命令：

* **list**: 列出指定目录中所有有效的技能。例如 `./goskills-cli list ./examples/skills`
* **parse**: 解析单个技能并显示其结构摘要。例如 `./goskills-cli parse ./examples/skills/artifacts-builder`
* **detail**:显示单个技能的完整详细信息，包括完整的内容体。例如 `./goskills-cli detail ./examples/skills/artifacts-builder`
* **files**: 列出构成技能包的所有文件。；例如 ./goskills-cli files ./examples/skills/artifacts-builder
* **search**：在目录中按名称或描述搜索技能。搜索不区分大小写。./goskills-cli search ./examples/skills "web app"



![](/personal-site-mvp/img/doc-placeholder.svg "")
你可以把这个命令行集成到你的应用在， 比如Comate代码工具、各种智能体等等。



#### 技能运行器 CLI ( `goskills-runner` )
位于 `cmd/skill-runner` ，该工具通过与大型语言模型（LLMs）如 OpenAI 的模型集成，模拟了 Claude 技能使用的流程。

您可以从项目根目录构建可执行文件：

```
go build -o goskills-runner ./cmd/skill-runner
```


它的run命令实现了一个简单的Agent:

* 首先发现可用的技能，然后询问 LLM 选择最合适的技能，最后将选中技能的内容作为系统提示输入 LLM 来执行用户请求。
* 如果技能包含网页的模板，会根据技能的指令使用这些模板
* 如果技能包含shell、python等一些脚本，会根据技能的需要调用这些脚本



下面是使用openai和千帆平台上的deepseek模型服务来执行"algorithm art" 这个技能：

```
# Example with default OpenAI model (gpt-4o)
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
./goskills-runner run "create an algorithm that generates abstract art"

# Example with a custom OpenAI-compatible model and API base URL
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
./goskills-runner run --model deepseek-v3 --api-base https://qianfan.baidubce.com/v2 "create an algorithm that generates abstract art"
```


![](/personal-site-mvp/img/doc-placeholder.svg "")


接下来，让我们开发一个AI研发提效的技能，并使用文心模型 + goskills-runner 来使用。

## 基于 Skills 的提效工具
在日常业务开发过程中，不可避免地会遇到创建表结构并转换为各自语言或框架的 ORM 对象的需求。一般情况下，我们可以自行编写 SQL 或者通过图形化工具来建表。同时需要额外考虑自动是否允许 NULL，默认值如何设置，添加默认的 created_at 和 updated_at 字段。以前还有一些同学通过 excel 的方式定义字段，然后再利用 python 脚本生成表。这种方式都落伍啦。我们可以基于 Skills 的方式来做。一次开发，反复使用。



为了解决上面的痛点，我们编写了一个生成数据库建表SQL的 Claude SKILL，结合上面介绍的goskills工具吗，实现AI 研发提效。

## 编写快速建表技能
新建一个目录 gen-mysql-table，作为我们要开发的技能的目录：

```
./gen-mysql-table
./gen-mysql-table/SKILL.md
```


接下来我们编写这个技能的SKILL.md, 这个是技能必须的文件：

```
---
name: 生成 MySQL 的建表 SQL 语句。
description: 基于用户对表的信息，字段，索引，外键等描述生成一个 MySQL 的标准建表SQL 语句。
---

# 生成规范

## 所有字段必须设置为 NOT NULL。
## 当表的字段定义没有显式指定默认值的时候，请根据字段类型推理出默认值并通过 DEFAULT 关键字进行设置。
## 通过 varchar 定义的字段默认值设置为空字符串（""），其他数值类型根据各自类型的零值并进行设置。
## 自动增加 created_at 和 updated_at 字段，其中 created_at 创建时默认值为 CURRENT_TIMESTAMP， updated_at 更新时默认值为 CURRENT_TIMESTAMP。
## 使用 UNIQUE KEY 关键字设置表的唯一性索引。
## 使用 KEY 关键字设置表的普通索引。
## 使用 ENGINE 关键字设置表的存储引擎为 InnoDB。
## 使用 DEFAULT CHARSET 关键字设置表的默认字符集为 utf8mb4。
## 使用 COMMENT 关键字设置用户指定的表注释。
## 除了 created_at 和 updated_at 以外，不要自行添加未定义的字段，索引，外键。

# 返回格式

请直接返回建表的 SQL 语句。不需要任何其他信息。
```


接下来我们编写用户表的信息， 这个信息我们保存在 issues/1.create-table.md 文件中：

```
以下为用户表定义。

# 表名

product_assistant_usage_record

# 表注释

质效助手使用记录

# 表字段

## id bigint(11) auto_increment primary_key comment "自增主键"
## username varchar(32) comment "用户账号"
## chat_source varchar(10) comment "消息渠道"
## user_input varchar(1024) comment "用户输入文本"
## output_msg varchar(4096) comment "响应的正常信息"
## output_err varchar(1024) comment "响应的错误信息"
## elapsed_seconds decimal(5,2) comment "响应耗时（单位：秒）"

# 表索引

## idx_chat_bot (chat_source asc, username asc)
```


万事俱备了，现在就差临门一脚。接下来我们把信息传递给skill-runner， 我们期望它调用我们开发的gen-mysql-table技能，最终输出SQL语句(这里我们使用的是 deepseek-v3.2 大模型)：

```
$ export OPENAI_API_KEY="你的apiKey"
$ cat issues/1.create-table.md | skill-runner run --api-base http://llms-se.baidu-int.com:8200 --model deepseek-v3.2 -d ./

样例输出：
根据提供的用户表定义，以下是符合规范的建表 SQL 语句：

```sql
CREATE TABLE `product_assistant_usage_record` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `username` varchar(32) NOT NULL DEFAULT '' COMMENT '用户账号',
  `chat_source` varchar(10) NOT NULL DEFAULT '' COMMENT '消息渠道',
  `user_input` varchar(1024) NOT NULL DEFAULT '' COMMENT '用户输入文本',
  `output_msg` varchar(4096) NOT NULL DEFAULT '' COMMENT '响应的正常信息',
  `output_err` varchar(1024) NOT NULL DEFAULT '' COMMENT '响应的错误信息',
  `elapsed_seconds` decimal(5,2) NOT NULL DEFAULT '0.00' COMMENT '响应耗时（单位：秒）',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_chat_bot` (`chat_source` ASC, `username` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='质效助手使用记录';
```
```


最后，成功的调用了gen-mysql-table技能，输出来建表SQL。

## 总结
Claude Skills 虽好，但是只能在Claude生态圈使用。我们介绍了一个新出现的goskills库，可以让我们在使用文心、千问、deepseek等大模型的时候，也能够使用丰富多彩、功能强大的Claude Skills。

最后，我们给出了一个厂内使用Claude Skills的例子：一个可以帮助按照需求，生成建表SQL的工具，展示了技能的强大功能。



以下是网友贡献的各种技能包，可以下载下来使用：

* [anthropics/skills](https://github.com/anthropics/skills)
* [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
* [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
* [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills)
* [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)

## 免费的模型服务
如果你苦于没有模型服务做测试，可以使用厂内免费的panda平台提供的免费额度。



厂内panda的API KEY 和各种模型的名称可以参考文档：[API_KEY获取](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/SCIE54A-T7/6qJ4FFzH-H/GX-Pwx0hu95OKN?t=mention&mt=doc&dt=doc)。

![](/personal-site-mvp/img/doc-placeholder.svg "")


 api-base请使用 http://llms-se.baidu-int.com:8200



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
