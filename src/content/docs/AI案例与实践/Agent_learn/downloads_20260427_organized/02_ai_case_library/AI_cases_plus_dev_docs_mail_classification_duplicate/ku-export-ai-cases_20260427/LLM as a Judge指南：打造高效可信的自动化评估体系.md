---
title: "背景"
description: "LLM as a Judge指南：打造高效可信的自动化评估体系"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\LLM as a Judge指南：打造高效可信的自动化评估体系.md"
---
LLM as a Judge指南：打造高效可信的自动化评估体系

#### 🧑‍🏫 案例作者：AI原生研发圆桌会
#### 🎬 案例场景：评估
#### 🔧 使用工具：Comate Stack, 蒸汽机绘想
#### 📒 案例概要：本文聚焦大模型自动化评测实践，来自百度MEG、蒸汽机团队等的分享涵盖语言模型、多模态生成及工具类评测框架。MEG在模型评测方面主要关注业界大模型选型评测和模型/策略业务迭代评测两个场景，采用judge-by-rule和judge-by-llm等方法。Comate Stack提供AI原生研发工具集，支持从生成式评估策略到智能AI表格的灵活评测方式。圆桌会强调建立系统化、可解释的评估体系，推动大模型从"单点能力验证"迈向"系统化、可解释、业务驱动"的智能评测新阶段。
**导语：**

为加速AI原生研发新范式在研发团队的落地，今年在TSC的牵引下，BIT联合EE&数据工程TOC推出本期【AI原生研发圆桌会】，旨在聚焦AI原生研发场景，组织厂内有相关实践和交流需求的同学，围绕业务实践落地中面临的关键问题和挑战，过程中积累的好经验/踩过的坑...展开深度的讨论与交流，促进跨业务间经验的流转与复用。



# 背景
当下，大语言模型评测已成为驱动模型选型与业务迭代的关键引擎，在自动化评估、多维度量化与效果对齐中扮演核心角色。业界借助LLM as a Judge提升评测效率，却仍面临一致性、稳定性与偏好偏差等挑战；MEG通过构建面向业务的高区分度数据集、细化评估维度与自动化打分方案，为模型选型与策略迭代提供可靠依据；蒸汽机团队以端到端评估体系支撑视频生成大模型的高效迭代，实现训练评估2小时、发布周期提速至2-3天；自动化评测技术系统梳理了语言、多模态及工具类评测框架，深入实践基于规则与基于大模型裁判的评估方法，推动评测流程标准化与灵活适配；Comate Stack更以AI原生研发平台赋能全流程评估，支持从生成式评估策略到智能AI表格的灵活评测方式。本期【AI原生研发圆桌会】聚焦大模型自动化评测实践，汇聚多位业务一线的同学，从语言模型、多模态生成到研发工具链，共同探索更科学、可解释、高效率的模型评估路径。

接下来，让我们深入本次h活动的精彩内容，在思想的碰撞中收获真知，激发灵感。

**现场分享视频请点击**👉[自动化评测实践分享](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56246?isFromPc=1&reportLog=true?t=mention&mt=doc&dt=sdk)

---

# 核心内容速览
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 实践分享详情
![韩照光（MEG-移动生态质量效能部）](/personal-site-mvp/img/doc-placeholder.svg "韩照光（MEG-移动生态质量效能部）")
![王伟（MEG-移动生态质量效能部）](/personal-site-mvp/img/doc-placeholder.svg "王伟（MEG-移动生态质量效能部）")
![张文婧（ACG-产品质量部）](/personal-site-mvp/img/doc-placeholder.svg "张文婧（ACG-产品质量部）")
![陈耀宗（TPG-工程效能部）](/personal-site-mvp/img/doc-placeholder.svg "陈耀宗（TPG-工程效能部）")
# 主题一：大语言模型评测业务实践——韩照光
# 一、问题背景（LLM as a judge）
当前大模型评测的常见方案和存在问题：

![](/personal-site-mvp/img/doc-placeholder.svg "")
对于裁判员模型（LLM as a Jundge）评测方案来说,  存在一致性与稳定性不足、位置偏差问题、模型偏好等问题， 为解决这些问题业界也有一些方案，如多次采样， 多裁判员模型交叉打分， G-Eval评估框架等。 

而MEG 在模型评测方向主要 业界大模型选型评测（评测标准通用） 和模型/策略业务迭代（评测标准专业且复杂&打分人工一致性要求更高）评测2个场景， 分别介绍一下我们的方案。

# 二、业界大模型选型场景自动化评测
**业界模型选型场景目标：** 为业务大语言模型选型、基座切换提供更高效、更专业模型选型 建议

![](/personal-site-mvp/img/doc-placeholder.svg "")
整体方案： 从数据集构建， 评估标准， 自动化评测方案3个方向展开

||MEG文本大模型评测方案|业界通用评测方案|
|-|-|-|
|数据集|MEG业务数据集+业界富集数据集改造|MMLU，MATH，**GSM8K，**‌**HumanEval,  LogiQA等**‌|
|答案类型|开放式问题+参考答案|客观固定答案为主（选择、填空、短句等）|
|评估指标|自定义评估标准|blue，rouge， accuracy等指标|
|评估方式|高阶裁判员大模型|工程指标算法|
|榜单排行|聚焦MEG场景数据集和落地场景，给出主客观， 以及细分子维度平均得分排行， 及模型优缺点数据分析|业界榜单一般采用各个模型在不同数据集上得分进行排名， 或者在匿名对战人工打分总分进行排名|

## **2.1 数据集构建思路**
    * **面向 MEG 业务场景的模型能力覆盖**：评测数据集基于线上真实用户 query 构建，覆盖MEG 核心业务所有子场景，确保评估结果能够真实反映模型在实际应用中的能力表现与差异。
    * **具备代表性与区分度的数据集设计**：在客观类评测任务中，融合业界公开数据与业界主流评测文章中的高质量、高区分度 query，确保数据集在多个模型能力维度上具备良好的区分效力，支持精细化能力分析与模型优劣识别。
    * **代码编程数据集：**重点关注当前评测公司&业界关注的大模型热点能力--代码编程能力，** ** 从业界基准数据与业界主流评测query，构建简单， 中等难度，高难度3种级别的数据集， 覆盖livecode（竞赛算法）， swe-bench verified（软件工程），前端UI设计等不同维度的代码编程场景。

## 2.2 评估标准
### 2.2.1 开放式问答（主观数据集）评估标准
![](/personal-site-mvp/img/doc-placeholder.svg "")
* **主观数据集评估标准：**从内容质量， 指令遵循， 幻觉问题， 创作生成， 摘要总结， 人格化， 联调搜索7个一级维度， 10个二级子维度进行分维度打分



|评估维度|评估子维度|是否核心|维度说明&打分标准||
|-|-|-|-|-|
|内容质量|准确性|是|0分：存在事实错误或逻辑矛盾；1分：基本正确但偶有误差；2分：信息准确，逻辑清晰。||
||完整&相关性|是|0分：内容残缺，关键信息缺失；1分：内容基本完整但细节不足；2分：内容全面，覆盖所有要点。||
|指令遵循|指令遵循|是|0分：完全偏离指令目标，导致回答错误；1分：部分完成任务，格式要求未遵循等；2分：准确理解并完整执行任务。||
||自然语言理解|否|0分：无法正确理解输入，在意图识别、指代消解、歧义处理、上下文理解等维度出现混乱1分：能识别基础语义与意图，但在复杂句式、上下文推理、歧义处理等方面能力有限，出现误解。2分：能较好理解复杂结构与隐含逻辑，处理跨句信息、歧义、指代与推理问题||
|幻觉问题|幻觉|是|0分：生成虚假或矛盾信息；2分：无虚构内容，事实准确||
|创作生成|创作生成|否|0分：内容平庸，缺乏想象力；1分：内容啰嗦冗余；有一定见解，但无创新2分：有吸引力，和启发性。观点有深度，能引发思考||
|摘要总结(语义理解&提取)|摘要总结|否|0分：遗漏重要信息；1分：提取部分关键信息但完整性不足；2分：全面覆盖核心要点。||
|人格化|情感表达|否|0分：情感生硬，缺乏共情；1分：情感表达适中但不够自然；2分：情感细腻，引发共鸣。||
||人设保持|否|0分：风格突兀，与设定不符；1分：风格基本统一但偶有偏差；2分：风格鲜明，贯穿始终。||
|联网搜索|信息时效性|是|0分：信息过时或错误；1分：信息基本准确但非最新；2分：信息最新且经过验证。||
||可靠权威性|否|0分：来源不明或不可信；1分：来源有一定可信度但非权威；2分：来源权威，引用规范。||



### 2.2.2 客观（有参考答案、要点）数据集评估标准
|评估维度|评估子维度|打分说明|
|-|-|-|
|客观数据集|逻辑推理|0分：答案错误。  1分：答案正确，但推理或分析过程存在错误，或者推理过程冗长、不够简洁易懂，包含不必要的步骤或重复表述。  2分：答案正确，推理或分析过程正确，并且表达简洁清晰，无冗余信息，能够准确呈现关键逻辑。 |
||数学||
||指令遵循||
||常识问题||
|代码编程|代码生成|0分：编译不通过， 或测试用例执行不通过  1分：编译通过且测试用例执行通过，但评估代码存在性能、可读性、安全性、鲁棒性等维度存在1个或多个问题2分：编译通过且测试用例执行通过，且评估代码在性能、可读性、安全性、鲁棒性等维度也不存在问题|

## 2.3 自动化评测方案
![](/personal-site-mvp/img/doc-placeholder.svg "")
* 主观数据集
    * 将主观数据评分标准转化， 与生成结果组合发送给高阶裁判员大模型， 不断优化评估prompt， 将大模型打分与人工打分进行对比评估， 一致率>85%。
    * 针对联网实效类query,  挂接搜索api， 构建评估agent，解决实效性信息来源问题

* 客观数据集
    * 大模型以参考答案为主要依据进行自动化打分，并结合推理过程分析进行分档划分

* 代码编程
    * 以代码生成或修复后的程序是否能通过测试用例为主要标准
    * 结合大模型进行代码性能、鲁棒性、语法等检测进行分档打分


对于开放性主观数据集 主要思路 提高打分过程的可解释性，（类似G-Eval评估框架的思路，为了平衡效率，未多次采样，结合人工复检保持准确性）

*  **分维度评分**：而不是给总分，要求裁判逐项（流畅性、相关性、覆盖度）打分。
* **理由链约束**：Prompt 中要求“逐步说明理由”，并与评分结果严格绑定。
* **分维度加权规则减少极端场景出现概率。加权打分规则**：
    * - 若任两个**核心子维度得分为 0 分** → 汇总评分为 **0 分**，不考虑非核心项
    * 若任意两个**核心子维度得分为 1 分**，且其他**核心子维度得分为 2 分**→ 汇总评分为 **1 分**，不考虑非核心项
    * 若任意全部**核心子维度得分为 2 分**，则核心子维度总得分1分，然后依次按照**非核心子维度**进行评估，满足标准，则总得分加0.2，部分满足标准，则总得分加0.1，不满足，则总得分加0，总得分最高为2分。
    * 加权统计规则不放在prompt 里面，单独在脚本中计算，避免模型计算幻觉


# 三、大模型在业务场景自动化评估（基于微调模型）
## 3.1 业务场景大模型生成效果评测面临的问题
![模型在业务迭代中一般流程和问题](/personal-site-mvp/img/doc-placeholder.svg "模型在业务迭代中一般流程和问题")
从上面的流程可以看出， 当前模型或策略在业务产品迭代过程中，存在评测效率低，成本高的问题。 QA通过自动化评测提高迭代效率， 降低评估成本。  而业务场景模型生成内容， 存在以开放式结果 为主（例如电商口播剧本，直播问答，妙笔，百家号的文章改写、扩写或生成）特点，存在以下几点挑战：

1. PM制定的人工评估标准非常复杂
2. 开放式生成内容，无参考答案或参考要点， 只能高阶大模型做裁判员进行评测打分
3. 基于1&2， 直接微调打分prompt输入给裁判员大模型， 打分准确率（与人工打分一致性）很难对齐， 而自动化评测或测试一个基本前提就准确&稳定。



**在业务场景下大模型自动化评测目标**： 提升大模型/策略迭代 评测效率，降低评测成本

## 3.2 基于微调大模型自动化评测方案
![微调评测模型的一般流程](/personal-site-mvp/img/doc-placeholder.svg "微调评测模型的一般流程")
![基于简化人工标准标注训练数据](/personal-site-mvp/img/doc-placeholder.svg "基于简化人工标准标注训练数据")
**微调评估大模型一般流程和经验：**

* 基座模型选型： 优先选择指令遵循能力强，概括总结能力，文本创作能力强的轻量级、高性能模型
* 简化评估标准： 将繁杂（二，三级标准）人工评估标准优化为大模型可识别遵循的评估标准，标准层级不超过2级
* 训练集标签筛选：
    * 数据质量， 多样性 大于数据集数量（>400）
    * 标注打分同时标注分档原因，告诉模型不同子维度分档原因

* 模型SFT微调： 基于失败case 从正反2个方向优化标注数据（正向数据集补充，反向数据集优化）
* 数据隔离打造专项评测模型： 构建相同量级的数据集， 可将多个评测场景集中到同一个评估大模型中，节省硬件资源

# 
# 主题二：蒸汽机模型开发中的自动化评测实践——王伟
# 一、蒸汽机视频生成大模型
****[蒸汽机（绘想）](https://huixiang.baidu.com/)是 MEG 商业团队自研的、全球首个中文音视频一体化生成的视频生成大模型，也是百度首个对外发布的视频生成大模型，打破了百度大模型技术在视频生成领域的 0 的突破。

虽然起步晚，但是基于强大的技术团队、深厚的 AI 技术积累、丰富的中文语料，蒸汽机研发团队快速实现了视频大模型从研究到产品化。

项目启动

登上Vbench-I2V 榜首

对外发布 1.0 版本

对外发布 2.0 版本

![蒸汽机模型的特点](/personal-site-mvp/img/doc-placeholder.svg "蒸汽机模型的特点")
![蒸汽机模型不同系列的能力对比](/personal-site-mvp/img/doc-placeholder.svg "蒸汽机模型不同系列的能力对比")
![](/personal-site-mvp/img/doc-placeholder.svg "")
创意描述：

身着传统汉服的男女乘坐在民航客机舱内。人物按照先男后女的次序进行对话交流，男："待会可不能跟父皇说咱们去玩了啊！" 女："不会不会，要不咱们下次还怎么出来啊！" 背景显现航空座椅与窗外云层。

[附件]
* 以视频编码器架构为例，一般视频的编码器中，都会包含一个解码器模块，以快速验证并调整相关的编码参数，保障编码的效果。



* 同样的，高效、置信的模型评估能力，为蒸汽机视频大模型的快速迭代提供了基本的保障。

![H264 视频编码器的架构图](/personal-site-mvp/img/doc-placeholder.svg "H264 视频编码器的架构图")
# 二、蒸汽机模型的评估体系
* 我们与蒸汽机团队的产品、研发进行了多次沟通，从评估标准、评估数据、评估方式等多个方面，协同构建起了一套端到端、高效的、置信的视频生成大模型的评估体系。
* 实现了训练阶段评估周期为 2H、测试阶段评估周期为 1 天的高效评估，模型训练发布提效 50%，从周级别提速到2-3天，为蒸汽机模型的快速迭代发挥了重要作用。

大模型 `开发`→`发布`的端到端、全流程如下图所示，在这个过程中，越到后期，评估的成本越大，越影响模型的迭代效率。

[流程图]
* 模型训练阶段，自动化评估+快速人工抽检，评估左移，用相对固定的数据集和指标提前暴漏模型的劣化问题；
* 模型测试阶段，扩大评估样本，增加竞对效果评估，用相对较新的数据集重点发现模型的优势区以及薄弱区，为模型后续迭代提供参考；

## 2.1 训练阶段自动化评估
基于 PDC 与 VBench 实现推理、评测一体化的工程化 pipeline。 

[流程图]
1. 多样化的【推理包】和【测试集】管理能力，方便用户调研
2. 推理、评测一体化，配置灵活，自动发起推理和评测任务

![测试集和部署包管理界面](/personal-site-mvp/img/doc-placeholder.svg "测试集和部署包管理界面")
![发起推理&评测界面](/personal-site-mvp/img/doc-placeholder.svg "发起推理&评测界面")
3. 实时更新推理和评测任务状态，可视化各指标打分详情
4. 模型的不同checkpoint之间的打分 Diff 分析

![任务查询界面](/personal-site-mvp/img/doc-placeholder.svg "任务查询界面")
![不同任务指标diff对比分析](/personal-site-mvp/img/doc-placeholder.svg "不同任务指标diff对比分析")


当前效果：

* 平台支持评测 3000+，昆仑芯训练架构部同学也在使用该能力。
* 赋能百度蒸汽机 VBench-i2v 榜首

## 2.2 数据集自动化pipeline
为什么要构建数据集 pipeline?一套样本用到底是否可以？

* 类似 SuperCLUE 的榜单，只给出打分和排序，并未给出评估集，不利于模型的后续迭代和优化。
* 缺乏评估集，其他机构也就无法复现评估结果，评测结论也不客观。
* 评测是一个抽样的过程、而大模型又存在概率性，一套样本用到底不利于评估模型的泛化能力。
* 人工构建视频评估集成本相对较大，从图片获取、撰写提示词、增加标签分类的全流程，构建一条样本大致需要 10min。

基于自动抓取系统和 VLM 的评估样本自动化生产 pipeline。

[流程图]
基于 VLM 的、多系统整合的、一键式、自动化数据集 pipeline 生产线。

![](/personal-site-mvp/img/doc-placeholder.svg "")


当前效果：

* 200W 视频数据作为源料库；
* 每天可以自动生产 200+ 视频评估数据集；
* 打通核心竞对的数据抓取能力；

![样本集自动筛选](/personal-site-mvp/img/doc-placeholder.svg "样本集自动筛选")
![生成的样本集与测试视频](/personal-site-mvp/img/doc-placeholder.svg "生成的样本集与测试视频")
![数据集自动抓取](/personal-site-mvp/img/doc-placeholder.svg "数据集自动抓取")
## 2.3 测试阶段自动化评估 
先做好评估体系的建设，然后再对其中的评估指标进行自动化、工具化建设，才能真正做到即快又准。

LLM 评估体系是一套系统化、可复现的方法论，用来衡量 LLM 在真实场景中的效果与价值。我们构建了六位一体的评估体系：

* 评什么：评测维度，分业务场景整理样本和打分
* 用什么评：评测集，用什么样的数据集评估 LLM 效果
* 怎么评-指标：评估指标，用哪些指标评估 LLM 效果
* 怎么评-方法：评估方法，人工评估还是自动评估
* 怎么评-策略：评估策略，如何用评估方法给指标打分，对比打分、成对 GSB 打分、无参考打分？
* 怎么算：打分策略，如果根据多指标计算单样本的打分，如何根据多样本计算 LLM 最终打分？

[流程图]
`评分细则`式的评估指标与`否决式打分`的打分策略。

* 蚂蚁和浙大在论文 [Reinforcement Learning with Rubric Anchors](https://arxiv.org/abs/2508.12790) 中提出了`评分细则`与`否决式打分`的模型训练奖励机制。
* `评分细则`：精心设计的一套结构化、可解释的评估指标标准。

![](/personal-site-mvp/img/doc-placeholder.svg "")
* `否决式`打分策略：一些关键的、不可协商的维度，一旦失败，就可以直接否决所有其他维度的打分。

$scores = \begin{cases}
0,\quad & \text{如果存在任一核心指标得分为 0} \\ \frac{
2 \times (\text{5 个核心指标打分} \cdots) + 1 \times (\text{5 个非核心指标打分} \cdots)}{15} , \quad & \text{否则}
\end{cases}$

基于 LLM-as-a-Judge 的自动化指标打分方式。

虽然，近期也有学者不断提出：**LLM as a Judge** 的方式并不靠谱，例如：

* 2025 年 8 月，[Neither Valid nor Reliable? Investigating the Use of LLMs as Judges](https://arxiv.org/abs/2508.18076) 和  [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play? ](https://arxiv.org/abs/2508.10014)这 2 篇论文均提到 LLM 裁判，还远不够“拟人”，还不够靠谱。



除了我们上面介绍的评估集 pipeline 会大量的用到 VLM，很多业界的数据集富集研究也会大量的用到 VLM。因此我们认为，在视觉大模型上，**LLM as a Judge** 是可行的。在我们的 10 个打分指标中，我们完成了其中的 8 个指标的自动化打分能力。

基于 CV 算法打分

* 视频流畅度

基于小模型打分

* 视频清晰度
* 主体一致性
* 背景一致性
* 动作幅度

基于 VLM+Prompt Engineering 打分

* 文本指令遵循
* 首帧图片和视频一致性
* 运镜语言遵循

LLM as a Judge 的流程与示例如下所示：

确定评估标准（以文本指令遵循指标为例）

![](/personal-site-mvp/img/doc-placeholder.svg "")
定义响应格式

![](/personal-site-mvp/img/doc-placeholder.svg "")
选择作为裁判员的 LLM

Qwen2.5-VL-72B

当前的自动化打分效果：

女生举起酒杯一饮而尽,然后把酒杯摔碎

![](/personal-site-mvp/img/doc-placeholder.svg "")
[附件]
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 三、为什么没有 SFT？
在“物理规则”遵循上，探索了 Qwen2.5-VL 模型的微调尝试（LLamaFactory 微调框架），但是效果并不理想。从我们的实践中，我们也探索了 SFT 需要关注的事项。

## 3.1 基座模型的裁判能力是保障SFT有更好效果的基石
基于视觉模型进行视觉检测的基本流程如右图所示。

因此基于帧序列检测要求 VLM 具备强大的上下文感知和物理知识推理能力，目前看，视觉模型在这一点上还有较大提升空间。

![](/personal-site-mvp/img/doc-placeholder.svg "")
|**测试视频**|**prompt**|**qwen2.5-vl-72b-instruct**|**GPT-4o**|
|-|-|-|-|
|[附件]|请理解视频帧序列内容，视频中物体或人物有变化不合理或不符合物理规律的地方吗？（视频处理方式：视频为每秒抽10帧，将视频以帧图片列表的形式传入）|从提供的视频帧序列来看，视频展示了一个多米诺骨牌的排列和倒塌过程。在这个过程中，没有明显的物体或人物变化不合理或不符合物理规律的地方。具体分析如下：……|这些画面展示了多米诺骨牌逐渐倒下的过程。 \n\n从观察来看，没有明显的不合理或不符合物理规律的地方。开始时，……这些帧图展示了这一现象的典型演示，没有违反物理规律的表现。|

## 3.2 SFT 对数据集的量级有一定要求，同时 SFT 还有可能影响模型的原本的能力
在 SFT 过程中，我们在数据集上进行了多次尝试：

* 数据量级为 100，正负样本比例为 1:1，数据涉及动力学、光学、热力学三大分类的七个子分类，每一类的样本较少，且采用 Lora 方式微调，最终模型微调前后的检测效果基本一致，未有提升。
* 数据量级为千级别，批量生成正样本数据，结合上一步的中的少量负样本，采用 Lora 方式微调，检测效果甚至低于基座模型。

|Qwen2.5-VL-7B|Qwen2.5-VL-7B 微调模型|
|-|-|
|**判断结果**：是。**问题时间段**：2s-7s。**违反的规律**：材料强度极限。**详细说明**：**现象**：在视频2s-7s时间段内，一块白色的物体（看起来像是塑料片）被放在一个由多种颜色积木搭建的结构上。突然，积木结构崩塌，白色物体被弹飞出去。**原理**：根据材料强度极限的原理，物体在受到一定外力时会达到其强度极限而发生破坏。如果物体的强度极限远低于施加的外力，那么物体应表现出明显的形变或断裂，而不会瞬间被弹飞。**矛盾点**：在视频中，白色物体在没有明显形变的情况下被弹飞出去，这与材料强度极限原理相矛盾。按照材料强度极限的原理，如果施加的力远低于材料的强度极限，物体应经历一定的形变或断裂，而不会瞬间被弹飞。|审核结果1. 判断结果否2. 问题时间段无3. 违反的规律无4. 详细说明‌**现象**‌：视频展示了一组彩色多米诺骨牌被手推动后依次倒下的过程。‌**原理**‌：多米诺效应是一种典型的连锁反应现象，当第一块骨牌倒下时，会通过接触传递力给相邻的骨牌，从而引发一系列骨牌依次倒下。‌……‌**结论**‌：视频中的多米诺骨牌倒下过程完全符合真实世界的物理规律，没有发现任何违反物理规律的现象。|

    * 数据量级为千级，即批量生成正样本数据，结合上一步的中的少量负样本，采用全参微调时，模型推理能力下降，答非所问。

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 3.3 对于裁判员模型微调而言，强化推理能力是关键，不能一味灌数据
我们的微调数据集只给出了视频描述和待检测的视频，但是却没有给出从人的视角看，违反物理规律的 CoT 内容。在  [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play? ](https://arxiv.org/abs/2508.10014) 论文中，作者也提到：强化推理是关键，想要打造一个好的“AI裁判”，关键不在于灌输更多的角色知识，而在于提升模型本身强大、稳健、具有上下文感知能力的推理引擎。

```
[{
    "messages": [
      {
        "content": "<video>你是一位物理专家，熟悉各类物理规律。请尽可能详细地理解此视频，并根据帧序列的内容变化分析视频中的物体、场景、动物和摄像机运动，判断其中固体形变是否存在违反真实世界物理规律的现象。\n\n以下是审核时可依据的物理规律及检测要点供参考，但审核时可不拘泥于以下几点： \n1. 材料力学异常：  \n   - 物体在受力时直接粉碎，未经历可见形变（如饼干被碾压瞬间成粉）。  \n   - 断裂方向与外力或材料内部应力分布明显矛盾（如沿非受力方向断裂）。  \n   - 脆性材料破坏后完全恢复原状（违背不可逆形变规律）。  \n\n2. 材料强度异常：  \n   - 远低于材料极限的外力导致物体完全破坏（如手指轻压西瓜瞬间爆裂）。  \n   - 远超材料极限的外力未引发破坏（如轻质物体承受巨大冲击却未破碎）。  \n\n3. 流体与气体异常：  \n   - 气体体积变化时压强未同步调整（如气球极大体积仍可轻松充气）。  \n   - 喷射物质的速度或总量远超物体初始能量或质量（如水果爆裂喷出远超自身体积的液体）。  \n   - 无外力或内部压力时液体/气体高速喷射。  \n\n4. 能量守恒异常：  \n   - 破坏时释放的能量（如声响、碎片动能）远大于外力输入（如轻压西瓜产生巨大声响）。  \n   - 物体在无外力或能量输入时自发形变或破坏。  \n\n5. 质量守恒异常：  \n   - 物体破碎后总质量异常（如碎片消失或新增不明物质）。  \n   - 喷射物质总量超过物体初始质量。  \n\n6. 运动与惯性异常：  \n   - 物体运动方向或速度与受力方向矛盾（如碎片飞出方向与外力方向相反）。  \n   - 无推力时物体加速、减速或改变轨迹（如气球无吹力却持续加速）。  \n\n \n最后，按以下结构输出审核结果：  \n1. 判断结果：是否违反物理规律（是/否）。  \n2. 问题时间段：具体违反现象发生的时间区间（如2s-7s）。  \n3. 违反的规律：对应的核心物理规律名称（如“材料强度极限”）。  \n4. 详细说明：  \n   - 现象：简要描述违反行为（如“轻微外力导致西瓜完全爆裂”）。  \n   - 原理：说明违反的具体物理规律（如“材料强度要求脆性材料需施加至少X N力破坏”）。  \n   - 矛盾点：分析现象与规律的冲突（如“施加的力远低于该值”）",
        "role": "user"
      },
      {
        "content": "1. 判断结果：是\n2. 问题时间段：0s-3s\n3. 违反的规律：材料力学异常、能量守恒异常\n4. 详细说明：\n\n- 现象描述：\n视频中展示了一个液压机对砖块进行压缩的过程。在液压机的压力作用下，砖块迅速被压碎，并且碎片以较高的速度向四周飞散。整个过程看起来非常剧烈，砖块的破坏和碎片的运动显得过于夸张。\n\n- 原理分析：\n\n (1) 材料力学异常\n- 现象：砖块在液压机的压力下直接粉碎，未经历明显的塑性形变或逐步断裂的过程。\n- 原理：根据材料力学，脆性材料（如砖块）在受压时通常会先经历一定的弹性形变和塑性形变，然后才会发生断裂。这种形变过程是由于材料内部应力逐渐积累并超过其极限强度所致。正常情况下，砖块在受到压力时，表面可能会出现裂纹，随后逐步破碎。\n- 矛盾点：视频中的砖块几乎是在瞬间完全粉碎，没有显示出任何可见的形变过程，这与真实世界中脆性材料的破坏行为不符。\n\n (2) 能量守恒异常\n- 现象：砖块破碎后，碎片以极高的速度向四周飞散，动能明显过大。\n- 原理：根据能量守恒定律，液压机施加的能量应等于砖块破碎所需的能量以及碎片获得的动能之和。然而，视频中碎片的飞散速度过高，似乎超过了液压机施加的能量所能解释的范围。\n- 矛盾点：碎片的动能远大于液压机施加的外力所传递的能量，违背了能量守恒定律。",
        "role": "assistant"
      }
    ],
    "videos": [
      "mllm_demo_data/6016db4612ae3a699fd8c9c72bde4b4250bbb8204f2739d318c458fd88cdfb29_error.mp4"
    ]
  }]
```




# 主题三：大模型自动化评测技术-llm as a judge——张文婧
# 一、大模型评测的分类
当前各类大模型层出不穷，含基座模型，领域模型，垂类模型等等；模型评测成为衡量模型能力的重要环节，针对大模型的评测技术也形态各异。每一种评测像一份考卷，验证模型在某个方面的能力表现。尽管评测数据集种类繁多，评测框架和方法也各有不同，但大体上模型的评测可以粗略归纳为以下几类：

* 语言模型评测：针对模型语言推理能力的测评；通过文字问题使模型回答，来评测模型对某类知识的掌握情况。
* 多模态模型评测：针对图像，视频识别或生成能力的测评
* 工具类评测：针对具体场景的模型能力表现，如函数调用；基于现实场景的agent交互；代码生成等需要特殊特定验证环境的场景。

其中语言类评测和多模态类评测会分别使用统一的评测框架；而工具类评测由于场景差异性较大，需要在框架中实现具体场景，会分别使用独立的框架实现。

# 二、大模型评测自动化基本架构
## 2.1 自动化评测功能
大模型评测自动化主要包含以下三个主要环节：

* 数据解析和封装
* 推理并解析结果
* 对推理内容评估，产生最终评估结果

在不同的评测场景和需求下,又新增以下衍生功能:

* 评测场景
    * 同一模型评测多个数据集
    * 多个模型评测同一个数据集
    * 多个模型评测多个数据集

* 推理控制
    * 被测模型配置：endpoint，api-key，think模式。。。
    * 并发数控制
    * 被测模型请求参数调整: max_tokens, temprature, top_p, top_k...

* 评测控制：主要涉及judge-by-llm的模型控制
    * judge模型配置
    * 并发控制
    * 请求参数调整


## 2.2 自动化评测框架构成
### 自动化评测框架
### 用户参数
##### 被测模型参数
##### 裁判员模型参数
##### 数据集参数
##### 用户参数（日志&结果保存地址等）
### 流程控制
##### 多模型控制
循环控制

异常退出控制

##### 多数据集控制
循环控制

异常退出控制

##### 评测维度
pass@k(至少一个解通过测试)

pass^k(全部通过测试)

### 模型
##### API类模型
Qwen系列，gpt系列，ds系列，gpt系列，ernie...

API base 模型

##### 离线模型
Qwen系列，gpt系列，ds系列，gpt系列，ernie...

离线 base 模型

##### 用户自定义模型
在线（endpoint + api_key）

离线(checkpoint + 模型参数)

### 各种类数据集
##### 普通数据集（语言、多模态）
prompt封装

结果评分

结果汇总&结果保存

##### 工具类
模拟现实数据库，工具调用

模拟用户提问

根据数据库终态结果&各步骤推理内容评测

##### 代码类
gitcode拉代码+打镜像

生成patch，运行修改前后代码并获取运行结果

结果评测&汇总

## 2.3 自动化评测介绍
语言类评测框架：OpenCompass

多模态评测框架：VlmEvalKit

工具类评测框架：bfcl（函数调用），tau-bench（场景类agent评测），tau2-bench，swe-bench，aider polyglot



# 三、评测的方法分类-普通数据集
评测的方法按大类主要分为judge-by-rule，以及judge-by-llm；这两种方法的主要区别在于是否使用第三方大模型作为裁判员来评测模型生成结果的正确性。

## 3.1 judge-by-rule
通过预定义规则（如正则表达式、关键词匹配、逻辑校验）判断生成结果的正确性，**不依赖外部模型**，但规则设计需覆盖所有可能情况。

常用评测方法：

* 完全相同：
    * 选择题：此类数据集prompt中一般会包含要求模型只输出选项的指令。

* 正则&关键词匹配&用户自定义规则：一般用于要求固定格式的数据集
    * 特别标记：prompt指令中会包含指定格式的标记，如要求模型生成的答案必须包裹在某些标记中，如<eoe><eoa>。此种评测会匹配标记关键词并提取最终结果；如**GaoKaoMM**
    * 固定答案格式：prompt指令中要求最终答案的格式【answer is 】，通过正则匹配筛选答案。
    * 特殊格式：prompt中要求识别图片中的考题并按照指定得格式生成yaml格式的文本，需要用户自定义yaml解析方法，并实现判分标准。如题目识别正确，选项识别正确，答案识别正确等。

* 语义相似性评测：此种方法由于未调用第三方模型，顾未划分至llm-as-a-judge这一类；常用语对比模型返回及正确的两段文本，也可使用第三方模型评估来替代。
    * **Rouge**：是评估自动文本摘要质量的常用指标，主要有ROUGE-N、ROUGE-L等类型；使用场景有图片描述，含单个词的命中率（多对象元素识别），以及生成文本与正确答案整理匹配情况。如：OpenCQA，Gui2Summary
        * **ROUGE-N**中的N代表n-gram的长度。比如ROUGE-1就是基于unigram（单个词）的匹配，计算预测和参考文本中重叠的unigram数量，然后计算F1分数。
        * **ROUGE-L**中的L代表Longest Common Subsequence（最长公共子序列）。它关注的是预测和参考文本中最长公共子序列的长度，而不是n-gram的精确匹配。这样能更好地捕捉到句子结构的相似性，比如词序的相似，而不仅仅是词的重叠

    * **BLEU: **基于精确率（Precision）衡量机器翻译质量，通过计算生成译文与参考译文的N-gram匹配度评估准确性；BLEU适用于强调翻译准确性的场景（如机器翻译），ROUGE适用于强调信息覆盖率的场景（如文本摘要）。如：CharSumm，MD2T（商业广告生成）

* **特殊评测规则**
    * **grounding：** IoU (Intersection over Union，交并比)
        * IoU = 1 → 完全重叠（最好情况）
        * IoU = 0 → 完全没有重叠（预测失败）
        * IoU 越高，预测越准确。

    * **count: **RA_5%, RA_10%


## 3.2 judge-by-llm
利用第三方大模型（如 GPT-4、Claude、 文心、 deepseek）作为“裁判”，判断模型生成结果与正确结果的相似性，**更灵活但成本较高**。主要适用于非唯一性答案且很难通过规则或简单的语言类相似性评测方法的情况。

常用评测方法：

### 3.2.1 预测&标准答案
向judge model传入预测&标准答案，使其判断正确与否。数据集：PlotQA

```
index                                                       0
image       iVBORw0KGgoAAAANSUhEUgAABNkAAAKKCAYAAAAA4o2EAA...
question     How many different coloured dotlines are there ?
answer                                                      2
Name: 0, dtype: object
question
How many different coloured dotlines are there ?
answer
2
index                                                       1
image       iVBORw0KGgoAAAANSUhEUgAABNkAAAKKCAYAAAAA4o2EAA...
question    Is the number of dotlines equal to the number ...
answer                                                    Yes
Name: 1, dtype: object
question
Is the number of dotlines equal to the number of legend labels ?
answer
Yes
index                                                       2
image       iVBORw0KGgoAAAANSUhEUgAABNkAAAKKCAYAAAAA4o2EAA...
question    What is the employment to population ratio(mal...
answer                                                   48.0
```
```
prompt = ("You are a judge, please score according to my answer and "
                  "prediction. If the answer and prediction are consistent, "
                  "return yes, otherwise return no. Just return yes or no, without any other extra words.The answer "
                  f"is {answer}. The output is {prediction}")
```
### 3.2.2 问题+预测+标准答案
向judge model传入问题+预测+标准答案，使其判断正确与否。一般用于比较复杂的答案判断。如以下数据集

[https://arxiv.org/pdf/2502.20808](https://arxiv.org/pdf/2502.20808)

该数据集包含多选，单步自由计算，多步骤自由计算。

其中三种题目均使用来判断最终答案是否正确

***为多步骤问题设计了两个评估指标：步骤准确率（SAR）和问题完成率（QCR）。SAR是指正确回答的步骤占总步骤的比例，而QCR是所有步骤都正确回答的问题的比例。

```
problem_id                                                     3
image          /9j/2wCEAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHR...
question       As shown in the figure, if a plane cuts the le...
answer                                                         D
answer_type                                               choice
subject                                           Solid Geometry
Name: 2, dtype: object
question
As shown in the figure, if a plane cuts the left cone, which of the following cross-sections is impossible to obtain?  [IMAGE_1] A.  [IMAGE_2] B.  [IMAGE_3] C.  [IMAGE_4] D.  [IMAGE_5]  ##
answer
D
answer_type 列的取值范围:
['choice' 'single-step' 'multi-step']
```
```
        prompt_format = """
    You have to answer whether the solution is correct or not.
    ---
    PROBLEM STATEMENT:
    {}

    CORRECT ANSWER:
    {}

    SOLUTION TO EVALUATE:
    {}
    ---
    Now please compare the answer obtained in the solution with the provided correct answer to evaluate whether the solution is correct or not.

    Think step-by-step, following these steps, don't skip any:
    1. Extract the answer from the provided solution
    2. Make any derivations or transformations that may be necessary to compare the provided correct answer with the extracted answer
    3. Perform the comparison
    4. Conclude with your final verdict — put either "Yes" or "No" on a separate line"""

```
**MV-MATH评测结果：**

[附件]
**K9-MATH：百度自研数据集**

```
    prompt = """请你作为一个测评专家，判断下面的答案是否与标准答案一致，即考生是否回答正确。下面是一些评判标准：
1. 有些答案可能包含多项内容，可能有单选题，多选题，填空题和问答题，只要答案与标准答案一致即可。
2. 有些答案可能通过不同的方式表达，比如有些答案可能是一个数学表达式，有些答案可能是一个文字描述，只要表达的意思一致即可。且有些公式通过不同的方式表达，但等价，也是正确的。
3. 你不需要重新计算问题答案，因为标准答案已经给出，只需要根据问题形式来判断考生的答案是否与标准答案一致，是否正确即可。
4. 数字类答案误差不超过10^(-2)视为一致。
你根据上述标准，判断下面的答案是否与标准答案一致，如果一致，请在最后输出“正确”,否则输出“错误”,如果难以判断，请输出“错误”.
原问题：%s
标准答案：%s
考生答案：%s
判断结果：
""" % (problem, answer, predict)
```
**模型生成：**

```
我们来看这道题目：
题目给出的方程是 $ax + y = 2$，并且已知一个解是：
$\begin{cases}x = 4 \\y = -6\end{cases}$
要求我们求出 $a$ 的值。
将已知的解代入方程：
将 $x = 4$ 和 $y = -6$ 代入原方程 $ax + y = 2$，
得到：$4a + (-6) = 2$。
简化方程：
将方程 $4a - 6 = 2$ 进行简化。
首先，将 $-6$ 移到等号的另一边：
$4a = 2 + 6$。
继续简化：
$4a = 8$。
求解 $a$：
将方程两边同时除以 4：
$a = \frac{8}{4} = 2$。
所以，$a$ 的值为 2。
知识点涉及：
方程的解的代入：这道题目主要考察了如何将已知的解代入方程中进行验证或求解其他未知数。
代数运算：涉及了基本的代数运算，如加法、减法、乘法和除法。
常见错误思路或误区：
代入错误：学生可能会在代入过程中出错，例如将 $x$ 和 $y$ 的值代错位置。
运算错误：在简化方程时，学生可能会在加减运算或除法运算中出错，导致最终答案错误。
通过以上步骤，我们可以清晰地理解题目并得出正确答案。
```
**标准答案：**

```
**答案**：D
**解析**：已知关于$x,y$的方程$ax+y=2$的一个解是$\left\{\begin{matrix}x=4,\\y=-6,\end{matrix}\right.$，
将$x=4,y=-6$代入方程$ax+y=2$中，得到：
$4a-6=2$
移项得：
$4a=2+6$
$4a=8$
系数化为$1$得：
$a=2$
所以，正确答案是D。
```
通过大模型评测后可以得到正确的精度

![](/personal-site-mvp/img/doc-placeholder.svg "")
**第二题:**

|预测答案|标准答案|评测结果|
|-|-|-|
|本题可根据平角的度数以及四边形内角和的性质来分别求出\(\angle1\)和\(\angle2\)的度数。

### 步骤一：求\(\angle2\)的度数
观察图形可知，\(\angle2\)与\(125^{\circ}\)的角组成一个平角，因为平角的度数为\(180^{\circ}\)，所以\(\angle2\)的度数为：
\(\angle2 = 180^{\circ} - 125^{\circ} = 55^{\circ}\)
 
### 步骤二：求\(\angle1\)的度数
根据四边形内角和是\(360^{\circ}\)，在该四边形中，已知其中三个角分别为\(60^{\circ}\)、\(90^{\circ}\)（直角的度数为\(90^{\circ}\)）、\(\angle2 = 55^{\circ}\)，设\(\angle1\)的度数为\(x\)，则可列出方程：
\(x + 60^{\circ} + 90^{\circ} + 55^{\circ} = 360^{\circ}\)
求解上述方程：
\[
\begin{align*}
x&=360^{\circ} - 60^{\circ} - 90^{\circ} - 55^{\circ}\\
&=300^{\circ} - 90^{\circ} - 55^{\circ}\\
&=210^{\circ} - 55^{\circ}\\
&= 75^{\circ}
\end{align*}
\]
即\(\angle1 = 75^{\circ}\)。

综上，\(\angle1\)的度数是\(75^{\circ}\)，\(\angle2\)的度数是\(55^{\circ}\)。|∠1 = 65°，∠2 = 55°|0|

### 3.2.3 问题+经过提炼后的预测+标准答案
向judge model传入问题+经过提炼后的预测+标准答案，使其判断正确与否。适用于较复杂的推理,需要模型给出中间过程的计算步骤

如MathVerse，HLE

1 .HLE包含以下两种类型的题目

**精确匹配题**‌（模型需输出与标准答案完全一致的字符串）

**多选题**‌（模型需从五个或更多选项中选出正确答案）

```
            if answer_type == "exactMatch":
                prompt = (f"{prompt} \n"
                f"Your response should be in the following format:"
                f"Explanation: {{your explanation for your final answer}}"
                f"Exact Answer: {{your succinct, final answer}}"
                f"Confidence: {{your confidence score between 0% and 100% for your answer}}")
            elif answer_type == "multipleChoice":
                prompt = (f"{prompt} \n"
                f"Your response should be in the following format:"
                f"Explanation: {{your explanation for your answer choice}}"
                f"Answer: {{your chosen answer}}"
                f"Confidence: {{your confidence score between 0% and 100% for your answer}}")

```
```
    def extract_answer(self, answer, answer_type):
        """
        """
        if answer_type == "exactMatch":
            start_mark = "Exact Answer:"
            end_mark = "Confidence:"
            
        elif answer_type == "multipleChoice":
            start_mark = "Answer:"
            end_mark = "Confidence:"
        answer_extract = answer
        answer_start = answer.find(start_mark)
        answer_end = answer.find(end_mark)
        if answer_end > answer_start and answer_start >= 0:
            answer_extract = answer[answer_start:answer_end]
        elif answer_end < 0 and answer_start >= 0:
            answer_extract = answer[answer_start:]
        return answer_extract

    def eval_prompt(self, problem, answer, predict):
        """
        """
        prompt_template =  """Judge whether the following [response] to [question] is correct or not
based on the precise and unambiguous [correct_answer] below.
[question]: { %s }
[response]: { %s }
Your judgement must be in the format and criteria specified below:
extracted_final_answer: The final exact answer extracted from the
[response]. Put the extracted answer as ’None’ if there is no exact, final
answer to extract from the response.
[correct_answer]: { %s }
reasoning: Explain why the extracted_final_answer is correct or incorrect
based on [correct_answer], focusing only on if there are meaningful
differences between [correct_answer] and the extracted_final_answer. Do
not comment on any background to the problem, do not attempt to solve
the problem, do not argue for any answer different than
[correct_answer], focus only on whether the answers match.
correct: Answer ’yes’ if extracted_final_answer matches the
[correct_answer] given above, or is within a small margin of error for
numerical problems. Answer ’no’ otherwise, i.e. if there if there is any
inconsistency, ambiguity, non-equivalency, or if the extracted answer is
incorrect.
confidence: The extracted confidence score between 0 and 100 from
[response]. Put 100 if there is no confidence score available.
""" % (problem, predict, answer)
        return prompt_template
```
具体效果：

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 
# 主题四：Comate Stack自动评估方案——陈耀宗
# 一、Comate Stack是什么？
# Comate Stack
是面向百度集团用户打造的**AI原生研发工具集产品**，支持对AI原生研发新要素（Prompt、数据等）的全生命周期追踪和管理，一站式提升AI原生研发的Prompt工程、数据工程和效果评估等重点场景研发效率。

**平台地址：**[https://console.cloud.baidu-int.com/comatestack](https://console.cloud.baidu-int.com/comatestack)



[流程图]
# 二、Comate Stack自动化评估的一些方案
##### **可点击**[Comate Stack能力中心](https://console.cloud.baidu-int.com/comatestack/lab)**，快速体验相关能力**
### 评估的基础能力
* **评估流程****：**“推理-评估-审核-验收”阶段可以自由选择。支持多人协作、多模型对比、任务分配与管理、盲评、抽样等等
* **评估对象****：**注册模型、稳定的海外模型等
* **评估集****：**我们提供一些开源数据集，也有很多生产数据的方案
* **评估报告****：**针对报告做（BI）分析等

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 一些完备的自动评估策略
* **已经接入不少自动评估策略****：**自然语言评估、语音、数字人、图像等，可以直接使用
* **裁判员模型评估****：**自己写Prompt，选择裁判员模型，也可以实现评估

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 自己来生成策略
**根据样本数据，即可生成自动评估策略**

![](/personal-site-mvp/img/doc-placeholder.svg "")
|query|response|response_accuracy|response_creative|response_clarity|notes_response_accuracy|notes_response_creative|notes_response_clarity|
|-|-|-|-|-|-|-|-|
|||打分维度1|打分维度2|打分维度3|维度1打分备注|维度2打分备注|维度3打分备注|
|解释什么是暗物质？|暗物质是一种不发光也不吸收光的物质，通过引力间接观察到它的存在。|2|1|2|科学准确，反映主流观点|无特别新颖之处|语言简洁明了|
|编一个关于时空门的童话故事|从森林中一扇发光的门里，孩子们进入了彩色的时间隧道。|1|2|1|幻想成分多，略离现实|构思独特，具童趣|部分表达不够顺畅|

### benchmark评估场景
* **利用平台快速进行benchmark评估****：**前期接入MMLU、MMMU、GPQA等benchmark，后期考虑接入SWE-bench等Agent相关的benchmark
* **基础设施支持****：**正在建设研发Agent的通用基础设施，提供稳定支撑生产级Agent运行的环境能力，包括但不限于各类Agent运行沙箱环境、运行时管理、Agent运行所需镜像等，能够支撑Agent的系列评估工作

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 更AI的方式来做评估*  *
* **我们的评估Agent准备上线****：**通过对话，就可以创建评估策略、评估任务，降低你理解我们能力、策略的门槛
* **智能AI表格来做评估：**线上的智能表格，可以通过需求生成Prompt或者代码，完成数据处理，在表格进行评估，也许能更加自由

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 三、一个使用方案
* 场景描述：业务侧在评估新模型时，仅有少量样例数据，手动配置评估维度与策略耗时长、难度高，希望借助平台智能能力快速生成评估策略并发起任务。
* 平台能力：支持上传样例数据自动生成评估维度与打分规则，平台智能识别内容特征，自动构建评估策略，用户可一键应用该策略发起评估任务，显著提升评估配置效率与准确性。

[附件]
[附件]
# 四、怎样联系我们
我们建设了能力中心、数据集广场、Prompt广场等，大家可以自己上传数据，供所有人使用  🫱 [点击快速体验](https://console.cloud.baidu-int.com/comatestack/lab)

如果你有任何需求，无论是想将优质的策略能力在平台露出，助力更多厂内业务使用，还是有任何AI原生研发流程上的诉求，都可以联系我们！

|**用户群**|**服务号**|
|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|产品：陈耀宗 chenyaozong、苏琳 sulin01研发：数据工程：王文进 wangwenjin01效果评估：黄一鹤 huangyihePrompt相关：张兆鑫 zhangzhaoxin01||

# 总结
本期圆桌会，从大语言模型选型与业务迭代中的自动化评测实践，到视频生成大模型高效评估体系的构建，再到多模态与工具类评测的系统化分类与架构演进，大模型自动化评估已从“单点能力验证”全面迈向“系统化、可解释、业务驱动”的智能评测新阶段。面对生成式内容复杂度提升、人工评估一致性难保障等挑战，唯有建立兼具自动化能力与人类感知的评估范式，大模型才能真正成为“可信、可靠、可交付”的生产力引擎。

创新之路，需聚众智。我们期待与各方同学继续务实共创，持续进化评估体系，赋能AI原生应用落地生花。

# 💗有奖互动💗
即日起至10月10日18:00，评论区留言互动：

###### 1、关于自动化评测，聊一聊你所在业务的实践～
######  2、围绕数据工程/评估主题，你还期待讨论哪些更聚焦的话题？
我们将挑选5个走心评论，特别送上**【蜜蜂小狗挂件】**～

![](/personal-site-mvp/img/doc-placeholder.svg "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
