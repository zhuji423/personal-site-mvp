---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "【MEG电商】zulu按照figma编码案例"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\【MEG电商】zulu按照figma编码案例.md"
---
【MEG电商】zulu按照figma编码案例

#### 🧑‍🏫 案例作者：[@崔旭](https://ku.baidu-int.com?t=mention&mt=contact&id=0a3f3000-fcec-11f0-9a1b-a747b3616683)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了MEG电商团队如何使用Zulu工具根据Figma设计图生成React+Ant Design代码的实践案例。通过明确技术栈要求、任务要求及开发指南，确保生成的代码保持原有页面结构和视觉效果，同时遵循最佳实践和代码规范。案例展示了使用Rules前后在组件复用、数据结构稳定性和CSS样式匹配度上的显著提升，提高了开发效率和代码质量。


使用手册：[https://cloud.baidu.com/doc/COMATE/s/jm5atx00b](https://cloud.baidu.com/doc/COMATE/s/jm5atx00b)（f2c）



##### Rules默认
```
## 技术栈要求
请根据代码库分析项目使用的技术栈。

## 任务要求
1. 保持原有的页面结构和视觉效果
2. 遵循目标框架的最佳实践和代码规范，包括以下几点：

一：注意优化DOM结构与逻辑关系：
   - 优化DOM结构，避免不必要的div嵌套和冗余！
   - 优先使用HTML5语义化标签（nav, header, main, footer, article, section等）
   - 列表内容必须使用map等循环方法渲染
   - 确保所有可交互元素的可访问性

二：布局与样式规范：
   - 优先使用Flex或Grid布局，避免滥用绝对定位
   - 只在必要时使用绝对定位（如模态框、tooltip等）
   - 实现移动优先的响应式设计

三：代码可读性与可维护性：
   - 组件名称和文件名应当语义化并使用PascalCase
   - 将页面拆分为合理的组件结构
   - 抽取重复逻辑
   - 为复杂逻辑添加简洁清晰的注释
   - 静态资源引用应当语义化命名

## 其他
```
##### Rules自定义
```
## 技术栈要求

本项目使用的react+antd design组件库，生成代码前优先读取package.json文件，不要安装其余插件本项目没有使用到typescript。

## 任务要求

1. 保持原有的页面结构和视觉效果
2. 遵循目标框架的最佳实践和代码规范，包括以下几点：

3. 命名规范：

    - 文件命名：PascalCase (例: UserProfile.jsx)
    - 组件命名：与文件名一致 (例: function UserProfile()或 const UserProfile = （） => {})
    - CSS类名：kebab-case (例: .user-profile)

4. 文件目录：

    - 将所有生成的文件统一放在src文件下的example文件下（如果没有这个文件就创建）
    - 每个组件都放在一个单独的文件夹 分别是index.jsx,[name].module.scss（本项目使用了sass,不要是用tailwind css）,component(这个是个文件夹，如果有子组件则创建，如果没有就不创建了)

5. 内容：
    - 超过200行的代码考虑拆分子组件
    - 如有条件渲染使用 && 或三元表达式，避免复杂逻辑
    - 循环渲染必须要提供唯一的key
    - 尽量配合使用antd Design组件库，若没用到组件库其余标签则用div标签，不要使用语义化标签
    - 预留图片坑位，可以mock图片
    - 采用响应式布局，适配小、中、大屏幕，
```


#### 编码案例
||相关规则|使用规则前|使用规则后|结论|
|-|-|-|-|-|
|项目介绍|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前项目介绍简短，无业务功能使用规则后对项目大致业务和一些重要模块的体现|
|项目结构|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前生成的组件结构杂乱，命名不规范放置的文件位置也是随机生成，并且没有识别到项目的框架，在最外层生成了项目的依赖。使用规则之后生成的组件统一文件命名规范。|
|代码案例（css）|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前这里的css生成的命名规范和写法不会统一，会使用普通scc写法造成代码冗余，也有一定概率去生成Tailwind CSS项目中没有此配置会造成项目错误。使用规则后会统一生成css代码。|
|代码案例（组件）|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前这里不会去配合使用提供的组件库，全是手动封装。使用规则后会结合antd-design组件库完成组件。|

```
## 项目概述

这是一个 vue3+ts+elementPluse 的后台管理系统

## 开发指南

1. **数据格式**

- 多数采用对象，支持嵌套结构
- 多数采用数组，支持循环遍历
- 解析数据 生成对应数据结构
- 不要把死数据写死在代码中，而是通过调用定义好的响应式数据

2. **css 写法**

- 使用传统 css 写法

3. **UI 组件**

- 优先考虑是否可用 elementPlus 组件进行开发

4. **类名处理**

- 去除多余的 class 类名

## 代码风格指南

1. **类型定义**

   - 优先使用接口（interface）定义类型
   - 为所有公开 API 提供完整的类型定义
   - 使用泛型增加代码复用性

2. **错误处理**

   - 统一使用 Error 对象处理错误
   - 在异步操作中正确处理错误传播

3. **命名规范**
   - 使用驼峰命名法
   - 类名使用大驼峰
   - 接口名清晰表达其用途
4. **代码组织**
   - 只生成需要的组件，不需要生成其他多余文件
   - setup 写在<script> 标签内

```


UI图链接：

[https://www.figma.com/design/IFBY5DIK3CQTnA6zxmjKqL/%E5%BA%97%E9%93%BA%EF%BC%88%E8%A7%A6%E8%BE%BE%E3%80%81%E5%95%86%E5%AE%B6%E5%85%A5%E9%A9%BB-%E5%85%B3%E5%BA%97%E3%80%81%E7%94%B5%E5%95%86%E5%AD%A6%E8%8B%91%EF%BC%89?node-id=11359-20305&p=f&t=m03dQRtkWWFRcyQa-0](https://www.figma.com/design/IFBY5DIK3CQTnA6zxmjKqL/%E5%BA%97%E9%93%BA%EF%BC%88%E8%A7%A6%E8%BE%BE%E3%80%81%E5%95%86%E5%AE%B6%E5%85%A5%E9%A9%BB-%E5%85%B3%E5%BA%97%E3%80%81%E7%94%B5%E5%95%86%E5%AD%A6%E8%8B%91%EF%BC%89?node-id=11359-20305&p=f&t=m03dQRtkWWFRcyQa-0)



编码案例

||相关规则|规则使用前|规则使用后|结论|
|-|-|-|-|-|
|class类名|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前  一个标签会携带多个类名 并且语意化较低 不易理解使用规则后每个标签都有对应的单个标签，语意化明确，方便理解与维护|
|script 结构 && ts 类型声明|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前script 结构 与项目中其他文件会存在差异  不会生成ts类型声明使用规则后script 结构  与项目中其他文件保持一致  提高了对项目文件的解析会生成明确的ts类型声明|
|数据生成|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前表格中的每一项都是单独编写，而非遍历数组并且数据写死不方便复用使用规则后数据响应式 方便替换真实数据请求接口，利于组件的复用|
|组件库的应用|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前对组件库的辨识度很低，代码生成几乎不会主动使用组件库内的组件  数据结构有时是数组有时是单个对象 不稳定使用规则后提高了对组件库的使用的可能性，用到el-card组件进行开发数据结构为数组形式，采用v-for遍历渲染页面|
|css样式|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|使用规则前css样式不生成生成的样式是@apply 写法 与 项目不匹配使用规则后css写法符合当前项目 在高度与宽度上需调整|

#### UI效果图
|原型|未使用rules效果图|生成时间|使用rules效果图|生成时间|
|-|-|-|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|6分钟还原度30%|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|6分钟还原度20%|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|5分钟生成可用版本还原度 70%|![](/personal-site-mvp/img/doc-placeholder.svg "")|3分钟生成可用版本还原度 80%|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|10分钟生成可用版本还原度70%|![](/personal-site-mvp/img/doc-placeholder.svg "")|2分钟生成可用版本还原度80%|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|4分钟生成可用版本还原度60%|![](/personal-site-mvp/img/doc-placeholder.svg "")|2分钟还原度80%|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|4分钟生成可用版本还原度70%|![](/personal-site-mvp/img/doc-placeholder.svg "")|2分钟生成可用版本还原度80%|

### 总结
1、当前的f2c中的默认rules已经具备解析不同项目的技术栈能力，但存在会另外起一个src文件夹的可能，会导致已起服务挂掉

2、增强通用rules，对UI组件库的解析以及ts的解析放到通用rules, 方便后期代码生成，更贴合已存在的文件，减少新页面编辑与原页面的差异性

3、生成样例展示文件后，会改动项目中的router文件，这是多余的操作，建议只生成样例展示文件，或直接在对话中给出如何使用即可，减少对项目中原文件的修改

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
