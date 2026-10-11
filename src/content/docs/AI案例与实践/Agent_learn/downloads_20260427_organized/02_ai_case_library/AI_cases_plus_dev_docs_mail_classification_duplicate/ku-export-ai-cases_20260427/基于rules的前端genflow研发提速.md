---
title: "一、背景"
description: "基于rules的前端genflow研发提速"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\基于rules的前端genflow研发提速.md"
---
基于rules的前端genflow研发提速

#### 🧑‍🏫 案例作者：[@张嘉琦](https://ku.baidu-int.com?t=mention&mt=contact&id=d7062270-fce1-11f0-8d93-0d2d85a8d706)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了通过配置rules加速前端genflow研发的实践。通过定义项目基本信息和结构信息的rules，统一了包管理和依赖规范，简化了开发工作流。同时，利用指令类rules指导工具类开发，结合工具研发流程规范，提高了工具开发效率。约束类rules确保了生成代码的稳定性和可编译性。整体上，rules的引入显著降低了新人上手难度，加速了研发进程。
# 一、背景
文库PC端的genflow经历的2.0到3.0的不断迭代，整体的流程复杂且难以理解

新人上手门槛高，每次新增功能涉及的改动点较多，容易遗漏，排查问题的成本也较高

# 二、目标
通过配置rules方式，抹平流程上的认知差异，降低上手难度

同时在使用过程中不断演化rules，使人+AI共同进步

# 三、rules设计
## 3.1 信息类rules
使用zulu的规则生成指令，生成一份关于项目大体信息的规则

![](/personal-site-mvp/img/doc-placeholder.svg "")
可以看到生成了一个代码规范的规则和vue的开发规则，但是受限于模型理解能力，该类规则并不能很好的执行，去除这两个rules，加到指令类rules中作为校验使用

其他的rules我们可以在做一些细节上的补充

### 3.1.1 项目基本信息
```
---
alwaysApply: true
description: 包管理和依赖规范
---

# 包管理和依赖规范

## pnpm Workspace 配置

### 工作区结构
项目使用 [pnpm-workspace.yaml](mdr:pnpm-workspace.yaml) 配置：
```yaml
packages:
  - 'packages/*'
  - '!**/test/**'
```

### 强制使用 pnpm@8.3.1, 如果pnpm版本不对，退出后续所有指令，并提示用户安装正确的pnpm版本，提供安装的命令
通过 [package.json](mdr:package.json) 的 `preinstall` 脚本强制使用 pnpm：
```json
{
  "preinstall": "npx -y only-allow pnpm"
}
```

## 包命名规范

### 统一命名模式
所有包都使用 `@baidu/orion-ai-union-` 前缀：
- `@baidu/orion-ai-union-core`
- `@baidu/orion-ai-union-genflow-core`
- `@baidu/orion-ai-union-genflow-ui`
- `@baidu/orion-ai-union-pc`
- `@baidu/orion-ai-union-utils`

### 版本管理
- **开发发包**: 可以使用k-tool中的，kp命令一键发包、安装、部署开发环境，具体的使用方式可以查看当前目录下的k-tool.mdr
- **生产发包**: 统一在ipipe流水线发布，严禁在本地发布正式版本的包

## 依赖管理规范

### 内部包依赖
使用 workspace 协议引用内部包：
```json
{
  "dependencies": {
    "@baidu/orion-ai-union-core": "workspace:^",
    "@baidu/orion-ai-union-utils": "workspace:^"
  }
}
```

### 外部依赖版本锁定
关键依赖使用精确版本：
- **Vue**: 2.7.16 (PC包) / 2.7.16 & 3.5.13 (genFlow包)
- **TypeScript**: 5.5.4
- **Vite**: 4.5.3

### 开发依赖管理
- **ESLint**: 使用 @ecomfe/eslint-config 统一配置
- **StyleLint**: 使用 @ecomfe/stylelint-config 统一配置

## 开发工作流

### 依赖安装
在项目根目录下执行以下命令
```bash
# 全新安装
pnpm run initial
```

### 开发构建
在项目根目录下执行以下命令
```bash
# 构建所有包
pnpm build

# 构建特定包
pnpm build:core
pnpm build:pc
```

### 代码检查
在项目根目录下执行以下命令
```bash
# 检查所有包
pnpm run lint:core
pnpm run lint:pc
# ... 其他包
```

### 发布前检查
- 运行完整构建流程
- 验证代码规范
- 检查类型定义生成
- 验证依赖关系正确性

```
主要是细化项目使用的工具版本(pnpm)，和一些版本发布的规范，同时增加了一个我们内部的研发工具k-tool的说明，作为补充信息供AI读取参考

### 3.1.2 项目结构信息
```

---
alwaysApply: true
description: 项目结构和架构指南
---

# Orion AI Union 项目结构指南

## 项目概述
这是一个基于 pnpm workspace 的 monorepo 项目，包含多个相关的 npm 包，主要用于文库对话系统。

## 核心包结构

### 1. packages/core - 核心逻辑包
- **入口文件**: [src/index.ts](mdr:packages/core/src/index.ts)
- **主要功能**: 提供核心的 Union 类型定义和基础功能
- **路径别名**: 
  - `@union/*` → `./src/union/*`
  - `@uconf/*` → `./src/conf/*`
  - `@utype/*` → `./src/@types/*`

### 2. packages/genFlowCore - 生成流核心包
- **Vue 版本支持**: 同时支持 Vue 2.7 和 Vue 3
- **路径别名**:
  - `@gfconf/*` → `./src/conf/*`
  - `@gftype/*` → `./src/types/*`
  - `@gfhooks/*` → `./src/hooks/*`
- **构建命令**: 
  - `pnpm run switch:2` - 切换到 Vue 2
  - `pnpm run switch:3` - 切换到 Vue 3

### 3. packages/genFlowUI - 生成流UI组件包
- **Vue 版本支持**: 同时支持 Vue 2.7 和 Vue 3
- **构建脚本**: [scripts/build.sh](mdr:packages/genFlowUI/scripts/build.sh) 自动处理双版本构建
- **路径别名**: `@gusrc/*` → `./src/*`

### 4. packages/pc - PC端应用包
- **Vue 版本**: Vue 2.7.16
- **路径别名**: `@src/*` → `./src/*`
- **开发配置**: [build/vite.config.js](mdr:packages/pc/build/vite.config.js) 包含文件监听和自动重新编译

### 5. packages/utils - 工具包
- **最简单的包**: 仅包含通用工具函数
- **依赖**: piexifjs, dayjs
- **复用**: 优先复用此包中的方法，不要重复编写通用方法

```
删除一些和项目基本信息中重复的规则，增加通用包的复用规则

### 3.2 指令类rules
### 3.2.1 根据现有工具生成编写规则
![](/personal-site-mvp/img/doc-placeholder.svg "")
```
---
globs: packages/genFlowCore/src/hooks/toolsMap/toolClass/*.ts
description: 工具类开发编写规范
---

# 工具类开发编写规范

## 基础架构

### 类定义结构
所有工具类必须继承自 [Tool](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/Tool.ts) 基类：

```typescript
export class PPT extends Tool<IPPTData> {
    // 类实现
}
```

### 接口定义
工具数据接口必须继承 [IBaseToolData](mdr:packages/genFlowCore/src/hooks/toolsMap/conf/index.ts)：

```typescript
export interface IPPTData extends IBaseToolData {
    stepId: string;
    toolData: {
        type: 'tool_thoughts';
        run_object: {
            id: string;
            name: string;
            thoughts: {
                wenku_thoughts_index: number;
                thought_type: 'tt_tools_tips' | 'tt_makeppt_loading';
                content: string;
            };
        };
    };
}
```

## 核心属性规范

### cacheData 结构
缓存数据必须包含标准字段：

```typescript
cacheData = {
    bdjsonArr: [] as any[],        // 数据数组
    toolTipsContent: {},          // 工具提示内容
    isEnd: 0,                     // 结束状态
    detail: {                     // 详情信息
        docId: '',
        title: '未命名文件',
        status: 1,
        type: 'ppt',
    },
    opData: {                     // 操作数据
        docId: '',
        opRes: null,
    },
};
```

### 初始化标识
必须包含初始化标识：

```typescript
init = false;
```

## 核心方法实现

### consumerFn 方法
这是工具的核心消费方法，必须实现：

```typescript
consumerFn(data: IPPTData) {
    const thoughts = data.toolData?.run_object?.thoughts;
    const tool = this.getTool(data.stepId, data.toolData.run_object.id);

    // 初始化逻辑
    if (tool && !this.init) {
        this.cacheData.bdjsonArr = tool?.toolData?.bdjsonArr?.slice(0) || [];
        this.cacheData.toolTipsContent = tool?.toolData?.toolTipsContent || {};
        this.init = true;
    }

    // 根据thought_type处理不同逻辑
    if (thoughts?.thought_type === 'tt_tools_tips') {
        this.cacheData.toolTipsContent = safeJSONParse(thoughts?.content || '{}');
    }

    // 更新工具列表
    this.addOrUpdateToolToList({
        stepId: data.stepId,
        id: data.toolData.run_object?.id,
        toolData: {
            ...this.cacheData,
            bdjson: JSON.stringify(this.cacheData.bdjsonArr),
        },
    });
}
```

## 数据处理规范

### JSON 安全解析
必须使用 [safeJSONParse](mdr:packages/genFlowCore/src/hooks/utils/json.ts) 进行安全解析：

```typescript
const parsedData = safeJSONParse(thoughts?.content || '{}');
```

### 数据累加逻辑
对于分片数据，必须实现累加逻辑：

```typescript
if (currentSild?.[0]?.id) {
    // 数据累加
    this.cacheData.bdjsonArr.push(...currentSild);
} else if (currentSild?.doc_id_str) {
    // 结束状态处理
    this.cacheData.isEnd = 1;
    this.cacheData.detail = {
        docId: currentSild.doc_id_str,
        title: currentSild.title || '未命名文件',
        status: 2,
        type: 'ppt',
    };
}
```

## 错误处理和边界情况

### 空值检查
所有属性访问必须进行空值检查：

```typescript
const thoughts = data.toolData?.run_object?.thoughts;
```

### 默认值处理
为所有可能为空的值提供默认值：

```typescript
this.cacheData.toolTipsContent = tool?.toolData?.toolTipsContent || {};
```

## 工具状态管理

### 状态更新
通过 `addOrUpdateToolToList` 方法更新工具状态：

```typescript
this.addOrUpdateToolToList({
    stepId: data.stepId,
    id: data.toolData.run_object?.id,
    toolData: {
        ...this.cacheData,
        bdjson: JSON.stringify(this.cacheData.bdjsonArr),
    },
});
```

### 数据序列化
数组数据必须序列化为字符串：

```typescript
bdjson: JSON.stringify(this.cacheData.bdjsonArr)
```

## 代码注释规范

### 文件头注释
必须包含文件描述：

```typescript
/**
 * @file ppt
 * @desc ppt生成工具
 */
```

### ESLint 禁用规则
对于复杂逻辑，可以禁用特定规则：

```typescript
/* eslint-disable complexity */
```

## 类型安全

### 泛型使用
工具类必须使用泛型指定数据类型：

```typescript
export class PPT extends Tool<IPPTData>
```

### 类型导出
数据接口必须导出供外部使用：

```typescript
export interface IPPTData extends IBaseToolData
```

## 性能优化

### 数组拷贝
使用 `slice(0)` 创建数组副本避免引用问题：

```typescript
this.cacheData.bdjsonArr = tool?.toolData?.bdjsonArr?.slice(0) || [];
```

### 条件判断优化
将最可能的情况放在前面：

```typescript
if (thoughts?.thought_type === 'tt_tools_tips') {
    // 处理提示
} else if (thoughts?.thought_type === 'tt_makeppt_loading') {
    // 处理加载
}
```

```
发现生成的规则非常粗糙，只是对参考文件的总结，并没有理解整体实现流程，所以我又添加了一个工具的研发rules，用来帮助AI理解工具的研发模式

```
---
alwaysApply: true
description: genflow-core工具开发流程
---

# packages/genFlowCore/src/hooks/toolsMap/toolClass中复制一个ppt.ts出来(尽量不要自己重新写，从原来的工具中复制一个出来改最好)

## 一个工具的consumerFn大概分为三部分
    - 第一部分，50-54行，是为了兼容历史记录，因为历史记录使用的chat实例和实际发送的实例并不一致，所以需要在数据消费前初始化当前类的上下文，保证数据的一致性
    - 第二部分，56-82行，是数据消费的主逻辑，每个工具的数据格式不同，这部分的处理逻辑也会不同，需要根据返回的数据相对应的处理
    - 第三部分，84-91行，是将处理好的数据更新到messageList中对应的字段上，这个方法是继承基类Tool的，没有特殊的情况不用修改

# 在packages/genFlowCore/src/hooks/toolsMap/toolClassIndex.ts中添加新的导出

# 在packages/genFlowCore/src/hooks/toolsMap/conf.ts中添加对应的工具名映射和一些类型
```
添加tool-info.mdr的规则后，再次生成生成工具的rules

```
---
globs: packages/genFlowCore/src/hooks/toolsMap/toolClass/*.ts
description: 工具开发流程规范
---

# 工具开发流程规范

## 工具开发标准流程

### 第一步：复制现有工具
从 [packages/genFlowCore/src/hooks/toolsMap/toolClass](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass) 中复制一个最相似的作为模板：

> **重要**: 尽量不要自己重新写，从原来的工具中复制一个出来改最好

推荐模板：
- **复杂工具模板**: [ppt.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/ppt.ts)
- **简单工具模板**: [imgGen.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/imgGen.ts)

### 第二步：修改基础信息
```typescript
/**
 * @file newTool
 * @desc 新工具描述
 */

import { Tool } from '@gfhooks/toolsMap/toolClass/Tool';
import { IBaseToolData } from '@gfhooks/toolsMap/conf';
import { safeJSONParse } from '@gfhooks/utils/index';

export interface INewToolData extends IBaseToolData {
    stepId: string;
    toolData: {
        type: 'tool_thoughts';
        run_object: {
            id: string;
            name: string;
            thoughts: {
                wenku_thoughts_index: number;
                thought_type: 'tt_tools_tips' | 'tt_newtool_loading';
                content: string;
            };
        };
    };
}

export class NewTool extends Tool<INewToolData> {
    cacheData = {
        toolTipsContent: {},
        // ... 其他工具特定字段
    };
    init = false;
    
    // 实现三段式 consumerFn
    consumerFn(data: INewToolData) {
        // 第一部分：初始化（兼容历史记录）
        // 第二部分：数据消费主逻辑  
        // 第三部分：更新状态
    }
}
```

## consumerFn 三段式结构

### 第一部分：初始化（兼容历史记录）
```typescript
consumerFn(data: INewToolData) {
    const tool = this.getTool(data.stepId, data.toolData.run_object.id);

    if (tool && !this.init) {
        // 为了兼容历史记录，因为历史记录使用的chat实例和实际发送的实例并不一致
        // 需要在数据消费前初始化当前类的上下文，保证数据的一致性
        this.cacheData.toolTipsContent = tool?.toolData?.toolTipsContent || {};
        this.cacheData.data = tool?.toolData?.data || {};
        this.init = true;
    }
```

### 第二部分：数据消费主逻辑
```typescript
    // 每个工具的数据格式不同，这部分的处理逻辑也会不同
    // 需要根据返回的数据相对应的处理
    if (data.toolData?.run_object?.thoughts?.thought_type === 'tt_tools_tips') {
        this.cacheData.toolTipsContent = safeJSONParse(data.toolData?.run_object?.thoughts?.content || '{}');
    }
    else if (data.toolData?.run_object?.thoughts?.thought_type === 'tt_newtool_loading') {
        // 处理工具特定的数据逻辑
        const toolData = safeJSONParse(data.toolData?.run_object?.thoughts?.content || '{}');
        // 根据工具需求处理数据
    }
```

### 第三部分：更新状态
```typescript
    // 将处理好的数据更新到messageList中对应的字段上
    // 这个方法是继承基类Tool的，没有特殊的情况不用修改
    this.addOrUpdateToolToList({
        stepId: data.stepId,
        id: data.toolData.run_object?.id,
        toolData: this.cacheData,
    });
}
```

## 注册和配置

### 1. 添加导出
在 [packages/genFlowCore/src/hooks/toolsMap/toolClassIndex.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClassIndex.ts) 中添加：
```typescript
export { NewTool, INewToolData } from './toolClass/newTool';
```

### 2. 添加工具名映射
在 [packages/genFlowCore/src/hooks/toolsMap/conf.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/conf.ts) 中添加：
```typescript
export enum ToolName {
    // ... 现有工具
    newTool: 'newTool',
}

// 添加对应的工具名映射和一些类型
```

## 工具类型和模式

### 生成类工具模式
- **代表**: [ppt.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/ppt.ts)、[excel.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/excel.ts)、[codeGen.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/codeGen.ts)
- **特点**: 
  - 累积数据到数组 (`bdjsonArr.push(...)`)
  - 最终生成文件ID
  - 包含结束状态判断 (`this.cacheData.isEnd = 1`)

### 搜索类工具模式
- **代表**: [webSearch.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/webSearch.ts)、[imgGen.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/imgGen.ts)
- **特点**:
  - 处理搜索结果
  - 更新工具提示内容
  - 简单的数据结构

### 控制类工具模式
- **代表**: [toolBegin.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/toolBegin.ts)、[thoughtsExecute.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/thoughtsExecute.ts)、[commonTool.ts](mdr:packages/genFlowCore/src/hooks/toolsMap/toolClass/commonTool.ts)
- **特点**:
  - 管理消息列表
  - 控制执行流程
  - 复杂的状态管理

## thought_type 命名规范

### 标准类型（所有工具通用）
- `tt_tools_tips`: 工具提示信息
- `tt_file_ids`: 文件ID信息
- `call_action_error`: 调用错误

### 工具特定类型（按工具命名）
```typescript
// 命名模式：tt_{工具名小写}_loading
tt_makeppt_loading     // PPT生成
tt_websearch_loading    // 网络搜索
tt_excelgen_loading    // Excel生成
tt_code_gen_loading    // 代码生成
tt_newtool_loading     // 新工具
```

## 标准数据结构

### 通用 cacheData 结构
```typescript
cacheData = {
    toolTipsContent: {},    // 工具提示（所有工具必需）
    data: {},              // 主要数据（简单工具）
    isEnd: 0,              // 结束状态（生成类工具）
    // ... 其他工具特定字段
};
```

### 生成类工具扩展结构
```typescript
cacheData = {
    // 通用字段
    toolTipsContent: {},
    isEnd: 0,
    
    // 生成类特有字段
    bdjsonArr: [],          // 数据数组
    detail: {               // 文件详情
        docId: '',
        title: '未命名文件',
        status: 1,
        type: 'ppt',
    },
};
```

## 必须遵循的规范

### 1. 基础架构
- 继承自 `Tool<T>` 基类
- 接口继承自 `IBaseToolData`
- 使用泛型确保类型安全

### 2. 核心属性
- 必须包含 `cacheData` 对象
- 必须包含 `init = false` 标识
- 使用 `safeJSONParse` 进行安全解析

### 3. 数据处理
- 空值检查：`data.toolData?.run_object?.thoughts`
- 默认值处理：`|| {}` 或 `|| []`
- 数组拷贝：`slice(0)` 避免引用问题

### 4. 状态更新
- 通过 `addOrUpdateToolToList` 更新状态
- 数据序列化：`JSON.stringify()`
- 条件判断优化：常见情况放前面

### 5. 代码质量
- 文件头注释：`@file` 和 `@desc`
- ESLint 禁用：复杂逻辑使用 `/* eslint-disable complexity */`
- 类型导出：`export interface`

## 工具生命周期

### 1. 工具开始 (toolBegin)
- 初始化工具列表
- 设置工具显示模式
- 创建工具基础结构

### 2. 思考执行 (thoughtsExecute)  
- 创建新的执行轮次
- 管理打字机效果
- 处理思考内容展示

### 3. 具体工具执行
- 各个具体工具类处理
- 遵循三段式 consumerFn 结构
- 更新工具状态和数据

## 错误处理和边界情况

### 1. 数据解析错误
```typescript
const parsedData = safeJSONParse(content || '{}');
```

### 2. 工具不存在处理
```typescript
const tool = this.getTool(data.stepId, data.toolData.run_object.id);
if (!tool) {
    return; // 或错误处理
}
```

### 3. 历史记录兼容性
确保 `init` 逻辑能正确处理历史记录数据

## 校验生成结果
- 在项目根目录执行pnpm run build:genflow，验证是否能编译成功，如果失败，根据失败信息修改报错的文件

```
[附件]
可以看到，生成的文件是基本符合要求的，但是生成过程中发生了重复行为和偷懒，怀疑是一是模型的原因，二是规则还没有增加约束类的rules，AI没有严格依从指令类的规则

![重复](/personal-site-mvp/img/doc-placeholder.svg "重复")
![偷懒](/personal-site-mvp/img/doc-placeholder.svg "偷懒")
### 3.3 约束类rules
该类规则是用来强限制AI的能力覆盖范围，降低AI逃逸规则的风险，增加生成的稳定性

```
---
alwaysApply: true
description: 生成约束规则
---

# 生成或修改文件后，必须在项目根目录执行一次pnpm run build命令，检查编译是否成功，如果失败，输出失败信息，提出修改方案，不允许忽略，不允许跳过，不允许不执行

# 如果已执行过的步骤，不需要重复执行，继续向下执行

```
再添加了约束规则后，再次生成一个工具

[附件]
![](/personal-site-mvp/img/doc-placeholder.svg "")
发现已经没有重复和偷懒的行为，执行的非常顺畅，生成的结果也很稳定

# 四、总结
1. rules本质上是对AI的上下文补充，上下文越详细，AI生成的结果越符合需求
2. 信息类的rules可以先由AI生成，但是约束类规则最好人工编写，让AI编写可能会有对AI’友好‘的偷懒规则
3. 对于上面应用的模版类生成的场景，使用rules提效会非常明显，如果让一个新手去开发此类需求，大概需要～1d熟悉项目&新建工具开始开发，如果使用rules的话，3min可以新建架子，因为注入了流程上的rules，AI也可以帮助快速定位流程上产生的问题
4. 如果当前项目有详细的研发文档，也可以作为信息类rules，但是如果文档中有多模态内容，比如图片，视频等，可以先用AI做下内容理解，使用结构化的纯文本定义规则

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
