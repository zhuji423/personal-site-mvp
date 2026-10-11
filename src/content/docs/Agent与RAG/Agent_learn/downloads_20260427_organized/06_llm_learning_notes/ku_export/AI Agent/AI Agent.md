---
title: "AI Agent"
description: "2024.06| 标题 | 发布日期 | 链接 | 机构 | 摘要 | | --- | --- | --- | --- | --- | | CodeR: Issue Resolving with Multi-Agent and Task G"
date: "2026-04-27"
category: "Agent与RAG"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\AI Agent\\AI Agent.md"
---
# AI Agent
1、背景介绍、综述综述论文【代码大模型综述】https://arxiv.org/pdf/2311.07989AIAgent产品平台（适合简单场景）产品调研：coze：appbuilder：其他相关检索增强评测基准SWE-Bench3、最新代码大模型论文整理2024.07| 标题 | 发布日期 | 链接 | 机构 | 摘要 |
| --- | --- | --- | --- | --- |
| Qwen2: Qwen2 Technical Report | 2024-07-15 | https://arxiv.org/abs/2407.10671 | Alibaba Group | 本文介绍了 Qwen2 系列开源大模型和多模态模型，涵盖了从 0.5B 到 72B 参数的模型，以及密集模型和混合专家模型。Qwen2 在语言理解、生成、多语言能力、编码、数学和推理等方面超越了大多数先前的开源模型，并在各种基准测试中展现出与闭源模型相媲美的性能：基座模型 MMLU 84.2，GPQA 37.9，HumanEval 64.6，GSM8K 89.5，BBH 82.4；微调模型 MT-Bench 9.1，Arena-Hard 48.1，LiveCodeBench 35.7。 |
| AFM: Apple Intelligence Foundation Language Models | 2024-07-29 | https://arxiv.org/abs/2407.21075 | Apple | 本文介绍了苹果公司为其智能功能开发的基座大模型 AFM，包括一款针对设备高效运行而设计的 3B 参数模型（AFM-on-device）和一款针对私有云计算而设计的更大规模服务器模型（AFM-server），两者都经历了 6.3T tokens 的预训练、1T tokens 的代码与数学加训以及额外 100B tokens 的长上下文训练。这些模型旨在以高效、准确和负责任的方式执行各种任务。论文详细阐述了模型架构、训练数据、训练过程、模型推理优化以及评估结果，并重点介绍了苹果公司对负责任人工智能的关注以及相关原则在模型开发中的应用。 |
| Llama 3.1: The Llama 3 Herd of Models | 2024-07-31 | https://arxiv.org/abs/2407.21783 | Llama Team, AI @ Meta | 本文介绍了 Llama 家族的最新模型 Llama 3.1 系列，在今年四月发布的 Llama 3 基础上增加了对多语言、工具调用、128K 长上下文的支持，同时也在 8B 与 70B 之外发布了一个 405B 的新模型。实验表明 Llama 3 在多项任务上的表现可与 GPT-4 等领先模型相媲美。论文还发布了用于输入输出安全的 Llama Guard 3 以及将图像、语音、视频等多模态功能整合到 Llama 3 中的实验结果。 |
| Code Less, Align More: Efficient LLM Fine-tuning for Code Generation with Data Pruning | 2024-07-06 | https://arxiv.org/abs/2407.05040 | NVIDIA | 本文探讨了针对代码大模型的数据剪枝方法。研究者提出了结合多种聚类和剪枝指标的技术，来有选择地减少训练数据，同时不影响生成代码的准确性和功能性。实验表明，合成训练数据中存在显著的冗余，仅使用 10% 的数据进行训练就能在很大程度上保持基准性能。更有趣的是，适度精简训练数据还能持续改善基准结果。这些剪枝策略不仅降低了所需的计算资源，还提高了整体代码生成质量。该研究为提高代码大模型的训练效率提供了新的思路，对于优化模型训练过程和提升代码生成质量具有重要意义。 |
| CoIR: A Comprehensive Benchmark for Code Information Retrieval Models | 2024-07-03 | https://arxiv.org/abs/2407.02883 | Huawei Noah’S Ark Lab | 本文提出了一个名为 CoIR 的代码信息检索基准，它包含十个精心收集的代码数据集，涵盖了七个不同领域的八个检索任务，旨在为代码检索系统的评估提供一个全面而鲁棒的工具。该基准通过提供一个用户友好的 Python 框架，以及与其他流行基准（如 MTEB 和 BEIR）相同的架构，简化了代码检索研究工作流程。研究者通过使用该基准评估了九个常用的检索模型，并发现即使是当前最先进的系统在执行代码检索任务方面也面临着巨大挑战，从而激发了代码检索领域的研究，并为进一步开发和探索更强大的代码检索系统提供了有力支撑。 |

2024.06| 标题 | 发布日期 | 链接 | 机构 | 摘要 |
| --- | --- | --- | --- | --- |
| CodeR: Issue Resolving with Multi-Agent and Task Graphs | 2024-06-03 | https://arxiv.org/abs/2406.01304 | Huawei | 本文提出了一个名为 CodeR 的多智能体框架，用于自动修复和解决代码仓库中报告的错误，以及添加新功能。CodeR 采用预定义的任务图来指导修复过程。在 SWE-bench lite 数据集上，CodeR 仅提交一次就能解决 28.33% 的问题。论文还分析了 CodeR 各项设计对性能的影响，为该研究方向的进一步发展提供了见解。CodeR 的提出有望提高软件开发和维护的效率。 |
| DataComp-LM: In search of the next generation of training sets for language models | 2024-06-17 | https://arxiv.org/abs/2406.11794 | University of Washington, Apple | 本文提出了一个用于语言模型受控数据集实验的测试平台 DCLM。作者提供了一个从 Common Crawl 中提取的 240T tokens 的标准语料库，有效的预训练方法以及广泛的 53 个下游评估任务。通过在 DCLM 上进行的大量实验，作者发现基于模型的过滤对于构建高质量的训练集至关重要。由此产生的数据集 DCLM-Baseline 能够使用 2.6T 训练 tokens 将一个 7B 参数的语言模型从头训练到 MMLU 上的 64% 的 5-shot 准确率，与之前最先进的开放数据语言模型 MAP-Neo 相比，在计算量减少 40% 的情况下，MMLU 上的性能提高了 6.6 个百分点。该基线模型在 MMLU 上的表现与 Mistral-7B-v0.3 和 Llama-3 8B 相当，在 53 个自然语言理解任务上的平均表现也与 Llama-3 8B 相似，但训练所需的计算量却减少了 6.6 倍。这些结果突出了数据集设计对语言模型训练的重要性，为进一步研究数据策展提供了一个起点。 |
| DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence | 2024-06-17 | https://arxiv.org/abs/2406.11931 | DeepSeek-AI | DeepSeek-Coder-V2 是基于 DeepSeek-V2 4T tokens 检查点做了 6T tokens 加训获得的模型，显著提高了代码和数学推理能力，同时在一般语言任务上保持相当的性能。与之前的版本相比，DeepSeek-Coder-V2 在代码相关任务、推理和通用能力方面都有重大进展，支持的编程语言从86 种扩展到 338 种，上下文长度从 16K 扩展到 128K。在标准基准测试中，DeepSeek-Coder-V2 在代码和数学基准测试方面优于 GPT4-Turbo、Claude 3 Opus 和 Gemini 1.5 Pro 等闭源模型。 |
| Long Code Arena: a Set of Benchmarks for Long-Context Code Models | 2024-06-17 | https://arxiv.org/abs/2406.11612 | JetBrains Research | 本文针对现有的代码处理基准数据集规模有限的问题，提出了一个名为 Long Code Arena 的大型代码处理基准套件，包含六个需要项目级上下文的代码处理任务。这些任务涵盖了代码生成的各种方面，例如基于库的代码生成、CI构建修复、项目级代码补全、提交信息生成、错误定位以及模块摘要等。论文为每个任务提供了经过人工验证的测试数据集、评估套件以及基于流行大语言模型的开源基线解决方案，方便其他研究人员使用和学习。 |
| ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools | 2024-06-18 | https://arxiv.org/abs/2406.12793 | Zhipu AI, Tsinghua University | 本文回顾了 ChatGLM 家族的发展历史与最新进展，并重点介绍了 GLM-4 模型，开源了 GLM-4 9B。这些模型在大规模中英文语料上进行预训练，并通过监督微调和人类反馈学习等多阶段后训练过程实现了高质量的对齐。实验结果表明，GLM-4 在通用评测、指令遵循、长文本任务和中文对齐等方面表现出色，与 GPT-4 和 Claude 等先进模型相当甚至超越。此外，论文还介绍了 GLM-4 All Tools 模型，它能够理解用户意图并自主决定使用各种工具来完成复杂任务。 |
| LiveBench: A Challenging, Contamination-Free LLM Benchmark | 2024-06-27 | https://arxiv.org/abs/2406.19314 | Abacus.AI | 本文提出了一个名为 LiveBench 的新型基准测试，旨在克服现有基准测试中存在的测试集污染和人工评估/LLM评估问题。LiveBench 通过引入从最近信息来源（如数学竞赛、arXiv论文、新闻文章和数据集）提取的实时问题，并利用客观地面真实值自动评估答案，来构建一个不易受污染且难度更大的基准测试，从而更准确地衡量大模型的能力。 |

2024.05| 标题 | 发布日期 | 链接 | 机构 | 摘要 |
| --- | --- | --- | --- | --- |
| Text-to-ML: Large Language Models Synergize with Automated Machine Learning | 2024-05-06 | https://arxiv.org/abs/2405.03727 | University of Tokyo | 本文提出了一种新颖的机器学习程序合成方法，称为 Text-to-ML。该方法结合了大语言模型和自动机器学习技术，可以根据机器学习任务的文本描述，自动生成和优化完整的机器学习工作流程代码，包括数据准备、建模和后处理等环节。为了应对机器学习程序的长度和多样性，该方法采用了将程序分解为更小、更易管理的部分，并针对机器学习程序设计了测试技术和数值评估方法。实验结果表明，Text-to-ML 在生成机器学习程序方面优于现有方法，且自动机器学习技术可以显著提高生成程序的性能。 |
| DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | 2024-05-07 | https://arxiv.org/abs/2405.04434 | DeepSeek-AI | DeepSeek-V2 是 DeepSeek 系列最新的混合专家语言模型（MoE）。该模型在保证高效推理和经济训练成本的同时，达到了 236B 的总参数量，其中每个 token 激活 21B 参数，并支持 128K tokens 的上下文长度。此外，论文还引入了创新的 multi-head latent attention（MLA）和 DeepSeekMoE 架构，前者通过将 KV 缓存压缩为潜在向量来保证推理效率，后者则通过稀疏计算实现了经济成本下的强模型训练。与之前的 DeepSeek 67B 模型相比，DeepSeek-V2 在显著提升性能的同时，减少了 42.5% 的训练成本，将 KV 缓存减少了 93.3%，并将最大生成吞吐量提高了 5.76 倍。 |
| MHPP: Exploring the Capabilities and Limitations of Language Models Beyond Basic Code Generation | 2024-05-19 | https://arxiv.org/abs/2405.11430 | University of Edinburgh, University of Hong Kong | 本文提出了一个新的数据集 Mostly Hard Python Problems (MHPP)，用于更全面、深入地评估大型语言模型在函数级代码生成方面的能力。作者分析了现有的 HumanEval 和 MBPP 两个常用基准测试的局限性，发现它们在质量、难度和粒度方面存在不足。因此，他们创建了由 140 个独特的人工精心设计的问题组成的 MHPP 数据集，重点测试语言模型在理解规范和限制、进行多步推理以及有效应用编码知识方面的能力。通过在 22 个语言模型上进行初步评估，发现许多在 HumanEval 上 表现出色的模型在 MHPP 上难以取得类似的成功，突显出这些模型的各种局限性。 |
| Multiple-Choice Questions are Efficient and Robust LLM Evaluators | 2024-05-20 | https://arxiv.org/abs/2405.11966 | Shanghai Jiao Tong University | 本文基于当前最流行的四个大模型测评数据集 GSM8K、MATH、HumanEval、MBPP 构建了三个多项选择题格式的测试基准 GSM-MC、MATH-MC 和 PythonIO。对 GSM8K 和 MATH，作者收集 60 个开源模型在原始数据集上的错误答案构建选择题，并通过大量实验表明大模型在选择题格式的测试基准上得分与在生成式评估的测试基准上得分强相关，且对干扰选项设置和选项顺序具有相当的鲁棒性，而测试开销则减小了 30 倍。对于 HumanEval 和 MBPP 两个代码生成数据集，作者则构造了一个全新的 Python 程序输出预测测试基准，且实验表明大模型还有很大的提升空间。 |
| AutoCoder: Enhancing Code Large Language Model with AIEV-Instruct | 2024-05-23 | https://arxiv.org/abs/2405.14906 | University of Connecticut | AutoCoder 是首个在 HumanEval 基准测试中超越 GPT-4 Turbo（2024 年 4 月版）和 GPT-4o 的大语言模型，实现了 90.9% 的 pass@1 得分。此外，AutoCoder 提供了比 GPT-4 Turbo 和 GPT-4o 更加通用的代码解释器，可以安装外部程序包。论文还提出了一种名为 AIEV-Instruct 的训练数据生成方法，结合了 agent 交互和外部代码执行验证，较之前的大规模代码数据集生成方法，减少了对大型专有模型的依赖，并提供了经过执行验证的代码数据集。 |



4、软件开发自动化开源项目| 项目 | 地址 | 介绍 |  |
| --- | --- | --- | --- |
| OpenDevin | https://github.com/OpenDevin/OpenDevin 30.2k | OpenDevin 是一个能够执行复杂工程任务并能够与用户积极协作的自主 AI 软件工程师，其目标是复制和改进 Devin。Devin 利用 shell、代码编辑器和网络浏览器等工具，展示了 LLM 在软件开发中的潜力。我们的目标是探索和扩展 Devin 的能力，明确优点和改进空间，以推动开放源代码模型的进步。项目目前的几个主要工作方向包括：UI：开发用户友好的界面，包括聊天界面，显示命令的 shell 和网络浏览器。架构：构建出稳定的框架，强壮的后端能够读取、写入和运行简单的命令。Agent 的能力：提升 Agent 的生成 bash 脚本、运行测试和执行其他软件工程任务的能力。评估：建立符合 Devin 评估准则的最小化评估管道。 | https://docs.all-hands.dev/modules/usage/intro |
| ChatDev | https://github.com/OpenBMB/ChatDev 24.9k | ChatDev是一个可以模拟整个软件开发团队的开源对话平台。由OpenBMB开发，OpenBMB是一个旨在为AGI构建基础模型和系统的研究实验室。ChatDev是一个多代理人的组织结构，以“通过编程彻底改变数字世界”为使命，将代理们团结在一起。ChatDev中的代理通过参加专门的功能研讨会进行协作，完成设计、编码、测试和文档编制等任务。ChatDev的主要目标是提供一个易于使用，高度可定制和可扩展的框架，该框架基于大型语言模型（LLM），是一个研究集体智慧的理想场景。ChatDev的功能包括：集成了版本控制的Git、用于交互式参与设计阶段的Human-Agent-Interaction模式，以及用于生成软件中使用到的图像的艺术模式。 |  |
| MetaGPT | https://github.com/geekan/MetaGPT 43k | MetaGPT 是另一个开源 AI 智能体框架，它试图模仿传统软件公司的结构。与 ChatDev 类似，智能体被分配了产品经理、项目经理和工程师的角色，并协作完成用户定义的编码任务。到目前为止，MetaGPT 只能处理中等难度的任务——比如编写贪吃蛇游戏或构建简单的实用程序应用程序——但它是一个很有前途的工具，未来可能会迅速发展。生成一个完整的项目将花费你大约 2 美元的 OpenAI API 费用。 |  |
| Devika | https://github.com/stitionai/devika 18.1k | Devika是由Lyminal和Stition.AI创始人Mufeed VH（Hamzakutty）研发的一款开源AI软件工程师。该系统能够理解人类指令，将其拆解成具体任务，并通过自主研究和编写代码来达成预设目标。与Devin相比，Devika力求成为一个有竞争力的开源替代方案。它运用了LLMs、规划与推理算法以及网络浏览功能，能够智能地进行软件开发工作。Devika的一大亮点在于其充当AI配对编程角色的能力，能在复杂的编码任务中大幅减少对人力介入的需求。这意味着它可以协助开发者在遇到复杂问题时共同完成编程工作，提升开发效率。Devika能够简化各种软件开发流程，包括创建新特性、调试代码，乃至从零开始构建整个项目，从而有效提高开发工作的整体效能。Devin与Devika之间的主要区别除了后者是开源性质之外，还在于Devika所采用的基础技术不同——Mufeed在构建Devika时选择了Claude 3而非GPT-4作为核心技术。这一选择可能影响到两者在处理软件开发任务时的具体表现和能力范围。 |  |
| Replit Code Repair |  | Replit的Code Repair是一款低延迟的代码修复AI工具。它利用了基于大量代码示例及其相应修复方案训练的大型语言模型。这种LLM能够分析你的代码，并识别潜在的错误或低效之处。Replit团队将一个规模达70亿参数的代码LLM进行了微调，使其行为模式模拟LSP（Language Server Protocol）代码操作。其特殊之处在于训练数据——精心混合了来自真实世界的错误案例（在Replit平台上收集）以及通过合成方式生成的代码修复方案。Replit采取的方法包括使用操作转换（Operational Transformations，OTs）和会话事件，构建包含（代码，诊断）对的数据集。他们利用大型预训练代码模型合成差异，并针对代码修复任务对其进行精细调整优化。 | https://blog.replit.com/code-repair |
| SWE Agent | https://github.com/princeton-nlp/SWE-agent 12.7k | SWE Agent 是一款开源的软件工程助手，与Devin和Devika类似，由普林斯顿大学John Yang、Carlos E. Jimenez和Alexander Wettig带领的团队开发。该工具旨在将诸如GPT-4这样的语言模型转变为能够在真实GitHub仓库中修复bug和处理问题的软件工程代理。在完整的SWE-bench测试集中，SWE-Agent成功解决了其中12.29%的问题。SWE-Agent之所以能取得这样的成果，关键在于其创新的Agent-Computer Interface（ACI，代理-计算机接口）。这一接口极大地优化了语言模型与代码仓库之间的交互流程。不同于传统的做法，SWE-Agent的ACI设计简化了命令和反馈格式，使得模型更容易在仓库内部导航、编辑及执行代码文件。开发者可以通过Docker和Miniconda轻松设置此工具，并按照项目文档中详述的简单安装和配置步骤来完成部署工作。 |  |

5、 AIAgent开源项目汇总【GitHub AIAgent开源项目】https://github.com/e2b-dev/awesome-ai-agents 

| 项目 | 地址 | 类别 | 介绍 |
| --- | --- | --- | --- |
| AutoGPT | https://github.com/Significant-Gravitas/AutoGPT 166k | 通用 | AutoGPT是一个使用GPT-4创建的完全自主的AI代理。AutoGPT于2023年3月由首席开发商Toran布鲁斯理查兹首次发布，他也被称为游戏公司Significant Gravitas Ltd.的创始人，该公司生产的电脑游戏带有“道德色彩”，旨在造福和教育全人类。Auto-GPT是一个实验性的开源应用程序，展示了GPT-4语言模型的功能。这个程序由GPT-4驱动，可以将LLM的“思想”汇聚、连接在一起，以自主实现用户设定的任何目标。 |
| MetaGPT | https://github.com/geekan/MetaGPT 43k | 多代理、编码、自定义构建 | MetaGPT 是另一个开源 AI 智能体框架，它试图模仿传统软件公司的结构。与 ChatDev 类似，智能体被分配了产品经理、项目经理和工程师的角色，并协作完成用户定义的编码任务。到目前为止，MetaGPT 只能处理中等难度的任务——比如编写贪吃蛇游戏或构建简单的实用程序应用程序——但它是一个很有前途的工具，未来可能会迅速发展。生成一个完整的项目将花费你大约 2 美元的 OpenAI API 费用。 |
| AgentGPT | https://github.com/reworkd/AgentGPT 31.1k | 通用 | AgentGPT 允许您配置和部署自主 AI 代理。命名您自己的自定义人工智能，并让它开始实现任何可以想象的目标。它将尝试通过思考要完成的任务、执行任务并从结果中学习🚀来实现目标。 |
| OpenDevin | https://github.com/OpenDevin/OpenDevin 30.2k |  | OpenDevin 是一个能够执行复杂工程任务并能够与用户积极协作的自主 AI 软件工程师，其目标是复制和改进 Devin。Devin 利用 shell、代码编辑器和网络浏览器等工具，展示了 LLM 在软件开发中的潜力。我们的目标是探索和扩展 Devin 的能力，明确优点和改进空间，以推动开放源代码模型的进步。项目目前的几个主要工作方向包括：UI：开发用户友好的界面，包括聊天界面，显示命令的 shell 和网络浏览器。架构：构建出稳定的框架，强壮的后端能够读取、写入和运行简单的命令。Agent 的能力：提升 Agent 的生成 bash 脚本、运行测试和执行其他软件工程任务的能力。评估：建立符合 Devin 评估准则的最小化评估管道。 |
| AutoGen | https://github.com/microsoft/autogen 29.7k | 通用、自定义构建、多代理 | AutoGen是一个由微软与OpenAI以及宾夕法尼亚州立大学和华盛顿大学的研究人员合作建立的人工智能代理框架。支持多代理对话，以解决用户的任务。可以使用多个代理来开发LLM应用程序，这些代理可以相互配合以解决任务。AutoGen代理是可定制的，可转换的，并且允许人类参与其中。它们可以在各种模式下运行，这些模式采用LLM，人工输入和工具的组合。 |
| ChatDev | https://github.com/OpenBMB/ChatDev 24.9k | 编码、多代理 | ChatDev是一个可以模拟整个软件开发团队的开源对话平台。由OpenBMB开发，OpenBMB是一个旨在为AGI构建基础模型和系统的研究实验室。ChatDev是一个多代理人的组织结构，以“通过编程彻底改变数字世界”为使命，将代理们团结在一起。ChatDev中的代理通过参加专门的功能研讨会进行协作，完成设计、编码、测试和文档编制等任务。ChatDev的主要目标是提供一个易于使用，高度可定制和可扩展的框架，该框架基于大型语言模型（LLM），是一个研究集体智慧的理想场景。ChatDev的功能包括：集成了版本控制的Git、用于交互式参与设计阶段的Human-Agent-Interaction模式，以及用于生成软件中使用到的图像的艺术模式。 |
| JARVIS | https://github.com/microsoft/JARVIS 23.5 | 通用 | 引入了一个协作系统，其中包括LLM作为控制器，众多专家模型作为协作执行者（来自 HuggingFace Hub）。我们系统的工作流程由四个阶段组成：Task Planning: 使用ChatGPT分析用户的请求以了解他们的意图，并将其分解为可能的可解决的任务。Model Selection: 为了解决计划的任务，ChatGPT 根据描述选择 Hugging Face 上托管的专家模型。Task Execution: 调用并执行每个选定的模型，并将结果返回给ChatGPT。Response Generation: 最后，使用ChatGPT整合所有模型的预测，并生成响应。 |
| BabyAGI  | https://github.com/yoheinakajima/babyagi 19.8k | 通用 | BabyAGI于2023年3月由Yohei Nakajima发布。与AutoGPT类似，也是使用GPT-4来开发的完全自主的聊天机器人。该系统使用OpenAI和矢量数据库（如Chroma或Weaviate）来创建、优先处理和执行任务。这个系统背后的主要思想是，它根据先前任务的结果和预定义的目标创建任务。然后，该脚本使用OpenAI的自然语言处理（NLP）功能来创建基于目标的新任务，并使用Chroma/Weaviate来存储和检索上下文的任务结果。BabyAGI通过运行一个无限循环来工作，该循环执行以下步骤：从任务列表中提取第一个任务。将任务发送给执行代理，执行代理使用OpenAI的API根据上下文完成任务。丰富结果并将其存储在 Chroma或者Weaviate（向量数据库）。创建新任务并根据目标和上一任务的结果重新确定任务列表的优先级。 |
| Aider  | https://github.com/paul-gauthier/aider 16.2k | 编码，GitHub | Aider 使用命令行编辑本地存储库中的代码。Aider 是 SWE Bench 上得分最高之一。 SWE Bench 是一个具有挑战性的软件工程基准测试，其中 aider 解决了 django、scikitlearn、matplotlib 等流行开源项目中的实际GitHub 问题。 |
| SuperAGI | https://github.com/TransformerOptimus/SuperAGI 15.1k | 通用 | SuperAGI 是 AutoGPT 更灵活、更用户友好的替代方案。你可以将其视为开源 AI 智能体的启动板，它提供了构建、维护和运行自己的代理所需的一切。它还包括插件和云版本，您可以在其中进行测试。该框架具有多个 AI 模型、图形用户界面、与矢量数据库的集成（用于存储/检索数据）和性能洞察。还有一个带有工具包的市场，可让你将其连接到流行的应用和服务，例如 Google Analytics。 |
| ShortGPT | https://github.com/RayVentura/ShortGPT | 视频 | 在生成内容方面，AI 模型的表现非常出色。但直到最近，视频格式仍然在很大程度上得不到充分支持。ShortGPT 是一个框架，它允许你使用大型语言模型来简化视频创建、语音合成和编辑等复杂任务。ShortGPT 可以处理大多数典型的视频相关任务，例如编写视频脚本、生成画外音、选择背景音乐、编写标题和描述，甚至编辑视频。无论使用哪个平台，该工具都适用于短视频内容和长视频内容。 |
| Camel  | https://github.com/camel-ai/camel 5.2k | 通用 | Camel 是早期的多智能体框架之一，它使用独特的角色扮演设计，使多个智能体能够相互通信和协作。两个 ChatGPT 代理之间的对话一切都始于一项人类定义的任务。该框架利用 LLM 的强大功能动态地为智能体分配角色，指定和开发复杂的任务，并安排角色扮演场景，以实现智能体之间的协作。这就像人工智能的剧场。 |
| agents | https://github.com/aiwaves-cn/agents 5.1k | 通用、自定义构建、多代理 | https://agentsv2.readthedocs.io/en/latest/agent.html |
| AgentVerse | https://github.com/OpenBMB/AgentVerse 4k | 通用、自定义构建、多代理 | AgentVerse 提供了一个多功能的框架，简化了为大型语言模型（LLMs）创建自定义多智能体环境的过程。旨在快速、低成本的开发和定制，我们的框架赋能研究人员专注于他们的研究，而不被实现细节所困扰。 |
| AutoDev | https://github.com/unit-mesh/auto-dev 2.7k | 编程 | AutoDev：人工智能驱动的编码向导，具有多语言支持、自动代码生成，以及有用的错误消除助手！包含可定制的提示和神奇的自动开发/测试/文档/代理功能！  |
| OpenAGI | https://github.com/agiresearch/OpenAGI 1.9k | 通用 | OpenAGI 是一个开源 AGI（通用人工智能）研究平台，结合了小型专家模型（针对情绪分析或图像去模糊等任务量身定制的模型）和任务反馈强化学习 (RLTF)，以提高其输出。从本质上讲，OpenAGI 与其他自主开源人工智能框架没有太大区别。它汇集了 ChatGPT 等流行平台、LLaMa2 等 LLM 和其他专用模型，并根据任务上下文动态选择正确的工具。 |
| LoopGPT | https://github.com/farizrahman4u/loopgpt/tree/main 1.4k |  | LoopGPT 是 Toran Bruce Richards 的 AutoGPT 的一个迭代。除了适当的 Python 实现之外，该框架还带来了对 GPT-3.5、集成和自定义智能体功能的改进支持。它还消耗更少的 API 令牌，因此运行起来要便宜得多。LoopGPT 可以基本自动运行，也可以在循环中由人参与运行，以最大限度地减少模型幻觉。有趣的是，该框架不需要访问矢量数据库或外部存储来保存数据。它可以将代理状态写入文件或 Python 项目。 |
| AI Legion | https://github.com/eumemic/ai-legion 1.3k |  | AI Legion: 可以协同工作完成任务的自主代理的框架。 |
| AutoPR | https://github.com/irgolic/AutoPR 1.2k |  | AutoPR在您的代码库上运行人工智能驱动的工作流程。 |
| Adala | https://github.com/e2b-dev/awesome-ai-agents <1k |  | Adala 为实施专门从事数据处理的代理提供了一个强大的框架，重点是各种数据标记任务。这些智能体是自主的，这意味着它们可以通过迭代学习独立获得一项或多项技能。这个学习过程受到他们的操作环境、观察和反思的影响。用户通过提供地面实况数据集来定义环境。每个代理都会在我们所说的“运行时”（即“运行时”）中学习并应用其技能，这与LLM。 |
| Agent4Rec | https://github.com/LehengTHU/Agent4Rec <1k |  | Agent4Rec，一个具有 1,000 个推荐系统的模拟器LLM- 授权的生成代理。这些代理是从MovieLens-1M数据集初始化的，体现了不同的社会特征和偏好。每个智能体以逐页的方式与个性化电影推荐进行交互，并进行观看、评分、评价、退出、采访等各种动作。通过 Agent4Rec，我们希望探索以下潜力：LLM -授权生成代理在推荐环境中模拟真实、独立的人类的行为。 |
| AgentForge | https://github.com/DataBassGit/AgentForge <1k |  | AgentForge是一个低代码框架，专为人工智能驱动的自主代理和认知架构的快速开发、测试和迭代而定制。兼容一系列LLM模型 - 目前支持 OpenAI、Google 的 Gemini、Anthropic 的 Claude 和 Ollama 或本地的 LMStudioLLMs — 它提供了根据您的特定需求为不同代理运行不同模型的灵活性。 |
| Agent Pilot | https://github.com/jbexta/AgentPilot <1k |  | Agent Pilot 是一款开源桌面应用程序，用于创建、管理 AI 代理并与 AI 代理聊天。在一种环境下组合来自不同提供商的模型，并且 在低代码环境中配置它们之间的交互。Open Interpreter 内置为应用程序代码解释器，让它运行代码 做你要求它做的任何事情。 |
| AIlice | https://github.com/myshell-ai/AIlice <1k |  | AIlice 是一个完全自主的通用人工智能代理。该项目旨在创建一个独立的人工智能助手，类似于JARVIS，基于开源LLM。 AIlice 通过构建使用大型语言模型的“文本计算机”来实现这一目标（LLM ）作为其核心处理器。目前，AIlice 表现出了对一系列任务的熟练程度，包括主题研究、编码、系统管理、文献综述以及超出这些基本能力的复杂混合任务。 |
| Automata | https://github.com/emrgnt-cmplxty/automata <1k |  | Automata 的目标是发展成为一个完全自主、自编程的人工智能系统。 |
| Autonomous HR Chatbot  | https://github.com/stepanogil/autonomous-hr-chatbot  <1k |  | 自主人力资源聊天机器人 - 一个能够使用现有工具回答 HR 查询的自主代理。它是使用 LangChain 的代理和工具模块制作的，使用 Pinecone 作为矢量数据库，并由 ChatGPT 或 gpt-3.5-turbo 提供支持。前端是使用streamlit_chat 组件的Streamlit。 |
| BondAI | https://github.com/krohling/bondai  <1k |  | BondAI有3种使用方式：🛠️ Command Line Interface (CLI) - 这是快速启动和运行的最简单方法。使用一组预先配置的工具在命令行上运行 BondAI。🐋 Docker - 如果您计划使用运行代码或直接访问 shell 的工具，建议在 Docker 容器中运行 BondAI。🏗️ Start Coding with BondAI - 将 BondAI 集成到您自己的代码库中并开始构建您自己的代理。 |
|  |  |  |  |







