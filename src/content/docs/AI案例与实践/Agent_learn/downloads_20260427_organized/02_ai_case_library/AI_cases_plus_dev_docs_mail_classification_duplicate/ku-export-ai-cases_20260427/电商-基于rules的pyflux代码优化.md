---
title: "规则概述"
description: "电商-基于rules的pyflux代码优化"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\电商-基于rules的pyflux代码优化.md"
---
电商-基于rules的pyflux代码优化

#### 🧑‍🏫 案例作者：[@武靖宇](https://ku.baidu-int.com?t=mention&mt=contact&id=e1fd9860-fcec-11f0-b2c1-e928856fca0b)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了电商搜索部通过制定和实施基于rules的代码优化方案，对flux-models项目进行治理。目标包括优化模型文件结构，使其对新人友好，并做适当改造。通过生成项目结构、开发规范和配置文件管理的rules，以及进行代码删除优化、注释生成、函数修改和性能优化，显著提升了代码质量和新人上手速度，同时确保了代码的兼容性和可维护性。
# 规则概述
|**规则名称**|**基于rules的pyflux代码优化**|
|-|-|
|**治理目标**|优化模型文件，使其对新人阅读友好，并且做适当改造。|
|**解决问题**|删除一些不必要的模型内容与变量，减少阅读障碍，增加一些注释方便新人学习|
|**技术手段**|进行一些结构上的修改，将neuron gate改成senet gate，并保存裁网|

## zulu分享链接
[https://console.cloud.baidu-int.com/comatestack/share/3646](https://console.cloud.baidu-int.com/comatestack/share/3646)

## 规则生成
[附件]
“请根据该代码库结构生成rules，包含整体结构”

在这里，我希望他能帮我生成一下整体模块的结构，编写规范等，帮助新人快速上手，

他首先基于对项目结构的分析，我现在将为该项目生成规则文件。flux-models是一个百度内部的机器学习模型训练框架，具有特定的项目组织结构。

flux-models-structure.mdr和flux-model-development.mdr

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
然后创建一个专门针对配置文件的规则

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### flux-models-structure.mdr（始终应用）
* 包含整个项目的目录结构规范
* 覆盖flux框架核心模块、模型组织结构和配置工具
* 着重强调项目特定的非通用知识

#### flux-model-development.mdr（Python文件专用）
* 针对 models/**/*.py 和 flux/**/*.py 文件的开发规范
* 包含分支管理策略、submit.py标准流程、API使用规范
* 强调版本兼容性和引擎选择规则

#### flux-configuration-files.mdr（配置文件专用）
* 针对配置文件（YAML、CONF、INI、SH）的管理规则
* 详细说明conf目录的结构和使用规范
* 包含不同产品线的配置特点和安全注意事项



## 代码删除优化
[附件]
当我喂给他：

我们的调用的代码层级在models/dslive/dslive_ctcvr_pyflux_main/底下的model.py和submit.py，其中model.py中有部分变量其实没有被用到，在新人学习的过程中带来了极大的阻碍，现在想将其优化一下，只保留用到的变量

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
得出反馈：

通过分析 model.py 的代码结构，我发现有以下未使用的变量或函数：

1. **未使用的函数**：

    * `get_tag_metrics(self)` - 被注释掉的完整函数
    * `get_infer_program(self, target_vars, main_program)` - 函数定义存在但未被调用

2. **初始化变量中使用但后面未使用的变量**：

    * `self._is_infer = is_infer` - VIP测试代码中被注释掉的标签变量
    * `self.var_tags = []` - 定义但没有实际使用

3. **冗余或无用的代码段**：

    * VIP测试相关标签代码块（已注释）
    * 很多重复的变量定义或类似的注释代码

## 代码注释生成
[附件]
假如我是一位新人，我希望我可以更好地学习这个代码库，所以我喂给他

请给model.py生成一些函数的注释吧，声明每个函数的作用

![](/personal-site-mvp/img/doc-placeholder.svg "")
我已经为 model.py 文件中的主要函数添加了详细的注释说明。这些注释包括：

1. **函数功能说明**：每个函数的主要作用和目的
2. **参数说明**：详细描述每个参数的含义和用途
3. **返回值说明**：明确说明函数的返回值和类型
4. **关键实现细节**：对复杂逻辑的简要说明

主要添加注释的函数包括：

* `debug_print()` - 调试打印功能
* `build()` - 模型构建主函数
* `self_attention()`/`attention()` - 注意力机制实现
* `neuron_gate_net()` - 神经元门控网络
* `wide_net()`/`deep_net()` - 网络结构定义
* `get_cross_embedding()` - 交叉特征处理
* `_base_net()` - 基础网络结构实现

这些注释将帮助新人开发者更好地理解代码逻辑和功能，减少学习成本。注释遵循了以下原则：

1. 简洁明了，避免冗余
2. 参数和返回值说明完整
3. 关键算法有简要说明
4. 保持与代码同步更新

## 代码内层函数修改
[附件]
而现在，我接到一个新的任务，我需要对模型结构做一点修改，于是我喂给他

“模型结构里有个函数叫neuron_gate_net，这个函数我想将其改造成senet的形式，进行门控加权，请帮我改写下model.py的这个函数并修改函数名为senet_gate_net”

![](/personal-site-mvp/img/doc-placeholder.svg "")
做了如下修改：

变更包括：

1. **函数重命名**：从`neuron_gate_net`改为`senet_gate_net`
2. **实现SENet结构**：

    * Squeeze阶段：使用全局平均池化获取通道级统计信息
    * Excitation阶段：通过两个全连接层形成瓶颈结构，学习通道间依赖关系
    * Scale阶段：将学习到的权重应用到原始特征上

3. **参数调整**：

    * 新增`reduction_ratio`参数控制压缩比例(默认16)
    * 保持原有的`lr_x`学习率参数

4. **注释完善**：添加了详细的函数说明和参数说明
5. **性能优化**：

    * 使用更高效的reduce_mean代替全局池化
    * 保持与Paddle框架的兼容性
    * 参数初始化使用Xavier方法

## 5.代码修改裁网适配
[附件]
为了上线该实验，我需要在训练模型的时候保存特定的裁网变量，所以我喂给他

“submit.py中，save_params部分保留了部分目标的结构方便线上使用，由于你改造了senet，也需要在这里修改对应的保存参数使其可以运行”

![](/personal-site-mvp/img/doc-placeholder.svg "")
变更包括：

1. **新增SENet参数**：在save_params的join_params列表中新增了以下参数：

    * `"senet_gate_fc1.b_0"` - SENet第一个全连接层的偏置
    * `"senet_gate_fc1.w_0"` - SENet第一个全连接层的权重
    * `"senet_gate_fc2.b_0"` - SENet第二个全连接层的偏置
    * `"senet_gate_fc2.w_0"` - SENet第二个全连接层的权重

2. **移除旧参数**：删除了原来的`"neuron_gate_w.b_0"`和`"neuron_gate_w.w_0"`参数
3. **保持兼容性**：保留了其他所有原有参数，确保不影响现有功能
4. **格式优化**：保持原有缩进和格式风格，便于代码维护

## 规则内容示例
```
---
alwaysApply: true
description: flux-models项目结构规范指南
---

# flux-models项目结构规范指南

## 核心目录结构

flux-models项目采用严格的模块化结构，主要包含以下关键目录：

### flux框架核心模块
- **flux/** - 框架核心组件，包含训练引擎、数据读取器、运行器等
- **flux/runner/** - 不同类型的运行器（OnlineRunner、MPIOnlineRunner、OfflineRunner等），具体配置参考[flux/runner/\_\_init\_\_.py](mdr:flux/runner/__init__.py)
- **flux/table/** - 稀疏表和稠密表定义模块，用于模型参数管理

### 模型组织结构
- **models/${PRODUCT}/${MODEL}/** - 所有模型按照产品线进行分类存储
- **models/shoubai/** - 百度手百产品线模型
- **models/haokan/** - 好看产品线模型
- **models/live/** - 直播产品线模型
- **models/micro_video/** - 短视频产品线模型

### 配置和工具
- **conf/** - 配置文件目录，包含K8s、日志、特征数据库等配置
- **tools/** - 辅助工具集，包括可视化、参数转换、离线运行等

## 模型开发规范

### 标准模型文件结构
每个模型目录应该包含以下文件模式：
```text
models/product/model_name/
├── data_reader.yaml    # 数据读取器配置
├── __init__.py         # 模块标识文件
├── model.py           # 模型网络结构定义
└── submit.py          # 训练任务提交入口
```

### 框架版本管理
- 框架版本定义在[flux/versions.py](mdr:flux/versions.py)中，通过`_add_version`新增稳定版本
- 线上模型应该固定分支，保证版本稳定性

### 环境配置
支持两种开发环境：
- **Python虚拟环境** - 适合策略同学使用，配置脚本在[scripts/install_pyvenv.sh](mdr:scripts/install_pyvenv.sh)
- **Docker环境** - 适合架构同学使用，完整环境配置在[docker/README.md](mdr:docker/README.md)

## 关键依赖和兼容性

- **Python版本要求**：必须使用Python 3.9+，在[flux/__init__.py](mdr:flux/__init__.py)中明确校验
- **引擎模式**：支持Paddle引擎模式和Abacus引擎模式，通过`ABACUS_MODE`环境变量控制

## 提交任务规范

任务提交使用统一的接口模式：
- K8s任务提交：[models/shoubai/sb_union_cp/submit.py](mdr:models/shoubai/sb_union_cp/submit.py)
- MPI任务提交：支持CPU任务
- 本地测试：使用OfflineRunner进行开发测试

## 文档规范

- 模型文档存储在**docs/models/${PRODUCT}/${MODEL}.md**
- 新模型文档需要在对应产品线的**__init__.md**中引用（手百除外，使用通配符引用）
```
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
