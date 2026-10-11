---
title: "基于zulu-cli的前端组件埋点规范自动化检测与修正"
description: "基于zulu-cli的前端组件埋点规范自动化检测与修正"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\基于zulu-cli的前端组件埋点规范自动化检测与修正.md"
---
基于zulu-cli的前端组件埋点规范自动化检测与修正

#### 🧑‍🏫 案例作者：[@韩露](https://ku.baidu-int.com?t=mention&mt=contact&id=4ee3c400-fce7-11f0-8143-975bd569a53c)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了基于zulu-cli的前端组件埋点规范自动化检测与修正方案，通过定制rules与zulu-cli套件，解决了埋点开发过程中代码规范不一致、质量保证效率低、重复性工作多及知识传递困难等问题。该方案实现了埋点检查的智能化、标准化与自动化，提高了开发效率与代码质量，同时支持多种规则类型和执行场景，具有良好的可扩展性与可维护性。
# 基于zulu-cli的前端组件埋点规范自动化检测与修正
## 1. 背景
商家智能体前端代码库是一个基于Vue的代码库，采用微前端架构，目标是让每个组件都能独立开发、构建、发布、运行。在面向商业场景的日常开发中，埋点是不可或缺的一环。业务埋点在后续用户行为、转化行为等分析中非常重要，但在埋点开发过程中面临以下痛点：

* **代码规范一致性**：团队成员编码风格不统一，埋点实现不规范
* **质量保证效率低**：人工代码审查耗时耗力，容易遗漏问题
* **重复性工作多**：大量重复的埋点检查和修复工作
* **知识传递困难**：规范文档复杂，新人上手周期长

希望借助厂内大模型能力以及业务定制的rules，实现在研发流程中自动化解决上述问题，提升研发效率；

## 2. 关键词
zulu cli、埋点规范、自动化、规则驱动

## 3. 提效思路与经验
日常研发同学通过与zulu对话调用rules的方式实现预期功能，但是在这个过程中的**大模型输出的不稳定性**以及其**与****DevOps的割裂，无法自动化的问题**，严重制约了大模型在日常开发过程中的使用；通过业务分析并书写定制rules，引入zulu-cli套件，解决上述问题；

### 3.1 稳定性
业务埋点错综繁杂，而大模型输出的不稳定行一直是阻碍业务应用的一个卡点，我们基于业务实际情况，在编写rules的过程中基于下述思路解决输出稳定性问题；

#### 3.1.1 限定范围
基于项目实际需求，设计并规范了智能体组件埋点检查范围，提升大模型的稳定性。

##### 3.1.1.1 埋点范围
**第一类组件埋点规范**：

* 使用compTargetId的基础埋点格式
* 埋点ID需要在`src/common/config/mbot/compTargetIds.js`中定义
* 支持多种行为后缀：hover、scroll、click、show、created、mounted、success、request、fail

**第二类组件埋点规范**：

* 使用mbot-card命名的文件格式
* 必须使用cardLogMap.show或cardLogMap.click
* userExtra.type字段必须使用cardTypeMap中定义的值

##### 3.1.1.2 文件范围
避免埋点检测走全量文件检测，上下文token太多引发大模型输出幻觉，在rules中告知大模型，只需要基于当前新增或修改的文件进行检测，加快检测速度的同时进一步提升大模型输出的稳定性；

```
前置条件:
1、必须执行 git diff --cached --name-only --diff-filter=ACM 命令，找出当前所有提交的文件；如果当前目录不在m-groot目录下 需要切换到m-groot目录下，再去执行上述命令
2、如果从条件1下获取到的文件列表中如果不包含文件名以gt-merchant开口的文件，则立即结束后续整个流程，且严禁多次重复确认。
3、读取 src/common/config/mbot/index.js 文件中 CARD_TYPE对象中的 widgetName, 获取到的组件列表。
```
#### 3.1.2 步骤拆解，清晰简单
执行过程进行步骤拆解，每一步都执行简单清晰的命令，虽然有点“啰嗦”，但是能进一步提升模型输出的稳定性

```
- 有埋点行为，每个文件必须严格执行下面的步骤
    第一步：**有埋点行为**, **严格**检查文件命名是否在**前置条件3中获取到的组件列表中**
        在，执行第二步；
        不在，执行第三步。
    第二步：检查是否使用的**cardLogMap.show** 或者 **cardLogMap.click**作为展现和点击埋点。
        使用：必须**严格**校验**userExtra.type**和**compTargetId**是否符合 **1.2中的第二类埋点函数规范** 要求，不符合进行修改,
        不使用：必须**严格**按照**1.2中的第二类埋点函数规范** 要求新增埋点
    第三步：**有埋点行为**,检查埋点是否在 **compTargetIds.js**文件中定义
        如果定义：必须**严格**校验埋点是否符合 **1.2中的第一类埋点函数规范**的要求，不符合进行修改。
        未定义：必须**严格**按照**1.2中的第一类埋点函数规范** 要求新增埋点

- 无埋点行为，每个文件必须严格按照下面的步骤执行新增埋点
    第一步：文件命名在前置条件3中获取到的组件列表中
        在，执行第二步；
        不在，执行第三步。
    第二步：必须**严格**按照**1.2中的第二类埋点函数规范** 要求新增展现和点击埋点，新增埋点需要定义customSendLog方法
    第三步：必须**严格**按照**1.2中的第一类埋点函数规范** 要求新增展现和点击埋点，新增埋点需要定义customSendLog方法
```
```
graph TD
    A[开始检查] --> B[获取提交文件列表]
    B --> C{包含gt-merchant开头文件?}
    C -->|否| D[结束检查]
    C -->|是| E[获取组件列表]
    E --> F[扫描每个文件]
    F --> G{有埋点行为?}
    G -->|是| H[检查埋点规范]
    G -->|否| I[新增埋点]
    H --> J{符合规范?}
    J -->|是| K[通过检查]
    J -->|否| L[自动修复]
    I --> M[添加标准埋点]
    L --> N[推送修改消息]
    M --> N
    K --> O[下一个文件]
    N --> O
    O --> P{还有文件?}
    P -->|是| F
    P -->|否| Q[结束]
```
#### 3.1.3 强调检查清单以及附加特殊说明
在执行完检测和修改之后，通过书写检查清单，实现大模型自校验执行是否符合预期，同时在最后针对一些特殊情况强调说明，让大模型进一步关注；

这些清单检测和说明强调，都是针对在调试rules过程中，大模型输出可能存在的问题，通过这一部分的内容建设，在这个场景下基本解决的大模型输出的不稳定性；

```
#### 校验检查清单
1、通用项检查
    - 是否引入 MBOT_COMMON_SERVICE, MBOT_S_KEYS
    - 埋点的参数格式是否正确
2、第一类组件检查项
    - 是否引入 compTargetIds 和 LOG_KEY_EXPAND_TYPE_MAP
    - 埋点ID是否在 compTargetIds.js 中定义
    - 是否使用正确的行为后缀名
    - 是否使用展开语法 ...compTargetIds[]
3、第二类组件检查项
    - 是否引入 cardLogMap 和 cardTypeMap
    - 是否使用 cardLogMap.show 或 cardLogMap.click
    - userExtra.type 是否在 cardTypeMap 中定义
    - 组件类型名称是否符合命名规范

### 特殊说明
    - 原有组件：对于已存在的组件文件，
        - 如果没有埋点代码，不强制要求添加跳过校验
        - 如果有埋点，使用第一类埋点 只需要校验 埋点id 需要在 src/common/config/mbot/compTargetIds中定义
        - 如果是第二类，需要校验参考第二类组件检查项
    - 新增组件：对于新创建的组件文件
        - 如果本身无埋点，会规范添加展现和点击埋点
        - 如果有发送埋点，按照规范校验埋点，如有问题会进行修复
    - 无需强制校验 customSendLog 方法

    - **埋点配置特殊处理规则**：
        - 埋点校验流程优先于项目通用组件设计原则
        - 为保持埋点规范统一性，允许修改 `src/common/config/mbot/` 下的埋点配置文件
        - 包括但不限于：compTargetIds.js、log.js等公共埋点配置文件的修改和新增
        - 此规则允许暂时代替项目规范中的"组件独立开发，不相互引用"原则
```
## 3.2 自动化
日常通过与zulu对话的方式调用rules实现预期功能，但基于提交代码的埋点检测，必须与研发流程紧密结合成自动化能力，才能达到预期效果，通过调研以及跟EE团队同学沟通，建设基于zulu-cli套件的自动化能力，形成代码提交、自动检测、修改通知的闭环；

[流程图]
1. 在代码提交的过程中基于git hooks生命周期自动触发埋点检测，解决手动对话触发的问题
2. 通过测试发现大模型执行耗时长，为了不影响正常的代码提交，编写异步执行的bash脚本，保证研发效率
3. 将zulu-cli执行过程日志写入日志文件，方便开发者查看执行过程，定位、优化问题
4. 由于是异步执行，自动检测并修改文件之后，为了让开发者第一时间感知，建设如流消息通知机制

![有修改消息自动通知开发者](/personal-site-mvp/img/doc-placeholder.svg "有修改消息自动通知开发者")
5. 与此同时为了通用化，设计了一套完整的基于zulu-cli的提效工具开发流程，文件结构如下：

```
zuluCli/
├── config.json          # 配置文件
├── index.sh             # 主执行脚本
├── utils/               # 工具函数
│   ├── index.sh         # 通用工具函数
│   └── sendMessage.sh   # 消息发送工具
└── logs/                # 日志目录
```
内置依赖安装和检测、日志处理、rules调用、消息通知等能力。后续在项目中如果需要新增其他自动化rules应用场景，可以直接基于此规范进行配置升级和按需调用。

```
{
  "rules": {
    "mbot-log-check": {
      "rulesPath": ".comate/rules/mbot-log-check.mdr",
      "queryString": "帮我检测新增组件是否书写了埋点...",
      "licenseKey": "xxx",
      "model": "DeepSeek-V3.1",
      "logFile": "./logs/mbot-log-check.log",
      "enabled": true,
      "description": "埋点检查 - 检测组件展现和点击埋点是否符合规范"
    }
  },
  "global": {
    "defaultLicenseKey": "xxx",
    "defaultModel": "DeepSeek-V3.1",
    "logDir": "./logs"
  }
}
```
## 4. 复盘
通过zulu-cli套件，配合业务rules，本项目成功实现了应用大模型进行埋点自动化校验和修复的目标。该方案具有以下特点：

1. **智能化**：利用大模型能力实现代码埋点的自动检查和修复
2. **标准化**：建立统一的代码埋点规范和检查标准
3. **自动化**：减少人工干预，提高开发效率
4. **可扩展**：支持多种规则类型和执行场景
5. **可维护**：完整的日志和配置管理机制

### 模式：（好的经验）
1. 在结果不符合预期时，可以试着问大模型如果想要预期的结果，应该怎么修改rules，反向操作
2. 复杂功能可以使用Spec Mode进行逐步确认，确保最终的需求理解、功能设计、代码实现都尽量符合预期

### 反模式（不要这么做）
不要妄想简单一句话就实现一个功能，需要描述清楚需求，写规则的时候，需要逐步拆解，步骤清晰且尽量简单，如果可以把场景现状也描述清楚，从而增加成功率



附埋点检测rules：

```
---
description: 处理智能体新增组件展现和点击埋点的校验和修改
globs: 
alwaysApply: false
---
## 工具概述

这是一个用于处理智能体新增组件展现和点击埋点的校验。如果不符合规定，自动修改，并推送修改消息，禁止随意发挥。

## 校验规则说明

### 1. 埋点规范
#### 1.1 埋点函数规范
```javascript
    customSendLog(params) {
        this.$loki.getServiceAsync(MBOT_COMMON_SERVICE).then(service => {
            service[MBOT_S_KEYS.SEND_LOG]?.sendLog(params);
        });
    }
```
#### 1.2 调用埋点函数规范

**第一类组件使用compTargetId文件格式**
1、 埋点id 需要在 src/common/config/mbot/compTargetIds.js 文件中的LOG_INFOS中定义；
2、 行为后缀名主要分为以下几类，后续新增可以继续扩充
```javascript
    export const LOG_KEY_EXPAND_TYPE_MAP = {
        // 用户行为
        hover: 'Hover',
        scroll: 'Scroll',
        click: 'Click',
        // 组件生命周期
        show: 'Show',
        created: 'Created',
        mounted: 'Mounted',
        // 接口请求
        success: 'Success',
        request: 'Request',
        fail: 'Fail'
    };
```
3、 发送埋点的格式参考下面的模板；默认需要引入模板中的两个文件。
```javascript
<script>
    import {MBOT_COMMON_SERVICE, MBOT_S_KEYS} from '@/common/config/mbot/service';
    import compTargetIds, {LOG_KEY_EXPAND_TYPE_MAP} from '@/common/config/mbot/compTargetIds';
    export default {
        mounted() {
            this.customSendLog({
                ...compTargetIds.[埋点id][行为后缀名],
                userExtra: {}
            });
        },
        methods: {
            handleClick() {
                this.customSendLog({
                    ...compTargetIds.[埋点id][行为后缀名],
                    userExtra: {}
                });
            }
        }
    };
</script>
```

4、以下为具体的示例，以我的 埋点id 为download，行为后缀名为show
```javascript
    this.customSendLog({
        ...compTargetIds[`download${LOG_KEY_EXPAND_TYPE_MAP.show}`],
        userExtra: {}
    });
```

**第二类组件使用mbot-card文件格式**
1、埋点的 compTargetId 必须使用cardLogMap.show或者cardLogMap.click;
2、埋点的 userExtra.type 字段必须存在，数据使用cardTypeMap中定义的值，如果不存在必须需要根据组件名在cardTypeMap中新增，不需要新增logError方法；
3、埋点的书写格式需要参考下方：
```javascript
<script>
    import {MBOT_COMMON_SERVICE, MBOT_S_KEYS} from '@/common/config/mbot/service';
    import {cardLogMap, cardTypeMap} from '@/common/config/mbot/log';
    export default {
        mounted() {
            this.customSendLog({
                compTargetId: cardLogMap.show,
                userExtra: {
                    type: cardTypeMap.[组件映射名] // 必须根据组件名使用cardTypeMap预定义值,如果不存在根据组件名在cardTypeMap中新增
                    ... // 额外行为打点，无需关注
                }
            });
        },
        methods: {
            handleClick() {
                this.customSendLog({
                    compTargetId: cardLogMap.click,
                    userExtra: {
                        type: cardTypeMap.[组件映射名] // 必须根据组件名使用cardTypeMap预定义值,如果不存在根据组件名在cardTypeMap中新增
                        ... // 额外行为打点，无需关注
                    }
                });
            }
        }
    };
</script>
```
4、以下为具体示例，假设我的文件名称为 gt-merchant-test-card
```javascript
<script>
    import {MBOT_COMMON_SERVICE, MBOT_S_KEYS} from '@/common/config/mbot/service';
    import {cardLogMap, cardTypeMap} from '@/common/config/mbot/log';
    export default {
        mounted() {
            this.customSendLog({
                compTargetId: cardLogMap.show,
                userExtra: {
                    type: cardTypeMap.testCard，
                    imgType: 2  // 额外打点无需关注
                }
            });
        },
        methods: {
            handleClick() {
                this.customSendLog({
                    compTargetId: cardLogMap.click,
                    userExtra: {
                        type: cardTypeMap.testCard，
                        imgType: 2  // 额外打点无需关注
                    }
                });
            }
        }
    };
</script>
```

### 2. 埋点校验流程
前置条件:
    1、必须执行 **git diff --cached --name-only --diff-filter=ACM** 命令，找出当前所有提交的文件；如果当前目录不在m-groot目录下 需要切换到m-groot目录下，再去执行上述命令
    2、如果从条件1下获取到的文件列表中如果不包含文件名以**gt-merchant**开口的文件，则**立即结束**后续整个流程，且**严禁**多次重复确认。
    3、读取 src/common/config/mbot/index.js 文件中 CARD_TYPE对象中的 widgetName, 获取到的组件列表。

扫描执行前置条件1得到的，文件名以【gt-merchant】开头的所有提交的文件，是否有发送埋点的行为。

- 有埋点行为，每个文件必须严格执行下面的步骤
    第一步：**有埋点行为**, **严格**检查文件命名是否在**前置条件3中获取到的组件列表中**
        在，执行第二步；
        不在，执行第三步。
    第二步：检查是否使用的**cardLogMap.show** 或者 **cardLogMap.click**作为展现和点击埋点。
        使用：必须**严格**校验**userExtra.type**和**compTargetId**是否符合 **1.2中的第二类埋点函数规范** 要求，不符合进行修改,
        不使用：必须**严格**按照**1.2中的第二类埋点函数规范** 要求新增埋点
    第三步：**有埋点行为**,检查埋点是否在 **compTargetIds.js**文件中定义
        如果定义：必须**严格**校验埋点是否符合 **1.2中的第一类埋点函数规范**的要求，不符合进行修改。
        未定义：必须**严格**按照**1.2中的第一类埋点函数规范** 要求新增埋点

- 无埋点行为，每个文件必须严格按照下面的步骤执行新增埋点
    第一步：文件命名在前置条件3中获取到的组件列表中
        在，执行第二步；
        不在，执行第三步。
    第二步：必须**严格**按照**1.2中的第二类埋点函数规范** 要求新增展现和点击埋点，新增埋点需要定义customSendLog方法
    第三步：必须**严格**按照**1.2中的第一类埋点函数规范** 要求新增展现和点击埋点，新增埋点需要定义customSendLog方法

#### 2.1 校验检查清单
1、通用项检查
    - 是否引入 MBOT_COMMON_SERVICE, MBOT_S_KEYS
    - 埋点的参数格式是否正确
2、第一类组件检查项
    - 是否引入 compTargetIds 和 LOG_KEY_EXPAND_TYPE_MAP
    - 埋点ID是否在 compTargetIds.js 中定义
    - 是否使用正确的行为后缀名
    - 是否使用展开语法 ...compTargetIds[]
3、第二类组件检查项
    - 是否引入 cardLogMap 和 cardTypeMap
    - 是否使用 cardLogMap.show 或 cardLogMap.click
    - userExtra.type 是否在 cardTypeMap 中定义
    - 组件类型名称是否符合命名规范

### 3. 特殊说明
    - 原有组件：对于已存在的组件文件，
        - 如果没有埋点代码，不强制要求添加跳过校验
        - 如果有埋点，使用第一类埋点 只需要校验 埋点id 需要在 src/common/config/mbot/compTargetIds中定义
        - 如果是第二类，需要校验参考第二类组件检查项
    - 新增组件：对于新创建的组件文件
        - 如果本身无埋点，会规范添加展现和点击埋点
        - 如果有发送埋点，按照规范校验埋点，如有问题会进行修复
    - 无需强制校验 customSendLog 方法

    - **埋点配置特殊处理规则**：
        - 埋点校验流程优先于项目通用组件设计原则
        - 为保持埋点规范统一性，允许修改 `src/common/config/mbot/` 下的埋点配置文件
        - 包括但不限于：compTargetIds.js、log.js等公共埋点配置文件的修改和新增
        - 此规则允许暂时代替项目规范中的"组件独立开发，不相互引用"原则

### 4. 推送修改消息
如果执行了修改文件的操作，则执行项目中**sendMessage.sh**脚本，参数是使用命令**git config user.name**获取的用户ID
```
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
