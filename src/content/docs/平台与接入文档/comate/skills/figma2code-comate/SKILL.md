---
title: "输入设计稿信息"
description: "根据Figma设计稿信息生成代码。当用户选择设计稿并希望根据设计稿生成代码时，请使用此skill。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\figma2code-comate\\SKILL.md"
name: "figma2code"
---
# 输入设计稿信息
【设计稿html】： 选中的设计稿信息中的htmlGeneratedByFigmaNode字段。
【设计稿图片】： 上下文中的图片
【设计稿名称】：选中的设计稿信息中的name字段。
【图片目录】：选中的设计稿信息中的assetsPath字段
【设计稿图片可访问url】：选中的设计稿图片的可访问链接，非特殊要求请勿使用。
【designTokenPath】：选中的设计稿信息中的designToken.md的路径,非特殊要求请勿使用。
【image2designMode】：用户配置项，表明是否使用image2design模式。
【designTokenMode】：用户配置项，表明是否要使用设计Token。

# 任务概述
你需要严格遵循下面的步骤根据【设计稿html】和【设计稿图片】来生成一个新组件或页面。你应该使用项目相同的技术栈或按照用户的要求来实现并遵循最佳实践。


# 步骤
请务必严格遵循该步骤。
1. 项目分析
   - 项目使用的技术栈（仅在未检测到使用其他css框架或用户要求的情况下才使用原生CSS。）
   - **组件注册方式**（如何导入/导出组件，组件如何被使用）
   - **页面路由配置**（路由系统如何工作，新组件如何集成到路由中）
   - 项目的构建和编译系统（webpack/vite/其他）

2. 设计稿分析
  - 请基于【设计稿图片】分析页面结构和语义。如果用户开启了【image2designMode】则基于references/image2md.md 的流程进行分析。
  - 组件识别与引入，请基于references/codeConnect.md 遵循Code Connect指南分析设计稿组件。


2. 图片资源管理
   - 请使用终端命令一次性将需要的图像复制到项目中的合适目录中 (请避免一个一个复制图片，使用一个命令复制整个图片目录)，并记住复制后的【图片目录】。注意无需执行终端命令检查目录中是否有图片。
   - 请确保在项目中使用正确的方法引用【图片目录】中的图片资源。【图片目录】中的图片名称和html代码中的图片名称是一致的。
**请注意tailwind框架中不要使用bg-[url]来引入本地图片资源，比如bg-[url('/images.png')]，而是使用style中的background-image属性。**

3. 代码生成
   - 根据读取的userRule和上述分析，生成对应代码。

# 其他
生成的代码写入项目中。
避免杜撰并引入任何不存在的资源（包括字体、图片等）。
请勿安装任何依赖项。

# 其他资源
- userRule请从rulePath中读取。无特殊要求默认读取。
- codeConnect流程请遵循[codeConnect.md](references/codeConnect.md)。无特殊要求默认读取。
- designToken流程请遵循[designToken.md](references/designToken.md)，当且仅用户使用designTokenMode时读取。
- image2design流程请遵循[image2design.md](references/image2design.md)，当且仅用户使用image2designMode时读取。