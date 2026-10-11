---
title: "🎁 有奖互动 🎁"
description: "广告相关性标注基于Comate Stack提效实践"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\广告相关性标注基于Comate Stack提效实践.md"
---
广告相关性标注基于Comate Stack提效实践

#### 🧑‍🏫 案例作者：[@叶玮彬](https://ku.baidu-int.com?t=mention&mt=contact&id=9f858680-fcdf-11f0-ae65-fd039460c37e)
#### 🎬 案例场景：评估
#### 🔧 使用工具：Comate Stack, iEValue
#### 📒 案例概要：本文分享广告相关性标注基于Comate Stack的提效实践。针对广告物料推荐场景，通过Comate Stack实现研发-发布-评估一体化：打通Jarvis-iEValue通路，支持小时级数据回流与自动化评估；利用在线Prompt调试、LLM自动评估（相关性达80%以上）及人工标注协同，将评估时长缩减75%。实践推动推词相关性提升6-11pp，账户召回率从38%升至85%，验证了AI原生工具在策略迭代与效果优化中的关键价值。
## 一、广告物料智能推荐业务介绍
随着人工智能技术的飞速发展，我们已全面进入AI原生时代。在广告投放领域，这一变革尤为明显，基于大模型的广告物料推荐大幅提升了投放的效率和效果，广告主在AI能力的加持下能够更简单地搭建和优化账户。

在广告投放环节中，广告主通常需要大量买词来扩流量，大量制作创意来吸引点击，并通过地域、意图、卖点等方式对词和创意进行组合，持续调优投放效果，整个过程耗费精力，且投放效果受广告主经验制约，参差不齐。

百度营销平台为广告主提供一站式投放服务，在广告物料推荐方向，主要聚焦在关键词推荐和创意推荐两大高频场景。在AI精准理解客户业务（行业、类目、卖点等）的基础上，结合大模型、词库等，向广告主推荐相关热词、吸睛创意。例如，从广告主落地页中提取内容并总结推广业务为“镀锌管租赁”，便可衍生出“租赁镀锌钢管多少钱一米”、“镀锌钢管租赁费用”等关键词，精准匹配用户流量。

![广告投放平台 - 关键词推荐](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=485e54806a314609b96a6418495fb441&docGuid=PfMsu32_rgkw0b "广告投放平台 - 关键词推荐")
![广告投放平台 - 创意文案推荐](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2f09b24dbb2e4ccfa335e5804eb18b7f&docGuid=PfMsu32_rgkw0b "广告投放平台 - 创意文案推荐")
![广告投放平台 - 创意图片推荐](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=54779a4da39d42dabee83aa714ec698c&docGuid=PfMsu32_rgkw0b "广告投放平台 - 创意图片推荐")


## 二、广告物料智能推荐的原理和挑战
#### 1. 广告物料推荐的执行过程
广告物料智能推荐系统从接收信号到触达广告主，中间经历数个核心环节。简化来看，首先要准确理解广告主的信号，这里既包含历史信号（买词、创意、落地页），也包含即时的客户表达（指定种子词、意图、词性等）；其次，预加载词库，根据信号指定触发各类策略，多路召回；最后，对一批词进行排序、过滤、分组，生成最终推荐物料。同时，定期采集推荐数据，人工标注相关性，再跟物料采纳的埋点日志做归因分析，并将标注数据反哺策略中的模型精调。整个过程涉及到对大模型的各项使用，是典型的AI应用场景。

![广告物料智能推荐执行流程简图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3aea1bdb36604054928b632bdfd7efed&docGuid=PfMsu32_rgkw0b "广告物料智能推荐执行流程简图")
其中，最关键的是召回策略，通常有数十种策略分支在生产环境同时运行，起到策略互补和实验比对的作用。以关键词推荐为例，典型的策略分支包括：

* **根据语义相似度召回：**根据大搜Query存储搜索词库，计算Embedding并构建BaikalDB向量索引，在业务信号识别种子词后，计算余弦相似度，并设定召回阈值。
* **基于竞品词库召回：**构建竞品词库，并通过预设的业务规则（如行业、预算规模、地域）圈选合适的一批竞对账户，再从竞品词库中召回相应的关键词。
* **大模型端到端生成：**把所有信号和评分标准构建Prompt输入给大模型，由大模型自由生成关键词，约束较少，结果更具多样性。

#### 2. 广告物料推荐的效果评估方法
面对多种策略分支的并行迭代，必须定期更新汰换、合理配比权重，才能达成最佳的采纳率。经分析，广告主采纳行为与推荐相关性、丰富度密切相关，以关键词为例，经过前期的调研、人工标注、数据分析，我们初步将词与业务的相关性划分为「强相关、中相关、低相关、不相关」四个档位，完整定义如下：

* **强相关：**完全匹配，也可以是同义、简称、缩写、英文表达，或者是子类产品。
* **中相关：**相关但非精确，是强相关品类，或者关键词指向核心产品的大类。
* **低相关：**功能类似但产品/服务不同，或者是上下游产品、配件等。
* **不相关：**完全不相关，两个产品之间基本没有关联。

下面以「屋面防水补漏服务」业务为例，介绍各种档位的推荐关键词差异。在生产环境中，不相关词将作为badcase拦截，强相关词通常能实现高转化，但竞价也更激烈，而中/低相关词则作为补流量的手段，三个档位组合推荐。

|**业务**|**档位**|**关键词**|
|-|-|-|
|屋面防水补漏服务|强相关|**屋顶补漏注胶**一般怎么收费、高层**屋面防水补漏**、楼顶**漏水防水补漏、屋顶防水**师傅|
||中相关|**防水补漏**专业施工公司、维修**渗水补漏**、**彩钢瓦漏水**维修、做**防水**电话号码、**防水补漏检测**|
||低相关|**卫生间防水补漏**多少钱、**热水器漏水补漏**维修、**管道防水补漏**、楼顶**补漏防水胶**哪个牌子好|
||不相关|铺房顶、房顶维修、专业清洗外墙服务|

#### 3. AI原生研发与评估遇到的挑战
综上可以看出，围绕物料相关性提升的优化和评估是业务的关键数据飞轮。然而，起初各策略研发组设定了不同的评估流程，导致效果难以横向比较，各分支之间的Prompt管理分散，评估流程复杂冗余，且数据分散无法沉淀，限制了进一步精调模型的效果。我们总结其中的两大挑战：

* **AI原生研发范式统一的挑战**
    * **部署效率问题：**线上服务为Java技术栈，发布较为低频，而Prompt迭代更高频，需解耦并独立开发部署上线；
    * **Prompt管理割裂：**需要统一版本管理、可视化管理、模板化管理，能够与Java生产环境联动；
    * **埋点与数据集管理：**涉及核心的召回、过滤、采纳全链路埋点，分支、行业等10+维度，需要沉淀为数据集。

* **多场景评估流程提效的挑战**
    * **验证型评估：**对于「创意文案推荐」等新场景，需要前置调研评估，测试不同模型、Prompt差异，验证效果；
    * **生产数据自动评估：**线上分支的效果比对，需随机取样真实数据，依靠大模型做相关性评估，监测异常；
    * **定期并行多人评估：**定期由标注团队人工评估，发现Corner Case，同时更新系统评估Prompt，支撑新一轮迭代。




## 三、基于Comate Stack提效的实践
根据对ComateStack的拓展能力调研，结合商业广告平台部的技术栈现状（生产环境大部分是Java/Spring应用，微服务均托管在Jarivs平台），Comate Stack当中的Prompt研发托管/集成、数据回流、例行数据生产、在线评估/调优等能力完全匹配业务诉求，我们决定围绕Comate Stack实现AI原生研发与评估的全过程托管。

#### 1. AI原生研发托管的实践
考虑到前期的基础技术积累，Jarvis与iEValue已打通发布-部署环节，自研Java AI原生基础库TinderSDK/Tinder Starter支持加载iEValue Prompt模板，在Java微服务应用中只需一次简单集成，后续即可在Comate Stack平台上迭代Prompt，无需硬编码，很好解决了广告物料推荐场景的部署效率、Prompt管理割裂问题。

这里再展开分享下数据集管理的方案，我们根据基于iEValue-Jarvis-K8s-Minos-AFS-iEValue的通路完成了从Prompt发布到数据回流的全过程，实现了小时级收集生产环境真实数据，并触发自动化评估，这种工程串联大幅节省人力，且保证了采样的随机性、可靠性，步骤如下。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8f233aed18934f68895f5e45864eef11&docGuid=PfMsu32_rgkw0b "")
* **数据埋点：**对每次触发推荐pv的所有bidword埋点，字段包含每个bidword对应的词源分支、原始种子词、行业、过滤标识等信息，日志存储于EKS实例。
* **数据回流形成数据集：**通过Minos拉取EKS实例的日志传输至AFS，Comate Stack数据回流支持小时级采集AFS数据，形成数据集，以可视化的方式管理。
* **配置数据生产工作流：**平台提供20+预置算子，Comate Stack工作流支持编排算子，我们通过行列筛选算子对多分支随机取样，通过分组算子分配标注人。
* **生成评估任务：**工作流运行后即可自动生成评估任务，配置例行任务后，广告物料相关性实现了系统自动评估，以及定期按需的并行多人评估。

![数据回流形成数据集](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3b5d325495184ac992a5019adc6d9e8e&docGuid=PfMsu32_rgkw0b "数据回流形成数据集")
![数据生产工作流](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5f668dd07a824a92957aab3c28b314fb&docGuid=PfMsu32_rgkw0b "数据生产工作流")
![工作流运行生成评估任务](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=644c636957e74eee8b63747639c306f6&docGuid=PfMsu32_rgkw0b "工作流运行生成评估任务")


#### 2. Prompt评估提效的实践
在最大化解决工程通路的问题后，还需by场景考虑Prompt的提效问题，基于Comate Stack的强大能力，我们的三类场景均得到最大化提效。

* **快速验证：**基于Comate Stack的托管和在线开发、调试的能力，可以自由切换模型、修改Prompt，修改temperature、top-p等参数，便于快速验证。
* **系统自动评估：**对于标准明确且允许一定误差的场景，往往通过LLM自动评估效果更高。利用Comate Stack批量评估并可视化观察结果，在广告物料相关性场景下，后期相关性已经稳定达到80%以上，此时可快速筛选出不相关的Case重点分析原因，避免把时间花在重复的标注上。
* **人工标注相关性：**标注任务以答题卡形式分发，附带关键的创意标题、落地页url等关键信息，标注人根据落地页判断广告主所做生意，结合种子词、创意标题、账户结构，综合判断推荐词的相关程度，并根据前文提到的四档打分。

![Prompt快速验证型评估](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3fa35aff56b54062930fd00e900c25c7&docGuid=PfMsu32_rgkw0b "Prompt快速验证型评估")
![系统批量评估广告物料相关性](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=da9beb14cff64975983b5cbf9991fd23&docGuid=PfMsu32_rgkw0b "系统批量评估广告物料相关性")
![人工标注广告物料相关性](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4334b45060004062b583916e389f3978&docGuid=PfMsu32_rgkw0b "人工标注广告物料相关性")
Comate Stack还能够支持下载最终的评估文件，进行本地的二次分析。如下所示，我们将评估的输入和输出平铺，可以看出种子词衍生推荐词字面，与业务类目、行业、账户结构、向量相似度的整体关联度，对于badcase可以进一步分析原因，帮助我们更好地迭代Prompt、作为优质标注预料SFT精调专用小模型。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5da617441c4f435db2231160288f5074&docGuid=PfMsu32_rgkw0b "")


## 四、总结与思考
广告物料推荐系统经过上述项目实践，实现了研发-发布-评估一体化，评价体系标准化。策略迭代效率大幅提升，采样方式从人工线下采样（0.5pd/）转变为生产环境零成本真实数据随机采样，基于评估标准和iEValue工具实现并行评估，每轮标注时长平均缩减约75%，基于Jarivs-iEValue工具实现Prompt打通与独立发布，最快小时级迭代上线。围绕「相关性」指标的数据飞轮快速运转，仅一个季度，各场景的推词相关性提升6pp~11pp不等，主流程场景推词账户召回率从38%提升至85%，采纳消费覆盖提升75%，因策略优化带来的关键词榜单等产品体验提升广受好评。

回顾项目发展，我们从中得到相应启示。生成式AI时代，模型应用和策略的门槛降低，不同技术背景的研发都可以借助大模型参与业务策略调优，但工程能力仍然不容忽视，只有拥抱AI原生新工具，响应TSC号召，结合业务正确选型，积极对接类似ComateStack这样的AI原生研发平台，工程和策略并举，才能达到研发效率和业务效果的双提升，“慢就是快”，为了短期追逐“快”而降低工程化投入并不可取。

展望未来，生成式AI的智能性、多模态能力还在肉眼可见地不断增强，以视频生成模型为例，业界诸如可灵AI、海螺AI，厂内的MuseSteamer频繁升级，正在不断拓展新的能力边界，这为广告物料推荐提供了更多可能性，我们将继续以AI原生工程能力为基础，持续探索AI赋能的新场景。以上是商业平台广告部研发团队的一些经验分享与思考，欢迎大家一起交流。









# 🎁 有奖互动 🎁
**💡 本文对你有帮助吗？**

**欢迎 点赞👍 + 留言💬，分享你的思考或实践经验**

**我们将从评论区随机抽取5位同学送出定制小礼品🎁，一起推动社区成长！🚀**

**「获奖名单将于9月19日公布」**



恭喜[@罗刚](https://ku.baidu-int.com?t=mention&mt=contact&id=a1f45100-94ff-11f0-a111-97e84b3c7f76)[@王奕智](https://ku.baidu-int.com?t=mention&mt=contact&id=a6f60e00-94ff-11f0-a111-97e84b3c7f76)获得**蛇年钥匙扣**一个！

后续会有同学通过如流联系领奖~❤





# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转

