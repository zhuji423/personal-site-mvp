---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "如何拓宽 Agent 的能力边界"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\如何拓宽 Agent 的能力边界.md"
---
如何拓宽 Agent 的能力边界

#### 🧑‍🏫 案例作者：[@陈泽](https://ku.baidu-int.com?t=mention&mt=contact&id=9518fe90-fcec-11f0-828d-79cda80a7f4a)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文讨论了如何明确并拓展Agent的能力边界，包括决定Agent能完成什么任务、不能完成什么任务，以及如何控制任务执行。强调理解代码库的重要性，建议通过Rules补齐模型对代码库的认知。实践案例展示了如何利用Agent治理知识集类型定义，通过分阶段实施和反思优化，确保任务按预期执行，并总结了有效提升Agent能力的策略和反模式。
## 背景
在 Q4 用 Agent 来完成需求时，我给自己的一个目标，是让大家真正熟悉 **Agent 的能力边界**——也就是三件事：

1. **什么能做**：决定了你能不能用 *AI-first* 的方式来思考问题，并在一开始就最大程度减少「任务失控」带来的沉没成本。
2. **什么做不了**：决定了你会如何在第 1 条的前提下，把任务拆分成 Agent 真正有可能完成的子任务。
3. **可以控制什么**：决定了当模型「跑偏」时，你还可以通过哪些手段，把 Agent 的任务规划拉回正轨。

这三件事合在一起决定了「**我们大概能委托 Agent 做多大的任务」**

社区里通常会用「人类专家需要的时间」来粗略衡量任务的大小。比如：

> 如果一个任务由专业人士来做，大概要 1 小时，而 Agent 也能以 X% 的成功率完成，那我们就可以把这个 Agent 的能力描述为「具备执行 *一小时任务* 的水平」。
![前沿通用模型的 50% 成功率大约在 50 分钟左右](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c429029380254eeab2d2846a9f757389&docGuid=uEaB9QbwewBNYi "前沿通用模型的 50% 成功率大约在 50 分钟左右")
在一个设计得比较完善的 Prompt 之下，这个「可委托的任务时长」会显著拉长；而当前大多数工程师的实际使用水平，大概还停留在 **「五分钟任务」** 左右。

我在观察其他同学的 Agent 使用示例时发现，**只要和编码沾边，大家往往都会依赖 **`#文件`** 能力**：通过一个入口文件，让 Agent 去读取并修改一个或多个文件。
但我通常不会推荐这么使用，从长远来看，一个二十分钟以下的任务，未来一定是交给 Background Agent 去并行完成的，甚至一个需求可能跑多个实现，最终 Review 取其中的一个或者合并。所以要多去探索「**在不依赖 **`#文件`** 的情况下，如何提示和驱动 Agent 完成任务**」的各种技巧。



## 理解代码库
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9e88d8261c754698b465f876f0fa1d13&docGuid=uEaB9QbwewBNYi "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ffcee4cefdd24babaa6b896e3153e4c3&docGuid=uEaB9QbwewBNYi "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f78981dfad6a4fa8a7d8c5eaea0c92cd&docGuid=uEaB9QbwewBNYi "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f7da30450c68444b81c90f2a69c2ed09&docGuid=uEaB9QbwewBNYi "")
在让 Agent 真正参与编码之前，有一个经常被忽略的前提：**先让它“理解”你的代码库**。这里面至少有几层现实要先想清楚：

1. **功能不是线性加法，复杂度是会“叉出去”的**
产研以外的同学，往往会直觉地认为：产品功能是做一块、加一块，整体复杂度就线性增长。但实际情况是，**模块复杂度往往会在某个时间点“岔出来”**：

    * 早期改动像是在做加法；
    * 到了某个规模之后，一次改动会牵扯到更多模块和耦合关系，复杂度更像是在做乘法。

2. **模块划分通常有“横纵”两套视角，**这两种视角通常是叠加存在的，而不是二选一

    * **按业务横向切分**：按功能域/业务域拆分模块，比如「用户」「交易」「工单」等；
    * **按架构纵向切分**：按技术分层拆，比如「接口层」「领域层」「基础设施层」。

3. 以整车制造为例，我们肯定不会指望「一次性 3D 打印出一辆完整的车」。正常做法一定是拆成若干子系统：**动力总成、底盘、车身、电气……**用 Agent 写代码也一样：

    * 不要一上来就让它「从无到有搞定一个大功能」；
    * 更合理的方式是按模块/子系统拆分，让 Agent 逐步在已有结构里补全或调整，而不是“平地起高楼”。

4. 多包架构下，公共模块改动一定会“外溢”，怎么保证所有依赖它的模块还能正常工作？

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=11ddfb928a8949fa807365b05e472d9e&docGuid=uEaB9QbwewBNYi "")
**在这个阶段，我们需要通过 Rules 去补齐模型对代码库的“世界观”。**

我会把 Rules 分成两类

1. 架构风格、概念类：通常用来描述有什么
2. 功能指导类：一个功能具体要按什么流程去实现，涉及哪些模块



## 实践-飞轮
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b151d1f17ef64626be34444e519d2ed6&docGuid=GrATX24gbJ9F-B "")
这个需求的背景是实现了一个知识集相关的工具能力拓展，但是里面有几个比较严重的问题

1. 知识集复用了一些知识的接口，类型定义模糊不清，比如一个实体写了20个字段，但有可能就返回了5个
2. 类型之间存在一些无意义的关联，比如下面的示例，你即捋不清`KnowledgeList`什么时候是准确的，也不应该关联一个不知道哪来的类型

```
interface KnowledgeList {
    type: KnowledgeSet['type']
}
```
3. 类型名称存在二义性，`KnowledgeList`既可以当做知识集，也可以当前输入框上下文
4. 类型存储方式不友好，维护在`chat.ts`里，这个文件超过 700 行，里面有很多其它无关业务的类型，对模型读取不太友好
5. Kernel 与 Webview 虽然有通信，但没有共享类型，即使共享了也是错的

**所以，我希望拿 Agent 帮我来治理一下这件事，但其实大概率我自己是不愿意做这件事情的。**

1. 先描述完想要的目标，「**我最终想要一个干净且独立的知识集类型定义文件**」

    * 在 packages/shared-internals/src/bridge/ 里创建 knowledge.ts 文件，并实现共用的类型，添加完需要再 shared-internals 目录下执行build
    * 检索所有和上述接口相关的 Knowledge 定义，替换成新的

2. 一些前置的可以减少任务跑偏的输入，我知道它会检索很多东西，但这些我可以做约束，用关键词描述即可

    * 所有knowledge相关的接口放在以下两个文件，你可以通过 curl 来获取其类型，我会给你一些必要的参数
        * packages/kernel/src/service/AgentConversation/Zulu/api/knowledge.ts
        * packages/kernel/src/service/AgentConversation/Knowledge/index.ts


3. 给它一个可以**确认事实**的方式，即哪里是最准确的信息来源。增加了一个 run_command 的工具用来获取接口信息，类型保证和跑的接口里的一致，剥离一些外置的信息干扰。同时要求它用 subagent 来完成。

    * 使用 Actor subagent 来使用curl命令完成类型查询，必须带上鉴权的header, 域名是测试环境，比如 validate 接口调用示例如下：

```
curl 'https://comate-external-dev.now.baidu-int.com/api/aidevops/autocomate/rest/autowork/v1/knowledge/validate' \
-X POST \
-H 'login-name: *' \
-H 'Uuap-login-name: *' \
-H 'plugin-version: VsCode-3.21.0' \
-H 'host: comate-external-dev.now.baidu-int.com' \
-H 'Content-Type: application/json' \
--data-raw '{"workspaceIds":[],"knowledgeIds":["16297406-0b32-408a-8d7c-3739b00adb53"]}'
```
4. 最后加反思`在根目录执行 npm run build 确保没有类型错误`

**第二个步骤是：可以看到它大概是能跑出一些东西来的，需要我们能观察其中出错的部分，然后加入 Query 里重新执行。我通常会习惯 Revert 掉，用新 Query 重跑。**

    * 不需要单独定义用户的类型，用不到，比如 createdUser 这种
    * Respone 的类型复用 kernel 里的  Res, 不需要额外定义
    * 参数定义在靠近 API 的地方，不要定义在 shared-internals
    * 简单参数不用定义 interface, 直接写在 axios 泛型里就行

**第三个步骤是：根据这次涉及的变更总结成 Rules，因为由人确认过的信息是很宝贵的，这类属于领域知识 Rules**

[https://console.cloud.baidu-int.com/comatestack/share/3423?token=80bb6be3](https://console.cloud.baidu-int.com/comatestack/share/3423?token=80bb6be3)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9b028bc6511f4bbb9b0e02a51515c104&docGuid=uEaB9QbwewBNYi "")
**第四个步骤是：验证 Rules 是否有效**

[https://console.cloud.baidu-int.com/comatestack/share/3422?token=eb43d287](https://console.cloud.baidu-int.com/comatestack/share/3422?token=eb43d287)

```
Agent 是怎么调用知识集工具的
```


## 对模型友好的架构
1. 单一职责、开闭原则、接口隔离，等等



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
