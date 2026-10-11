---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "IaaS前端团队Rule实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\IaaS前端团队Rule实践.md"
---
IaaS前端团队Rule实践

#### 🧑‍🏫 案例作者：[@骈瑞杰](https://ku.baidu-int.com?t=mention&mt=contact&id=78903ca0-fcee-11f0-b3b8-9d6a48e824f0)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了IaaS前端团队通过建设完善的Rules来提升Coding Agent生成代码质量的实践。规则涵盖项目规范、技术栈特定规范及业务相关规范，通过多轮对话生成工具库使用文档和业务场景规则，显著提升开发效率。规则可复用并维护在公共代码库中，便于团队持续完善和使用。
## 愿景
![](/personal-site-mvp/img/doc-placeholder.svg "")
通过建设完善的Rules，让Coding Agent生成的代码更加贴合业务的需求

## Rule设计
IaaS前端产品目前主要分为san、react、san+react混合三种技术栈产品，因此设计的rule需要满足这三种产品的业务需求：

```
├── common/ # 通用rule
│   ├── project-standard.mdr #项目通用规范，如：变量命名规范、文件命名规范、目录结构等
│   └── style.mdr #项目样式规范
├── react/ #react技术栈相关rule
│   ├── acud-icon.mdr #react基础icon库相关rule
│   ├── acud.mdr #react基础组件库相关rule
│   ├── service.mdr #react请求规范rule
│   └── toolkit.mdr #react业务组件、通用hook、工具函数rule
│   └── route.mdr #react路由规范rule
├── san/ #san技术栈相关rule
│   ├── runtime.mdr #san工具函数、装饰器rule
│   ├── service.mdr #san请求规范rule
│   ├── sui-biz.mdr #san业务组件rule
│   └── sui.mdr #san基础组件rule
│   └── sui-icon.mdr #san基础icon库相关rule
│   └── route.mdr #san路由规范rule
├── project/ #业务相关rule
│   ├── xxx.mdr #业务根据需求自行补充
├── react.mdr #react技术栈产品或者混合技术栈中react页面入口rule
├── san.mdr #san技术栈产品or混合技术栈中san页面入口rule
└── san2React.md #san技术栈页面重构为react技术栈页面rule

```
## Rule生成
**工具库**

对于工具库，通过多轮对话，让comate熟悉并生成使用文档，且需要保证生成文档的内容覆盖全面。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
**在所有工具库中按照相同的方式，为业务依赖的这些基础工具库生成使用说明**

**业务相关**

对于重复度高的工作，可以先引导Agent逐步完成一次任务，然后让Agent对上述任务步骤进行总结，这个总结就可以作为这个业务场景的rule

**一个真实的案例**：

**xx产品中，有几十个页面中的标签展示交互需要升级，我们实现了一个通用的标签展示组件，现在需要完成这几十个页面中的替换工作**

**rule生成：**

        1. 让agent生成这个通用组件的使用规范，作为初版rule
        2. 让agent参考已经完成的示例梳理替换规则，完善rule
        3. 让agent基于rule去完成一个新页面的组件升级
        4. 效果验证

**rule使用**

        1. 让agent梳理剩余所有需要升级的页面列表
        2. 根据页面列表基于rule完成逐步升级，每完成一个页面就要停下来进行等待人工验证，人工确认通过后再继续下一个页面的替换，最终完成所有页面的升级

**效率提升**

替换工作涉及30+页面，本来人工替换+验证需要花费1.5天，在ai的帮助下，只花费了0.5天就完成了，效率提升**60%**，且这个rule沉淀下来，其它产品有类似需求可以复用

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## **Rule使用**
**Rule维护**

以上基础工具库的rule在所有业务中都可以复用，所以将这些rule维护在一个公共的代码库中，便于大家使用、持续完善：[文件页：baidu/baiducloud/console-base-rule  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/baiducloud/console-base-rule/tree/master/comate/san?t=mention&mt=doc&dt=sdk)

**Rule获取**

产品可以通过命令：`git archive --remote=ssh://pianruijie@icode.baidu.com:8235/baidu/baiducloud/console-base-rule master comate | tar -x -C ./`将远程代码库中的rule拉取到自己的产品代码库，根据产品自身需求将rule移入项目自己的.comate目录，比如react技术栈产品只保留react相关rule即可

**Rule使用**

如果是san或者react技术栈产品，在保留合适的rule以后，可以将相关rule生效规则设置为 `总是生效`，混合技术栈产品需要根据需求手动选用合适的入口rule

![](/personal-site-mvp/img/doc-placeholder.svg "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
