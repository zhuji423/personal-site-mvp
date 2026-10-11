---
title: "组件名称"
description: "YY Yo Portal 项目 AI 开发 Ducc团队总结"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\YY Yo Portal 项目 AI 开发 (Ducc)团队总结.md"
---
YY Yo Portal 项目 AI 开发 (Ducc)团队总结

#### 🧑‍🏫 案例作者：[@陈锴林](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：需求
#### 🔧 使用工具：Figma、Comate、Ducc
#### 📒 案例概要：Yo Portal项目通过AI协作开发，AI承担90%以上重复编码，并实现自动化测试和质量提升。
> **项目**：Yo Portal (Yo语音大厅)
> **时间跨度**：2026-03-12 ~ 2026-04-02（21天）
> **团队成员**：4人（liangzhirong、hupanpan2、xujie2、chenkailin）
> **文档更新**：2026-04-02
---

## 一、项目背景简介
### 1.1 项目概述
Yo Portal 是 YY 平台推出的语音大厅 PC 端门户应用，为用户提供沉浸式的社交娱乐体验。核心功能包括：

|功能模块|描述|
|-|-|
|首页大厅|Banner 轮播、推荐房间列表、热门大神推荐、人气派对推荐|
|频道管理|创建/加入语音频道、频道列表管理|
|社交互动|关注列表、好友消息、群聊功能|
|用户中心|个人资料、金钻余额、福利签到|

### 1.2 技术架构
```
┌────────────────────────────────────────────────────────────┐
│                     YY 客户端【CEF】                        │ 
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Yo Portal (React 19 + EMP)             │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ │   │
│  │  │  Header │  │  Left   │  │  Right  │  │  Main   │ │   │
│  │  │         │  │ Sidebar │  │ Sidebar │  │         │ │   │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                              │                             │
│                    Module Federation                       │
│                              ▼                             │
│              @astro/ui (Remote Components)                 │
└────────────────────────────────────────────────────────────┘
```
### 1.3 技术栈详情
|类别|技术选型|说明|
|-|-|-|
|框架|React 19 + TypeScript|核心框架|
|构建工具|EMP (基于 Rspack)|通过 `@astro/cli` 配置|
|路由|React Router 6|Hash Router + 懒加载|
|状态管理|Valtio|自定义 BaseStore 模式|
|样式|Tailwind CSS 4 + CSS Modules|SCSS 支持|
|HTTP 客户端|ActHttp|扩展 `@astro/utils/Http`，自动注入 YY 认证|
|微前端|Module Federation|消费 `@astro/ui` 远程组件|
|平台集成|`@astro/yyapi`|YY 客户端原生 API|
|测试|Puppeteer (chrome-devtools skill)|E2E 自动化测试|
|AI 辅助|Ducc |代码生成、调试、文档编写|

---

## 二、团队模式变化
### 2.1 从"人工开发"到"AI协作开发"的转型
#### 传统开发模式
```
产品设计 → 开发编写代码 → 测试验证 → 人工审查 → 上线
```
**痛点**：

* 开发周期长（复杂模块 5-7 个工作日）
* 重复性编码工作量大（多状态切换、样式调试）
* 测试依赖人工，回归测试成本高
* 文档与代码容易脱节

#### AI 协作开发模式
```
产品设计 → 编写 Spec 文档 → AI 生成代码 → 人工验证 → AI 自动化测试 → 上线
```
**优势**：

* AI 承担重复性编码工作
* AI 驱动自动化测试，质量闭环
* 文档与代码同步更新

### 2.2 核心方法论：Spec 驱动开发
团队沉淀出 **"文档驱动 + AI 执行"** 的开发范式：

```
设计稿/Figma → Markdown Spec 文档 → AI 生成代码 → 验证 → 文档同步
```
#### Spec 文档标准模板
```
# 组件名称

## 功能描述
组件的核心职责和使用场景

## 尺寸规范
具体的宽高、间距、字号等数值

## 样式细节
颜色、圆角、阴影、图标 URL 等

## 交互行为
hover、click、右键等事件响应

## 数据结构
TypeScript 类型定义
```
### 2.3 多层级上下文配置体系
团队建立了三层文档体系，让 AI 在不同粒度上理解项目：

|层级|文件|作用|
|-|-|-|
|项目级|`CLAUDE.md`|项目架构、技术栈、开发命令|
|规范级|`AGENTS.md`|代码风格、命名规范、导入顺序|
|组件级|`src/components/*/doc/*.md`|25+ 份组件规格文档|

### 2.4 Skills 生态扩展
通过安装领域特定 Skills，扩展 AI 的专业能力：

|Skill|作用|
|-|-|
|`yymain-api`|YY 客户端原生 API 调用|
|`chrome-devtools`|E2E 自动化测试|
|`vercel-composition-patterns`|React 组合模式规范|
|`vercel-react-best-practices`|React 性能优化（62条规则）|

### 2.5 AI 驱动的测试闭环
```
AI 静态代码审查 → AI 编写 E2E 脚本 → AI 执行测试 → AI 生成报告 → Bug 修复 → 迭代验证
```
---

## 三、团队取得的成效
### 3.1 核心量化指标
|指标|数据|
|-|-|
|开发周期|**21 天**（03-12 ~ 04-02）|
|总提交数|**118 次**|
|参与人数|**4 人**|
|日均提交|**5.6 次**|
|最高单日提交|**29 次**（4月1日）|
|代码采纳率（AI生成）|**98%**|
|代码行|11504 codes，126 files|
|AI 生成文档数|**25+ 份**|
|E2E 测试用例|**16 项**|
|AI 发现 Bug 数|**4 个真实 Bug**|

### 3.2 各模块 AI 提效数据
|模块|传统方式（估算）|AI 辅助方式|提效比|
|-|-|-|-|
|Header 组件|4-5 小时|53 分钟|**~5x**|
|Left 组件|11-12 小时|~2.5 小时|**4-5x**|
|Right 组件|5-6 小时|50 分钟|**6-7x**|
|Main 模块|5-7 天|4 天核心开发|**大幅缩短**|

### 3.3 团队提交分布
```
liangzhirong  ████████████████████████  43次 (36.4%)
hupanpan2     ██████████████████        29次 (24.6%)
xujie2        █████████████████         27次 (22.9%)
chenkailin    █████████                 15次 (12.7%)
```
### 3.4 四个模块开发成果
#### Header 组件
* 8 个功能子组件：搜索框、福利签到、直播入口、社区动态、关注列表、反馈、窗口控制、桌面快捷方式
* AI 发现并修复：清除按钮事件时序问题、全局头像 fallback 遗漏

#### Left 组件
* 3 个核心模块：LeftTab（导航）、RoomStatus（房间状态）、UserInfo（用户信息）
* 攻克难点：频道信号监听、音频状态管理、网络状态三级显示

#### Right 组件
* 频道列表 + 消息模块（好友/群聊）
* 实现：右键菜单、收起/展开动画、三级筛选分类

#### Main 模块
* 4 个子模块：Banner、推荐列表、HotMaster、HotParty
* 48 个文件，约 **4,476 行**新增代码
* AI E2E 测试：62.5% → **75%** 通过率

### 3.5 价值体现
#### 效率提升
* **开发周期缩短**：首页模块从 5-7 天缩短到 4 天核心开发
* **重复工作释放**：AI 承担 90%+ 的重复性编码
* **Bug 发现前置**：AI 静态审查在编码阶段发现 4 个 P0/P1 Bug

#### 质量保障
* **AI E2E 测试自动化**：16 项测试用例自动执行，测试周期从天级缩短到分钟级
* **代码一致性**：通过 `AGENTS.md` 规范，团队代码风格统一

#### 知识沉淀
* **25+ 份组件文档**：形成可复用的"AI 可读需求库"
* **E2E 测试脚本**：642 行 Puppeteer 脚本，可复用到后续迭代

---

## 四、补充说明
### 4.1 行业先进性
#### AI 辅助开发的最佳实践
|实践|说明|行业领先性|
|-|-|-|
|**Spec 驱动开发**|先写文档再让 AI 生成代码|✅ 业界推荐范式|
|**多层上下文配置**|CLAUDE.md + AGENTS.md + 组件 doc.md|✅ 团队创新|
|**AI E2E 测试闭环**|AI 编写脚本 → 执行 → 报告 → Bug 修复|✅ 突破传统测试模式|
|**Skills 生态扩展**|按需安装领域 Skills|✅ 工具链扩展|
|**98% 代码采纳率**|AI 生成代码直接上线|✅ 接近生产级别|

#### 技术亮点
1. **React 19 + EMP 微前端**：业界较早采用 React 19 的生产项目
2. **YY 客户端深度集成**：`yyExternal`、`MFApi` 等原生 API 的 AI 调用封装
3. **Valtio 状态管理**：自定义 BaseStore 模式，AI 理解成本低
4. **多域名 HTTP 客户端**：自动切换 test/prod 环境，AI 调用简便

### 4.2 团队经验沉淀
#### 可复用的方法论
```
Step 1: 准备输入材料
├── 测试用例 Excel/文档（QA 提供）
├── Figma 设计稿（导出 HTML 或截图）
├── API 协议文档（完整的请求/响应字段说明）
└── 项目规范（CLAUDE.md 中的架构模式和约定）

Step 2: 为每个子模块编写 doc.md
├── 功能描述 + 业务逻辑
├── API 协议（请求参数 + 响应字段）
├── Figma HTML 参考代码
├── 布局规格 + 响应式断点
└── 特殊交互说明

Step 3: AI 生成代码
├── 按模块逐个生成（index.tsx + Store.ts + types.ts + 子组件）
├── 人工审查 AI 生成的代码，确认架构模式一致
└── 补充 AI 无法处理的平台 API 调用细节

Step 4: AI 驱动测试
├── Ducc 静态代码审查（对照测试用例 Excel）
├── Ducc 编写 + 执行 E2E 测试脚本
├── 根据测试报告修复 Bug
└── 迭代至通过率达标
```
#### AI 指令最佳实践
```
# 组件生成
"根据 docs/xxx.md 创建组件"

# 批量修改
"将所有列表组件的数据从组件内迁移到 store 层"

# 问题定位
"[描述问题现象]，请帮忙定位原因并修复"

# 文档同步
"组件已更新，同步更新对应的 docs 文档"
```
#### 关键成功要素
|要素|说明|
|-|-|
|**Spec 文档质量**|尺寸数值精确、交互行为明确、数据结构清晰|
|**状态集中管理**|Store 层统一管理，AI 只需修改一处|
|**渐进式指令**|先核心功能，再边缘 case|
|**提供复现路径**|问题描述包含状态变化路径|
|**文档与代码同步**|每次修改后同步更新文档|

### 4.3 后续规划
#### 短期规划（1-3个月）
|方向|内容|
|-|-|
|**AI 能力扩展**|引入更多 Skills，如性能分析、代码审查|
|**E2E 测试覆盖**|扩展测试用例到 50+，覆盖更多场景|
|**文档体系完善**|补充缺失的组件文档，建立文档审查机制|
|**模板沉淀**|沉淀 Header/Left/Right/Main 模块的 AI 开发模板|

#### 中期规划（3-6个月）
|方向|内容|
|-|-|
|**跨项目复用**|将 AI 开发模式推广到其他项目|
|**自动化程度提升**|AI 自动生成 doc.md（基于 Figma API）|
|**测试左移**|AI 在代码编写阶段即进行逻辑验证|
|**团队能力提升**|全员掌握 AI 协作开发范式|

#### 长期愿景
```
┌──────────────────────────────────────────────────────────────┐
│                    AI 原生开发范式                            │
│                                                              │
│   需求 → AI 理解 → AI 生成 Spec → AI 生成代码 → AI 测试      │
│     ↑                                            ↓            │
│     ←←←←←←←←← 人工验证 + 反馈 ←←←←←←←←←←←←                  │
│                                                              │
│   目标：AI 承担 90%+ 编码工作，开发者聚焦架构设计和业务创新      │
└──────────────────────────────────────────────────────────────┘
```
---

## 五、附录
### 5.1 项目文件结构
```
portal/
├── CLAUDE.md                    # Ducc 项目全局指南
├── AGENTS.md                    # AI Agent 编码规范
├── docs/                        # 项目级文档
│   ├── portal-header-component-ai-practice.md   # Header 模块总结
│   ├── portal-left-component-ai-practice.md     # Left 模块总结
│   ├── portal-right-component-ai-practice.md     # Right 模块总结
│   ├── portal-main-component-ai-practice.md     # Main 模块总结
│   ├── portal-development-guide.md               # 开发规范
│   └── portal-ducc-development-summary.md       # 全过程总结
├── src/
│   ├── components/layout/
│   │   ├── Header/              # 顶部导航栏（8子组件）
│   │   ├── Left/                # 左侧栏（3模块）
│   │   └── Right/               # 右侧栏（2大模块）
│   └── view/Main/home/          # 首页（4子模块）
└── test-report-e2e.md           # E2E 测试报告
```
### 5.2 关键文件路径
|文件|说明|
|-|-|
|`src/index.tsx`|入口点（EMP runtime 和 MFApi 初始化）|
|`src/components/layout/index.tsx`|布局组件|
|`src/store/index.ts`|BaseStore 基类|
|`src/rpc/http.ts`|HTTP 客户端|
|`src/view/Main/home/`|首页模块代码|

---

*本文档由 AI（Ducc）辅助生成，整合自项目 21 天开发过程中的 25+ 份实践文档。*

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
