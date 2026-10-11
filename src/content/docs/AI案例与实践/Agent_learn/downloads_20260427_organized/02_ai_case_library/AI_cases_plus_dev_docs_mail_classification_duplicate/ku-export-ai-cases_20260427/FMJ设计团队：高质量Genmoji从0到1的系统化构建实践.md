---
title: "0.介绍&感谢"
description: "FMJ设计团队：高质量Genmoji从0到1的系统化构建实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\FMJ设计团队：高质量Genmoji从0到1的系统化构建实践.md"
---
FMJ设计团队：高质量Genmoji从0到1的系统化构建实践

#### 🧑‍🏫 案例作者：[@骆奕伶](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：设计
#### 🔧 使用工具：Al Studio、Cursor
#### 📒 案例概要：FMJ设计团队通过AI Coding构建了Genmoji Studio平台，将碎片化的表情生产流程整合为一体化解决方案。平台实现了从生成、处理到多尺寸导出的全流程可视化操作，极大降低了使用门槛。团队核心优化了生图效果：采用“单图多表情”矩阵策略确保画风统一，结合“Prompt+垫图”双约束控制风格，并选定高效模型，最终实现了高质量、高效率、可复用的Genmoji生产能力。
# 0.介绍&感谢
主要介绍设计团队0到1探索Genmoji功能，从构想到落地与不断实践，持续打磨生成效果，最终实现了可作为功能上线的Genmoji表情生产能力

![⬆️ 主要参与；感谢FMJ设计的小伙伴以及其他参与的同学](/personal-site-mvp/img/doc-placeholder.svg "⬆️ 主要参与；感谢FMJ设计的小伙伴以及其他参与的同学")
****

**【✨趣味结果案例展示✨】**

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 1.背景
**🛣️ 从效率问题出发**

* 初期的genmoji生成脚本实现使用复杂，需要一定的学习成本，
* UE自身在使用的时候都会遇到很多问题，
* genmoji更多依赖AI生成，不以设计为中心，所花费的设计时间和修改成本并不能够直接为设计带来价值

![❌原始的批量脚本方案-没有教学看不懂](/personal-site-mvp/img/doc-placeholder.svg "❌原始的批量脚本方案-没有教学看不懂")


这时候我们就思考，随着模型的迭代，能不能有一种方式能够保证现有质量的同时，快速&低成本的把重复性的工作解决掉

**目标制定**

利用AI Coding以及图像模型，从设计角度把 genmoji 生成这件事简单化，实现无门槛&快速&的可长期复用的平台式解决方案，**让其他角色也能够一起参与，实现设计能力AI化**



# 2.让想法成为现实的AI全流程
### 2.1 0-1生成平台构建
平台核心需要解决设计此前在Genmoji过程中的核心痛点

**生产流程碎片化**

生成、处理与导出分散在不同工具中，设计师需要在多个软件与脚本之间反复切换。



**学习与使用门槛较高**

早期批量生成依赖脚本，使用成本较高，非设计角色难以参与。

**重复操作消耗大量时间**

大量时间被消耗在裁剪、调整、导出等重复性步骤，而不是在创意与质量判断上。

**AI能力没有真正转化为生产力**

虽然生成能力强，但缺少完整的生产流程设计，AI仍然停留在“单点工具”的阶段

因此，我们开始思考：

**能否把整个生产链路重新设计，并通过 AI Coding 构建一个轻量的平台，将分散的步骤整合成一条可复用的生产流程？**

#### 2.1.1 Vibe coding 构建平台Demo
* 不需要在脑内有非常清晰的样式，把自己模糊的构思以及需要解决的问题使用自然语言的方式与GPT交流，让GPT进行整理补充后再汇总成完整的需求prompt；
* 利用gemini 3在自然语言下能够快速实现高质量web构建的能力，依照prompt思路能够一次性构建可交互的工具站;

![](/personal-site-mvp/img/doc-placeholder.svg "")
**gemini的一次性生成足够简约美观，在后续Coding我们只想一件事：****非设计角色也能够简单使用**，更关注交互方式搭建

#### 2.1.2 契合真实生产链路的交互构建
genmoji制作的核心痛点并非“不会生成”，而是“生成过程被大量重复步骤拖慢”；我们明确了“人力介入节点”，将设计师从重复劳动中解放出来。

### **项目管理**
实际genmoji生成管理会有多个不同项目，首页按照项目分类，并将所有结果保存在网站本地避免丢失，随时可以进行历史查看和找回

![](/personal-site-mvp/img/doc-placeholder.svg "")
### **整合式的生产方式构建**
Genmoji制作在之前往往是被零碎&重复步骤拖慢；点为了能够更可视化的进行图片生产操作，我们将：图片生成，图片对比，图片处理 等零散的高频操作固化为可视化操作模块，支持不同维度的生产和修改需要，直线降低了学习门槛

[附件]


### **一站式多尺寸导出**
在 Genmoji 实际生产中，图片尺寸需要适配不同平台；如果依赖设计师手动导出与调整尺寸，不仅耗时，也容易产生尺寸错误或资源遗漏；因此，我们将 **资源导出能力直接整合进平台**，提供一站式的多尺寸导出方案

最终一个平台就能够实现 **一键生图、选图、调整、调色、扣图、导出 **的一体化操作

![](/personal-site-mvp/img/doc-placeholder.svg "")


##### **Tips：AI 平台构建小技巧**
构建中发现每次都需要额外的网页刷新；

Cursor插件-Browser tab能够实现直接在Cursor窗口中实时浏览，能够更快速的进行实时浏览查看

![](/personal-site-mvp/img/doc-placeholder.svg "")
****

**Before-之前的设计流程：**

画风、情景、IP、数量



沟通、迭代

调色、裁剪、重绘等

手机效果预览





⬇️

**After-重构后的操作流程：**

全程仅需 PM 介入需求输入和结果取舍，无需设计师参与重复劳动，实现“一次进入、全程完成”。

清晰项目管理

画风、情景、IP、数量



裁剪、AI反馈修改、调色

自由排序、一键扣图、双端尺寸压缩包

**详细流程可参考文档：**[Genmoji Studio 网站使用说明](https://ku.baidu-int.com/d/IUrzpS2krKuJqw?t=mention&mt=doc&dt=doc)



### 2.2 不断打磨的核心生图效果
平台是为了能够更高效的使用，但是genmoji的重要核心是生成的图片质量与最终交付，为此我们从 **模型，策略，prompt **三个维度做了细致打磨



#### 2.2.1.模型选择-banana pro
我们对比了banana和banana相同prompt下的生成结果

* pro作为一个编辑模型，他对于图片风格转化和主体准确性的理解度更高，图生图下对比banana生成效果明显更优秀，直接选择了当时最新的pro来作为主要模型，
* 纯prompt的方式容易造成风格的不稳定，因此我们选择采用底图垫图的方式进行

banana

![3d emoji风格-服装丰富度有，但是动作较呆，](/personal-site-mvp/img/doc-placeholder.svg "3d emoji风格-服装丰富度有，但是动作较呆，")
![2D风格-特征丢失](/personal-site-mvp/img/doc-placeholder.svg "2D风格-特征丢失")
![MC风格-完全被原图风格影响，没有迁移](/personal-site-mvp/img/doc-placeholder.svg "MC风格-完全被原图风格影响，没有迁移")
banana pro

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
🍌 Tips：在banana2发布后，我们经过测试发现其生成质量不输pro，生成成本降低并且速度更快，立刻进行了替换



#### 2.2.2.生成策略-从单点到矩阵排列
在制作前，我们测试发现，在同等风格 Prompt 下，“单张图内生成多个表情”的效果远优于“单张图只生成一个表情”。

* **单图单表情（传统模式）：** AI 容易在每一轮生成中产生风格偏移，IP 形象稳定性差，导致成套表情包的画风割裂，后期调整成本极高。
* **单图多表情（矩阵模式）：** 在同一张画布内，AI 会倾向于维持视觉元素的统一性，并且对比单次生成能够极大减少生产时间，加快生成速度，节约生成成本

![单点生成](/personal-site-mvp/img/doc-placeholder.svg "单点生成")
❌ IP 跑偏概率大，风格差异明显，生成结果无法组合成一套使用，需大量后续调整。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


✅ 画风统一、IP 识别稳定，生成结果可直接组合使用，大幅降低后续调整成本。



* **定量实验——寻找AI生成的“黄金分割点”**

为了确定单图承载的最佳容量，我们针对 4、8、16、24 个表情的生成效果，在质量，画风，趣味度，效率进行了多维对比：

||单图质量|画风不稳定性|出图效率|成图率|重复度（多次生成）|部分图片展示|
|-|-|-|-|-|-|-|
|单图4个|较高，少低模感 ⬆️|24%|低|28%|35%|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|单图8个|较高，少低模感 ⬆️|18%|高|35% ⬆️|25% ⬆️|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|单图16个|较低，细节丢失|15%|很高|22%|30%|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|单图24个|低|13% ⬆️|非常高 ⬆️|17%|45%|![](/personal-site-mvp/img/doc-placeholder.svg "")|

最终综合出图质量、生产效率与防重复表现，**“单图 8 表情”** 被确立为 Genmoji Studio 的标准生产方案。



#### 2.2.3.提示词构建-多维度prompt构建优质效果
表情的难点就在于用户的图片输入内容多样，且不可控，而我们需要设计一套完整的prompt来进行适配



**为了解决这个问题，在prompt设计上采用了多维度构建的方式，将整体的prompt分为五层**

# **风格转换**
# **多样化构建**
# **IP保护机制**
# **严格边界定义**
# **后处理**


##### ✨ 风格转换——从文本驱动到“Prompt + 垫图”双约束
——prompt选择过往设计Genmoji的常用指令进行调整迭代



在 Genmoji 早期测试中，我们发现单纯依赖 Text Prompt 存在较高不确定性。

因此，在流程设计中我们引入「垫图」作为视觉锚点，通过“文本约束 + 视觉约束”的方式加强风格控制，并基于业务已有模板，沉淀出 6 类核心风格方向。

---

**垫图选择与问题发现**

* 批测中发现，AI 在部分情况下无法稳定区分“用户图”与“垫图”
* 当垫图角色信息过强（例如纯色背景 + 单一主体占比过大）时，会导致模型向垫图风格过度偏移
* 拼贴元素过多时，容易被 mix 进最终结果，影响主体表达

![❌拼贴风过多猫咪，有概率会mix到最终结果](/personal-site-mvp/img/doc-placeholder.svg "❌拼贴风过多猫咪，有概率会mix到最终结果")
**优化策略**

针对上述问题，我们进行了多轮迭代：

* 优化垫图结构，控制主体占比与背景复杂度
* 逐字调试 Prompt 描述，减少模糊形容词
* 统一每一类风格对应的标准化 Prompt 模板
* 固定「标准 Prompt + 迭代垫图」的组合形式



**最终实现：👉 风格表达一致 👉 批量生成稳定 👉 多样性与可控性兼顾**

⬇️ 部分案例 ⬇️

![](/personal-site-mvp/img/doc-placeholder.svg "")
【严格参考以下图片的画风风格，仅学习其艺术风格，不复制内容】学习苹果 ios 系统表情风格，将prompt中指定的人物生成为此风格的3D emoji小人。模仿形体、脸型、肤色、发饰，服装、配饰并保持一致。确保真人形象特色的识别度和圆润感的画风。背景白底，不要描边，只要完整人物。

![](/personal-site-mvp/img/doc-placeholder.svg "")
【严格参考以下图片的画风风格，仅学习其艺术风格，不复制内容】用立体块概括模仿形体，脸型，肤色，五官表情。色彩随机由同色的不同明度小正方形组成。不要投影，柔和阴影，背景白底，不要黑色描边，不要像素化。边缘保持浅色，只要完整主体。



##### ✨ 多样化prompt构建——打破 AI 的“创意舒适圈”
在实践过程中发现，在没有强制prompt的情况下，AI更倾向于安全的生图方式，这就导致生成多轮之后AI不会再额外进行创意实现，不同批次产出的表情重复度高、动作单一，缺乏趣味度



为此，我们思考了两个方案

* 提示词穷举，但是限制太大，没办法全覆盖；
* 纬度组合，让AI在不同维度之间组合，形成差异

最终选择 ⬇️

### **【7个多样性约束维度】**
### **维度 1：情绪类型**
Emotion Category

预先定义一个情绪池

* 开心类：开心 / 得意 / 期待
* 负面类：委屈 / 生气 / 崩溃
* 社交类：害羞 / 尴尬 / 无语
* 功能类：疑问 / 同意 / 拒绝

### **维度 2：情绪强度**
Emotion Intensity

* Level 1：平静 / 中性
* Level 2：轻微情绪（微笑、轻惊讶）
* Level 3：明确情绪（大笑、哭）
* Level 4：夸张情绪（爆哭、狂喜）
* Level 5：极端 / meme 级

### **维度 3：动作维度**
Action / Gesture

决定了 emoji 的“叙事性”。

* 无动作（纯表情）
* 面部动作（眨眼、吐舌）
* 手部动作（比心、挥手、捂脸）
* 全身姿态（跳跃、趴下）

### **维度 4：朝向与构图**
Pose & Orientation

限定几个安全角度：

* 正面
* 3/4 侧脸
* 轻微仰视
* 轻微俯视

### **维度 5：道具参与度**
Prop Involvement

* Level 0：无道具
* Level 1：轻道具（爱心、汗滴、星星）
* Level 2：功能道具（手机、咖啡、礼物）



### **维度 6：道具多样性**
PROP DIVERSITY

每个表情符号都必须有不同的和主题对应的道具



### **维度 7：外观多样性**
APPEARANCE DIVERSITY

* 服装/套装
* 配饰（眼镜、珠宝、帽子）
* 面部装饰（化妆、面部彩绘、面具）
* 发型（不同的剪裁、颜色、发饰）

```
DIVERSITY REQUIREMENTS - Ensure maximum variety across all 8 emojis in these 7 dimensions:
EMOTION INTENSITY (5 levels): Calm/Neutral → Mild → Clear → Exaggerated → Extreme
EMOTION TYPE (4 categories): Positive / Negative / Social / Functional
ACTION DIMENSION (4 types): No action / Facial action / Hand action / Full body posture
CAMERA ANGLE & COMPOSITION (4 types): Front-facing / 3/4 side profile / Slight upward / Slight downward
PROP INVOLVEMENT: Some with props, some without
PROP DIVERSITY: Different prop types when props are present
APPEARANCE DIVERSITY: Each emoji must have different combinations of clothing/outfits, accessories (glasses, jewelry, hats), facial decorations (makeup, face paint, masks), and hairstyles (different cuts, colors, hair accessories)

CRITICAL: All 8 emojis must be COMPLETELY DIFFERENT from each other in ALL 7 dimensions above, but the CHARACTER IDENTITY must remain 100% consistent with the IP reference image(s) (if provided).
```


经过多样化prompt后，AI每次出图都会在7个维度中随机选择匹配，最终出图率和有趣程度直线上升

![❌ 重复性较高，表情姿势去趋向于稳定](/personal-site-mvp/img/doc-placeholder.svg "❌ 重复性较高，表情姿势去趋向于稳定")
![同样prompt下更丰富](/personal-site-mvp/img/doc-placeholder.svg "同样prompt下更丰富")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### ✨ IP保护机制——减少信息干扰
这一块主要解决是在复杂的业务需求下，AI 常面临的多重信息干扰；

在genmoji生成平台；

当 PM 上传一张“戴墨镜、比例夸张”的非标参考图并命名为 布丁狗 时，AI 会在「脑海里的标准形象」与「眼前的非标参考图」之间反复横跳，导致产出物既不符合标准 IP 特征，也未还原参考图细节。

![平台操作会有角色命名](/personal-site-mvp/img/doc-placeholder.svg "平台操作会有角色命名")
![IP传图](/personal-site-mvp/img/doc-placeholder.svg "IP传图")
![❌生成四不像](/personal-site-mvp/img/doc-placeholder.svg "❌生成四不像")
**所以这里我们针对这个情况设计了专门的IP识别模式，给AI传递要以用户给予的形象为唯一标准。**

|模式A - 只有名字无参考图：|【IP 识别模式】IP RECOGNITION MODE: KNOWN CHARACTER (NAME-ONLY)|The character name "{角色名}" refers to a widely known IP.The model must strictly follow the most canonical, globally recognized visual design of this character.Do NOT reinterpret, redesign, or localize the character.Do NOT merge with any other similar characters.|
|-|-|-|
|模式B - 知名角色+参考图：|【IP 识别模式】IP RECOGNITION MODE: KNOWN CHARACTER WITH VISUAL OVERRIDE|Although the character "{角色名}" is widely known, the provided IP reference image(s) are the FINAL and OVERRIDING authority.If there is any discrepancy between your internal knowledge and the reference images, ALWAYS follow the reference images.Do NOT blend, average, or 'improve' the character design.|
|模式C - 原创/未知角色：|【IP 识别模式】IP RECOGNITION MODE: UNKNOWN OR ORIGINAL CHARACTER|The character is NOT a known public IP.You must treat the provided reference image(s) as the ONLY source of truth.Do NOT invent, beautify, stylize, or complete missing details.If a detail is unclear, preserve ambiguity rather than making assumptions.|

📱 Tips：在后续业务上线中因为不存在角色命名问题，这一块我们就只保留了对于形象的识别和优先级



##### ✨ 严格的边界定义——明确边界与规则
随着风格、IP、切图等 5 类指令叠加，风格与角色会发生冲突，因此制定了“身份 > 风格”的强限制边界规则；

确定优先级，并要求AI执行具体的检查清单，清楚告诉AI哪里时不能够修改的，哪里是可以被风格影响的，在多样化的同时保留角色的特征，

|【优先级1 - 角色形象基础（强限制）】CHARACTER IDENTITY REQUIREMENTS:|The IP character reference image(s) provided below are the PRIMARY and STRICT visual reference for the character's complete appearance. You MUST maintain 100% consistency with the character's face, hair, body proportions, and distinctive features across all 8 emojis.|
|-|-|
|【优先级2 - 画风转换（强限制）】STYLE TRANSFORMATION REQUIREMENTS:|After establishing the character identity from the IP reference, apply the art style from the style reference image.|
|【严格边界规则】STYLE vs IDENTITY BOUNDARY:|Style MUST NOT affect:Head shapeFacial proportionsEye placement and shapeBody ratio and proportionsAny distinctive character featuresIf style conflicts with character identity, character identity ALWAYS wins.CRITICAL: Any style/theme images must NOT change identity traits. Only change rendering technique (shading, line style, color treatment), never change WHO the character is.|



##### ✨ 后处理——图片排列与规范逻辑
此前，一次性生成8个表情解决了生成稳定性问题，但带来了新的问题：**AI 生成的位置具有随机性，导致后端无法自动裁剪或裁歪****。**

![裁剪不准](/personal-site-mvp/img/doc-placeholder.svg "裁剪不准")
为此我们针对生成设计了 **切图 Prompt 模块**

通过布局约束 (Layout Constraint) 明确布局（4×2网格）、尺寸规范、切割方式，搭配对应垫图，确保批量出图后可直接切割、导出。

### **1. 模块划分**
强制 AI 在固定坐标区域内生成内容

### **2. 自裁剪**
我们把坐标参数给到AI，让系统能够根据预设的坐标参数，对生成后的大图自动物理切割

### **3. 单体化**
被切割后的单体表情自动填充至编辑框中，转化为可独立微调、导出的标准化资源



最后，为了避免不同类型的指令相互污染，我们将 3 张垫图 —— 风格图，用户图，切割样本 的使用逻辑规范化：

```
[FINAL EXECUTION STEPS]
1. Analyze [Image 1] to understand the character.
2. Analyze [Image 2] to understand the rendering technique.
3. Analyze [Image 3] to understand the position/size of each emoji.
4. Generate the final image combining these elements.
```


### **✨ 最终prompt组合 ✨**
用户prompt+风格prompt+固定 prompt

```
🚨 ABSOLUTE REQUIREMENT 🚨
You MUST generate EXACTLY 8 emojis arranged in a 4×2 grid layout:
- Row 1: [Emoji1] [Emoji2] [Emoji3] [Emoji4]
- Row 2: [Emoji5] [Emoji6] [Emoji7] [Emoji8]

DO NOT generate 9, 10, or any other number of emojis. ONLY 8 emojis in 4 columns × 2 rows.

[INPUT IMAGE ROLES]
1. First Image: CHARACTER REFERENCE (Source of Truth for identity/face/hairstyle).
2. Second Image: STYLE REFERENCE (Source of Truth for art style/rendering).
3. Third Image: LAYOUT REFERENCE (Source of Truth for 4×2 grid structure).

[MANDATORY LAYOUT SPECIFICATIONS]
🚨 NON-NEGOTIABLE GRID STRUCTURE:
- EXACTLY 4 emojis in the TOP ROW (horizontally aligned)
- EXACTLY 4 emojis in the BOTTOM ROW (horizontally aligned)
- Total: EXACTLY 8 emojis (4+4=8)
- Each emoji must be EQUAL SIZE and EQUALLY SPACED
- Grid must be PERFECTLY RECTANGULAR with ALIGNED rows and columns

❌ ABSOLUTELY FORBIDDEN LAYOUTS:
- 3×3 grid (9 emojis) - WRONG
- 2×4 grid (2 columns, 4 rows) - WRONG
- 5×2 grid (10 emojis) - WRONG
- Irregular/scattered layout - WRONG
- Any layout with more or fewer than 8 emojis - WRONG
- Any layout that is NOT 4 columns × 2 rows - WRONG

✅ CORRECT LAYOUT VISUALIZATION:
[Emoji1] [Emoji2] [Emoji3] [Emoji4]  ← Row 1 (Top)
[Emoji5] [Emoji6] [Emoji7] [Emoji8]  ← Row 2 (Bottom)

[TECHNICAL SPECIFICATIONS]
- Dimensions: 1456px wide × 736px tall (LANDSCAPE, width > height)
- Background: PURE SOLID WHITE (#FFFFFF)
- Emoji spacing: Evenly distributed with equal gaps
- DO NOT copy grid lines, markers, or any reference elements from the layout image

[STYLE INSTRUCTION]
Style: %s

[CONTENT THEME]
Theme/Subject: %s

[DIVERSITY & VARIATION RULES]
Ensure maximum variety across all 8 emojis in these 7 dimensions:
1. EMOTION INTENSITY (5 levels): Calm/Neutral → Mild → Clear → Exaggerated → Extreme
2. EMOTION TYPE (4 categories): Positive / Negative / Social / Functional
3. ACTION DIMENSION (4 types): No action / Facial action / Hand action / Full body posture
4. CAMERA ANGLE & COMPOSITION (4 types): Front-facing / 3/4 side profile / Slight upward / Slight downward
5. PROP INVOLVEMENT: Some with props, some without
6. PROP DIVERSITY: Different prop types when props are present
7. APPEARANCE DIVERSITY: Each emoji must have different combinations of clothing/outfits, accessories (glasses, jewelry, hats), facial decorations (makeup, face paint, masks), and hairstyles (different cuts, colors, hair accessories)

[CRITICAL]
All 8 emojis must be COMPLETELY DIFFERENT from each other in ALL 7 dimensions above, but the CHARACTER IDENTITY must remain 100%% consistent with the IP reference image.

[STYLE vs IDENTITY BOUNDARY]
Style MUST NOT affect:
* Head shape
* Facial proportions
* Eye placement and shape
* Body ratio and proportions
* Any distinctive character features

If style conflicts with character identity, character identity ALWAYS wins.
CRITICAL: Any style/theme images must NOT change identity traits. Only change rendering technique (shading, line style, color treatment), never change WHO the character is.

[FINAL EXECUTION STEPS]
1. Analyze [Image 1] to understand the character.
2. Analyze [Image 2] to understand the rendering technique.
3. Analyze [Image 3] to understand the position/size of each emoji.
4. Generate the final image combining these elements.
```


#### 2.2.4 反馈收集——从实践中不断获得反馈
我们在做的时候，并不需要一次性的100分，只要跑通核心MVP就会进行小范围的内部测试；

让 AI 进行上线部署，使用本地MAC作为服务器实现内网上线，发给感兴趣的PM&设计同学，直接从实际体验中拿问题并不断调优解决，最终形成现在的生成方案

![](/personal-site-mvp/img/doc-placeholder.svg "")
问题收集文档——[优化建议](https://ku.baidu-int.com/d/ovjuopaWxdO-7F?t=mention&mt=doc&dt=datasheet)；❤️ 这里非常感谢参与了测试的同学 ❤️

****

# ✨ 在新流程下对我们对Genmoji的生产效率进行了真实业务场景下的验证 ✨
⚡️**出图效率提升超**

500%

2–3 工作日 → 

**分钟级生成 + 少量调整**

🛡️**稳定性提升**

90%

依赖“会不会和 AI 聊” → 

**结果可控、批量一致**

📉**修改成本降低**

50%

多轮描述/反复改稿 → 

**需求即生成条件**

💬**沟通成本降低**

80%

5-8 次 → 

1 次需求输入

# 3 从效率工具转为产品功能MVP上线
genmoji效率工具在开放测试中得到了非常好的反馈，**内部同学发挥自己创意想法把Genmoji工具玩出了新的花样，并获得了内部传播**

内部同学测试使用效果

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


### 3.1. 线上MVP流程设计
❤️感谢佳虹姐给了Genmoji生成直接上线进行MVP测试的机会，年前genmoji生成功能在FMJ iOS端上线，设计同样直接参与到产品设计中

**MVP设计稿**

构建合理的进入路径，把优质结果展示给用户，吸引用户点击尝试，目标测试用户对于功能的付费意愿，拿到数据后再进行优化

**AI参与产品设计流程**

在实际设计过程中优先使用figma make来进行交互方式的快速构建，与pm在交互上快速达成一致

中间在边界case设计&文案设计&流程设计 中遇到不确定问题则直接发给GPT来进行辅助判断

![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


### 3.2.AI实现设计制作👉测试自闭环
在上线前，我们需要对生成进行批测，保证当前方案的生产结果在用户侧有足够的稳定性

利用 Cursor + 自然语言交互，UE 侧独立完成了从后台跑批脚本到前端可视化控制台的全链路开发，实现了测试验证的自主化与即时化，打破了以往“UE 提需求 → RD 写脚本 → UE 等结果”的被动模式。

**Before：**

—— 在此前我们做表情的时候，批测需要rd同学来进行参与，并把结果给到设计来判断

**After**：

—— 在API连接问题上和服务端同学协同，只需要告诉AI我们的需求即可实现 Cursor 构建脚本进行自测，终端可以直接看到任务进展和数量等相关信息；

我们在这一步让AI根据 照片/风格/prompt 自动创建层级目录 `output/{imageName}/{styleName}/prompt_{x}/`，将图片按逻辑归档，方便后续的对比验收；

![](/personal-site-mvp/img/doc-placeholder.svg "")
—— 图片量级快速比对：Cursor一句话就能快速构建可视化的网页前端的页面，不用再一个个文件夹翻找比对，UE能够直接进行问题定位

![生成结果1200+，但是AI能快速归类](/personal-site-mvp/img/doc-placeholder.svg "生成结果1200+，但是AI能快速归类")
测试结果展示【局域网】：[http://172.18.166.177:8080/results_comparison.html](http://172.18.166.177:8080/results_comparison.html)

测试总结【感兴趣可看】：[【genmoji】批测结论](https://ku.baidu-int.com/d/CZ1a1-g673RnGB?t=mention&mt=doc&dt=doc)



# 4.总结
随着新模型的发布以及线上结论回收，我们也在不断的对 genmoji 方案进行调整，目标能够成为产品的新卖点

Genmoji 生成工具的构建与上线，不只是一次功能探索，更是一次 AI 思维落地的实践。

设计的价值不再局限于设计图的制作，而是能够通过理解模型能力、拆解流程结构、重构生产方式，建立一套属于自己的能够串联的工作方式；我们完成的不仅是工具搭建亦或是功能上线，更是工作方式的升级。

未来对于genmoji我们也在思考是否能够通过AI的方式实现自动化运营，提高功能外部曝光，实现设计参与的全闭环。



**鸣谢所有参与的大家·FMJ UE全体至上**





# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
