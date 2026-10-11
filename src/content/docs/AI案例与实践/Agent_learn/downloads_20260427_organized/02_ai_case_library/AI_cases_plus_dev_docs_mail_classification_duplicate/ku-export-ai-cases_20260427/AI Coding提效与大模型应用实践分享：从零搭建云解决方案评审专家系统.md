---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "AI Coding提效与大模型应用实践分享：从零搭建云解决方案评审专家系统"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI Coding提效与大模型应用实践分享：从零搭建云解决方案评审专家系统.md"
---
AI Coding提效与大模型应用实践分享：从零搭建云解决方案评审专家系统

#### 🧑‍🏫 案例作者：[@程广连](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：设计、开发、评估、模型
#### 🔧 使用工具：码力随心搭、知识库、如流机器人、Comate、文心一言
#### 📒 案例概要：在数字化转型浪潮中，企业级解决方案评审环节长期存在三大痛点：
1. 评审效率低下：传统专家评审需多人会议，跨部门协调耗时；
2. 知识传承断层：专家经验难以沉淀，新人培养周期长；
3. 标准执行偏差：人工评审易受主观因素影响，质量波动大。

作为技术团队，我萌生了用AI重构评审流程的想法：能否通过大模型+低代码，打造一个24小时在线的"智能评审专家"？ 这个设想最终落地为"云解决方案评审专家系统"，其核心价值在于：
* 效率提升：将数小时的评审周期压缩至10+分钟；
* 知识固化：将专家经验转化为可复用的AI模型；
* 标准统一：通过算法消除人为判断差异。
## 一、初心：用AI解决传统评审的痛点
在数字化转型浪潮中，企业级解决方案评审环节长期存在三大痛点：

1. **评审效率低下**：传统专家评审需多人会议，跨部门协调耗时；
2. **知识传承断层**：专家经验难以沉淀，新人培养周期长；
3. **标准执行偏差**：人工评审易受主观因素影响，质量波动大。

作为技术团队，我萌生了用AI重构评审流程的想法：**能否通过大模型+低代码，打造一个24小时在线的"智能评审专家"？** 这个设想最终落地为"云解决方案评审专家系统"，其核心价值在于：

* **效率提升**：将数小时的评审周期压缩至10+分钟；
* **知识固化**：将专家经验转化为可复用的AI模型；
* **标准统一**：通过算法消除人为判断差异。

## 二、实现路径
### 技术选型：AI低代码+文心大模型
我选择**码力随心搭平台+Panda平台**作为技术底座，其核心优势在于：

* **低代码开发**：通过可视化界面快速构建应用，降低技术门槛。
* **大模型工具**：提供ERNIE 4.5、ERNIE Speed、GPT-4、DeepSeek-V3.2等适配不同场景的模型；

**关键决策点**：

* 通过码力随心搭搭建前端界面，支持读取知识库设计文档，可以真正实现"零代码"开发。
* 选择ERNIE 4.5 8k作为评审模型，通过多个模态联合建模实现协同优化，多模态理解能力优秀；具备更精进的语言能力，理解、生成、逻辑、记忆能力全面提升，去幻觉、逻辑推理、代码能力显著提升；
* 使用HTTP API提供项目方案数据，将内部经验文档转化为训练数据；

### 核心能力：方案评审API的智能实现
**方案评审API**是系统的核心，其实现包含三个关键步骤：

1. **提取规划方案**：

    * 提取蓝图项目规划方案关键数据
    * 关键数据包括：服务器用途、服务器数量、服务器详细配置等

![](/personal-site-mvp/img/doc-placeholder.svg "")


2. **评审能力所需知识：**

    * 撰写评审经验和技能
    * 调试经验：知识内容要有条理，有层次结构

![](/personal-site-mvp/img/doc-placeholder.svg "")
3. **提示词工程**：

    * 首先将评审所需知识输入到大模型，并描述知识的内容结构，使用条件限制等
    * 明确需要大模型做什么事情，任务的步骤方法，预期的结果，如果有示例则更好
    * 调用大模型调试功能，不断调整优化Prompt(可以先用其他大模型优化自己的Prompt，再自己调整)
    * 直到可以按照预期完成方案可行性分析，输出评分与改进建议

4. **结果生成**：

    * 自动生成评审报告，包含风险点、优化建议、合规性结论；
    * 支持markdown格式

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 白屏化功能：UI设计与实现
码力随心搭平台( [https://lowcode.baidu-int.com/ai-coding](https://lowcode.baidu-int.com/ai-coding))是厂内优秀的低代码平台之一，在用户鉴权等方面具备天然优势。

* 首先撰写白屏化的需求，该需求较为简单，提供录入项目方案的URL，然后可以返回评审报告即可。

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 将需求写入知识库，然后将知识库链接录入到随心搭平台
    * 随心搭平台支持文本框录入需求，我这里用知识库来保存，方便后续调整优化，能够把内容系统化的记录下来，后续迭代更方便

* 随心搭平台完成需求分析并完成代码编写，根据生成平台预览功能，进行代码/需求微调，直至满意
    * 需要注意，当前随心搭平台支持限定后端开发语言，但只有nodejs支持平台部署运行。


![](/personal-site-mvp/img/doc-placeholder.svg "")
## 三、成果展示
[云解决方案评审专家系统](https://aicoding-sandbox-prod.dev.weiyun.baidu.com/apps/app-by6ubit2mkmx/?t=mention&mt=doc&dt=sdk)支持浏览器页面和如流群工作台。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")
## 四、经验总结：AI落地的关键要素
### 1. 数据质量决定模型上限
* **数据清洗**：需去除重复、错误、过时数据，确保训练集质量；
* **特征工程**：对文本进行分句、实体识别、情感分析等预处理；
* **持续迭代**：通过A/B测试验证模型效果，定期更新训练数据。

### 2. 模型选择需平衡性能与成本
* **轻量化模型**：对实时性要求高的场景（如API调用），选择ERNie Speed；
* **大模型微调**：对复杂任务（如方案评审），使用ERNie 4.5并进行领域适配；
* **混合部署**：核心功能用大模型及API能力实现，交互能力用低代码平台降低成本；

## 五、未来展望：从评审专家到决策大脑
三大升级方向：

1. **实时协作**：通过语音识别、自然语言交互实现人机协同评审；
2. **预测分析**：基于历史数据预测方案实施风险，提供决策建议；
3. **规划能力**：基于客户诉求、成本竞价、产品能力等多维度，自动完成方案设计

**结语**：

通过AI低代码与大模型的结合，我们不仅实现了评审效率的量变，更推动了评审质量的质变。未来，我们将继续探索AI在数字化转型中的深度应用，让技术真正成为企业增长的引擎。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
