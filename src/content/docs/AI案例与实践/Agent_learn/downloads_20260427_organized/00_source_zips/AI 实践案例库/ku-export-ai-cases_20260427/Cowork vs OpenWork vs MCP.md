---
title: "ZFS 快照示例 - 像游戏存档一样"
description: "Cowork vs OpenWork vs MCP"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Cowork vs OpenWork vs MCP.md"
---
Cowork vs OpenWork vs MCP

#### 🧑‍🏫 案例作者：[@闫世锋](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：其他、通用
#### 🔧 使用工具：Claude
#### 📒 案例概要：本文档对比了Cowork、OpenWork和MCP三种AI工作流方案。Cowork是Anthropic推出的付费产品，强调通过虚拟机实现安全隔离；OpenWork是其开源替代，注重用户体验与权限控制；MCP是基于WebSocket的轻量级远程执行框架。结论指出MCP可借鉴Cowork的安全机制（如VM隔离、网络白名单）和OpenWork的用户体验设计（如GUI、权限审批），以增强安全性与易用性，向通用AI Agent标准发展。
## 结论摘要
### 一句话定位
|方案|一句话定位|本质|
|-|-|-|
|**Cowork**|Claude Code 的 GUI 版 + VM 级沙盒|把「终端里的 Claude」包装成「桌面上的助手」，用 VM 隔离解决安全问题|
|**OpenWork**|Cowork 的开源平替 + 多模型支持|复刻 Cowork 的产品形态，去掉 Claude 绑定，换成权限审批做安全|
|**MCP**|纯协议层，无 UI、无沙盒|只定义「AI 怎么调用工具」，其他全靠自己建|

### MCP 方案可借鉴的关键改进方向
|优先级|借鉴来源|改进方向|
|-|-|-|
|🔴 高|Cowork|增加 **VM/容器级隔离**，而非直接在宿主机执行|
|🔴 高|Cowork|增加 **网络白名单** 机制，限制外部访问|
|🔴 高|Cowork|增加 **文件系统快照**，支持操作回滚|
|🟡 中|OpenWork|增加 **权限审批弹窗**，敏感操作需用户确认|
|🟡 中|OpenWork|增加 **Skills/Templates** 复用机制|
|🟢 低|OpenWork|增加 **实时进度追踪** 和任务时间线展示|

---

## 一、Cowork（Claude Work）
### 1.1 产品定位
2026年1月，Anthropic 正式推出了 Claude Cowork，这是一款集成于 Claude Desktop 应用中的产品。

**官方定义**：「让所有人都能用的 Claude Code」—— 让非开发者也能像使用 Claude Code 那样驱动 AI 完成实际工作，直接访问本地文件并生成可交付成果。

> 📌 当前的 Claude Cowork 是 Preview 版本，仅支持 MacOS，Max 和 Pro 订阅用户可用
```
flowchart LR
    subgraph Anthropic产品矩阵
        A[Claude API] --> B[Claude Desktop]
        B --> C[Claude Code<br/>终端助手<br/>面向开发者]
        B --> D[Claude Cowork<br/>屏幕助手<br/>面向知识工作者]
    end
    
    style C fill:#e3f2fd
    style D fill:#fce4ec
```
|产品|目标用户|界面形态|主要场景|
|-|-|-|-|
|**Cowork**|知识工作者（非技术用户）|可视化桌面应用|文档整理、研究、非编码任务|
|**Claude Code**|软件开发者|CLI/终端|代码库操作、Git、Docker 等开发工具|

### 1.2 内置能力
> 用户每次为 Cowork 授权一个本地文件夹，本质上是**通过数据定义一个工作场景**
```
flowchart LR
    A[用户授权文件夹] --> B[定义工作场景]
    B --> C[明确目标上下文]
    C --> D[AI 精准执行]
    
    E[NotebookLM] --> F[资料即上下文]
    G[Cowork] --> H[文件夹即上下文]
    
    F -.->|理念相似| H
```
|能力|描述|
|-|-|
|**浏览器代理**|AI 接管浏览器，控制光标点击、打开窗口、填写表单|
|**MCP 支持**|通过 MCP 连接外部工具和数据源|
|**Skills 支持**|读取 Skills 文件，完成特定任务|
|**跨应用工作流**|依托 MCP、Skills、浏览器自动化，具备跨应用工作流演进能力，为企业级场景自动化、智能协作提供基础|

### 1.3 关键技术
Anthropic 认为，真正的生产力提升来自于 AI 对用户本地数据和工作流的直接介入，但这种介入必须是**受控的**。

#### 关键技术一：递归多智能体系统
这是 Cowork 能够处理复杂任务的核心架构，有效规避了长文本任务中常见的「上下文溢出」或「注意力丢失」问题。

```
flowchart TB
    subgraph Lead[主智能体 Lead Agent]
        direction TB
        M1[Claude 4.5 Opus]
        M2[理解高层指令]
        M3[分解任务和制定策略]
        M4[监控和结果聚合]
    end
    
    subgraph Sub[子智能体群 Sub-agents]
        direction LR
        S1[子智能体A Sonnet]
        S2[子智能体B Sonnet]
        S3[子智能体C Sonnet]
    end
    
    U[用户指令] --> Lead
    Lead -->|任务分发| S1
    Lead -->|任务分发| S2
    Lead -->|任务分发| S3
    S1 -->|结果返回| Lead
    S2 -->|结果返回| Lead
    S3 -->|结果返回| Lead
    Lead --> R[最终交付物]
    
    style Lead fill:#e8eaf6
    style Sub fill:#e3f2fd
```
|角色|模型|职责|
|-|-|-|
|**主智能体**|Claude 4.5 Opus|理解用户高层指令，分解为执行步骤，监控子智能体输出|
|**子智能体**|Claude 4.5 Sonnet（多实例）|并行处理主智能体分发的子任务|
|**自我修正**|-|子智能体报错时，主智能体调整指令并重试|

**优势**：

* 保证长时间处理复杂任务不会因对话超时或上下文限制而中断
* 大幅提升稳定性与吞吐效率

#### 关键技术二：本地虚拟化沙盒
Cowork 利用 **Apple Virtualization Framework** 在 macOS 上创建轻量级、隔离的 Linux 虚拟机（VM）。

```
flowchart TB
    subgraph Host[macOS宿主机]
        direction TB
        A[用户本地文件夹]
        B[macOS系统文件]
    end
    
    subgraph VM[隔离的Linux VM]
        direction TB
        C[Cowork Agent]
        D[代码执行环境]
        E[依赖安装区]
        F[沙盒文件系统]
    end
    
    A <-->|授权挂载实时同步| F
    B -.->|无法访问| VM
    
    style VM fill:#ffebee
    style Host fill:#e8f5e9
```
|特性|描述|
|-|-|
|**隔离性**|所有文件操作、代码执行、依赖安装都在 VM 中进行。即使执行 `rm -rf /`，也只能删除 VM 内的沙盒文件|
|**文件系统映射**|用户将本地文件夹挂载给 Cowork，变动实时同步回宿主机|
|**安全边界**|VM 无法触及 macOS 系统的核心文件|

### 1.4 安全隔离机制（三道防线 + 额外防线）
Cowork 采用了企业级的安全隔离策略：

```
flowchart LR
    subgraph L1[防线一 VM隔离]
        A1[独立虚拟机运行]
        A2[危险命令仅影响VM]
    end
    
    subgraph L2[防线二 网络白名单]
        B1[默认全拒绝]
        B2[仅允许白名单域名]
    end
    
    subgraph L3[防线三 文件授权]
        C1[仅访问授权文件夹]
        C2[未授权区域不可见]
    end
    
    subgraph L4[额外防线 文件快照]
        D1[ZFS快照]
        D2[操作可回滚]
    end
    
    危险操作 --> L1 --> L2 --> L3 --> L4 --> 安全执行
    
    style L1 fill:#ffcdd2
    style L2 fill:#fff9c4
    style L3 fill:#c8e6c9
    style L4 fill:#bbdefb
```
#### 防线一：VM 虚拟机隔离
* Agent 运行在独立虚拟机中，而非用户本地电脑
* 即使执行 `rm -rf /` 这样的危险命令，也只会影响虚拟机，宿主机毫发无损
* **这是正确的隔离姿势**，大多数所谓的"沙箱"都达不到这个级别

#### 防线二：网络白名单
* 默认网络全拒绝策略
* 只允许访问特定白名单域名
* 防止数据泄露和恶意网络请求

#### 防线三：文件夹挂载授权
* 只能访问用户明确授权的文件夹
* 未授权的文件系统区域对 Agent 不可见

#### 额外防线：文件系统快照
```
# ZFS 快照示例 - 像游戏存档一样

# 做大操作前先存档
zfs snapshot pool/home/me@2026-01-12

# Claude 把你桌面删光了？一条命令回到5分钟前
zfs rollback pool/home/me@2026-01-12
```
> 文件系统快照 = 打游戏时的存档：做大操作前存档，出事了读档回滚
### 1.5 使用案例
#### 案例一：整理本地桌面大文件
> 展示 Cowork 处理本地文件和执行系统级操作的能力
```
sequenceDiagram
    participant U as 👤 用户
    participant C as 🤖 Claude
    participant F as 📁 文件系统
    
    U->>C: 查找桌面上体积较大的文件
    C->>F: 扫描桌面目录
    F-->>C: 返回文件列表
    C->>C: 生成 Excel 表格
    C-->>U: 展示文件名、大小、类型、路径
    
    U->>C: 删除体积超过 1GB 的大文件
    C-->>U: 列出符合条件的文件，请求确认
    U->>C: 确认删除
    C->>F: 执行删除操作
    C-->>U: ✅ 释放 22.4GB 磁盘空间
```
#### 案例二：浏览器自动化数据分析
> 展示浏览器代理能力 + 小红书视频数据分析
```
sequenceDiagram
    participant U as 👤 用户
    participant C as 🤖 Claude
    participant B as 🌐 浏览器
    participant F as 📁 本地文件
    
    U->>C: 分析小红书视频数据
    C->>B: 自动打开小红书后台
    C->>B: 点击「内容分析」菜单
    B-->>C: 返回视频数据
    C->>C: 提取最近10条视频数据
    C->>C: 筛选3条爆款视频
    C->>C: 分析爆款原因 & 总结规律
    C->>F: 生成 Excel（3个Sheet）
    C-->>U: ✅ 完整数据 + 深度分析 + 规律总结
```
### 1.6 商业模式
Cowork 是**付费产品**，面向专业付费用户。这也催生了开源替代方案的需求，于是有了 **OpenWork**。

## 二、OpenWork
### 2.1 产品定位
OpenWork 是 "Claude Work" 的**可扩展开源替代方案**，构建于 [OpenCode](https://opencode.ai/) 之上。

**核心价值**：将 OpenCode 配置转化为非技术用户可用的体验。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b4b51da23f534da480ec07aa4ea4df3e&docGuid=d7F8palkHd3tI2 "")
### 2.2 运行模式
```
flowchart TB
    subgraph HostMode[Host模式]
        H1[本地启动OpenCode]
        H2[完全离线运行]
        H3[适合个人使用]
    end
    
    subgraph ClientMode[Client模式]
        C1[连接远程服务器]
        C2[工具在远程执行]
        C3[适合团队协作]
    end
    
    User[用户] --> HostMode
    User --> ClientMode
    
    style HostMode fill:#e8f5e9
    style ClientMode fill:#e3f2fd
```
|模式|描述|适用场景|
|-|-|-|
|**Host 模式**|在本地启动 OpenCode 服务，完全离线|个人使用、隐私敏感场景|
|**Client 模式**|连接远程 OpenCode 服务器|团队协作、企业部署|

#### 💡 OpenWork Client 模式 vs MCP 方案的区别
虽然两者都涉及"远程连接"，但**架构方向完全相反**：

```
flowchart LR
    subgraph OW[OpenWork Client模式]
        direction LR
        U1[用户浏览器GUI] -->|请求| S1[远程服务器]
    end
    
    subgraph MC[MCP方案]
        direction LR
        S2[AI Agent服务端] -->|请求| U2[本地执行器]
    end
    
    OW -.->|工具在远程执行| Remote[远程]
    MC -.->|工具在本地执行| Local[本地]
    
    style OW fill:#e3f2fd
    style MC fill:#fff3e0
```
|对比维度|OpenWork Client 模式|MCP 方案|
|-|-|-|
|**连接方向**|用户 → 远程服务器|AI 服务端 → 本地执行器|
|**执行位置**|远程服务器|用户本地机器|
|**典型场景**|团队共享 AI 环境|AI 操作本地代码库|
|**安全模型**|远程隔离（服务器保护）|需本地隔离（保护用户机器）|

**核心区别**：

* **OpenWork Client**：把执行环境放到远程，保护用户本地
* **MCP**：让 AI 能操作用户本地，需要保护用户本地

### 2.3 引导式工作流
```
flowchart LR
    A[1.选择工作区] --> B[2.启动运行]
    B --> C[3.查看进度]
    C --> D[4.审批权限]
    D --> E[5.保存复用]
    
    style A fill:#e1f5fe
    style B fill:#e8f5e9
    style C fill:#fff9c4
    style D fill:#ffccbc
    style E fill:#e1bee7
```
1. **选择工作区（Workspace）** - 指定任务执行的目录范围
2. **启动运行（Run）** - 输入自然语言指令启动任务
3. **查看进度与计划更新** - 实时追踪执行状态
4. **审批权限** - 在需要时批准敏感操作
5. **保存并复用** - 将成功流程保存为模板或技能

### 2.4 权限控制与审计
```
flowchart LR
    A[敏感操作] --> B{权限弹窗}
    B -->|允许一次| C[执行]
    B -->|始终允许| D[执行 + 记住]
    B -->|拒绝| E[取消]
    
    C --> F[操作记录]
    D --> F
    F --> G[时间线视图]
    
    style B fill:#fff9c4
    style F fill:#e8f5e9
```
|功能|描述|
|-|-|
|**权限弹窗**|敏感操作会弹出权限请求：允许一次 / 始终允许 / 拒绝|
|**执行计划时间线**|清晰展示 AI 做了什么、为什么做|
|**操作记录**|所有操作步骤均被记录，便于事后审查|

## 三、MCP（我们的远程执行方案）
### 3.1 方案概述
我们的 MCP 方案基于 **WebSocket + JSON** 协议实现，是一个轻量级的远程工具执行框架。

**核心文件**：`mcp_remote_tools.py`

**设计理念**：

* 通过 WebSocket 连接到服务端，接收工具执行请求并在本地执行
* 支持会话 ID 管理，多客户端可同时连接
* 工具定义与执行解耦，便于扩展

### 3.2 架构设计
```
flowchart TB
    subgraph 服务端["☁️ AI Agent 服务端"]
        A1[AI 决策引擎]
        A2[发送 tool_execute]
        A3[接收 tool_result]
    end
    
    subgraph 通信层["📡 WebSocket + JSON"]
        B1[双向通信]
        B2[会话管理]
        B3[心跳检测]
    end
    
    subgraph 客户端["🏠 RemoteExecClient"]
        C1[工具执行器]
        C2[Bash/Read/Write/Edit]
        C3[Glob/Grep]
    end
    
    subgraph 本地资源["📁 本地资源"]
        D1[文件系统]
        D2[Shell 环境]
        D3[Git 仓库]
    end
    
    服务端 <-->|WebSocket| 通信层
    通信层 <-->|WebSocket| 客户端
    客户端 --> 本地资源
    
    style 服务端 fill:#e3f2fd
    style 客户端 fill:#e8f5e9
    style 本地资源 fill:#fff9c4
```
### 3.3 支持的工具集
```
flowchart LR
    subgraph 命令执行["⚡ 命令执行"]
        A1[Bash<br/>Shell命令]
        A2[BashOutput<br/>后台输出]
        A3[BashKill<br/>终止进程]
    end
    
    subgraph 文件操作["📁 文件操作"]
        B1[Read<br/>读取文件]
        B2[Write<br/>写入文件]
        B3[Edit<br/>查找替换]
    end
    
    subgraph 搜索功能["🔍 搜索功能"]
        C1[Glob<br/>模式匹配]
        C2[Grep<br/>内容搜索]
    end
    
    style 命令执行 fill:#ffccbc
    style 文件操作 fill:#c8e6c9
    style 搜索功能 fill:#bbdefb
```
|工具名|功能描述|关键参数|
|-|-|-|
|**Bash**|执行 Shell 命令|`command`, `timeout`, `run_in_background`|
|**BashOutput**|获取后台进程输出|`bash_id`, `filter`（正则过滤）|
|**BashKill**|终止后台进程|`shell_id`|
|**Read**|读取文件内容|`file_path`, `offset`, `limit`|
|**Write**|写入文件|`file_path`, `content`|
|**Edit**|查找替换编辑|`file_path`, `old_string`, `new_string`|
|**Glob**|文件模式匹配|`pattern`, `path`|
|**Grep**|内容正则搜索|`pattern`, `path`, `glob`|

### 3.4 通信协议
```
sequenceDiagram
    participant S as ☁️ Server
    participant C as 🏠 Client
    
    Note over S,C: 连接建立
    C->>S: tools_register<br/>注册工具列表
    
    Note over S,C: 工具执行
    S->>C: tool_execute<br/>{tool_name, tool_input}
    C->>C: 本地执行
    C->>S: tool_result<br/>{exit_code, output}
    
    Note over S,C: 心跳检测
    S->>C: ping
    C->>S: pong
```
|消息类型|方向|用途|
|-|-|-|
|`tools_register`|Client → Server|客户端注册支持的工具列表|
|`tool_execute`|Server → Client|服务端发送工具执行请求|
|`tool_result`|Client → Server|客户端返回执行结果|
|`ping` / `pong`|双向|心跳检测|

### 3.5 关键特性
```
flowchart TB
    subgraph 已实现["✅ 已实现"]
        A1[后台进程管理]
        A2[进程组隔离]
        A3[系统信息采集]
        A4[断线重连]
        A5[超时控制]
        A6[输出截断]
    end
    
    subgraph 待实现["❌ 待实现"]
        B1[VM/容器隔离]
        B2[网络白名单]
        B3[权限审批]
        B4[操作回滚]
        B5[进度追踪 UI]
    end
    
    style 已实现 fill:#c8e6c9
    style 待实现 fill:#ffcdd2
```
#### ✅ 已实现
|特性|描述|
|-|-|
|**后台进程管理**|支持 `run_in_background`，可启动、监控、终止后台任务|
|**进程组隔离**|使用 `start_new_session=True`，确保能杀死整个进程树|
|**系统信息采集**|自动采集 OS、Python 版本、Git 状态等上下文|
|**断线重连**|支持自动重连，可配置重连间隔和最大次数|
|**超时控制**|命令执行支持超时（默认 2 分钟，最大 10 分钟）|
|**输出截断**|超长输出自动截断（30000 字符）|

#### ❌ 尚未实现（可借鉴改进）
|特性|来源|改进建议|
|-|-|-|
|**VM/容器隔离**|Cowork|封装到 Docker/VM|
|**网络白名单**|Cowork|增加 iptables/防火墙规则|
|**权限审批**|OpenWork|敏感操作增加确认机制|
|**操作回滚**|Cowork|集成快照机制|
|**进度追踪 UI**|OpenWork|增加可视化界面|

## 四、MCP 方案可借鉴的方向
### 4.1 综合改进架构
```
flowchart TB
    subgraph GUI层["🖥️ GUI 层 ← OpenWork"]
        G1[可视化界面]
        G2[权限审批弹窗]
        G3[实时进度追踪]
    end
    
    subgraph 扩展层["🔧 扩展层 ← OpenWork"]
        E1[Skills 技能]
        E2[Templates 模板]
        E3[Plugins 插件]
    end
    
    subgraph 协议层["📡 协议层"]
        P1[MCP 协议]
        P2[WebSocket + JSON]
    end
    
    subgraph 安全层["🔐 安全层 ← Cowork"]
        S1[VM/容器隔离]
        S2[网络白名单]
        S3[文件快照/回滚]
    end
    
    subgraph 执行层["⚡ 执行层"]
        X1[MCP Server 生态]
        X2[自定义工具]
    end
    
    GUI层 --> 扩展层
    扩展层 --> 协议层
    协议层 --> 安全层
    安全层 --> 执行层
    
    style GUI层 fill:#e3f2fd
    style 扩展层 fill:#e8f5e9
    style 协议层 fill:#fff9c4
    style 安全层 fill:#ffccbc
    style 执行层 fill:#e1bee7
```
### 4.2 改进方向汇总
|层面|借鉴来源|改进方向|实现建议|
|-|-|-|-|
|**安全**|Cowork|VM 级隔离|容器/VM 运行时封装|
|**安全**|Cowork|网络白名单|协议层增加网络策略|
|**安全**|Cowork|快照/回滚|集成文件系统快照|
|**体验**|OpenWork|实时进度追踪|标准进度反馈协议|
|**体验**|OpenWork|权限审批|敏感操作确认流程|
|**扩展**|OpenWork|Skills 机制|业务逻辑标准封装|
|**扩展**|OpenWork|Templates|工作流模板导入/导出|

---

## 五、总结
|方案|核心优势|适用场景|
|-|-|-|
|**Cowork**|安全隔离最强，开箱即用|企业付费用户、高安全要求场景|
|**OpenWork**|开源免费，用户体验好|个人开发者、团队协作、成本敏感场景|
|**MCP**|灵活度高，生态丰富|深度定制、自建平台、技术型用户|

### MCP 方案发展方向
```
flowchart LR
    A[MCP现状] --> B[向下: 安全底座]
    A --> C[向上: 用户体验]
    A --> D[横向: 扩展生态]
    
    B --> B1[VM隔离]
    B --> B2[网络白名单]
    
    C --> C1[GUI界面]
    C --> C2[权限审批]
    C --> C3[进度追踪]
    
    D --> D1[Skills]
    D --> D2[Templates]
    D --> D3[Plugins]
    
    style A fill:#fff9c4
    style B fill:#ffccbc
    style C fill:#c8e6c9
    style D fill:#bbdefb
```
**发展路径**：

1. **向下**：借鉴 Cowork 的 VM 隔离和网络白名单，增强安全底座
2. **向上**：借鉴 OpenWork 的 GUI、权限审批、进度追踪，提升用户体验
3. **横向**：借鉴 OpenWork 的 Skills/Templates/Plugins 体系，完善扩展生态

三种方案各有侧重，可根据实际需求选择或组合使用。MCP 作为开放协议，具有最大的灵活性和可塑性，通过借鉴 Cowork 和 OpenWork 的优秀设计，有望成为 AI Agent 领域的通用标准。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
