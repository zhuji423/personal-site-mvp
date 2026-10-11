---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "商业RD小刚CTS实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\商业RD小刚CTS实践.md"
---
商业RD小刚CTS实践

#### 🧑‍🏫 案例作者：[@徐健](https://ku.baidu-int.com?t=mention&mt=contact&id=314ed750-fceb-11f0-87a5-1dc5de9c1097)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Ducc
#### 📒 案例概要：本文介绍了百度商业团队利用大模型（LLM）提升CTS测试效率的实践，通过“RD小刚”插件实现测试用例生成与验证修复，显著提高测试效率与质量。该插件降低测试门槛，使新人也能快速产出合格测试代码，并助力团队优化测试覆盖率，节省大量人力成本。
🔥商业ENIAC杯AI Coding大赛相关事宜可加群：[12154968](baidu://viewobject/?type=group&id=12154968)

🔥AI IDE及百度CC相关问题可加群：[12063827](baidu://viewobject/?type=group&id=12063827)

## **前置安装与使用指南**
Comate AI IDE客户端：可通过 [官网安装](https://comate.baidu.com/zh/download?track=AIIDEfromBaidu-Int) 下载最新版，若已安装了AI IDE，可通过右上角“重启以更新”。默认会自动搭载Ducc。

RD小刚插件：Teminal中内执行`ducc marketplace install RDxiaogang`

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0e0215b2f7504176826f855205429da6&docGuid=IpEc3vnRX6aigH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4a007fec7e2d4313b76d03692d0f633c&docGuid=IpEc3vnRX6aigH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac91a824a5324f84ad67b8d634c3d016&docGuid=IpEc3vnRX6aigH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4c8362d871c4432cacbc86ec40719d27&docGuid=IpEc3vnRX6aigH "")
IDE内三级目录下打开Ducc执行/RD小刚命令

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=73f917906f054e72952dbc5b03be3e07&docGuid=IpEc3vnRX6aigH "")
## 常见异常情况解决方案
1. 执行`ducc`命令后提示`ducc: command not found`

* 方式一：完全退出IDE后，重启。
* 方式二：新开一个Terminal终端。

2. 执行`ducc marketplace install RDxiaogang`后未成功安装RD小刚插件。

* IDE左侧商店里面卸载已经安装的ducc插件
* 在 IDE 内使用快捷键 cmd + shift + p
* 输入 Baidu Comate: Clear Global State Key 找到对应选项......
* 输入"baiducc"，即可删除安装记录，然后 重启IDE 就会重新安装 ducc了

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0e4fa76848434487b3062e5cb7104f8d&docGuid=CMZnRdLpiznoht "")
## **一、摘要与概述**
1. **核心结论：** 大模型（LLM）为功能测试的自动化与智能化带来了革命性潜力，尤其在测试用例生成领域已取得显著进展，但距离全流程、高可靠性的无人化应用仍有距离。
2. **主要进展：** 商业侧CTS测试用例三条技术路径均已跑通，并在特定场景下展现出极高效率，成功将部分测试用例编写工作从“小时级”缩短至“分钟级”。
3. **核心挑战：** 生成结果的**稳定性、准确性、上下文深度**仍是主要阻塞点，严重依赖高质量的输入（Prompt Engineering）和高质量模型能力（Model Capability）。
4. **未来方向：** 构建全面的业务知识工程、打造“测试智能体”、实现闭环评估与自优化是下一阶段的重点。

## **二、背景与挑战**
1. **行业趋势：** AI在软件工程中的应用，测试是最高频的场景之一。
2. **团队痛点：**

    * 业务快速迭代带来的测试压力与日俱增。根据前期对核心业务迭代的RD同学的抽样统计，RD同学平均每次升级需要**编写约100行-500行**不等的CTS测试代码，DEBUG自测**耗费约2小时-5小时**不等。
    * 测试用例的形式是python代码形式，技术门槛很高。新人上手周期长，平均需要**2-3个月的学习培训**才能独立产出合格测试代码。
    * 代码变更（CR）频繁，人工评估测试影响域易遗漏。
    * 长尾场景、边缘用例覆盖率难以保证。

3. **目标：**

    * **提升效率：** 极速生成高质量测试用例（代码形式）。前期统计预估可测性工作上可**节省50%+的人耗**。
    * **保证质量：** 补齐测试覆盖率，尤其针对代码变更和覆盖盲区。
    * **降低门槛：** 让新人研发也能通过自然语言驱动自动化测试生成。

## **三、“RD小刚”插件**
为解决上述痛点，我们在IDE场景内结合百度Claude Code推出了“RD小刚”插件，支持**CTS用例生成、CTS验证修复**两大功能。它作为一个轻量级工具，无缝集成于厂内AI IDE中，为开发者在编码阶段提供强大的CTS测试支持。

### **3.1 核心功能一：CTS用例生成**
**功能描述：**
该功能允许开发人员直接在源代码界面，通过简单的斜杠命令 “/RD小刚:CTS用例生成” 操作，针对本次升级，一键生成CTS测试用例及对应的测试环境。

**工作流程与价值：**

1. **操作简便：** 在IDE中，右上角打开“百度CC”，通过斜杠选择“/RD小刚:CTS用例生成”。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ec7a32907c24cedbeaf03b294fb1a6b&docGuid=rruLZml6K7xreC "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3fec6d010adc47238b3ad2c3322e8f28&docGuid=rruLZml6K7xreC "")
2. **智能分析：** RD小刚会智能识别变更范围、深度代码分析（理解代码改动、调用链追踪、配置提取及设计等）、学习用例规范、生成测试用例/环境。
3. **自动生成：** 生成一个结构完整、包含数据构造、配置组合、日志断言的完整测试用例文件。

[附件]
4. **价值：**

    * **提升效率：** 将测试用例编写时间从数小时缩短至分钟级别。
    * **降低门槛：** 即使不精通CTS规范的开发者也能快速产出标准测试用例。
    * **保证规范：** 生成的用例结构符合标准，减少了因手写导致的格式错误。

### **3.2 核心功能二：CTS验证修复**
**功能描述：**
此功能实现了在IDE内部“RD小刚”直接运行、验证、调试和修复CTS测试用例。

**工作流程与价值：**

1. **本地执行：** 在AI IDE的代码库三级目录下，右上角打开“百度CC”，通过斜杠选择“/RD小刚:CTS验证修复”，即可开始自动执行。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9a660c47b4c74fec962de5f5c7c32cbb&docGuid=rruLZml6K7xreC "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cba64d7e005041269d3f753e8f4003bd&docGuid=rruLZml6K7xreC "")
2. **环境搭建：** RD小刚熟悉CTS任务执行流程，可自动检测本地环境是否完善，可帮助开发着完成本地编译、CTS环境搭建等操作。
3. **验证与修复：** RD小刚可像开发者一样验证、调试、修复。多轮反思执行，快速定位CTS失败的根本原因并修复测试用例代码。

[附件]
4. **价值：**

    * **效率提升：** 将“修改-验证”循环从小时级缩短分钟级，极大加速CTS调试过程。

## **四、为团队带来的核心价值**
AIQA反思测试用例生成补充覆盖率，目前赋能项目数40+，用例生成成功率94.74%，一次通过率76.32%，覆盖率达成率31.58%。

|价值维度|具体收益|
|-|-|
|**效率提升**|将CTS相关工作的耗时从“天/小时”级别降低到“分钟”级别，大幅缩短项目周期。|
|**质量保障**|实现测试左移，让兼容性问题在开发阶段尽早暴露和修复，降低后期修复成本。|
|**成本降低**|减少手动操作和重复劳动，解放开发人力，使其能专注于更高价值的创新工作。|
|**能力普及**|降低CTS测试的技术门槛，使团队所有成员都能高效参与。|
|**流程优化**|无缝集成至现有开发流程，无需改变团队习惯，即可享受自动化带来的便利。|

### **五、结语与呼吁**
“RD小刚”不仅仅是一个工具，更是我们迈向更高水平研发效能的重要一步。它旨在将团队成员从繁琐、重复的劳动中解放出来，让大家能够更多地享受编码和创新的乐趣。我们强烈建议并鼓励所有相关的开发同事**立即尝试安装和使用**本插件。您的实践反馈对于我们持续改进和优化产品至关重要。让我们携手，共同打造更加流畅、高效的开发测试体验，为公司产品的质量与竞争力保驾护航！

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
