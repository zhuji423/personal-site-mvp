---
title: "使用体验"
description: "Spec驱动的开发流程体验"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Spec驱动的开发流程体验.md"
---
Spec驱动的开发流程体验

#### 🧑‍🏫 案例作者：[@高赛](https://ku.baidu-int.com?t=mention&mt=contact&id=a5b58950-fcea-11f0-a437-7f5bc90a1cdd)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了Spec驱动开发流程的实战体验，通过明确需求、系统设计、任务拆解与自动化执行，实现了从需求到代码的高效转化。该流程提升了代码质量与一致性，减少了返工，并促进了文档的沉淀与版本管理，尽管在快速探索阶段可能显得繁重，但为长期维护与团队协作提供了坚实基础。
# 使用体验
说明：使用spec-kit

Spec 驱动开发的本质是“先明确契约，再做开发”，它为稳定性、协作和长期维护提供巨大价值，但在快速探索或需求不明确时，可能会显得笨重。

#### 🟩 优点
**💠 提升代码质量与一致性**

* 通过“项目宪法”和结构化模板约束模型行为，遵循最佳实践，减少随意性

**💠 明确需求，减少返工**

* 强制在编码前厘清“做什么”和“为什么”，减少因需求模糊导致的后期修改。
* 将开发重心从琢磨“提示词”转移到严谨的需求分析和技术设计上，过程更可控

**💠 文档可沉淀、可版本管理**

* 文档（specs）作为“单一事实来源”，为后续维护、团队沟通提供完整上下文，有利于长期维护、重构与回归验证。

---

#### 🟥 缺点
**⛔ 流程较繁重，前期成本高，速度慢**
编写详细的规格文档本身耗时，尤其对于小型项目或简单修改，可能显得“杀鸡用牛刀“。

**⛔ 文档维护成本高，可能滞后实现**
一旦需求频繁变化，spec 可能会成为负担，需要不断修改文档，文档可能变得滞后。

# SDD开发流程实战
## 任务背景
评测rerank模型在beir公开数据集上的表现，评测指标使用ndcg@10。评测流程如下：

* 下载beir评测数据集并解析
* 使用faiss对数据集进行向量化索引
* 进行faiss检索，保留top100检索结果，评测ndcg@10
* 在top100检索结果基础上进行rerank，评测ndcg@10

其中retrieval和rerank通过api进行访问，不需要本地启动模型。

## 一、第一步：需求定义（The Specify Phase）
通过 /speckit.specify 指令输入原始需求。输入比较非常粗糙，仅仅描述了核心逻辑：

> /speckit.specify 评测rerank模型在beir公开数据集上的表现，评测指标使用ndcg@10。评测流程如下：
> * 下载beir评测数据集并解析
> * 使用faiss对数据集进行向量化索引
> * 进行faiss检索，保留top100检索结果，评测ndcg@10
> * 在top100检索结果基础上进行rerank，评测ndcg@10
> * 其中retrieval和rerank通过api进行访问，不需要本地启动模型。
> 
##### 1. “产品经理”思维
Spec-Kit 并没有直接扔出一堆代码，而是立刻切换到了“产品经理”模式。它完成了如下的操作：

* **自动化 Git 管理**：自动识别需求关键词，创建了标准化的分支 001-evaluate-beir-rerank
* **结构化拆解**：将简单的5 行文字，扩充成了一份完整的功能规格书 (Spec)。

##### 2. 产出物分析
* **用户故事 (User Stories) 与优先级**：AI 自动将任务拆解为 P1/P2/P3 三个阶段。
    * P1 数据准备：它敏锐地指出“没有可靠的数据准备就无法继续”，并定义了“缓存复用”的场景。
    * P2 基线检索：定义了不依赖 Rerank 的独立测试路径。
    * P3 Rerank 对比：明确了最终的业务价值是“对比提升”。


      这种拆分符合敏捷开发的 MVP 思维，保证了每一步都是可独立验收的。

* **边界情况 (Edge Cases)**：
    * “数据集下载中断怎么办？” -> 系统需支持断点续传/重试。
    * “API 挂了怎么办？” -> 需要熔断策略。
    * “Top100 里没有相关文档怎么办？” -> 评测计算需回退处理。


      以往这些通常是agent写完代码时踩坑了才发现的问题，在spec模式下模型在设计阶段就指出来了问题，边界情况考虑的很完善。

* **可量化的成功标准 (Success Criteria)**：AI 将模糊的目标变成了数字：
    * “100% 数据集在 30分钟内完成下载”
    * “缺失查询比例 <1%”

* **质量自检 (Validation)**： 生成了一份 checklists/requirements.md 并进行了自检。它核对了“是否有含糊不清的需求”、“是否依赖具体技术栈（如指定用 Flask 还是 FastAPI，Spec 阶段应避免）”。结果是 **All Pass**。



## 二、架构蓝图 (The Plan Phase)
在这一步，提供具体的技术栈偏好和外部依赖信息。输入包含非常具体的约束：

> /speckit.plan 使用python3.12进行开发，使用uv工具管理python包并创建相应的虚拟环境；遵守python PEP8编码规范；
> 检索api如下：
> curl --location '[http://10.45.136.17:8345/embeddings](http://10.45.136.17:8345/embeddings)' \
> --header 'Content-Type: application/json' \
> --data '{
> }'
> 返回结果格式如下：
> {"embeddings":[[xxxx], [xxxxx]]}
> 
> rerank模型的api如下：
> curl --location '10.27.143.110:8866/api/v1/relevance' --header 'Content-Type: application/json' --data '{
> "query": "ConvertTo converts this GCPClusterList to the Hub version (v1beta1).",
> "documents": [
> "func (src *GCPClusterList) ConvertTo(dstRaw conversion.Hub) error { // nolint\n\tdst := dstRaw.(*v1beta1.GCPClusterList)\n\treturn Convert_v1alpha3_GCPClusterList_To_v1beta1_GCPClusterList(src, dst, nil)\n}"
> ]
> }'
> 返回结果如下：
> {
> "scores": [
> 1.0
> ]
> }
> 注意：检索api和rerank的api需在配置文件中指定
任务发送之后，spec-kit开始执行plan workflow，进行了一次完整的系统设计，概括如下：

##### 精准的技术选型与环境感知
在 specs/001-evaluate-beir-rerank/plan.md 中完成总体方案，明确以 Python 3.12 + uv 构建 agent-cli CLI，远程检索/重排 API 通过配置驱动，并约束文档、测试目录及性能目标，宪章缺失已按阶段两次 Gate 复检均为 PASS。自动推导出了核心依赖库——typer(用于 CLI)、pydantic(用于数据校验)、httpx(用于高性能 HTTP 请求)、beir(数据集处理)、faiss-cpu(向量索引)。

##### 专业的项目结构设计
采用模块化设计，将配置、API 客户端、核心流水线分离开来。

```
agent-cli/
├── pyproject.toml            # uv 管理的 project 元数据
├── uv.lock                   # 依赖锁
├── README.md                 # 指向 docs 与 quickstart
├── docs/
│   ├── architecture.md
│   └── api-config.md         # 记录检索/rerank 配置示例
├── config/
│   ├── settings.example.toml # 包含 API 地址、token、批量大小、数据集清单
│   └── datasets.yaml
├── data/
│   ├── raw/                  # 原始 BEIR 压缩包
│   ├── cache/                # 解析后的 corpora/queries/qrels
│   ├── indexes/              # FAISS 索引与元数据
│   └── rerank/               # Top100 与 rerank 结果
├── src/agent_cli/
│   ├── __init__.py
│   ├── cli.py                # Typer CLI 入口
│   ├── config_loader.py      # 读取/校验配置（pydantic models）
│   ├── datasets/beir_loader.py
│   ├── embeddings/api_client.py
│   ├── rerank/api_client.py
│   ├── pipelines/
│   │   ├── prepare_dataset.py
│   │   ├── build_index.py
│   │   ├── run_retrieval.py
│   │   └── run_rerank.py
│   ├── metrics/ndcg.py
│   ├── storage/faiss_store.py
│   └── reporting/report_builder.py
├── docs/                     # (同上，满足“文档位于 agent-cli/docs”要求)
└── tests/
    ├── test_config.py
    ├── test_metrics.py
    ├── test_pipeline_prepare.py
    └── resources/
```
##### 解决“未知” 
在research.md中，围绕数据源、FAISS 类型、HTTP 客户端、配置格式、ndcg@10 计算等关键不确定性给出决策、原因与备选。比如：

* **决策**：使用beir官方工具链。
* **原因**：官方库提供了最稳定的数据加载方式，避免重复造轮子。
* **决策**：使用pydantic管理配置。
* **原因**：因为用户提供了具体的 API JSON 格式，强类型校验能避免运行时错误。

##### 定义数据契约
根据提供的curl命令，反向生成了contracts/evaluations.openapi.yaml和data-model.md。它定义了系统内部如何存储“索引任务”、“检索运行结果”和“Rerank 结果”。这意味着后续生成的代码将严格遵守这些数据结构，不会出现字段乱飞的情况。

##### 阶段总结
通过/speckit.plan，本阶段共产出6个文档，可以得到了一份详尽的**实施计划 (Implementation Plan)**

* **核心价值**：本阶段给人的感受就是它不仅仅是在写代码，它是在**设计系统, **从简单的用户输入触发以此为基础构建了整个项目的骨架。
* 另，本阶段一共生成了6篇文档，需要一个个文档进行check，阅读成本较高。

```
specs/001-evaluate-beir-rerank/plan.md
specs/001-evaluate-beir-rerank/research.md
specs/001-evaluate-beir-rerank/data-model.md
specs/001-evaluate-beir-rerank/contracts/evaluations.openapi.yaml
specs/001-evaluate-beir-rerank/quickstart.md
.cursor/rules/specify-rules.mdc（由 agent-context 更新脚本生成/刷新）
```


## 第三步：任务拆解 (The Tasks Phase)
输入 /speckit.tasks 后，spec-kit 并没有简单列出 "To-Do List"，而是生成了一份**分阶段的任务实施路径**。执行过程概括如下：

##### 1. 阶段化执行 
tasks.md 内容组织概括如下：

* **Phase 1: Setup（基础设施）**
    * 任务：初始化 uv 环境，建立目录结构。

* **Phase 2: Foundational（核心库）**
    * 任务：实现配置加载器、API 客户端封装、日志系统。

* **Phase 3/4/5: User Stories (P1/P2/P3)**
    * 任务：分别对应最早在 Spec 中定义的优先级：数据准备->检索->rerank


##### 2. 任务颗粒度
task.md中定义了非常合适的任务颗粒度，比如：

> **T012 [P] 实现 ****src/agent_cli/datasets/beir_loader.py**
> * 封装 BEIR 下载、缓存、校验逻辑
> * 支持断点续传
> * 编写 tests/test_pipeline_prepare.py::TestBeirLoader
> 
它包含了：

1. **功能边界**（下载+缓存+校验）
2. **非功能需求**（断点续传）
3. **验收标准**（对应的测试用例）

这种颗粒度刚刚好，既不会太细碎（比如“定义变量 x”），也不会太宏大（比如“完成数据模块”），任务也很明确。

##### 3. 测试驱动 (Test-Driven)
几乎每个核心任务都伴随着测试要求：

* T011 -> tests/test_config.py
* T013 -> tests/test_api_clients.py
* T201 -> tests/test_metrics.py

##### 阶段总结
拿到这份 tasks.md，会感受到一种“掌控感”，spec罗列了详细和清晰的任务todo，相比传统的与agent的交互在感受上会觉得更加可控。



## 第四步：任务执行（The Implementation Phase）
输入 /speckit.implement，它会严格按照task.md中的的规划执行代码编写任务。执行过程概括如下（未展示完整的任务执行过程）：

##### 检查
在开始写代码前，Spec-Kit 会自动检查在 Spec 阶段生成的质量清单。如果需求定义不清晰，它会拒绝执行。

##### 基础设施先行
* 构建环境：首先生成了pyproject.toml，并精准地写入了在 Plan 阶段要求的uv配置和依赖列表（faiss-cpu,beir,typer等）。
* 配置管理：接着实现了config_loader.py，使用了pydantic来定义数据模型（EmbeddingConfig,RerankConfig）。
* 校验：它自动添加了校验逻辑，例如batch_size必须是正整数。这不是我显式告诉它的，而是它根据“工程常识”补全的。
* 网络层封装：实现了重试机制（此前在Spec 的Edge Cases里提到了“API 出现超时需重试”）

通过构建良好的基础设施，为项目打造了一个结构标准、配置健壮、网络可靠、测试覆盖的项目地基，会让后续业务逻辑开发变得更加轻松。

##### 测试与代码同行
在生成功能代码的同时，AI 同步生成了测试文件：

* src/agent_cli/config_loader.py对应生成了tests/test_config.py
* datasets/beir_loader.py对应生成了tests/test_pipeline_prepare.py

##### 任务追踪
明确已完成任务，并在tasks.md中标记为完成态。其次更新下一阶段的todo

##### 明确代办与风险
* 配置校验范围：config/datasets.yaml 中的 expected_* 数值为公开资料估算，若与实际 BEIR 数据略有出入，可在运行前按需调整。
* 数据目录 ignore：后续完成 T405 时需在 agent-cli/data/ 下新增专用 .gitignore，避免缓存被提交。
* 下一步建议：继续 Phase3（T101-T105）实现数据准备流水线，随后推进检索与 rerank 逻辑，并在具备写权限的环境中重新执行 uv lock、uv sync 与测试。



##### 阶段总结
agent按照tasks.md按部就班执行任务，并阶段性完成部分任务，非一蹴而就。完成任务后还带有反思，列出当前任务执行后还存在的风险，并明确下一步任务。这个阶段就像一个J人在写代码，非常有秩序感，也能增加用户对其写作代码完成任务的信任感。



后续通过多次执行implement以及与模型的多次交互，模型成功完成了完整的任务。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转

