---
title: "一、知识库随心搭是什么？"
description: "🔥知识库随心搭中的Prompt实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\🔥知识库随心搭中的Prompt实践.md"
---
🔥知识库随心搭中的Prompt实践

#### 🧑‍🏫 案例作者：[@李港](https://ku.baidu-int.com?t=mention&mt=contact&id=a32d45e0-fcec-11f0-85b2-4f8c2f4407df)
#### 🎬 案例场景：办公
#### 🔧 使用工具：随心搭
#### 📒 案例概要：本文介绍了知识库随心搭功能，用户可通过自然语言生成可运行的功能组件，无需代码编写。随心搭组件支持动态交互、数据操作，并能自动利用文档信息。文章提供了搭建随心搭的步骤和实用Prompt技巧，包括下定义、搭框架、调细节等，助力用户低成本搭建个性化应用，实现知识库场景下的高效内容生成与管理。

[文档目录]
**本文档视频讲解：**[知识库随心搭中的Prompt实践：手把手教你搭建第一个随心搭](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56683?activityId=8435?t=mention&mt=doc&dt=sdk)*（👈10min，点击学习）*

# 一、知识库随心搭是什么？
**知识库随心搭是一种“用说话就能搭应用”的能力，内置在知识库里。**你只需要告诉它你想做什么，它就能自动帮你生成一个可运行的功能、工具，直接放进文档里使用。

### 用自然语言就能生成组件
你只要说一句话，比如：

* “做一个投票给团队选择会议时间”
* “把这段数据做成柱状图”

随心搭就能自动理解并生成对应的组件，不用写代码。

### 组件在文档里直接使用
随心搭做出来的内容不是图片，也不是装饰，而是“能动的”：

* 可以点按钮
* 可以提交信息
* 可以操作数据

所有操作都在文档里完成，不用跳系统、不用开发、不用部署。

### 更理解知识库场景
随心搭天然懂知识库，因此能自动用到文档里的信息。比如组件可以：

* **读文档内容**（如自动总结文档内容）
* **读评论内容**（如根据大家的评论统计“最常提的问题”）
* **知道是谁在使用**（如自动记录填写人、不需要他自己输入名字）
* **存/取数据**（如记住谁已经投过票）

### **可修改、可复用**
生成后仍可：

* 编辑逻辑和样式
* 调整布局与展现
* 直接复制，供团队共享与复用

让低成本搭建变成真正“人人可用”。

# 二、如何搭建一个随心搭
在文档空白行输入`/`或点`+`，选择“随心搭”。也可在顶栏或“插入”菜单中找到。

![顶部工具栏](/personal-site-mvp/img/doc-placeholder.svg "顶部工具栏")
![空白行斜杠菜单](/personal-site-mvp/img/doc-placeholder.svg "空白行斜杠菜单")
![空白行+号菜单](/personal-site-mvp/img/doc-placeholder.svg "空白行+号菜单")


![顶部](/personal-site-mvp/img/doc-placeholder.svg "顶部")
进入随心搭后，可用模板，也可点 **【自定义】** 进入对话空间。像聊天一样输入指令，例如：“生成一个动态自我介绍卡片”。AI 会自动生成代码。

![自定义入口](/personal-site-mvp/img/doc-placeholder.svg "自定义入口")
![对话空间](/personal-site-mvp/img/doc-placeholder.svg "对话空间")
![代码生成](/personal-site-mvp/img/doc-placeholder.svg "代码生成")


预览区会自动渲染组件点击**【发布版本】**，组件即插入到文档中。

![生成后效果](/personal-site-mvp/img/doc-placeholder.svg "生成后效果")
![发布版本后，可看到最终文档内效果](/personal-site-mvp/img/doc-placeholder.svg "发布版本后，可看到最终文档内效果")


# 三、玩转随心搭的实用Prompt技巧
## 基础玩家
## 1️⃣ 下定义
---

###### 先总结一下我想要一个什么样的组件
* 荣誉墙？
* 邀请函？
* 调研问卷？

**一个概括性强的组件名称，是随心搭定调的第一步**

还有**意外惊喜💓**！当你没有想全组件有哪些功能的时候，通过下定义，随心搭可以提供行业通用示例，帮助你**找灵感**

###### 再补充组件整体的风格
* 用流行元素 eg：超级玛丽、赛博朋克
* 用具体的颜色 eg：浅蓝绿色、具体的色值
* 让它自由发挥 eg：科技感、神秘感、动态交互

## 2️⃣ 搭框架
---

###### **想想你要的组件需要哪些功能？一般来讲：**
👀 一个组件会有**管理员视角**

* eg：编辑文案、导出明细、统计数据、管理名单

👀 也会有**普通用户视角**

* eg：报名活动、填写问卷、互动留言



按照上述分类标准，你已经确定了需要的功能框架

如果**文档的成员权限已经足够**区分功能权限，那这样输入已经足够：

* 文档编辑态：实现管理员的功能，XXX
* 文档阅读态：实现普通用户功能，XXX



如果还想要有**更精细的权限管理：**

* 可以通过在编辑态设置名单管理的功能，指定在名单用户才能使用功能、其他人显示没有权限

## 3️⃣ 调细节
---

###### 如果完成了前两步，应该已经生成了9成的组件
现在就剩下细节的调整了，按照以下思路进行：

* **明确文档状态**：调整文档编辑态/阅读态的功能
* **明确具体位置**：个人信息模块/留言板模块
* **描述更改信息**：不展示头像/补充一个点赞功能



**⚠️提示**：如果组件的页面、功能比较多，描述的路径就需要更详细一些，方便AI定位。

eg：将文档阅读态，写感谢信弹窗中，添加老师的弹窗中，增加“课程”字段。



#### 现在，就让我们用上面的三步走方法论，实际体验一下如何写一个prompt吧！
##### 💡 有一个idea、先找找灵感
给一个大概的描述，看看AI怎么理解

**✅ 目标**：生成一个只有指定人员可以答题的问卷

**✍️ prompt**：

生成一个调研问卷组件，整体要浅蓝绿色风格，增加一些动态感的元素；需要管理名单的功能，只有指定的人可以填写问卷

##### 👍 需求很明确、想要生成一步到位
需要在prompt中描写清楚你的业务逻辑

**✅ 目标**：生成一个只有指定人员可以答题的问卷

**✍️ prompt**：

*下定义* 生成一个调研问卷组件，整体要浅蓝绿色风格，增加一些动态感的元素

*搭框架*

文档编辑态：需要问题管理、名单管理、问卷明细三个模块

1. 问题管理：支持增删改问题、设置问题是否必答、支持单选、多选、填空三种类型题目、每个题目都要填写名称、描述；选项只需要填写名称
2. 名单管理：支持增删改用户名单（包括：用户姓名、邮箱）、支持批量上传名单，提供csv格式的模板。只有在名单管理的用户、才可以在阅读态回答问卷；其他用户显示没权限
3. 问卷明细：展示所有完成问卷的用户明细，包括：时间、用户姓名、邮箱、每道题的答案。支持导出为CSV。展示用户数量

文档阅读态：需要展示所有问题、支持名单管理的用户答题

*调细节*

1. 风格调整：整体风格调整为暗黑色系
2. 功能调整：文档编辑态、单选和多选的选项，支持选择“填空”类型；当用户在阅读态选择该选项，可以填写文本

## 高阶玩家
### 2.1 特色能力
**数据可留存**：用户在组件里的操作（填表、投票等）可以保存，下次打开还在。

prompt参考：

* 利用存储能力，使得生成出来的最新图表会被保存，并且刷新后仍然展示该图表
* 每一个用户填写问卷的数据都会被记录，并且可以点击“下载”按钮下载包含所有填写数据的csv格式的表格

**识别用户信息：**可以获取当前用户头像、昵称、邮箱，并记录操作时间。

prompt参考：

* 每个用户完成评分后会显示其评分结果和自己对应的头像、用户名
* 编辑态支持下载当前所有评分用户的评分数据结果，下载为包含用户名、用户邮箱、评分时间、评分值四个字段的csv格式表格

**读取文档内容：**获取全文或部分内容，用于后续处理或展示。

prompt参考：

* 请利用接口能力读取全文内容并调用AI进行总结
* 请利用接口能力读取全文内容并调用AI解析提取其中关于“项目安排”的内容，然后将其用时间线的形式展现出来
* 请读取全文并提取全文标题结构填入输入框中

**读取评论内容：**可以获取评论区（含划线评论和底部评论）的全部内容。

prompt参考：

* 请利用接口能力读取评论区的内容，并调用AI将所有评论内容进行总结分析为聚合观点

**视图切换**：组件可在只读态和编辑态展示不同内容。

prompt参考：

* 请区分只读态和编辑态的显示页面，编辑态下用户可以通过编辑器对图表样式进行调整，只读态不显示编辑器，仅显示图表

**调用 AI：**将获取到的内容交给 AI，总结、提取或改写。

prompt参考：

* 请利用接口能力调用AI进行总结
* 请利用接口能力调用AI解析提取关于“项目安排”的内容，然后将其用时间线的形式展现出来

### 2.2 组件样式
###### 1. 给组件设置背景图片+主题色
---

推荐prompt：

请在编辑态新增上传背景图片的功能，要求：

1.  用户可以上传图片作为组件背
2. 支持预览和删除背景图片
3. 背景图片要保存到系统设置中
4. 根据上传图片的颜色占比提取不同色阶主题色做组件的配色，其中提取一个深色，用来做文字色

###### 2. 调整组件为明确的颜色
---

推荐prompt：

请你将xx的主色调改为深蓝色（#1e40af）

> ps:具体的颜色和色号编码可以在此查询[https://www.figma.com/color-palettes/](https://www.figma.com/color-palettes/)
###### 3. 调整组件为某类样式
---

推荐prompt：

组件底层画布颜色修改为「蓝绿渐变并增加流动的动态效果」

###### 4. 精准修改组件样式
---

推荐prompt：

* 「阅览态/编辑态」下的「xxx」模块中的「xxx」样式由「xxx」修改为「xxx」样式
* 「阅览态/编辑态」下的「xxx」模块中的「xxx」文案颜色改为「#1e40af」

###### 5. 给组件增加动态效果
---

推荐prompt：

* 组件整体增加「全息投影/浮动例子」效果
* 组件整体风格采用「极客风格/卡通风格/游戏（超级玛丽）风格/梦幻/漫画/卡通风格」
* 「阅览态/编辑态」下的「xxx」模块中的「xxx」文字增加逐字弹跳动画
* 「阅览态/编辑态」下的「xxx」模块中的「xxx」位置的头像增加轻微的呼吸式缩放

###### 6. 复制其他组件样式
---

推荐prompt：

将以下描述主题样式的代码

**「** {

        id: 'royal_purple', name: "紫霞幻境",

        backgroundStyle: { backgroundImage: 'linear-gradient(135deg, #C299FF, #808AFF)' },

        numColor: '#FFFFFF', titleColor: '#FFFFFF', labelColor: 'rgba(255,255,255,0.7)', separatorColor: 'rgba(255,255,255,0.5)',

        timeBlockStyle: { backgroundColor: 'rgba(255, 255, 255, 0.2)', backdropFilter: 'blur(4px)' }

    }**」**复用至当前组件中

###### 7. 调整布局
---

推荐prompt：

文档阅览态下XXX模块中的「案例」卡片一排只展示「3」张

###### 8. 提高屏效
---

推荐prompt：

「阅览态/编辑态」下的「xxx」模块中的「作品/数据/案例」明细增加「竖直向/水平向」滑动轴，一屏最多展示「6」个明细，超出部分滑动滑动轴查看

###### 9. 移动端适配
---

推荐prompt：

「阅览态/编辑态」下的「xxx」模块中的「xxx」）移动端展示界面自适应（通过window.isMobile判断是否是移动端，而不是通过屏幕宽度）

###### 10. 头像展示修复
---

推荐prompt：

**「xxx」**位置获取并展示用户*头像*（avatar）/获取用户邮箱（email）/获取中文名（nickname）/获取英文名（name）

###### 11. 输入框内容失焦修复
---

推荐prompt：

避免在组件中声明其它组件，请将嵌套的组件拆分出来

###### 12. 弹框位置固定
---

推荐prompt：

**「xxx」**位置触发的弹窗的CSS属性修改为：position: fixed;高度top为当前按钮位置（或者为**「xxx」**px），弹窗水平居中，去掉transform属性

### 2.3 权限控制相关
###### 1. 只有白名单用户可以查看所有人数据
---

推荐prompt：

请在编辑态添加用户权限管理功能：

1. 设置一个白名单，可以添加/删除用户邮箱

2. 白名单中的用户可以查看所有人的数据

3. 普通用户只能查看自己提交的数据

4. 在系统设置中管理白名单

###### 2. 只有白名单用户可以查看使用组件
---

推荐prompt：

编辑态下的XXX模块中新增下载csv模板功能和导入「评委明细」功能，支持一键导入「评委明细」的csv文件，阅览态时仅导入名单中的用户可「查看/使用」组件



###### 3. 某个模块设置可见状态
---

推荐prompt：

编辑态下的中新增「权限控制」开关。当开关开启时，阅读态下「xxx」模块展示；当开关关闭时，阅读态下「xxx」模块隐藏

### 2.4 组件功能相关
###### 1. 增加/删除内容
---

推荐prompt：

* 「阅览态/编辑态」下的「xxx」模块中的「xxx」内容删除
* 「阅览态/编辑态」下的「xxx」模块中增加「xxx」内容

###### 2. 增长/删除/修改功能
---

推荐prompt：

* 「阅览态/编辑态」下的「xxx」模块中的「xxx」功能由「xxx」修改为「xxx」功能
* 「阅览态/编辑态」下的「xxx」模块中新增「xxx」功能
* 删除「阅览态/编辑态」下的「xxx」模块中的「xxx」功能（可适当补充描述该功能操作方式/实现效果）

###### 3. 导出/导入组件数据
---

推荐prompt：

* 编辑态下的「用户明细」模块中新增导出「用户明细」功能，支持一键导出「用户明细」的csv
* 编辑态下的XXX模块中新增下载csv模板功能和导入明细功能，支持一键导入明细的csv文件

###### 4. 添加按钮
---

推荐prompt：

编辑态下「基础设置」模块中新增「添加跳转链接」功能，用户可输入链接网址，阅览态下用户点击「活动进展」模块中的「立即参赛」按钮可一键跳转至编辑态添加的网址页面

###### 5. 上传文件支持预览
---

推荐prompt：

「阅览态/编辑态」下的「xxx」模块中上传的附件，新增「在线预览」功能，支持用户点击「xxxx」按钮在线预览附件

###### 6. 图片放大预览
---

推荐prompt：

「阅览态/编辑态」下的「xxx」模块中的「xxx」位置处的图片支持点击放大预览

# 四、优秀案例（欢迎评论区分享出你的随心搭和背后的prompt）
## 阿龙：用随心搭构建「一站式运维查询工具」
### ** 🤔 ****频繁在多平台穿插**
* 负责线上问题排查，需要频繁跨多个平台
* A 查用户信息 / B 申请权限 / C 看日志 / D 查监控
* 4–5 个页面来回切，切换慢、流程碎片化



![](/personal-site-mvp/img/doc-placeholder.svg "")
### **😄 ****一键查询更便捷**
[云上信息一键搜索](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/cRCG7IPZxK/Gscjl_GYblp1zh?t=mention&mt=doc&dt=doc)（测试：i-ObO4iRMs）

这个组件可以直接整合多平台查询与权限申请流程，让原本需要人工跳转的操作统一在一个界面内完成。



不仅如此，阿龙利用随心搭做了一个 CPU 性能可视化看板：

[云上CPU/GPU性能天梯图 - beta2](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/cRCG7IPZxK/qrd6POZLxN3-Op?t=mention&mt=doc&dt=doc)

以前，性能数据都藏在 Excel 表格里，难以直观看出机器性能的差异。现在，他能用图表一眼看出不同设备的表现，就像“我们自己的鲁大师”。


## 阿翁：用随心搭搭建「培训活动页」
### ** 🤔 ****培训活动成本高、效果差**
* 活动页面通常需要频繁更新、调整样式；
* 以往抽奖、报名等活动要手动汇总信息，流程链路长；
* 产品培训内容表格形式不够直观，用户查找效率低；
* 设计和交互想法多，但缺乏技术人力支持。

![](/personal-site-mvp/img/doc-placeholder.svg "")
### **😄 ****想法快速落地**
[🎈今天是什么好日子？抽大奖就对了🎊](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/EP0jvgcwqD/2wJxSy_-2CGL6e?t=mention&mt=doc&dt=doc)

[2025年双十一投放指导](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_x449fbLCV/Uc7XEcfsCi/ycei1Vr-YXpTJV?t=mention&mt=doc&dt=doc)

[🔥『每日一问』· 第三季 | 从从容容学知识，轻松松松抽大奖](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/EP0jvgcwqD/plNb_02OZFjkCw?t=mention&mt=doc&dt=doc)

[🌈还在用excel提报小流量吗？快来体验AppGo提交，轻松搞定](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/EP0jvgcwqD/9xkLeRGkYDyMHK?t=mention&mt=doc&dt=doc)

[🔥『每日一问· 第三季』| 闯关地图](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/EP0jvgcwqD/gwKEKWSmzxvLUc?t=mention&mt=doc&dt=doc)

[AI出考题工具](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/EP0jvgcwqD/aVN97O8U5GCQgy?t=mention&mt=doc&dt=doc)



[随心搭]
## 阿琴：用随心搭搭建「项目管理日历」，还放到了群聊中
### ** 🤔 ****项目管理成本高，且需要一定灵活性**
* 设计小美：这些项目现在是什么状态啊？
* 产品小李：我的这些项目什么时候上线啊？
* 研发小伟：我这有项目要提测？你们何时有人力啊？
* 阿琴自己：每次提测、上线阶段等重要节点，我还需要逐个提醒 😭

![](/personal-site-mvp/img/doc-placeholder.svg "")
### **😄 ****项目管理日历好便捷**
* **支持项目和成员管理**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
* **重要节点有提醒**

![](/personal-site-mvp/img/doc-placeholder.svg "")
* **项目一目了然，也可以按照人或者项目维度查看**

![](/personal-site-mvp/img/doc-placeholder.svg "")
* **群聊侧边栏便于查看**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
**组件地址**：[随心搭项目日历管理](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/AtKECXn-wv/o5tLzp0YdaOZ_7?t=mention&mt=doc&dt=doc)

[随心搭]
## 更多先锋者案例...
#### 活动运营场景
通过随心搭组件，快速实现运营/活动方案落地，提升用户参与度，提升活动效果：

* 答题闯关组件：[【已截止】丝路小懂王闯关赛限时开启！通关赢徽章，瓜分大奖池！](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/94XAO0y0b8/jRyKXVw6P_/ugJBj-z11nJzYy?t=mention&mt=doc&dt=doc)
* 荣誉墙组件：[线上荣誉墙（脱敏版）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/AhkQkHD47-/sNswyp8smcz6X5?t=mention&mt=doc&dt=doc)
* 音频播放组件：[当多智能体开始思辨，我们还需要什么样的人机协同？-「产品漫谈&Hackathon」播客特辑05期](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/T8xkHDmQKW/RhYvysHyxU/WL9lPewiJ-5snj?t=mention&mt=doc&dt=doc)
* 抽奖券展示：[AI 研发，焕新升级，“易”起进化 ！](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/z97pwhZizu/hy296wAZ7z/JfaZzfDRFfy1kt?t=mention&mt=doc&dt=doc)
* 话题互动：[🌍《互联网风向刊》20251124-周一刊](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/94XAO0y0b8/87Aqp3rVqS/78VcmsnMsNRYRR?t=mention&mt=doc&dt=doc)
* 幸福日历、幸福储蓄罐等：[《三好幸福周》最终效果](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/mT8FSFWk1V/X1yYldJb8Zymg1?t=mention&mt=doc&dt=doc)
* [随心搭搭](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/7zeHf89Ft6/l0s7Fjck16SXPg?t=mention&mt=doc&dt=doc)

#### 业务提效场景
通过随心搭组件，快速实现业务平台功能&流程等，提升业务效率：

* 运维信息查询：[云上信息一键搜索](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/cRCG7IPZxK/Gscjl_GYblp1zh?t=mention&mt=doc&dt=doc)
* 机型验收时间计算组件：[新机型验收耗时预估](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/f6yNP_yYge/hMGQJLWCwaTAP1?t=mention&mt=doc&dt=doc)
* 故障演练数据看板：[【随心搭】故障演练版本](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/szW7a5MbT3/CkgMDvtcjW8Gui?t=mention&mt=doc&dt=doc)
* 调起链接转换工具：[调起链接转换工具-v2.0在线版](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/9JEwxDz6hO/-dC7vjHFX_ryBt?t=mention&mt=doc&dt=doc)
* 管理员问卷收集系统：[竞品观察室-低质/刷分评论举报-Q4专项](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MXiHTmpyGM/9sMH9JBvqk/JKhaK3ZXfK1DUi?t=mention&mt=doc&dt=doc)
* Simple URL Encoder：[侧边栏开发文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/I4xVWSifd9bhE9?t=mention&mt=doc&dt=doc)
* URL生成器：[20251125-applink带入草稿支持艾特机器人](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/a3igSPzRj7/VCLsd1BbGDQxzc?t=mention&mt=doc&dt=doc)
* 事故复盘标准模版：[事故复盘标准模板](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/PfOEiHv6e6/BztFplG312fhe9?t=mention&mt=doc&dt=doc)
* 项目日历管理：[随心搭项目日历管理](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/AtKECXn-wv/o5tLzp0YdaOZ_7?view=onlycontent?t=mention&mt=doc&dt=doc)
* [在线工具合集](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/yXKP6rZUMR/hi4f7grVe0iCUJ?t=mention&mt=doc&dt=doc)

#### 信息收集场景
通过随心搭组件，快速实现信息填报&收集场景需求，提升信息收集效率：

* 礼盒信息登记组件：[2025年新春礼盒套餐信息登记](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/PKFJcuE2AO/oGdeBAyA1_PTA_?hi_client_lang=zh-Hans?t=mention&mt=doc&dt=doc)
* 许愿站组件：[蜜糖补给许愿墙](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/AhkQkHD47-/aj-twK_Xx19r-S?t=mention&mt=doc&dt=doc)
* 心愿墙组件：[⭐️ 产品调研-满意度抽奖记录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/HXFtYvbMQj/4iVCdSwaVV/P3qZgS2p2bzidd?t=mention&mt=doc&dt=doc)
* Rules场景申报组件：[网盘AI Coding实战工坊](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/zf7rq2G1GdJCwf?t=mention&mt=doc&dt=doc)
* 内测登记组件：[「🎁体验有礼」 超级助理➕文心5.0上线：你的AI工作搭子，让效率飞起来！🚀](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/z97pwhZizu/MTWsieUgXx/4Y4q9smyd3y3Dv?t=mention&mt=doc&dt=doc)

#### 展示增强场景
[🔍「AI+社区」是什么？](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg?t=mention&mt=doc&dt=doc)

[智能体-小帅指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/6Sn4ie9z6t/D6i3LLJrHEuE2Y?t=mention&mt=doc&dt=doc)

[⭐️ 必看目录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/-Ki0oWtVz8/V8qtSE-WWTadcu?t=mention&mt=doc&dt=doc)

[🌟术说200期专刊丨术说END？不， V2.0上线](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/No39ajz9a1d6P9?t=mention&mt=doc&dt=doc)

[🔥【Vibe Coding大乱斗】正式开战!——全程热AI<工程师的1024>](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/-bBajn6H7xNVDK?t=mention&mt=doc&dt=doc)

#### 产品Demo场景
通过随心搭组件，快速实现可交互的产品原型，用于产品Demo演示：

* 团队工作台：[团队工作台模板](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/AtKECXn-wv/tE7_jDvTqRcl24?t=mention&mt=doc&dt=doc)
* 周报管理系统：[周报随心搭测试](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/Ypya9mGd_G/sRcWVK-vPoed1P?t=mention&mt=doc&dt=doc)
* ...

##### 申请内测 👉 [🪄 知识库随心搭](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/mfrhJmtqNgXEoi?t=mention&mt=doc&dt=doc)，欢迎加入随心搭交流群：11717613
##### 重点项目一对一支持（[🌟 【知识库随心搭】案例墙](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/_5wzlzeefAsroY?t=mention&mt=doc&dt=doc)），请联系[@侯俊莹](https://ku.baidu-int.com?t=mention&mt=contact&id=9ed99690-cf62-11f0-a78c-a39e714310e4)
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
