---
title: "基础技巧"
description: "AI前端编程实用技巧"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\AI前端编程实用技巧.md"
---
AI前端编程实用技巧

#### 🧑‍🏫 案例作者：[@朱维](https://ku.baidu-int.com?t=mention&mt=contact&id=c7ad6ce0-fce4-11f0-9747-ebd4030ec41a)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了数据智能平台组朱维分享的AI辅助前端开发技巧，包括编写高质量提示词以提升AI代码生成质量，通过提供内部组件库文档解决私有组件库使用难题，以及利用AI自动化重复任务如生成API方法。还探讨了高级技巧如使用Graphiti MCP实现跨对话持久记忆，以及利用Figma MCP快速还原设计稿，提升前端开发效率和质量。
随着大语言模型（LLM）的兴起，AI辅助编程已经成为前端开发者提升效率的重要工具。本分享文档旨在介绍如何更好地利用AI进行前端开发，从编写高质量的提示词到利用高级工具解决复杂任务。

PS：主流AI IDE（comate、trae、cursor、windsurf等）的使用方式大同小异，文章中的案例基本可适用于主流编辑器，配置方式可能略有不同。

# 基础技巧
## 高质量提示词的编写：提升AI代码生成质量
在使用大模型辅助前端开发时，写出清晰、规范的提示词（Prompt）是关键。为了让模型生成的代码更加符合团队的编码规范和项目结构，我们可以通过定义一系列规则（rules）来提升输出质量与一致性。以下从**代码规范**、**项目结构**、**开发指引**三个维度，介绍如何编写高质量的提示词，以便更高效地使用 AI 助力开发。



**代码规范rules**

AI生成代码时需要遵守的编码风格，例如变量命名规范，文件命名规范，文档注释规范等。

```
# 编码规范

## 语言要求

**所有代码、注释、文档、变量名、函数名、类名、文件名以及提交信息** 必须使用英文编写。

### 代码风格

* 所有新代码必须使用 TypeScript
* 遵循一致的命名规范：

  * 使用 camelCase（小驼峰）命名变量和函数
  * 使用 PascalCase（大驼峰）命名类和组件
  * 使用 UPPER\_SNAKE\_CASE 命名常量
  * 文件名使用 camelCase
* 使用有意义且具描述性的英文命名
* 注释应使用清晰简洁的英文书写
* 遵循 ESLint 和 Prettier 的配置规范

### 文件命名

* 所有文件必须使用英文命名
* 组件文件使用 camelCase 命名（如：`userProfile.tsx`）
* 工具类文件使用 camelCase 命名（如：`apiClient.ts`）
* 文件名应具描述性，清楚表明文件用途

### 文档编写

* 所有文档必须使用英文
* README 文件应使用清晰、专业的英文书写
* 复杂逻辑部分应添加英文注释
* API 文档必须使用英文编写

### 提交信息

* 所有提交信息必须使用英文
* 遵循 [conventional commit](https://www.conventionalcommits.org) 格式：

  * `feat: 添加新功能的描述`
  * `fix: 解决具体问题的描述`
  * `chore: 更新依赖或工具配置`
  * `docs: 更新文档`
  * `refactor: 优化代码结构`

```


**项目结构rules**

用于告知AI当前项目各个文件夹的具体作用。

```
# 项目结构指南

## 概述

`console-databuilder` 是一个包含大数据应用前端代码的 monorepo（多包仓库）。

## 主要结构

```
src/                # 主应用的源代码目录  
src/api             # 应用的 API 接口调用方法  
src/components      # 应用的通用组件  
src/pages           # 应用的页面组件  
src/store           # 应用的全局状态管理  
src/styles          # 公共样式文件  
public              # 所有静态资源文件  
```
```


**开发指引rules**

用于告知AI当前项目的开发编码习惯，让AI写的代码更符合你的习惯。

可以通过good case 和 bad case来让AI学习好的编码风格。

```
# 开发指南

## 组件使用

当前项目使用 **acud 组件库** 作为 UI 组件库。开发中优先使用 acud 组件来满足需求。acud 组件库的文档位于项目根目录下的 `acud-docs.md` 文件中。

## 组件创建

新建组件时需要包含 `index.tsx` 和 `index.module.less` 两个文件，分别用于存放组件逻辑和样式。请使用一个文件夹来存放这两个文件，文件夹名称即为组件名称。

## 使用 MobX 进行状态管理

**项目中所有状态管理应使用 MobX。不要使用 React 的 `useState` 来管理复杂状态或多个组件间共享的状态。**

### Store 创建模式示例：

```typescript
// ✅ 推荐 - 使用 MobX Store 模式
export class MyStore implements Store {
  sid = 'MyStore';
  someProperty = '';
  isLoading = false;

  constructor() {
    makeAutoObservable(this);
  }

  // 动作方法
  updateProperty(value: string) {
    this.someProperty = value;
  }
}

// ❌ 不推荐 - 不要用 useState 管理复杂状态
const [complexState, setComplexState] = useState({});
```
```


可参考的优秀rules

[https://github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)

一千个代码库可能有一千种风格，需要根据自己的代码库风格定制契合度更好的rules。

## 私有组件库的AI训练：解决组件使用难题
AI模型都是基于开源代码库进行训练的，对于公司私有的组件库AI基本不知道怎么用，因此生成的代码片段就会经常出现组件使用错误，组件传参错误，需要浪费大量时间进行二次调整。

**以下提供两种思路解决该问题：**

**1.让AI参考历史代码中的组件使用方式**

这种方式有一定局限性，对于项目中没有出现过的使用方式无法很好的生成代码。

**2.为AI提供内部组件库文档**

如何为AI提供组件库文档是一个关键问题，目前很多的IDE支持添加文档类型的上下文。内部组件库的文档多以网页形式存在，如果你尝试直接将文档地址提供给AI参考，效果一般不会太好，这主要受文档网页是否包含支持大模型识别的[LLMs.txt](https://zhuanlan.zhihu.com/p/1893956842943673806)以及IDE读取网站的能力影响。

但是无论是为组件库文档添加LLMs.txt还是提升IDE的读取能力，对于普通开发者来说都不太现实。

**下面为大家带来一种“简单粗暴”的方式:**

前端组件库内多包含使用markdown文件书写的组件参数说明以及使用示例，这些内容可以很好的被大模型理解。但问题是目前IDE并不能跨项目进行上下文添加。为了解决这个问题我们可以利用**脚本**将组件库内的所有markdown文档合并在一起，生成一个完备的组件使用说明，放置在项目的特定目录供大模型使用。



文档合并的脚本示例伪代码供大家参考：

```
const fs = require('fs');
const path = require('path');

// 组件目录路径
const componentsDir = path.join(__dirname, '../components');

// 输出文件路径
const outputFile = path.join(__dirname, '../merged-docs.md');

// 获取所有组件目录
const getComponentDirs = () => {
    return fs.readdirSync(componentsDir)
        .filter(dir => {
            const stat = fs.statSync(path.join(componentsDir, dir));
            return stat.isDirectory() && dir !== '_util' && dir !== 'style' && dir !== 'locale' && !dir.startsWith('.');
        });
};

// 读取markdown文件内容
const readMarkdownFile = (filePath) => {
    try {
        return fs.readFileSync(filePath, 'utf8');
    } catch (error) {
        console.warn(`Warning: Could not read file ${filePath}`);
        return '';
    }
};

// 获取组件的demo文件内容
const getDemoContent = (componentDir) => {
    const demoDir = path.join(componentsDir, componentDir, 'demo');
    let demoContent = '';

    if (fs.existsSync(demoDir)) {
        const demoFiles = fs.readdirSync(demoDir)
            .filter(file => file.endsWith('.md'));

        demoContent = demoFiles
            .map(file => readMarkdownFile(path.join(demoDir, file)))
            .join('\n\n');
    }

    return demoContent;
};

// 获取组件的index.md内容
const getIndexContent = (componentDir) => {
    const indexPath = path.join(componentsDir, componentDir, 'index.md');
    return fs.existsSync(indexPath) ? readMarkdownFile(indexPath) : '';
};

// 主函数
const mergeDocumentation = () => {
    const componentDirs = getComponentDirs();
    let mergedContent = '';

    componentDirs.forEach(componentDir => {
        // 添加组件名称作为标题
        mergedContent += `\n\n# ${componentDir}\n\n`;

        // 先添加demo内容
        const demoContent = getDemoContent(componentDir);
        if (demoContent) {
            mergedContent += `## Demo\n\n${demoContent}\n\n`;
        }

        // 再添加index.md内容
        const indexContent = getIndexContent(componentDir);
        if (indexContent) {
            mergedContent += `## API\n\n${indexContent}\n\n`;
        }

        mergedContent += '---\n';
        console.log(`Merged documentation for ${componentDir}`);
    });

    // 写入合并后的文件
    fs.writeFileSync(outputFile, mergedContent.trim());
    console.log(`Documentation merged successfully to ${outputFile}`);
};

// 执行合并
mergeDocumentation();

```


合成好的文档需要按组件进行划分，每个组件都要包含名称，使用示例，API定义等信息。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1b50a996a61c440cb47cd04a2b7c7f02&docGuid=wfNP8Y5KSyACmA "")


然后添加下面的rules，这样就不用每次手动添加文档了。

```
## 组件使用情况
当前项目使用 [acud] 组件库作为 UI 组件库。优先使用 [acud] 组件来满足需求。[acud] 组件库的文档位于项目根目录下的 [acud-docs.md] 文件中。
```
## 自动化重复任务：以生成API方法为例
### 案例：配合iAPI平台快速生成接口定义方法
前端开发经常会需要根据接口文档来生成前端调用接口的方法函数，这个工作也是极其重复和枯燥的。用AI来处理这种工作是最合适不过的了。



#### **1.通过iAPI平台获得接口描述信息**
**这里有两种方式可供选择**

* 手动导出接口定义

特点：可批量操作，并且比较准确

* 通过iAPI MCP导出

特点：快捷方便，但有时不够准确



**手动导出具体操作**

iAPI平台提供丰富多样的导出格式，这里我们选择markdown格式即可。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aa78a4afca2845b09abb3f8248bf6b9a&docGuid=wfNP8Y5KSyACmA "")
将导出结果添加到项目内

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b28ba75a21324eea8a4efe51228ba2ae&docGuid=wfNP8Y5KSyACmA "")


**MCP具体操作**

MCP安装

安装方式参考：[https://console.cloud.baidu-int.com/comatestack/mcp/square/server/243](https://console.cloud.baidu-int.com/comatestack/mcp/square/server/243)



先获取到接口所在的iAPI项目ID，然后命令AI批量查询接口详情，这种情况会获取到项目所有的接口列表，AI再根据描述进行筛选，获取的接口可能并不完全准确。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fe2511aba90e417f9b312e27b853c99c&docGuid=wfNP8Y5KSyACmA "")
或者可以先获取指定的接口ID，让MCP根据接口ID一个一个生成，这样可以解决上面不准确的问题。

对应ID的获取方式，可以参考下图。（接口ID不用加api-）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=48a3734157744dfa9be2acb03f98d5a4&docGuid=wfNP8Y5KSyACmA "")


#### **2.制定API方法生成的rules**
这一步需要我们在项目全局添加API方法生成的rules，主要用于说明项目中API方法的规范写法。

```
# API方法生成

## 要求
- 根据提供的接口定义文档，生成接口调用方法。
- 生成到src/api文件夹内。
- 使用src/api/apiFunction.tsx中的request方法，以及urlPrefix请求路径前缀。

## 示例
```ts
import {request, BaseResponseType, urlPrefix} from './apiFunction';
interface GetComputeResourceListParams {
  workspaceId: string;
  pageNo?: number;
  pageSize?: number;
  keyword?: string;
  status?: string;
  order?: 'asc' | 'desc';
  orderBy?: string;
  // 计算实例类型
  engine?: Engine;
}

export interface ComputeResourceItem {
  workspaceId: string; // 工作空间id
  name: string; // 计算实例名字
  status: ComputeStatus;
  creator: string; // 创建者名字
  createdAt: string; // 创建时间
  computeId?: string; // 计算实例 id
  region?: string; // 地域
  runtime?: string; // 运行环境
  clusterType?: string; // 集群资源规格
  engine?: string; // 集群计算引擎
  accountId?: string; // 账户id
  updatedAt?: string; // 更新时间
  nodeCount?: number; // 节点数量
  mirrorVersion?: string; // 镜像版本
}

export interface GetComputeResourceListResult {
  computes: ComputeResourceItem[];
  total: number;
}

export function getComputeResourceList(
  params: GetComputeResourceListParams
): BaseResponseType<GetComputeResourceListResult> {
  return request({
    url: `${urlPrefix}/workspaces/${params.workspaceId}/instances`,
    method: 'GET',
    params
  });
}
```

```
#### **3.提示词示例**
最后我们需要将API声明描述作为上下文，然后命令AI开始生成。

```
根据@databuilder.md 生成一个新的接口方法定义文件，文件名instance.ts
```
# 高级技巧
## 高级记忆功能：Graphiti MCP的应用
Cursor等AI编辑器没有办法持久记住我们曾经处理过的问题，以及一些开发偏好。当完成了某些开发任务后，例如修复了某个bug，关闭IDE后，下次如果我们遇到类似bug还需要进行重复的对话描述，cursor虽然自带记忆功能，但是使用效果并不理想。这里就为大家介绍使用**Graphiti MCP**将AI编程与**Graphiti**时序感知知识图谱进行连接，实现跨对话、持久化的记忆共享。

### Graphiti简介
> Graphiti 是一个专为动态环境中运行的 AI 智能体设计的时序感知知识图谱构建与查询框架。与传统检索增强生成（RAG）方法不同，Graphiti 持续将用户交互、结构化与非结构化企业数据以及外部信息整合为可查询的连贯图谱。该框架支持增量数据更新、高效检索和精确历史查询，无需完整图谱重新计算，适合开发具有交互性和上下文感知能力的 AI 应用。
### Graphiti MCP应用场景
* 跨对话持久记忆
* 记住出现过的bug
* 追踪项目需求演进
* 记住模块重构原因
* 团队之间的知识共享

### 使用前配置
* 下载neo4j客户端（用于存储知识数据）
* 下载Graphiti MCP代码
* 在IDE中配置Graphiti MCP
* IDE中添加Graphiti MCP调用的相关rules

详细的配置步骤：[Graphiti MCP配置方法](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/pX9p9dcNOc/Vg_n2GxdrJnjIh?source=137?t=mention&mt=doc&dt=doc)

### 使用案例
#### 案例一：保存项目基础信息
命令AI分析当前项目并保存至记忆，此时AI会对项目基础信息进行检索总结。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=df8871aa308645f3b6360595b88c3543&docGuid=wfNP8Y5KSyACmA "")
完成基础信息收集后，AI会调用Graphiti MCP的add_memory方法将信息保存到neo4j数据库中。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6355e419eed24dabad54b04905e376a0&docGuid=wfNP8Y5KSyACmA "")
我们打开neo4j客户端后可以清楚的看到项目详情记录。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=68c041673e494e3fa62176d6a3762238&docGuid=wfNP8Y5KSyACmA "")
我们重新打开编辑器后，再次询问关于项目的介绍，并且让AI**优先使用记忆**，此时AI就不会再重复进行项目库检索了，而是通过Graphiti MCP直接调用之前保存的记忆。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2c682d085d844628afcbb5225514e0bb&docGuid=wfNP8Y5KSyACmA "")
#### 案例二：记录历史需求、BUG等
下面让AI开发一个小需求，具体为：把”导入新文案“按钮的颜色调整为红色，并且文字显示调整为从右向左。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0b9f71a9caa145eaab053b0de8a6084f&docGuid=wfNP8Y5KSyACmA "")
AI先进行了记忆检索，确认没有相关历史后，然后对功能进行了实现，并将实现过程记录到了数据库中。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ad9501339f044a16aa50e701cb7a6d95&docGuid=wfNP8Y5KSyACmA "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6cd5e320fc5e4a04a1a06a8a8c170c8c&docGuid=wfNP8Y5KSyACmA "")
AI只实现了按钮颜色改变，但是没有成功调整文字方向，我们继续让AI修复这个bug，并将修复过程保存到记忆中。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5c0e36b84383434d879455fd3ee17ed6&docGuid=wfNP8Y5KSyACmA "")
然后我们关闭当前对话窗口，提一个相似的需求，让AI调整另一个按钮的文字方向，AI犯了第一次相同的错误，此时我们让他看看历史上有没有相似的问题修复，AI进行了数据库检索，并成功搜索到了历史问题修复方案，学习方案后成功完成了问题修复。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6d6a794e314c4e1c867e153079e32bb3&docGuid=wfNP8Y5KSyACmA "")
## UI一键还原：Figma MCP的使用
还原设计师UI稿是前端工程师日常重要的日常工作内容，下面介绍如何使用AI+Figma MCP快速还原设计稿。

### 使用案例
首先需要为AI客户端配置好Figma MCP，然后在Figma中拷贝需要生成的设计元素链接。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c1c14ed8c1f847189271d204dba05157&docGuid=wfNP8Y5KSyACmA "")
将链接拷贝到AI客户端，命令AI进行设计稿的还原

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=83d3102ec1da433e8207c0b5518813a9&docGuid=wfNP8Y5KSyACmA "")
生成结果虽然存在一些问题，但是只需要一些简单调整就可以使用了。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=40caffc3620e4483af5a39b511700736&docGuid=wfNP8Y5KSyACmA "")
## 复杂任务分解：Serena MCP的实战
我们使用AI编码的过程中，是否有这样的体验——开发简单的功能效果还不错，但是遇到复杂功能时效果总是差强人意。Serena MCP可以从一定程度上提升复杂任务的完成质量。

### Serena简介
Serena 是一款功能强大的**编码代理工具包，** 能够将 LLM 转变为可**直接在你的代码库上**运行的功能齐全的代理。Serena 提供了类似于 IDE 功能的基本**语义代码检索和编辑工具 **，可以在符号级别提取代码实体并利用关系结构。与现有的编码代理结合使用时，这些工具可以显著提高（token）效率。

以下是Serena MCP工具集具备的主要能力：

```
graph TD
    A[Serena MCP 工具集] --> B[文件操作]
    A --> C[代码分析与编辑]
    A --> D[记忆管理]
    A --> E[系统与项目管理]
    A --> F[AI思考分析]

    B --> B1["文件读写、查找、替换"]
    C --> C1["代码搜索、符号查找、代码编辑"]
    D --> D1["项目知识存储与检索"]
    E --> E1["命令执行、项目配置、模式切换"]
    F --> F1["反思决策、任务评估"]

    classDef fileOps fill:#e1f5fe
    classDef codeWork fill:#f3e5f5
    classDef memory fill:#fff3e0
    classDef system fill:#e0f2f1
    classDef thinking fill:#f1f8e9

    class B,B1 fileOps
    class C,C1 codeWork
    class D,D1 memory
    class E,E1 system
    class F,F1 thinking
```
### 使用案例
### 为项目快速搭建一个注册登录系统
下面这个项目是一个i18n国际化语料管理工具，下面我们让Serena在项目基础上增加一个注册登录系统。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ce43566a527748f4b52832ef301eb960&docGuid=wfNP8Y5KSyACmA "")
首先让Serena执行项目入门设置，此过程Serena会全面收集项目信息，并保存到项目中的.serena文件夹中。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0716fcb71e8a4758bfd6a99086092114&docGuid=wfNP8Y5KSyACmA "")
然后提出需求，重点是要求Serena先使用plane模式进行规划。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0567247f6c864f25824bd4806f6af835&docGuid=wfNP8Y5KSyACmA "")
规划完成后，会在memories中生成完整的需求规划文档。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=660b664a6aea4f95b4c79c2bcfd5fdce&docGuid=wfNP8Y5KSyACmA "")
之后我们只需要让AI按照需求规划一步一步实现即可，最后得到的效果也比单独使用AI编码的效果要好很多，并且开发过程中几乎没有进行人工干预。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fbb175368f8947db822c6eee2850f579&docGuid=wfNP8Y5KSyACmA "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1c7f3ee8f1af4bc8ad35623e12dbb7bf&docGuid=wfNP8Y5KSyACmA "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
