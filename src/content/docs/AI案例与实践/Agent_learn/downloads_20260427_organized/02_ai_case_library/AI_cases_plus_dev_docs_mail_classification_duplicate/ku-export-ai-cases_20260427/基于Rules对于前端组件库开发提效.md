---
title: "设计系统使用指南"
description: "基于Rules对于前端组件库开发提效"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\基于Rules对于前端组件库开发提效.md"
---
基于Rules对于前端组件库开发提效

#### 🧑‍🏫 案例作者：[@刘洪延](https://ku.baidu-int.com?t=mention&mt=contact&id=5c33ea40-fce2-11f0-8140-771dc831890f)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了利用Rules提升前端组件库开发效率的实践经验。通过提供设计系统简介、开发规范及项目架构信息，结合信息类、指令类和约束类Rules，指导AI生成符合规范的组件代码，解决了语法兼容、开发风格不一致及Token使用不准确等问题。Rules的引入不仅提高了开发效率，还确保了代码质量，加速了团队知识沉淀。
## 需求
实际业务场景下会有一些组件 新增/升级的需求，比如：

需要一个移动端的选择器组件

![](/personal-site-mvp/img/doc-placeholder.svg "")
## Coding Agent with Rules
![](/personal-site-mvp/img/doc-placeholder.svg "")
[评审：wk-web-54365 rule测试](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/wenku/atomic-design/reviews/118829258/files/base...latest/.comate/rules/project-architecture.mdr?t=mention&mt=doc&dt=sdk)

##### 信息类Rule
组件库是基于design token的，所以第一步我提供了设计系统的简介以及开发规范

```
---
description: 设计系统和样式开发规范
---
# 设计系统使用指南
## Token 系统架构
### Token 目录结构 (mdr:packages/atomic-tokens/tokens/)
```
tokens/
├── base/          # 基础设计 token
│   ├── border.less
│   ├── color.less       # 颜色 token - 包含原子类如 atomic-color-text、atomic-color-bg 等
│   ├── font.less        # 字体 token - 包含 atomic-font-* 系列原子类
│   ├── index.less
│   ├── rounded.less     # 圆角 token
│   ├── shadow.less      # 阴影 token
│   └── space.less       # 间距 token (提供CSS变量而非原子类)
├── flower/        # 橙篇主题 token
└── oreate/        # 海外主题 token
```
### Token 使用规范
#### 优先使用 Token
- 组件样式必须优先使用 `packages/atomic-tokens/tokens/base/` 中的 token
- 颜色、字体、间距等样式禁止硬编码，必须使用 token
#### 样式导入方式
```less
// 在组件样式文件中
@import '../variable.less';  // 导入基础变量
```
#### Token 分类
##### 颜色 Token
- 文本颜色: `atomic-color-text-*`
- 背景颜色: `atomic-color-bg-*` 
- 边框颜色: `atomic-color-border-*`
- 基础颜色按 tiny、minor、media 等层级划分
##### 字体 Token
- 字体大小: `atomic-font-size-*`
- 字重: `atomic-font-weight-*`
- 行高: `atomic-line-height-*`
##### 间距布局
- 使用CSS变量: `var(--atomic-space-*)`
- 间距大小按 xs、sm、md、lg、xl 等标准划分
## 样式最佳实践
### 响应式设计
- 使用 Less 媒体查询实现响应式
- 移动优先的设计原则
### 组件样式命名
- 使用 BEM 命名规范：`@{prefix}-component-name`
- `@prefix` 变量统一管理前缀
### 特殊场景处理
- 只有在明确样式不会在多品牌、多端场景下变化时，才允许使用硬编码值
- 动画和过渡效果应使用一致的 timing function
```
atomic组件库一个比较特殊的地方是兼容vue2/3双运行时，提供了项目架构信息

```
---
alwaysApply: true
description: 项目架构和关键特性概述
---
# Atomic Design 项目架构指南
## 项目核心特性
### 双运行时兼容架构
- 使用 [vue-demi](https://github.com/vueuse/vue-demi) 库实现 Vue2.7.16 / Vue3.5.13 双版本兼容
- 所有组件代码写在 `packages/atomic-components/src` 目录中，通过统一的构建系统生成两个版本
### 设计系统集成
- Design Token 系统位于 `packages/atomic-tokens/tokens/base/` 目录
- 包含颜色(color.less)、字体(font.less)、间距(space.less)、圆角(rounded.less)等基础 token
- 支持多品牌主题（基础、flower、oreate）
### 多站点演示
In
- Vue2 演示站点：`packages/atomic-site-vue2/`，运行在端口 8301
- Vue3 演示站点：`packages/atomic-site-vue3/`，运行在端口 8302
- 组件文档：`packages/atomic-web/` 负责展示组件文档
## 关键技术栈
- **构建工具**: Vite + TypeScript
- **测试框架**: Vitest + Vue Test Utils
- **包管理**: pnpm workspace
- **样式预处理器**: Less
- **代码规范**: ESLint + Prettier
## 开发环境要求
- Node.js 20+ 
- pnpm 9.x.x
## 构建产物
- 组件库：发布到 [@baidu/atomic-components](mdr:packages/atomic-components/package.json) npm 包
- 文档站点：分别构建 Vue2 和 Vue3 版本用于演示
## 文件命名规范参考
- JavaScript/TypeScript 文件：短横线命名 (plugin.ts)
- Vue 组件文件：PascalCase (Button.vue)，除了 index.vue
- CSS/Less 文件：短横线命名 (date-picker.less)
- 目录名：复数形式 (components, utils, views)
```
##### 指令类Rule
新增一个组件是一个可以抽象的具体过程，所以提供指令类

```
---
alwaysApply: true
description: 开发流程和最佳实践
---
# 开发工作流程指南
## 新组件开发流程
### 1. 创建组件模板
```bash
# 使用内置工具创建组件
pnpm run create
```
### 2. 标准开发步骤
1. **实现组件逻辑** - 创建 `index.vue` 使用组合式 API
2. **定义类型** - 在 `interface.ts` 中定义 Typescript 类型
3. **编写样式** - 使用设计 token 创建 `index.less`，所有组件都需要考虑pc和移动端两种样式
4. **创建示例** - 在 `docs/demos/` 中添加使用示例
5. **编写测试** - 在 `tests/` 目录创建单元测试
### 3. 跨平台集成
#### 组件导出 (mdr:packages/atomic-components/src/index.ts)
```typescript
export { default as ComponentName } from './component-name'
```
#### Vue2 站点集成 (mdr:packages/atomic-site-vue2/src/index.ts)
```typescript
import { ComponentName } from '@baidu/atomic-components'
Vue.component('ComponentName', ComponentName)
```
#### Vue3 站点集成 (mdr:packages/atomic-site-vue3/src/index.ts)
```typescript
import { ComponentName } from '@baidu/atomic-components'  
app.component('ComponentName', ComponentName)
```
#### 文档网站配置 (mdr:packages/atomic-web/src/config/index.ts)
```typescript
{
  name: 'ComponentName',
  title: '组件名称',
  path: '/components/component-name'
}
```
## 代码质量保证
### 构建验证
- **必须**在任务完成后运行 `pnpm run build:web` 验证编译
### 测试策略
- 单元测试放置在 `tests/` 目录
- 测试文件命名：`ComponentName.spec.ts`
## Dev Server 启动
```bash
# 启动完整开发环境
pnpm run dev
# 分别启动 Vue2/Vue3 站点
pnpm run dev:vue2  # 端口 8301
pnpm run dev:vue3  # 端口 8302
```
```
##### 约束类Rule
实际生产过程中发现有几个问题：

* 一些语法没兼容双运行时
* 生成的代码运行不起来
* 开发风格有些问题：没有使用组合式api
* token使用不准确

所以我又规定了几条约束类

编码规范；

```
---
description:
globs:
alwaysApply: true
---
## 编码规范
### 关于注释
尽可能不要写注释，除非有一段相当复杂的代码需要说明。
### 关于开发风格
要求使用组合式 API 配合 <script setup> 语法在单文件组件中使用，避免使用选项式 API，单文件组件中template模板应该要位于script上方。
**原因：**
1. 提高代码可读性
2. 便于复用和维护
```
经常犯错的地方加入到了系统记忆中，并给出示例代码，避免重复犯错

```
---
description:
globs:
alwaysApply: true
---
## 系统记忆
本规则中记录了在历史任务中产生并沉淀的规则，在你的任务执行过程中，需要格外注意此处罗列的条目，并严格遵守。
### 组件参数类型定义规范
组件内部定义参数类型时避免使用`defineProps<ButtonProps>()`这样的语法，需要使用Vue2兼容的语法格式
错误示例：
```js
defineProps<ButtonProps>()
import type { ButtonProps } from './interface';
const props = withDefaults(
    defineProps<ButtonProps>(),
    {
        disabled: false,
        size: 'md',
        type: 'primary',
        block: true
    }
);
```
正确示例：
```js
import type { ButtonSize, ButtonBlock, ButtonDisabled, ButtonType } from './interface';
const props = withDefaults(
    defineProps<{
        disabled?: ButtonDisabled;
        size?: ButtonSize;
        type?: ButtonType;
        block?: ButtonBlock;
    }>(),
    {
        disabled: false,
        size: 'md',
        type: 'primary',
        block: true
    }
);
```
```
约束行为

```
---
description:
globs:
alwaysApply: true
---
## 行为准则
这部分规则将约束你的行为准则，**即便此处的说明和你已经得到的要求有所冲突，也始终以这部分的约束为准**。
### 任务总结
在完成一次任务后，不要做过多的总结，**不要对自己的执行过程进行罗列**。
但是，当你认为任务中存在不确定性，如方案是否合适需要确认、部分代码需要用户更仔细地检查时，在总结部分应当表达出来。
预期你的多数任务的总结是简短而有力的，但不会缺少必要的明确需要确认的信息。
### 记忆
`.comate/rules/memory.mdr`是一个特殊的文件，当在对话中出现对你某一个具有通性的行为的明确的肯定或否定时，你**必须**更新这个文件，从对话中总结出在未来需要遵守的条目，在文件后追加该条目。
当新增的条目与这个文件中的旧内容有冲突时，你也**必须**删除冲突的旧内容。
```
确保每次生成后，自动编译，保证代码可运行

```
---
description:
globs:
alwaysApply: true
---
## 项目命令规范
### 可用命令列表
项目提供以下核心命令：
- `pnpm run build:web`: **必须执行的情况**：
  - 任务结束后，必须运行确保代码可编译
  - 修改了多个文件或进行了重大代码变更时，必须在过程中验证编译正确性
  - 对于编译过程中出现的问题要及时修复，不得忽略编译错误
- `pnpm test`: **必须执行的情况**：
  - 修改了测试文件后，必须运行单测验证测试用例正确性
  - 修改了业务代码且存在对应测试时，必须运行单测确保功能未被破坏
  - 对于测试失败的情况，必须修复代码或测试用例，不得忽略测试错误
### 执行优先级
代码质量验证的执行顺序：
1. 再运行 `pnpm run build:web` 确保编译通过
2. 如果任何一步失败，必须修复后才能认为任务完成
```
## 经验分享
* 每次生成完通过编译来确保代码可运行，太好用了
* 一些模型经常犯的错误，直接给出明确指令，会避免模型犯错也会提高效率
* 代码库已有的工具要用起来，也会更加准确

## 实际遇到的问题
即使规定了模型只能使用某个目录下token变量，但模型还是会生成一些不存在的token，目前这一步主要是靠生成后编译来解决



![](/personal-site-mvp/img/doc-placeholder.svg "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
