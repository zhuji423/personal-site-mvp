---
title: "Claude Mythos泄露震动市场，Codex插件生态启动，TurboQuan"
description: "**1. Anthropic 意外泄露下一代模型 Claude Mythos，称其为'阶跃式变革'**"
date: "2026-03-28"
category: "每日科技日报"
---

# 20260328 Claude Mythos泄露震动市场，Codex插件生态启动，TurboQuant重塑存储芯片格局

Owner: 每日新闻抓取器
Last edited time: 2026年3月28日 10:04

## 每日 AI 新闻简报｜2026-03-28

### 今日 20 条（按重要度排序）

---

**1. Anthropic 意外泄露下一代模型 Claude Mythos，称其为"阶跃式变革"**

- **核心做了什么（What happened）**：Anthropic 因 CMS 配置错误，将约 3000 份内部文件（含未发布博文）暴露在公开数据存储中，其中详述了名为 "Claude Mythos"（代号 Capybara）的新一代模型。该模型定位为 Opus 之上的全新层级，在编码、学术推理和网络安全测试中"显著超越" Opus 4.6。Anthropic 已确认模型真实存在并正在向早期客户测试。
- **启示 / To-dos**：
    - 关注 Mythos 对 Agent 多步推理和编码任务的实际提升幅度
    - 网络安全能力的"双刃剑"效应需要纳入安全评估框架
    - 企业级定价将显著上升，需提前规划算力与成本预算
    - 观察"Capybara"层级是否开启前沿模型的分层定价趋势
- **正面**：前沿能力再次大幅跃进；编码与推理能力突破可能加速 Agent 落地
- **负面 / 风险**：泄露事件本身暴露 Anthropic 的安全管理漏洞；网络安全股因此下跌；超高算力需求可能加剧供应瓶颈
- **原文链接**：[Fortune 独家报道](https://fortune.com/2026/03/26/anthropic-data-leak-mythos-model/)
- **补充链接**：[The Verge 跟进](https://www.theverge.com/2026/3/27/anthropic-security-lapse-model-release) ｜ [The Decoder 技术分析](https://the-decoder.com/anthropic-leak-reveals-new-model-claude-mythos/)

---

**2. Anthropic 在高峰时段收紧 Claude 使用限额，算力紧张浮出水面**

- **核心做了什么（What happened）**：Anthropic 宣布在工作日高峰时段（太平洋时间 5am-11am）"加速消耗" 5 小时会话限额，约 7% 用户会比以前更快触及限制。每周总限额不变，但分布发生调整。此举是因 Claude 近期需求激增导致的算力瓶颈。
- **启示 / To-dos**：
    - 将重度 token 密集型任务（如 Claude Code 后台作业）调至非高峰时段
    - 对依赖 Claude 的 Agent 工作流建立降级/切换方案
    - 开源模型与本地推理的战略价值再次凸显
- **正面**：每周总量不变，多数用户影响有限；推动用户优化使用效率
- **负面 / 风险**：实质上是涨价/降量；对全天候运行的自动化流程不友好；信任危机
- **原文链接**：[Business Insider 报道](https://www.businessinsider.com/anthropic-claude-session-limits-peak-hours-compute-strain-2026-3)

---

**3. OpenAI 推出 Codex 插件系统，正式超越编码工具定位**

- **核心做了什么（What happened）**：OpenAI 为 Codex 发布插件体系，首批 20+ 集成包括 Figma、Notion、Gmail、Slack、Google Drive 等。插件将应用与技能打包，实现一键认证与调用，支持 Codex App、CLI 和 IDE 扩展。同时重置所有订阅层级的 Codex 使用额度以鼓励试用。
- **启示 / To-dos**：
    - 评估 Codex 插件对现有自动化流程（Zapier/Make）的替代潜力
    - 关注插件 Marketplace 的开放策略与自定义插件开发模式
    - 插件标准化可能成为 AI 编码助手的新竞争维度
- **正面**：将 AI 编码助手从"写代码"拓展为"端到端工作流自动化"；生态效应显著
- **负面 / 风险**：平台锁定风险增加；插件安全审计与权限管理需跟进
- **原文链接**：[OpenAI 官方博客](https://developers.openai.com/)
- **补充链接**：[Ars Technica：Codex 正式超越编码](https://arstechnica.com/2026/03/openai-codex-plugins/) ｜ [ZDNET 评测](https://www.zdnet.com/article/openai-codex-plugins-standardize-ai-workflows/)

---

**4. Google TurboQuant 压缩算法发布，存储芯片股一周蒸发约 $1000 亿**

- **核心做了什么（What happened）**：Google Research 发表 TurboQuant（ICLR 2026），可将 LLM KV Cache 压缩至 3-bit 级别（约 5-6x 压缩）且精度几乎无损（99.5% 注意力保真度）。论文引发市场恐慌，Micron 一周跌 15%，美国存储芯片股总市值蒸发约 $1000 亿。
- **启示 / To-dos**：
    - llama.cpp / vLLM 社区已开始集成，值得跟进实测
    - 量化技术路线（TurboQuant vs GPTQ vs AWQ）需要在实际推理场景对比
    - 对 AI 基础设施投资假设的"内存需求"部分可能需要重新评估
- **正面**：大幅降低推理内存需求与成本；推动边缘部署可行性
- **负面 / 风险**：短期市场可能过度反应；实际产业落地周期可能比预期更长
- **原文链接**：[Google Research Blog](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)
- **补充链接**：[llama.cpp 社区讨论](https://github.com/ggml-org/llama.cpp/discussions/20969)

---

**5. SoftBank 获 $400 亿过桥贷款，加注 OpenAI 投资**

- **核心做了什么（What happened）**：SoftBank 从摩根大通、高盛等银行获得 $400 亿过桥贷款（2027 年到期），主要用于追加 OpenAI 投资。此前 OpenAI 已完成 $1100 亿融资（$730 亿 pre-money 估值），SoftBank、NVIDIA 和 Amazon 各出资 $300 亿、$300 亿和 $500 亿。
- **启示 / To-dos**：
    - 关注 OpenAI 2026 年 IPO 时间线信号
    - 巨额债务融资对 AI 基础设施投资周期的影响
    - 对比 Anthropic IPO（消息称 Q4）与 OpenAI IPO 的竞争格局
- **正面**：资本持续涌入 AI 基础设施；多元化投资者结构
- **负面 / 风险**：杠杆风险高企；若 AI 回报不达预期可能引发连锁反应
- **原文链接**：[Reuters 报道](https://www.reuters.com/technology/softbank-secures-40b-bridge-loan-2026-03-27/)

---

**6. NVIDIA 开源 Nemotron 3 Super 120B：美国首个开源前沿 MoE 模型**

- **核心做了什么（What happened）**：NVIDIA 发布 Nemotron 3 Super 120B-A12B 开源模型（仅激活 12B 参数的 MoE 架构），在同级别模型中速度领先。NVIDIA 还宣布未来 5 年投入 $260 亿发展开源模型生态。
- **启示 / To-dos**：
    - 硬件厂商直接下场做模型，对"模型-芯片-工具链"垂直整合的影响
    - 12B 活跃参数 + MoE 是极具工程价值的部署甜点
    - 与 Qwen3.5、Llama 4 等竞品做部署效率对比
- **正面**：开源 + MoE + 高吞吐的组合对企业部署极具吸引力
- **负面 / 风险**：NVIDIA 生态绑定加深；开源模型的长期维护承诺待观察
- **原文链接**：[DeepLearning.AI](http://DeepLearning.AI) [The Batch](https://www.deeplearning.ai/the-batch/nvidias-open-nemotron-3-super-120b-a12b-model-sets-new-paces-in-its-class/)

---

**7. OpenAI 与 Amazon 合作构建 AI Agent 有状态运行时环境**

- **核心做了什么（What happened）**：OpenAI 与 Amazon 联合宣布将构建面向 AI Agent 的"有状态运行时环境"（stateful runtime environment），计划在 AWS 上部署。此举标志 OpenAI 正式将云计算资源从 Microsoft Azure 向多元化方向拓展，Amazon 也可在自有产品中使用 OpenAI 模型。
- **启示 / To-dos**：
    - "有状态运行时"对 Agent 持久化记忆与任务续接至关重要
    - OpenAI-Microsoft 关系降温信号，关注对 Azure AI 生态的影响
    - AWS 作为 Agent 基础设施的竞争力可能因此大幅提升
- **正面**：Agent 运行时基础设施标准化加速；多云策略降低单一供应商风险
- **负面 / 风险**：发布日期未定；Microsoft-OpenAI 合作裂痕可能加深
- **原文链接**：[DeepLearning.AI](http://DeepLearning.AI) [报道](https://www.deeplearning.ai/the-batch/openais-deal-with-amazon-to-build-a-stateful-runtime-environment-for-ai-agents/)

---

**8. xAI 发布 Grok Imagine 1.0，视频生成成本大幅下降**

- **核心做了什么（What happened）**：xAI 发布 Grok Imagine 1.0 视频生成器，支持文本+图片/视频输入生成含对话和音效的视频片段。定价约 $4.20/分钟（含音频），与 Kling 2.5 Turbo（不含音频）持平，远低于已停服的 Sora 2 Pro（约 7 倍价差）。在独立质量排名中位居榜首。
- **启示 / To-dos**：
    - 视频生成已进入"质量+成本"双重竞争阶段
    - 含音频生成的一体化方案可能成为差异化方向
    - 对比 Sora 停服后的市场格局变化
- **正面**：性价比极高；质量与成本同时领先
- **负面 / 风险**：xAI 平台可用性与企业级 SLA 待验证
- **原文链接**：[DeepLearning.AI](http://DeepLearning.AI) [报道](https://www.deeplearning.ai/the-batch/grok-imagine-1-0-sharply-cuts-costs-for-high-quality-video-generation/)

---

**9. Anthropic 赢得联邦法院裁决，但"供应链风险"标签仍未完全解除**

- **核心做了什么（What happened）**：联邦法官在加州北区法院裁定初步禁令有利于 Anthropic，阻止国防部根据 10 U.S.C. § 3252 执行"供应链风险"标签，认定此举构成"第一修正案报复"。但国防部依据另一法规（41 U.S.C. § 4713）的相同标签仍在生效，需 DC 巡回上诉法院另行裁决。
- **启示 / To-dos**：
    - 关注 DC 巡回法院的后续裁决，这将决定 Anthropic 能否完全恢复政府合同资格
    - AI 公司与政府关系的法律框架正在快速演变
    - 对 AI 治理与安全发言可能带来的商业风险需要评估
- **正面**：法院明确反对以"言论报复"为由限制 AI 公司；Anthropic 法律地位初步改善
- **负面 / 风险**：双重法律路径意味着不确定性持续；Google 继续资助 Anthropic 数据中心表明大厂押注未变
- **原文链接**：[Politico 深度分析](https://www.politico.com/news/2026/03/27/anthropic-dod-supply-chain-risk-ruling)
- **补充链接**：[Wired 报道](https://www.wired.com/story/anthropic-supply-chain-risk-designation-halted-judge/)

---

**10. Google Gemini 支持导入 ChatGPT/Claude 聊天记录与记忆**

- **核心做了什么（What happened）**：Google 发布 Gemini 新工具，允许用户上传其他 AI 应用（ChatGPT、Claude 等）的聊天记录和上下文记忆，大幅降低迁移门槛。这是首次有主流 AI 助手提供正式的"竞品迁移"功能。
- **启示 / To-dos**：
    - AI 助手间的"数据可迁移性"成为新竞争焦点
    - 关注用户锁定策略的演变方向
    - 企业用户可借此做多平台对比评估
- **正面**：降低用户切换成本；推动行业向开放标准演进
- **负面 / 风险**：隐私与数据安全需要审慎评估；竞品可能加固自身数据壁垒作为回应
- **原文链接**：[Google Keyword 官方博客](https://blog.google/products/gemini/import-ai-memories-chat-history/)

---

**11. Meta 为路易斯安那数据中心资助 7 座天然气发电厂（5.2GW+）**

- **核心做了什么（What happened）**：Meta 与 Entergy Louisiana 达成协议，将资助新建 7 座联合循环天然气发电厂（总计 5.2GW+），外加 240 英里 500kV 输电线路和电池储能设施。这是在已有 3 座电厂（约 2GW）基础上的大规模扩建，总计约 7.2GW。Entergy 称将为客户节省 $20 亿。
- **启示 / To-dos**：
    - AI 基础设施的能源需求正以指数级增长
    - 数据中心自建电力设施正成为新常态
    - 碳排放与可持续性将成为 AI 产业面临的关键挑战
- **正面**：解决算力扩张的电力瓶颈；Meta 全额承担成本保护纳税人
- **负面 / 风险**：7 座新化石燃料电厂的环境影响巨大；加深对天然气的依赖
- **原文链接**：[Bloomberg 报道](https://www.bloomberg.com/news/articles/2026-03-27/meta-funds-seven-gas-plants-biggest-data-center)

---

**12. Microsoft 接手 Crusoe 德州 900MW 数据中心，OpenAI/Oracle 退出**

- **核心做了什么（What happened）**：Microsoft 将租赁 Crusoe 在德州 Abilene 的 900MW 数据中心项目，此前 Oracle 和 OpenAI 据报已退出该项目。首栋建筑预计 2027 年中交付。Mustafa Suleyman（Microsoft AI 负责人）称此举为 AI 基础设施舰队扩容。
- **启示 / To-dos**：
    - AI 数据中心需求的"可替代性"极高——一家退出立刻有下家接手
    - OpenAI-Microsoft 基础设施关系的微妙变化值得关注
    - Crusoe 作为 AI 数据中心供应商的地位上升
- **正面**：AI 算力需求依然旺盛；微软积极扩张基础设施
- **负面 / 风险**：OpenAI 与 Microsoft 渐行渐远的信号；数据中心过度投资风险
- **原文链接**：[Bloomberg 报道](https://www.bloomberg.com/news/articles/2026-03-27/microsoft-crusoe-abilene-data-center)

---

**13. Google 将资助 Anthropic 德州数据中心（Nexus 1GW+ 园区）**

- **核心做了什么（What happened）**：据 FT 报道，Google 正与 Nexus Data Centers 洽谈资助其德州 1GW+ 数据中心园区（该园区租给 Anthropic 使用），银行方面准备提供高达 $50 亿的第一期融资。Google 持有 Anthropic 约 14% 股权并已锁定 100 万颗 TPU 的合作。
- **启示 / To-dos**：
    - "投竞品 + 提供基础设施"的策略在 AI 领域已成常态
    - Google-Anthropic 关系不受政府供应链争议影响
    - 数据中心融资规模持续膨胀
- **正面**：Anthropic 基础设施获强力保障；Google 对冲自研 Gemini 的风险
- **负面 / 风险**：竞争关系与投资关系的冲突可能加剧；过度集中化风险
- **原文链接**：[FT 报道](https://www.ft.com/content/google-nexus-anthropic-data-center-2026)

---

**14. Physical Intelligence 机器人公司拟融资 $10 亿，估值 $110 亿+**

- **核心做了什么（What happened）**：成立仅两年的机器人 AI 初创公司 Physical Intelligence（由前 Google DeepMind 研究员创立）正在洽谈新一轮约 $10 亿融资，估值将达 $110 亿以上。该公司致力于开发面向机器人的通用 AI 模型。
- **启示 / To-dos**：
    - 具身智能（Embodied AI）赛道持续升温
    - 关注其通用机器人模型对工业自动化的潜在影响
    - 与 Figure、1X 等竞品的对比
- **正面**：验证了 AI+机器人赛道的资本吸引力；学术团队创业的标杆案例
- **负面 / 风险**：估值是否过高；商业化路径仍不清晰
- **原文链接**：[Bloomberg 报道](https://www.bloomberg.com/news/articles/2026-03-27/physical-intelligence-robotics-funding)

---

**15. OpenAI 关停 Sora 视频生成服务**

- **核心做了什么（What happened）**：OpenAI 宣布关闭 Sora 视频生成器服务。结合近期 OpenAI 将算力重新分配给核心模型训练的趋势，以及 Anthropic Mythos 的"阶跃式"竞争压力，此举被解读为战略性收缩以集中资源。
- **启示 / To-dos**：
    - 视频生成赛道的竞争格局因 Sora 退出而重新洗牌
    - 企业用户若依赖 Sora 需立即寻找替代方案（Grok Imagine、Kling、Runway 等）
    - AI 公司的"算力分配"决策正变得越来越关键
- **正面**：聚焦核心竞争力；释放算力用于更具战略价值的方向
- **负面 / 风险**：损害用户信任；视频生态合作伙伴受影响
- **原文链接**：[DeepLearning.AI](http://DeepLearning.AI) [报道](https://www.deeplearning.ai/the-batch/sora-no-more-openai-shuts-down-video-maker/)

---

**16. Karpathy autoresearch 持续迭代：AI Agent 自动化研究范式深化**

- **核心做了什么（What happened）**：Karpathy 的 autoresearch 仓库（58.5k 星）和 nanochat（50.5k 星）在 3 月保持高频更新（47% commits、18% PR、26% issues）。autoresearch 让 AI Agent 在单 GPU 上自动运行训练实验，通过 Markdown 编程"研究组织"来驱动自动化优化循环。SkyPilot 团队已探索将其扩展到 GPU 集群。
- **启示 / To-dos**：
    - "用 Markdown 编程研究组织"的范式值得团队尝试
    - 单 GPU 自动研究 → 多 GPU 集群是自然演进方向
    - 把"能跑、能测、能回归"的实验基建当作核心生产力
- **正面**：极大降低 AI 研究的人力门槛；社区生态活跃
- **负面 / 风险**：自动化研究的可复现性与质量保证仍需工程化
- **原文链接**：[GitHub - karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- **补充链接**：[GitHub - karpathy/nanochat](https://github.com/karpathy/nanochat)
- **对研发/工程启示（Karpathy 视角）**：将研究实验视为"可编程的自动化流水线"，不再手动修改 Python 而是编写 `program.md` 来指导 Agent。这种思路可迁移到产品开发中——让 AI Agent 成为"夜间值班的研究助手"，每天早上查看实验日志即可。

---

**17. 阿里巴巴与字节跳动计划订购华为 950PR AI 芯片**

- **核心做了什么（What happened）**：据 Reuters 报道，阿里巴巴和字节跳动在测试后计划订购华为新一代 950PR AI 芯片，该芯片展现出更好的 CUDA 兼容性。华为目标在 2026 年出货约 75 万颗 950PR。
- **启示 / To-dos**：
    - 中国 AI 芯片自主化进程加速，CUDA 兼容性是关键突破方向
    - 对全球 AI 芯片供应链格局的潜在影响
    - NVIDIA 在中国市场的替代风险持续上升
- **正面**：降低中国 AI 产业对美国芯片的依赖；竞争促进创新
- **负面 / 风险**：性能差距可能仍然存在；地缘政治风险加剧
- **原文链接**：[Reuters 报道](https://www.reuters.com/technology/alibaba-bytedance-huawei-950pr-chip-2026-03-27/)

---

**18. NeurIPS 撤回针对受制裁机构的论文禁令，回应中国学者抗议**

- **核心做了什么（What happened）**：NeurIPS 撤回了此前可能禁止受美国制裁实体研究人员提交论文的政策变更。该政策引发中国 AI 研究社区强烈反弹。NeurIPS 发表声明称理解社区关切并致歉。
- **启示 / To-dos**：
    - 学术出版与地缘政治的交叉点正在扩大
    - 国际 AI 研究合作面临的制度性风险在增加
    - 关注替代性学术平台与发表渠道的发展
- **正面**：维护学术开放性；回应社区诉求的速度较快
- **负面 / 风险**：政策不确定性已经造成伤害；"美国单边控制学术发表"的印象难以消除
- **原文链接**：[Reuters 报道](https://www.reuters.com/technology/neurips-reverses-sanctions-policy-2026-03-27/)
- **补充链接**：[Wired：AI 研究越来越难与地缘政治分离](https://www.wired.com/story/ai-research-geopolitics-neurips/)

---

**19. Moonshot AI 拟放弃开曼架构，筹备港交所 IPO（估值约 $180 亿）**

- **核心做了什么（What happened）**：据 WSJ 报道，月之暗面（Moonshot AI）可能放弃其开曼群岛控股结构，改为中国或香港实体，以准备港交所 IPO。同时计划以约 $180 亿估值进行新一轮融资。
- **启示 / To-dos**：
    - 中国 AI 公司的上市路径正在从美股转向港股
    - $180 亿估值反映了中国 AI 赛道的资本热度
    - 关注 Moonshot 的 Kimi 系列模型（此前 K2.5 发布 1T 参数 MoE）在港股市场的表现
- **正面**：为中国 AI 公司提供新的资本退出渠道；港交所 AI 生态扩容
- **负面 / 风险**：架构重组的法律与税务复杂性；中美 AI 脱钩趋势加剧
- **原文链接**：[Wall Street Journal 报道](https://www.wsj.com/articles/moonshot-ai-hong-kong-ipo-2026-03)

---

**20. Telnyx PyPI 包被投毒：AI 供应链安全再敲警钟**

- **核心做了什么（What happened）**：Python 包管理器 PyPI 上的 Telnyx 包遭到供应链攻击，恶意代码被注入官方包中。此事件与此前 LiteLLM 供应链攻击（HN 热门讨论）同属近期 AI/ML 工具链安全事件。Cursor 的 Composer 同期通过实时 RL 改进编码质量。
- **启示 / To-dos**：
    - AI/ML 供应链安全已成高优先级议题
    - 使用包管理器的锁文件（lockfile）与校验和验证
    - 建立内部包镜像与安全审计流程
    - 评估"软件包冷却期"（package cooldown）策略
- **正面**：社区快速发现与响应；安全意识在提升
- **负面 / 风险**：AI 工具链的依赖链条极长，攻击面持续扩大；自动化部署放大了风险
- **原文链接**：[Telnyx 安全公告](https://telnyx.com/blog/pypi-compromise-2026)
- **补充链接**：[HN 讨论](https://news.ycombinator.com/item?id=47513475)

---

## ✅ 质量自检

- [x]  **满 20 条且去重**
- [x]  **每条均有可跳转原文链接**
- [x]  **突出"核心做了什么 + 启示"，无冗长翻译或空泛表述**
- [x]  **每条均提供正面/负面两类评价（至少各 1 点）**
- [x]  **Karpathy 动态已优先收录并增加"Karpathy 视角启示"**（第 16 条）