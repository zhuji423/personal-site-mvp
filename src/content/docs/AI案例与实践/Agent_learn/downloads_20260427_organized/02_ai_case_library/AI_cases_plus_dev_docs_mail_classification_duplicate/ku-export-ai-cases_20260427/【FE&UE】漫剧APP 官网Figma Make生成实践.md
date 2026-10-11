---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "【FE&UE】漫剧APP 官网Figma Make生成实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\【FE&UE】漫剧APP 官网Figma Make生成实践.md"
---
【FE&UE】漫剧APP 官网Figma Make生成实践

#### 🧑‍🏫 案例作者：[@王桃峰](https://ku.baidu-int.com?t=mention&mt=contact&id=498f0820-fdaf-11f0-aa3d-c9e6fb50c0d3)
#### 🎬 案例场景：设计
#### 🔧 使用工具：Figma
#### 📒 案例概要：本文围绕Figma Make在漫剧APP官网搭建中的应用，介绍了研发模式、协同过程、成本提效、问题及优化思考，助力团队高效利用AI生成高质量前端代码。

## 背景与目标
* **背景**：探索基于 Figma Make（AI Code生成工具）的全新研发模式，旨在减少重复性切图与布局工作。
* **现状**：在“官网搭建”项目中试运行，整体研发提效显著（开发周期 6pd => 2pd），但在模型能力边界、上下文理解及跨职能协作上仍存在一些痛点。
* **目标**：建立一套标准化的 UE/FE 协作SOP，明确双方职责边界，最大化 AI 生成代码的可用性。

## 协同过程
> 详细记录见**附录**
#### 概览
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 前置准备 (FE 主导)
在开始生成代码前，前端需明确技术基准，从源头规避架构风险。

* **技术栈锁定**：统一使用 React + Tailwind CSS。明确禁止引入 Next.js 等非必要框架。
* **输出基准 Prompt**：前端需提供标准提示词模板，包含以下核心逻辑：
    * **视口适配**：禁止使用 `100vh`，强制采用 `calc(var(--vh, 1vh) * 100)` 以兼容移动端。
    * **响应式断点**：PC 端基准宽度 1440px，移动端 414px。
    * **资源加载**：动效限定使用 `transform/opacity`；大图必须开启 Lazy Loading。


> **🔧 通用技术 Prompt 模板：**
```
### 精密视口与高度适配 (Engineered Viewport Logic)

* **PC 优先架构：** 以 **1440px** 为核心设计基准。默认样式即为 PC 端，通过 `max-width` 断点向下兼容。
* **动态高度计算 (Dynamic Calc)：** \* **禁止**使用 `100vh` 或 `100%` 处理全屏容器。
  * **实现方案：** 必须通过计算逻辑（如监听 `resize` 结合 `requestAnimationFrame` 或使用现代 CSS 变量注入）动态更新 `--vh` 单位。
  * **公式应用：** 容器高度应通过 `calc(var(--vh, 1vh) * 100)` 实现，确保在移动端动态工具栏伸缩时，布局能进行精密重绘或保持稳定，避免内容被遮挡或溢出。
* **比例锁定：** 核心展示组件优先使用 `aspect-ratio` 配合 `calc()` 进行自适应缩放，而非硬编码高度。
* **存量优化：** 会影响整体高度内容区域, 检查并优化不符合要求的100vh
```
```
### 动效性能与 DOM 生命周期 (State-Driven Lifecycle)

* **非视口静默策略 (Off-screen Silencing)：**
  * **目标：** 不在当前视口内的元素，其计算逻辑（如 JS 循环、Canvas 渲染、高频计时器）必须**彻底挂起**。
  * **DOM 优化：** 在不破坏进场/退场动画连贯性的前提下，利用**状态驱动渲染**（State-driven rendering）。当元素处于“非活跃且无过渡动画”状态时，尽可能将其从 DOM 树中移除，以减轻内存压力和浏览器的层合成负担。
* **动效解耦：** 动效实现需与业务逻辑解耦，支持“动画预判”。通过组件的生命周期钩子（如 `useEffect` 销毁函数或 `cancelAnimationFrame`）**确保没有任何无效的后台计算在静止页面上运行。确保不影响现有的动效及显示效果**
```
### 生成与迭代 (UE 主导)
UE 负责利用 AI 进行视觉还原，重点把控生成效率与视觉精度。

* **分模块生成**：禁止整页一次性生成。需按“首屏”、“列表区”、“底部”等模块分批产出，以降低上下文丢失风险。
* **自然语言微调**：通过自然语言（如调整间距、动画速率）优化视觉细节。
* **熔断机制**：若同一布局问题（如错位、遮挡）经 **多次迭代** 仍未修复，**应立即停止尝试**，转交 FE 处理，避免无效消耗。

### 代码验收与重构 (FE 主导)
前端介入解决 AI 无法处理的逻辑问题。

* **结构修正**：
    * 接管复杂的 Flex/Grid 自适应布局逻辑。
    * 修复层级上下文（Stacking Context）导致的 z-index 遮挡问题。

* **代码清洗**：
    * 移除 Figma Make 生成的冗余 Context 和工具函数。
    * 检查并补充 `useEffect` 的清理函数，防止内存泄漏。
    * 修复异形屏（刘海/灵动岛）遮挡及极端宽窄屏的布局异常。


## 总结与思考
### 成本&提效
从研发角度评估，粗估如果采用传统全人工开发+走查成本：5pd开发+1pd走查，采用figma make生成后的成本：1pd协同UE调试Prompt+1pd代码适配。整体开发周期从6pd到2pd，提效67%；

官网项目无历史包袱，且整体比较重交互和动画，故提效较为明显

### 遇见的问题
#### 模型能力边界
* figma make使用通用大语言模型 (Claude/GPT), 模型上下文长度有限, 如连续对话过多, 上下文太长时, 生成的结果很多都与其描述不符
* 无法进行有效的rules限制、全局上下文定义，且UE可能并没有太多技术栈相关的感知，依赖研发侧输出，但很多背景为黑盒，无法完全cover，如使用的npm包版本，对其他组件库/图标库的依赖（@radix-ui/react-slot，lucide-react）

#### UE/FE职责问题
目前来说, 这次是尝试使用figma make整体落地, 相当于生成一套直接可用的代码

但对于UE/UI来说, 如适配, 性能, 兼容这块, 可能不太有这个层面的感知, 这块就需要FE辅助, 但figma make生成的代码为黑盒, 有时候改个问题会涉及到整体结构的改动, 这种就不是FE调优来解决, 应该是在初期, 在提示词里尽量的避免

UE/UI更专注动效和还原视觉的处理, 对于一些bug问题/细节优化修改, 如之前反馈标签部分图太小, 这点其实可以FE直接修改, 也不需要花费token

但, 代码整体结构, FE无法控制, 由figma make生成的, 怕生成的想要改好需要很大工作量, 所以其实可以在生成的时候, 限制一下它的质量, 给点提示词这种

总结来说, 对于复杂的页面:

* 前置需限制好页面整体框架, 可通过prompt的方式, 避免后续堆积过多FE难以修改
* UE关注动效. 视觉还原, 基本适配能力
* FE关注性能, bug, 适配细节优化

#### 协同问题
当前尝试时协同流程如下

![](/personal-site-mvp/img/doc-placeholder.svg "")
其中主要的问题是, 在一些细节/bug/未知原因无法符合预期时, 需要FE辅助, 但双方交互的方式目前比较繁琐, 如上图中虚线框内(**FE无figma make编辑权限/付费**)

主要协作有以下三点

1. FE现场在UE的figma make上修改调试
2. FE保存对话到草稿. 通过提示词的方式让figma make修改, 完成后输出提示词
3. UE导出代码给FE, FE进行修改. 修改后让UE在figma make上同步修改
4. 细节部分UE找到对应代码位置, 通过其他通用大模型进行修改, 如修改元素的宽高/大小/位置等

上述协作方式实际都比较繁琐, 可以有以下的一些优化方式

* FE/UE共用一个figma make, 双方均有编辑能力
* 给UE输出一些简单的元素知识, 如怎么在代码中定位到元素, 后续的修改可以通过通用大模型进行(一般修改比较简单, 如改变大小/位置等)



### 思考
——能否提供一些常用的代码快捷微调方法，常用语法教学？例如一些边距、元素大小、动效参数等，UE微调时更快捷也避免过度消耗token？

* 多层级结构, UE无法选中要改的部分, 可以通过命名的方式, 即给每个模块的组件, 让AI命名并告知, 这样修改时, 就知道要改哪部分
* 对于多页面, 多页面联动时, 可以事先从整体上梳理, 有几个页面, 页面间切换效果, 随后再一一补充细节，这样的好处是, 事先可以整体有个好的代码架构, 细节部分补充不会改变整体架构，而一页一页的让AI去加, 可能会做一页会影响到之前的页面, 或者整体的页面架构, 因为在没有做下一页的时候, 是不知道上下间的关联, 代码里也不会从整体去做
* UE同学专注于样式还原和动效生成, 至于一些性能问题, 边界case, 可能出现的bug之类的, fe配合去排查测试及修改, 如100vh在手机端需要计算, 部分PC弹性滚动导致bug等问题

### 总结
figma make生成代码对于**重交互动画无历史包袱**的项目而言有**明显提效（6pd->2pd）**，但是能力仍存在边界, 对于多页面/复杂页面, 难以完全通过UE/RD一方完成代码输出直接可用，需要根据项目复杂程度确定不同的协作方式

* 对于**复杂**的页面或项目, 可以拆分不同模块或者组件, UE负责关键模块动效, 输出模块或者组件的动效代码：
    * 相对独立的组件和模块，FE可以直接采用生成代码导入到现有项目中；
    * 与现有复杂项目耦合性较重的，FE可以将生成的动效部分为参考输入给coding Agent，结合本项目的上下文适配到项目中；

* 对于**结构简单/单页面**来说, 可以尝试figma make整体生成，但整体生成流程需要UE和RD协同进行优化，包括但不限于：
    * 生成前：RD先输入一部分技术要求如技术栈、移动PC多机型适配等要求，UE在此上下文下对figma make效果进行调试；
    * 生成后：RD基于生成代码进行性能调优以及一些边界case的优化；








## 附录
**UE文档: **[柚漫剧动态官网搭建](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/zr9SzkF3c9/hjCZ7mrlVX/b_txIXlFA0X5F7?t=mention&mt=doc&dt=doc)

### UE交付前FE工作
#### 输出/沉淀提示词
> 研发基于项目背景, 可能出现的问题, 提供了一套提示词, 如当前为官网, 有动效, 需要做屏幕适配
由于提示词应用过晚, 应该在初始时就需要把要求加入, 项目完成后再加入的话, 会出现**修改遗漏**的case

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
```
### 精密视口与高度适配 (Engineered Viewport Logic)

* **PC 优先架构：** 以 **1440px** 为核心设计基准。默认样式即为 PC 端，通过 `max-width` 断点向下兼容。
* **动态高度计算 (Dynamic Calc)：** \* **禁止**使用 `100vh` 或 `100%` 处理全屏容器。
  * **实现方案：** 必须通过计算逻辑（如监听 `resize` 结合 `requestAnimationFrame` 或使用现代 CSS 变量注入）动态更新 `--vh` 单位。
  * **公式应用：** 容器高度应通过 `calc(var(--vh, 1vh) * 100)` 实现，确保在移动端动态工具栏伸缩时，布局能进行精密重绘或保持稳定，避免内容被遮挡或溢出。
* **比例锁定：** 核心展示组件优先使用 `aspect-ratio` 配合 `calc()` 进行自适应缩放，而非硬编码高度。
* **存量优化：** 会影响整体高度内容区域, 检查并优化不符合要求的100vh
```


![](/personal-site-mvp/img/doc-placeholder.svg "")
```
### 动效性能与 DOM 生命周期 (State-Driven Lifecycle)

* **非视口静默策略 (Off-screen Silencing)：**
  * **目标：** 不在当前视口内的元素，其计算逻辑（如 JS 循环、Canvas 渲染、高频计时器）必须**彻底挂起**。
  * **DOM 优化：** 在不破坏进场/退场动画连贯性的前提下，利用**状态驱动渲染**（State-driven rendering）。当元素处于“非活跃且无过渡动画”状态时，尽可能将其从 DOM 树中移除，以减轻内存压力和浏览器的层合成负担。
* **动效解耦：** 动效实现需与业务逻辑解耦，支持“动画预判”。通过组件的生命周期钩子（如 `useEffect` 销毁函数或 `cancelAnimationFrame`）**确保没有任何无效的后台计算在静止页面上运行。确保不影响现有的动效及显示效果**
```


#### 辅助代码生成/排查问题
1. 提示词使用技巧

![](/personal-site-mvp/img/doc-placeholder.svg "")
2. 表现不符合预期, 模型难以理解和解决问题
    1. 画廊多余空白bug，fe排查，需要ue替换图片以及更新布局


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
b. 画廊逻辑问题，该消失时不消失，fe找到逻辑问题并告知ue修改

![](/personal-site-mvp/img/doc-placeholder.svg "")
3. 提供提示词快速帮ue修改不符合预期的动画

![](/personal-site-mvp/img/doc-placeholder.svg "")
4. 如何在复杂的上下文中选中元素

![](/personal-site-mvp/img/doc-placeholder.svg "")
5. activePage切换时, 让最后一页的顶部效果回到第一页的效果, 以及视频列数无法在最后一页消失, UE通过figma make修改尝试困难/无法达到预期, FE排查和修改逻辑

![](/personal-site-mvp/img/doc-placeholder.svg "")
6. 选中组件局部修改有限: 颜色, padding, margin, border, 其余的如动画效果, 位置, 层级等, 需要定位到代码部分进行修改, 但对于UE来说, 代码修改不是很合适, FE配合辅助修改

![](/personal-site-mvp/img/doc-placeholder.svg "")
具体方式如下

    * FE直接同步UE修改, 适合简单的修改, 如想要修改某个元素的大小/布局
    * UE定位到元素, 借助其他通用大模型进行简单修改, 如修改元素宽为40, h-[30px] => h-[40px]
    * 元素难以定位. UE通过提示词定位并修改. 如若提示词无法定位. FE根据元素特征修改提示词, 如右上角图片 => topRightMask
    * 判断比较复杂的元素修改, FE通过代码判断是直接代码层面修改, 还是提供一个定位到元素的详细的修改的提示词

#### 协作流程探索
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### prompt调试
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 对比zulu/f2c
> **以UE视角, 即不去手动修改代码, 不参与从代码逻辑层面反推模型的query**
|页面|最终效果|迭代|总结|
|-|-|-|-|
|整体滚动框架|[附件]|使用Claude 4.5, spec模式生成, 整体框架效果基本符合, 一些滚动细节部分需要优化下![](/personal-site-mvp/img/doc-placeholder.svg "")修复滚动切换问题, 对话了3次, 第一次无效果, 第二次加了防抖, 导致停止滚动才切换, 第三次修改才正常![](/personal-site-mvp/img/doc-placeholder.svg "")|从整体上搭个架子的话, ai coding能力还是挺好的, 细节部分可以慢慢调优|
|首页|[附件]|初版, 依旧使用spec生成, 逻辑基本能实现, 但样式有较大差异![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")第二版, 优化细节, 依旧spec, 依旧样式还原问题, header细节logo+描述的细节还原不行![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")切换到f2c, 经历了两次修改后基本还原![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|对于页面整体, spec可以准确的完成其逻辑和结构部分但对于设计稿的精细化还原, f2c效果会好一些, 但注意需要**标注好模块进行单一处理**|
|第二屏|同上录屏|**版本迭代次数过多, 拿主要部分进行记录**首次基本完全忽略提示词随心发挥, 大小, 位置, 动画等均无关联![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")随后不断的重复修改n次, 仍是布局大小混乱, 对于画廊部分, 仅布局就难以实现(实际就横向排列, 铺满), 要么自己给定宽, 要么定高, 要么定最大宽, 最大高..., 如图, **最终自己手动添加flex: 1, 删除height**![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")关于层级问题, f2c和zulu始终无法理解或正确处理, 即使告诉了不在同一个层叠上下文内, 还会保持去不断的修改z-index, 最后**人工 + zulu**的方式去改为正确的结构![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|对于页面中分层的情况, 无法准确的理解层叠上下文, **会出现重复去改明确告诉了不会生效的内容**|
|首屏new|![](/personal-site-mvp/img/doc-placeholder.svg "")|尝试详细提示词 + rules + f2c上下文 + 分模块Role: 你是一位顶级前端架构师，擅长将 Figma 设计稿转化为高性能、自适应的响应式代码（React + Tailwind CSS + motion）。

-   **命名要求, 每次新增的组件或者图片等, 都需要回复我名称, 便于我后续告诉你需要修改什么位置**
-   **图片资源缺失直接告诉我, 不要从 figma 上下载保存任何图片, 我会给你提供对应的图片路径, 已经提供了路劲的图片, 不要再使用 figma 上的各个元素进行拼接, 如下, 这不合理**
    {/_ 装饰性图标 _/}
    <img 
          src={logoImage} 
          alt="Decoration" 
          className="w-[21.32px] h-[22.40px] absolute top-[35.71px] left-[126.99px]" 
        />
    <img 
          src={logoImage} 
          alt="Decoration" 
          className="w-[9.94px] h-[75.39px] absolute top-[10.81px] left-[126.37px]" 
        />
    <img 
          src={logoImage} 
          alt="Decoration" 
          className="w-[9.94px] h-[75.39px] absolute top-[10.81px] left-[162px]" 
        />
    <img 
          src={logoImage} 
          alt="Decoration" 
          className="w-[9.94px] h-[64.33px] absolute top-[21.88px] left-[144.55px]" 
        />
    <img 
          src={logoImage} 
          alt="Decoration" 
          className="w-[12.54px] h-[53.83px] absolute top-[32.38px] left-[111.78px]" 
        />
    <img 
          src={logoImage} 
          alt="Decoration" 
          className="w-[16.36px] h-[62.46px] absolute top-[23.94px] left-[173.14px]" 
        />
-   **不要使用 nextjs**

-   核心适配基准 (Layout Foundations)
    PC 端基准：

最大宽度约束： 主内容区限制 max-width: 1440px 并水平居中。

超宽屏缩放： 当屏幕宽度 > 1440px 时，内容区保持居中，两侧留白或背景延伸；禁止内容无限拉伸。

异型屏防护： 使用媒体查询确保在 21:9 或带内挖孔屏上，UI 元素不发生重叠或被切边。

移动端适配： 以 414px \* 896px 为适配基准。

高长比适配： 针对长屏设备，核心交互组件（如 CTA 按钮、导航）必须计算安全区域（Safe Area），防止在 19.5:9 或更长比例的屏幕上出现内容断档。

弹性高度： 严禁对容器使用固定像素高度，必须使用 min-h-screen 或百分比配合 aspect-ratio。

-   动效性能与模块化 (Animation & Performance)
    严禁全屏动效： 禁止使用覆盖整个视口的单一动画层。必须将动效拆解为独立模块（如：Card_A_Animation, Hero_Text_Fade）。这样可以确保在不同尺寸屏幕缩放时，动效中心点不偏移、不被裁剪。

渲染优化：

仅允许对 transform 和 opacity 进行动画，禁止操作会触发重排（Reflow）的属性（如 width, height, flex-basis）。

大型动画组件需添加 will-change: transform 提示浏览器开启 GPU 加速，但需在动画结束后移除（防止显存溢出）。

内存清理： 如果使用了 requestAnimationFrame 或自定义计时器，必须在组件 Unmount 时显式执行销毁逻辑，防止内存泄漏。

交互频率限制： 随滚动或窗口 Resize 触发的动画必须进行 Throttle (节流) 处理（建议间隔 16ms 以上）。

-   资源加载策略 (Asset Management)
    图片加载： 默认使用 loading="lazy"。严禁加载超过 500KB 的原始图，必须生成 WebP 格式并提供占位色块。

代码分割： 复杂组件需支持动态导入（Dynamic Import），确保首屏仅加载必要资源。

节点控制： 避免过深的 DOM 嵌套，单页面 DOM 节点数建议控制在 1500 个以内，以降低内存占用。

-   样式实现要求 (CSS Implementation)
    使用 Tailwind CSS 进行原子化建模。

字体大小、间距需在移动端和 PC 端之间设置合理的断点（Breakpoints），而不是简单的等比缩放。

针对 414 \* 896 尺寸下的字号，在小屏手机上需自动下调 10-15% 的比例以防溢出。
![](/personal-site-mvp/img/doc-placeholder.svg "")||

#### 性能排查
无内存泄漏, 但页面较卡

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
用于动画特效的图比较大

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
沟通后

1. 列图分列给出, 让模型排列, 给出间距, 并行加载
2. 图片导出大小改变, 压缩

### UE交付后FE工作
|内容|修改前|修改后|备注|
|-|-|-|-|
|裁剪组件, 移除不需要的引入, 只引入必要的组件|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|figma make生成时, 有较多的基于figma make自己的上下文所定义的组件和方法, 很多都是没有用到的, 需要移除下|
|移除无用资源, 减小打包体积|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|图片资源figma make在命名和引入时, 使用的都是hash值, 导致寻找困难, 是否可以在上传图片时给定命名方式|
|header与设计稿有较大差异|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|无|
|修复PC遮挡问题, 且加入适配|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|代码层面断点定义和使用比较混乱, 不太便于阅读和维护使用zulu直接跳过查找和各个屏幕的断点使用, 直接修改![](/personal-site-mvp/img/doc-placeholder.svg "")|
|修复部分设备移动端遮挡问题, 且加入适配, 各page间距统一高效搜索页丢失的mask修复联系我们在小屏幕上被遮挡|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|使用zulu, 方案和布局制定好该怎么去做, 具体重复的逻辑由ai进行![](/personal-site-mvp/img/doc-placeholder.svg "")|
|下载按钮功能支持|\|\|直接复制之前的逻辑即可|
|底部政策相关文案|\|\|直接复制之前的逻辑即可|

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
