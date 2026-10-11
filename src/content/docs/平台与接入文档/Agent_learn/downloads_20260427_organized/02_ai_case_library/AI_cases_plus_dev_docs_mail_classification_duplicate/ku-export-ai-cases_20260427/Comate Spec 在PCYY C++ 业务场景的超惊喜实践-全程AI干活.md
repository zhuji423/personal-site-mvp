---
title: "一、背景：超高难度C++开发场景的AI提效挑战"
description: "Comate Spec 在PCYY C++ 业务场景的超惊喜实践-全程AI干活"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Comate Spec 在PCYY C++ 业务场景的超惊喜实践-全程AI干活.md"
---
Comate Spec 在PCYY C++ 业务场景的超惊喜实践-全程AI干活

#### 🧑‍🏫 案例作者：[@林俊坚](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：Spec模式通过结构化文档解决企业C++框架AI辅助难题，将开发时间从8小时降至2.75小时。
# 一、背景：超高难度C++开发场景的AI提效挑战
### 1.1 通用场景痛点：AI 辅助 C++ 桌面客户端开发的困境
当前 AI 编码助手在以下 C++ 场景中效果急剧下降：

**企业内部框架 —— AI 的知识盲区**。大量企业存在自研 C++ 框架，从未公开发布，不在任何 AI 模型的训练数据中。AI 面对的是「从未见过的 API」，只能靠方法名猜测行为，而企业内部框架的命名往往不规范（`setFixSize` vs `setFixedSize`），导致猜测失败率极高。另外因重写了Qt的布局，继承的方法`setPos`无法实现绝对定位。

**遗留代码 —— 过时范式无法推断**。大量桌面客户端代码使用 10-20 年前的编程范式：字符串宏的 `SIGNAL/SLOT`、COM 智能指针隐式转换、模板化的变参调用。这些模式在现代开源代码中几乎不存在，AI 缺乏足够的上下文进行正确推断。

**隐式约定 —— 代码之外的知识**。框架行为往往依赖于团队口口相传的隐式约定，不体现在头文件或命名中。例如「设置背景图前必须先设某个 attribute」「下拉框不能用 addItem」「标题栏并非全宽而是在右上角」。这类知识 AI 无论如何分析代码都无法自行发现，只能靠运行时踩坑。

**规模庞大 —— 上下文窗口不够用**。企业框架通常有数百个接口、数千个方法。即使 AI 能读取源码，受上下文窗口限制也无法一次性加载全部 API，无法建立全局理解。

**核心矛盾**：AI 编码助手在开源生态中表现优秀，但一进入企业级 C++ 桌面客户端的「无文档内部框架」场景，准确率从 90%+ 骤降至 ~50%，反而增加了开发者的验证和修正成本。

### 1.2 实际业务场景
本次挑战发生在 **YY桌面客户端 —— 游戏厅（gameHall）模块**。

|框架|年龄|规模|文档状态|
|-|-|-|-|
|**duifw** — 自研 UI 框架|15 年|69 个组件、127 个方法/类、168 个 Q_PROPERTY|零文档|
|**yycomponent** — COM 接口框架|15 年|335 个接口、3000 个成员函数、200+ Debus 常量|零文档|
|**Qt 4.x** 信号槽|宏字符串范式|SIGNAL/SLOT 宏连接|AI 训练数据稀缺|

**开发任务**：实现 `CmdHandler::joinMyGuild()` 功能——用户在游戏厅活动页点击"即刻体验"时，判断其名下是否有自建频道，并弹出对应操作弹窗。涉及 duifw 中 8 种控件类型、yycomponent 中 2 个 COM 接口、3 种 Debus 通信模式、至少 5 个无法从命名推断的隐式约定。

# 二、解决方案：Spec模式如何破解超高难度场景？
## 2.1、Spec 模式原理
### 核心思想
Spec 模式的核心是：**不让 AI 猜，而是给 AI 看规格说明书（Specification）**。

在代码生成之前，将内部框架的关键知识提炼为**结构化的 Spec 文档**，作为上下文注入 AI 的提示中。AI 不再依赖训练数据中的记忆，而是**基于当前上下文中的 Spec 进行受约束的代码生成**。

## 工作流程
[流程图]
## 2.2、Spec 模式的特点
### 将隐式知识显式化
|问题|传统方式|Spec 模式|
|-|-|-|
|内部 API 命名不规范|AI 靠猜（`setFixedSize` vs `setFixSize`）|Spec 中明确写出正确 API 名|
|隐式调用顺序|AI 无从得知，运行时崩溃|Spec 中标注前置条件和调用约束|
|框架特有的反模式|AI 生成"看起来对但实际出错"的代码|Spec 中标注"禁止"规则|

### 按需加载，突破上下文限制
Spec 模式不要求一次性加载全部框架知识。它按**当前任务涉及的组件**选择性加载对应的 Spec 片段，将上下文占用从"全部 API"缩减到"本次任务相关的 5-10 个组件"。

### 可积累、可复用
* Spec 文档一次编写，团队内所有人复用
* 随着使用不断补充，逐步覆盖框架全貌
* 踩过的坑（隐式约定）写入 Spec 后，团队不再重复踩坑

### 准确率的质变
Spec 模式将 AI 的工作模式从**开放式猜测**转变为**闭卷考试变开卷考试**：

* 无 Spec：AI 根据方法名猜行为 → 准确率 ~50%
* 有 Spec：AI 根据明确规格生成代码 → 准确率可回升至 85-95%

---

## 2.3、使用场景
###  最适合的场景
* **零文档内部框架**：如 duifw、yycomponent 等自研框架，外部无任何参考资料
* **隐式约定密集的老代码库**：大量"必须这样做但没人写下来"的规则
* **COM / 宏 / 模板等复杂范式**：AI 训练数据中样本稀缺的编程模式
* **团队协作中的知识传递**：新人或 AI 都能通过 Spec 快速上手

# 三、实战过程：从8小时到2.75小时的蜕变
## 3.1、 准备阶段
* 将 **duifw **UI 框架的头文件给 comate，让其生成 **duifw **skill
* 将 **yycomponent **UI 框架的头文件给 comate，让其生成 **yycomponent **skill
* 将知识库需求文档转成 md 放在本地
* 将 Figma 设计稿转成 html 设计稿放在本地

## 3.2、实战全景时间线
```
  0:00 ─── 开始 ──────────────────────────────────────────
    │
    │  第一阶段：需求理解与规格生成（~15 min）
    │
  0:15 ─── doc.md + tasks.md 确认 ────────────────────────
    │
    │  第二阶段：AI 首次代码生成（~10 min）
    │
  0:25 ─── 首版代码生成完毕，开始编译运行 ────────────────
    │
    │  第三阶段：API 纠错（6轮，~35 min）
    │    0:25  [1] duiBus 调用方式错误
    │    0:30  [2] 背景图用了冗余 ImageWidget
    │    0:35  [3] 中文字符串 hex 编码
    │    0:40  [4] WindowFlags 枚举错误
    │    0:45  [5] 缺少透明背景三件套
    │    0:55  [6] 关闭按钮应用 titlebar 自带
    │
  1:00 ─── API 层面基本正确 ──────────────────────────────
    │
    │  第四阶段：功能补全 + Skill 反哺（3轮，~20 min）
    │    1:00  [7] 新增"创建频道"链接
    │    1:10  [8] emitSignalMessage 参数缺失
    │    1:15  [9] 排查 Skill 文档缺陷并修复
    │
  1:20 ─── 功能完整，进入布局调试 ────────────────────────
    │
    │  第五阶段：布局三次重构（3轮，~45 min）
    │    1:20  [10] setPos 无效 → Anchor 重构
    │    1:35  [11] Anchor 有问题 → HBox/VBox 方案分析
    │    1:50  [12] HBox/VBox 间距推导 + 代码重写
    │
  2:05 ─── 布局正确，最后微调 ────────────────────────────
    │
    │  第六阶段：最终修正 + 验证（~40 min）
    │    2:05  [13] setAnchor2 调用顺序（已切布局，无效）
    │    2:10  [14] titlebar top 偏移修正（25→9）
    │    2:15  [15] 编译运行验证
    │    2:35  [16] 文档同步更新
    │
  2:45 ─── 代码运行正确 ✓ ────────────────────────────────
```
---

## 3.3、第一阶段：需求理解与规格生成（0:00 ~ 0:15）
**输入**：一句话需求 + 设计稿 HTML + 需求文档 MD

> "根据md文档的2.2部分功能描述和设计稿，在CmdHandler::joinMyGuild中实现其他功能。ui用duifw，pcyy的接口调用yycomponent"
**AI 自主完成**：

1. 探索代码库，定位 `CmdHandler.h/.cpp`、设计稿 `index.html`、需求文档
2. 分析设计稿尺寸，提取 6 个控件的绝对坐标
3. 生成 `doc.md`（需求规格 + 技术方案 + 影响文件）
4. 生成 `tasks.md`（6 个任务、13 个子步骤）

**开发者参与**：审阅确认 2 份文档，各 ~2 分钟

**阶段评价**：Skill 在此阶段发挥了关键作用——AI 正确识别出需要调用 `IYYHomeTree::getMyGuildChannelList()` 和 `debusCall(KChannelJoin)`，这些信息全部来自 Skill 文档，而非头文件分析。

---

## 3.4、第二阶段：AI 首次代码生成（0:15 ~ 0:25）
AI 一次性生成了完整的代码框架：

**CmdHandler.h 新增**：

```
// 成员变量
DuiFrameWindow* m_guildDialog;
DuiComboBox*    m_guildComboBox;

// 槽函数
void onConfirmGuild();
void onGuildDialogClosed();
```
**CmdHandler.cpp 新增 ~200 行**：

* `joinMyGuild()`：获取频道列表 → 筛选 OWNER → 分支处理 → 创建弹窗
* `onConfirmGuild()`：读取 ComboBox sid → debusCall 加入频道
* `onGuildDialogClosed()`：清空成员指针

**阶段评价**：业务逻辑一次到位（COM 接口调用、频道筛选、排序、分支判断），但 UI 层面存在多处细节错误——这正是 15 年无文档框架的典型表现。

---

## 3.5、第三阶段：API 纠错（0:25 ~ 1:00，6 轮）
这是「隐式约定」集中暴露的阶段。每轮遵循相同模式：开发者编译/运行发现问题 → 指出错误 → AI 修正。

### 第 1 轮：duiBus 调用方式（0:25）
```
错误：bus->emitSignalMessage(...)        // 通过 COM 接口调用
正确：duiBus()->emitSignalMessage(...)    // 通过 duifw 全局函数调用
```
**根因**：Skill 中 duiBus 和 IYYDebusHelper 的使用场景描述分散，AI 混淆了两个通道。

### 第 2 轮：冗余背景图组件（0:30）
```
错误：new DuiImageWidget() 作为背景      // 多此一举
正确：setBackgroundImage() 直接设置       // DuiFrameWindow 自带能力
```
**根因**：AI 不知道 DuiFrameWindow 支持直接设置背景图，采用了过度设计的方案。

### 第 3 轮：中文字符串编码（0:35）
```
错误：QString::fromUtf8("\xe9\x80\x89...")   // UTF-8 hex
正确："选择创建语聊房间的频道"                  // 直接字面量
```
**根因**：AI 对旧版 Qt 的字符编码过度担忧，实际项目已配置 UTF-8。

### 第 4 轮：WindowFlags 枚举（0:40）
```
错误：Qt::Dialog | Qt::FramelessWindowHint
正确：Qt::SplashScreen | Qt::FramelessWindowHint
```
**根因**：`SplashScreen` 是 duifw 弹窗的惯用 flag，Skill 中有记录但 AI 未优先采用。

### 第 5 轮：缺少透明背景三件套（0:45）
```
缺失的三行（顺序敏感）：
  setAttribute(Qt::WA_TranslucentBackground);
  setWindowFlags(Qt::SplashScreen | Qt::FramelessWindowHint);
  setStyleSheet("QGraphicsView { border-style: none; background: transparent }");
```
**根因**：duifw 最核心的隐式约定之一——背景图前必须设置这三个属性，否则出现白色花边。Skill 有记录，但 AI 在第 4 轮只改了 flags 没有补全其余两项。

### 第 6 轮：关闭按钮用 titlebar 自带（0:55）
```
错误：new DuiPushButton() 自定义关闭按钮，手动绑定 close()
正确：titlebar->titleButton(DuiTitlebar::Button_Close) 内置按钮，换图即可
```
**根因**：AI 不知道 DuiTitlebar 内置了关闭按钮（位于窗口右上角而非标题栏全宽），这是 duifw 独有的设计。

**阶段总结**：6 轮纠错消灭了 API 层面的全部错误，每轮平均 5 分钟。核心问题集中在「隐式约定」和「旧范式理解偏差」。

---

## 3.6、第四阶段：功能补全 + Skill 反哺（1:00 ~ 1:20，3 轮）
### 第 7 轮：新增"创建频道"链接（1:00）
开发者补充需求：在确认/取消按钮下方增加蓝色"创建频道"可点击文字链接。

AI 跨 4 个文件完成修改：

* `doc.md`：增加控件行（x=198, y=166, 80×16）
* `tasks.md`：新增任务 6
* `CmdHandler.h`：添加 `onCreateChannelLinkClicked()` 槽
* `CmdHandler.cpp`：添加 `DuiLabelWidget` + `setAcceptClick(true)` + 实现槽函数

### 第 8 轮：emitSignalMessage 缺少参数（1:10）
```
错误：QVariantList args;  // 空参数
      duiBus()->emitSignalMessage("MainframeMenuService", "MFMenuCreateChannelTriggered", args);

正确：QVariantList args;
      args << false;  // 是否为向导模式（false=普通模式）
      duiBus()->emitSignalMessage("MainframeMenuService", "MFMenuCreateChannelTriggered", args);
```
**根因**：Skill 的 DUIBUS.md 信号表中缺少"参数说明"列，AI 无法关联到 `args<<false` 的要求。

### 第 9 轮：排查 Skill 缺陷并修复（1:15）
开发者提出关键问题：「Skill 本身是否有缺陷，导致 AI 首次无法生成正确代码？」

AI 自查后发现 DUIBUS.md 的信号表确实缺少参数说明，**反哺 Skill**：

* 信号表新增"参数说明"列
* `KMFMenuCreateChannelTriggered` 标注 `args[0]=false: 普通模式`
* 示例代码注释添加参数引用

**阶段亮点**：这是 Skill 知识工程的闭环——开发过程中发现 Skill 不足 → 立即修复 → 下次 AI 不再犯同样错误。

---

## 3.7、第五阶段：布局三次重构（1:20 ~ 2:05，最艰难的阶段）
这是整个开发过程中**难度最高、耗时最长**的环节，布局方案经历了三次推翻重做。

### 第 10 轮：第一次重构——setPos → Anchor（1:20）
**问题**：AI 初始代码使用 `widget->setPos(QPointF(x, y))` 进行绝对定位，编译通过但运行时控件全部堆叠在左上角。

**原因**：duifw 基于 QGraphicsWidget 的布局系统中，`setPos()` 会被布局管理器覆盖，实际不生效。

**AI 方案**：改用 Anchor 锚点布局

```
root->setLayout(DuiWidget::Anchor);
titleLabel->setAnchor2(StringUtils::string2AnchorInfo2("Left:parent.Left:121|Top:parent.Top:16"));
```
### 第 11-12 轮：第二次重构——Anchor → HBox/VBox（1:35）
**问题**：Anchor 锚点方案运行后仍有兼容性问题。

**开发者决策**：不急于改代码，先让 AI 分析 HBox/VBox 方案的可行性。

**AI 分析产出**——从设计稿绝对坐标推导出完整的间距计算表：

|间距|推导公式|结果|
|-|-|-|
|标题左偏移|121 - root.left_margin(20)|101px Spacer|
|标题→下拉框|76 - 16 - 24|36px gap|
|下拉框→按钮|126 - 76 - 32|18px gap|
|确认按钮左偏移|46 - root.left_margin(20)|26px Spacer|
|确认→取消间距|230 - 46 - 164|20px Spacer|
|按钮→链接|166 - 126 - 36|4px gap|
|链接左偏移|198 - root.left_margin(20)|178px Spacer|

**最终布局结构**（第三版，运行正确）：

```
root (VBox, margins: 20/16/20/2, spacing=0)
  ├── titleRow [HBox, h=24]
  │     ├── DuiSpacerItem [w=101]
  │     ├── titleLabel [198×24] "选择创建语聊房间的频道"
  │     └── DuiSpacerItemEx      (弹性填充)
  │
  ├── gap1 [h=36]
  │
  ├── DuiComboBox [400×32]       "sid(name)" 格式
  │
  ├── gap2 [h=18]
  │
  ├── buttonRow [HBox, h=36]
  │     ├── DuiSpacerItem [w=26]
  │     ├── confirmBtn [164×36]   guild_sure.png
  │     ├── DuiSpacerItem [w=20]
  │     └── cancelBtn [164×36]    guild_cancel.png
  │
  ├── gap3 [h=4]
  │
  └── linkRow [HBox, h=16]
        ├── DuiSpacerItem [w=178]
        └── createLink [80×16]    "创建频道" 蓝色
```
**阶段反思**：布局是 AI 最难一次做对的环节。duifw 有 4 种布局模式（None/VBox/HBox/Anchor），但哪种在当前版本可用、哪种有兼容性问题，只有运行才能验证。Skill 中对此描述不足，是后续需要加强的方向。

---

## 3.8、第六阶段：最终修正 + 验证（2:05 ~ 2:45）
### 第 13 轮：调用顺序调整（2:05）
开发者要求将 `setAnchor2` 放在 `addItem` 之前。由于已切换到 HBox/VBox 布局，此轮实际无影响，但 AI 仍完成了顺序调整以保持代码一致性。

### 第 14 轮：titlebar margins 偏移——最后一个隐式约定（2:10）
**问题**：关闭按钮位置偏下，设计稿要求 y=25，实际显示在 y=41。

**根因**：`titlebar->setMargins()` 的 top 值会叠加 `root->setMargins()` 的 top 值。root 的 top margin = 16，所以 titlebar 的 top 应设为 `25 - 16 = 9`。

```
// 错误
titlebar->setMargins(QMargins(0, 25, 16, 0));

// 正确
titlebar->setMargins(QMargins(0, 9, 16, 0));  // 9 = 设计稿25 - root.top(16)
```
**Skill 反哺**：将这条隐式约定写入 `DuiTitlebar.md`，后续 AI 不再踩此坑。

### 第 15-16 轮：编译运行验证 + 文档同步（2:15 ~ 2:45）
* 编译通过，运行验证弹窗显示正确
* 6 个控件全部在设计稿指定位置
* 确认/取消/创建频道三个交互路径均正常
* 同步更新 doc.md、tasks.md、summary.md

**2:45 —— 代码运行正确。**

---

## 3.9、关键代码亮点
最终 AI 生成的代码中有几处值得关注的实现质量：

### 旧弹窗安全清理
```
if (m_guildDialog) {
    m_guildDialog->close();
    m_guildDialog->deleteLater();   // 而非直接 delete
    m_guildDialog   = nullptr;
    m_guildComboBox = nullptr;
}
```
使用 `deleteLater()` 避免窗口关闭时异步事件回调到已销毁对象导致崩溃，是 Qt 对象销毁的最佳实践。

### 防御性编程全覆盖
```
void CmdHandler::onConfirmGuild()
{
    if (!m_guildComboBox)                              // 指针防空
        return;
    QStandardItemModel* model = m_guildComboBox->model();
    int idx = m_guildComboBox->currentIndex();
    if (!model || idx < 0 || idx >= model->rowCount()) // 模型+索引防越界
        return;
    quint32 sid = model->item(idx)->data(Qt::UserRole).toUInt();
    if (sid == 0)                                      // 业务数据有效性
        return;
    IYYDebusHelperPtr bus = commonService;
    if (bus)                                           // COM 接口防空
    {
        gamehall_log() << "joinMyGuild: joining channel sid=" << sid;
        bus->debusCall(KChannelService, KIChannel, KChannelJoin, sid, 0, sid);
    }
    if (m_guildDialog)                                 // 关闭前再次防空
        m_guildDialog->close();
}
```
5 层防御覆盖指针空检查、模型有效性、索引越界、业务数据合法性、COM 接口可用性。

### 透明无边框弹窗三件套
```
m_guildDialog->setAttribute(Qt::WA_TranslucentBackground);
m_guildDialog->setWindowFlags(Qt::SplashScreen | Qt::FramelessWindowHint);
m_guildDialog->setStyleSheet("QGraphicsView { border-style: none; background: transparent }");
```
这 3 行组合来自 Skill 知识沉淀：缺任何一行都会出现白色花边。AI 在第 5-6 轮纠错后正确掌握了这一隐式约定。

# 四、核心成果与经验总结
## 4.1、数据复盘
### 时间分布
|阶段|时间|占比|内容|
|-|-|-|-|
|需求理解 & 规格|15 min|9%|doc.md + tasks.md|
|首次代码生成|10 min|6%|~200 行完整代码框架|
|**API 纠错（6轮）**|**35 min**|**21%**|隐式约定 + 旧范式偏差|
|功能补全 + Skill 反哺|20 min|12%|新增控件 + 修复 Skill|
|**布局重构（3轮）**|**45 min**|**27%**|setPos → Anchor → HBox/VBox|
|最终修正 + 验证|40 min|25%|titlebar 偏移 + 编译运行|
|**合计**|**165 min**|**100%**||

### 错误分类
|类型|轮次|说明|
|-|-|-|
|隐式约定未覆盖|1,5,12,17|最难发现，只能运行时暴露|
|AI 旧范式偏差|3,4|对 15 年前 Qt 用法理解偏差|
|需求理解差异|6,8|组件选型和功能补充|
|布局方案失误|10,11|需三次尝试才找到可用方案|
|Skill 信息分散|9|参数说明分散在三处|
|框架行为未记录|14|titlebar 受 root margins 偏移|

### 效率对比
|维度|纯人工|AI 辅助|倍率|
|-|-|-|-|
|总时间|6~8 小时|2.75 小时|**2.5~3x**|
|查 API 文档|翻 69 个头文件|Skill 直出|-|
|布局调试|手工像素调试|AI 推导间距表|-|
|Debus 常量查找|200+ 常量手动搜索|分类表直查|-|
|代码框架搭建|逐行手写|AI 一次生成 ~200 行|-|

---

## 4.2、Skill 反哺清单
本次开发过程中，有 3 条新发现的框架知识被即时写回 Skill，形成闭环：

|发现轮次|知识点|写入文件|
|-|-|-|
|第 9 轮|emitSignalMessage 需传 `args<<false` 参数|DUIBUS.md 新增"参数说明"列|
|第 14 轮|titlebar margins 受 root margins 偏移|DuiTitlebar.md 新增偏移说明|
|第 12 轮|HBox/VBox + Spacer 精确像素定位方法|WIDGET_API.md 补充布局示例|

这意味着**下一次**类似开发，AI 将不再犯这 3 类错误，纠错轮次预期从 12 轮降至 8~9 轮。

---

## 4.3、蜕变总结
```
纯人工开发（无 AI）
────────────────────
翻阅 69 个头文件找 API      → 2~3 小时
在 200+ 常量中搜索 Debus    → 0.5~1 小时
手工编写 270 行 C++ 代码    → 2~3 小时
像素级布局调试               → 1~2 小时
────────────────────
总计：6~8 小时


AI 辅助开发（有 Skill）
────────────────────
需求 → doc → tasks           → 15 分钟
AI 生成 200 行代码框架       → 10 分钟
12 轮纠错迭代                → 75 分钟（核心时间）
布局方案推导 + 重写          → 45 分钟
验证 + 文档同步              → 20 分钟
────────────────────
总计：2.75 小时 (165 min)


效率提升 = 2.5~3 倍
────────────────────
而且：每次纠错都反哺 Skill
下一次开发，纠错更少，效率更高
这是一个持续加速的飞轮
```
从 8 小时到 2.75 小时，节省的不仅是时间。更重要的是：

1. **知识不再流失**——每个踩过的坑都沉淀为 Skill 文档，新人不必重新摸索
2. **AI 持续进化**——每次 Skill 反哺后，AI 下次生成的代码更准确
3. **开发者角色转变**——从「写代码」变为「审代码 + 补知识」，专注更高价值的判断

这不是终点。12 轮纠错中仍有 4 轮是 Skill 未覆盖的隐式约定。随着 Skill 持续完善，纠错轮次将继续下降，AI 辅助的效率将进一步逼近理论上限。

# 
# 五、如何复用这套实践？
## 5.2、Skill 知识工程 SOP
这是整套方案的**基石**。没有 Skill，AI 对无文档内部框架的代码生成准确率约 50%，反而增加验证成本。

### 第一步：框架规模摸底
在开始之前，量化你的框架规模，用于预估 Skill 建设时间。

**统计方法**（以 C++ 框架为例）：

```
# 统计组件/类数量
grep -r "class.*:.*public.*BaseWidget" --include="*.h" | wc -l

# 统计 COM 接口数量
grep -r "DWDEFINE_INTERFACE" --include="*.h" | wc -l

# 统计 Q_PROPERTY 数量
grep -r "Q_PROPERTY" --include="*.h" | wc -l

# 统计预定义常量
grep -r "static const.*QString.*=" --include="*.h" | wc -l
```
**产出**：一张规模表，用于后续决策。

|统计项|你的框架|joinMyGuild 参考值|
|-|-|-|
|组件/类数量|___|69|
|接口数量|___|335|
|方法/函数总数|___|3000|
|预定义常量|___|200+|

### 第二步：高频 API 筛选（80/20 法则）
**不要试图覆盖全部 API**。335 个接口中，gamehall 业务实际高频使用的仅 5~10 个。

**筛选方法**：

1. 从最近 3~6 个月的业务需求中提取涉及的框架 API
2. 按调用频次排序，取 Top 10~15 个组件/接口
3. 每个组件只覆盖常用方法（通常 20~~30 个方法取 8~~10 个）

**参考**：joinMyGuild 案例中，69 个 duifw 组件只覆盖了 10 个（14.5%），但这 10 个覆盖了 90% 的业务场景。

### 第三步：AI 初始生成 + 代码驱动纠错
这是最耗时的核心环节（占 Skill 建设 ~57% 的时间）。

**流程**：

```
Step A: 让 AI 读取头文件，生成初始文档
         ↓
Step B: 用实际示例代码逐一核对
         ↓  发现错误
Step C: 修正文档，标注"已验证"
         ↓
Step D: 重复 B-C 直到核心 API 全部验证
         ↓
Step E: 提取隐式约定，补充为"注意事项"
```
**关键原则**：

* **永远以头文件/源码为准**，不信任 AI 对未知框架的猜测
* **枚举值和方法名是重灾区**：AI 初始生成的枚举值全部虚构的概率约 30%
* **每个错误平均修正时间约 8 分钟**

**纠错记录模板**：

|步骤|触发源|发现的错误|纠正操作|
|-|-|-|-|
|1|`XxxWidget.h` L19-25|`addItem()` 方法不存在|改为 `model()->appendRow()`|
|2|`helper_i.h`|常量名虚构|删除虚构常量，补充实际值|
|...|...|...|...|

### 第四步：文档拆分与规范化
|规范项|建议|原因|
|-|-|-|
|单文件行数|≤ 250 行|超过后 AI 上下文效率下降|
|目录结构|`SKILL.md` + `references/` 子目录|主文档做索引，子文档做详情|
|每个控件独立文件|`references/XxxWidget.md`|便于定位更新，避免膨胀|
|命名规范|大写蛇形：`WIDGET_API.md`|与 Skill 规范一致|

**推荐目录结构**：

```
.comate/skills/
  your-framework/
    SKILL.md              # 主文档：框架概览 + quickstart + 控件索引
    references/
      WINDOW_API.md       # 窗口级 API
      WIDGET_API.md       # 组件通用 API
      XxxButton.md        # 具体控件
      XxxComboBox.md
      COMMUNICATION.md    # 组件间通信机制
      RESOURCES.md        # 资源路径规范
      CONSTANTS.md        # 预定义常量分类表
```
### 第五步：交叉引用与常量表
* SKILL.md 中建立控件索引表，指向各子文档
* 常量表按业务领域分类（频道、用户、菜单、信号...）
* 每个示例代码标注来源文件和行号

---

## 5.3、SDD 工作流模板
SDD（Spec-Driven Development）通过 doc → tasks → code → summary 的流程，将复杂任务拆解为可独立验证的步骤。

### 5.3.1 doc.md 模板
```
# {功能名称} —— 需求规格

## 需求描述
{一句话描述 + 业务背景}

## 技术方案
### 涉及框架
{列出用到的内部框架及具体 API}

### 控件清单
| 控件 | 类型 | 位置(x,y) | 尺寸(w×h) | 属性 |
|------|------|-----------|-----------|------|

### 数据流
{入口 → 数据获取 → 业务逻辑 → UI 渲染 → 用户交互 → 响应处理}

## 影响文件
| 文件 | 修改类型 | 影响函数 |
|------|---------|---------|

## 边界条件
{空数据、异常、并发、内存管理等}
```
**必填字段检查**：

- [ ] 涉及的内部框架 API 是否全部在 Skill 覆盖范围内？
- [ ] 控件清单是否有精确坐标（来自设计稿）？
- [ ] 数据流是否覆盖了全部用户交互路径？
- [ ] 边界条件是否包含指针防空和资源释放？

### 5.3.2 tasks.md 模板
```
# {功能名称} —— 任务计划

- [ ] Task 1: {动词开头的任务描述}
    - 1.1: {子步骤}
    - 1.2: {子步骤}

- [ ] Task 2: {动词开头的任务描述}
    - 2.1: {子步骤}
```
**粒度建议**：

* 顶层任务：3~8 个，每个可独立编译验证
* 子步骤：每个任务 2~5 个子步骤
* 单个任务的代码变更量：≤ 100 行

### 5.3.3 执行循环
```
for each task in tasks.md:
    1. 标记任务 in_progress
    2. AI 生成代码
    3. 开发者编译/运行验证
    4. if 发现错误:
         纠错（参见第四部分）
         if 是隐式约定: 反哺 Skill（参见第五部分）
    5. 标记任务 completed（更新 checkbox）
    6. 进入下一个任务
```
**关键规则**：

* 一次只执行一个顶层任务
* 完成后立即更新 tasks.md 中的 checkbox
* 纠错不算新任务，在当前任务内完成

### 5.3.4 summary.md 输出规范
完成后生成 summary.md，包含：

* 实际完成的任务清单
* 代码变更统计（文件、行数、新增/修改）
* 纠错记录（轮次、根因、修正）
* Skill 反哺记录（如有）

---

## 5.4、Skill 反哺机制
### 5.4.1 触发条件
当满足以下**任一条件**时，应立即将新知识写回 Skill：

|触发条件|说明|
|-|-|
|发现 Skill 未覆盖的隐式约定|如 `titlebar margins 受 root margins 偏移`|
|AI 因 Skill 信息不足而犯错|如 `emitSignalMessage` 缺少参数说明导致生成不完整代码|
|发现框架行为与 Skill 描述不符|纠正后同步更新 Skill|
|尝试了多种方案后确定最优解|如 `setPos → Anchor → HBox/VBox`，记录可用方案|

### 5.4.2 写回规范
```
写回位置：对应控件/模块的 references/Xxx.md
写回格式：
  1. 在"注意事项"或"隐式约定"段落追加
  2. 标注发现来源（哪个功能开发中发现）
  3. 提供正确写法的代码片段
  4. 如果有错误写法，也列出作为对比
```
**示例**：

```
### 注意事项
- **titlebar margins 偏移**（joinMyGuild 开发中发现）：
  titlebar 的 `setMargins()` top 值会叠加 root widget 的 top margin。
  正确计算：`titlebar.top = 设计稿值 - root.topMargin`
  ```cpp
  // 设计稿要求关闭按钮 y=25，root topMargin=16
  titlebar->setMargins(QMargins(0, 9, 16, 0));  // 9 = 25 - 16
```
### 5.4.3 闭环验证
写回 Skill 后，用以下方法验证生效：

1. 开启新对话，让 AI 基于更新后的 Skill 重新生成同类代码
2. 检查 AI 是否自动规避了之前的错误
3. 如果仍然犯错，说明 Skill 描述不够清晰，需进一步优化措辞

---

## 5.5、快速启动清单
如果你决定在自己的业务中复用这套实践，按以下顺序执行：

```
Week 1: Skill 知识工程
  □ 统计框架规模（第二章 2.1）
  □ 筛选 Top 10 高频 API（第二章 2.2）
  □ AI 生成 + 代码驱动纠错（第二章 2.3）
  □ 文档拆分与规范化（第二章 2.4）

首次业务开发:
  □ 选一个中等复杂度功能作为试点
  □ 按 SDD 工作流执行（第三章）
  □ 记录纠错轮次和根因（第四章）
  □ 将新发现写回 Skill（第五章）

复盘:
  □ 统计度量指标（第六章）
  □ 识别 Skill 薄弱环节并补强
  □ 更新本指南中的基准线数据
```


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
