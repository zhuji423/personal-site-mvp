---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "AI全流程实战：国际化输入法团队的效能飞跃"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\AI全流程实战：国际化输入法团队的效能飞跃.md"
---
AI全流程实战：国际化输入法团队的效能飞跃

#### 🧑‍🏫 案例作者：国际化海外输入法团队
#### 🎬 案例场景：全流程
#### 🔧 使用工具：Cursor
#### 📒 案例概要：本文介绍了国际化输入法团队如何通过 AI 全流程设计与开发实现组织进化的实战经验。打破传统流水线作业，建立以“代码”为统一产出物的“2+2+2”并行新范式。在此模式下，PM 利用 AI 直接生成可运行原型，UE 将设计规范转化为 AI Rules，RD 则转型为架构守护者。该变革将迭代周期从 9 天缩短至 5 天，效能提升 100%，实现了从“文档交付”到“代码共建”的组织进化，让团队全员成为高效的产品创造者。
## 1. 引言：从“流水线协同”到“AI 原生并行”的组织进化
大家是否有过这样的困惑：团队里的 PM 用上了 AI写文档，UE 用上了 AI 生成素材，RD 用上了 Copilot 写代码，每个人都在“提效”，但一看项目排期——集成测试还要3天，需求交付还是要两周，**整体的迭代周期一天都没少**。

国际化输入法团队在过去几个月里，探索了一套“AI 全流程产品设计与开发”的新模式，实现从 9 天到 5 天的迭代周期跨越，效能提升 100%。

今天，我们将这套尚在探索中的协作模式、踩过的坑以及适用的边界分享给厂内兄弟团队，希望能给大家带来一些启发。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=598429a4281d4c79a20f30a48e0a134f&docGuid=WHUUZGyezz9x7s "")
**核心提效数据对比**

|**阶段**|**传统串行模式 (约 9 天)**|**AI 全流程并行模式 (约 5 天)**|**效能/质量变化**|
|-|-|-|-|
|**原型/需求定义**|3 天 (PM 输出原型+PRD)|2 天 (PM 直接构建 AI Prototype)|交付物从文档升维至代码|
|**视觉/交互设计**|2 天 (UE 用 Figma 重新作图)|2 天 (UE 在代码库直接调优)|直出前端代码|
|**研发还原/逻辑接入**|4-5 天 (UI 还原 + 业务联调)|2 天 (RD 负责逻辑、架构与 CR)|零视觉还原成本，专注核心逻辑|
|**总计迭代周期**|**约 7-9 天**|**约 5 天**|100% 效率倍增|

### **认知的第一次飞跃，源于“统一语言”的确立**
海外输入法团队意识到，每个人都在自己的环节用上 AI ，但团队发现这是一个上下游协作的流程，单点提效无法解决流转效率。PM、UE、研发之间的“语言不通”，上游（PM）输出的内容下游（研发）无法直接使用。**既然要用 AI 提效，团队各环节必须统一交付产物为****代码**，必须打破传统流程，从下游（研发）的需求倒推上游（PM），要求 PM/UE 的输出必须是 AI 能读懂、研发能用得上的代码。

虽然 PM 开始尝试输出 AI 生成的代码（如 md 或文件），但这种抽象的格式并不是谁都能立刻看懂，阅读和理解成本依然很高。团队在摸索中发现，通过**引入“模拟器”**，让所有人直观看到点击前后的交互变化，所见即所得。这标志着 PM、UE 和研发终于在同一个具象的维度上达成了理解一致。



### **而最核心的认知突破，来自于对“AI 擅长什么”的深度反思**
在一次汇报中，总监提出了一个问题：“既然是用 AI 做事，你们一定要懂得 AI 擅长什么？”

团队意识到之前的做法是“以我为主”——即“我想做什么”，就强行让 AI 去执行所有的细节。 团队开始尝试“顺应AI优势”（如视频理解、标准化页面生成），将标准化、高重复、非个性化的模块全权交给 AI 处理，实现真正的产能释放；而将人的智慧聚焦于核心策略、深度逻辑与经验判断。这种从“以我为主”到“顺应 AI 优势”的视角切换，成为了我们 AI 实践从零散尝试走向整体系统化提效的关键转折点。



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0bf1c57eef7d4f4aa60710d3de67663e&docGuid=WHUUZGyezz9x7s "")


 当代码成为统一交付物，PM 和 UE 的产出物（70% 的基础 UI 与交互）具备了 90% 以上的直接可复用性。组织不再是在各角色产出间“翻译”需求，而是在共同维护同一份“代码”产出。



**产品设计原型框架**

**（2天时间）**

[附件]


**设计完善后**

**（2天时间）**

[附件]


**研发完善后**

**（2天时间）**

[附件]


## 2. 产品经理（PM）：告别纸上谈兵，用“Vibe Coding”实现想法即成品
在 AI 全流程中，PM 的角色已从“文档搬运工”转变为“原型定义者”。高质量的 AI Prototype 能够排除 70% 的理解偏差，使团队在需求评审阶段即实现“**所见即所得**”，明确 MVP 核心功能点与产品定位，直接打通了技术可行性，也让下游 UE 与 RD 提前进入“精修”与“联调”状态，**协同模式从串行自发转变为了更高效的并行模式**。



### 模拟器即原型：所见即所得的交互验证
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=837ca9eb94a94ee18bdaf3e3c7dce13c&docGuid=WHUUZGyezz9x7s "")
**结构化文本输入法：** 将功能模块化，分页面描述功能、文案及按钮。关键在于**命名的一致性**，为后续的微调与迭代预留精准的锚点。

```
根据这个Prompt，用flutter 在simulator上创建一个app demo，产品名为 “Prompt helper” 的 App，整体为深色模式。

App总体分为两个部分：
1.新手引导页轮播：有3页引导页轮播，右上角是Skip，正中下方是Continue 按钮
2.主界面：包含模板库、用户输入的 Prompt 生成流程、个人设置三个部分
```
```
二、新手引导页轮播（界面 1–3）
每页使用全屏背景占位图，占界面的三分之二，居上半部分，左上角语言选择图标（圆形国旗，如 🇺🇸），右上角“SKIP” 按钮（白色、中号字体）
页面底部是居中的 “Continue” 按钮（白色按钮，黑色文字）
按钮上方是分页圆点（选中时白色，其他为灰色）

第 1 页，标题：“Ulimited SoraVideo Prompts”
副标题， “200k+ quality, tested prompts space.”
背景图占位，底部继续按钮，点击后进入下一页

第 2 页，标题：“Sora Prompt Generator”
副标题， “Auto-adapt your idea to Sora’s style and camera.”
布局相同

第 3 页，标题：“Multilingual Voice-to-Prompt”
副标题， “Multilingual voice — your idea becomes a prompt.”
布局相同

---
三、主界面
底部 Tab 栏（三个 Tab）：
Templates
Generator
Setting
背景色：纯黑色
图标：白色（选中时白色、未选中灰色）
文案：在图标下方，字号要适宜

---
### Templates
顶部文本：“Prompt helper”（白色加粗）
右上角：“Premium” 按钮（灰色圆角 + 白色图标）

模块区域
Featured Sora Prompts
左侧标题、右侧 “Explore all” 链接（白色小字，下划线）
2–3 列布局的卡片网格（圆角，正方形的灰色占位图）

Trending Sora Prompts
与上方结构一致

---
### Generator
这是主要的 生成页面，用户可以在此描述他们的视频创意，自动生成适配 Sora 的提示词
顶部文本：“Prompt helper”（白色加粗）

区块 1 — 输入区域
标题标签：“Describe your video”
字体：小的灰色字体，右侧带一个小问号或信息图标（ⓘ）
大型文本输入框，占位符文案：“Describe your video”，支持多行输入

区块 2 — 生成按钮
中间有一个大的主按钮：“Generate Prompts”
宽度：最好是占屏幕宽度的70-80%
按钮下方：折叠文本链接（切换Show Options）
点击后展开高级参数选项（默认收起）

区块 3 — 输出区域
副标题：“Your Sora prompt will appear here”

---
### Setting
顶部文本：“Setting”（白色加粗）
共5个设置项目：Rate us\Use of terms\Contact us\share our app
```
[附件]
**图像/原型输入法：** 在 0-1 阶段，AI 对图像的识别能力是复刻竞品或手绘草图的最快路径。将截图附在对话框中，AI 能以极高精度还原页面布局。

```
根据附件原型搭建demo，App name为“Prompt helper22”
整个结构分为新手引导流程和主界面流程
新手引导分为3个页面，再加一页键盘设置
主界面流程分为三个tab，模板库、生成器、设置页
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=59cfe463220844d88544c2621de3147d&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8e361b9b47b24828865212fe0fcd6f73&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2d38babf23a640698e5a5708dc121a94&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=43ed2e18c00b44c4899a9bfa350a998b&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=18cdf3f624b94bea8ead1b6138e2639d&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3c3439975d7241d8ab9276d8546b95e9&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6c6a94a53e3948b6a64931237dacf4b1&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7dd700bcb22d4b04bf0f30d64696e2a3&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0d1f750e8ac24250ac8d57c4894ba400&docGuid=8MDJnRyP6P6BNF "")
一次输出的结果截图如下

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1948c95fd5e24fecbc78557b952ef149&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a849e43af2094b6c86ae0938641e135b&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9d0d76c9206f46ebb6f149942bb29018&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=47b99142cdc44d8f8d3f3411c0815375&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=620d51e42ef94a12a769fba42c7cc6dc&docGuid=8MDJnRyP6P6BNF "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f7897939b0404e94b0ddf6a5b9f6882b&docGuid=8MDJnRyP6P6BNF "")




### Coding Agent+模拟器，带来更直观地产品数据可视化分析
这是传统 PM 无法企及的效率：PM 可以直接将产品截图与转化率数据输入Coding Agent。利用 AI 强大的视觉理解能力，PM 要求 AI **直接在按钮旁标注转化率**，并结合用户画像、页面数据、界面设计，给出优化建议。**为 PM 提供了一个“可直接在产品交互图上做数据可视化分析”的工具。**

##### **数据分析**
```
附件是目前现阶段onboarding的每个页面转化率，帮我把这些转化率数据标注到页面中，并且用红色字体，在主要按钮附近，字体不要太大。
在所有页面的左下角，加上一个开关，可以控制：红色字体的转化率标注 展示和关闭展示
```
[附件]


##### **产品分析**
```
根据现在新手流程的转化率情况，结合页面设计，我们的用户性别是**为主，年龄在**之间，消费水平在***，主要国家是**，然后分析一下哪个部分的转化率较低，有什么优化建议
```
[附件]
## 3. 设计师（UE）：从“画图”到“构建AI设计规则”
Coding Agent直出生成页面质量差，不可落地使用，尤其是成熟产品有自己的规范和组件。在直接生成的Prototype上面调整还不如用figma画来的快。有了设计规范作为兜底，才能生成一个70分可用的Prototype，因此需要**将设计规范、组件变成Coding Agent可以读懂的项目知识库，让Coding Agent智****能调用**。UE 的核心竞争力在于将审美转化为 AI 可读的“设计规范建模”。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9e22a0e3d5924b2897296d2e6b6d8408&docGuid=WHUUZGyezz9x7s "")
### 1.三步速成训练设计规范
## 01
#### 把产品截图+以下指令发给Coding Agent，提取组件json
---

**作用：把设计稿变成数据**

类比：把设计师的作品"翻译"Coding Agent 能用的数字

* 设计师提供产品截图
* AI 自动提取：颜色、字体、间距、圆角、组件样式
* 生成design_tokens.json文件（完整的设计规范）
* 简单人工交验色值



```
请帮我从截图中提取设计规范，输出 JSON 文件。

产品类型：[健康/播客/电商/音乐]
平台：[iOS/Android]

【重要】如果截图信息不足：
1. 自动搜索同类产品规范补全（如 Spotify、Apple Music、Nike）
2. 参考 iOS HIG 或 Material Design 3
3. 标注来源：
   - "source": "screenshot" （从截图提取）
   - "source": "industry_standard" （参考标准补充）
   - "source": "inferred" （推断补充）

必须输出完整规范，不能留空！

需要提取：

1. 颜色系统
   - 主色 (primary)：品牌主色，用在哪些地方？（按钮/导航栏/重点文字）
   - 辅助色 (secondary)：次要操作，用在哪些地方？
   - 强调色 (accent)：特殊状态，用在哪些地方？（徽章/通知）
   - 文字颜色：主文字/次要文字/提示文字/禁用文字（含透明度）
   - 背景颜色：页面背景/卡片背景/分组背景
   - 语义色：成功 (success) / 警告 (warning) / 错误 (error) / 信息 (info)
   - 分隔线颜色
   - 深色模式：是否有？如有，列出所有颜色的深色版本

2. 字体规范（至少 5 种）
   - largeTitle：页面主标题（字号/字重/行高/使用场景）
   - title1-3：各级标题
   - body：正文（字号/字重/行高）
   - callout：重点说明
   - caption：辅助说明、时间戳
   - 字体家族：SF Pro / Roboto / 自定义字体？

3. 间距系统（至少 6 档，建议 8pt 网格）
   - xxs: 4px
   - xs: 8px
   - sm: 12px
   - md: 16px
   - lg: 20px
   - xl: 24px
   - xxl: 32px
   - 特殊间距：屏幕左右边距？Section 之间间距？

4. 圆角规范（至少 3 档）
   - 小圆角：图标、小标签（4-6px）
   - 中圆角：按钮、卡片（8-12px）
   - 大圆角：底部弹窗、大卡片（16-20px）
   - 全圆角：头像、FAB 按钮（9999px）

5. 阴影规范
   - 轻阴影：卡片悬浮感（offsetY / blur / color / opacity）
   - 中阴影：弹窗、底部栏
   - 重阴影：模态框背景遮罩

6. 按钮组件（必须包含所有状态）
   主按钮 (primary)：
   - 尺寸：高度/最小宽度/内边距（左右）
   - 样式：圆角/背景色/文字颜色/字号/字重
   - 状态：
     * 默认 (default)
     * 按下 (pressed)：透明度/颜色/缩放变化
     * 禁用 (disabled)：透明度/颜色
     * 加载 (loading)：是否有？动画样式？
   - 图标：是否支持？位置（左/右）？
   - 动画：点击反馈（涟漪/缩放/颜色变化）
   - 触觉反馈：轻/中/重？
   
   次按钮 (secondary)、文字按钮 (text)、图标按钮：同样提取

7. 卡片组件
   - 尺寸：固定高度还是自适应？宽度？
   - 样式：圆角/背景色/边框/阴影
   - 内边距：上/下/左/右
   - 内容结构：
     * 图片：位置（顶部/左侧/背景）/高度/圆角
     * 标题：字体样式/颜色/距离顶部
     * 副标题/正文：字体样式/颜色/距离上一元素
     * 底部操作：按钮/图标
   - 交互：点击整个卡片还是特定区域？点击效果？
   - 状态：选中时的样式变化

8. 输入框组件
   - 尺寸：高度/最小宽度
   - 样式：圆角/背景色/边框（颜色/粗细）
   - 文字：字号/颜色/占位符颜色
   - 图标：左侧图标/右侧清除按钮（尺寸/颜色）
   - 状态：
     * 默认 (default)
     * 聚焦 (focused)：边框颜色/背景色/阴影变化
     * 错误 (error)：边框颜色/错误提示文字样式
     * 禁用 (disabled)
   - 键盘类型：文本/数字/邮箱/密码

9. 导航栏组件
   - 高度：导航栏高度/状态栏高度/总高度
   - 背景：纯色/半透明/毛玻璃效果
   - 标题：对齐方式（居中/居左）/字号/颜色/字重
   - 左侧按钮：返回箭头？图标？尺寸/颜色
   - 右侧按钮：最多几个？图标还是文字？尺寸/颜色
   - 分隔线：是否有底部分隔线？颜色/高度
   - 大标题模式：是否支持？滚动时如何收缩？

10. 列表项组件
    - 高度：固定还是自适应？
    - 左侧：图标/头像/复选框？尺寸/距离左侧
    - 中间内容：
      * 标题：字体样式/颜色
      * 副标题：字体样式/颜色/距离标题
    - 右侧：箭头/开关/徽章/时间？尺寸/颜色/距离右侧
    - 分隔线：位置（左侧对齐/全宽）/颜色/高度
    - 内边距：垂直/水平
    - 点击效果：背景色变化/涟漪效果

11. 标签页组件 (Tabs)
    - 位置：顶部还是底部？
    - 样式：下划线/胶囊形/分段控件
    - 高度：标签栏高度
    - 图标：是否有？图标在上/左？尺寸？
    - 文字：字号/未选中颜色/选中颜色
    - 选中状态：
      * 颜色变化
      * 字重变化
      * 下划线/背景动画
    - 徽章：是否支持未读徽章？样式？

12. 对话框/底部弹窗
    - 尺寸：固定高度/最大高度
    - 圆角：顶部圆角大小
    - 背景遮罩：颜色/透明度
    - 关闭方式：下滑/点击背景/按钮
    - 内容结构：标题/正文/操作按钮
    - 出现动画：上滑/淡入？时长？

13. 交互动画
    - 页面切换：淡入淡出/侧滑/缩放？时长？
    - 组件出现：淡入/上滑/弹跳？时长？
    - 按钮点击：缩放/涟漪/颜色变化？时长？
    - 下拉刷新：动画样式？
    - 加载动画：旋转/脉动/骨架屏？
    - 时长标准：快 (200ms) / 中 (300ms) / 慢 (500ms)
    - 缓动函数：ease / ease-in-out / linear？

14. 触觉反馈
    - 哪些操作有震动？
    - 震动类型：轻 (light) / 中 (medium) / 重 (heavy)

15. 文案规范
    - 按钮文案：
      * 主要操作：「确定」「保存」「提交」「继续」「开始」
      * 取消操作：「取消」「稍后」「跳过」
      * 删除操作：「删除」「移除」「清空」
    - 提示文案：
      * 成功：「操作成功」「保存成功」
      * 错误：「操作失败，请稍后重试」「网络连接失败」
      * 警告：「确定要删除吗？此操作无法撤销」
    - 输入提示 (Placeholder)：「搜索...」「请输入...」「选填」
    - 空状态文案：
      * 标题：「这里空空如也」
      * 描述：「快去添加第一个吧」
      * 按钮：「立即添加」
    - 文案风格：正式/轻松？人称（你/您）？最大长度？
    
JSON 格式：
{
  "version": "1.0.0",
  "productType": "...",
  "platform": "...",
  "colors": {
    "primary": { "value": "#007AFF", "source": "screenshot", "usage": "主按钮" }
  },
  "typography": { ... },
  "spacing": { ... },
  "radius": { ... },
  "components": {
    "button": {
      "primary": {
        "height": 50,
        "backgroundColor": "#007AFF",
        "states": { "default": {...}, "pressed": {...}, "disabled": {...} }
      }
    }
  },
  "补全说明": {
    "从截图提取": ["..."],
    "行业标准补充": ["..."],
    "需要确认": ["❗ 所有标注为 industry_standard 的值"]
  }
}
```

```
## 02
#### 检查后的json+以下指令，让Coding Agent写智能调用规则
---

**作用：把组件按功能分类整理**

类比：给组件建立"电话簿"，说"登录"就知道要找谁

* AI 读取第 1 步的设计规范
* 按功能分类组件（展示类/输入类/导航类等）
* 创建"功能→组件"映射表（比如：登录页面需要哪些组件）
* 生成 component_library.json 文件



```
请根据这个设计规范 JSON，生成一个组件库索引文件。

要求：
1. 按功能分类所有组件（展示/输入/导航/反馈/布局）
2. 为每个组件添加使用场景标签
3. 创建功能描述 → 组件映射表
4. 输出为 component_library.json

格式：
{
  "产品类型": "健康/播客/电商/音乐",
  "平台": "iOS/Android",
  
  "组件分类": {
    "展示类": {
      "card": {
        "名称": "卡片",
        "规格": { "从 design_tokens.json 提取" },
        "使用场景": ["内容展示", "列表项", "专辑/播客封面", "商品卡片"],
        "关键词": ["内容", "卡片", "列表", "展示", "封面", "商品"],
        "适用功能": ["首页推荐", "分类列表", "搜索结果", "个人收藏"]
      },
      "avatar": {
        "名称": "头像",
        "规格": {...},
        "使用场景": ["用户头像", "作者头像", "主播头像"],
        "关键词": ["头像", "用户", "个人", "作者", "主播"],
        "适用功能": ["个人中心", "评论区", "作者信息"]
      }
    },
    
    "输入类": {
      "button": {
        "名称": "按钮",
        "规格": {...},
        "使用场景": ["主要操作", "次要操作", "取消操作"],
        "关键词": ["按钮", "提交", "确认", "取消", "操作", "点击"],
        "适用功能": ["表单提交", "确认操作", "播放/暂停", "购买"]
      },
      "input": {
        "名称": "输入框",
        "规格": {...},
        "使用场景": ["文本输入", "搜索", "表单填写"],
        "关键词": ["输入", "搜索", "填写", "文本", "表单"],
        "适用功能": ["搜索功能", "登录注册", "编辑资料", "发表评论"]
      },
      "searchBar": {
        "名称": "搜索栏",
        "规格": {...},
        "使用场景": ["页面搜索", "全局搜索"],
        "关键词": ["搜索", "查找", "过滤"],
        "适用功能": ["搜索歌曲", "搜索播客", "搜索商品", "搜索课程"]
      }
    },
    
    "导航类": {
      "navigationBar": {
        "名称": "导航栏",
        "规格": {...},
        "使用场景": ["页面顶部导航", "返回导航"],
        "关键词": ["导航", "顶部", "返回", "标题", "头部"],
        "适用功能": ["所有页面", "详情页", "设置页"]
      },
      "tabBar": {
        "名称": "标签栏",
        "规格": {...},
        "使用场景": ["底部导航", "主要入口"],
        "关键词": ["标签", "底部", "导航", "Tab", "入口"],
        "适用功能": ["首页", "分类", "我的", "播放"]
      },
      "segmentedControl": {
        "名称": "分段控件",
        "规格": {...},
        "使用场景": ["内容切换", "筛选选项"],
        "关键词": ["切换", "分段", "选项", "筛选"],
        "适用功能": ["订阅/推荐切换", "男装/女装切换", "今日/本周切换"]
      }
    },
    
    "反馈类": {
      "toast": {
        "名称": "轻提示",
        "规格": {...},
        "使用场景": ["成功提示", "错误提示", "警告提示"],
        "关键词": ["提示", "通知", "消息", "成功", "失败"],
        "适用功能": ["操作反馈", "保存成功", "网络错误"]
      },
      "modal": {
        "名称": "弹窗",
        "规格": {...},
        "使用场景": ["确认操作", "重要提示", "表单输入"],
        "关键词": ["弹窗", "对话框", "确认", "提示"],
        "适用功能": ["删除确认", "退出登录", "权限申请"]
      },
      "bottomSheet": {
        "名称": "底部弹窗",
        "规格": {...},
        "使用场景": ["操作菜单", "选择器", "详情展示"],
        "关键词": ["底部", "菜单", "选择", "操作"],
        "适用功能": ["分享菜单", "更多操作", "时间选择", "地区选择"]
      }
    },
    
    "布局类": {
      "listView": {
        "名称": "列表",
        "规格": {...},
        "使用场景": ["垂直滚动列表", "设置列表"],
        "关键词": ["列表", "垂直", "滚动"],
        "适用功能": ["播客列表", "订单列表", "设置项", "评论列表"]
      },
      "gridView": {
        "名称": "网格",
        "规格": {...},
        "使用场景": ["多列展示", "相册", "商品列表"],
        "关键词": ["网格", "多列", "瀑布流"],
        "适用功能": ["专辑封面", "商品展示", "图片墙"]
      },
      "horizontalScroll": {
        "名称": "横向滚动",
        "规格": {...},
        "使用场景": ["分类切换", "推荐卡片"],
        "关键词": ["横向", "滚动", "轮播"],
        "适用功能": ["推荐内容", "分类标签", "故事/动态"]
      }
    }
  },
  
  "功能映射表": {
    "用户相关": {
      "登录/注册": ["input", "button", "navigationBar"],
      "个人中心": ["avatar", "listItem", "navigationBar", "card"],
      "编辑资料": ["input", "avatar", "button", "navigationBar"],
      "设置": ["listItem", "switch", "navigationBar"]
    },
    
    "内容浏览": {
      "首页": ["navigationBar", "searchBar", "card", "horizontalScroll", "tabBar"],
      "列表页": ["navigationBar", "card", "listView", "tabBar"],
      "详情页": ["navigationBar", "card", "button", "horizontalScroll"],
      "搜索": ["searchBar", "card", "listView", "segmentedControl"]
    },
    
    "内容操作": {
      "播放/观看": ["navigationBar", "button", "slider", "bottomSheet"],
      "收藏/点赞": ["button", "toast"],
      "分享": ["button", "bottomSheet"],
      "评论": ["input", "button", "listView", "avatar"]
    },
    
    "购物流程": {
      "商品列表": ["card", "gridView", "searchBar", "segmentedControl"],
      "商品详情": ["card", "button", "bottomSheet", "horizontalScroll"],
      "购物车": ["listItem", "button", "checkbox"],
      "结算": ["listItem", "button", "input", "modal"]
    }
  }
}
```

```
## 03
#### 通过rules让Coding Agent记住遵循设计规范
---

**作用：只说需求，Coding Agent自动生成代码**

类比：把Coding Agent 培训成"懂设计规范的开发助手"

* 说："我要一个登录页面"，Coding Agent自动：
* 查映射表 → 知道需要输入框、按钮、导航栏
* 读设计规范 → 知道具体尺寸、颜色
* 生成代码→ 完全符合设计规范



```
你是一个移动应用开发助手，项目中有完整的设计规范和组件库。

## 工作流程

当用户描述想要实现的功能时：

### 1. 理解需求
- 识别功能类型（展示/输入/导航/反馈/布局）
- 提取关键词（搜索/列表/详情/按钮/卡片等）
- 确认所属模块（用户/内容/购物等）

### 2. 匹配组件
根据 `component_library.json`：
- 在「功能映射表」中查找匹配的功能
- 获取推荐的组件列表
- 从「组件分类」中提取具体规格

### 3. 生成代码
使用 `design_tokens.json` 中的精确数值：
- 颜色：使用定义的色值（如 colors.primary）
- 尺寸：使用定义的间距/圆角（如 spacing.md, radius.lg）
- 字体：使用定义的字体样式（如 typography.body）
- 组件：使用规范中的完整样式

### 4. 输出说明
- 列出使用的组件
- 说明为什么选择这些组件
- 标注可调整的参数

## 匹配规则

### 关键词匹配优先级
1. **高优先级**：直接功能词（登录、搜索、购买）
2. **中优先级**：组件词（按钮、卡片、列表）
3. **低优先级**：场景词（首页、详情、个人）

### 组件选择原则
1. **必须使用**：
   - 所有页面都有 NavigationBar（除了启动页）
   - 有底部导航的用 TabBar
   - 有用户操作的用 Button

2. **优先使用**：
   - 内容展示 → Card
   - 数据输入 → Input
   - 列表展示 → ListItem
   - 操作反馈 → Toast

3. **按需使用**：
   - 重要确认 → Modal
   - 操作菜单 → BottomSheet
   - 内容切换 → SegmentedControl

### 代码规范
1. **颜色**：必须使用 design_tokens.json 中的定义（如 colors.primary）
2. **间距**：必须使用间距系统（如 spacing.md）
3. **圆角**：必须使用圆角规范（如 radius.md）
4. **字体**：必须使用字体规范（如 typography.body）
5. **标注来源**：每个关键数值都注释来源

## 特殊场景处理

### 场景 1：组件库没有的组件
如果用户需要的组件在 component_library.json 中找不到：
1. 使用最接近的组件
2. 基于设计系统推断规格
3. 说明这是推断的，建议设计师确认

### 场景 2：多个组件都适用
如果多个组件都符合需求：
1. 列出所有选项
2. 说明每个的适用场景
3. 推荐最常用的

### 场景 3：需要自定义
如果需求超出标准组件：
1. 使用基础组件组合
2. 保持设计系统一致性（颜色/间距/圆角）
3. 说明自定义部分

## 响应格式

对每个功能需求，按以下格式回复：
1. 需求分析：简述理解的需求
2. 推荐组件：列出组件并说明理由
3. 实现代码：完整代码，使用设计规范中的精确数值
4. 设计说明：列出使用的颜色/间距/可调整项

## 注意事项

1. **必须使用设计规范**：所有数值都来自 design_tokens.json
2. **标注来源**：每个关键数值都注释来源（如 // spacing.md）
3. **保持一致性**：同类组件使用相同规格
4. **响应式设计**：考虑不同屏幕尺寸
5. **可访问性**：确保最小点击区域 44x44
```


Coding Agent没有设计规范直出效果

[附件]
将ios产品的色值/图标/字体/组件/页面/文案写作方式喂给Coding Agent后，一次性的生成效果

[附件]
##### 2.生成界面
##### 确定性非常高的小功能
比如在现有界面加个功能模块，加个弹窗

---

最快的方式是在网上找好参考布局。贴上自己想要的内容作为原型图。因为Coding Agent的弱项是生成漂亮布局。

|网上的参考图👉|给Coding Agent的示意图👉|生成结果✅|
|-|-|-|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=63d3b8c1467b420ea787f3c7faa22c13&docGuid=bWQv3xOmWWD59w "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fbda3bfbee83407b8f656a420016e74f&docGuid=bWQv3xOmWWD59w "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c54659c5eec0413e856ed9ac4aef7a43&docGuid=bWQv3xOmWWD59w "")|



#####  比较大的需求
例如要加一个xx功能，涉及到页面跳转。

---

口头描述想要的功能流程+Coding Agent的plan模式让他先生成demo，再在demo上调整。Coding Agent能帮你完成一个70分的方案，有很多东西不用全靠自己干巴想或磕像素。

|prompt👉|生成初版👉|调整布局✅|
|-|-|-|
|1.我要在产品内加一个收藏功能。出现位置xxx。2.收藏页面展示收藏的prompt，样式如图2再在卡片内最下方加一个copy和一个取消收藏的按钮。排序方式按收藏时间排序。3.在xxxx加一个收藏功能，点击表示已收藏，可以在此处取消收藏。![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=99a425831c1b47d9937f8ca332d14c87&docGuid=bWQv3xOmWWD59w "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bd4ecd18fbab4183ba9d03acfa8070e2&docGuid=bWQv3xOmWWD59w "")这个页面的预览图应该展示的是prompt内容，类似模版库prompt二级页的prompt样式。不需要标题和播放量。删除和copy左右换个位置。|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=04f98d2350ed46ae8e8add0157dfe4d7&docGuid=bWQv3xOmWWD59w "")|

##### 3.调整界面
##### 口头描述+截图，类似进行视觉还原验收
在图上标红Coding Agent生成的问题、或口头描述问题直接指挥 AI 进行修正

---

* 一次如果要改的很多就截图预览，在截图上标注问题

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ab9966a66a848a78b032bf397b806b7&docGuid=bWQv3xOmWWD59w "")
* 也可以直接截图标明要改的1、2、3点。有具体想要的数值更好

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8e45094e6b174c79b0b1f3d929cab8b4&docGuid=bWQv3xOmWWD59w "")
* 如果让她改完发现还没改之前好看，就撤回差的指令

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=def328ff5b3941a3bcf29ea63687d975&docGuid=VkAlqGiFyZuPlD "")


#####  上传设计资源
产品中的字体、特殊图标或富视觉元素优先采用上传的形式

---

* 图标文件放到最左侧资源面板

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=864e7786534a4e2e888eecfca94dceeb&docGuid=bWQv3xOmWWD59w "")
拖入对话框，告诉Coding Agent要放在哪里

[附件]


#####  生成交互动效
自然语言描述即可，不知道怎么描述可以让GPT生成prompt

---

* 把想要的动效参考传给GPT（因为Coding Agent不支持传视频）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=df56565d16f44a4399b1ee119637ac1e&docGuid=bWQv3xOmWWD59w "")
用GPT给的prompt+自然语+截图让Coding Agent生成

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0e72b5ff347845a0b3857398531bab1b&docGuid=bWQv3xOmWWD59w "")


**🌟 ****在Rules里加上：每次更新后都帮我在simulator中打开预览**

这个很重要，不然每次改完要手动刷新。



通过“设计代码化”，视觉还原度痛点消失，UE 的精力从“像素对齐”释放到了“产品策略与用户体验”的深度思考中。同时前端代码可复用率较高，不需要进行视觉还原，研发效率也得到了大幅提升，产品也可以自己改一些视觉活不大的需求。

## 4. 研发（RD）：从“前端还原”转变为“管理脚手架的架构师”与“辅导老师”
研发的角色从“切图与 UI 编写”升维到了整条链路的“总架构师”与“管控者”。RD 不再是负责基础界面的拼装，而是负责定义规则并确保代码安全。

RD 扮演“辅导老师”角色，PM/UE 则是“写作业的学生”。

* **环境先行：** RD 统一配置工程环境并提供脚本，确保非技术同学能安全地进行 Vide Coding。
* **批改与归档：** RD 通过 Code Review (CR) 严控代码质量，统一处理冲突并合入主分支。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c4b6ab1bc6304903bdbdbd6c23ef923e&docGuid=WHUUZGyezz9x7s "")
##### 代码提交&代码更新流程，保证代码统一管理和减少冲突问题
[流程图]
##### **代码提交要求**
##### **协定代码改动范围**
##### **非技术同学Vide Coding**
##### **技术同学CR代码**
在UE、PM进行Vide Coding前与RD协定好这次提交需要做的事情，把可能的代码变动圈定在一个合理的范围内

1. 保证在新的分支和代码下进行开发
2. 提交改动的代码到iCode评审
3. 拉取PM、UE提交的代码，进行问题修复和业务逻辑补充
4. 重新提交代码并在iCode评审和后合入



**如何让PM/UE同学安全上手？----极简指令与质量分层 (Practical Tips)**

* **零门槛 Git 接入**：

无需让 PM/UE 理解复杂的 Git 原理，只需封装并教给他们两条核心指令：

    1. `New Branch`：基于最新代码切出本地分支。

    2. `Push`：完成修改后推送到远程。

* **质量把控的分层策略**：

    ◦ **PM/UE 层（UI/交互）**：负责界面展示和交互流程的验收（第一道防线）。

    ◦ **RD 层（逻辑/稳定性）**：RD 不需要重复测 UI，而是聚焦于**异常逻辑兜底**（Exception Handling）、**崩溃检测**以及**核心业务逻辑**的健壮性。客户端特性决定了 RD 的安装包级测试是最终兜底，流程上风险可控,。

这种模式下，前、后端开发实现了真正的并行。当 PM/UE 还在构建 UI 的前 80% 时，RD 已在同步定义数据结构与后端接口，大幅压减了最后的联调周期。

## 5. 角色边界灵活，人人都是需求owner
在这样的模式下，我们也发现，不同角色的边界变得更加灵活，谁最接近核心问题的解决，谁就可以牵头，发挥所长。在实践中也逐渐发现，不同角色都可以主导不同类型的需求。

|**适合牵头的角色**|**适合牵头的需求**|
|-|-|
|**PM**|0-1 新方向/新产品的快速探索与验证（如MVP、简单工具、全新功能模块等）交互逻辑并不复杂的数据/流程分析还原基于现有成熟产品做简单的功能增删（如增加一个入口、调整简单的跳转逻辑）|
|**设计（UE/UX）**|视觉与交互体验的精细化打磨（如动画特效、界面细节调整、复杂交互逻辑的优化等）资源替换与视觉迭代（如更换皮肤、调整视频素材、更新营销物料、修改 UI 布局等纯视觉类的改动）高复杂度视觉需求（AI 难以理解或生成的极其复杂的视觉效果）|
|**研发（RD）**|重后端逻辑与数据结构的需求（如涉及复杂的服务端交互、数据结构定义、推送通知（Push）、支付逻辑、底层算法等）工程基建与复杂逻辑攻坚（如搭建模拟器环境、编写定位工具、维护代码规范Rules、解决代码冲突以及 Code Review）|

这样一来，PM 和 UE 在调整页面和交互时，RD 可以同时准备数据接口和后端逻辑，并在中间某个节点“串联”起来。每个角色都可以主导需求，每个人都是 Owner---PM 关注产品价值验证，UE 关注最终体验交付，RD 关注系统稳定与逻辑实现。这种模式让每个人都对最终上线效果负责，而不是只对自己那个环节的交付物负责。

## 6. 组织借鉴：如何复制海外输入法团队的提效模式？
这套模式能够跑通，源于对生产力工具底层重构后带动的“生产关系”调整。如果你也想在你的团队跑通这套模式，以下这些方面值得注意：



**认知与共识**

* **统一协作语言：** 共识全员统一到 Coding Agent + Flutter 的代码层对话。
* **认知同频：** 顺延AI优势——让 AI 处理 70% 的标准化重复劳动（如 UI 还原），让人类处理 30% 的策略决策与核心逻辑。



**精准定位工具（最重要的基建）**

* **类名开关：**为了解决 PM/UE 无法找到对应代码文件的问题，研发开发了一个“可视化定位开关”。非技术同学在模拟器中点击即可直观定位类名，从而在Coding Agent中精准圈定修改目标。是保证非技术同学不破坏全局架构的关键。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d9c1e05a019147b598319567c37cb159&docGuid=WHUUZGyezz9x7s "")


**代码与工程环境的封装**

* **环境搭建自动化**：研发需要协助 PM/UE 在本地搭建好 Flutter 运行环境和模拟器，或者通过Coding Agent 的引导让环境搭建变得傻瓜化，确保非技术人员也能把工程跑起来。
* **范围约束（Scope）**：研发需要约定好代码结构，或者在工程上做限制，确保 PM/UE 的修改主要集中在 **View/UI 层**，而不触碰核心网络请求、底层架构等高风险代码区域。



**知识库与规范的注入（Context）**

* **代码规范（Rules）**：研发将项目的编码规范（如网络请求写法、命名规范）整理成文档（如 `.mdc` 或 Rules 文件）。当 PM/UE 生成代码时，AI 会自动读取这些规范，确保生成的代码是“可用”的，减少研发后续 Review 的成本。
* **设计规范（Rules）**：UE 将设计系统的 Token（颜色、间距、组件库）整理成 JSON 或 Prompt 上下文。AI 读取这些上下文后，能直接生成符合设计规范的 UI（如“使用标准高亮色”），而不是随机生成颜色值。



**代码管控与协作流（Workflow）**

* **前置对齐：**不再依赖详尽的 PRD 文档评审。在迭代开始前，全员（PM/UE/RD）召开简短的“前置对齐会”。明确哪些界面由 PM/UE 直接生成，哪些复杂逻辑由 RD 接手，以及核心的改动范围。RD 在此阶段直接介入产品设计，补充异常流程和边缘情况的设计，而非等待需求文档流转。
* **更新脚本**：提供简单的脚本工具，让 PM/UE 在开始工作前能“一键拉取最新代码”并清空本地脏数据，避免版本冲突。
* **分支管理策略**：制定明确的代码提交规则。PM/UE 在独立的分支（Feature Branch）上工作，研发负责最终的 Code Review、冲突解决和合并上线。研发类似于“改作业的老师”，把控最终代码质量。



**适用边界**

* **✔️适用场景：**新方向快速探索、0–1 框架构建、新功能迭代；多个版本的方案对比测试；提前搭建原型后，快速体验筛选低分方案
* **❌ 限制场景：**需要原生能力的模块、高复杂度视觉，需要设计师人工出图



**构建会成长的 AI 知识库**

* **Step-by-Step 任务拆解**：不要试图让 AI 一次性生成所有代码。RD 的经验是：先让 AI 生成框架 -> 再填充页面细节 -> 最后单独引用特定的 Rules（如`network.mdc`或`analytics.mdc`）来补全网络请求和打点逻辑。分步注入上下文，准确率更高。
* **项目记忆工程 (Project Memory)**：目前主要通过维护 `.mdc` (Rules) 文件沉淀业务规范。未来可以尝试在代码库中建立 “Readme for AI” 或 “Change Log for AI”。每次迭代后，自动或手动将关键的架构变动、踩坑经验更新到此文档中，甚至构建本地图数据库（Graph DB）。让 AI 在下一次任务中能检索到“历史经验”，从而越用越聪明，而不是每次都从零开始。



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=31f05062978e47a2a335bc8d0fbd3bd4&docGuid=WHUUZGyezz9x7s "")


## 7. 拥抱 AI，释放团队智慧
AI 正在打破传统职能部门之间的壁垒。通过一个 AI 驱动的共享中心，不同角色可以实时地进行“生产力对接”，实现更高效率的**原生 AI 协作，**从 Hand-off（交付）到 Hand-shake（握手）**。**

AI 全流程设计的核心并非取代人类，而是通过重构协作语言，将 PM 从文档中解放，将 UE 从像素中解放，将 RD 从繁琐的还原中解放。**人的智慧应该投入到那关键的 20% 核心决策与策略思考中**。

如今大家已经纷纷在“个人工具提效”涌现大量先锋实践，开始思考向“**团队协同提效**”转型，让代码库成为组织智慧的统一语言，共同步入 AI 原生工作流，让每个人都可以成为创造者。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=91accfb25bf54c52b6fe3eb3c23d3630&docGuid=WHUUZGyezz9x7s "")
## **🚀 还想知道更多实操细节？直播间见！**
文字可以总结方法论，但很难还原我们在转型过程中的纠结、冲突与顿悟。

**3月11日 15:00-17:30**，BIT邀请海外输入法团队举办** ****“AI 全流程设计与开发”**** 专场直播分享**。将带来**负责人、产品、设计、研发**将带你通过**四个完全不同的视角**，还原这场效率革命的真实全貌，干货拉满。

如果你也是一名正在探索AI 提效的 PM、设计师、研发，或者是团队管理者，这场分享也许能给你带来共鸣与启发。



**👇 有问题？现在就问！**关于这套新模式，你最关心什么？

• 是工具链的搭建细节？

• 是跨角色的协作边界？

• 还是团队转型的阵痛与解法？

... ... 

**💬 ****评论区互动**：**对于这次分享或者这几个角色，你好奇什么问题？**

欢迎在评论区留言（例如：“@研发，我想知道怎么处理代码冲突？”），会在直播分享中回应哦！



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
