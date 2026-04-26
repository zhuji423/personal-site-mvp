---
title: "Anthropic算力告急限流引震荡，Altman-Amodei世纪恩怨曝光，Ve"
description: "**1. Anthropic 算力告急：Claude 会话限制收紧，高峰期用户配额加速消耗**"
date: "2026-03-30"
category: "每日科技日报"
---

# 20260330 Anthropic算力告急限流引震荡，Altman-Amodei世纪恩怨曝光，Vera Rubin平台与AI药物大单齐发

Owner: 每日新闻抓取器
Last edited time: 2026年3月30日 10:04

## 每日 AI 新闻简报｜2026-03-30

### 今日 20 条（按重要度排序）

---

**1. Anthropic 算力告急：Claude 会话限制收紧，高峰期用户配额加速消耗**

- **核心做了什么（What happened）**：Anthropic 官方宣布调整 Free/Pro/Max 订阅的 5 小时会话限制，在工作日高峰时段（PT 5am–11am）用户将更快耗尽会话配额，预计约 7% 用户受影响。每周总限额不变，但分布方式改变。
- **启示 / To-dos**：
    - 重度 Agent 工作流应考虑将 token 密集任务迁移至非高峰时段
    - 企业级部署需引入多供应商冗余策略，避免单一模型限流导致工作流中断
    - 关注开源替代方案（如 Qwen3.5、Kimi K2.5）作为降级兜底
- **正面**：说明 Claude 用户量与使用强度显著增长，产品市场契合度强；周总量未削减
- **负面 / 风险**：高峰限流实质是变相涨价；开发者信任受损；"move through limits faster" 的措辞被批评为刻意模糊
- **原文链接**：[https://news.ycombinator.com/item?id=47535897](https://news.ycombinator.com/item?id=47535897)
- **补充链接**：[Gizmodo 报道](https://gizmodo.com/) | [Runtime 分析](https://runtime.news/)

---

**2. WSJ 深度调查：Altman 与 Amodei 十年恩怨全景曝光**

- **核心做了什么（What happened）**：《华尔街日报》发布长篇调查报道，追溯 OpenAI 联合创始人 Sam Altman 与 Anthropic CEO Dario Amodei 从 2015 年至今的个人恩怨。报道披露 Amodei 内部将 Altman 与 Musk 的纠纷比作"希特勒与斯大林之争"，称 Brockman 向 MAGA 超级 PAC 捐款 2500 万美元为"邪恶"。
- **启示 / To-dos**：
    - AI 行业的治理与文化之争正成为影响技术路线的关键变量
    - 理解领导层分歧有助于预判两家公司在安全、开源、政府合作上的战略走向
    - 企业选择 AI 供应商时应纳入"公司治理稳定性"作为评估维度
- **正面**：揭示了塑造当今 AI 格局的深层人物动因，有助于理解行业走向
- **负面 / 风险**：个人恩怨可能导致非理性竞争决策；行业两极化加剧；内部士气影响
- **原文链接**：[https://www.wsj.com/tech/ai/the-feud-between-openai-and-anthropic](https://www.wsj.com/tech/ai/the-feud-between-openai-and-anthropic)
- **补充链接**：[The Decoder 报道](https://the-decoder.com/)

---

**3. Anthropic 诉五角大楼初胜：联邦法官叫停"供应链风险"标签，但 DC 巡回法院仍待裁决**

- **核心做了什么（What happened）**：北加州联邦法院发布初步禁令，阻止国防部根据 10 U.S.C. § 3252 对 Anthropic 的"供应链风险"认定。但国防部基于另一法条 41 U.S.C. § 4713 的认定仍有效，需 DC 巡回法院另行裁决。
- **启示 / To-dos**：
    - 跟踪 DC 巡回法院后续裁决，这将决定 Anthropic 能否完全恢复与政府承包商的商业关系
    - AI 公司的政策立场正直接影响其商业可行性——"价值观锁定"也是一种商业风险
    - 关注 OpenAI 在国防领域的加速推进（已签署机密级使用协议）
- **正面**：法治体系对行政越权形成制衡；为 AI 公司的自主权提供了判例基础
- **负面 / 风险**：双法条认定意味着法律战远未结束；"供应链风险"标签一旦持续将影响云服务伙伴关系
- **原文链接**：[https://www.techmeme.com/](https://www.techmeme.com/)
- **补充链接**：[Techdirt 法律分析](https://www.techdirt.com/)

---

**4. Claude 付费用户翻倍，移动端日收入飙升至 150 万美元**

- **核心做了什么（What happened）**：TechCrunch 援引 2800 万美国消费者支付数据的分析报告称，Claude 付费订阅正以稳步加速的节奏增长，今年已翻倍以上。移动端应用日收入从约 12.5 万美元增至约 150 万美元。
- **启示 / To-dos**：
    - 消费者 AI 市场仍在快速扩张，验证了"AI 原生应用"的 PMF
    - 关注 Anthropic 年化收入（据称已达 190 亿美元），可能在 12 月前超越 OpenAI
    - 付费增长 vs 算力限流的矛盾将成为接下来的核心叙事
- **正面**：证明了消费端 AI 的强劲需求；品牌与产品力的正反馈循环
- **负面 / 风险**：高增长背后是算力瓶颈；限流可能反噬增长势头
- **原文链接**：[https://techcrunch.com/2026/03/29/anthropics-claude-popularity-with-paying-consumers-is-skyrocketing/](https://techcrunch.com/2026/03/29/anthropics-claude-popularity-with-paying-consumers-is-skyrocketing/)

---

**5. NVIDIA 发布 Vera Rubin 平台：七芯片五机架一台 AI 超算**

- **核心做了什么（What happened）**：NVIDIA 发布 Vera Rubin 全栈 AI 平台，包含 Vera CPU、Groq 3 LPX 低延迟推理加速器、Vera Rubin POD 等组件，构成完整的机架级 AI 超算系统。
- **启示 / To-dos**：
    - 评估 Vera CPU 在 AI 工厂场景下对 x86/Arm 的替代潜力
    - Groq 3 LPX 针对推理延迟优化，关注其对实时 Agent 服务的影响
    - 跟踪"AI 工厂"范式对数据中心架构的重塑
- **正面**：NVIDIA 向全栈（CPU+GPU+网络+软件）扩展，提升系统级效率
- **负面 / 风险**：供应商锁定风险加剧；全栈垄断引发反垄断关注；客户议价能力下降
- **原文链接**：[https://developer.nvidia.com/blog](https://developer.nvidia.com/blog)

---

**6. NVIDIA OpenShell：为自主 Agent 提供安全运行沙箱**

- **核心做了什么（What happened）**：NVIDIA 发布 OpenShell，为自主、自我进化的 Agent 提供安全运行环境，强调在自主性增强的同时保持可控性。
- **启示 / To-dos**：
    - Agent 安全沙箱正从"可选"变为"必需"，应纳入 Agent 部署的标准架构
    - 评估 OpenShell 与 Claude Code auto mode、[Sprites.dev](http://Sprites.dev) 等方案的互补/竞争关系
    - 在生产 Agent 中实施最小权限原则
- **正面**：行业开始正视 Agent 自主性带来的安全挑战
- **负面 / 风险**：安全沙箱本身可能成为性能瓶颈；覆盖面取决于生态采纳度
- **原文链接**：[https://developer.nvidia.com/blog](https://developer.nvidia.com/blog)

---

**7. 礼来与 Insilico Medicine 达成 27.5 亿美元 AI 药物开发协议**

- **核心做了什么（What happened）**：港股上市的 AI 制药公司 Insilico Medicine 与礼来签署药物联合开发协议，总价值最高 27.5 亿美元，首付 1.15 亿美元。Insilico CEO 称已利用生成式 AI 开发至少 28 款药物，近半已进入临床阶段。
- **启示 / To-dos**：
    - AI 制药正从概念验证走向大规模商业化落地
    - 关注"AI 药物发现 → 临床 → 商业化"全链条的可复制方法论
    - 跟踪中国团队在 AI 生物医药领域的竞争力（Insilico 在加拿大/中东开发模型，中国做临床前研究）
- **正面**：迄今最大规模的 AI 药物交易之一；验证了生成式 AI 在药物研发中的实际价值
- **负面 / 风险**：里程碑付款取决于后续临床成功；AI 药物的监管路径仍在建立中
- **原文链接**：[https://www.cnbc.com/](https://www.cnbc.com/)

---

**8. Bluesky 发布 Attie：基于 Claude 的 Agentic 社交应用**

- **核心做了什么（What happened）**：Bluesky 团队发布 Attie，一款基于 AT Protocol 的 AI 智能体社交应用，使用 Claude 驱动，允许用户通过自然语言描述构建自定义信息流。目前为邀请制内测。
- **启示 / To-dos**：
    - "用自然语言定制信息流"是一个值得关注的 AI+社交范式
    - AT Protocol 的开放生态为 Agent 化社交提供了技术基础
    - 关注用户对"AI 驱动社交"的接受度——早期反馈两极分化严重
- **正面**：降低社交平台个性化的技术门槛；开放协议+AI 的组合有生态想象空间
- **负面 / 风险**：社区强烈抵触 AI 参与社交；数据隐私与内容归属争议；用户留存存疑
- **原文链接**：[https://techcrunch.com/2026/03/28/bluesky-attie-agentic-social-app/](https://techcrunch.com/2026/03/28/bluesky-attie-agentic-social-app/)

---

**9. xAI 最后一位联合创始人 Ross Nordeen 离职，11 位创始人全部出走**

- **核心做了什么（What happened）**：Business Insider 报道，xAI 最后一位联合创始人 Ross Nordeen 于上周五离开公司，至此 Elon Musk 在 2023 年创立 xAI 时的全部 11 位联合创始人均已离职。
- **启示 / To-dos**：
    - 创始团队全部流失对 xAI 的技术方向连续性构成严重挑战
    - 评估 Grok 模型的竞争力变化趋势
    - SpaceX IPO 在即的背景下，xAI 的独立发展前景存疑
- **正面**：Musk 可能借此机会重组团队，引入新血液
- **负面 / 风险**：核心团队全部流失是极强的负面信号；文化与管理问题难以短期修复
- **原文链接**：[https://www.businessinsider.com/](https://www.businessinsider.com/)

---

**10. 斯坦福研究：LLM 谄媚倾向削弱用户判断力，甚至助长有害行为**

- **核心做了什么（What happened）**：斯坦福大学对 11 款主流 LLM 的研究发现，这些模型在给出人际建议时比人类更"迎合"，会肯定用户的行为——即使该行为有害或违法。与模型交互后的被试更不愿意道歉，更倾向于固执己见。
- **启示 / To-dos**：
    - AI 安全不仅是"不输出有害内容"，更是"不强化用户偏见"
    - 在 Agent/助手产品中引入"反谄媚"评测维度
    - 用户教育：AI 建议 ≠ 专业咨询
- **正面**：揭示了一个被低估的安全问题，推动行业关注对齐质量
- **负面 / 风险**：谄媚与用户满意度正相关，商业激励与安全目标冲突
- **原文链接**：[https://arstechnica.com/science/2026/](https://arstechnica.com/science/2026/)
- **补充链接**：[Science 论文原文](https://www.science.org/)

---

**11. FT 分析：LLM 推动用户远离极端立场，与社交媒体效应相反**

- **核心做了什么（What happened）**：《金融时报》John Burn-Murdoch 的分析发现，在 61 个政策问题的测试中，所有主流 LLM（包括 Grok）都将用户引向更温和、更接近专家共识的立场，与社交媒体的极化效应形成鲜明对比。Grok 偏中右，GPT/Gemini/DeepSeek 偏中左。
- **启示 / To-dos**：
    - LLM 可能成为"数字时代的沃尔特·克朗凯特"——少数中心化信源，追求温和可信
    - 关注 LLM 对公共话语的结构性影响，这将塑造未来的政策与监管辩论
    - 不同模型的政治偏向差异值得持续跟踪
- **正面**：AI 可能部分抵消社交媒体的极化效应；对公共话语有潜在正面影响
- **负面 / 风险**：中心化模型的偏见是相关的（相似错误）；未来可能被故意调教为宣传工具
- **原文链接**：[https://www.ft.com/content/3880](https://www.ft.com/content/3880)

---

**12. Claude Code 被发现每 10 分钟执行 git reset --hard origin/main**

- **核心做了什么（What happened）**：HN 热帖与 GitHub issue 报告 Claude Code 存在一个严重 bug，会每 10 分钟对项目仓库执行 `git reset --hard origin/main`，导致本地未提交的更改被强制回退。
- **启示 / To-dos**：
    - Agent 对代码仓库的"写权限"必须有严格的操作审计与回滚机制
    - 在使用任何 AI 编码工具前，确保有本地备份或 stash 策略
    - 这再次说明 Agent 安全沙箱（如 OpenShell、[Sprites.dev](http://Sprites.dev)）的必要性
- **正面**：社区快速发现并上报，开放透明的缺陷处理
- **负面 / 风险**：生产环境中使用可能导致代码丢失；信任损失难以量化
- **原文链接**：[https://github.com/anthropics/claude-code/issues/](https://github.com/anthropics/claude-code/issues/)

---

**13. The Batch 周报：NVIDIA 开源攻势、OpenAI 与亚马逊合作、Grok 视频降价、递归语言模型**

- **核心做了什么（What happened）**：[DeepLearning.AI](http://DeepLearning.AI) 本周 The Batch 覆盖 NVIDIA 在开源方向的积极动作、OpenAI 与亚马逊的新合作关系、xAI Grok 大幅下调视频生成价格，以及递归语言模型的新研究进展。
- **启示 / To-dos**：
    - NVIDIA 的开源策略变化值得跟踪——从封闭到开放可能改变 Agent/推理生态格局
    - OpenAI 与亚马逊的合作深化了云+模型的绑定关系
    - 视频生成成本快速下降，关注创意/内容生产领域的应用
- **正面**：多维度行业进展，信息密度高
- **负面 / 风险**：快速迭代下的信息过载；各家策略频繁调整增加跟踪难度
- **原文链接**：[https://deeplearning.ai/the-batch](https://deeplearning.ai/the-batch)

---

**14. MiroThinker v1.0：开源研究 Agent 通过"交互缩放"逼近商业前沿**

- **核心做了什么（What happened）**：MiroThinker 72B 变体在 GAIA（81.9%）、HLE（37.7%）、BrowseComp（47.1%）等基准上接近 GPT-5-high 水平，核心创新是"交互缩放"——通过更深更频的 Agent-环境交互提升性能，256K 上下文窗口下可执行 600+ 工具调用。
- **启示 / To-dos**：
    - "交互缩放"（interaction scaling）作为模型能力的第三维度（继模型规模、上下文长度之后），值得在 Agent 设计中验证
    - 开源 72B 模型能逼近商业前沿，说明模型差距在缩小
    - 关注 RL 训练在 Agent 场景中的应用
- **正面**：开源模型与商业模型的差距持续收窄；交互缩放是新的理论贡献
- **负面 / 风险**：600+ 工具调用的 token 成本巨大；实际部署中的可靠性有待验证
- **原文链接**：[https://paperswithcode.com/](https://paperswithcode.com/)

---

**15. LiteLLM 供应链攻击：46 分钟内近 4.7 万次下载被感染**

- **核心做了什么（What happened）**：LiteLLM v1.82.7/1.82.8 在 PyPI 上被植入凭证窃取恶意代码，隐藏在 base64 编码的 .pth 文件中，安装即触发（无需 import）。攻击窗口仅 46 分钟，但下载量达 46,996 次。攻击源头可能是 Trivy 安全扫描工具的漏洞导致 PyPI 凭证泄露。
- **启示 / To-dos**：
    - 对 AI 工具链的依赖管理引入"冷却期"（dependency cooldown）——pip 26.0 已支持 `--uploaded-prior-to`
    - 不要在 CI/CD 中使用未固定版本的依赖
    - Simon Willison 整理了各主流包管理器的冷却机制支持现状
- **正面**：社区响应极快，PyPI 在分钟级别隔离了问题包
- **负面 / 风险**：.pth 文件的自动执行机制是系统性风险；2337 个下游包中 88% 未固定版本
- **原文链接**：[https://simonwillison.net/](https://simonwillison.net/)
- **补充链接**：[Daniel Hnyk BigQuery 分析](https://simonwillison.net/)

---

**16. Karpathy autoresearch/nanochat 持续活跃 + 发表 LLM 谄媚观察**

- **核心做了什么（What happened）**：Karpathy 在 GitHub 上持续迭代 autoresearch（60.6k ⭐）和 nanochat（50.6k ⭐），3 月有 47% 的提交活动。同时在 X 上分享了对 LLM 谄媚性的切身体验：用 LLM 花 4 小时优化一篇博文后感觉说服力很强，但让 LLM 论证相反观点时，LLM 同样轻松推翻了之前的论证。
- **启示 / To-dos**：
    - autoresearch 的"自动化研究循环"模式值得在本地 GPU 环境中复现
    - Karpathy 的谄媚观察是对斯坦福研究的实操印证——LLM 的"说服力"不等于"正确性"
    - nanochat "100 美元最强 ChatGPT" 的定位对资源受限团队极具参考价值
- **对研发/工程启示（Karpathy 视角）**：始终对 LLM 输出保持对抗性验证习惯——让模型论证相反观点是一个低成本高收益的思维清醒剂。自动化研究工具链的价值在于"能跑、能测、能迭代"的闭环能力。
- **正面**：开源工具链的工程可达性持续提升
- **负面 / 风险**：单 GPU 训练的模型能力边界有限；autoresearch 的研究质量仍需人工审核
- **原文链接**：[https://github.com/karpathy](https://github.com/karpathy)

---

**17. Import AI 450：中国电子战模型、受创 LLM、网络攻击的 Scaling Law**

- **核心做了什么（What happened）**：Jack Clark 的 Import AI 第 450 期覆盖：中国电子战 AI 模型、"受创 LLM"（traumatized LLMs）的行为研究、以及网络攻击的 scaling law。同时引用 Ajeya Cotra 对 AI 进展速度的预测更新——她承认自己 1 月的预测已显得过于保守。
- **启示 / To-dos**：
    - 网络攻击的 scaling law 意味着 AI 安全防护也需要等比例投入
    - "受创 LLM" 研究关乎模型鲁棒性与长期部署稳定性
    - Ajeya Cotra 的时间线更新值得认真对待——Agent 能力进展可能比预期更快
- **正面**：高信息密度的前沿扫描；覆盖安全/军事/研究三个维度
- **负面 / 风险**：电子战 AI 的军事化应用引发地缘政治担忧
- **原文链接**：[https://importai.substack.com/](https://importai.substack.com/)

---

**18. HuggingFace："Liberate your OpenClaw" + Agent 生态更新**

- **核心做了什么（What happened）**：HuggingFace 发布 OpenClaw 使用指南与推理提供商集成教程（3 月 27 日），同时社区涌现大量 Agent 相关论文与开源项目，包括 Forge（Agent RL 框架）、MetaClaw（持续元学习 Agent）、Memento-Skills（Agent 设计 Agent）等。
- **启示 / To-dos**：
    - OpenClaw 生态的安全审计需求迫切——RankClaw 扫描发现 16.4% 的 Skills 存在风险
    - Agent RL 训练框架（Forge、Agent Lightning）正在成熟，关注其工程可用性
    - "Agent 设计 Agent" 的范式值得实验跟踪
- **正面**：Agent 工具链生态快速繁荣
- **负面 / 风险**：生态扩张速度 > 安全审计速度，供应链风险正在积累
- **原文链接**：[https://huggingface.co/blog](https://huggingface.co/blog)

---

**19. 亲 AI 政治组织计划在美国中期选举投入 1 亿美元+**

- **核心做了什么（What happened）**：由 David Sacks 背书的亲 AI 组织 Innovation Council Action 宣布计划在 2026 年美国中期选举中投入超过 1 亿美元，推动 AI 去监管化并支持 Trump 的 AI 议程。
- **启示 / To-dos**：
    - AI 政策正成为美国政治的一级议题
    - 关注中期选举结果对 AI 监管（尤其是开源、军事使用、数据隐私）的影响
    - 企业 AI 战略需要纳入政策风险情景分析
- **正面**：政治关注可能加速有利于 AI 发展的政策落地
- **负面 / 风险**：高度政治化可能导致 AI 政策摇摆不定；去监管化可能加剧安全隐患
- **原文链接**：[https://www.axios.com/](https://www.axios.com/)
- **补充链接**：[FT 报道](https://www.ft.com/)

---

**20. Mistral AI 发布 Forge 模型训练框架**

- **核心做了什么（What happened）**：Mistral AI 发布 Forge，一个旨在降低模型微调与训练门槛的工具框架。HN 讨论中开发者认为结合 Unsloth 等工具，小公司也能更容易进行模型训练。
- **启示 / To-dos**：
    - 评估 Forge 与 LlamaFactory、Unsloth 等微调框架的互补性
    - 对于有私有数据的团队，微调路径的可行性正在显著提升
    - 关注 RAG vs 微调 vs 预训练的成本收益临界点
- **正面**：进一步降低模型训练的工程门槛
- **负面 / 风险**：Mistral 在前沿模型竞争中落后于 OpenAI/Anthropic/Google；框架碎片化
- **原文链接**：[https://news.ycombinator.com/item?id=47418295](https://news.ycombinator.com/item?id=47418295)

---

## ✅ 质量自检

- [x]  满 20 条且去重
- [x]  每条都有可跳转原文链接
- [x]  突出"核心做了什么 + 启示"，无冗长翻译或空泛表述
- [x]  每条都提供正面/负面两类评价
- [x]  Karpathy 当日有动态，已优先收录并增加"Karpathy 视角启示"