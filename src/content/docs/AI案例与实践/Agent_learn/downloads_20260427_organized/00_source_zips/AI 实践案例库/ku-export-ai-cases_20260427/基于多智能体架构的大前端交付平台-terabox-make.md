---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "基于多智能体架构的大前端交付平台-terabox-make"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于多智能体架构的大前端交付平台-terabox-make.md"
---
基于多智能体架构的大前端交付平台-terabox-make

#### 🧑‍🏫 案例作者：PSIG-海外研发组
#### 🎬 案例分类：需求、设计、开发、测试、运维、研发全流程、运营、工作流自动化、项目管理
#### 🔧 使用工具：面向前端交付场景的 AI工作台、Onetool、iCode、Ducc、Comate、Claude、ChatGPT、Figma
#### 📒 案例概要：make 是一个面向前端交付场景的 AI 工作台
* 核心定位，通过 AI 能力压缩"从设计稿到页面上线"链路中的重复人工环节
[文档目录]
### 在线体验网站：[https://terabox-make.pages.dev/](https://terabox-make.pages.dev/)
### ppt可视化讲解：[https://cf-worker-page-publish.teraboxfe.workers.dev/publish/terabox-make-20260419151050/2026.04.19-275](https://cf-worker-page-publish.teraboxfe.workers.dev/publish/terabox-make-20260419151050/2026.04.19-275)
---

## 背景：make 在解决什么问题
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1581ee1fe38f45a080d6fa93e935f1cb&docGuid=uz7MLANZMaPAVC&sign=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiYXBwSWQiOjEsInVpZCI6IkpGd1pIbzJRbTEiLCJkb2NJZCI6IkVGaW9idllQNDBUMUR6In0..rgJTN1QXxXqQOewT.tO7IYSVa5Rqm3YEDu8qdSs2113UtcAM1oXVEY7xkkH90ld0Q6RiNKm2fycZ1FoBTlGWAeOgoQ6jsLbaAkwyWvlbsw85uvd26icV4o1ZuNKKTXSBp7xJEdMDDfMk9bzZCL3FE-Zr4KLWB4jRj8T3OiSoRVp5Cd39NDzVO6u6ztKKiVilte9JpkAgD31Q_fovBnFYYUMaE5oXFCSdiP-HhQFcTLg.BpJor2DNfTlukzKy_DdWtQ "")
make 是一个面向前端交付场景的 AI 工作台

* 核心定位，**通过 AI 能力压缩"从设计稿到页面上线"链路中的重复人工环节**

这一工具的建设背景来自 TeraBox 大前端日常**研发中的实际需求**。当前前端需要交付的页面类型较多——运营活动页（抽奖、任务中心、签到）、SEO 落地页、渠道推广着陆页、产品功能介绍页、下载引导页，以及带登录注册和支付流程的完整业务页面。这些页面的交付长期存在几个**效率瓶颈**：

**5大效率瓶颈**

**设计到开发的信息断层**

---

设计师在 **Figma** 里画好稿，前端拿到的是一张"图"，布局层级、间距数值、颜色色值、圆角阴影全靠人眼识别和手动还原，一个中等复杂度页面的**纯还原工作量**就要 3~4 天

**运营活动大量重复建设**

---

九宫格抽奖、金币任务中心、签到页这些结构几乎**每期活动**都重做一遍，每次**改的只是视觉皮肤和配置项**，但工程成本几乎等**同于新建**



**落地页交付效率低**

---

SEO 落地页、渠道推广页、产品介绍页这类页面**结构相对简单但数量大、上线节奏快**，每个页面都走**完整研发流程**不经济，但作品外包或低代码平台又做不到品牌一致性和 SEO 要求

**缺少端到端的闭环验证**

---

一个**完整的业务页面**往往需要登录态、接口对接、支付跳转等能力才算"真正可用"，但大部分 AI 工具只能生成静态展示页，缺少登录/鉴权/支付等**真实业务能力的集成**，导致 AI 产出物离"上线标准"始终隔着额外的人工环节

**AI生成的代码不能直接用**

---

市面上的 **AI 代码生成工具**能出 **Demo**，但产出的代码跟真实项目跑不通，没有校验环节，改起来全靠**人工二次拼接**

**make 即针对上述问题，在各环节逐步落地 AI 提效方案。以下按具体场景展开当前已完成的工作、技术方案及阶段性效果。**

---



## 场景一：Figma 设计稿直接生成可运行页面（figma to web）
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=591f8aff9d8f48b0be6b17d6780f7e54&docGuid=uz7MLANZMaPAVC&sign=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiYXBwSWQiOjEsInVpZCI6IkpGd1pIbzJRbTEiLCJkb2NJZCI6IkVGaW9idllQNDBUMUR6In0..rgJTN1QXxXqQOewT.tO7IYSVa5Rqm3YEDu8qdSs2113UtcAM1oXVEY7xkkH90ld0Q6RiNKm2fycZ1FoBTlGWAeOgoQ6jsLbaAkwyWvlbsw85uvd26icV4o1ZuNKKTXSBp7xJEdMDDfMk9bzZCL3FE-Zr4KLWB4jRj8T3OiSoRVp5Cd39NDzVO6u6ztKKiVilte9JpkAgD31Q_fovBnFYYUMaE5oXFCSdiP-HhQFcTLg.BpJor2DNfTlukzKy_DdWtQ "")
### 1.1 场景痛点
前端拿到设计稿后的第一件事是"翻译"——把 Figma 里的视觉语言逐属性翻译成 CSS。一个中等复杂度的运营页面（5~~8 个区块、200+ 节点），这个翻译过程至少占 **3~~4 天**。翻译本身没有创造性价值，但非常容易出错：px 像素值偏移、渐变角度算偏、阴影参数漏一个，每个细节都需要反复比对。

### 1.2 生产原链路
工程师手动交付、多次返工

设计师交付 Figma设计稿 链接 → 前端打开 Figma 逐层查看节点 → 手写 HTML/CSS 还原布局 → 切图导出 → 反复走查对比 → 修修补补上线。核心耗时在"看稿 + 手写还原"上。

### 1.3 平台新链路
端到端快速还原，零代码验证

1. 设计师在 Figma 装一个我们开发的插件 `figma-to-web`，一键导出结构化 JSON（包含节点树、样式属性、图片资源、截图）
2. 前端把 JSON 拖进 make 工作台
3. make自动遍历节点树，把 Figma 的 Auto Layout 转 Flexbox、把填充转 CSS 渐变、把效果转 box-shadow、把字号映射成语义化标签（h1/h2/p/span）
4. 直接输出一个完整的 Vue 3 SFC(网页运行时)，在浏览器里实时运行

### 1.4 关键技术方案
** 结构化导出替代截图**

---

不是给 AI 一张截图去猜，而是直接导出 Figma 节点树中的布局、样式、层级等结构化数据，让设计稿从“视觉图像”变成“工程输入”。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=058e78cad7964c7dafdf0a443072be70&docGuid=EFiobvYP40T1Dz "")


**确定性转换器（FigmaConverter）**

---

不依赖大模型猜测，而是用确定性规则把 Figma 属性精确映射为 CSS 和 Vue3 SFC，保证转换结果稳定、一致、可控。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e9a6c122337a40678528275220fd3832&docGuid=EFiobvYP40T1Dz "")
****

**图片资源自动处理**

---

将 Figma 中的图片填充和导出资源自动拆分为独立文件，并在生成代码中直接引用，减少手工整理和二次处理成本。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=222b9de4f48e4bfbbe4fed3e708d3c59&docGuid=_FPVZ0CvL6RfNJ "")
### 1.5 场景实践
##### 业务收益
---

* 一个中等复杂度的运营页面（5~~8 个区块、200+ 节点），从拿到设计稿到跑起来一个视觉基本还原的页面，时间从 3~~4 天压缩到几分钟级别。当然后续还需要调整部分细节，但"从 0 到 0.9"这一步的人工量大幅减少（下一个环节，ai修复将完成剩下的0.1的工作）。

##### 演示-从零开始还原业务设计稿
---

[附件]
---

## 场景二：Visual Diff——生成完不靠肉眼对，自动告诉你哪里不一样
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2877655803104324b82eaea821afe96b&docGuid=uz7MLANZMaPAVC&sign=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiYXBwSWQiOjEsInVpZCI6IkpGd1pIbzJRbTEiLCJkb2NJZCI6IkVGaW9idllQNDBUMUR6In0..rgJTN1QXxXqQOewT.tO7IYSVa5Rqm3YEDu8qdSs2113UtcAM1oXVEY7xkkH90ld0Q6RiNKm2fycZ1FoBTlGWAeOgoQ6jsLbaAkwyWvlbsw85uvd26icV4o1ZuNKKTXSBp7xJEdMDDfMk9bzZCL3FE-Zr4KLWB4jRj8T3OiSoRVp5Cd39NDzVO6u6ztKKiVilte9JpkAgD31Q_fovBnFYYUMaE5oXFCSdiP-HhQFcTLg.BpJor2DNfTlukzKy_DdWtQ "")
### 2.1 生产原链路/场景痛点
人工走查还原设计稿

页面写完之后，设计师和前端肉眼走查：把 Figma 稿和页面截图放在一起比，一个像素一个像素找差异，说不清楚的来回沟通。

### 2.2 平台新链路
AI自动修复

make 内置了 Visual Diff 引擎，三个阶段层层递进：

* **Phase 1 — 视觉叠加对比**：把 Figma 截图和实际页面叠在一起，提供拖拽分割线、透明度调节、闪烁切换、3D 分层四种对比方式，10 秒内看出大面上的差异
* **Phase 2 — 结构化 Diff**：引擎通过 `postMessage` 从 iframe 里采集实际 DOM 的位置和样式，跟 Figma 节点树逐一比对宽高、位置、颜色、圆角，输出结构化差异报告，每条差异标注严重程度（low/medium/high）
* **Phase 3 — AI 一键修复**：点一下，把差异报告 + Figma 截图发给 AI，让它直接改代码修复，改完自动重新 Diff 验证

### 2.3 关键技术方案
**视觉叠加对比**

---

把 Figma 截图和实际页面叠在一起，提供拖拽分割线、透明度调节、闪烁切换、3D 分层四种对比方式，10 秒内看出大面上的差异

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=49b20c5cee36451e873cefc426b457d7&docGuid=_FPVZ0CvL6RfNJ "")


**结构化 Diff**

---

引擎通过 `postMessage` 从 iframe 里采集实际 DOM 的位置和样式，跟 Figma 节点树逐一比对宽高、位置、颜色、圆角，输出结构化差异报告，每条差异标注严重程度（low/medium/high）



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=313281e2c74b40ecb2d45284913d9aba&docGuid=_FPVZ0CvL6RfNJ "")
**AI 一键修复**

---

点一下，把差异报告 + Figma 截图发给 AI，让它直接改代码修复；

改完自动重新 Diff 验证

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2a4d076630cc44209c82a8084b2093ff&docGuid=_FPVZ0CvL6RfNJ "")


### 2.4 场景实践
##### 业务收益
---

* 走查效率提升明显。以前一轮走查修复至少半天，现在大部分像素级差异能在 5 分钟内定位 + 修复完成。设计师和前端之间"你看看第三个卡片左边多了 2px"这类沟通基本消失。

##### 演示-Ai视觉自动检测&AI修复
---

[附件]
---

## 场景三：运营活动智能识别 + 多模式导入
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=587b6b2be51c4540b262c95c64bbb807&docGuid=uz7MLANZMaPAVC&sign=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiYXBwSWQiOjEsInVpZCI6IkpGd1pIbzJRbTEiLCJkb2NJZCI6IkVGaW9idllQNDBUMUR6In0..rgJTN1QXxXqQOewT.tO7IYSVa5Rqm3YEDu8qdSs2113UtcAM1oXVEY7xkkH90ld0Q6RiNKm2fycZ1FoBTlGWAeOgoQ6jsLbaAkwyWvlbsw85uvd26icV4o1ZuNKKTXSBp7xJEdMDDfMk9bzZCL3FE-Zr4KLWB4jRj8T3OiSoRVp5Cd39NDzVO6u6ztKKiVilte9JpkAgD31Q_fovBnFYYUMaE5oXFCSdiP-HhQFcTLg.BpJor2DNfTlukzKy_DdWtQ "")
### 3.1 场景痛点
运营活动大量重复性工程环节

每期运营活动（抽奖、任务中心、签到等），前端拿到设计稿后从头搭建页面结构 + 业务逻辑。活动视觉皮肤每次不同，但骨架结构和交互逻辑 80% 是重复的——九宫格抽奖永远是 3x3 格子加一个抽奖按钮，任务中心永远是任务列表加状态按钮。每期活动重做这些逻辑，7~8 天的工期里有大半花在"已经写过的东西"上面。

### 3.2 生产原链路
工程师手工搭建

每期运营活动（抽奖、任务中心、签到等），前端拿到设计稿后从头搭建页面结构 + 业务逻辑。活动视觉皮肤每次不同，但骨架结构和交互逻辑 80% 是重复的。

### 3.3 平台新链路
AI自动识别，多模式导入，交互自动组装

1. 设计稿导入 make 时，自动扫描节点树，通过名称规则和尺寸特征识别出"这块是九宫格抽奖区""这块是任务中心"
2. 弹出确认面板，每个识别到的活动区域可以选择三种导入模式：

    * **static**：只保留视觉壳，不加交互（适合纯展示区域）
    * **hybrid**：保留 Figma 的精确视觉背景，在上面叠加一层透明的交互覆盖层，点击区域、动画、接口调用都在覆盖层里完成（视觉保真度最高）
    * **full**：整块替换为功能完整的交互组件，视觉由组件内的 CSS 变量控制

3. 从设计稿里自动提取配色方案（按钮色、背景色、文字色、强调色），注入到生成组件的 CSS 变量里
4. 从文本节点里抽取奖品名、任务标题等内容，作为配置种子填充

### 3.4 关键技术方案
** 活动检测规则**

---

基于节点名称的正则匹配（lottery/grid/九宫格 → 抽奖；task/任务/金币 → 任务中心）+ 尺寸阈值过滤

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ffbb64d11795461d9a287fa1cea4b8e0&docGuid=_FPVZ0CvL6RfNJ "")
**Hybrid 模式的分层架构**

---

底层是 Figma 精确还原的静态 DOM，上层是绝对定位的交互组件，两层叠加实现"视觉保真 + 逻辑可用"



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3d78e60206e1480492393d0c1d4242fc&docGuid=QfyAe4FS50uEp- "")
****

**内容种子与配置面板**

---

检测活动配置种子并映射

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a4c8fad3a4d44b41a96a791494248299&docGuid=_FPVZ0CvL6RfNJ "")
### 3.5 场景实践
##### 业务收益
---

* 一个标准的九宫格抽奖 + 任务中心活动页，从设计稿到可运行的页面（含交互逻辑、Mock 数据、主题配色），整体时间从 7~8 天压缩到5分钟以内。后续活动换皮时只需要重新导入新设计稿，交互逻辑和接口对接自动复用。

##### 演示-Ai视觉自动检测&AI修复
---

[附件]


---

## 场景四：对话式页面生成与多轮修改
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=83518906988843b192782cdb6126f823&docGuid=_FPVZ0CvL6RfNJ "")
### 4.1 生产原链路/场景痛点
AI缺失对工程项目的运行时理解

直接把需求发给 ChatGPT/Claude 生成代码，复制粘贴到项目里——跑不起来。原因很简单：AI 不知道你的项目里有什么文件、装了什么包、入口在哪。每次对话都是从零开始，上下文完全断裂。更麻烦的是，AI 生成的代码即使语法正确，也缺少真实的运行环境去验证。

### 4.2 平台新链路
改动实时闭环反馈，工程链路透明化

make 内置了完整的对话式开发环境：

1. 用自然语言描述需求，AI 实时生成代码
2. AI 通过 Tool Call 机制直接操作项目文件系统——写文件、改文件、装依赖、搜索图标，每个操作都在 WebContainer 里实时生效
3. 浏览器内 Vite HMR 即时刷新，左边聊天右边看效果
4. 多轮对话不丢上下文，AI 知道项目当前所有文件和已安装的包

### 4.4 关键技术方案
**WebContainer + 快照加速**

---

整个 Node.js 运行时跑在浏览器里，预构建的快照（99MB gzip 到 13MB）包含 node_modules，启动时间从 255 秒降到 35 秒

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=80996929fe4147d9be99beae66248327&docGuid=QfyAe4FS50uEp- "")
**8 个 AI 后端支持层架构**

---

Claude API、Gemini、通义千问、Azure OpenAI、Ducc（百度内部）、本地模式等，按场景切换

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=482646edbde8485abb216cc448ba2530&docGuid=_FPVZ0CvL6RfNJ "")


****

**Tool Call 执行引擎**

---

AI 输出的不只是代码文本，而是结构化工具调用（write_file / edit_file / install_package），由 ToolExecutor 在 WebContainer 里真实执行

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1d6814b213b5426c8c3048fae30824ce&docGuid=_FPVZ0CvL6RfNJ "")




**上下文压缩**

---

对话超过 20 轮时自动生成摘要，保留关键上下文（业务原子注入、模板信息），避免 token 溢出

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c3435bec22e548cebebd8993982e3538&docGuid=_FPVZ0CvL6RfNJ "")


****

make 的对话系统和传统 AI 编程助手的根本区别：**AI 的输出不是代码文本，而是结构化的工具调用**。AI 说"我要创建一个登录页"，实际执行的是 `write_file({ path: 'src/views/Login.vue', content: '...' })`，由 ToolExecutor 在 WebContainer 里真实写入文件系统，Vite HMR 即时刷新预览。

#### 4.4.1 Tool Call 引擎
工具调用模型

|工具|做什么|风险等级|
|-|-|-|
|`write_file`|创建或覆盖文件。自动修复 Vue SFC 未闭合标签、自动注入远程图片桥接、自动安装 shim 依赖|中|
|`edit_file`|精确字符串替换。三级匹配：精确 → 尾部空白标准化 → 缩进标准化，逐级降级|低|
|`install_package`|在 WebContainer 里 `npm install`。shim 包（@iconify/vue、lottie-web、motion）拦截后直接返回|中|
|`iconify_search`|调用 Iconify API 搜索 200,000+ 图标库，返回 `prefix:icon-name` 格式|低|
|`publish_tool`|触发页面发布流程（需要用户确认）|高|

AI 的每次响应最多执行 **10 轮**工具调用。每轮：流式接收模型输出 → 提取 `tool_use` 块 → 执行 → 将结果回传 → 下一轮。纯文本响应终止循环。

高风险工具（`bash`、`supabase_connect`、`publish_tool`）必须用户确认后才能执行，由 ToolRegistry 的权限模型控制。

#### 4.4.2 WebContainer：浏览器里的 Node.js
运行时底层机理&工程优化

整个开发环境跑在浏览器里。关键性能数据：

|阶段|优化前|优化后|提升|
|-|-|-|-|
|WebContainer WASM 初始化|12s|12s|—|
|依赖安装|**222s**|**3~5s**（快照挂载）|**98%**|
|Vite 启动|21s|~20s|—|
|**总启动时间**|**255s**|**~35s**|**86%**|

核心优化：预构建快照。把 42MB 的 `node_modules` 序列化为 99MB JSON，再 gzip 压缩到 **13MB**。启动时 `WebContainer.boot()` 和 `fetch(snapshot)` 并行执行，快照解压后直接 `mount` 到虚拟文件系统，**跳过 pnpm install**。如果快照加载失败，fallback 到 `pnpm install --prefer-offline`。

Vite 采用**编程式启动**（`createServer()` 而非 CLI），因为 WebContainer 不能运行 esbuild 原生二进制。`optimizeDeps` 被完全禁用，HMR overlay 关闭防止错误遮挡 UI。

#### 4.4.3 8 种 AI 后端
多模型快速接入

|模式|默认模型|特点|
|-|-|-|
|Claude API|claude-sonnet-4-5|原生 tool_use + SSE 流式|
|Gemini|gemini-2.5-flash|Cloudflare Worker 代理，多 Agent 阶段自动切模型|
|Gemini Trial|gemini-2.5-flash|密码门控的共享体验入口|
|通义千问|qwen-coder-plus|DashScope OpenAI 兼容格式|
|Azure OpenAI|gpt-5.4|支持 reasoningEffort 参数|
|Ducc（百度内部）|MiniMax-M2.1|13 个可选模型（MiniMax/GLM/Claude/Kimi）|
|本地模式|—|文件桥接，不调用外部 API|
|远程模式|—|用户自定义 MCP Server URL|

其中 6 种支持多智能体流水线调度（Claude / Gemini / Gemini Trial / Qwen / Azure / Ducc）。

#### 4.4.4 上下文管理
上下文管理体系

对话超过 **20 轮**时自动触发压缩。压缩策略：

1. **系统消息永远保留**——业务原子注入、模板上下文不会被压缩掉
2. **保留最近 10 条**对话
3. **更早的消息做本地摘要**（不调用 AI API）——提取 assistant 回复，每条截断 200 字，编号拼接
4. 文件快照中的 base64 图片数据被截断为 `[BASE64_TRUNCATED]`，避免 token 浪费

增量快照机制：`WebContainerManager` 通过 `_dirtyPaths` Set 追踪被修改的文件，只重新读取变更文件而非全量扫描。

### 4.5 场景效果
从"描述需求"到"看到可运行的页面"，简单页面（着陆页、展示页）5 分钟内完成。复杂页面通过多轮对话逐步迭代，全程不需要离开 make 工作台。相比传统的复制粘贴 AI 代码的方式，省去了环境搭建、依赖安装、文件管理的所有手动步骤（演示视频见下方场景五）。

---

## 场景五：多智能体流水线——PM/UI/Dev/QA/Publish 五阶段协作
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=98e16b74ec5c4afbae439c103351ef28&docGuid=_FPVZ0CvL6RfNJ "")
### 5.1 生产原链路/场景痛点
语意澄清成本高

直接给 AI 写一大段需求，让它一口气输出完整页面，结果往往不可控：需求理解偏差、配色千篇一律的 `#1890FF` 蓝、布局结构混乱、缺少响应式处理、没有错误兜底。更根本的问题是——单个 AI 同时扮演产品经理、设计师、开发者、测试四个角色，每个维度都只能做到 60 分。这和人类团队协作中的分工逻辑是矛盾的：你不会让一个人同时写 PRD、画设计稿、写代码、跑测试。

行业内的多智能体框架（LangChain/CrewAI/AutoGen）大多面向通用任务编排，Agent 之间用自然语言传递信息。但前端交付场景的问题很具体——配色数值不能传错、布局类型不能模糊、动效库不能用平台不支持的——自然语言传递在这类场景下信息损耗太大。

### 5.2 平台新链路
多智能体分工

make 把单次生成拆成五个专业角色的固定流水线，**Agent 之间用结构化 JSON 交接**，不用自然语言传话：

1. **PM Agent（需求分析）**：扮演"资深产品经理"角色，把用户的一句话模糊描述转化为结构化的 JSON 交付规格书。输出包含 `modules`（模块拆分 + 优先级）、`userStories`（用户故事）、`acceptanceCriteria`（验收标准）、`constraints`（约束条件）。对于运营推广类页面，PM 会强制将"动效表达"标记为核心交付项而非可选项
2. **UI Agent（设计方案）**：扮演"资深 UI/UX 设计师"，在 PM 规格书的基础上输出完整设计方案 JSON。包含配色体系（`colorScheme`，含 7 个语义化色值）、布局方案（`layout`）、排版规格（`typography`）、动效计划（`effects[]`，每个效果标注使用的库和降级方案）、资源规划（`assets[]`，图标用 Iconify、图片用 Picsum）。UI Agent 收到的 system prompt 里内嵌了平台的设计能力清单（`DesignCapabilityRegistry`），确保它只推荐平台实际支持的效果库
3. **Dev Agent（代码生成）**：不是一个独立的 "AI 角色"，而是标准的 AI 对话 + Tool Call 执行引擎。它拿到的 prompt 是 `buildEnrichedPrompt()` 组装的结构化文档——包含原始用户需求、PM 摘要、UI 设计 JSON、7 条硬性实现规则。Dev Agent 有权限调用 `write_file`、`edit_file`、`install_package` 等工具，在 WebContainer 里真实执行代码
4. **QA Agent（质量检查）**：扮演"资深前端 QA"，从 7 个维度检查代码：需求符合度、设计准确度、代码规范、响应式、可访问性、安全性、性能。输出结构化评估报告——每条问题标注严重级别（`error`/`warning`/`info`）、定位到具体文件和行号、附带修复建议。包含 `error` 级别问题时，报告状态标记为 `warning` 提醒用户关注
5. **Publish Agent（发布上线）**：不涉及 AI 调用，是纯程序化的发布流程触发器。该阶段设有 **人工确认门禁**（`requiresConfirmation: true`，`riskLevel: 'high'`），在执行发布动作前会切换到 `awaiting_confirmation` 状态等待用户审批。确认后自动触发 Vite 构建 → BOS 上传 → Cloudflare 部署，生成可访问 URL

### 5.3 关键技术方案
### 
**Agent 间用 JSON 交接**

---

不是自然语言传递，避免信息损耗

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fb3e4d4296e14b3081a28e5eeb37d10a&docGuid=_FPVZ0CvL6RfNJ "")






**DesignCapabilityRegistry 约束生成边界**

---

明确声明平台支持哪些动效库（GSAP/anime.js/Lottie/Motion）、哪些图标源（Iconify/Picsum）、每个库的正确用法和已知坑点，从源头减少生成不可用代码的概率

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c06ca548c2694e259b276488c0242dc9&docGuid=_FPVZ0CvL6RfNJ "")


****

**QA报告与降级机制**

---

降级不影响功能运行

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=31646efb844748af8a400449ec5cb35b&docGuid=_FPVZ0CvL6RfNJ "")


#### 5.3.1 Agent 之间怎么交接
JSON 协议替代自然语言

这是和 CrewAI/AutoGen 等通用框架最大的区别。通用框架的 Agent 之间传的是"一段话"，PM 告诉 Dev"用蓝色主题做一个卡片式布局"——这种表述留给 Dev 的解释空间太大。make 的做法是每个 Agent 输出规范化的 JSON，下游 Agent 直接解析字段：

**PM → UI 的交接**（PM Agent 输出的 JSON 直接作为 UI Agent 的输入）：

```
{
  "title": "TeraBox 双十二年终促销落地页",
  "modules": [
    { "name": "Hero 区", "priority": "high", "requiredFields": ["主标题", "副标题", "CTA 按钮"] },
    { "name": "会员权益对比", "priority": "high", "requiredFields": ["免费版", "高级版", "功能对比表"] },
    { "name": "用户评价", "priority": "medium", "requiredFields": ["评价卡片", "评分", "头像"] }
  ],
  "userStories": ["作为新用户，我想快速了解付费和免费版的区别"],
  "acceptanceCriteria": ["Hero 区 CTA 按钮点击后跳转支付页", "对比表格移动端横向可滚动"],
  "constraints": ["必须支持 15 种语言", "页面首屏加载 < 2s"]
}
```
**UI → Dev 的交接**（UI Agent 输出的 design.json 片段）：

```
{
  "colorScheme": {
    "primary": "#6366f1", "secondary": "#8b5cf6", "background": "#0f0f1a",
    "surface": "rgba(255,255,255,0.08)", "text": "#ffffff"
  },
  "effects": [
    {
      "id": "hero-entrance", "type": "animation", "library": "motion",
      "description": "Hero 区元素依次淡入上移",
      "fallback": "降级为 CSS transition opacity 0.3s ease"
    }
  ],
  "assets": [
    { "id": "iconify-star", "type": "icon", "source": "iconify", "iconName": "mdi:star" },
    { "id": "hero-bg", "type": "background", "source": "picsum", "searchKeyword": "gradient dark" }
  ]
}
```
`buildEnrichedPrompt()` 把上述两份 JSON 和原始用户需求组装成一份结构化的 Markdown 文档交给 Dev Agent，附带 7 条硬性规则：必须实现所有 PM 定义的模块、必须遵循 UI 定义的配色、动效优先用 `motion` 其次 `lottie`、图标必须用 Iconify（并强制安装 `@iconify/vue`）等。

#### 5.3.2 为什么不用通用多智能体框架
智能体架构选择

我们评估过 CrewAI、AutoGen 和 LangGraph，最终选择自建固定流水线，原因有三：

1. **前端交付的角色分工是确定的**。不需要 Agent 自主决定"下一步该交给谁"——PM 分析完一定是给 UI，UI 设计完一定是给 Dev，这个顺序不会变。通用框架的动态任务编排在这个场景下是多余的复杂度
2. **JSON schema 比自然语言可靠**。配色值 `#6366f1` 不能传成"紫蓝色"再让下游猜，布局类型 `grid` 不能传成"网格感觉的"。结构化交接在精确度要求高的场景下必须的
3. **失败降级要快**。如果 PM 或 UI 阶段挂了（模型超时、格式解析失败），make 会自动标记为 `fallbackToSingleAgent`，跳过剩余预处理阶段，直接用原始用户消息走 Dev 单 Agent 生成——整个降级过程对用户透明，不需要重新发起对话。通用框架的错误处理要自己实现这些

#### 5.3.3 DesignCapabilityRegistry——从源头约束生成边界
AI工具约束

AI 最容易犯的错是用了平台不支持的库。比如生成了 `import { useSpring } from '@react-spring/web'`——WebContainer 里根本没装这个包，代码直接跑崩。

`DesignCapabilityRegistry` 是一个静态注册表，明确声明 make 平台支持的所有效果库和资源来源：

|**能力**|**库**|**复杂度**|**预注册（免安装）**|
|-|-|-|-|
|GSAP 滚动触发|gsap@^3.12|高|否，需 npm install|
|anime.js 时间轴|animejs@^3.2|中|否|
|Lottie 矢量动画|lottie-web@^5.12|低|是（ShimRegistry 预注册）|
|Motion 动效|motion@^10.18|低|是|
|Iconify 图标|@iconify/vue|低|是|
|Picsum 占位图|（无 npm 包）|低|是（URL 直接引用）|

这张表会被 `buildDesignCapabilityManifest()` 渲染成 Markdown 文本，注入到 UI Agent 的 system prompt 里。UI Agent 在输出设计方案时只能从这张表里选库。如果用户在 UI 面板里手动禁用了某个库（比如关掉 GSAP），被禁用的条目会被追加到 prompt 的 `⚠️ 用户已禁用以下能力` 区域，强制排除。

另外一个关键细节：注册表里标注了一些 **已知坑点**——比如 Motion 库的 `spring()` 函数在 WebContainer 环境下会 crash，prompt 里直接写了 `FATAL: spring() 在 WebContainer 环境下会崩溃，禁止使用`。这种把工程踩坑经验编码进 prompt 的做法，比让 AI "自己发现问题" 高效得多。

#### 5.3.4 QA Agent 的 7 维度检查
QA Agent 工作范围

QA Agent 不是简单地 "看一眼代码说还行"，而是从 7 个维度出具结构化报告：

1. **需求符合度** ：PM 定义的每个模块是否都实现了
2. **设计准确度** ：配色是否匹配 UI 方案、布局类型是否正确
3. **代码规范** ：Vue SFC 结构、命名规范、无硬编码
4. **响应式** ：是否处理了移动端适配
5. **可访问性** ：语义化标签、alt 文本、键盘导航
6. **安全性** ：XSS 防护、外部资源引用检查
7. **性能** ：大图未压缩、未必要的依赖引入

输出示例（摘自实际运行结果）：

```
{
  "score": 82,
  "summary": "整体实现完成度较高，主要问题在移动端适配和图片资源处理",
  "issues": [
    {
      "severity": "error",
      "rule": "响应式设计",
      "detail": "对比表格在 640px 以下宽度溢出容器",
      "location": "src/components/ComparisonTable.vue:45",
      "suggestion": "添加 overflow-x: auto 或改为卡片式堆叠布局"
    },
    {
      "severity": "warning",
      "rule": "性能",
      "detail": "Hero 背景图使用 Picsum 原图未指定尺寸参数",
      "location": "src/App.vue:12",
      "suggestion": "使用 https://picsum.photos/1200/600 限制请求尺寸"
    }
  ],
  "fixable": {
    "canAutoFix": false,
    "fixSteps": ["1. 给 table 容器加 overflow-x: auto", "2. Picsum URL 追加尺寸参数"],
    "risks": ["表格横向滚动可能影响用户体验，建议考虑响应式改为堆叠布局"]
  }
}
```
当前 QA 评分是**纯参考性质**——不会自动阻断流水线或触发重做。包含 `error` 级别问题时，QA 阶段状态标记为 `warning`，流水线卡片上显示橙色警告。用户可以根据报告决定是手动修改还是让 AI 再改一轮。

之所以没做自动重试，是因为我们在实践中发现：自动 retry 经常陷入"改了 A 又崩了 B"的循环，不如把问题清晰地呈现给人类决策。这个取舍和 QA 在软件工程中的角色一致——QA 提问题，不直接改代码。

#### 5.3.5 降级机制——预处理失败不影响主流程
稳定性机制

多智能体流水线的一个现实问题是：PM 或 UI 阶段可能因为模型超时、JSON 格式解析失败等原因挂掉。make 的处理策略是**快速降级到单 Agent 模式**：

* PM 阶段失败 → 标记 `fallbackToSingleAgent`，跳过 UI 阶段，Dev 直接用原始用户消息生成代码
* UI 阶段失败 → 同样降级，Dev 拿到的只有 PM 摘要和原始需求（缺少设计方案）
* QA 阶段失败 → 不影响已生成的代码，只是缺少质量报告
* Publish 阶段失败 → 返回 null，用户可手动从发布面板重新触发

降级对用户是透明的——工作流卡片上会显示"多智能体预处理失败，已降级为直接代码生成"，但代码生成不会中断。这个设计保证了多智能体是"锦上添花"而非"必须依赖"，任何阶段挂掉都不会让用户卡住。

### 5.4 场景实践
##### 业务收益
---

* 生成质量稳定性有明显提升。以前单次生成的页面可能需要 3~~5 轮人工调整，引入多 Agent 后大部分页面 1~~2 轮就能到可用状态。尤其是配色合理性、布局结构完整性这两个维度，改善最为明显。

##### 演示-智能体协作闭环全流程
---

[附件]


---

## 场景六：业务原子——把重复集成的业务逻辑变成"装一下就能用"
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2cf58588ee9044be80f194189a73d7fe&docGuid=_FPVZ0CvL6RfNJ "")
### 6.1 生产原链路/场景痛点
业务原子接入成本高

每个新项目都要重新写 HTTP 请求封装、配置 i18n、接入任务中心 API、处理权限校验……这些跟业务强相关的基础能力，每次都重复搭建。更深层的问题是：即使手动配好了 i18n，AI 生成代码时依然会硬编码中文文案——因为 AI 不知道项目里已经有了 i18n 基建。

### 6.2 平台新链路
业务原子快速集成 

我们把这些能力封装成"业务原子"，当前已有 9 个：

|原子|功能|
|-|-|
|`tera-request`|TeraBox 出海请求封装（原生 fetch，自带鉴权和错误处理）|
|`i18n`|15 种语言国际化（vue-i18n v9，自动 RTL，mainPatch 自动注入）|
|`lottery-nine`|九宫格抽奖（完整 API + Mock 引擎 + 动画）|
|`tera-task-center`|金币任务中心（8 个接口 + useTaskCenter/useTaskActions）|
|`http-request`|通用请求封装|
|`permission-system`|权限控制|
|`message-system`|消息通知|
|`approval-system`|审批流程|
|`announcements`|公告系统|

选择需要的原子 → `BusinessLoader` 自动完成：写入运行时文件、安装依赖、修改 main.js 入口（mainPatch）、把原子的使用规范注入 AI 上下文。后续 AI 生成代码时会自动调用这些原子的 API，而不是重新发明轮子。

### 6.3 关键技术方案
**原子注入流水线**

---

每个业务原子在注入项目时都会经过依赖安装、运行时文件写入、mainPatch修改、AI约束注入和few-shot注入5个步骤，让能力既进入运行环境，也进入AI上下文。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4f50f75c0d03457889a2e0cc0f02e05d&docGuid=_FPVZ0CvL6RfNJ "")


****

**AI 上下文约束**

---

每个原子自带 `systemPrompt` 和 `fewShot`，注入后 AI 会按照原子的 API 规范生成代码，比如 i18n 原子会约束 AI "禁止硬编码任何语言的文案，所有文本必须用 t() 包裹"

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c54ccc007a4f42f99b16d29bb121702e&docGuid=_FPVZ0CvL6RfNJ "")


#### 6.3.1 原子注入流水线
业务原子底层注入机制

每个原子在注入时 执行 5 个步骤：

|步骤|做什么|示例|
|-|-|-|
|1. 安装依赖|聚合所有选中原子的 `dependencies`，增量 npm install|`vue-i18n: ^9.13.0`|
|2. 写入运行时文件|遍历原子的 `files` map，逐个写入 WebContainer|i18n 原子写入 17 个文件（1 个插件入口 + 15 个语言包 + 1 个 composable）|
|3. mainPatch|自动修改 `main.js`——注入 import 语句和 `.use()` 调用|`import i18n from './i18n.js'` + `.use(i18n)`|
|4. 注入 AI 约束|所有原子的 `systemPrompt` 合并为一条系统消息推入对话历史|"禁止硬编码任何语言的文案，所有文本必须用 t() 包裹"|
|5. 注入 few-shot|原子的 `fewShot` 示例插入对话历史，让 AI 学会用法|登录页 + 多语言切换的完整代码示例|

关键设计：步骤 4 的系统消息带有标记 `'项目已注入以下业务能力'`，`clearHistory()` 时会识别并保留这些消息——确保清空对话后 AI 依然知道项目有哪些业务能力。

#### 6.3.2 当前原子清单
已有功能枚举

|原子|分类|功能|注入文件数|
|-|-|-|-|
|`tera-request`|tera-activity|TeraBox 出海请求封装（原生 fetch，自带鉴权和错误处理）|2|
|`i18n`|infra|15 种语言国际化（vue-i18n v9，自动 RTL，mainPatch 自动注入）|17|
|`lottery-nine`|tera-activity|九宫格抽奖（完整 API + Mock 引擎 + 动画）|3|
|`tera-task-center`|tera-activity|金币任务中心（8 个接口 + 19 种 task_kind + Mock 引擎）|4|
|`http-request`|foundation|通用请求封装|1|
|`permission-system`|foundation|权限控制|2|
|`message-system`|infra|消息通知|2|
|`approval-system`|infra|审批流程|2|
|`announcements`|infra|公告系统|2|

另有 5 个原子（auth、track、upload、pagination、payment）已定义文件但尚未注册到 Registry，处于开发中状态。

#### 6.3.3 深潜：i18n 原子
i8n原子原理解析

i18n 是一个典型业务原子。

**支持 15 种语言**：简体中文、繁體中文(港/台)、English、Español、Português、العربية、Русский、日本語、한국어、Tiếng Việt、ไทย、हिन्दी、Bahasa Indonesia、Türkçe。

**mainPatch 机制**——原子声明两个字符串：

```
mainPatch: {
    import: "import i18n from './i18n.js';",
    use: '.use(i18n)',
}
```
client 读取顶层配置 `main.js`，在顶部插入 import（去重检查），把 `.mount('#app')` 替换成 `.use(i18n)\n.mount('#app')`，无需人工改动。

**RTL 自动处理**：`useLocale` composable 切换语言时检查 locale code，如果是 `'ar'`（阿拉伯文）自动设置 `document.documentElement.dir = 'rtl'`，其他语言设 `'ltr'`。

**AI 约束的实际效果**：注入 i18n 原子后，AI 生成的每一行文案都会用 `t('module.key')` 包裹，且每次新增 key 必须同步更新 15 个语言文件——这不是靠"提示词建议"，而是注入到 system prompt 里的硬性约束。few-shot 示例展示了登录页和按钮列表的完整多语言写法，AI 直接模仿。

**事后迁移工具**：对于已经写完的项目（硬编码中文），提供 `i18nMigration` 工具——6 步自动化：提取中文 → 生成 i18n key → 生成 15 个语言包 → 调用 clinet 翻译 14 种语言 → 替换源码中的硬编码 → 输出结果。

### 6.4 场景实践
##### 业务收益
---

* 项目初始化阶段的重复工作量大幅减少。以 i18n 为例，以前配置 15 种语言的国际化环境需要半天到一天，现在勾选原子后几秒内完成，且 AI 后续生成的所有代码自动遵循多语言规范。

##### 演示-业务原子注入全流程
---

[附件]


---

## 场景七：落地页批量交付 + 登录支付闭环验证
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1d78138f70fd403aa0fe4e700b9fe2b7&docGuid=_FPVZ0CvL6RfNJ "")
### 7.1 生产原链路/场景痛点
落地页依赖业务功能进行闭环转化

除了运营活动页，TeraBox 的大前端交付还有一大块高频需求：

* **SEO 落地页**：针对不同关键词、不同地区投放的搜索着陆页，结构简单但数量大、上线节奏快，需要支持多语言和 SEO meta 标签
* **推广渠道着陆页**：Facebook/Google/TikTok 等广告投放的落地页面，需要 UTM 参数追踪、A/B 测试变体、转化埋点
* **产品功能介绍页**：新功能上线时的宣传页，包含 Hero 区、功能对比、用户评价、CTA 引导
* **下载引导页**：各端下载入口，适配不同设备和地区的应用商店链接

这些页面有个共同特点：视觉和结构不复杂，但要做到"真正可用"需要打通登录态、接口对接、甚至支付跳转——否则只是个好看的静态页面，验证不了真实转化效果。

### 7.2 生产原链路
人工组装流程

* 每个落地页走完整研发流程（PRD → 设计 → 开发 → 联调 → 上线），周期 3~5 天
* 多语言版本靠人工复制修改，容易遗漏
* 登录/支付等能力每次单独接入，重复工作
* 想做 A/B 测试时需要再创建一套变体页面

### 7.3 平台新链路
业务功能自动组装视图

make 当前已经可以覆盖这类场景的核心链路：

1. **快速生成**：通过对话式开发或 Figma 导入，几分钟内出页面首版
2. **多语言即开即用**：i18n 业务原子一键注入 15 种语言支持，AI 生成的代码自动用 `t()` 包裹所有文案，阿拉伯文自动 RTL
3. **登录/鉴权能力集成**：`tera-request` 原子自带 TeraBox 登录态和鉴权封装，页面可以直接调用需要登录态的后端接口，验证真实用户流程
4. **支付/会员跳转**：通过原子能力对接会员购买和支付跳转链路，落地页的 CTA 按钮可以直接触发真实的购买流程
5. **SEO 支持**：多智能体的 PM Agent 在需求分析阶段就会生成 SEO 相关的 meta 标签、结构化数据建议
6. **一键发布到 Cloudflare 边缘节点**：生成即可发布，拿到真实 URL 投入投放测试

### 7.4 场景实践
一个带多语言、登录态、会员购买引导的推广落地页，从需求描述到可访问 URL，整体时间从 13~15 天压缩到 1 小时以内。关键是这不是一个"只能看"的 Demo，而是一个登录能登、接口能调、支付能跳的真实业务页面，可以直接用于投放验证转化效果（相关原子化组件建设测试中）。这也是 make 当前重点建设的方向之一——**把 AI 的产出物从"看起来像"推进到"真实业务上线"**。

---

## 场景八：从生成到发布的闭环
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=83df7a7531ea4acd827f3774a7d9f163&docGuid=_FPVZ0CvL6RfNJ "")
### 8.1 生产原链路/场景痛点
发布链路程序繁杂、时间长

AI 工具生成的代码，还需要手动复制到真实项目、手动构建、手动上传、手动配置路由、手动验证上线。"生成完"和"能上线"之间隔着一条人工装配线。大部分 AI 编程工具到"生成代码"就结束了，剩下的发布环节回到传统流程。

### 8.2 平台新链路
一键cdn部署

make 把发布环节接入了平台：

* 工作台内直接触发 Vite 构建
* 构建产物自动上传 BOS
* 生成标准访问 URL
* 发布前有人工确认门禁（防误操作）
* 发布结果回填到工作台

### 8.3 关键技术方案
**五层发布流水线**

---



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc2bb1e301c6481ca7c7fd58345ff73d&docGuid=EFiobvYP40T1Dz "")
**page.json 版本清单协议**

---



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=38e58c8a40344e798f0cecb8c99f7aef&docGuid=EFiobvYP40T1Dz "")


**缓存策略**

---



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c6cfda4b4e1f4ec6a18ea313d5b4afad&docGuid=EFiobvYP40T1Dz "")
#### 8.3.1 五层发布流水线
部署基本环节&稳定性考虑

make 把从"点击发布"到"用户通过 URL 看到页面"的全链路做成了自动化流水线，总共 5 层进程接力：

```
① 前端编排层（PublishPanel.vue → publish store）
   ↓ 从 WebContainer 提取源码快照
② 本地中继服务（publish-relay，端口 3004）
   ↓ 标准化快照（补 build 脚本 / 修 vite 配置）→ spawn CLI 子进程
③ CLI 构建上传（publish-page-cli.mjs）
   ↓ npm install → vite build → 逐文件上传 BOS → 生成 page.json
④ 索引注册（Cloudflare KV）
   ↓ POST /api/publish-index → 写入 KV：publish:page:{pageId}
⑤ Worker 回源（cf-worker-page-publish）
   ↓ 用户访问 → 查 KV → 拉 page.json → 拉 HTML → 原样返回
```
##### 为什么要 5 层
* **浏览器不能直接调 BOS SDK**——需要 AK/SK，不能暴露在前端
* **浏览器不能 spawn 子进程**——npm install 和 vite build 必须在 Node 环境跑
* **WebContainer 的快照需要标准化**——可能缺 build 脚本、vite 配置可能有编辑器内部插件（`fidPlugin`）
* **BOS 上传和 KV 注册分两步**——先保证所有资源文件传完，最后再注册版本索引

#### 8.3.2 page.json：版本清单协议
部署机制依赖

每个版本的核心中间产物是 `page.json`，描述了这个版本的所有资源位置：

```
{
  "schemaVersion": "1.0",
  "pageId": "task-center-20260414123456",
  "version": "2026.04.14-456",
  "render": {
    "mode": "html-url",
    "htmlUrl": "https://nd-static.bdstatic.com/ai-images/{pageId}/{version}/index.html"
  },
  "assets": {
    "base": "https://nd-static.bdstatic.com/ai-images/{pageId}/{version}/",
    "scripts": ["...index-a1b2c3.js"],
    "styles": ["...index-d4e5f6.css"]
  }
}
```
Worker 收到访问请求时：查 KV 拿到 `jsonUrl` → fetch page.json → 取 `render.htmlUrl` → fetch HTML → 原样返回。两跳回源，每层都可以独立缓存。

上传前 CLI 自动把 `index.html` 里的相对路径改写成 CDN 绝对路径（这步在上传时做而非 Worker 端做，Worker 拿到的 HTML 已经改写好）。

#### 8.3.3 缓存策略
缓存设计

|路径|版本来源|Cache-Control|
|-|-|-|
|`/publish/:pageId`（不带版本）|KV 查最新|`max-age=60, s-maxage=300`|
|`/publish/:pageId/:version`（带版本）|URL 直接指定|`max-age=300, s-maxage=86400, immutable`|

### 8.4 场景实践
##### 业务收益
---

* 从"页面做好了"到"能通过 URL 用户级访问"，在 make 里一步完成，不需要切到终端跑命令、不需要手动传文件。这条链路目前是 MVP 状态，核心流程已经跑通，网页目前会发布在cloudFlare边缘节点上（分级发布待接入）。

##### 演示-业务原子注入全流程
---

[附件]
---

## 场景九：本地真实项目接入——不只是生成 Demo
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4c5fba3879494b03a6b457b2f9f28097&docGuid=_FPVZ0CvL6RfNJ "")
### 9.1 生产原链路/场景痛点
存量业务场景改造诉求

AI 工具只能在沙箱里生成独立页面。想改真实项目？把代码复制出去，手动 merge，出了冲突自己解。更根本的问题是——AI 看不到你真实项目的运行状态，也改不了你本地跑着的代码。沙箱和真实项目之间隔着一道墙。

### 9.2 平台新链路
一键接入存量代码

make 支持"直连模式"：本地项目已经在跑（`npm run dev`），直接把 make 的预览 iframe 指向本地 dev server。

* 输入本地地址（如 `localhost:3111`）→ 点击连接 → 即时看到本地项目
* AI 可以针对页面中的具体元素做定向修改
* 支持版本快照和冲突处理

### 9.3 关键技术方案
#### 9.3.1 两种接入模式
make 提供两种方式把 AI 能力接入本地真实项目：

|模式|原理|AI 能否改代码|适用场景|
|-|-|-|-|
|**导入模式**（FSA）|通过 File System Access API 读取本地目录，同步到 WebContainer|能——双向写回（WC + 本地文件系统）|需要 AI 完整改造的项目|
|**直连模式**（Direct Connect）|iframe 直接指向本地 `npm run dev` 的 dev server|暂不能——只能预览和元素选取|已在运行的项目，快速查看和定向调整|

##### 9.3.1.1 直连模式：零等待接入
直连模式底层机理

本地项目已经在跑，直接把 make 的预览 iframe 指向 dev server。输入 `localhost:3111` → 点击连接 → 即时看到本地项目。

但这里有一个不容易绕过的技术障碍：

**COEP 限制**。make 宿主页面启用了 `Cross-Origin-Embedder-Policy: require-corp`（为了支持 WebContainer 的 SharedArrayBuffer），这意味着**普通 iframe 无法嵌入任何跨域内容**——包括你自己 localhost 跑的项目。浏览器会直接报 `ERR_BLOCKED_BY_RESPONSE`。

解决方案是使用 `<iframe credentialless>` 属性（Chrome 94+）。这个属性告诉浏览器：这个 iframe 放弃所有凭证（cookie、HTTP auth），换取绕过 COEP 的嵌入权限。对于本地 dev server 预览来说，不需要凭证，所以这个取舍是合理的。

实现细节：

* `PreviewPanel.vue` 维护两个 iframe——直连模式用 `<iframe credentialless :src="effectivePreviewUrl">`，普通模式用带 `sandbox` 属性的标准 iframe
* `LocalDirectBridge.setUrl()` 自动把 `localhost` 替换为 `127.0.0.1`——这两个在浏览器里是不同的 origin，不替换会触发 Private Network Access 限制
* `ping()` 直接返回 `true`——COEP 环境下 fetch/img 跨域探测都会被拦截，不如让 iframe 自然呈现结果（连不上就显示浏览器默认错误页）
* 面板内提供 vite.config.js 的 CORP 头配置指引（一键复制），用户需要在目标项目加两个响应头

**选取桥接**（Selection Bridge）：直连模式不止能看，还能选。make 提供一个 Vite 插件（`teraboxSelectionBridge()`），注入到目标项目后，用户可以在 make 里直接点击页面元素——插件会通过 `postMessage` 回传选中元素的标签名、类名、文本内容、层级位置等信息。父页面发送 `TB_PING` 检测插件就绪，收到 `TB_PONG` 后激活选取功能。

##### 9.3.1.2 导入模式：双向文件同步
导入模式底层机理

完整模式用 File System Access API 获取本地目录的读写权限，执行双向同步：

```
本地文件系统 ←→ FSABridge ←→ WebContainer VFS
                                    ↓
                              AI Tool Call 修改
                                    ↓
                            writeBack() 双写
                          ├→ WebContainer VFS
                          └→ 本地文件系统（FSA Handle）
```
`syncFileWrite(path, content)` 执行双写：先写 WebContainer 虚拟文件系统（Vite HMR 即时生效），再通过 `FileSystemFileHandle.createWritable()` 写回本地磁盘。新文件会自动创建中间目录。

反方向也有：`FSWatcher` 以 2s 轮询（页面不可见时 10s）检测本地文件变更——先比时间戳，再算 DJB2 哈希确认内容变化。如果 AI 和用户同时改了同一个文件，触发冲突检测（`pendingConflicts`），用户在 UI 上选择保留哪个版本。

### 9.4 场景实践
##### 业务收益
---

* 已有项目的局部修改不再需要把代码搬到 make 里重建。直接连上去、定向改、实时看效果。对于维护期的页面调整（改文案、换颜色、调布局，新增需求），这条链路比传统方式快得多。

##### 演示-接入本地代码库
---

[附件]
## 场景十：**NA端快速验证——编译安装，实时预览**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d7fb11d6f9c849a5bb0c81bec8ea4ae9&docGuid=uz7MLANZMaPAVC "")
### 10.1 生产原链路
端内需求强依赖端版本发版，人力有限

TeraBox 客户端（Android/iOS）日常积累大量小颗粒需求——调整按钮样式、修改文案措辞、新增功能入口等。这类需求单个工作量不大，但受限于排期优先级和开发人力，往往需要 5~7 天才能走完从提需求到合并上线的完整流程（需求提交 → 开发排期 → 编码实现 → Code Review → 合并发版）。大量低优先级但有业务价值的需求因此长期积压，产品经理难以快速验证想法的可行性和实际效果。

### 10.2 平台新链路
pm自主修改端内需求，实时预览

通过如流等即时通讯工具接入 AI 编码能力，产品经理以自然语言描述需求或直接提供需求文档，即可对 TeraBox Android/iOS 工程发起修改：

* AI 解析需求语义，自动定位目标代码模块并完成修改
* 增量编译变更模块，自动安装到真机或模拟器
* 通过 VNC 远程连接设备画面，产品经理实时查看修改效果
* 满意后自动生成 git commit 并提交 Code Review，完成从需求到 CR 的全流程闭环

整个过程无需产品经理了解代码细节，也不占用开发团队排期资源。

PM可以通过如流等聊天工具，通过自然语言描述或者需求文档的方式，对现有项目，如terabox Android/iOS，进行快速需求验证和实现。实现自动完成从需求到CR提交的全流程。通过需求描述并编码后，可以实时安装Android/iOS应用，并通过VNC方式让PM进行实时预览和体验。可极大节省沟通成本和快速验证。

### **10.3 关键技术方案**
* **VNC 双屏联动**：左屏实时呈现 Android/iOS 设备画面，右屏为对话式调试面板。产品经理用自然语言描述调整意图，AI 完成语义解析 → 代码定位 → 自动修改 → 增量编译 → 推送安装的完整链路，设备画面同步刷新
* **语义化代码定位**：不依赖精确的文件路径或代码行号，通过代码结构分析与语义理解双重校验，根据自然语言描述智能匹配目标代码位置
* **增量编译与快速部署**：仅编译变更涉及的模块，跳过全量构建流程；通过 adb install（Android）或对应工具链快速推送安装包到目标设备
* **修改记录与回滚**：每轮对话修改自动生成独立的 git commit，支持通过对话指令回退到任意修改节点，保证可追溯性和安全性

### **10.4 效果**
##### 业务收益
---

* 一个典型的客户端小需求（如调整按钮文案、修改入口位置），从产品经理描述需求到在真机上看到效果并提交 CR，耗时从 5~7 天压缩到小时级别。该能力尤其适用于需求验证阶段——产品经理可以快速试验多种方案、对比实际效果后再决定是否正式排期，有效降低无效开发的资源投入。

##### 演示-远程编译验证
---

[附件]
---

## 整体提效总结
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=61d7296f123b48f099e9487cc75e7b9f&docGuid=_FPVZ0CvL6RfNJ "")
### **从5-6个角色工具来回交接，到一个平台一条线走完**
|环节|以前|现在|
|-|-|-|
|设计稿 → 页面首版|1~2 天手工还原|几分钟自动转换，人工调整细节|
|视觉走查修复|半天+，肉眼对比反复沟通|Visual Diff 自动定位 + AI 修复，10 分钟级|
|运营活动页搭建|每期重建，2~3 天|智能识别 + 模板复用，30 分钟内|
|SEO/推广落地页|3~5 天完整研发流程|1 小时内生成 + 发布，含多语言和登录支付（建设中）|
|项目初始化（国际化/请求/权限等）|半天~1 天手动配置|业务原子一键注入，秒级|
|AI 生成代码的可用性|复制粘贴后大量手动调整|Tool Call 直接操作文件系统，实时运行|
|生成到上线|手动构建、上传、配置|平台内一键发布（MVP）|

核心价值不仅是某一步快了多少，而是**从设计稿到可访问页面这条路，以前要经过 5~6 个角色和工具来回交接，现在在 make 里可以一站式ai协同交接**。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
