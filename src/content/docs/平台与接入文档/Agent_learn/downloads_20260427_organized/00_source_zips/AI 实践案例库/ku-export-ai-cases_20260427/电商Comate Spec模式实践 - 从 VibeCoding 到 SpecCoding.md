---
title: "目录"
description: "电商Comate Spec模式实践 - 从 VibeCoding 到 SpecCoding"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\电商Comate Spec模式实践 - 从 VibeCoding 到 SpecCoding.md"
---
电商Comate Spec模式实践 - 从 VibeCoding 到 SpecCoding

#### 🧑‍🏫 案例作者：[@文胜平](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：信息洞察、项目管理、数据分析、知识加工、提示词、开发、设计
#### 🔧 使用工具：Comate、知识库
#### 📒 案例概要：电商Comate Spec模式实践：对比Vibe与Spec编码，通过eDB-MCP工具案例验证，总结混合使用平衡效率与规范的方法论。
# 目录
[文档目录]


# 背景
在[🌟电商产研AI Coding实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/t0Wg1AdIFUwIoJ?t=mention&mt=doc&dt=doc)的实践案例中， 案例5/6 使用到了  Spec Coding 的相关理念，本案例通过

1. 实际使用 Comate Spec 模型，进行一个具体工具的开发，进行相关效果验证；  
2. 搭建一个 eDB-mcp 服务，解决研发环节 AI IDE 与 数据库交互的阻断问题；

# 概述


## 2.1 Vibe Coding vs Spec Coding 对比
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b4f7aff9663643bc9d13619419498ba5&docGuid=IdUVi69h2Oh3w7 "")
|**对比维度**|**Vibe Coding（氛围/体感编码）**|**Spec Coding（规范驱动编码）**|
|-|-|-|
|定义与核心逻辑|无详尽规范，靠「体感/直觉」驱动编码，边做边调|基于详尽规范说明书（Spec）驱动编码，按规执行|
|核心假设|需求/场景可快速迭代验证|需求可提前定义且相对稳定|
|前置准备|无/极简 Spec，仅核心目标口头共识|编写详尽 Spec（需求、边界、输入输出、异常等）|
|需求粒度|粗粒度，仅明确核心目标|细粒度，明确每一步逻辑、校验规则|
|编码节奏|快速迭代、边写边改、小步验证|按阶段推进（Spec 评审→编码→测试）|
|沟通方式|口头/轻量化沟通（如即时消息）|书面化沟通（Spec 文档、评审会议）|
|质量保障|靠开发者经验、手动测试、快速反馈|靠 Spec 校验、自动化测试、流程合规|
|容错机制|高容错，允许频繁调整|低容错，偏离 Spec 需走变更流程|
|实践流程|1. 口头对齐核心目标2. 快速原型编码3. 边编边验证4. 快速交付5. 持续迭代|1. 需求拆解为规格项2. 编写完整 Spec3. 多方评审 Spec4. 按 Spec 编码5. 对照 Spec 测试6. 变更先更 Spec|
|优点|1. 开发速度快2. 灵活度高3. 适配快速变化的需求4. 低文档成本|1. 规范可控2. 沟通成本低（靠文档）3. 易维护/交接4. 质量可量化5. 适配大型团队|
|缺点|1. 易需求漂移、失控2. 维护成本高（无文档）3. 团队协作成本高4. 易留技术债务|1. 前期准备耗时久2. 灵活度低（变更繁琐）3. 文档成本高4. 对需求稳定性要求高5. 易过度设计|
|适用场景|1. 初创/MVP 快速验证2. 1-3 人小团队3. 需求频繁变化的创新功能4. 临时/一次性脚本5. 个人项目|新功能开发，开发新功能时，从需求分析到实现验收的完整流程技术方案选型，通过多工具对比和方案评审确定最优方案系统重构，通过详细设计和MVP验证，降低重构风险问题排查与优化，通过需求分析和方案设计，找到最优解决方案|
|协作门槛|高，依赖团队默契，新成员需花时间对齐「体感」|低，新成员可直接通过 Spec 理解需求/逻辑|
|质量风险点|易遗漏边界场景，仅关注核心体感|易过度设计，编码复杂度上升|
|迭代效率（短期 1-2 周）|效率极高，无需等待 Spec 编写/评审|效率低，前期准备耗时占比高|
|迭代效率（长期 3 个月+）|效率骤降，技术债务积累导致维护成本飙升|效率更高，低沟通/维护成本抵消前期投入|



## 2.2 总结
1. **核心差异**：Vibe Coding 是「直觉驱动」，优先效率和灵活；Spec Coding 是「规则驱动」，优先规范和可维护。
2. **选型关键**：小团队、短期验证、需求多变选 Vibe Coding；大团队、长期维护、核心/合规系统选 Spec Coding。
3. **实践建议**：可混合使用（核心逻辑用 Spec，非核心迭代用 Vibe），平衡效率与规范。

# 实践案例
## 3.1 需求概述
[eDB 数据查询服务概要设计 - v0.5](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/07bgldhn2sY3WE?t=mention&mt=doc&dt=doc)



**核心业务场景：**

* **不同角色使用问题**
    * 研发： 频繁切换工具查数据库（AI IDE ↔  Navicat || 命令行）
    * 数据分析师：数据关联查询，BI分析
    * 产品/运营： 可以通过 自然语言描述，进行数据分析

* **数据安全问题**
    * 数据库均在 云服务器上，需要对服务授权
    * 核心账号、密码的脱敏管理




**MVP版本：**

|场景|用户量|痛点强度|实施难度|MVP适配度|
|-|-|-|-|-|
|**研发场景**|中|⭐⭐⭐⭐⭐|中|⭐⭐⭐⭐⭐|
|数据分析|少|⭐⭐⭐⭐|高|⭐⭐⭐|
|产品运营|多|⭐⭐⭐|高|⭐⭐|



为什么聚焦研发场景？

用户画像：

```
研发人员
├── 痛点明确：频繁切换工具查数据库（AI IDE ↔ Navicat）
├── 技术敏感：容错率高，愿意给反馈
├── 价值直接：提升开发效率，ROI可衡量
└── 验证快速：小范围试点即可验证效果
```


```
传统方式：
1. 在Cursor / Comate 写代码
2. 想查数据 → 打开Navicat → 找到表 → 写SQL → 复制结果 → 回到Cursor / Comate
3. 总耗时：3-5分钟

eDB-MCP方式：
1. 在Cursor / Comate 写代码
2. 直接问AI："查一下user_id=123的订单"
3. AI直接返回结果
4. 总耗时：10秒 - 30秒

效率提升：10倍+
```


## 3.2 功能效果
持续开发完善中，目前完成初版mvp 数据库基础查询功能开发；



**v0.5开发耗时：**

本地项目验证初版效果，深度编码投入状态 ，大概耗时 6-8小时， 

* 明确场景以及核心痛点，厂内外方案了解评估，耗时约     1/3 ,  
* 方案生成，reivew ，明确耗时约 1/3；
* v0.5 功能编码，微调 1/3；



**服务配置**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0decfade0941480c95494e08fe5aee19&docGuid=IdUVi69h2Oh3w7 "")
```
{
  "mcpServers": {
      "edb-mcp": {
          "url": "http://wsp.bcc-szzj.baidu.com:8050/api/mcp/edb",
          "transportType": "streamableHttp",
          "description": "数据库查询MCP服务 edb - 提供数据库列表、表结构查看和SQL查询功能",
          "defaultArguments": {
              "token": "dev_team_test"
          }
      }
  }
}
```


### **3.2.2 效果示例：v0.5 - 本地数据库验证**
![使用mcp工具](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=db8b6d6e81c5476b934a181bd01b9c58&docGuid=IdUVi69h2Oh3w7 "使用mcp工具")
![查看可访问数据库](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7382987f8f014b319fa0d756792e1b1a&docGuid=IdUVi69h2Oh3w7 "查看可访问数据库")


**表结构示例：**

![mcp执行说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=edf595094b2a4a2599647e5c245dc834&docGuid=IdUVi69h2Oh3w7 "mcp执行说明")
![mcp返回表详情](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e4aece601835421c9747917c17872e44&docGuid=IdUVi69h2Oh3w7 "mcp返回表详情")
![navicat 查看表结构](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cf8b3f862d5040e4920a5265d0bfa76e&docGuid=IdUVi69h2Oh3w7 "navicat 查看表结构")


**TEXT 2 SQL示例 :**

![数据分析过程](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=57603dcdf2ad46f6abcf40de1cbc654a&docGuid=IdUVi69h2Oh3w7 "数据分析过程")
![基础分析结果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7cc4d81274a54fd9a572ee5b7e0deea2&docGuid=IdUVi69h2Oh3w7 "基础分析结果")
![进阶数据分析结果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0eb58167716d4b3ba7f80e38636184cc&docGuid=IdUVi69h2Oh3w7 "进阶数据分析结果")




### **3.2.3 效果示例：v0.8 - 线上数据库验证**
在[🌟电商产研AI Coding实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/t0Wg1AdIFUwIoJ?t=mention&mt=doc&dt=doc)中的示例case  ，需要通过 3步才能得出分析结论，但是同时 mcp方式，通过一次对话即可获取到对应数据分析结论；



**Step1:** 分析表结构

**Step2:** 生成数据查询sql

**Step3: **获取到数据后分析结论



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ddbce61f67914e8bb1741f104ed73e8f&docGuid=IdUVi69h2Oh3w7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ff5e41f69ac4c708addd5ef450b78c9&docGuid=IdUVi69h2Oh3w7 "")




**模型一次性调用验证：**

|**需求说明**|**分析结论**|**完整SQL**|**线下验证**|
|-|-|-|-|
|使用edb 查询 ec_content_db 数据库，统计视频化生产各阶段成功的数据漏斗，**包含Query下发-视频脚本生产-数字人生产-素材处理-云剪辑-封面审核-百家号发布**多个阶段成功的数据；![需求说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=58c08a56f3e34ce48c0cbfa9b617d30f&docGuid=IdUVi69h2Oh3w7 "需求说明")|![分析结论](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=67b52eb2b645409d96fbd227f1e0bf60&docGuid=IdUVi69h2Oh3w7 "分析结论")|![完整的SQL](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1535b8116193446dba0fa3e1aab352e8&docGuid=IdUVi69h2Oh3w7 "完整的SQL")|![线下验证](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b875cc8ed87f48f79437827ce190a0df&docGuid=IdUVi69h2Oh3w7 "线下验证")|





### 3.2.4 效果示例：v1.0 - MVP版本-支持本地Rules结合
完善中 ...



## 3.3 Spec 模式实践 
### 3.3.1 项目方案初始编写 - 仅包含计划流程
#### 3.3.1.1  方案多轮设计
[评审：DS-sousuo2023-9500 edb mvp 版本提交](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/db-mcp/reviews/119218982/files/base...latest/.comate/specs/GDP%E6%A1%86%E6%9E%B6%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8A%A8%E6%80%81%E9%85%8D%E7%BD%AE%E5%8A%A0%E8%BD%BD%E6%96%B9%E6%A1%88/plan_mvp_detail.md?t=mention&mt=doc&dt=sdk)



**Step1：**明确核心业务场景，痛点问题

**Step2:  **人工收集信息，借鉴 厂内外的相关解决方案

**Step3：**使用不同 AI 客户端，提出相同问题，查看反馈方案的优缺点

**Step4**：选择最优方案/客户端，进行持续沟通，澄清需求，优化方案，确认总体设计   (Comate Spec  +  Claude 4.5 sonnet)

**Step5：**明确mvp版本，细化详细设计

**Step6:   **明确task list， 确认Coding 计划方案

**Step7: **  实际编码

**Step8: **  功能微调，保证正常编译通过

**Step9:**   单元测试

**Step10: ** 效果验收 







![多种AI客户端，多轮交互](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d263ff96ddf74c16bc4525f722de3bfa&docGuid=IdUVi69h2Oh3w7 "多种AI客户端，多轮交互")
![Comate Spec 模式应用 + claude 4.5 sonnet](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1486979bdf3f482cb069a5804fba65cb&docGuid=IdUVi69h2Oh3w7 "Comate Spec 模式应用 + claude 4.5 sonnet")


**对话示例：**

|**对话轮次**|**说明**|**inpu**|**output**|
|-|-|-|-|
|1|核心业务场景说明， 方案初始化|[https://console.cloud.baidu-int.com/comatestack/share/3816?token=2f3cd0bc](https://console.cloud.baidu-int.com/comatestack/share/3816?token=2f3cd0bc)![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c5d149b059344d7e80d8d0de5437ba99&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0d6cce4f8c8c4151ac2f1a8d49f980ba&docGuid=IdUVi69h2Oh3w7 "")|
|2|人工review，补充场景，澄清需求|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=575e07000d0c4c4c8648edb1775b28b7&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e7e57b04a5eb4beb92ad336db47891d9&docGuid=IdUVi69h2Oh3w7 "")|
|3|人工review， 多份技术文档整合，不同方案间对比整合|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=94285897eea84059b159b56d46bff556&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7330eb06e9124557b5b430c547cd965f&docGuid=IdUVi69h2Oh3w7 "")|
|4|持续追问，需求扩散，查漏补缺|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b770f726b0aa4a7b8afebe414f907bae&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c2caa9bee9d74512b3537ba8bd753be8&docGuid=IdUVi69h2Oh3w7 "")|
|5|问题整合收敛，明确优先级|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=958d0a5a2a594b8ba5001dabacafac48&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=96371cb6ee72449c9dae06cdb1442b26&docGuid=IdUVi69h2Oh3w7 "")|
|6|方案review ， 给peer 或者  high peer 把关|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7d8e9a31c12840e2a874005556f50aae&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=66a2cacee5884d5885267c2d33fc5094&docGuid=IdUVi69h2Oh3w7 "")|
|7|明确落地 mvp功能集合，进行快速验证|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8da90c130aa44ead8af958264fdceb7d&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f79177d60b6d4630abc4a29869cef5bf&docGuid=IdUVi69h2Oh3w7 "")|
|**8**|确认mvp集合后，结合之前其他项目沉淀-可复用的 rules ， 对技术方案进行详细设计 |![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3b99445134ea4dcf9b64247d27d014c7&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6f44449eb8734b7099999e56ca4a4051&docGuid=IdUVi69h2Oh3w7 "")|
|**9**|**产出任务ToDo list **|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6b4fa1f8b7ec42c7aa086b10559f390f&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9a0a49c404aa43d6b838c1ae594617cd&docGuid=IdUVi69h2Oh3w7 "")|
|**10**|**实际编码实现**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8eda955ea2c4479cb8ea1dfb39a208d9&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=113ec711de4c4d70b753e6aa7471e602&docGuid=IdUVi69h2Oh3w7 "")|
|**11**|**功能测试，效果验证**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8cb75fda1141406c96b4610c453ef587&docGuid=IdUVi69h2Oh3w7 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cbf0e90731d54636b48d278fc74d6955&docGuid=IdUVi69h2Oh3w7 "")|





#### 3.3.1.2 效果验证
case1: 使用edb 列出当前可访问的 数据库 

case2: 使用edb 查看  订单库近 7天的订单情况 



|**客户端 IDE **|**使用说明**|**配置说明**|**效果示例**|
|-|-|-|-|
|**Cursor**（Auto模式）|**用户群体：**全栈开发者、AI研究者、编程新手/学生、企业开发团队**是否收费**：收费使用|~/.cursor/mcp.json目前cursor 配置完成 mcp服务后，可默认调用，无需额外配置![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6f7914c976544d25bc58ea97c6a824ed&docGuid=IdUVi69h2Oh3w7 "")|![case1](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=87cd4a00346e4bddbe4a1e493d94574b&docGuid=IdUVi69h2Oh3w7 "case1")![case2](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=83d5dcada00c42d5aa1005b86202b70a&docGuid=IdUVi69h2Oh3w7 "case2")|
|**Comate**（Zulu + Claude 4.5）|**用户群体：**全栈/前端工程师、产品经理、技术小白**是否收费**：厂内 集成，智能云统一收费|~/.comate/mcp.json![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=66b7f094c37b4526b9a0efd3619dc61e&docGuid=IdUVi69h2Oh3w7 "")需要手动勾选 对应 Agent，对应MCP服务才能使用![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d79ca3a11ab24dd3bbbb3ead4a9248ab&docGuid=IdUVi69h2Oh3w7 "")|case 1 ![case1](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bc0068c2c8db4ea2b0a21a851d315063&docGuid=IdUVi69h2Oh3w7 "case1")![case2](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7d3dd13a75ae4318947b4555af044af7&docGuid=IdUVi69h2Oh3w7 "case2")|
|**Cherry Studio**(qianfan ernie-turbo-4.5)|**用户群体：**国内开发者（技术团队、个人开发者）、**AI工具使用者****是否收费：**客户端免费，高级模型API收费，每天有部分免费额度|MCP服务添加![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5b011618d30e44e5a60097888a5edf76&docGuid=IdUVi69h2Oh3w7 "")会话中 显示勾选确认 使用的 mcp工具![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6cc5d37806cb42e489d48f7ba0df7b7a&docGuid=IdUVi69h2Oh3w7 "")|![case1](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8b102bf5bdbf483e8d54b581506923a1&docGuid=IdUVi69h2Oh3w7 "case1")![case2](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d2cdcafc875641b9b955f5873c77180a&docGuid=IdUVi69h2Oh3w7 "case2")|
|**如流数字员工**|**待后续接入；**如流客户端内使用，方便业务同学使用|||





### 3.2.1 功能迭代  - 完整流程


#### 3.2.2.1 功能优化说明
**对话**：[https://console.cloud.baidu-int.com/comatestack/share/3884?token=1cac8305](https://console.cloud.baidu-int.com/comatestack/share/3884?token=1cac8305)

### **Input**
### **Output**
**prompt:**

```
1. 进行代码 重构优化 ， 基础功能逻辑迁移至 service  #mcp   ， 调度整合 存放在servers   #mcp  
  #server.go   #handlers.go  

2. 思考插件的 Mysql 查询场景，补充2-3个高频使用 查询工具

3. 进行实际新增工具验证
  #test_mcp_tools.sh    #test_comate_mcp.sh    #simple_mcp_test.sh  相关工具整合 ，保留一个
```


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1671c43187e84bca964ca33802dc3594&docGuid=IdUVi69h2Oh3w7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ca581aca9f434370aba85ac0ffb28421&docGuid=IdUVi69h2Oh3w7 "")




#### 3.2.2.2 效果验证


**验证输出对话：**[https://console.cloud.baidu-int.com/comatestack/share/3886?token=c462f202](https://console.cloud.baidu-int.com/comatestack/share/3886?token=c462f202)



![MCP服务 ](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b3da22bab2594b77851eb67f0ce4b4b4&docGuid=IdUVi69h2Oh3w7 "MCP服务 ")
![权限配置](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9ba2af95e39446b6ac2b93b5d772eb7c&docGuid=IdUVi69h2Oh3w7 "权限配置")
![线上Mysql 测试表配置](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7a589806f31440fc879ed1320c017a70&docGuid=IdUVi69h2Oh3w7 "线上Mysql 测试表配置")




|需求说明|分析结论|完整SQL|线下验证|
|-|-|-|-|
|![需求说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=58c08a56f3e34ce48c0cbfa9b617d30f&docGuid=IdUVi69h2Oh3w7 "需求说明")|![分析结论](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=67b52eb2b645409d96fbd227f1e0bf60&docGuid=IdUVi69h2Oh3w7 "分析结论")|![完整的SQL](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1535b8116193446dba0fa3e1aab352e8&docGuid=IdUVi69h2Oh3w7 "完整的SQL")|![线下验证](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b875cc8ed87f48f79437827ce190a0df&docGuid=IdUVi69h2Oh3w7 "线下验证")|

















# 总结
本文档总结了基于AI辅助的软件开发完整流程，将业务场景分析、方案设计、编码实现、测试验收等环节系统化，形成可复用的方法论。







|**Input**|**Output**|
|-|-|
|**prompt:**@spec.md 将对应流程整合 ，总结经验沉淀， 形成方法论 ， 然后产出 mermaid流程图 、 SVG矢量图形式[附件]![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fe72fa94b8924c0cbaacd48de31bd4d3&docGuid=IdUVi69h2Oh3w7 "")|[附件]![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=32a02307a74749b09bef4a2aa4154f2a&docGuid=IdUVi69h2Oh3w7 "")|

****

## 4.1 核心流程总览
|**阶段**|**步骤**|**步骤名称**|**目标**|**输出**|**对话轮次**|**工具**|
|-|-|-|-|-|-|-|
|**阶段一：需求分析与方案探索**|Step 1|明确核心业务场景，痛点问题|清晰定义要解决的业务问题|业务场景文档、痛点清单|对话轮次1|人工收集，内部访谈|
||Step 2|人工收集信息，借鉴厂内外的相关解决方案|收集现有解决方案，避免重复造轮子|竞品分析、技术调研报告|对话轮次2|Github 收集内网查阅|
||Step 3|使用不同AI客户端，提出相同问题，查看反馈方案的优缺点|通过多AI工具对比，获得不同视角的方案|多方案对比分析|对话轮次3|多个AI工具Cusror + Auto模式 （GTP 5.1 Codex）Gemini 网页 + Gemini 3.0 Comate Zulu + Claude 4.5 sonnetComate Spec + Claude 4.5 sonnet|
||Step 4|选择最优方案/客户端，进行持续沟通，澄清需求，优化方案，确认总体设计|确定最终技术方案和设计架构|总体设计方案、技术架构文档|对话轮次4-6|优选：Comate Spec 模式 + Claude 4.5 Sonnet|
|**阶段二：详细设计与规划**|Step 5|明确MVP版本，细化详细设计|确定最小可行产品范围，完成详细设计|MVP功能清单、详细设计文档|对话轮次7-8|-|
||Step 6|明确Task List，确认Coding计划方案|将设计转化为可执行的任务清单|任务清单（Todo List）、开发计划|对话轮次9|-|
|**阶段三：开发实现**|Step 7|实际编码|按照设计实现功能代码|功能代码|对话轮次10|-|
||Step 8|功能微调，保证正常编译通过|修复编译错误，确保代码可运行|可编译运行的代码|-|-|
|**阶段四：测试与验收**|Step 9|单元测试|编写并执行单元测试，保证代码质量|单元测试用例、测试报告|-|-|
||Step 10|效果验收|验证功能是否符合预期，完成验收|验收报告|对话轮次11|-|

## 4.2 详细说明 
### 4.2.1 对话轮次详细说明
|**对话轮次**|**所属步骤**|**主要内容**|**关键活动**|
|-|-|-|-|
|1|Step 1|核心业务场景说明，方案初始化|明确业务场景、痛点问题，启动方案设计|
|2|Step 2|人工review，补充场景，澄清需求|人工审核、补充遗漏场景、澄清模糊需求|
|3|Step 3|人工review，多份技术文档整合，不同方案间对比整合|整合多份技术文档，对比不同AI工具方案|
|4|Step 4|持续追问，需求扩散，查漏补缺|深入追问细节，扩展需求边界，发现遗漏点|
|5|Step 4|问题整合收敛，明确优先级|整合所有问题，收敛需求范围，确定优先级|
|6|Step 4|方案review，给peer或high peer把关|技术方案评审，获得peer或high peer认可|
|7|Step 5|明确落地MVP功能集合，进行快速验证|确定MVP范围，准备快速验证|
|8|Step 5|确认MVP集合后，结合之前其他项目沉淀-可复用的rules，对技术方案进行详细设计|结合历史项目经验，完成详细技术设计|
|9|Step 6|产出任务ToDo list|将设计转化为可执行的任务清单|
|10|Step 7|实际编码实现|按照设计进行代码实现|
|11|Step 10|功能测试，效果验证|执行功能测试，验证效果是否符合预期|

## 4.3 关键说明
### 4.3.1 方法论要点说明
|**要点**|**核心内容**|**具体实践**|
|-|-|-|
|**多工具协同**|使用多个AI工具进行方案对比，选择最适合的工具进行深度协作|- 使用多个AI工具（Comate、Claude等）进行方案对比- 选择最适合的工具进行深度协作|
|**人工审核机制**|关键节点进行人工review，重要方案需要peer或high peer把关|- 关键节点进行人工review- 重要方案需要peer或high peer把关|
|**MVP优先**|先确定MVP范围，快速验证，基于MVP反馈迭代优化|- 先确定MVP范围，快速验证- 基于MVP反馈迭代优化|
|**知识复用**|结合历史项目沉淀的可复用rules，借鉴厂内外最佳实践|- 结合历史项目沉淀的可复用rules- 借鉴厂内外最佳实践|
|**迭代优化**|通过多轮对话持续澄清需求，问题整合收敛，明确优先级|- 通过多轮对话持续澄清需求- 问题整合收敛，明确优先级|

### 4.3.2 关键因素
|**因素**|**对应步骤**|**说明**|
|-|-|-|
|**需求清晰**|Step 1-4|确保需求理解准确，通过多轮对话和方案对比，明确业务场景和痛点|
|**设计完善**|Step 5-6|确保设计可执行，通过MVP确定和详细设计，将需求转化为可落地的技术方案|
|**实现规范**|Step 7-8|确保代码质量，通过规范编码和编译验证，保证代码可运行|
|**验证充分**|Step 9-10|确保功能正确，通过单元测试和效果验收，验证功能是否符合预期|

### 4.3.3  阶段产出物清单
|**阶段**|**产出物**|
|-|-|
|**阶段一：需求分析与方案探索**|- 业务场景文档- 痛点清单- 竞品分析报告- 技术调研报告- 多方案对比分析- 总体设计方案- 技术架构文档|
|**阶段二：详细设计与规划**|- MVP功能清单- 详细设计文档- 任务清单（Todo List）- 开发计划|
|**阶段三：开发实现**|- 功能代码- 可编译运行的代码|
|**阶段四：测试与验收**|- 单元测试用例- 测试报告- 验收报告|

### 4.3.4 适用场景
|**场景类型**|**说明**|
|-|-|
|**新功能开发**|开发新功能时，从需求分析到实现验收的完整流程|
|**技术方案选型**|需要选择技术方案时，通过多工具对比和方案评审确定最优方案|
|**系统重构**|系统重构时，通过详细设计和MVP验证，降低重构风险|
|**问题排查与优化**|问题排查和优化时，通过需求分析和方案设计，找到最优解决方案|

### 4.3.5 流程特点
|**特点**|**说明**|
|-|-|
|**AI辅助**|充分利用AI工具进行方案设计、代码实现等环节|
|**人工把关**|关键节点进行人工review，确保方案质量|
|**迭代优化**|通过多轮对话和反馈，持续优化方案|
|**知识沉淀**|结合历史项目经验，形成可复用的方法论|
|**MVP优先**|优先实现MVP功能，快速验证，降低风险|





# 后续优化
## 5.1 EDB功能维度
### 5.1.1 持续完成P1相关功能
**P1阶段功能（第二阶段 ）**

P1阶段聚焦于提升AI对数据库的理解能力和查询准确性，主要包括：

|功能模块|具体内容|预期价值|
|-|-|-|
|**智能表结构理解**|- 自动解析表关系（主外键、索引）- 识别业务语义（表名、字段名语义化）- 构建表关系图谱|提升AI对数据库结构的理解准确度，减少查询错误|
|**上下文增强**|- 基于代码上下文推荐相关表- 智能补全表名、字段名- 查询历史记忆与复用|减少用户输入成本，提升查询效率|
|**查询优化建议**|- SQL性能分析- 索引使用建议- 查询结果缓存|提升查询性能，降低数据库负载|
|**多数据源支持**|- 支持MySQL、GaiaDB、Doris等- 统一查询接口- 数据源配置管理|扩展系统适用范围，支持更多业务场景|



**实施策略**

1. **迭代开发**：按照MVP → P1 → P2的顺序，逐步迭代，确保每个阶段都有可用的功能
2. **用户反馈驱动**：每个阶段完成后，收集用户反馈，及时调整后续功能优先级
3. **技术债务管理**：在功能开发过程中，持续重构和优化代码
4. **性能优化**：随着功能增加，持续优化系统性能，确保响应速度

### 5.2 完成相关平台能力
**平台化能力建设**

为了支撑EDB功能的持续演进和规模化应用，需要建设以下平台能力：

|**平台能力**|**建设内容**|**价值**|
|-|-|-|
|**配置管理平台**|- 数据库配置的统一管理- 多环境配置支持（开发/测试/生产）- 配置版本控制与回滚|提升配置管理效率，降低配置错误风险|
|**监控告警平台**|- 系统性能监控（QPS、延迟、错误率）- 数据库连接池监控- 异常查询告警|及时发现问题，保障系统稳定性|
|**用户管理平台**|- 用户权限管理- 使用统计与分析- 用户行为追踪|支持精细化运营，优化用户体验|
|**知识库平台**|- 查询模板库- 最佳实践文档- 常见问题FAQ|知识沉淀与共享，降低学习成本|
|**API网关**|- 统一API入口- 限流与熔断- 请求路由与负载均衡|保障系统高可用，支持大规模访问|

**平台能力建设原则**

1. **可扩展性**：平台架构设计要考虑未来功能扩展，避免频繁重构
2. **可观测性**：完善的监控和日志体系，便于问题定位和性能优化
3. **安全性**：从设计阶段就考虑安全因素，包括数据加密、访问控制等
4. **易用性**：平台界面和API设计要简洁易用，降低使用门槛

## 5.2 方法论能力沉淀  ( 探讨 -  AI-Coding实践中 进阶类问题 的拓展 )
### 5.2.1 将方法论沉淀为Skill或Agent形式 
**目标**

将本文档总结的AI辅助软件开发方法论，转化为可执行的AI Skill或Agent，使其能够在实际开发过程中自动应用，提升开发效率和代码质量。

**Skill/Agent设计思路**

|能力类型|实现方式|应用场景|
|-|-|-|
|**需求分析Agent**|基于Step 1-4流程，自动进行需求分析和方案设计|新功能开发、技术方案选型|
|**代码审查Agent**|基于Step 8-9流程，自动进行代码审查和测试建议|代码提交前审查、持续集成|
|**任务规划Agent**|基于Step 5-6流程，自动将需求拆分为任务清单|项目启动、迭代规划|
|**知识沉淀Agent**|自动提取项目中的最佳实践，形成可复用知识库|项目总结、知识管理|

**技术实现路径**

1. **规则引擎**：将方法论中的步骤和检查点转化为规则，通过规则引擎执行
2. **Prompt模板**：为每个阶段设计标准化的Prompt模板，确保AI按照方法论执行
3. **上下文管理**：维护项目上下文，确保AI能够理解当前项目状态和历史信息
4. **反馈机制**：收集AI执行结果和用户反馈，持续优化Agent能力

**预期效果**

* **效率提升**：自动化执行方法论中的重复性工作，节省人工时间
* **质量保障**：通过标准化流程，确保每个项目都遵循最佳实践
* **知识复用**：将方法论固化到Agent中，便于团队共享和传承
* **持续改进**：通过Agent执行反馈，不断优化方法论本身

### 5.2.2 针对文档、方案设计场景进行延伸
**文档生成场景**

基于方法论，开发专门的文档生成Agent，支持以下场景：

|场景|功能|实现方式|
|-|-|-|
|**需求文档生成**|根据业务场景自动生成需求文档|基于Step 1-2，提取业务场景和痛点，生成结构化需求文档|
|**技术方案文档**|根据需求自动生成技术方案文档|基于Step 3-4，整合多方案对比，生成技术方案文档|
|**API文档生成**|根据代码自动生成API文档|解析代码注释和接口定义，生成标准化的API文档|
|**测试文档生成**|根据测试用例自动生成测试文档|基于Step 9，提取测试用例和测试结果，生成测试报告|

**方案设计场景**

基于方法论，开发专门的方案设计Agent，支持以下场景：

|场景|功能|实现方式|
|-|-|-|
|**架构设计**|根据需求自动生成系统架构设计|基于Step 4-5，分析需求特点，推荐合适的架构模式|
|**数据库设计**|根据业务需求自动生成数据库设计|分析业务实体和关系，生成ER图和建表SQL|
|**接口设计**|根据业务逻辑自动生成接口设计|分析业务流程，生成RESTful API设计文档|
|**部署方案设计**|根据系统特点自动生成部署方案|分析系统规模和特点，推荐合适的部署架构|

# 参考
* **厂内：**

[重磅升级！更开放、更先进的 Comate AI IDE 来了！](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/z97pwhZizu/hy296wAZ7z/xjYnjWL3qtdDW_?t=mention&mt=doc&dt=doc)

[🌟面向生产环境的Vibe Coding：如何构建低成本的验证体系？](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/jCva49xwIBHCYB?t=mention&mt=doc&dt=doc)

[🌟Coding Agent实践：业务与平台的双向奔赴](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/kcH3cHcakHm37t?t=mention&mt=doc&dt=doc)

[🌟电商产研AI Coding实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/t0Wg1AdIFUwIoJ?t=mention&mt=doc&dt=doc)



* **厂外**

[https://kiro.dev/docs/specs/concepts/](https://kiro.dev/docs/specs/concepts/)

[https://www.infoq.cn/article/fjmkp6owah4yhtf1nkbi](https://www.infoq.cn/article/fjmkp6owah4yhtf1nkbi)

[https://www.cnblogs.com/tlnshuju/p/19304242](https://www.cnblogs.com/tlnshuju/p/19304242)





**更多团队实践沉淀参考：**

[AI-Coding-Topic分享](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/1MxrXIeQB-1zzC?t=mention&mt=doc&dt=doc)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f031b5dfe46b4754b20b1900bf622407&docGuid=C9U3wC_9skbauC "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=78ccae016804424aab1a04a421c18b3b&docGuid=IdUVi69h2Oh3w7 "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
