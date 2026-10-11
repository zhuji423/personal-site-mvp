---
title: "第四组rules经验分享"
description: "基于Zulu rules实现后端自动化测试"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于Zulu rules实现后端自动化测试.md"
---
基于Zulu rules实现后端自动化测试

#### 🧑‍🏫 案例作者：[@李静敏](https://ku.baidu-int.com?t=mention&mt=contact&id=9d89af20-fce2-11f0-b3fe-5b92780c49b9)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了利用Zulu rules实现后端自动化测试的经验。通过编写规则，让模型自动梳理项目结构、生成API文档、分析接口关联关系，并生成多接口用例及pytest测试代码。该方案提高了测试代码的生成和执行效率，支持修复失败用例并分析原因，最终将成功的测试场景总结为可复用的rules，提升了测试工作的整体效能。
## 一、背景
基于项目的背景知识比如研发业务代码，API文档，需求等编写自动化测试代码执行后发现质量缺陷来控制产品质量

 并应用于研发自测阶段，回归测试阶段，线上测试阶段等是QA的高频且耗时较高的工作内容

## 二、目标
将上述过程即自动化测试代码的生成，执行，修复，bug发现各个阶段用rules规则实现，形成有效可复用的方案可迁移到各个服务去使用从而提高效率

## 三、rules具体实施
  场景一：以研发业务代码做为背景知识

###### 首先让rules梳理下当前项目结构
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b00115f9365c41fb9f3594a4255b1327&docGuid=fwgIb5r_z2Tvkt "")
###### 第二步骤 让大模型找到我们要测试的接口信息是基础
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e36aabfefb084529ac20f3aef443528a&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2054398e74d047e6813ab83d4c217179&docGuid=fwgIb5r_z2Tvkt "")
发现找到了API接口 但是没有完整的API文档 包含参数信息 我们继续完善文档

###### 3.继续生成完整的API文档，包含所有参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=23f4ce0794a34936b9205d558f493b44&docGuid=fwgIb5r_z2Tvkt "")
可以看到目前的API文档比较完整了 包含了请求 和响应的格式及示例

###### 4.接下来让我们继续分析API接口的关联关系，用来生成多接口的用例
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b83a95ac4ac9444098d55610e5e75a60&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b48a8210ab7340b3838de6b193ae1495&docGuid=fwgIb5r_z2Tvkt "")
很好，还能帮我们生成模块的流图，看起来更清晰易懂

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=998ee8a927b74c8a92b383b9fea42aef&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ee891679c0f04f97bb5600aa4b0d7746&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3d4efecd4e0a4731b1d6516ae93271aa&docGuid=fwgIb5r_z2Tvkt "")
###### 5.接下来我们让模型帮我们生成pytest测试用例，给模型一些环境信息和约束信息
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dda3a3ff180944f79133544340959b40&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ace1c5a7257041f9ab40b277e12a3283&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=56250c5b3f574653b1a8d873b6f5ae6b&docGuid=fwgIb5r_z2Tvkt "")
让我们看一下生成的结果，看起来还可以，符合我们的要求

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ef8e18bc77264665b14c252c58601640&docGuid=fwgIb5r_z2Tvkt "")
###### 6.接下来运行一下，zulu会根据环境信息自动安装必要的依赖并运行测试 点赞 👍
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e4d4e74dbcc54164acb2fb13ed332f1f&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a7d33dc4c77641c4a5fcffc946240a95&docGuid=fwgIb5r_z2Tvkt "")
###### 7.修复失败的用例
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2ae6dee4966d48ebab9f4c93ffe4ca78&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5a102172096b4029b00e191175ea9e30&docGuid=fwgIb5r_z2Tvkt "")
###### 8.对于运行失败的用例进行分析，判断是代码bug问题还是case问题
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=246b173a1f4246abb723c179da25d00d&docGuid=fwgIb5r_z2Tvkt "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2f9f86d220e243958189731828882640&docGuid=fwgIb5r_z2Tvkt "")
我们发现测试用例均已执行成功

###### 9.下面让我们根据上述过程生成rules规则
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fd2b08d43f11472a80609018e0d35f23&docGuid=fwgIb5r_z2Tvkt "")
###### 场景扩展：
接下来可以给模型更多的上下文信息 比如 需求文档，设计文档，QA历史用例等信息让生成用例的rules更健壮

## 四、实践总结
1. 如果想要场景的rules最终效果好，需要给模型更多的上下文信息
2. 更多的规则给到rules，根据规则生成结果更贴近用户想要的效果
3. 根据需求出方案，验证方案有效性，调试优化方案，最终将效果好的方案总结成rules

遇到的问题

1. 写文件失败
2. 任务执行时间长会被卡死

# 第四组rules经验分享
## 一、组内个人心得
|**组员**|**业务场景**|**心得**|
|-|-|-|
|**李静敏**|基于Zulu 实现后端自动化测试rules|1.如果想要场景的rules最终效果好，需要给模型更多的**上下文信息和更多的规则。**2.将**调试后验证有效**的方案，总结、沉淀为稳定、可复用的**Rules**。|
|**郑林**|基于百度智能助理平台（一言/Yiyan）的自动化测试框架的Rules|对于测试用例生成场景，通过限定请求格式， 参数规则（必填/可选/边界值），异常场景  ，上下游依赖关系等要素来**规范rules的编写框架**，这样生成的Rules 可以更高效生成测试用例，同时准确率也更高。|
|**李帆**|Zulu生成SDK测试工程Rules|1.**细化需求**，并描述清楚需求，不断追问细节，调试过程中**不断补充上下文信息**，生成更精准的方案。2.存在多个Rules可以采用**动态Rules**方式灵活处理不同情况下的任务。|
|**李少航**|代码自查和代码规范检查Rules实践|1.**整理思路**：明确要转换的内容和规则。2.生成规则：使用Zulu生成初始规则。3.编辑和修改：根据需要对规则进行调整。4.**添加排除规则**：对于不希望被修改的部分，制定排除规则，这些规则在最后应用，以保护某些内容。|
|**迪力亚尔·帕尔哈提**|基于易水平台测试任务调度中心的Rules|1.鼓励Zulu自我纠错：如果生成的代码有问题，不必失去耐心。应指示Zulu自行查找问题并**自我迭代修复**，此过程往往比人工阅读修改更为迅速。**2.复杂任务重置上下文**：在同一会话中连续开发多个接口会积累干扰，导致反应变慢。最佳实践是：将公共规则固化到基础文档中，然后开启新会话进行后续开发，以确保最佳性能。|
|**张艳**|通过Rules执行实现数据集自动化测试|1. 稳定性：生成过程中遇到卡死的情况，**不要盲目等待**，可以直接取消任务重新生成。2. 数据展示：当前报表类输出的默认数据格式可读性有待提升，可以用“标准表格形式输出“**引导语输出**表格，确保数据展示更加直观清晰。|

## **二、总结**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c334056eff954a24a4524854341520a5&docGuid=hce07WD5eXcAHn "")
**1. 信息输入：提供充足的“燃料”**

* **原则**：将Zulu视为资深专家，其输出质量直接取决于我们输入的“信息质量”。
* **做法**：提供详尽的业务背景、接口文档、参数约束、指令词、边界场景和依赖关系，避免让Zulu在“黑暗中猜测”。

**2. 方案生成与验证：构建“测试-学习”闭环**

* **原则**：首版方案通常是原型，需要通过实践来检验和修正。
* **做法**：基于初始规则生成方案后，必须进行有效性验证，可让Zulu生成自动化测试用例来运行验证，将结果与预期进行比对，识别差距。

**3. 调试与优化：实施精准“手术”**

* **原则**：调试是迭代的关键，而非失败。
* **做法**：根据验证结果，精准调整规则细节，例如修正参数边界、补充异常场景或明确依赖关系。遇错直接反馈，令其**“**自查修复**”**，速度远超人工修改。

**4. 规则固化：将“最佳实践”流程化**

* **原则**：将调试后验证有效的方案，总结、沉淀为稳定、可复用的Rules**。**对于复杂项目、多场景的应用，可采用**动态Rules**，灵活处理不同场景任务。
* **价值**：至此，可将宝贵的实践经验，转化为了一个可复用、可扩展的系统性工作方法。



> 要点：**高质量的rules，源于丰富的上下文和经过验证的规则**
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
