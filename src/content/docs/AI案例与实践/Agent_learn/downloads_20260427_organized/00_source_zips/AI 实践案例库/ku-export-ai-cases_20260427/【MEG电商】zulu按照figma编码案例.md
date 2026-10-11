---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "【MEG电商】zulu按照figma编码案例"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\【MEG电商】zulu按照figma编码案例.md"
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
|项目介绍|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d9e3a78604534dab9757afa6aabe8015&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=95f12c0aa6b245a3a5e3e3862ff08ae2&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1a32a95dbefb451bb92313d28cd01725&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9cb55aeee5b346dcae7669962832f6b3&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=95ec0bdb7359440a84320e0745b67265&docGuid=YJByhAmjQZBnnz "")|使用规则前项目介绍简短，无业务功能使用规则后对项目大致业务和一些重要模块的体现|
|项目结构|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cd6f05590c374f02849b98a5a399888b&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ee35397deb894e4b9f7206fb89c7f5b2&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7f71cf35d7ec4a72a3b9f4d5d123455e&docGuid=YJByhAmjQZBnnz "")|使用规则前生成的组件结构杂乱，命名不规范放置的文件位置也是随机生成，并且没有识别到项目的框架，在最外层生成了项目的依赖。使用规则之后生成的组件统一文件命名规范。|
|代码案例（css）|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=549347db79584fa0ad10e9309616d4ee&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0bcae21db65c46409c6d4527a3d6b086&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1754b0ebcadd45b89c871b653283df0d&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b50d653235d64f2a8210a2c70c0b3346&docGuid=YJByhAmjQZBnnz "")|使用规则前这里的css生成的命名规范和写法不会统一，会使用普通scc写法造成代码冗余，也有一定概率去生成Tailwind CSS项目中没有此配置会造成项目错误。使用规则后会统一生成css代码。|
|代码案例（组件）|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=61363f9c070b4c9c881fdd906272d82b&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=81d6401396f14e6491210989d2880677&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b9e621bb2f0a4f7bb3fe49ca3a9f922d&docGuid=YJByhAmjQZBnnz "")|使用规则前这里不会去配合使用提供的组件库，全是手动封装。使用规则后会结合antd-design组件库完成组件。|

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
|class类名|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=37097fc61c6b4388a810c87374afec1a&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fcce6d18bdfb4074bd3ea5b3b23dbe05&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bfdfa54d6011476aa867c5a1e95efbde&docGuid=YJByhAmjQZBnnz "")|使用规则前  一个标签会携带多个类名 并且语意化较低 不易理解使用规则后每个标签都有对应的单个标签，语意化明确，方便理解与维护|
|script 结构 && ts 类型声明|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7f97f8e653b34dc4a4be3ffaed33d710&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=03fd428cbf1b48fb9e0148f00b8071f8&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d254aaf0256a4237a8ecc7a2eff2bcff&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=462579f9f0b74c3091155dc7a8475322&docGuid=YJByhAmjQZBnnz "")|使用规则前script 结构 与项目中其他文件会存在差异  不会生成ts类型声明使用规则后script 结构  与项目中其他文件保持一致  提高了对项目文件的解析会生成明确的ts类型声明|
|数据生成|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fd94b2e688bc4224ae6e0e8b7dce21c5&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8b075629e0a34f68be675be2e633e183&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=caf5a065c2ce45d89d2a35088127fdb3&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9b439ddb28c94754b0ca788cedf482a5&docGuid=YJByhAmjQZBnnz "")|使用规则前表格中的每一项都是单独编写，而非遍历数组并且数据写死不方便复用使用规则后数据响应式 方便替换真实数据请求接口，利于组件的复用|
|组件库的应用|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=225ec80f8e3a4592af46d315ec2bd27f&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f946eab6f4c4d62a76f227bdd0a988e&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7c8f96d9491340df9e3b42c42a5baa3f&docGuid=YJByhAmjQZBnnz "")|使用规则前对组件库的辨识度很低，代码生成几乎不会主动使用组件库内的组件  数据结构有时是数组有时是单个对象 不稳定使用规则后提高了对组件库的使用的可能性，用到el-card组件进行开发数据结构为数组形式，采用v-for遍历渲染页面|
|css样式|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=80f43151088e48cc9e256013561ef0f1&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0cba4f18bb3d40f0837a3d324a021f76&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1ee2682917dc4143ab707f390ec48539&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=984eb7b407254793b9086d0f4c11871c&docGuid=YJByhAmjQZBnnz "")|使用规则前css样式不生成生成的样式是@apply 写法 与 项目不匹配使用规则后css写法符合当前项目 在高度与宽度上需调整|

#### UI效果图
|原型|未使用rules效果图|生成时间|使用rules效果图|生成时间|
|-|-|-|-|-|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e07aef718d8048e7ab91ad417a21c68b&docGuid=YJByhAmjQZBnnz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=32252263b2164bbdae6c062cf6f47da8&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b3d47d0511434fa294f8b04676c7d2f3&docGuid=YJByhAmjQZBnnz "")|6分钟还原度30%|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f5339fa7dee144bda46ba8741dae18fa&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6b78ac112b4c4e3985206b55310a031b&docGuid=YJByhAmjQZBnnz "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=19c2710aa32044268179ea7a31fcbe92&docGuid=YJByhAmjQZBnnz "")|6分钟还原度20%|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=50952ac878d840e098002d313082d629&docGuid=Gcs97srFTCLfFS "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=692a3a09faec4bf88360db9f72495f22&docGuid=Gcs97srFTCLfFS "")|5分钟生成可用版本还原度 70%|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f707786fe9284ede9a33184ff134b60d&docGuid=Gcs97srFTCLfFS "")|3分钟生成可用版本还原度 80%|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a72fe15b284a47188589a0091655be69&docGuid=Gcs97srFTCLfFS "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ee2a0048e694805a8c22af314698254&docGuid=YJByhAmjQZBnnz "")|10分钟生成可用版本还原度70%|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fbc2f2c4048e49c482f1a86facb59fad&docGuid=Gcs97srFTCLfFS "")|2分钟生成可用版本还原度80%|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=616259ef23ca4e5da08c0edc0000cfb6&docGuid=Gcs97srFTCLfFS "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f37a4cd28a494b4e88d38f2849e55835&docGuid=Gcs97srFTCLfFS "")|4分钟生成可用版本还原度60%|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d29ec19c6ca048199d470adc686b866e&docGuid=Gcs97srFTCLfFS "")|2分钟还原度80%|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dedee207492040f0afe4098f2abc7f94&docGuid=Gcs97srFTCLfFS "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8a38106e73154f56be4237e1519a6802&docGuid=Gcs97srFTCLfFS "")|4分钟生成可用版本还原度70%|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=da273da63e7f4e13bd2f6f00cb9cba4e&docGuid=Gcs97srFTCLfFS "")|2分钟生成可用版本还原度80%|

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
