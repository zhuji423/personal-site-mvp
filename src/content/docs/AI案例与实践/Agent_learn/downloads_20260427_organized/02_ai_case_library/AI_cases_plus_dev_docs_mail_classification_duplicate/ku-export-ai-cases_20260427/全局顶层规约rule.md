---
title: "IntelliJ插件开发指南"
description: "全局顶层规约rule"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\全局顶层规约rule.md"
---
全局顶层规约rule

#### 🧑‍🏫 案例作者：[@慕海龙](https://ku.baidu-int.com?t=mention&mt=contact&id=e2c2cf10-fcea-11f0-a691-81f58da6da17)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文是IntelliJ插件开发的全局顶层规约，涵盖项目概述、架构、代码结构、技术栈版本及关键约定。项目旨在开发一款AI编码辅助工具，采用[Kernel+Agent]与WebView架构，支持代码补全、智能调试等功能。规定了Java编码规范、插件开发规约，强调EDT线程使用、网络请求封装等关键开发约定，确保开发一致性和质量。
### 全局性rule主要分为
1. 项目概述
    1. 主要描述项目（产品）业务功能

2. 项目架构
    1. 技术架构，最大的（外层）模块之间架构

3. 代码结构
    1. 交代各个核心模块（模块局部）的功能，代码路径
    2. 也可以将项目的目录树给出，关键节点处给必要的注释解释

4. 技术栈版本
    1. 框架版本
    2. 语言版本
    3. 编译系统版本
    4. 中间件版本
    5. 项目外部依赖

5. 关键约定
    1. 编码规范
        1. Java语言详见下方(这里只能是prompt级控制，实践中还是建议让AI去调用Lint工具)

    2. 项目开发约定
        1. 项目团队自己特定开发约定，比如http请求必须使用项目中已封装好的HttpManager，json处理必须使用gson



```
---
description: IntelliJ插件开发指南
globs:
alwaysApply: true
---
# IntelliJ插件开发指南

## 项目概述
这是一个IntelliJ插件项目，它是一款创新型AI编码辅助工具，提供Agent智能体创建与使用、侧边栏智能问答、代码补全、智能调试、代码解释、单元测试生成等功能。

## 项目架构
[Kernel+Agent] ⇆ [Plugin] ⇆ [WebView]
用户在JetBrains IDE中使用[Plugin]通过[Kernel+Agent]与大模型通信，[WebView]为插件的侧边栏用于问答输入以及模型输出展示
- **Kernel+Agent**: 两者均为JavaScript开发的二进制，它们的代码实现不在本项目，本项目只使用他们二进制负责与AI大模型服务器做代理通信。
    - Kernel: 位于ext/comate-agent/bin/comate-kernel（comate-kernel-internal表示厂内版本），负责Agent智能体业务通信，比如侧边栏的智能问答。
    - Agent:  位于ext/comate-agent/bin目录下的二进制，负责代码补全、代码改写业务通信，比如代码编辑区光标处自动补全以及补全后光标自动跳转至代码相关处再做补全。
- **Plugin**: 即当前插件项目，它是一个标准的IntelliJ插件项目，采用Gradle构建，插件ID为 `com.baidu.comate`，名称为"Baidu Comate"。
- **WebView**: 位于src/main/resources/webview，其代码实现也不在本项目内，由JavaScript开发的前端页面，用做插件的侧边栏展示。

## 代码结构说明
插件所有代码均在`com.baidu.comate.intellij`包名下，以下是插件核心模块
### 1. 代码补全 模块
- **职责：** 代码补全分为续写和改写，模型会根据光标所在位置进行判断，在当前位置进行补全还是将光标跳到别的位置做代码修改，前者为代码续写，后者则为代码改写；此模块主要负责提取光标处现场代码数据以及上下文，通过Agent调用AI模型服务完成代码补全功能
- **位置：** src/main/java/com/baidu/comate/intellij/completions

### 2. Kernel 模块
- **职责：** 底层基于jsonrpc技术实现的lsp协议，用于Kernel二进制与IDE通信
- **位置：** src/main/java/com/baidu/comate/intellij/agent

### 3. WebView侧边栏 模块
- **职责：** 插件侧边栏界面，底层基于JCEF与插件进行通信
- **位置：** src/main/java/com/baidu/comate/intellij/toolwindow

### 4. 插件功能设置面板 模块
- **职责：** 插件的功能设置面板页面实现，以及插件设置数据的本地化读写保存以及远端服务器读写同步
- **位置：** src/main/java/com/baidu/comate/intellij/settings

### 5. Action 模块
- **职责：** 插件交互入口，比如点击菜单、工具栏按钮、快捷键、右键菜单项时Comate相关按钮的响应
- **位置：** src/main/java/com/baidu/comate/intellij/actions

### 6. 网络请求 模块
- **职责：** 插件与服务器的直接网络请求，主要是HTTP网络请求支持SSE
- **位置：** src/main/java/com/baidu/comate/intellij/request

## 技术栈版本
1. 项目基于Java 11开发
2. SDK使用IntelliJ Platform SDK 2021.1.1版本
3. 插件依赖多个IntelliJ官方插件："Git4Idea", "com.intellij.java", "svn4idea",
                              "org.jetbrains.plugins.go:211.7142.36",
                              "org.jetbrains.plugins.terminal:211.7142.37",
                              "org.intellij.plugins.markdown:211.7142.37",
                              "PythonCore:211.7142.45",
                              "org.jetbrains.kotlin:211-1.5.21-release-317-IJ7442.40",
                              "maven",
                              "yaml",
                              "gradle"
## 关键约定
### 1. 编码规范
- **代码格式：** 严格遵守K&R编程风格，每行不超过120字符
- **注释规范：** 类、方法必须有Javadoc注释
- **异常处理：** 不要吞异常；使用具体异常类型，不用Exception兜底；仅在需要恢复时捕获异常，否则向上抛出
- **日志规范：** 禁止使用System.out.println()，使用LOG.info("[Comate] xxx")，插件日志以[Comate]开头
- **注解规范：** 严格启用 @Override、@Nullable、@NonNull 等注解

### 2. 插件开发规约
- **IntelliJ Platform SDK：** 所有的插件库均基于2021.1.1；如果不得不使用2021.1.1以上版本代码，允许使用反射方式调用但要写有详细注释
- **EDT线程使用：** 严禁在EDT中做耗时操作，EDT仅用于处理UI事件，其余情况下禁止使用EDT；EDT调用已封装在`ThreadPoolHolder`类，酌情调用
- **网络请求：** 不要单独实现，http请求已在`HttpManager`类中做封装，酌情调用

```
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
