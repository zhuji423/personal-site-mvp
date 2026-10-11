---
title: "一、一见平台简介"
description: "一见平台前端整体架构rules配置&技能编排场景实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\一见平台前端整体架构rules配置&技能编排场景实践.md"
---
一见平台前端整体架构rules配置&技能编排场景实践

#### 🧑‍🏫 案例作者：[@张哲](https://ku.baidu-int.com?t=mention&mt=contact&id=36d75f40-fce5-11f0-8307-8315946bdd1e)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了一见平台前端整体架构的规则配置与技能编排场景实践，通过大模型自动生成详细架构规则，指导开发过程。内容涵盖平台定位、技术栈、开发规范、安全架构等多个方面，结合实际代码库分析，确保规则准确性和实用性。同时，展示了Zulu在技能编排中的应用，通过自动化生成和优化组件，提升开发效率，体现了大模型在复杂前端项目中的重要作用。
# 一、一见平台简介
一见平台是多模态专业视觉管理平台

* **一见定位：**基于多模态大模型的专业视觉管理平台
* **一见解决的核心问题：**无死角监控 -> 无死角管理  （基于视觉的管理数字化），重新定义看见的价值
* **三大场景：**大模型时代，企业生产过程中大量的安全、合规、品控等视觉检测需求正在被激活
    * 安全生产（私有化）：面向高危生产企业，解决隐患AI主动识别，安全管理数字化的问题
    * 连锁合规（公有云）：面向连锁门店，解决门店定销存、服务辅助、服务合规的量化管理问题
    * 工厂SOP（私有化）：面向工厂生产线，解决工序SOP合规等品控问题


# 二、背景
由于一见平台除了一些基础业务库（比如aibc业务组件库、 s3Sdk、一见微前端sdk等），**其他所有业务代码都是采用monorepo方案在一个代码仓库维护的**，这个代码仓库包括官网、一见4.9大模型平台以及5.0视觉应用平台及开发平台，更重要的是全局@com中还有公共库 16 package，一见公有云标品和私有化定制版是一份代码，所以在业务中要深度把coding agent用好，就必须让大模型对于这个仓库整体前端架构有个整体理解，大到知道每个包是什么作用，新代码应该写在哪里。小到新代码符合团队页面[统一规范](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/0ebIgLpF-L/gNnHNN0ejh/hK5O18lipAftSd)和[最佳实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/0ebIgLpF-L/g4MmmAbWVf/miib3NCsYEx295)。 **所以写一个整体前端架构的规则是非常重要的。**

# 三、前端经典场景实践
## 4.1 首先让zulu来理解下我们整体项目，生成一份rules看看
```
---
description: 
globs: 
alwaysApply: true
---
# 百度一见平台前端架构规则

## 项目概览

**项目定位**：百度ACG工业方向的企业级AI质检平台（AIQA）
**核心业务**：工业AI模型训练与管理、多租户SaaS平台、设备质检监控告警一体化解决方案
**技术架构**：React 18 + TypeScript + 微前端（Qiankun）+ Monorepo（Nx）

## 技术栈规范

### 核心框架
- **React 18.x**：使用Hooks API，禁止类组件
- **TypeScript**：全面采用，严格类型检查
- **Redux Toolkit + Zustand**：双轨制状态管理，复杂业务用Redux，局部状态用Zustand

### UI组件库
- **ACUD**：百度定制Ant Design版本（优先使用）
- **@baidu/aibc**：百度内部业务组件库
- **Ant Design**：原生版本作为补充
- **Framer Motion**：动画效果实现

### 构建工具
- **ReSKriPT**：百度自研脚手架（基于Webpack 5）
- **SWC**：Rust编译器，提升构建速度
- **Vite**：部分模块开发环境使用

## 模块架构

### Monorepo结构
```
packages/
├── @com/           # 公养组件库（@yijian/*命名空间）
├── apaas/          # 低代码平台模块
├── app/            # 移动端应用
├── base/           # 基础服务模块
├── custom/         # 客户定制模块
├── spi/            # 核心业务模块
└── yijian-home/    # 主应用（微前端基座）
```

### 模块职责划分
- **@com**：统一工具库，按业务域分层（common/biz/old）
- **custom**：客户差异化实现（kangtuo/ruixing/shuyi）
- **微前端**：主应用负责任务调度，子应用独立部署

## 项目级开发契约

### 工具类组织
- **统一导入**：优先使用`@yijian/*`内部工具库
- **请求封装**：统一使用`axiosRequest.js`工厂函数，50秒超时
- **错误处理**：401统一跳转鉴权，响应格式`{success, message: {code}}`

### 组件封装模式
- **组件结构**：`React.memo + forwardRef`优化
- **表单组件**：统一使用`Form + Form.Item`模式
- **列表组件**：统一使用`Table + 分页器`模式
- **业务组件**：按域划分`@com/components/biz/{alarm,skill,device}`

### 状态管理规范
- **Redux**：复杂业务状态，统一在`@com/store`集中导出
- **Zustand**：组件级状态，支持`persist`持久化
- **不可变更新**：统一使用`immer`处理

### 日志规范
- **开发环境**：详细日志输出
- **生产环境**：关闭日志输出
- **错误格式**：`console.error('[模块名] 错误描述', error)`
- **分级管理**：log（调试）/warn（警告）/error（错误）

## 命名与结构规范

### 文件命名
- **组件**：PascalCase（`ProductCard/index.tsx`）
- **工具函数**：camelCase（`useClient.ts`）
- **常量**：camelCase文件，UPPER_SNAKE_CASE值
- **Hooks**：use前缀（`useScroll.ts`）

### 目录结构
```
src/
├── components/     # 公共组件
├── hooks/         # 自定义Hooks
├── utils/         # 工具函数
├── constants/     # 常量定义
├── types/         # 类型定义
├── server/        # 服务端相关
└── assets/        # 静态资源
```

### 样式规范
- **CSS Modules**：`*.module.less`文件启用
- **类名规范**：小写+连字符（`.product-card`）
- **BEM扩展**：`.product-card-content`
- **状态类名**：`is-`前缀（`.is-active`）

### 类型定义
- **接口**：PascalCase，完整JSDoc注释
- **枚举**：PascalCase命名，UPPER_SNAKE_CASE值
- **Props接口**：`组件名 + Props`格式

## 百度生态集成

### 内部组件库
- **ACUD**：优先使用百度定制Ant Design
- **@baidu/aibc**：内部业务组件，深度集成
- **虚拟导航**：`VIRTUAL_BASE_URL`配置

### 构建配置
- **ReSKriPT**：统一构建配置，基于Webpack 5
- **分包策略**：maxSize: 10MB，minSize: 300KB
- **按需加载**：babel-plugin-import实现
- **多环境支持**：dev/qa/preonline/online

## 代码质量规范

### ESLint规则
- **控制台警告**：`no-console: ['warn']`
- **参数限制**：方法最多8个参数
- **箭头函数**：允许使用提升可读性
- **变量定义**：允许先使用后定义（需谨慎）

### Git提交
- **提交前检查**：设置Git Hook
- **代码检查**：不通过无法提交

## 开发环境配置

### 路径别名
- **`@/`**：指向`src/`目录
- **内部包**：`@yijian/*`统一命名空间

### 代理配置
- **开发环境**：统一在`devServer.proxy`配置
- **HTTPS支持**：开发环境支持HTTPS
- **跨域处理**：开发环境设置`Access-Control-Allow-Origin: *`

### 端口规范
- **主应用**：8898端口
- **子应用**：按模块分配端口

## 国际化支持

### 实现方案
- **i18next + react-i18next**：统一国际化方案
- **默认函数**：`DEFAULT_T_FUNCTION = str => str`
- **语言检测**：`i18next-browser-languagedetector`

## 权限管理

### 权限模型
- **统一接口**：`Authorizations`权限接口
- **用户状态**：包含`roleList`、`dataPermission`、`cloudId`
- **功能权限**：支持`FunctionPermission`树形结构

## 关键开发命令

```bash
# 开发启动
npm run start        # 启动开发服务器
npm run build        # 生产环境构建
npm run lint         # 代码质量检查
npm run fix:style    # 样式格式化
```

---

**注意**：所有规则基于真实代码库分析得出，禁止虚构推断。不确定内容已标注[需人工确认]。

**最终规则**：所有回答均使用中文

```
可以看到它写了几个部分

* 项目概览
    * 核心业务说明：这部分里面一些平台和业务介绍过时了，大概率是之前业务平台里面写的marddown介绍过时了。
    * 技术架构：整体这块写的太简单了

* 技术栈规范
    * 状态管理方式有分析到用了Redux Toolkit + Zustand，但是团队最新希望统一到Zustand
    * UI组件有识别历史代码用到少量ant design，但目前新代码统一使用acud。这是属于规范范围的。需要告诉大模型
    * 构建工具探测到reSKRipt 这个百度自研脚手架，但没有说明非子应用都使用其中vite配置，子应用由于vite对于当前微前端框架qiankun支持有一个bug使用webpack。

* 关于monorepo代码分层
    * 对于各个包的理解有偏差

* 项目开发契约（规范）& 代码规范
    * 直接让它从代码层理解有不少偏差。
    * 对于最重要的列表和表单组件推荐使用acud的组件，这是完全不正确的，我们推荐使用的是aibc的List和Form组件。这块比较有疑惑，我们业务中80%列表和表单都是用最新写法了，这块分析为啥还是错的比较困惑。

* 关键开发命令
    * 缺失不少不完整


此步总结：仅仅读取源码的情况下，自动产出的整体架构规则还有不少问题，当然也有很大一部原因之前各个包中的readme文件写的还是比较简单。

## 4.2 给大模型更多之前沉淀的文档
虽然之前在代码中readme比较少，但是之前知识库中有不少关于一见架构和开发规范的总结文档。

[一见前端技术架构（2025-03-21）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/0ebIgLpF-L/gNnHNN0ejh/waC1iBGdOgwsbW?t=mention&mt=doc&dt=doc)

[ACG工业一见平台用户体验规范](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/0ebIgLpF-L/gNnHNN0ejh/hK5O18lipAftSd?t=mention&mt=doc&dt=doc)

[React 及 hooks 规范及最佳实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/0ebIgLpF-L/g4MmmAbWVf/miib3NCsYEx295?t=mention&mt=doc&dt=doc)

把他们导成pdf，让zulu （claude4.5模型）帮我生成一份规则。

```
---
alwaysApply: true
description: 一见平台整体技术架构规则
---

# 一见平台整体技术架构规则

## 架构概览

### 项目定位
- **平台名称**: 百度一见（yijian-fe）
- **业务领域**: ACG工业AI质检平台（AIQA）
- **核心能力**: 工业AI模型训练、多租户SaaS服务、设备质检监控告警、低代码平台
- **技术架构**: Monorepo + 微前端 + 多应用生态

### 技术栈总览
- **前端框架**: React 18.x（Hooks API）
- **类型系统**: TypeScript 5.x（严格模式）
- **状态管理**: Redux Toolkit 2.x + Zustand
- **构建工具**: ReSKriPT（基于Webpack 5）+ Nx + pnpm
- **微前端**: @baidu/micro-fusion（基于Qiankun）
- **UI组件**: ACUD（百度定制Ant Design）+ @baidu/aibc

## Monorepo架构设计

### 工作空间结构
项目采用pnpm Workspace + Nx的Monorepo架构，支持多应用、多团队协作开发。

#### 核心分层
```
packages/
├── @com/           # 公共基础层（@yijian/*命名空间）
│   ├── api/        # API服务层（旧版）
│   ├── api-new/    # API服务层（5.0新版）
│   ├── components/ # 业务组件库
│   ├── hooks/      # 公共Hooks库
│   ├── store/      # Redux全局状态
│   ├── constants/  # 业务常量
│   ├── types/      # TypeScript类型定义
│   ├── utils-new/  # 工具函数库
│   ├── assets/     # 静态资源
│   ├── styles/     # 主题样式
│   └── configure/  # 路由与配置
│
├── spi/            # SPI核心业务层（主应用生态）
│   ├── app-core/           # SPI主应用基座
│   ├── iflow/              # 流程编排引擎
│   ├── labelset/           # 标注集管理
│   ├── modelstore/         # 模型仓库
│   ├── train/              # 模型训练
│   ├── endpointhub/        # 端点管理
│   ├── base-admin/         # 系统管理
│   ├── base-data-pool/     # 数据湖
│   ├── base-tenant-manage/ # 租户管理
│   ├── app-monitor-alarm/  # 监控告警
│   ├── app-sop/            # SOP标准作业
│   ├── app-video-monitor/  # 视频监控
│   └── apaas-skill/        # APaaS技能
│
├── apaas/          # APaaS低代码平台层
│   ├── apaas-core/  # APaaS主应用基座
│   ├── apaas-data/  # 数据管理模块
│   ├── apaas-model/ # 模型管理模块
│   ├── apaas-train/ # 训练管理模块
│   └── apaas-skill/ # 技能管理模块
│
├── app/            # 移动端应用层（5.0新架构）
│   ├── app-core/           # App主应用基座
│   ├── app-device-center/  # 设备中心
│   ├── app-monitor-alarm/  # 监控告警（新版）
│   ├── app-sop/            # SOP管理（新版）
│   └── app-visual-analysis/ # 视图分析
│
├── base/           # 基础服务层（5.0新架构）
│   ├── base-data-pool/      # 数据湖（新版）
│   ├── base-skill/          # 技能管理（新版）
│   └── base-tenant-manage/  # 租户管理（新版）
│
├── custom/         # 客户定制层
│   ├── custom-core/ # 定制基座
│   ├── kangtuo/     # 康拓定制版本
│   ├── ruixing/     # 瑞星定制版本
│   └── shuyi/       # 舒逸定制版本
│
└── yijian-home/    # 主门户（微前端基座）
```

### 架构分层原则

#### 1. 公共基础层（@com）
- **职责**: 提供跨应用的公共能力（组件、工具、类型、API封装）
- **命名空间**: 统一使用`@yijian/*`导入
- **依赖方向**: 不依赖任何业务层，被所有应用层依赖
- **版本管理**: workspace协议（`workspace:^`）

#### 2. 业务应用层（spi/apaas/app/base）
- **spi**: 面向企业级客户的完整功能平台（4.x版本主线）
- **apaas**: 低代码平台生态（独立部署）
- **app**: 面向移动端的轻量化应用（5.0新架构）
- **base**: 5.0架构的基础服务模块（跨平台复用）

#### 3. 定制层（custom）
- **职责**: 满足特定客户的差异化需求
- **架构**: 继承custom-core基座，按客户划分子包
- **部署**: 独立部署，不影响标准版本

### 包命名规范

所有内部包必须使用`@yijian/`命名空间：

```typescript
// ✅ 正确：使用命名空间导入
import {useClient} from '@yijian/hooks';
import {ProductCard} from '@yijian/components';
import {API_SPI_PREFIX} from '@yijian/api';

// ❌ 错误：不要使用相对路径跨包导入
import {useClient} from '../../../@com/hooks';
```

### 依赖管理策略

#### Workspace协议
所有内部包依赖使用`workspace:^`协议：

```json
{
  "dependencies": {
    "@yijian/api": "workspace:^",
    "@yijian/components": "workspace:^",
    "@yijian/hooks": "workspace:^"
  }
}
```

#### 外部依赖版本锁定
- **根package.json**: 定义所有外部依赖的统一版本
- **子包package.json**: 只声明实际使用的依赖，版本自动继承根配置
- **幽灵依赖处理**: 使用pnpm的strict模式避免幽灵依赖

## 微前端架构

### 主子应用模型

#### 主应用职责（yijian-home）
- **路由管理**: 控制子应用的激活和卸载
- **权限管理**: 统一鉴权和权限控制
- **全局状态**: 提供跨应用的共享状态
- **通信机制**: 通过props和自定义事件实现主子通信

#### 子应用接入规范
所有子应用必须在[packages/@com/configure/micro.config.ts](mdr:packages/@com/configure/micro.config.ts)注册：

```typescript
export interface MicroConfig {
    name: string;           // 子应用唯一标识
    entry: string;          // 子应用访问路径
    container: string;      // 挂载DOM的ID
    activeRule: string;     // 激活路由规则
    props: {
        basepath: string;       // 子应用路由basename
        apiUrl: string;         // 接口请求地址
        publicPath: string;     // 静态资源路径
        spiRoutePrefix?: string; // 路由前缀
        spiEmitter?: any;       // 主应用事件总线
    };
}
```

#### 子应用类型
- **SPI子应用**: endpoint-fe、train-fe、annotation-fe、model-store-fe
- **APaaS子应用**: apaas-model-fe（独立低代码平台）
- **管理子应用**: tenant-manage-fe（租户管理）

### 通信机制

#### 1. Props传递（主→子）
```typescript
props: {
    spiEmitter: emitter,              // 主应用事件总线
    spiEventTypeEnum: EventTypeEnum,  // 事件类型枚举
    isPrivate: false,                 // 环境标识
    platform: 'spi',                  // 平台标识
}
```

#### 2. 事件总线（子→主、子↔子）
使用`@yijian/utils-new/biz/emitter`实现跨应用通信：

```typescript
// 子应用发送事件
props.spiEmitter.emit(EventTypeEnum.ROUTE_CHANGE, {path: '/new-route'});

// 主应用监听事件
emitter.on(EventTypeEnum.ROUTE_CHANGE, (data) => {
    // 处理路由变化
});
```

#### 3. 全局状态共享
通过主应用Redux Store实现跨应用状态共享。

## 构建与部署架构

### Nx任务编排

#### 任务依赖图
Nx自动分析包依赖关系，按拓扑序执行构建任务：

```json
{
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],        // 先构建依赖包
      "inputs": ["noMarkdown"],       // 忽略Markdown文件
      "outputs": ["{projectRoot}/dist"]
    }
  }
}
```

#### 增量构建
- **缓存策略**: 基于文件内容哈希缓存构建产物
- **缓存操作**: build、test、lint
- **缓存位置**: `.nx/cache/`

### ReSKriPT构建配置

#### Webpack优化策略
[reskript.base.ts](mdr:reskript.base.ts)定义全局构建配置：

```typescript
// 代码分包优化
webpackConfig.optimization.splitChunks = {
    chunks: 'all',
    maxSize: 2 * 1024 * 1024,      // 单chunk最大2MB
    minSize: 100 * 1024,           // 最小100KB
    maxInitialSize: 2 * 1024 * 1024,
    minRemainingSize: 100 * 1024,
    maxAsyncRequests: 30,          // 最大异步请求数
    maxInitialRequests: 30,        // 最大初始请求数
    enforceSizeThreshold: 500 * 1024,
};

// 产物路径优化
webpackConfig.output = {
    filename: 'static/js/[name].[contenthash:8].js',
    chunkFilename: 'static/js/[name].[contenthash:8].chunk.js',
    assetModuleFilename: 'static/img/[name].[hash][ext]',
};
```

#### 按需加载配置
使用babel-plugin-import实现组件库按需引入：

```typescript
// ACUD按需引入
babelConfig.plugins.push([
    'import',
    {libraryName: 'acud', style: true, libraryDirectory: 'es'},
    'acud',
]);

// @baidu/aibc按需引入
babelConfig.plugins.push([
    'import',
    {libraryName: '@baidu/aibc', style: true, libraryDirectory: 'es'},
    '@baidu/aibc',
]);
```

### 多环境配置

#### 环境类型
- **development**: 本地开发环境
- **qa**: 测试环境
- **preonline**: 预发布环境
- **online**: 生产环境

#### 环境变量注入
每个应用根目录配置`.env.*`文件：

```bash
# .env.development
NODE_ENV=development
API_BASE_URL=https://dev.baidu.com

# .env.production
NODE_ENV=production
API_BASE_URL=https://api.baidu.com
```

### K8s部署配置

#### 部署目录结构
```
deploy/
├── k8s/
│   ├── bin/
│   │   └── helm_install.sh      # Helm部署脚本
│   └── chart/
│       ├── templates/           # K8s资源模板
│       ├── values.yaml          # 默认配置
│       ├── values-online.yaml   # 生产环境配置
│       └── values-preonline.yaml # 预发布配置
└── Dockerfile                   # 容器镜像构建
```

#### 部署流程
1. **构建**: `pnpm build` → 生成dist产物
2. **打包**: `docker build` → 构建容器镜像
3. **发布**: `helm install` → K8s集群部署

## API架构设计

### API分层结构

#### 统一API前缀管理
[packages/@com/api/constants.ts](mdr:packages/@com/api/constants.ts)定义所有API前缀：

```typescript
export const API_SPI_PREFIX = '/api/spi';              // SPI核心业务
export const API_VISTUDIO_PREFIX = '/api/vistudio';    // 模型训练
export const API_WINDMILL_PREFIX = '/api/windmill';    // 任务调度
export const API_SOP_PREFIX = '/api/sop';              // SOP标准作业
export const API_DATA_POOL_PREFIX = '/api/datapool';   // 数据湖
export const API_ANNOTATION_PREFIX = '/api/annotation'; // 标注集
export const API_MODEL_STORE_PREFIX = '/api/modelstore'; // 模型仓库
export const API_ALARM_PREFIX = '/api/alarm';          // 告警管理
export const API_SKILL_PREFIX = '/api/skill';          // 技能管理
```

### API请求封装规范

#### 统一请求工厂
所有API请求必须使用`axiosRequest`工厂函数：

```typescript
import axiosRequest from '@yijian/api/server';

// 定义API函数
export const getProductList = (params: ProductQuery) => {
    return axiosRequest<ProductListResponse>({
        url: `${API_SPI_PREFIX}/product/list`,
        method: 'POST',
        data: params,
        timeout: 50000, // 统一50秒超时
    });
};
```

#### 响应格式规范
所有接口响应必须符合统一格式：

```typescript
interface ApiResponse<T> {
    success: boolean;           // 请求成功标识
    message: {
        code: string;           // 业务错误码
        message?: string;       // 错误描述
    };
    result?: T;                 // 业务数据
}
```

### 错误处理机制

#### 统一错误拦截
- **401未授权**: 自动跳转登录页
- **403无权限**: Toast提示权限不足
- **500服务错误**: Toast提示服务异常
- **网络错误**: Toast提示网络连接失败

## 状态管理架构

### Redux全局状态

#### Store结构
[packages/@com/store/index.ts](mdr:packages/@com/store/index.ts)定义全局状态树：

```typescript
export const store = configureStore({
    reducer: {
        upload: uploadSlice,                      // 任务上传面板
        filter: filterSlice,                      // 筛选条件状态
        subscription: subscriptionSlice,          // 订阅管理
        modelConfigurations: modelConfigurationsSlice, // 模型配置
        skillArrangement: skillArrangementSlice,  // 技能编排
        organization: organizationSlice,          // 组织架构
    },
});
```

#### Slice设计规范
每个业务域独立Slice，使用Redux Toolkit的createSlice：

```typescript
import {createSlice, PayloadAction} from '@reduxjs/toolkit';

const uploadSlice = createSlice({
    name: 'upload',
    initialState: {
        visible: false,
        taskList: [],
    },
    reducers: {
        showPanel: (state) => {
            state.visible = true;
        },
        addTask: (state, action: PayloadAction<Task>) => {
            state.taskList.push(action.payload);
        },
    },
});
```

### Zustand轻量级状态

#### 使用场景
- 组件级UI状态（如展开/收起、选中项）
- 表单临时状态（如草稿数据）
- 需要持久化的用户偏好设置

#### Store定义规范
[packages/@com/store/zustand/](mdr:packages/@com/store/zustand/)目录下按域划分：

```typescript
import {create} from 'zustand';
import {persist} from 'zustand/middleware';

interface FilterState {
    keywords: string;
    category: string;
    setKeywords: (keywords: string) => void;
}

export const useFilterStore = create<FilterState>()(
    persist(
        (set) => ({
            keywords: '',
            category: '',
            setKeywords: (keywords) => set({keywords}),
        }),
        {name: 'filter-storage'}  // localStorage key
    )
);
```

### 状态选择原则
- **全局业务状态**: Redux Toolkit（如用户信息、权限、订阅状态）
- **跨页面共享**: Redux Toolkit
- **组件级状态**: Zustand或组件内useState
- **表单状态**: 优先使用Ant Design Form内部状态
- **服务端数据**: 使用React Query或SWR管理缓存

## 路由架构

### 路由常量管理
[packages/@com/configure/routes/allPath.ts](mdr:packages/@com/configure/routes/allPath.ts)集中定义所有路由：

```typescript
export const ALL_PATH = {
    // 工作台
    HOME: '/',
    
    // 体验中心
    EXPERIENCER_HOME: '/experiencer',
    
    // 技能管理
    POWER_SKILL_COMMON: '/power/skill/common/store',
    POWER_SKILL_COMMON_DETAIL: '/power/skill/common/store/detail/:id',
    
    // 监控告警
    MONITOR_ALARM_CAMERA: '/app/monitor/alarm/camera',
    MONITOR_ALARM_AUDIO: '/app/monitor/alarm/audio',
    
    // 数据湖
    DATA_POOL: '/base/data-pool',
    DATA_POOL_DETAIL: '/base/data-pool/detail/:id',
};
```

### 路由使用规范
- **禁止硬编码**: 必须使用`ALL_PATH`常量引用路由
- **动态参数**: 使用`:paramName`格式定义
- **路由跳转**: 统一使用`useNavigate` Hook

```typescript
// ✅ 正确：使用路由常量
import {ALL_PATH} from '@yijian/configure/routes/allPath';
navigate(ALL_PATH.POWER_SKILL_COMMON);

// ❌ 错误：硬编码路由
navigate('/power/skill/common/store');
```

## 权限管理架构

### 权限模型

#### 数据结构
[packages/@com/configure/auth/](mdr:packages/@com/configure/auth/)定义权限接口：

```typescript
interface UserAuthInfo {
    roleList: Role[];              // 角色列表
    dataPermission: DataPermission[]; // 数据权限
    cloudId: string;               // 云账号ID
    functionPermission: FunctionPermission[]; // 功能权限树
}

interface FunctionPermission {
    code: string;                  // 权限码
    name: string;                  // 权限名称
    children?: FunctionPermission[]; // 子权限
}
```

### 权限验证

#### 路由级权限
在路由配置中声明所需权限：

```typescript
{
    path: ALL_PATH.POWER_SKILL_COMMON,
    element: <SkillStore />,
    meta: {
        requireAuth: true,
        permissions: ['skill:view'],
    },
}
```

#### 组件级权限
使用权限HOC包裹组件：

```typescript
import {withAuth} from '@yijian/configure/auth';

const DeleteButton = withAuth(
    Button,
    {permissions: ['skill:delete']}
);
```

## 百度生态集成

### 内部组件库

#### ACUD（优先使用）
百度定制Ant Design，深度集成百度设计规范：

```typescript
import {Button, Table, Form} from 'acud';
```

#### @baidu/aibc
百度内部业务组件库，包含行业通用组件：

```typescript
import {ProductCard, DataTable} from '@baidu/aibc';
```

### 百度云服务集成

#### 对象存储（@baidu/s3sdk）
```typescript
import {S3Client} from '@baidu/s3sdk';

const s3Client = new S3Client({
    bucket: 'yijian-bucket',
    region: 'bj',
});
```

#### 视频播放（@baidu/evs-player）
```typescript
import {EvsPlayer} from '@baidu/evs-player';

<EvsPlayer
    src="https://video.baidu.com/xxx.mp4"
    controls
/>
```

#### 智能对话（@baidu/industry-chatsdk）
```typescript
import {ChatSDK} from '@baidu/industry-chatsdk';

const sdk = new ChatSDK({
    appId: 'xxx',
    token: 'xxx',
});
```

## 性能优化策略

### 代码分包优化
- **单chunk最大**: 2MB
- **单chunk最小**: 100KB
- **最大并行请求**: 30个
- **强制分包阈值**: 500KB

### 组件懒加载
使用React.lazy实现路由级懒加载：

```typescript
import {lazy, Suspense} from 'react';

const SkillStore = lazy(() => import('./pages/SkillStore'));

<Suspense fallback={<Loading />}>
    <SkillStore />
</Suspense>
```

### 图片资源优化
- **格式**: 优先使用WebP格式
- **压缩**: 使用TinyPNG压缩
- **懒加载**: 使用`loading="lazy"`属性

### 接口请求优化
- **并发控制**: 最多5个并发请求
- **请求去重**: 相同请求复用结果
- **接口缓存**: 使用SWR或React Query

## 开发工作流

### 本地开发

#### 启动命令
```bash
# 启动SPI主应用
pnpm start

# 启动APaaS应用
pnpm start:apaas

# 启动App应用
pnpm start:app

# 启动所有应用（开发调试）
pnpm start:all
```

#### 开发服务器配置
- **主应用端口**: 8898
- **子应用端口**: 按模块分配（8888-8899）
- **HTTPS支持**: 开发环境支持HTTPS

### 代码质量

#### Lint检查
```bash
# 检查所有包
pnpm lint

# 自动修复
pnpm lint-fix
```

#### Git Hooks
项目配置了pre-commit钩子：
- ESLint检查
- Stylelint检查
- TypeScript类型检查
- 检查不通过禁止提交

### 构建部署

#### 构建命令
```bash
# 构建SPI主应用
pnpm build

# 构建所有应用
pnpm build:all

# 构建SPI生态应用
pnpm build:spi-all

# 构建APaaS生态应用
pnpm build:apaas-all
```

#### 增量构建
```bash
# 仅构建变更包
pnpm affected
```

## TypeScript配置架构

### 基础配置
[tsconfig.base.json](mdr:tsconfig.base.json)定义全局TS配置：

```json
{
  "compilerOptions": {
    "target": "ES2018",
    "module": "ESNext",
    "jsx": "react-jsx",
    "strict": false,                      // 暂未启用严格模式
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "allowSyntheticDefaultImports": true,
    "experimentalDecorators": true,
    "lib": ["es2021", "dom", "es7", "es6", "es5"]
  }
}
```

### 路径映射策略
所有内部包通过paths映射实现别名导入：

```json
{
  "paths": {
    "@yijian/api/*": ["./packages/@com/api/*"],
    "@yijian/components/*": ["./packages/@com/components/*"],
    "@yijian/hooks/*": ["./packages/@com/hooks/*"],
    "@yijian/app-monitor-alarm/*": ["./packages/spi/app-monitor-alarm/src/*"]
  }
}
```

## 国际化架构

### 技术方案
- **核心库**: i18next + react-i18next
- **语言检测**: i18next-browser-languagedetector
- **默认回退**: `DEFAULT_T_FUNCTION = str => str`

### 语言资源管理
[packages/@com/i18n/locales/](mdr:packages/@com/i18n/locales/)按语言划分：

```
locales/
├── zh-CN/      # 简体中文
├── en-US/      # 英文
└── index.ts    # 资源聚合
```

## 安全架构

### 鉴权机制
- **IAM集成**: 百度统一身份认证
- **Token管理**: JWT令牌，自动刷新
- **权限验证**: 基于RBAC的权限模型

### 数据安全
- **敏感数据**: 前端不存储敏感信息
- **XSS防护**: React默认转义 + CSP策略
- **CSRF防护**: Token验证

## 监控与日志

### 前端监控
- **性能监控**: Web Vitals指标采集
- **错误监控**: Sentry错误上报
- **用户行为**: 百度统计集成

### 日志规范
- **开发环境**: 详细日志输出
- **生产环境**: 关闭日志输出
- **错误格式**: `console.error('[模块名] 错误描述', error)`

## 架构演进规划

### 版本规划
- **4.x版本**: SPI主线（当前稳定版本）
- **5.0版本**: App + Base新架构（逐步迁移中）
- **APaaS**: 独立低代码平台生态

### 技术债务
- **旧组件重构**: packages/@com/components/old/待迁移
- **API统一**: 逐步从api/迁移到api-new/
- **类型增强**: 逐步启用strict模式

---

**注意**: 本规则基于项目实际代码分析生成，所有架构设计和技术选型均为项目真实情况，禁止虚构。
```


可以看到结合一些现有文档 ，生成的架构规则明显详细准确多了，详细分析如下

好的部分：

* 技术栈总览比之前版本更加详细
* 代码分层更加详细，每个package都有说明，而且基本判断准确。
* 对于微前端集成方式有简单说明。
* 包含了启动、打包等一系列应用
* 包含了全局状态工具zustand使用说明

不好的部分

* 有点冗余，有些不是当下最关心的内容，已经不太需要改的东西它也生成了规则。
* 安全架构这块有点范，作用不大。
* 对于前端最佳实践规范总结的不清楚
* 对于编写经典场景页面总体架构说明缺失。
* TypeScript配置架构 这个模块意义不大，因为一般后续不太会去大改。
* 对于性能优化说明也不需要出现在整体架构规则中。



## 4.3 持续给大模型提了几次建议  + 人工修改后版本
接下来又经过几轮修改建议 + 人工修改建议最终得到yijian-fe 总体project规则如下

```

---
description: 一见平台前端整体架构及开发规范规则
globs: 
alwaysApply: true
---

# 一见平台前端整体架构及开发规范规则

本规范基于**一见平台（yijian-fe）**的实际代码库结构，涵盖技术架构、开发规范指南等全方位指引。

## 一见平台整体业务概述

一见平台是多模态专业视觉管理平台
* 一见定位：基于多模态大模型的专业视觉管理平台
* 一见解决的核心问题：无死角监控 -> 无死角管理  （基于视觉的管理数字化），重新定义看见的价值
* 三大场景：大模型时代，企业生产过程中大量的安全、合规、品控等视觉检测需求正在被激活
    * 安全生产（私有化）：面向高危生产企业，解决隐患AI主动识别，安全管理数字化的问题
    * 连锁合规（公有云）：面向连锁门店，解决门店定销存、服务辅助、服务合规的量化管理问题
    * 工厂SOP（私有化）：面向工厂生产线，解决工序SOP合规等品控问题

## 技术栈总体说明
- **前端框架**: React 18.x（Hooks API 及方法组件）+ react-routet-dom
- **开发语言**: TypeScript 5.x（严格模式）
- **状态管理**: Zustand latest版本
- **构建工具（脚手架）**: 百度内部工具 reSKRipt（基于vite 或者 webpack）+ pnpm + Nx
- **微前端框架**: 底层QianKun 上层 `@baidu/micro-fusion`
- **核心业务组件库**: 一见业务组件库 [@baidu/aibc](https://acg-packages-v3.now.baidu-int.com/aibc/components/list) 
- **UI基础组件库**: [ACUD（百度acg部门定制Ant Design）](https://acud.now.baidu-int.com/components/button)
- **s3管理库**: `@baidu/s3sdk`,包含s3协议文件的上传、查看、删除等功能。
- **智能对话sdk**: `@baidu/industry-chatsdk` 度安安是基于这个库实现的
- **请求库**: axios
- **主要工具库**: lodash-es、dayjs、moment
- **hooks库**: 百度内部hooks库huse、ahooks
- **样式方案**: less
- **国际化**: i18next + react-i18next
- **图表库**: echarts5

## 主要开发命令

```bash
# 安装依赖
pnpm install

# 启动开发服务
pnpm start              # 启动一见4.9主应用（spi）
pnpm start:apaas        # 启动技能开发平台应用(apaas)
pnpm start:app          # 启动视觉应用平台(app)
pnpm start:all          # 启动所有应用

# 构建
pnpm build:all          # 构建所有应用
pnpm build:spi-all      # 构建所有spi（4.9）应用
pnpm build:apaas-all    # 构建所有apaas + app（5.0）应用

# 代码检查
pnpm run lint           # 检查所有包语言规范

```

## Monorepo架构设计

### 工作空间结构
项目采用pnpm + Nx的Monorepo架构，支持多应用、多团队协作开发。

### 核心分层

```
yijian-fe/
├── packages/
│   ├── @com/              # 公共基础层（@yijian/*命名空间）
│   │   ├── api/           # API服务层（旧版）
│   │   ├── api-new/       # API服务层（5.0新版）
│   │   ├── components/    # 跨平台业务组件库
│   │   ├── hooks/         # 公共Hooks库
│   │   ├── hooks-new/     # 公共Hooks库（5.0新版）
│   │   ├── store/         # Redux全局状态管理
│   │   ├── constants/     # 全局常量（主要是对象常量 + 通用常量）
│   │   ├── types/         # TypeScript对象类型定义
│   │   ├── utils-new/     # 工具函数库（5.0新版）
│   │   ├── assets/        # 静态资源
│   │   ├── styles/        # 全局主题样式
│   │   ├── i18n/          # 国际化配置
│   │   ├── configure/     # 全局路由、权限点及微前端配置
│   │   ├── iflow-new/     # 流程编排引擎（5.0新版）
│   │   └── helper/        # 业务辅助函数
│   │
│   ├── spi/               # SPI核心业务层（4.x主线）
│   │   ├── app-core/              # SPI主应用
│   │   ├── iflow/                 # 流程编排引擎(for 4.x)
│   │   ├── labelset/              # 标注集管理子应用
│   │   ├── modelstore/            # 模型仓库子应用
│   │   ├── train/                 # 模型训练子应用
│   │   ├── endpointhub/           # 推理服务子应用
│   │   ├── base-admin/            # 系统管理子包
│   │   ├── base-data-pool/        # 数据湖子包
│   │   ├── base-tenant-manage/    # 租户管理子应用
│   │   ├── app-monitor-alarm/     # 监测预警应用子包
│   │   ├── app-sop/               # SOP标准作业应用子包
│   │   └── app-video-monitor/     # 视频监控应用子包
│   │
│   ├── apaas/             # 一见5.0-技能开发平台
│   │   ├── apaas-core/    # 技能开发平台主应用
│   │   ├── apaas-data/    # 数据集模块子包（新版）
│   │   ├── apaas-data-old/# 数据管理模块（旧板-后续删除废弃）
│   │   ├── apaas-model/   # 模型仓库模块子应用
│   │   ├── apaas-train/   # 训练管理模块子应用
│   │   └── apaas-skill/   # 技能管理模块子包
│   │
│   ├── app/               # 一见5.0-视觉应用平台
│   │   ├── app-core/              # 视觉应用平台主应用
│   │   ├── app-device-center/     # 设备中心子包
│   │   ├── app-monitor-alarm/     # 监测预警应用子包
│   │   ├── app-sop/               # SOP子应用子包
│   │   └── app-visual-analysis/   # 视图分析应用子包
│   │
│   ├── base/              # 基础服务层（5.0新架构）下属模块是同时给5.0 app和apaas使用的
│   │   ├── base-data-pool/        # 数据湖（新版）子包
│   │   ├── base-skill/            # 技能管理（新版）子包
│   │   └── base-tenant-manage/    # 租户管理（新版）子包
│   │
│   ├── custom/            # 客户定制化模块
│   │   ├── custom-core/   # 客户定制化主应用
│   │   ├── kangtuo/       # 康拓定制版本
│   │   ├── ruixing/       # 瑞星定制版本
│   │   └── shuyi/         # 舒逸定制版本
│   │
│   └── yijian-home/       # 一见官网应用
│
├── deploy/                # K8s部署配置
├── .comate/               # Comate智能体规则
├── .nx/                   # Nx缓存与配置
├── node_modules/          # 依赖包
├── nx.json                # Nx工作空间配置
├── pnpm-workspace.yaml    # pnpm工作空间配置
├── package.json           # 根package.json
├── tsconfig.base.json     # TypeScript基础配置
└── reskript.base.ts       # ReSKriPT基础构建配置
```

### 分层原则

**1. 公共基础层（@com）**
- **职责**: 提供跨应用的公共能力（组件、工具、类型、API封装、hooks等）
- **命名空间**: 统一使用`@yijian/*`
- **依赖方向**: @com中的包只能依赖@com中的其他包，不依赖任何业务层代码，被所有业务层依赖使用。
- **版本管理**: workspace协议（`workspace:^`）
- **其他重要说明**
  - 对于同样作用的包，例如api、api-new的这种的，后续新代码只能加到api-new中，api中现存的代码也要逐步挪到api-new中，最终废弃掉api包
  - 新功能开发不要去依赖它们old文件下的代码，这些是即将废弃的代码
  - biz文件夹说明有业务属性的，common文件夹说明是通用的，可以理解为它们的实用性更广，不局限于当前代码仓库。
  - 原则上`api`或者`api-new`中的接口请求层方法，只被`对象hooks`依赖，业务组件不应该直接去使用，业务代码中需要请求后端接口的情况下，使用`对象hooks`来实现。
  - `对象hooks`作用：通过hooks方式实现，其中主要某个对象的接口请求集合，接口返回数据保存在对象hooks中的状态，对于后端返回需要前端做format的情况，也推荐放在对象hooks供业务层复用。有些情况下通过`useEffect`在对象hooks也可以发送请求，减少业务层发送请求的逻辑。
  - 全局国际化解决方案的代码都放在`@com/i18n`文件夹中，包括国际化配置，翻译文件以及一个`useLanguage`hooks。
  - 全局状态使用zustand库在store中实现，当前例如用户权限点集合、用户信息以及全局配置是存储在全局状态中的，页面中内部的状态不建议使用全局状态管理。
  - `@com/iflow-new`是5.0新版的技能编排引擎，主要给技能开发平台技能编排功能使用的。
  - `@com/styles`中包含全局样式，以及一些主题样式和全局样式变量。
  - `@com/types`中是放置部分对象类型的，这个当前是不全的。
  - `@com/utils-new`是5.0最新的工具库，可以被整个代码仓库中应用使用，工具函数都是比较通用的方法，是不建议放置业务相关工具函数的，业务帮助函数放在 `helper`文件中实现。
  - `@com/helper`包含全局业务相关帮助函数。

**2. 业务层（spi/apaas/app/base）**
- **spi**: 一见多模态视觉管理平台（4.x版本主线）
- **apaas**: 一见5.0技能开发平台（5.0新架构）
- **app**: 一见5.0视觉应用平台（5.0新架构）
- **base**: 5.0架构的基础服务模块或子应用（跨平台复用）

**3. 定制层（custom）**
- **职责**: 满足特定客户的定制化化需求
- **架构**: custom-core是主应用，其他则是不同客户的一些子包
- **部署**: 独立部署，不影响标准版本

## 一见前端开发规范

### 命名规范

#### 包命名规范

所有内部包必须使用`@yijian/`命名空间

#### 文件命名规范

| 文件类型 | 命名规则 | 示例 |
|---------|---------|------|
| 组件文件 | PascalCase | `ProductCard/index.tsx` 或者 `ProductCard.tsx` |
| 类文件 | PascalCase | `Request/index.ts` 或者 `Request.ts` |
| Hooks文件 | camelCase，use前缀 | `useClient.ts` |
| 工具函数 | camelCase | `formatDate.ts` |
| 常量文件 | camelCase文件，里面常量是类似`UPPER_SNAKE_CASE`命名规范 | `apiConstants.ts` |
| typescript类型文件 | camelCase | `product.ts` |
| 样式文件 | 与组件同名 | `index.less` 或 `index.module.less` |
| 配置文件 | camelCase | `options.tsx` |

#### 变量规范
| 变量类型 | 命名规则 | 示例 | 补充说明 |
|---------|---------|------|------|
| 组件名 | PascalCase | 类似`ProductCard`，要求与组件文件命名一致 ||
| 方法 | camelCase | `handleSelectChange`、`doSubmit` ||
| 变量 | camelCase | `client` `project`， | 在业务代码中（不管是组件还是hooks内），尽量使用有含义的命名，不要使用『范命名』，例如`datasource`、`items`这类就是范命名，而类似`projectDatasource`、`roleList`就是有含义的命名 |
| 常量 | UPPER_SNAKE_CASE | `PROJECT_STATUS_MAP` ||
| typescript类型 | PascalCase | `Project`，注意无论是interface还是type不要前面加上`I`前缀 ||
| 类名 | PascalCase | 类似`Request`，要求与组件文件命名一致 ||

### 依赖导入顺序规范

**严格按照以下顺序组织import语句**：

```typescript
// 1. React核心库
import React, {useState, useEffect, useCallback} from 'react';
import type {FC, ReactNode} from 'react';
// 2. 第三方库
import {useTranslation} from 'react-i18next';
import * as _ from 'lodash-es';
import classNames from 'classnames';
// 3. 百度内部库（百度内部非一见团队的库 → 一见团队的库)
import {Button, Modal, Form} from 'acud';
import type {FormProps} from 'acud/es/form';
import {List, Card} from '@baidu/aibc';
import type {ListProps} from '@baidu/aibc/es/list';

// 4. 跨模块的内部包（@yijian/*）
import {useClient} from '@yijian/hooks';
import {ProductCard} from '@yijian/components';
import {getProductListApi} from '@yijian/api-new';
import type {Product} from '@yijian/types';

// 5. 本包内跨文件夹的
import {ProjectComponent} from '@/components';

// 6. 本保内本文件夹内相对路径导入
import {formatDate} from './utils';
import type {LocalProps} from './types';

// 7. 样式文件（放在最后）
import './index.less';
```

### React组件属性顺序规范

组件属性需要有一定顺序逻辑，建议样式相关放在最前面，回调事件(onXXX)相关统一都放在最后，其他一些方法函数统一放在回调上面。参考下面例子

```typescript
<DistrictCascader
    // 样式一般放在上面
    style={{width: 240, height: 32}}
    className="table-type-cascader"
    ref={cascaderRef}
    // 配置相关
    options={DISTRICT_OPTIONS}
    // 数据相关
    detail={detail}
    list={list}
    productName={productName}
    // 和这个组件本身展现相关的属性放在一起
    type="primary"
    placeholder="请选择区域"
    visible
    // 一些传递到子组件的方法
    getListData={getListData}
    // 所有onXXX都放在最后，注意这里的属性大概率都是onXXX，不是handleXXXX
    onChange={handleDistrictChange}
    onInput={handleInput}
/>
```

### React属性或者对象参数解构规范

组件属性解构建议一般属性在前，方法属性在中间，回调属性在最后，并且能加上默认值的尽可能加上，如下例子说明。

```typescript
const Component = props => {
    const {
        // 非方法属性
        productName = '',
        visible = false,
        // 方法属性
        doSumit,
        // 所有回调放在最后
        onChange,
        onInput,
    } = props;

    ...

    return null;
};
```

### 前端路由规范

**路由常量**（[packages/@com/configure/routes/](mdr:packages/@com/configure/routes/allPath.ts)）：
```typescript
export const ALL_PATH = {
    HOME: '/',                                    // 工作台
    EXPERIENCER_HOME: '/experiencer',             // 体验中心
    POWER_SKILL_COMMON: '/power/skill/common/store', // 技能管理
    MONITOR_ALARM_CAMERA: '/app/monitor/alarm/camera', // 告警管理
    // ... 其他路由
};
```
前端路由常量统一配置在`packages/@com/configure/routes/`文件夹下面，注意以下区别
- `packages/@com/configure/routes/allPath.ts`中的是spi(4.9)应用的路由常量
- `packages/@com/configure/routes/apaas/allPath.ts`中的是apaas(5.0)应用的路由常量
- `packages/@com/configure/routes/app/allPath.ts`中的是app(5.0)应用的路由常量

**路由规范**：
- 所有路由路径统一在 `@yijian/configure` 包定义
- 使用常量引用路由，禁止硬编码字符串
- 路由命名：大写下划线格式（`POWER_SKILL_COMMON`）
- 动态路由参数使用 `:paramName` 格式

### 前端最佳实践规范

**核心概念**: 对象(api/constants/hooks/types) + 业务hooks + 配置化 + 常量抽离 + 业务组件复用 + 页面级组件

重点概念说明

#### 对象(api/constants/hooks/types)

对象的概念是一见平台前端实现的基座，一个页面往往有一个或多个对象数据展现，例如技能平台空间管理详情页中有三个对象`workspace`、`workspaceRole`和`workspaceUser`。有些页面展示的是对象列表数据，有些页面则展示对象详情数据。
在新开发一个页面的时候，首先分析这个页面有几个对象，这些对象是否在当前平台中已经存在，如果不存在则需要在合适的模块创建对象的`api`、`constants`、`hooks`和`types`。

当前5.0平台`现有对象表`如下：

|平台复用性|模块|英文名|对象|
|-|-|-|-|
|apaas、 app|全局|global|globalConfiguration： 全局配置s3: s3存储|
|apaas、app|系统管理|system-admin|message: 消息log: 日志|
|apaas|空间|workspace|workspace: 空间workspaceUser: 空间下用户workspaceRole: 空间下角色|
|apaas、 app|用户|user|user：平台用户 比如getUserDetailuserAuth：用户权限相关，比如获取用户权限点列表放这个对象中|
|apaas、 app|租户|tenant|tenant: 租户function: 平台功能permission: 权限点tenantUser: 租户下用户organization: 组织role：系统角色|
|apaas、 app|订阅|subscription|subscriptionOrder:  订阅购买对象subscriptionUsage :  订阅套餐内使用情况|
|apaas、app|技能|skill|skill: 技能主对象skillGraph: 技能图skillDebug: 技能试运行skillPublication: 技能发布skillVersion: 技能版本multimodalSkill: 多模态大模型技能 （长期还有么？）|
|apaas、app|模型|model|modelStore: 模型仓库model：模型主对象modelService: 模型推理服务 （不用endpoint这个名词）modelIndicator: 模型指标modelTraining: 模型训练 （训练任务创建、列表、删除）modelPipeline: 训练产线|
|apaas、app|数据集（将来没有标注集概念了）|dataset|dataset：数据集datasetVersion: 数据集版本datasetImage: 数据集图片promptTemplate: prompt模板annotationJob :  标注任务annotationLabel ： 标注标签|
|app|设备|device-center|device： 设备集合对象deviceChannel: 设备通道deviceEventRule: 设备事件规则devicePoint: 设备点位deviceNotification: 设备通知deviceVideo: 设备视频相关对象deviceVideoRecord: 设备视频录制对象 ? |
|app|平台|platform|edgeNode: 子平台 (边缘服务器)gbPlatform： 国标平台|
|app|边缘设备|edge|edgeBox: 边缘盒子edgeBoxHardware  边缘盒子硬件|
|app|边缘版本|edge-version|edgeVersionDeployment: 边缘版本部署包edgeVersionService: 边缘版本服务edgeVersionServiceVersion: 边缘版本服务版本？|
|app|监测预警应用|monitor-alarm|alarmRecord:  预警记录alarmCollection:  预警收藏alarmArchive:  预警档案alarmRule:  预警规则alarmNotification: 预警通知alarmFilter:  预警复判alarmFilterRule：预警复判规则alarmCallback: 预警回调|
|app|SOP应用|sop|sopAlarmRecord: SOP预警记录sopRule: SOP规则sopMonitor: SOP实时监控sopStatistics: SOP统计对象sopNotification: SOP通知sopStorage: SOP存储配置|
|app|视图分析应用|visual-analysis|offlineFile: 离线文件offlineAnalysisPlan: 离线分析计划offlineAnalysisTask: 离线分析计划vaNotification: 视图分析通知|
|app|视频监控|video-monitor|...待补充|
|app|人脸|face|person 成员personTag 成员标签personGroup 成员组personRecord 人员记录|
|apaas、 app|任务中心|task-center|taskCenter：任务中心|
|apaas、 app|数据湖|data-pool|dataPool : 数据湖|
|||||

注意：上述对象集合并一定能够覆盖后续新页面的对象，但是如果对象存在了则不需要再新建了，在现有对象的`api`、`constants`、`hooks`和`types`中添加就可以了。

##### 对象api

是某个对象所有ajax请求方法的集合，如下是当前平台存在的`workspace`对象的`spi`示例：

```typescript
import {requestInterceptor} from '@yijian/utils-new/request';
import {isApp} from '@yijian/utils-new/biz/platform';

import {
    API_ORG_PREFIX,
    API_VISTUDIO_PREFIX,
    API_URL_WORKSPACE_PREFIX,
    API_URL_PLATFORM_ROLE_PREFIX,
    API_WINDMILL_PREFIX,
} from '../constants';

/**
 * 获取工作区列表
 *
 * @param params 请求参数
 * @returns 返回请求结果
 */
export const getWorkspaceListApi = params => {
    return requestInterceptor({
        apiPrefix: isApp() ? API_WINDMILL_PREFIX : API_VISTUDIO_PREFIX,
        url: `${API_URL_WORKSPACE_PREFIX}/get`,
        method: 'post',
        data: params,
    });
};

/**
 * 创建一个工作空间
 *
 * @param params 创建工作空间所需的参数
 * @returns 创建工作空间的结果
 */
export const createWorkspaceApi = params => {
    return requestInterceptor({
        apiPrefix: API_VISTUDIO_PREFIX,
        url: `${API_URL_WORKSPACE_PREFIX}/post`,
        method: 'post',
        data: params,
    });
};
```
注意：这个api文件的方法不建议直接被业务组件使用，只能被`对象hooks`使用。

##### 对象constants

`packages/@com/constants-new`是项目中最新存放对象常量的地方，其中文件夹及常量文件基本与上面`现有对象表`中是一一对应的，并且`对象constants`中只有与这个对象相关的常量，不要在其中放置页面中需要使用的常量。

下面是一个`视图分析`模块`skillPlan`对象的常量示例：

```typescript
import {StatusType} from '@baidu/aibc/es/status';

import {VSPicturePng, VSVideoPng} from '@yijian/assets/visual-analysis';
import Enum from '@yijian/utils-new/Enum';

// 分析计划状态
export const VA_SKILL_PLAN_STATUS = new Enum(
    {
        alias: 'PENDING',
        text: '未开始',
        value: 'Pending',
        status: StatusType.INACTIVE,
    },
    {
        alias: 'RUNNING',
        text: '进行中',
        value: 'Running',
        status: StatusType.PROCESSING,
    },
    {
        alias: 'COMPLETED',
        text: '已完成',
        value: 'Completed',
        status: StatusType.SUCCESS,
    },
    {
        alias: 'STOPPED',
        text: '已停止',
        value: 'Stopped',
        status: StatusType.WARNING,
    }
);

// 分析计划列表操作
export const enum VASkillActionEnum {
    DETAIL = 'detail', // 查看
    DELETE = 'del', // 删除
    JUMP = 'jump', // 跳转
}

// 分析计划任务类型
export const VA_SKILL_PLAN_TYPE = new Enum(
    {
        alias: 'IMAGE',
        text: '图片分析',
        title: '图片分析',
        value: 'Image',
        icon: <img src={VSPicturePng} width={16} />,
        description: '对离线图片进行批量分析',
    },
    {
        alias: 'VIDEO',
        text: '视频分析',
        title: '视频分析',
        value: 'Video',
        icon: <img src={VSVideoPng} width={16} />,
        description: '对离线视频和文件进行批量分析',
    }
);
```

##### 对象hooks

`对象hooks`是一见前端核心的概念，它是hooks形式实现，其中主要某个对象请求后端接口操作的方法集合、这些请求返回数据状态、对于返回数据的format操作、复用性高的数据状态格式转换，以及通过`useEffect`控制一些方法的请求发出。

业务中请求后端接口不能直接使用`对象api`中的方法，而是应该使用`对象hooks`中的方法，并且直接使用请求数据状态，在业务层面就不用重复定义请求数据的方法和状态了。新开发的`对象hooks`存放在`@com/hooks-new/object`文件夹下。

下面是设备`对象hooks`的示例

```typescript
import {useCallback, useEffect, useState} from 'react';
import {useTranslation} from 'react-i18next';
import * as _ from 'lodash-es';
import {Overflow, toast} from '@baidu/aibc';

import useGlobalStore from '@yijian/store/zustand/globalStore';
import {
    getDeviceListApi,
    addDeviceApi,
    getDeviceDetailApi,
} from '@yijian/api-new/device-center/device';
import {requestErrorToast} from '@yijian/utils-new/request';
import {downloadZip} from '@yijian/utils-new/file';
import {
    DeviceRequest,
    DeviceSummary,
    DeviceModelType,
    Device,
    DeviceKinds,
    DeviceModels,
} from '@yijian/types/device-center';

import {formatDeviceSummary, formatDeviceKindsAndModels} from './helper';

interface UseDeviceParams {
    actionText?: string; // 操作文案
    firstFetchDeviceKindsAndModels?: boolean; // 是否首次获取设备类型和型号
    firstDetailFetch?: boolean; // 是否首次获取设备详情
    firstFetchDeviceTags?: boolean; // 是否首次获取设备标签
    deviceLocalName?: string; // 设备唯一标识
}

const useDevice = (params?: UseDeviceParams) => {
    const {
        actionText = '设备',
        firstFetchDeviceKindsAndModels = false,
        firstDetailFetch = false,
        firstFetchDeviceTags = false,
        deviceLocalName,
    } = params || {};

    const {t} = useTranslation();
    const config = useGlobalStore(state => state.config);

    const [deviceDetail, setDeviceDetail] = useState<Device>({});

    // 获取设备列表
    const getDeviceList = useCallback(
        async (params?: Partial<DeviceRequest>) => {
            try {
                const res = await getDeviceListApi(params, config);
                return res?.page;
            }
            catch (e) {
                requestErrorToast(e, '', {
                    actionText: '获取',
                    name: `${actionText}列表`,
                    t,
                });
                return Promise.reject(e);
            }
        },
        [actionText, config, t]
    );

    // 创建设备
    const addDevice = useCallback(
        async (params: DeviceModelType) => {
            try {
                const res = await addDeviceApi(params, config);
                toast.success({actionText: '创建', name: actionText, t});
                return res?.result;
            }
            catch (e) {
                requestErrorToast(e, '', {
                    actionText: '创建',
                    name: actionText,
                    t,
                });
                return Promise.reject(e);
            }
        },
        [actionText, config, t]
    );


    // 获取设备详情
    const getDeviceDetail = useCallback(
        async (params: any) => {
            try {
                const res = await getDeviceDetailApi(params, config);
                const data: any = res?.result || {};
                setDeviceDetail(data);
                return data;
            }
            catch (e) {
                requestErrorToast(e, '', {
                    actionText: '获取',
                    name: `${actionText}详情`,
                    t,
                });
                return Promise.reject(e);
            }
        },
        [config, t]
    );

    // 控制详情接口发出
    useEffect(
        () => {
            if (firstDetailFetch && deviceLocalName) {
                getDeviceDetail({localName: deviceLocalName});
            }
        },
        [firstDetailFetch, deviceLocalName, getDeviceDetail]
    );

    // 设备中心设备管理对象的方法集合
    const deviceFunctions = {
        addDevice, // 创建设备
        getDeviceList, // 获取设备列表
        getDeviceDetail, // 获取设备详情
    };

    return {
        deviceDetail, // 设备详情
        ...deviceFunctions,
        deviceFunctions, // 方法合集
    };
};

export default useDevice;

```

##### 对象types

对象的typescript定义，统一存放在`packages/@com/types`文件夹下

#### 业务hooks

`业务hooks`就是用来处理业务一个独立的功能逻辑的hooks，比如项目中有的`usePurchase`就是平台中复用性很高的一个关于套餐相关的hooks，可根据套餐购买情况限制用户使用平台功能，也有未购买时跳转购买相关的逻辑等。

##### `业务hooks`与`对象hooks`的区别
`业务hooks`是处理业务逻辑的，`对象hooks`则是实现某个对象与后端接口请求相关的，它往往没有太多逻辑处理。

##### `业务hooks`的分类及放置位置

- **全局作用范围**：跨多个应用存在复用性，则放置在`package/@com/hooks-new/biz`下面
- **应用级作用范围**：在某个应用或者子模块，则放置对应应用或子模块文件夹的`hooks/biz`文件夹下，比如只作用于apaas平台的业务hooks放置在`packages/apaas/apaas-core/src/hooks/biz`文件夹下。
- **页面级作用范围**：只作用于某个页面的情况下则放置在页面组件下面的hooks文件夹下面即可，例如`packages/apaas/apaas-skill/src/pages/skillCommon/Create/useCreateSkillModal.tsx`就是用来打开创建技能弹框这个功能的业务hooks。

#### 配置化
`配置化`是业务开发功能中很重要的一部分，例如一个列表中有哪些列，这些列中分别展现什么数据。又或者是一个表单中有哪些表单项这些都是`配置化`的概念。
通常对于相对复杂的配置强烈建议都不在组件内部实现，而是在独立的`options.tsx`文件夹中实现，这样配置与组件内的实现可以解耦。
举个例子，下面是技能创建表单的配置，`packages/apaas/apaas-skill/src/pages/skillCommon/Create/options.tsx`

```typescript
import * as _ from 'lodash-es';
import {SimpleTags} from '@baidu/aibc';
import type {FormProps} from '@baidu/aibc/es/form';

import {alphanumericChineseReg} from '@yijian/utils-new/regExp';

import {SKILL_NAME_LIMIT_LENGTH} from '../constants';
import {SkillImagePreview} from './components';

export const getSkillFormItems = (params): FormProps['formItems'] => {
    const {
        tags,
        customTagRef,
        setTagCount,
        handleShowImagesForm,
    } = params;

    return [
        {
            type: 'input',
            label: '技能名称',
            name: 'displayName',
            required: true,
            extra: '仅支持数字、中文、大小写英文字母、非特殊符号，不允许空格',
            rules: [
                {pattern: alphanumericChineseReg, message: '仅支持数字、中文、大小写英文字母、非特殊符号，不允许空格'},
            ],
            componentProps: {
                autocomplete: 'off',
                placeholder: '请输入技能名称',
                limitLength: SKILL_NAME_LIMIT_LENGTH,
                forbidIfLimit: true,
            },
        },
        {
            type: 'input',
            subType: 'textarea',
            label: '技能描述',
            name: 'description',
            componentProps: {
                autocomplete: 'off',
                placeholder: '请输入技能描述',
                limitLength: 255,
                forbidIfLimit: true,
            },
        },
        {
            type: 'custom',
            label: '自定义标签',
            name: 'tagsArray',
            customComponent: (
                <SimpleTags
                    defaultValue={tags}
                    tagsRef={customTagRef}
                    maxCount={20}
                    showCount
                    onAddTag={count => {
                        setTagCount(count);
                    }}
                />
            ),
        },
        {
            type: 'custom',
            label: '技能配图',
            name: 'imageURI',
            required: true,
            customComponent: (
                <SkillImagePreview
                    onShowImageForm={handleShowImagesForm}
                />
            ),
        },
    ];
};
```

#### 常量抽离
上文有提到`对象常量`的概念，就是和对象相关的，比如某个对象status枚举与映射，某个对象ID前缀的常量等和这个对象相关的都应该放在`对象常量`文件中。
但是也有一些其他常量的存在，比如默认请求页面数据是10条，这个10就可以抽成一个全局常量`DEFUALT_PAGE_SIZE`，又或者是请求超时常量、轮询建个常量等这些就是`业务常量`的概念

##### 常量作用范围及放置位置

- **全局作用范围**：跨多个应用存在复用性，则放置在`package/@com/constants-new`下面
- **应用级作用范围**：在某个应用或者子模块，则放置对应应用或子模块文件夹的`constants`文件夹下.
- **页面级作用范围**：只作用于某个页面的情况下则放置在页面组件文件夹下的constants.tsx文件中即可。

#### 业务组件及页面级组件

##### 组件类型划分

- **基础UI组件**：acud是一见平台基础UI组件，是百度acg共建实现的
- **底层业务组件aibc**：aibc库是一见团队实现的，服务于一见平台前端通用的业务组件库，在所有应用中都有深度使用。
- **业务组件**：有一定复用性跨页面可使用的业务组件，相较于aibc复用性么有那么强，有一定业务属性，比如可复用的`组织树列表`组件在一见平台中多个页面中使用，它就是典型的一个业务组件。由于它里面实现的一见组织这个概念，所以它没有跨项目使用的复用性。
- **业务级组件**：往往是pages文件夹下的某个页面级组件。

## 业务组件库(aibc)

随着一见业务的快速发展，前端开发的需求日益增多，业务复杂度也随之提升。为了提高开发效率、降低维护成本、确保产品一致性，构建和维护一个高效的前端组件库显得尤为重要。
一见业务组件库从24年初开始建设，它是基于ACG基于组件库acud的上层实现，主要满足一见特有的一些业务场景及快速实现而持续沉淀的，覆盖90%场景的各类组件54个组件。尤其是列表、表单、弹框、上传组件、筛选组件、录入组件等组件在业务开发中发挥着巨大的价值。
aibc（V3）组件库帮助文档：https://acg-packages-v3.now.baidu-int.com/aibc/components/list

- **开发列表页规则**: `common/aibc-list.mdr`
- **开发表单页规则**: `common/aibc-form.mdr`

## 权限管理规范

**权限管理规范详见**: `biz/auth-management.mdr`

## 国际化规范

**国际化规范详见**: `common/i18n-guide.mdr`


```


这个规则是一见平台前端整体架构说明及规范，并且全局生效，**是之后所有其他规则的一个入口或者说是指导**。

## 4.4 开始使用规则创建一个页面 —— 模型版本列表页
**步骤一：创建一个空页面**

**propmt:**

帮我在apaas主应用里面创建一个新页面，放在系统管理平级位置，新页面是模型版本页，并且在新页面中加一个title叫`模型版本列表页`

[附件]
空页面创建成功了，这边5个文件修改，路由、侧边栏配置、权限点、页面级组件，大概在3分钟左右生成，符合预期：）

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
**步骤二：创建一个新对象modelVersion**

这里预期是在@com下 api-new、 constants-new 、hook-new/object 和 types文件夹下创建4个文件，主要测试大模型有没有理解对象常量、对象api、对象hooks这些概念

**prompt:**

很好，接下来创建一个新对象`modelVersion`，模型版本，注意这里要创建对象api、对象常量、对象hooks和对象types这4个文件

[附件]


此步骤总结：

1. ✅ api 、 constants、hooks、types都生成对了，并且放到了合适的位置。
2. ❌ 但是由于没有告诉它这个对象里面要有几个方法，它照着其他一个model对象把所有api都放进来了，太多了
3. ❌ 执行速度有点慢，这里它做了6分半

于是我让它去删掉代码

![](/personal-site-mvp/img/doc-placeholder.svg "")
最终只留下了一个api这个步骤是成功的！

**步骤三：在这个页面开发一个列表页**

**prompt:**

在这个页面中帮我参考场景模型列表，使用aibc中List组件创建一个列表页，这个列表页中有一个根据模型版本名称筛选功能。这个列表有2列，第一列模型版本名称，第二列操作，操作列中只有一个查看功能

[附件]
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
此步骤总结：

1. ✅ 虽然需求比较简单，但是列表页创建成功，最重要的一行代码没改直接可以跑起来，并且它完全可以理解aibc List组件使用方式。
2. ✅ 做到了配置从组件中分离，写在了独立的options文件中。

**步骤四：开发一个简单的创建表单功能**

**prompt:**

非常好，在这个页面中增加一个创建按钮，通过aibc useModal 这个hooks来打开弹窗表单，表单使用aibc库中的Form组件。当前表单有两个FormItem，第一个是模型版本名称，第二个是模型版本描述

[附件]
此步骤总结：

1. ❌ 这个创建按钮生成错误

![](/personal-site-mvp/img/doc-placeholder.svg "")
2. ❌ aibc form 多行文本框配置没有理解，配置错了，并且表单配置写在了Form组件里面，没有按照要求拆分到组件外面，导致页面长的这样

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
3. ✅  打开弹框生成了useCreateModelVersionModal 这个hooks是完全正确的。

经过手动修改最终正确

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 四 一见技能编排场景的实践
## Zulu提升技能编排开发效率背景
![](/personal-site-mvp/img/doc-placeholder.svg "")
* 技能编排组件是AI Infra的重要模块。模块本身比较庞大，内部组件数量多且逻辑复杂，每次添加新类型的算子能都需要大量排期去编码和调试。这其中有一部分重复耗时的工作，主要体现在修改画布中每一个节点的样式、功能、或者新增节点这些希望可以借助大模型能力完成大部分重复的工作
* 基于当前技能编排组件，借用网络检索能力，快速开发新功能。



## 主要场景和实现方式
### 2.1 场景一：修改技能编排组件主题样式
需求背景：常见的技能编排产品有深色和浅色2种主题。一见为浅色主题。在私有化项目交付过程中有遇到过很多次客户希望调整为深色的诉求，这种工作往往工作量比较大，以往都是手动修改。这次可以借助智能体提供的能力代替人力完成这种机械式的工作。

#### 2.1.1 实现步骤
步骤一：让zulu学习技能编排组件画布的代码，并找到代码中关于颜色的样式，提炼出变量

```
// 当前主题样式(浅色)
@graph-background-color: #F8F9FC;
@node-primary-color: #1955FA;
@node-error-color: #F33E3E;
@node-font-color: #171F2E;
@node-background-color: #FFFFFF;
@node-header-color: #151b26;
@node-tag-key-color: #171F2E;
@node-tag-value-color: #151b26;
@node-tag-background-color: #F5F7FA;
@node-tag-border-color: #E1E6F0;
@node-tag-empty-color: #7D8799;
@node-context-menu-background-color: #fff;
@node-context-menu-font-color: #151b26;
@node-context-menu-item-hover-color: #F7F7F9;
```
步骤二：让Zulu 分析每个变量对应的色值，并计算出深色样式

步骤三：在Zulu chart中输入Query如下：

将技能编排画布更新为深色主题

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2.1.2 功能清单
1. **主题变量文件** (`variables.less`)

* 将当前主题从浅色切换为深色
* 背景色: `#3d3d3d` (深灰色)
* 节点背景: `#1d1e1f` (深灰蓝)
* 字体颜色: `#f0f0f0` (浅色文本)

2. **GraphPanel组件** (`index.tsx`)

* 修改Background组件，设置深色网格点和背景
* 网格点颜色: `#666`
* 背景色: `#3d3d3d`

3. **技能编排流程样式** (`index.less`)

* 页面容器背景色: `#3d3d3d`
* 画布容器背景色: `#3d3d3d`
* 操作面板背景色: `#1d1e1f`

#### 2.1.3 效果特点
* **深色背景**：所有容器的背景都已转换为深色主题
* **节点样式**：基于ProcessingNode的音频源节点已适配深色主题
* **视觉对比**：深背景下浅色文本和节点边框提供良好的视觉对比度
* **一致性**：整个技能编排界面的主题风格保持统一

#### 2.1.4 最终效果和视频录制
![浅色主题](/personal-site-mvp/img/doc-placeholder.svg "浅色主题")
![深色主题](/personal-site-mvp/img/doc-placeholder.svg "深色主题")
[附件]


---

### 2.2 场景二：基于figma设计稿智能化生成新类型算子节点前端组件和后端mock数据
需求背景：每次添加新类型的算子能都需要大量排期去编码和调试。这其中有一部分重复耗时的工作，主要体现在修改画布中每一个节点的样式、功能、或者新增节点这些希望可以借助大模型能力完成大部分重复的工作

#### 2.2.1 实现步骤
步骤一：借助Zulu提供的figma分析能力分析组件的dom结构和样式



步骤二：和上一个场景类似，投喂Zulu关于技能编排node组件的代码，并让Zulu学习业务逻辑和组件的结构

步骤三：训练Zulu基于步骤一学习到的业务逻辑和提出的具体需求生成rules，并在后期不断验证效果和优化

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
步骤四：编辑rules.添加mock数据生成的规则和步骤

最终得到能完成本次新需求的rules,如下：

```
---
alwaysApply: false
description: 音频源节点创建规范
---

# 音频源节点规范

## 节点基本数据结构

```json
{
    "category": [
        "AudioSource:音频"
    ],
    "categoryType": "AudioSource", // 必须使用NODE_CATEGORY_TYPE中定义的类型
    "kind": "AudioSourceOperator", // 必须与OPERATORS_MAP中的键保持一致
    "categoryVisual": {
        "displayName": "音频",
        "name": "AudioSource"
    },
    "description": "提供音频输入流的源节点",
    "displayName": "音频源",
    "kind": "AudioSourceOperator",
    "kindDisplayName": "音频源",
    "localName": "AudioSourceOperator-node-{timestamp}",
    "name": "AudioSourceOperator-node-{timestamp}",
    "parentKind": "FunctionOperator",
    "version": "2",
    "visuals": "{\"position\":{\"x\":135,\"y\":285},\"modelPackageDisplayName\":\"\",\"modelPackageVersion\":\"\"}",
    "inputs": [
        {
            "defaultValue": "",
            "description": "音频输入流",
            "displayName": "输入",
            "name": "input0",
            "optional": false,
            "readonly": false,
            "schema": [
                {
                    "defaultValue": "",
                    "description": "音频输入源",
                    "displayName": "音频输入",
                    "name": "audioInput",
                    "optional": false,
                    "readonly": false,
                    "type": "Audio",
                    "value": null,
                    "valueType": "Audio",
                    "visuals": "",
                    "constraint": null
                },
                {
                    "defaultValue": "30",
                    "description": "采集音频的decibel",
                    "displayName": "分贝",
                    "name": "decibel",
                    "optional": false,
                    "readonly": false,
                    "type": "Integer",
                    "value": '30',
                    "valueType": "Integer",
                    "visuals": "",
                    "constraint": {"range":{"max":200, "min": 0}}
                },
                {
                    "defaultValue": "false",
                    "description": "是否降噪",
                    "displayName": "是否降噪",
                    "name": "isReduction",
                    "optional": false,
                    "readonly": false,
                    "type": "Boolean",
                    "value": 'false',
                    "valueType": "Boolean",
                    "visuals": "",
                    "constraint": null
                }
            ],
            "type": "Dataset",
            "value": "",
            "valueType": "Dataset",
            "visuals": ""
        }
    ],
    "outputs": [
        {
            "defaultValue": "",
            "description": "音频输出流",
            "displayName": "输出",
            "name": "output0",
            "optional": false,
            "readonly": false,
            "schema": [
                {
                    "defaultValue": "",
                    "description": "音频输出",
                    "displayName": "音频输出",
                    "name": "audioOutput",
                    "optional": false,
                    "readonly": false,
                    "type": "Audio",
                    "value": null,
                    "valueType": "Audio",
                    "visuals": ""
                }
            ],
            "type": "Dataset",
            "value": "",
            "valueType": "Dataset",
            "visuals": ""
        }
    ]
}
```

## 组件样式规范

### 样式实现规范

#### 基本要求
- 必须复制ProcessingNode样式文件的所有内容
- 仅允许进行类名替换和音频特定样式添加

#### 类名替换规则
```less
// ProcessingNode类名替换为AudioSourceNode
.iflow-processing-node → .iflow-audio-source-node
react-flow__node-ProcessingNode → react-flow__node-AudioSourceNode

// 保持所有其他样式完全一致
```

#### 验证标准
- 确保所有样式规则与ProcessingNode完全一致
- 仅允许上述3个差异化点
- 禁止修改布局、尺寸和基础样式
## 组件实现规范

### DOM结构规范
```typescript
<div className="node-content">
  {/* 输入区域 */}
  <div className="node-content-item">
    <div className='operator-title'>输入</div>
    <ParamTags params={inputs} />
  </div>
  
  {/* 新增音频采集区域 */}
  <div className="node-content-item">
    <div 
        className='operator-title' 
        style={{
            height: '60px',
            lineHeight: '18px',
        }}>
            音频采集
    </div>
    <div className='operator-content'>
      <audio controls>
        <source src="horse.mp3" type="audio/mpeg" />
        <source src="horse.ogg" type="audio/ogg" />
        您的浏览器不支持该音频格式。
      </audio>
    </div>
  </div>

  {/* 输出区域 */}
  <div className="node-content-item">
    <div className='operator-title'>输出</div>
    <ParamTags params={outputs} />
  </div>
</div>
```

### 必须包含的关键hooks
1. **useMemo hooks**（4个）：
   ```typescript
   // 1. 节点class计算
   const classSpace = useMemo(
       () => {
           const kindClass = `${kind}-operator-node`;
           const defaultClass = 'iflow-spi-node`;
           if (status?.type === 'error') {
               return classnames(prefixCls, className, defaultClass, kindClass, 'node-error node-error-ani');
           }
           return classnames(prefixCls, className, defaultClass, ifHoverayVisible ? 'node-hover' : '', kindClass);
       },
       [className, prefixCls, ifHoverayVisible, status?.type, kind]
   );

   // 2. 抠图算子判断
   const ifMattingRestoreOperator = useMemo(
       () => kind === MATTING_RESTORE_OPERATOR,
       [kind]
   );

   // 3. 输入参数处理
   const inputs = useMemo(
       () => _.get(operator, 'inputs.formItems', []) || [],
       [operator]
   );

   // 4. 输出参数处理
   const outputs = useMemo(
       () => {
           const flatTreeData = getFlattenTreeToLevel2(_.get(operator, 'outputs', []) || []);
           return _.get(flatTreeData, '0.children', []);
       },
       [operator]
   );
   ```

2. **useState**：
   ```typescript
   const [ifHoverayVisible, setIfOverlayVisible] = useState(false);
   ```

### 文件结构要求
```typescript
// 必须包含的导入
import {useMemo, useState} from 'react';
import {getFlattenTreeToLevel2} from '../../../../../utils';
import {useNodeHeaderChange} from '../../../../hooks';
```

### 验证标准
- 确保4个useMemo hooks完全一致
- 确保依赖项数组与ProcessingNode相同
- 确保状态管理逻辑一致
- **文案必须与ProcessingNode保持一致**：输入/输出标题必须使用"输入"和"输出"，不能修改为"音频输入"/"音频输出"
            const kindClass = `${kind}-operator-node`;
            const defaultClass = 'iflow-spi-node';
            if (status?.type === 'error') {
                return classnames(prefixCls, className, defaultClass, kindClass, 'node-error node-error-ani');
            }
            return classnames(prefixCls, className, defaultClass, ifHoverlayVisible ? 'node-hover' : '', kindClass);
        },
        [className, prefixCls, ifHoverlayVisible, status?.type, kind]
    );

    // 是否为抠图算子
    const ifMattingRestoreOperator = useMemo(
        () => {
            return kind === MATTING_RESTORE_OPERATOR;
        },
        [kind]
    );

    const inputs = useMemo(
        () => {
            return _.get(operator, 'inputs.formItems', []) || [];
        },
        [operator]
    );

    const outputs = useMemo(
        () => {
            const flatTreeData = getFlattenTreeToLevel2(_.get(operator, 'outputs', []) || []);
            return _.get(flatTreeData, '0.children', []);
        },
        [operator]
    );

    const {
        showContextMenu,
        handleEditNode,
        ifActive,
        headerRef,
        setIfActive,
    } = useContextMenuState(selected);

    return (
        <div className="iflow-spi-node-wrapper">
            <div className={classSpace} id={id}>
                {
                    showContextMenu && <ContextMenu node={props} handleEditNode={handleEditNode} />
                }
                <div className={`${prefixCls}-header`}>
                    <Header
                        headerRef={headerRef}
                        node={props}
                        ifActive={ifActive}
                        setIfActive={setIfActive}
                        selected={selected}
                        status={status}
                        handleValuesChange={handleValuesChange}
                    />
                </div>
                <div className="node-content">
                    <div className="node-content-item">
                        <div className='operator-title'
                            style={{
                                height: inputs.length > 0 ? '18px' : '24px',
                                lineHeight: inputs.length > 0 ? '18px' : '24px',
                            }}
                        >
                            输入
                        </div>
                        <div className='operator-content'>
                            <ParamTags
                                priorityNameField={['label', 'displayName', 'title', 'name']}
                                params={inputs}
                                emptyText={'未配置输入'}
                            />
                        </div>
                    </div>
                    <div className="node-content-item">
                        <div className='operator-title'
                            style={{
                                height: outputs.length > 0 ? '18px' : '24px',
                                lineHeight: outputs.length > 0 ? '18px' : '24px',
                            }}
                        >
                            输出
                        </div>
                        <div className='operator-content'>
                            <ParamTags
                                priorityNameField={['label', 'displayName', 'title', 'name']}
                                params={outputs}
                                emptyText={'未配置输出'}
                            />
                        </div>
                    </div>
                </div>
                {
                    (showSkillDebugStatus
                        && skillDebugStatus
                        && globalSkillDebugStatus !== GLOBAL_SKILL_DEBUG_STATUS.NotRun
                    )
                    && <SkillDebugStatus
                        globalSkillDebugStatus={globalSkillDebugStatus}
                        skillDebugStatus={skillDebugStatus}
                        nodeId={id}
                    />
                }
            </div>
            {
                _.map(handles, (handle: HandleProps, index) =>
                    (
                        <Handle
                            key={`${id}OperatorHandle_${index}`}
                            {...handle}
                            onMouseEnter={() => setIfOverlayVisible(true)}
                            onMouseLeave={() => setIfOverlayVisible(false)}
                        />
                    )
                )
            }
        </div>
    );
};

export default AudioSourceNode;

```

### 差异点实现
1. **音频特定功能**：
   - 添加音频播放控件
   - 支持音频输入/输出参数
   - 自定义节点标题颜色

2. **状态处理**：
   - 继承相同的错误状态动画
   - 保持一致的悬停/选中交互

### 验证标准
1. **结构验证**：
   - 组件tsx文件与ProcessingNode一致

2. **样式验证**：
   - 基础样式继承自ProcessingNode
   - 自定义样式不破坏原有布局

3. **功能验证**：
   - 通过所有ProcessingNode的基础测试用例
   - 添加音频特定的测试用例

### 节点注册规范
1. **导入声明**：
```typescript
import AudioSourceNode from './core/AudioSourceNode';
```

2. **类型注册**：
```typescript
const CustomNodeTypes = {
  // ...其他节点
  AudioSource: AudioSourceNode
};
```

3. **导出声明**：
```typescript
export {
  // ...其他节点
  AudioSourceNode
};
```

### 样式变量引用
使用项目定义的LESS变量：
- `@node-background-color`
- `@node-primary-color` 
- `@text-color-secondary`
- `@error-color`

## 常量配置规范

### 节点映射规则
1. **NODE_CORE_WIDGET_MAP配置**：
```typescript
// 在_constants/index.ts中添加
export const NODE_CORE_WIDGET_MAP = {
    // ...其他节点映射
    AudioSource: 'AudioSourceNode', // key为categoryVisual.name，value为组件名称
};
```

2. **OPERATORS_MAP配置**：
```typescript
// 在_constants/index.ts中添加
export const OPERATORS_MAP = {
    // ...其他算子
    AudioSourceOperator: 'AudioSourceOperator', // key和value都为节点数据的kind字段
};
```

3. **映射关系验证**：
- 确保`categoryVisual.name`与`NODE_CORE_WIDGET_MAP`的key匹配
- 确保`kind`字段与`OPERATORS_MAP`的key匹配
- 组件名称必须与实际组件文件名一致(不带扩展名)

## Mock数据生成规范

### Mock数据源位置
Mock数据文件：[operatorMockData.ts](mdr:baidu/acg-industry-fe/yijian-fe/packages/apaas/apaas-skill/src/pages/skillCommon/Arrangement/SkillArrangementFlow/operatorMockData.ts)

### Mock数据补充要求
- 在`zuluNodes.page.result[0].content.nodes`数组中补充音频源节点数据
- 数据结构必须包含完整的节点属性
- 位置坐标需与其他节点协调，建议`{"x": 330, "y": 315}`

### Mock数据示例
```typescript
{
    "category": [
        "AudioSource:音频"
    ],
    "categoryType": "AudioSource", // 必须使用NODE_CATEGORY_TYPE中定义的类型
    "kind": "AudioSourceOperator", // 必须与OPERATORS_MAP中的键保持一致
    "categoryVisual": {
        "displayName": "音频",
        "name": "AudioSource"
    },
    "description": "提供音频输入流的源节点",
    "displayName": "音频源",
    "kind": "AudioSourceOperator",
    "kindDisplayName": "音频源",
    "localName": "AudioSourceOperator-node-{timestamp}",
    "name": "AudioSourceOperator-node-{timestamp}",
    "parentKind": "FunctionOperator",
    "version": "2",
    "visuals": "{\"position\":{\"x\":135,\"y\":285},\"modelPackageDisplayName\":\"\",\"modelPackageVersion\":\"\"}",
    "inputs": [
        {
            "defaultValue": "",
            "description": "音频输入流",
            "displayName": "输入",
            "name": "input0",
            "optional": false,
            "readonly": false,
            "schema": [
                {
                    "defaultValue": "",
                    "description": "音频输入源",
                    "displayName": "音频输入",
                    "name": "audioInput",
                    "optional": false,
                    "readonly": false,
                    "type": "Audio",
                    "value": null,
                    "valueType": "Audio",
                    "visuals": "",
                    "constraint": null
                },
                {
                    "defaultValue": "30",
                    "description": "采集音频的decibel",
                    "displayName": "分贝",
                    "name": "decibel",
                    "optional": false,
                    "readonly": false,
                    "type": "Integer",
                    "value": '30',
                    "valueType": "Integer",
                    "visuals": "",
                    "constraint": {"range":{"max":200, "min": 0}}
                },
                {
                    "defaultValue": "false",
                    "description": "是否降噪",
                    "displayName": "是否降噪",
                    "name": "isReduction",
                    "optional": false,
                    "readonly": false,
                    "type": "Boolean",
                    "value": 'false',
                    "valueType": "Boolean",
                    "visuals": "",
                    "constraint": null
                }
            ],
            "type": "Dataset",
            "value": "",
            "valueType": "Dataset",
            "visuals": ""
        }
    ],
    "outputs": [
        {
            "defaultValue": "",
            "description": "音频输出流",
            "displayName": "输出",
            "name": "output0",
            "optional": false,
            "readonly": false,
            "schema": [
                {
                    "defaultValue": "",
                    "description": "音频输出",
                    "displayName": "音频输出",
                    "name": "audioOutput",
                    "optional": false,
                    "readonly": false,
                    "type": "Audio",
                    "value": null,
                    "valueType": "Audio",
                    "visuals": ""
                }
            ],
            "type": "Dataset",
            "value": "",
            "valueType": "Dataset",
            "visuals": ""
        }
    ]
}
```

## Mock数据生成规范

### 1. 文件位置
- 文件路径：`baidu/acg-industry-fe/yijian-fe/packages/apaas/apaas-skill/src/pages/skillCommon/Arrangement/SkillArrangementFlow/operatorMockData.ts`
- 插入位置：`zuluNodes.page.result[0].content.nodes`数组的开头位置
- zuzuCreateNode变量位置：文件末尾的`export const zuzuCreateNode`

### 2. 双重赋值要求
- 音频源节点数据必须同时赋值给`zuluNodes.page.result[0].content.nodes`和`zuzuCreateNode`
- 两个赋值必须保持数据结构完全一致
- `zuzuCreateNode`包含单个节点对象，而`zuluNodes`包含节点数组

### 3. 插入位置验证
- 必须插入到`nodes`数组的开头位置
- 确保与现有节点的位置不重叠(x坐标相差至少100，y坐标相差至少80)
- 示例坐标：`"x": 330, "y": 315`

### 4. 数据验证清单
| 检查项 | 要求 |
|--------|------|
| category | 必须包含"AudioSource:音频" |
| inputs | 必须包含audioInput字段 |
| outputs | 必须包含audioOutput字段 |
| position | 不能与其他节点重叠 |

### 5. 关键字段验证
| 字段 | 要求 |
|------|------|
| type | 必须为"Audio" |
| valueType | 必须为"Audio" |
| visuals | 必须包含有效的position坐标 |

### 6. 位置坐标规范
- x坐标范围：300-700
- y坐标范围：200-500
- 推荐坐标：`"x": 330, "y": 315`

## 最佳实践

1. **数据一致性**：
   - mock数据必须与节点实现完全匹配
   - 使用相同的数据类型和结构

2. **测试覆盖**：
   - 包含正常和异常音频数据用例
   - 验证输入输出参数处理

3. **版本控制**：
   - mock数据version字段与实现版本保持一致
   - 变更时同步更新mock数据

4. **可维护性**：
   - 添加清晰的注释说明
   - 使用常量代替魔法值

## 生成一类型节点的步骤
 比如当用户输入query:希望重新添加一类节点：节点类型为音频，节点名称叫音频源

 1. 步骤1：按照组件样式规范和组件实现规范生成节点组件，插入对应位置
 2. 步骤2：注册节点
 3. 步骤3：更新常量
 4. 步骤4：按照Mock数据生成规范生成这个节点的mock数据

参考实现：
- [音频源节点组件](mdr:baidu/acg-industry-fe/yijian-fe/packages/@com/iflow-new/graph-panel/components/node/core/AudioSourceNode/index.tsx)
- [音频源节点样式](mdr:baidu/acg-industry-fe/yijian-fe/packages/@com/iflow-new/graph-panel/components/node/core/AudioSourceNode/index.less)
```
步骤四：Zulu chart 中输入Query如下：

希望在技能编排组件中添加一类新的算子节点：节点类型为音频，节点名称叫音频源,样式参考选中的Figma设计稿选中模块，不同点为输入输出中间有一个音频采集模块，模块中为音频播放器。并生成音频节点的mock数据

#### 2.2.3 完整功能清单
现在音频源节点的所有规则都已完善，包括：

* ✅ 组件实现规范
* ✅ 样式规范（无行内样式）
* ✅ Mock数据生成规范
* ✅ 双重赋值要求（zuluNodes + zuzuCreateNode）

规则文件已完全符合要求，不需要在audio元素上添加任何行内样式。

#### 2.2.4 最终效果和视频录制
![生成的音频节点前端组件](/personal-site-mvp/img/doc-placeholder.svg "生成的音频节点前端组件")
![注册音频节点](/personal-site-mvp/img/doc-placeholder.svg "注册音频节点")
![生成音频节点后端mock数据](/personal-site-mvp/img/doc-placeholder.svg "生成音频节点后端mock数据")
![](/personal-site-mvp/img/doc-placeholder.svg "")
[附件]


---

### 2.3 场景三：Zulu基于现有业务逻辑优化技能编排组件
需求背景：当前技能编排画布已实现缩放、居中等功能。考虑节点过多、编排杂乱等情况，希望增加【优化布局】功能。

**Zulu提供能力：网络检索 + Chat Mode**

#### **2.3.1 提供官方demo地址，选中本地文件，提问：**
![](/personal-site-mvp/img/doc-placeholder.svg "")
> Zulu帮我完成了优化布局方法的实现，结合当前项目中变量数据和Reactflow官方示例快速实现优化布局功能。
> 引入官方推荐的Drage库，新增一个utils文件，并将计算方法提取到 utils 中，使代码更加模块化和可复用。
![](/personal-site-mvp/img/doc-placeholder.svg "")
过程视频如下：

[附件]
#### **2.3.2 此时实现90%，继续微调。**接下来进行了如下提问：
```
Chat1: 我不想要一个具体的zoom值，实际项目中节点可能超级多或者超级少，固定值不能满足所有需求，希望动态计算。
Chat2: 有个bug，点击优化布局之后，整体并未居中；再次点击才会整体居中。
Chat3: 我说错了，不是相当于可视区域整体居中，是基于reactflow画布容器整体居中
```
**完整功能清单：**

✅Dagre 树形布局：节点按清晰的层级结构自动排列

✅第一次点击即生效：使用`window.requestAnimationFrame`确保状态同步

✅精确居中：React Flow 的`fitView`自动计算准确居中位置

✅动态缩放：自动计算最佳缩放比例（最大2倍）

✅适当留白：10% 的相对留白，视觉舒适

✅完整可见：所有节点在可视区域内完整显示

✅平滑动画：300ms 过渡效果

✅代码简洁：使用官方推荐方式，易于维护

#### **2.3.3 效果展示**
![优化布局前](/personal-site-mvp/img/doc-placeholder.svg "优化布局前")
![优化布局后](/personal-site-mvp/img/doc-placeholder.svg "优化布局后")
总结：Zulu网络检索提供了多种网络搜索API，可直接喂给Zulu学习网络资料，快速生成80%的新功能开发，后续通过不断微调或者手动修改代码达到100%的目的。

# 五  总结心得
* 一个总体架构及开发规范的规则对于后续agent 产出符合规范的代码至关重要。
* 除了代码部分，如果给大模型更多输入，它生成的规则会更好更准确。
* 大模型做不了所有事情，**在写rules的时候很多也需要人工来修改**，后面基于这些rules才能发挥更大价值。
* 之后一些技术文档可以rules化，就是用markdown语法写，即可以放在如流文档库中，又可以直接在rules使用。
* **大模型对于团队内的业务组件库理解不够，需要写更多详细的配置rules来增强这块能力。或者如果comate能有学习组件库帮助文档的能力？**
* 对于团队中比较定制化的代码需要喂给大模型更多输入

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
