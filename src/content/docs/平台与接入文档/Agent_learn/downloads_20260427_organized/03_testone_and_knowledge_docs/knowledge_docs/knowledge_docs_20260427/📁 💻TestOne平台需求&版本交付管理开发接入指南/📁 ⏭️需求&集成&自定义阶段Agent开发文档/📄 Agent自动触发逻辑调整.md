---
title: "1、问题"
description: "Agent自动触发逻辑调整"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📄 Agent自动触发逻辑调整.md"
---
Agent自动触发逻辑调整

# 1、问题
TestOne各阶段Agent执行完成的返回结果里面有个字段 enter_next_stage 用于各个开发者控制是否可以自动进入下一个阶段，触发下一个阶段Agent。

但是，平台并不是完全按照这个字段的返回结果来进行控制的，具体控制方式如下

|阶段|enter_next_stage字段的处理逻辑|设计考虑|
|-|-|-|
|需求阶段|true: 不触发false：不触发|需求创建就会自动导入到TestOne平台，此时自动触发开发阶段不太合理。为了避免Agent开发者误填，平台进行了屏蔽，一律不触发|
|开发阶段|true: 不触发false：不触发|Agent开发者不太可能知道一张卡片什么时候开发完成，期间自动触发提测准入的时候 ，可能研发都还没开发自测玩。为了避免开发者误填，平台进行了屏蔽，一律不触发|
|准入阶段|true: 自动触发false：不触发||
|测试阶段|true: 自动触发false：自测需求：自动触发非自测需求：不触发|针对自主测试需求，通常RD也不太可能来使用TestOne平台操作开始测试，触发准出校验。如果开发者漏下发这个字段，不自动触发准出。那么准出阶段的Agent可能就不会执行到，存在一定的问题漏出风险，所以针对自测的需求，平台一律自动准出。|
|联调阶段|true: 自动触发false：不触发||
|准出阶段|true: 自动触发false：不触发||
|完成阶段|true: 自动触发false：不触发||



但是，随着接入的业务越来越多，各个业务的流程要求也存在很大的差异，很多业务场景下，业务平台默认的处理逻辑并不满足业务需要，平台的处理逻辑和业务Agent返回的结果是相悖的。



# 2、目标
流程自动推进的逻辑完全交由业务Agent开发者控制，平台不再特殊干预

|阶段|升级前 enter_next_stage字段的处理逻辑|升级后 enter_next_stage字段的处理逻辑|
|-|-|-|
|需求阶段|true: 不触发false：不触发|true: 自动触发false：不触发|
|开发阶段|true: 不触发false：不触发|true: 自动触发false：不触发|
|准入阶段|true: 自动触发false：不触发|true: 自动触发false：不触发|
|测试阶段|true: 自动触发false：自测需求：自动触发非自测需求：不触发|true: 自动触发false：不触发|
|联调阶段|true: 自动触发false：不触发|true: 自动触发false：不触发|
|准出阶段|true: 自动触发false：不触发|true: 自动触发false：不触发|
|完成阶段|true: 自动触发false：不触发|true: 自动触发false：不触发|



# 3、升级方案
自己根据需要决定，是否需要自动触发下一阶段（如不主动赋值，默认的enter_next_stage都是false）








