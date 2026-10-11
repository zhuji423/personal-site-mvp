---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "【ACG系统部】光传输控制器结合Zulu编码案例"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\【ACG系统部】光传输控制器结合Zulu编码案例.md"
---
【ACG系统部】光传输控制器结合Zulu编码案例

#### 🧑‍🏫 案例作者：[@靳晓莹](https://ku.baidu-int.com?t=mention&mt=contact&id=68ab7f40-fce7-11f0-8f6f-bd0ea6c8c7c6)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了ACG系统部光传输控制器项目中结合Zulu编码的实践，通过引入Rules提升AI Coding的代码质量与风格一致性。项目通过对比添加Rules前后的代码生成效果，验证了Rules在代码生成与项目介绍中的有效性。Rules确保了AI在复杂项目中的一致性，显著提升了研发效能，为大型项目的AI Coding应用提供了宝贵经验。
## 背景
【SDN自研光传输系统控制器】于今年立项，**旨在对百度光传输设备/资源建立完全自主可控的管理体系**，支持多种传输设备命令下发及相关资源的管理，适配 **5+ 厂商与 15+ 类型板卡，代码量庞大**。在有限人力条件下，项目积极探索引入 AI Coding 工具，**提升****研发效能并确保代码质量与风格一致性**。由于大型语言模型在多次补全间无法保留上下文，而Rules 可提供持久、可复用的指导，**保证 AI 在代码生成、解释与工作流辅助中的一致性**。本项目在实际编码场景中引入 Rules，**针对相同问题对比添加前后的回复差异**，评估其在代码生成与项目介绍中的应用效果。

[cursor增加项目规则](https://docs.cursor.com/zh/context/rules)

[comate增加项目规则](https://cloud.baidu.com/doc/COMATE/s/Zm9l4agw3)

## Rules定义
```
---
description: 
globs: 
alwaysApply: true
---
## 项目概述

本项目旨在提供一个全面的网络设备管理平台，支持多种设备和资源的管理，覆盖传输设备、拓扑、业务及物理资源管理，支持事件上报、告警与倒换处理等。

## 项目架构
项目采用模块化设计，主要分为以下几个核心部分：

1. **业务接口** (`controller/`)
   - 实现了多个业务控制类，负责处理设备相关的请求和逻辑
   - 提供了数据的输入输出接口

2. **数据访问层** (`dao/`)
   - 包含 `impl` 和 `interface` 子包，处理与数据库的交互，提供数据的增删改查功能
   - 包含接口和实现类，如 DeviceDao 和 DeviceDaoImpl。

3. **服务层** (`service/`)
   - 包含 `impl` 和 `interface` 子包，实现了业务逻辑，协调业务控制类和数据访问层之间的交互
   - 包含服务接口和实现类，如 DeviceService、TopologyService 等。

4. **实体类** (`entity/`)
   - 定义了与数据库表对应的实体类
   - 包含了数据的属性和相关的注解

5. **异常处理** (`exception/`)
   - 定义了自定义异常类，处理业务逻辑中的异常情况

## 开发指南

### 1. 基本开发流程

1. 如需增加新的业务控制类，放置在 `src/main/java/com/baidu/bin/fiber/controller` 目录下。
2. 所有服务类应放置在 `src/main/java/com/baidu/bin/fiber/service` 目录下，并实现相应的接口。
3. 数据访问层的实现类应放置在 `src/main/java/com/baidu/bin/fiber/dao/xdb/impl` 目录下，接口应放置在 `src/main/java/com/baidu/bin/fiber/dao/xdb` 目录下。

### 2. 扩展开发指南

1. **添加新的业务控制类**
   - 在 `controller/` 目录下创建新文件
   - 实现相应的业务逻辑
   - 确保与现有接口保持一致

2. **添加新的服务**
   - 在 `service/` 目录下创建新文件
   - 实现服务接口
   - 在 `service` 包中注册新服务

3. **添加新的数据访问接口和实现**
   - 在 `dao/` 目录下创建新接口
   - 在 `dao/impl` 目录下实现接口

## 代码风格指南

1. **命名规范**
   - 类名使用大驼峰命名法（PascalCase）
   - 类名的命名格式必须与package下其他类的风格相同，例如DeviceDao、DeviceDaoImpl
   - 方法名和变量名使用小驼峰命名法（camelCase）
   - 常量使用全大写字母，单词之间用下划线分隔

2. **代码格式**
   - 每行代码不超过 120 个字符
   - 使用四个空格进行缩进，不使用制表符（Tab）
   - 每个方法之间应留有一个空行，每个类之间应留有两个空行

3. **注释规范**
   - 所有公共方法应有 Javadoc 注释，描述方法的功能、参数和返回值
   - 复杂的逻辑应添加行内注释，解释代码的意图
   
4. **异常处理**
   - 使用通用异常类以及自定义异常类处理业务逻辑中的异常，确保异常信息清晰且具有上下文
   - 记录异常时，使用完整的异常对象 e 作为最后一个参数传递给日志方法，以便于调试

5. **日志格式**
   - 记录日志时必须使用英文
   - 日志级别只使用info或error
   - 涉及到变量的，使用统一的日志规范，例如log.info("device :" + deviceIp + "is Empty")的方式来记录日志

## 注意事项
1. 定期进行代码审查，确保代码质量和一致性
2. 使用日志记录异常信息，确保记录完整的异常对象以便于调试
```
## 编码样例
##### 样例一：项目结构介绍
**rules中与项目结构相关的介绍**

![](/personal-site-mvp/img/doc-placeholder.svg "")






**添加rules之前，zulu回复的项目结构介绍**



![](/personal-site-mvp/img/doc-placeholder.svg "")
#### ☹️
#####  **介绍较为简短、无项目结构、业务功能等信息**
**添加rules后，再次让zulu回复的项目结构介绍**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### **😄**
##### ** 对项目结构、业务功能理解更详细，更准确**
##### 样例二：crud基础代码生成
**rules中与代码结构、框架相关的介绍**

![](/personal-site-mvp/img/doc-placeholder.svg "")
**添加rules之前，zulu根据项目结构生成的数据库持久化代码**

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### ☹️
zulu无法识别项目使用的是dao接口+impl+jdbcTemplate实现数据持久化，**采用了jpa的repository接口来进行代码编写**

##### **代码可用性：0%**
**添加rules后，让zulu根据项目结构生成的数据库持久化代码**

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### **😄**
zulu成功按照项目结构生成service、serviceImpl、dao、daoImpl四个类及对应的函数，**并使用了与代码库相符合的数据持久化方式**

##### **代码可用性：80%**
##### 样例三：函数日志生成
**rules中与日志规范相关的介绍**

![](/personal-site-mvp/img/doc-placeholder.svg "")
**添加rules之前，zulu为函数生成注释**

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### ☹️
**zulu未按照类中已定义的日志格式来进行日志打印**

1. 未按照项目已有日志打印规范，拼接变量来打印日志
2. 根据自己的思考来打印日志级别

**添加rules后，让zulu再次生成注释**

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### **😄**
zulu根据已定义的日志规范，**在打印变量以及日志级别上都做了调整，可直接使用生成的代码**

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
