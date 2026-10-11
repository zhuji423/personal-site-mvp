---
title: "什么是 Zulu？"
description: "Zulu 在 Web 前后端开发中的实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Zulu 在 Web 前后端开发中的实践.md"
---
Zulu 在 Web 前后端开发中的实践

#### 🧑‍🏫 案例作者：[@李智](https://ku.baidu-int.com?t=mention&mt=contact&id=551a1b50-fce5-11f0-96d6-a1a7cbb15db0)[@刘志鹏](https://ku.baidu-int.com?t=mention&mt=contact&id=5974e9f0-fce5-11f0-96d6-a1a7cbb15db0)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了Zulu在Web前后端开发中的实践应用，Zulu作为文心快码推出的自动编程智能体，具备强大的全自然语言交互能力，能够理解复杂任务并进行分解执行。文章通过具体案例展示了Zulu在Web前端快速搭建项目、已有项目迭代中的表现，以及在Web后端快速搭建项目和需求迭代中的能力，体现了Zulu自助任务执行和反思能力对研发效率的显著提升。
# 什么是 Zulu？
Zulu 是文心快码（Baidu Comate）全新推出的自动编程智能体，旨在让编程变得简单、直观。它提供从代码生成到业务理解的完整智能服务，让你无需任何开发经验也能轻松创建软件、网站和游戏。

![Zulu](/personal-site-mvp/img/doc-placeholder.svg "Zulu")
# Zulu 能做什么？
Zulu 拥有强大的全自然语言交互能力，用户可以通过自然语言与 Zulu 沟通需求。它还具备规划与反思能力，可以理解复杂任务并进行分解，逐步完成。

Zulu 还能调用丰富的工具，例如代码搜索、命令执行等，来辅助编程过程。

## Zulu 的基本逻辑
Zulu的核心是通过工具调用，将IDE中与问题分析和代码编辑有关的能力暴露给LLM，由LLM进行思考、规划并使用这些工具，基于每一次工具的结果进一步推进问题的解决，直到LLM认为问题全部解决后给出总结并停止循环。

[流程图]
一类典型的Zulu处理问题流程：

[流程图]
# 实践
## Web 前端 [@刘志鹏](https://ku.baidu-int.com?t=mention&mt=contact&id=079d4d60-88ab-11f0-a369-1d268abc1763)
### 从零快速搭建前端框架
指定技术栈生成项目

#### 提示词
以react、react-router v6、mobx、axios为基础技术栈，并且使用monorepo进行管理，生成前端代码库，代码库名称为comate-fe-demo

* 初始规划

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 执行过程
    * 创建项目

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 安装依赖

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 使用pnpm管理

![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 初始化主应用目录及相关代码文件

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 上述任务异常后，继续上述任务

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 未指定构建的情况下，自动生成构建工具

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 执行结果
![](/personal-site-mvp/img/doc-placeholder.svg "")
* 代码库运行
    * pnpm dev报错


```
解决报错 failed to load config from /Users/liuzhipeng/vscodespace/baidu/ai/content-audit-front/comate-fe-demo/packages/app/vite.config.js
error when starting dev server:
Error [ERR_REQUIRE_ESM]: require() of ES Module /Users/liuzhipeng/vscodespace/baidu/ai/content-audit-front/comate-fe-demo/node_modules/.pnpm/vite@7.1.4/node_modules/vite/dist/node/index.js from /Users/liuzhipeng/vscodespace/baidu/ai/content-audit-front/comate-fe-demo/packages/app/vite.config.js not supported.
Instead change the require of index.js in /Users/liuzhipeng/vscodespace/baidu/ai/content-audit-front/comate-fe-demo/packages/app/vite.config.js to a dynamic import() which is available in all CommonJS modules.
    at _require.extensions.<computed> [as .js] (file:///Users/liuzhipeng/vscodespace/baidu/ai/content-audit-front/comate-fe-demo/node_modules/.pnpm/vite@7.1.4/node_modules/vite/dist/node/chunks/dep-C6pp_iVS.js:36641:9)
    at Object.<anonymous> (/Users/liuzhipeng/vscodespace/baidu/ai/content-audit-front/comate-fe-demo/packages/app/vite.config.js:36:19)
    at _require.extensions.<computed> [as .js] (file:///Users/liuzhipeng/vscodespace/baidu/ai/content-audit-front/comate-fe-demo/node_modules/.pnpm/vite@7.1.4/node_modules/vite/dist/node/chunks/dep-C6pp_iVS.js:36640:44)
```
    * 解决报错

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 启动项目

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 已有 WEB 项目需求迭代
#### 项目上手
##### 提示词
```
梳理项目中主要业务流程尤其是策略管理、审核过程
```
##### 结果
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
    * 继续追问

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 结论
对已有项目的业务分析部分可用

#### 需求迭代
##### Figma涉及稿 -> 代码
###### 能力调用
![](/personal-site-mvp/img/doc-placeholder.svg "")
###### 生成效果
![](/personal-site-mvp/img/doc-placeholder.svg "")
###### 结论
生成代码样式正确，但是当前代码库结构分析错误

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 结论
代码库生成可用，已有代码库业务分析较为浅显，对业务梳理作用有限，但在技术框架分析方面则效果较好

#### 缺点
* 无法准确识别项目代码库，切换代码库后，在新代码库下检索，还是去查找旧代码库
* 生成过程部分操作不生效，如下图点击叉号不生效

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 稳定性不太好

![](/personal-site-mvp/img/doc-placeholder.svg "")
## Web 后端
### 从零快速搭建 WEB 项目
基于给定的 JSON Schema 生成 WEB 项目中常用的 controller、service、dao

#### 提示词
```
基于这个学生成绩表的JSON Schema，快速生成Springboot项目，包括controller、service、dao层，dao层可以使用SpringDataJPA，快速搭建项目。JSON Schema如下：

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "学生成绩表",
  "description": "存储学生基本信息及各科成绩的结构定义",
  "type": "array",
  "items": {
    "type": "object",
    "required": ["id", "name", "gender", "grade", "scores"],
    "properties": {
      "id": {
        "description": "学生唯一标识符",
        "type": "string",
        "pattern": "^[A-Za-z0-9]{5,10}$"
      },
      "name": {
        "description": "学生姓名",
        "type": "string",
        "minLength": 1,
        "maxLength": 20
      },
      "gender": {
        "description": "学生性别",
        "type": "string",
        "enum": ["男", "女", "未知"]
      },
      "grade": {
        "description": "学生年级",
        "type": "integer",
        "minimum": 1,
        "maximum": 12
      },
      "class": {
        "description": "学生班级",
        "type": "string",
        "pattern": "^[0-9]{1,2}$"
      },
      "birthDate": {
        "description": "学生出生日期",
        "type": "string",
        "format": "date"
      },
      "scores": {
        "description": "各科目成绩",
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "required": ["score", "fullMark"],
          "properties": {
            "score": {
              "description": "科目得分",
              "type": "number",
              "minimum": 0
            },
            "fullMark": {
              "description": "科目满分值",
              "type": "integer",
              "minimum": 50,
              "maximum": 150
            },
            "comment": {
              "description": "成绩评语",
              "type": "string",
              "maxLength": 100
            }
          }
        }
      },
      "totalScore": {
        "description": "总成绩",
        "type": "number"
      },
      "rank": {
        "description": "班级排名",
        "type": "integer",
        "minimum": 1
      }
    }
  }
}
```
过程中，Zulu 首先会拆解任务，并且尝试从远程拉去项目骨架，发现无法访问网络后，采用人工创建的方式

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
接下来，便开始进行项目搭建，从实体类的定义，到项目的配置文件，最终增加对应的API层、数据层、数据访问层的代码，并提供了项目的启动命令和数据库访问

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 结果
在 2min 内，完成了整个项目的搭建，并按要求完成了API接口的封装，可快速验证业务逻辑

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 已有 WEB 项目需求迭代
对于已有项目，如果不了解项目代码的话，可以通过 Zulu 快速了解代码逻辑、架构、业务流程等。

#### 项目上手
##### 提示词
```
介绍项目的业务目标、核心功能、整体架构、数据实体、业务流程
```
##### Zulu 的分析
Zulu 分析这个当前项目的业务目标、核心功能、整体架构、数据实体和业务流程。从项目的主要配置文件和入口点开始了解项目结构。

![](/personal-site-mvp/img/doc-placeholder.svg "")
并对项目的核心功能、架构、实体等做整理和总结

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
最终给出项目的业务流程，帮助开发者快速上手项目

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 需求迭代
##### 提示词
```
我了解这个项目了，下面帮我实现一个新的需求：解析任务列表，需要支持
* 分页
* 按resourceName的模糊匹配
* 按createTime的排序
* 需要实现对应的controller、service和dao层代码
* api放在ParserTaskController内
```
##### Zulu 的分析
Zulu 会了解当前的数据访问方法，当前的服务层逻辑，项目中已有的数据传输对象结构等信息

![](/personal-site-mvp/img/doc-placeholder.svg "")
基于分析的结论，生成需求代码

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 结果
按要求，在 ParserTaskController 中增加列表查询接口，并新增了对应的业务层和数据访问层的代码。

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 结论
Zulu 具备自助任务执行和反思能力，能够端到端从需求生成代码。会依据代码库的实际情况动态调整规划和执行的过程，确保生成效果，大大降低RD在实际开发中的人力投入，提升研发速度和效率。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
