---
title: "NSA无视黑名单使用Mythos引爆政策博弈，Vercel遭AI工具链供应链攻击，"
description: "1. **NSA 无视五角大楼黑名单使用 Anthropic Mythos，政策博弈白热化**"
date: "2026-04-20"
category: "每日科技日报"
---

# 20260420 NSA无视黑名单使用Mythos引爆政策博弈，Vercel遭AI工具链供应链攻击，全球RAM荒冲击消费电子与AI基建

Owner: 每日新闻抓取器
Last edited time: 2026年4月20日 10:01

### 每日科技快讯（AI 方向）

#### 2026-04-20｜今日 20 条

1. **NSA 无视五角大楼黑名单使用 Anthropic Mythos，政策博弈白热化**
    - **核心做了什么（What happened）**：Axios 独家报道，NSA 正在使用 Anthropic 的 Mythos Preview 模型，且消息称该模型已在美国国防部内部广泛使用——尽管五角大楼此前已将 Anthropic 列为供应链风险。与此同时，白宫与 Anthropic CEO Amodei 举行了"富有成效的"会晤，双方寻求妥协。
    - **启示 / To-dos**：
        - 关注前沿 AI 在国家安全场景的部署边界与合规路径
        - "供应链风险"标签与实际使用的脱节，暴露政策制定滞后于技术采用速度
        - 对企业级 AI 部署需关注政府合规动态对供应商选择的影响
    - **正面**：Mythos 的网安能力如此突出，以至于安全机构不惜绕过政策限制——说明其技术壁垒确实领先；白宫主动对话意味着监管走向务实
    - **负面 / 风险**：政策执行力受损，若 NSA 可绕过黑名单，其他机构是否效仿？Anthropic 的政治风险未消除；约 18 个未公开组织已获 Mythos 访问权，透明度堪忧
    - **原文链接**：[Axios: NSA using Anthropic's Mythos despite blacklist](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon)
    - **补充链接**：[NYT: White House and Anthropic Hold 'Productive' Meeting](https://www.nytimes.com/2026/04/17/technology/white-house-anthropic-artificial-intelligence.html)
2. **Vercel 遭 ShinyHunters 入侵：AI 工具 [Context.ai](http://Context.ai) 成供应链攻击入口**
    - **核心做了什么（What happened）**：云开发平台 Vercel 确认遭安全入侵。攻击者通过一名员工使用的第三方 AI 工具 [Context.ai](http://Context.ai) 的 Google Workspace OAuth 应用被攻破，逐步升级权限，访问了 Vercel 内部系统。ShinyHunters 在暗网以 200 万美元出售包括 NPM token、GitHub token 在内的数据。
    - **启示 / To-dos**：
        - AI 工具链已成为新型供应链攻击面——所有使用第三方 AI 工具的团队需立即审计 OAuth 权限
        - Vercel CEO Rauch 指出攻击者"显著被 AI 加速"，说明 AI 既是被攻击面，也是攻击工具
        - 企业需将 AI 工具纳入零信任安全策略
    - **正面**：Vercel 快速披露事件并发布 IOC（攻击指标），有利于社区防御
    - **负面 / 风险**：Next.js 周下载量 600 万，一次恶意推送即可造成全球供应链攻击；OAuth 权限链传播风险被严重低估
    - **原文链接**：[Vercel April 2026 security incident](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)
    - **补充链接**：[BleepingComputer: Vercel confirms breach](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/)
3. **全球 RAM 荒可能持续数年，AI 需求挤压消费电子**
    - **核心做了什么（What happened）**：The Verge 报道 RAM 短缺可能持续数年。SemiAnalysis 的 Dylan Patel 在 Dwarkesh Podcast 中预测手机市场今年可能因 RAM 价格缩水 50%。Jeff Geerling 指出 DRAM 价格正在杀死爱好者 SBC 市场。HBM（高带宽内存）被 AI 数据中心大量吸收，消费级 DRAM 产能被挤压。
    - **启示 / To-dos**：
        - AI 基建对内存的巨量需求正在重塑全球半导体供应链
        - 关注 TurboQuant 等内存压缩技术——Google 的 6 倍压缩算法若落地可缓解部分压力
        - 端侧 AI 部署需更关注内存效率优化
    - **正面**：内存厂商利润丰厚，长期将激励扩产；压力倒逼更高效的量化与压缩方案
    - **负面 / 风险**：消费者承受成本转嫁；Apple Mac Studio 和触屏 MacBook Pro 因内存短缺推迟发布；产能扩张周期长达数年
    - **原文链接**：[The Verge: The RAM shortage could last years](https://www.theverge.com/ai-artificial-intelligence/914672/the-ram-shortage-could-last-years)
    - **补充链接**：[Jeff Geerling: DRAM pricing is killing the hobbyist SBC market](https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/)
4. **Apple WWDC 2026 预告暗示 iOS 27 Siri 大改，内存短缺推迟 Mac 发布**
    - **核心做了什么（What happened）**：Bloomberg Gurman 报道 WWDC 2026 邀请函中的发光"26"暗示全新 Siri 界面将随 iOS 27 发布。同时因内存短缺，M5 Ultra Mac Studio 推迟至约十月，触屏 MacBook Pro 可能延至 2026 年末至 2027 年初。
    - **启示 / To-dos**：
        - Apple 的 AI 战略核心仍是 Siri——与 Google Gemini 的合作能否带来质变值得关注
        - 内存短缺对硬件发布节奏的影响开始实质化
        - 关注 iOS 27 作为 Agent 入口的可能性
    - **正面**：Apple 终于正面回应 AI 竞争，Siri 有望获得实质性升级
    - **负面 / 风险**：Apple AI 策略已落后竞争对手近两年；硬件延迟削弱产品周期
    - **原文链接**：[Bloomberg: Apple WWDC 2026 teases revamped Siri in iOS 27](https://www.bloomberg.com/news/newsletters/2026-04-19/apple-ios-27-siri-interface-ios-27-details-mac-studio-touch-macbook-release-mo5u23o7)
5. **Claude Opus 4.7 系统提示差异曝光：推理成本降半但上下文召回严重回退**
    - **核心做了什么（What happened）**：Simon Willison 详细对比了 Claude Opus 4.6 与 4.7 的系统提示变化。社区发现 Opus 4.7 的新 tokenizer 导致相同输入消耗约 1.35 倍 token；MRCR v2 基准上下文召回率从 256K 的 91.9% 降至 59.2%（1M 从 78.3% 降至 32.2%）。推理成本从 4.6 到 4.7 几乎减半，但代价是能力回退。
    - **启示 / To-dos**：
        - 模型升级不等于全面进步——需在自有基准上做回归测试
        - 4.7 的 adaptive thinking 成为唯一模式，无法禁用，对依赖精确控制的用户是重大变化
        - 长上下文场景需谨慎评估是否升级
    - **正面**：推理成本降低有利于降本；Willison 的分析推动透明度
    - **负面 / 风险**：上下文召回大幅退化；tokenizer 变化导致配额超支；静默升级中途切换模型引发信任危机
    - **原文链接**：[Simon Willison: Changes in the system prompt between Claude Opus 4.6 and 4.7](https://simonwillison.net/2026/Apr/18/opus-system-prompt/)
6. **Anthropic Mythos 加剧开源维护者负担：Bloomberg 调查报告**
    - **核心做了什么（What happened）**：Bloomberg 记者 Chris Stokel-Walker 报道，Anthropic 的 Mythos 发现漏洞速度远超开源维护者修复能力，大量 bug 报告涌入开源项目（如 Ruby Central 因此陷入"真正的财务危机"）。这与 Anthropic Project Glasswing 用 Mythos 修复漏洞的承诺形成讽刺对比。
    - **启示 / To-dos**：
        - AI 漏洞发现能力的不对称性正在成为系统性风险
        - 开源社区需要新的资金和资源模型来应对 AI 驱动的漏洞洪流
        - 企业应评估自身依赖的开源项目是否有能力消化 AI 发现的漏洞
    - **正面**：加速漏洞发现本身有利于安全；倒逼开源治理升级
    - **负面 / 风险**：发现速度远超修复速度，实质上暴露了更多未修补的攻击面
    - **原文链接**：[Bloomberg: Anthropic's Mythos adds strain on cybersecurity teams](https://www.bloomberg.com/news/articles/2026-04-17/anthropic-s-mythos-adds-strain-on-cybersecurity-teams-facing-ai-threats)
7. **Claude 3 Haiku 今日正式退役，API 请求将失败**
    - **核心做了什么（What happened）**：Anthropic 的 Claude 3 Haiku（`claude-3-haiku-20240307`）于 2026 年 4 月 20 日到达退役日期，此后 API 请求将失败。官方迁移目标为 Claude Haiku 4.5（`claude-haiku-4-5-20251001`），但价格从 $0.25/$1.25 升至 $1.00/$5.00 每百万 token（4 倍涨价）。
    - **启示 / To-dos**：
        - 所有仍在使用 Claude 3 Haiku 的产品需立即完成迁移
        - 4 倍价格涨幅需重新评估成本模型
        - 提醒关注 Claude 3.7 Sonnet 将于 5 月 11 日退役
    - **正面**：Haiku 4.5 能力远超前代，单位性价比仍可能更优
    - **负面 / 风险**：依赖旧模型的服务今日即中断；价格跳升对小团队冲击大
    - **原文链接**：[Anthropic model deprecations page](https://platform.claude.com/docs/en/about-claude/model-deprecations)
8. **Karpathy 的 LLM Wiki 模式爆红：个人知识库的新范式**
    - **核心做了什么（What happened）**：Andrej Karpathy 在 GitHub Gist 发布的"LLM Wiki"概念在数日内获得 5000+ star。核心思想：让 LLM 持续维护一个结构化、交叉引用的个人 Wiki，而非每次查询都从零开始 RAG 检索。社区已涌现多个实现（如 MehmetGoekce/llm-wiki、Astro-Han/karpathy-llm-wiki 等 Agent Skill）。
    - **启示 / To-dos**：
        - "知识积累型 LLM"比"即时检索型 RAG"可能是更好的长期知识管理范式
        - 值得在团队/个人工作流中实验 LLM Wiki 模式
        - 关注两层缓存架构（L1/L2）的实现细节
    - **正面**：概念简洁、可复用性强，与 Claude Code/Codex 等工具天然集成
    - **负面 / 风险**：大规模 wiki 的一致性维护仍是挑战；依赖 LLM 质量
    - **原文链接**：[Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
    - **对研发/工程启示（Karpathy 视角）**：把知识管理从"被动检索"转向"主动编纂"，让 LLM 作为持续迭代的编辑器而非一次性问答机，是提升个人与团队知识复利的关键路径
9. **SemiAnalysis 预计 2026 年营收破 1 亿美元：AI 研究型媒体崛起**
    - **核心做了什么（What happened）**：Techmeme 报道 Dylan Patel 创立的 SemiAnalysis——一家 AI 通讯与研究公司——预计 2026 年从订阅和 AI 供应链研究中获得超 1 亿美元收入。此前已传出 SemiAnalysis 正在与投资者洽谈数亿美元的 VC 基金。
    - **启示 / To-dos**：
        - AI 行业信息不对称催生新型研究服务商——深度技术分析本身成为高价值业务
        - 对 AI 供应链的深入理解正在成为关键竞争力
    - **正面**：证明高质量技术研究有巨大市场需求
    - **负面 / 风险**：SemiAnalysis 创始人与 Anthropic RL 技术负责人 Sholto 是室友——潜在利益冲突需关注
    - **原文链接**：[Techmeme: SemiAnalysis expects $100M+ in 2026 revenue](https://www.techmeme.com/260419/p2)
10. **溴化物瓶颈：中东局势可能中断全球内存芯片生产**
    - **核心做了什么（What happened）**：War on the Rocks 刊文分析"溴化物卡点"——中东局势可能影响溴化物供应，而溴化物是 DRAM 生产中的关键化学品。这一供应链风险叠加 AI 对 HBM 的巨大需求，可能进一步加剧全球内存短缺。
    - **启示 / To-dos**：
        - AI 基建的脆弱性不仅在芯片制造端，也在上游化工原料端
        - 企业需关注半导体供应链中的非直觉瓶颈
    - **正面**：提前预警有利于企业做供应链风险管理
    - **负面 / 风险**：地缘政治风险向技术产业的传导路径越来越短且不可预测
    - **原文链接**：[War on the Rocks: The Bromine Chokepoint](https://warontherocks.com/cogs-of-war/the-bromine-chokepoint-how-strife-in-the-middle-east-could-halt-production-of-the-worlds-memory-chips/)
11. **Anthropic Mythos 产能瓶颈：FT 报道暂缓更广泛发布**
    - **核心做了什么（What happened）**：FT 消息称 Anthropic 正在推迟 Mythos 的更广泛发布，直到能可靠地为客户提供服务。近几周 Anthropic 遭遇了多次服务中断。目前约 30 个组织（含约 18 个未公开）获得了 Mythos 的受限访问。
    - **启示 / To-dos**：
        - 前沿模型的可用性受算力/推理成本约束——"能做"与"能规模化服务"之间鸿沟巨大
        - 关注 Anthropic 的基础设施扩容节奏
    - **正面**：审慎发布体现负责任的产品化态度
    - **负面 / 风险**：产能不足直接限制商业化节奏，竞争对手有窗口期
    - **原文链接**：[FT: Anthropic holding off from wider Mythos release](https://www.ft.com/content/c9f5b690-a10e-4c66-9245-017f8bfbc7b4)
12. **ElevenLabs 发布 ElevenAgents：70+ 语言超低延迟 Expressive Mode 语音 AI**
    - **核心做了什么（What happened）**：ElevenLabs 推出 ElevenAgents，主打 Expressive Mode——号称最拟人的 AI 语音技术，支持 70 多种语言，超低延迟。SDK 覆盖 TypeScript、Swift、Android、Flutter、React Native 等全平台，支持 MCP 协议。
    - **启示 / To-dos**：
        - 语音 AI Agent 正在从实验走向全平台生产化
        - MCP 协议集成意味着语音 Agent 可接入更广泛的工具生态
        - 关注"情感表达"能力对客服、教育等场景的影响
    - **正面**：全平台覆盖 + 低延迟 + 多语言，商业落地门槛大幅降低
    - **负面 / 风险**：拟人语音加深 deepfake 风险；定价与配额模型待观察
    - **原文链接**：[ElevenLabs ElevenAgents SDK](https://github.com/elevenlabs/packages)
13. **微软开源 Agent Governance Toolkit：首个覆盖 OWASP 十大 Agent 风险的运行时安全框架**
    - **核心做了什么（What happened）**：微软发布 Agent Governance Toolkit（MIT 许可），号称首个覆盖 OWASP 2026 年 Agentic AI 十大风险（目标劫持、工具滥用、身份滥用、内存投毒、级联故障、失控 Agent 等）的确定性策略执行工具包。支持亚毫秒级策略执行，兼容现有 Agent 框架。
    - **启示 / To-dos**：
        - Agent 安全治理从"事后补丁"走向"运行时内嵌"——新项目应从第一天就集成
        - OWASP Agentic AI Top 10 值得作为 Agent 开发的安全检查清单
        - EU AI Act 高风险 AI 义务将于 2026 年 8 月生效——合规需求迫切
    - **正面**：开源 + MIT 许可 + 框架无关，降低采用门槛
    - **负面 / 风险**：早期项目成熟度待验证；需要持续的社区贡献与维护
    - **原文链接**：[Microsoft: Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)
14. **Palantir 发布 22 条"技术共和国"宣言：引发硅谷激烈争论**
    - **核心做了什么（What happened）**：Palantir 在 X 发布其 CEO Alex Karp 著作《The Technological Republic》的 22 条摘要，主张硅谷对国防负有道德义务、呼吁考虑恢复征兵制、推崇硬实力与 AI 武器。从 Yanis Varoufakis 到 Peter Thiel 的支持者，各界反应极其两极化。
    - **启示 / To-dos**：
        - AI 公司的政治化表态正在重塑科技行业的公共形象与监管预期
        - 关注 Palantir 在国防/情报领域的实质影响力——其客户包括 ICE、DoD、NHS
    - **正面**：推动了关于技术与国家安全关系的公开讨论
    - **负面 / 风险**：企业直接发布政治宣言模糊了商业与政治边界；对多元主义的批评引发广泛担忧
    - **原文链接**：[TechCrunch: Palantir posts mini-manifesto](https://techcrunch.com/2026/04/19/palantir-posts-mini-manifesto-denouncing-regressive-and-harmful-cultures/)
15. **Apple Silicon 上的 WebAssembly Zero-Copy GPU 推理突破**
    - **核心做了什么（What happened）**：[abacusnoir.com](http://abacusnoir.com) 发布技术文章，展示在 Apple Silicon 上通过 WebAssembly 实现零拷贝 GPU 推理，消除 CPU-GPU 间的数据传输开销。
    - **启示 / To-dos**：
        - 对端侧 AI 推理的性能瓶颈提供了新的优化路径
        - WebAssembly + Metal 的组合可能成为跨平台端侧推理的重要技术栈
    - **正面**：降低端侧推理延迟与能耗
    - **负面 / 风险**：仅限 Apple Silicon 平台；生产环境成熟度待验证
    - **原文链接**：[Zero-Copy GPU Inference from WebAssembly on Apple Silicon](https://abacusnoir.com/2026/04/18/zero-copy-gpu-inference-from-webassembly-on-apple-silicon/)
16. **Kelp DAO 遭 2.92 亿美元攻击：2026 年最大 DeFi 漏洞利用**
    - **核心做了什么（What happened）**：攻击者利用 Kelp DAO 的 LayerZero 跨链桥漏洞，在不到一小时内抽走约 116,500 rsETH（价值约 2.92 亿美元）。引发 Aave 流动性危机，62 亿美元资金紧急撤出。AAVE 代币暴跌 10%，LayerZero ZRO 代币跌 18%。
    - **启示 / To-dos**：
        - 跨链桥仍是 DeFi 安全最薄弱环节
        - AI 驱动的安全审计对跨链协议尤为紧迫
        - 级联风险（从单一协议到整个 DeFi 生态）需要系统性防御
    - **正面**：事件推动行业重新审视桥接协议安全标准
    - **负面 / 风险**：Aave 面临超 2 亿美元坏账；DeFi 用户信心再受打击
    - **原文链接**：[The Block: Kelp DAO's rsETH bridge exploited for $292M](https://www.theblock.co/post/397988/kelp-daos-rseth-bridge-apparently-exploited-for-roughly-292-million-in-layerzero-based-attack)
17. **创意软件行业向 Adobe 宣战：免费工具竞争加剧**
    - **核心做了什么（What happened）**：The Verge 报道创意软件行业正在掀起一场反 Adobe 浪潮，多家竞争者推出免费或低价替代品。AI 驱动的设计工具（包括 Anthropic 的 Claude Design、Adobe 自身的 AI Agent、Canva 等）正在重新定义设计工作流。
    - **启示 / To-dos**：
        - AI 正在降低创意工具的进入门槛，打破 Adobe 垄断
        - 关注 Claude Design、Google Stitch 等 AI-native 设计工具的发展
    - **正面**：竞争加剧有利于创作者；AI 能力嵌入设计流程
    - **负面 / 风险**：设计质量与"vibe-coded slop"的界限模糊；专业设计师价值可能被低估
    - **原文链接**：[The Verge: The creative software industry has declared war on Adobe](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates)
18. **Meta 从开放权重路线转向：[DeepLearning.AI](http://DeepLearning.AI) 最新分析**
    - **核心做了什么（What happened）**：[DeepLearning.AI](http://DeepLearning.AI) The Batch 最新一期分析 Meta 正从开放权重策略转向。此前 Meta 开源了 Llama 系列，但最近迹象显示其可能调整策略，这将对开源 AI 生态产生重大影响。
    - **启示 / To-dos**：
        - 对依赖 Llama 系列模型的团队需做好供应商多元化准备
        - 关注 Qwen、Gemma 等替代开源选项
        - "开放权重"与"真正开源"的区别在 2026 年变得更加关键
    - **正面**：Meta 的商业化压力可以理解；其他开源力量（Google Gemma、阿里 Qwen）正在补位
    - **负面 / 风险**：AI 生态开放度可能整体收缩；对学术研究与创业公司的影响最大
    - **原文链接**：[DeepLearning.AI](http://DeepLearning.AI) [The Batch: Meta Pivots From Open Weights](https://www.deeplearning.ai/the-batch/)
19. **Gemma 4 浏览器端 Demo：Prompt-to-Excalidraw 仅需 3.1GB**
    - **核心做了什么（What happened）**：Hacker News Show HN 项目展示在浏览器中运行 Gemma 4 E2B（仅 3.1GB），实现从自然语言 prompt 直接生成 Excalidraw 图表。这是端侧 AI 能力的又一个实用案例。
    - **启示 / To-dos**：
        - 浏览器内运行 3B+ 参数模型的实用性已初步验证
        - 对需要离线/隐私保护的图表生成场景有直接价值
        - WebGPU/WebAssembly 的端侧推理生态正在成形
    - **正面**：无需后端、零延迟网络开销、数据不出浏览器
    - **负面 / 风险**：3.1GB 下载对移动端仍偏大；生成质量与云端模型有差距
    - **原文链接**：[Show HN: Prompt-to-Excalidraw with Gemma 4 in browser](https://teamchong.github.io/turboquant-wasm/draw.html)
20. **Claude Opus 4.7 过度拒绝回退：计算结构生物学标准任务被错误标记违规**
    - **核心做了什么（What happened）**：GitHub issue 反馈 Claude Opus 4.7 将标准的计算结构生物学任务（如对已发表 PDB 结构进行表位映射和 motif 脚手架设计）错误地标记为使用政策违规并拒绝执行，而同样的任务在 4.6 上正常运行。这是 4.7 安全过滤器过度敏感的又一例证。
    - **启示 / To-dos**：
        - 模型安全过滤需要更精细的领域感知——科学研究场景不应被过度限制
        - 升级前需用专业领域测试集做回归测试
        - 关注 Anthropic 是否会调整 4.7 的安全阈值
    - **正面**：社区反馈推动 Anthropic 改进安全策略的精确度
    - **负面 / 风险**：过度拒绝实质上降低了模型对科研用户的可用性；信任成本累积
    - **原文链接**：[GitHub: Opus 4.7 flags standard computational structural biology as Usage Policy violation](https://github.com/anthropics/claude-code/issues/49751)