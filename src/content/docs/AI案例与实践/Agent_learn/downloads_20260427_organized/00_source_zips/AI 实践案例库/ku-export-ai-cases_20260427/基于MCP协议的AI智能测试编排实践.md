---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "基于MCP协议的AI智能测试编排实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于MCP协议的AI智能测试编排实践.md"
---
基于MCP协议的AI智能测试编排实践

#### 🧑‍🏫 案例作者：[@李静静](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：数据分析、测试
#### 🔧 使用工具：Ducc
#### 📒 案例概要：降低反复切换机器的频率，提升测试效率并减少人为操作风险，本实践旨在构建一个个性化、自动化的工作流。将AI模型的能力，通过标准化的协议，无缝、安全地转化为对单个/多个远程服务器的直接操作能力。
## **实践简介**
**案例贡献人：**李静静

**相关背景：**

       随着AI助手能力的深度内化，我们不再满足于使用通用、标准化的工具。为了更紧密地贴合我们的**业务场景**，降低反复切换机器的频率，减少冗余操作，提升测试效率并减少人为操作风险，本实践旨在构建一个**个性化、自动化的工作流**。核心目标是：**将AI模型的能力，通过标准化的协议，无缝、安全地转化为对单个/多个远程服务器的直接操作能力。**本实践基于风控业务token校验接口（c/11/z，c/12/z接口）测试方向展开，通过mcp工具实现在本地可以自由对远端服务器进行命令输入并获取结果的能力。本案例以c/12/z进行样例展示：

```
graph TD
    A[开始接口c/12/z测试] --> B[准备测试参数池<br>AK/SK对列表, IP列表]
    
    B --> C{还有未测试的<br>参数组合?}
    
    C -->|是| D[选择一组参数<br>AK/SK, IP]
    
    D --> E[构造原始JSON请求数据<br>根据接口规范]
    
    E --> F[使用加密工具加密请求数据<br>基于当前SK]
    
    F --> G[将加密后的数据填充至python脚本<br>包含: data, deviceID, skey]
    
    G --> H[执行Python脚本发起请求]
    
    H --> I[脚本解析接口响应]
    
    I --> J{响应状态判断}
    
    J -->|成功| K[符合预期: 参数组合 + 解密后的响应数据]
    J -->|失败| L[不符合预期: 参数组合 + 查看原因]
    
    
    %% 样式定义
    classDef process fill:#e2f0fb,stroke:#0c5460
    classDef decision fill:#fff3cd,stroke:#856404
    classDef security fill:#cfe2ff,stroke:#084298
    classDef script fill:#d1ecf1,stroke:#0c5460
    classDef success fill:#d4edda,stroke:#155724
    classDef failure fill:#f8d7da,stroke:#721c24
    
    class A,B,D,E process
    class C,J decision
    class F security
    class G,H,I script
```
**当前测试流程存在的痛点：**

```
flowchart LR
    subgraph 传统模式["😫 传统测试模式"]
        direction TB
        P1[登录机器A] --> P2[执行加密脚本]
        P2 --> P3[复制加密结果]
        P3 --> P4[登录机器B]
        P4 --> P5[粘贴数据]
        P5 --> P6[修改配置文件]
        P6 --> P7[运行测试脚本]
        P7 --> P8[查看结果]
        P8 --> P9[手动记录]
    end
    
    subgraph 智能模式["🚀 MCP智能模式"]
        direction TB
        N1[一句话描述需求] --> N2[AI自动编排]
        N2 --> N3[跨机器执行]
        N3 --> N4[结果自动汇总]
    end
    
    传统模式 -.->|"效率提升 10x"| 智能模式
    
    style 传统模式 fill:#ffebee,stroke:#c62828
    style 智能模式 fill:#e8f5e9,stroke:#2e7d32
```
## **为何选用MCP？**
#### mcp是什么？
MCP（Model Context Protocol）是**一个开放协议，用于让AI模型安全、标准化地连接和使用外部工具、数据源与服务**。MCP协议通过**JSON-RPC**标准化了AI模型与外部工具的交互方式。

想象一个研究员（LLM）在一个有固定大小办公桌（上下文窗口）的房间里：

* 桌上只能放几本书（当前对话内容）
* MCP 就像是**图书馆借阅系统**
* 研究员不需要把整个图书馆搬上桌，只需知道如何查找和借阅
* 当需要某本书时，通过协议“借阅”相关内容

#### mcp&当前方案的优点
1. **标准化集成**：统一接口，简化工具接入
2. **模型无关性**：支持多种AI模型调用
3. **动态扩展**：运行时即插即用
4. **突破上下文窗口限制**：无需将庞大的日志文件或代码库全部塞入AI的上下文，而是通过 `Read`、`Grep`、`Glob` 等工具按需、精准地获取信息，极大扩展了AI处理复杂任务的能力边界。
5. **解决AI“幻觉”与落地鸿沟**：大语言模型在生成命令或代码时可能存在“幻觉”。MCP通过提供一套真实、可执行且结果可验证的工具，将AI的“思考”直接转化为“行动”，确保了输出的准确性与可落地性。
6. **统一交互范式，降低认知负荷**：无论背后操作的是Bash、数据库还是K8s，用户都只需通过自然语言与AI对话。MCP在背后统一了异构系统的交互方式，让用户和开发者都只需关注“要做什么”，而非“怎么做”。

#### 基于mcp具备跨平台环境集成能力
```
graph TD
    A[agent] -->|1. 发起请求| B[MCP Client]
    B -->|2. 建立连接| C[MCP Server]
    
    C -->|3. 协议交互| D{MCP协议层}
    
    D -->|工具调用| E[外部工具集<br/>文件系统/API/数据库/自定义]
    D -->|数据访问| F[外部数据源<br/>本地文件/云存储/数据库/API]
    D -->|资源获取| G[外部资源<br/>配置/模板/代码片段]
    D -->|跨平台集成| H[跨平台环境<br/>Windows/Linux/macOS/容器]
    
    E -->|执行结果| I[统一响应处理]
    F -->|数据返回| I
    G -->|资源内容| I
    H -->|环境信息| I
    
    I -->|4. 返回结果| D
    D -->|5. 响应| C
    C -->|6. 传递| B
    B -->|7. 最终结果| A
    
    style A fill:#e1f5ff
    style B fill:#fff4e6
    style C fill:#fff4e6
    style D fill:#f3e5f5
    style E fill:#c8e6c9
    style F fill:#ffe0b2
    style G fill:#f8bbd0
    style H fill:#fff9c4
    style I fill:#e0f2f1
```
我们成功开发并部署了一个基于 **Model Context Protocol** 协议的服务器脚本 (`mcp_sse_server.py`)。该脚本的核心突破在于**实现了八项关键服务器操作的“原子化”工具集**，并将其暴露为标准化的AI可调用接口。

**已实现的原子化工具清单：**

|**工具名称**|**对应函数**|**核心能力说明**|
|-|-|-|
|`Bash`|**_handle_bash**|**执行**任意Shell命令|
|`BashOutput`|**_handle_bash_output**|**获取**异步命令的实时输出|
|`BashKill`|**_handle_bash_kill**|**终止**正在运行的后台命令|
|`Read`|**_handle_read**|**读取**服务器上的任意文件内容|
|`Write`|**_handle_write**|**创建或覆盖**写入文件|
|`Edit`|**_handle_edit**|**查找并替换**文件中的特定内容|
|`Glob`|**_handle_glob**|**匹配查找**符合规则的文件路径|
|`Grep`|**_handle_grep**|**搜索过滤**文件中的特定文本|

这些工具通过一个统一的**工具处理器映射表**进行管理，确保了每个请求都能被精准路由和高效执行。

#### MCP协议中的客户端请求流程
1. 客户端发送的JSON-RPC请求格式--当MCP客户端要调用"Bash"工具时，会发送类似这样的JSON-RPC请求：

```
{
  "jsonrpc": "2.0",
  "id": 42,
  "method": "tools/call",
  "params": {
    "name": "Bash",
    "arguments": {
      "command": "ls -la",
      "timeout": 30000,
      "run_in_background": false
    }
  }
}
```
2. 服务器接收和解析流程

服务端接收请求的处理路径是：

接收请求 → mcp_endpoint（MCP Streamable HTTP 端点 - 直接处理 JSON-RPC） 或 SSE处理函数
解析方法 → method = request.get("method") → 得到 "tools/call"
解析参数 → params = request.get("params", {}) → 得到工具调用参数
调用处理器 → _handle_tools_call(params)

```
flowchart LR
    A[接收请求] --> B[JSON-RPC解析]
    B --> C{method判断}
    C -->|"tools/call"| D[提取params参数]
    D --> E[调用_handle_tools_call]
    E --> F[返回响应]
```
3. 工具调用处理

在_handle_tools_call方法中的关键步骤：

```
tool_name = params.get("name")  # "Bash"
tool_args = params.get("arguments", {})  # {"command": "ls -la", ...}

handler = self.tool_handlers.get(tool_name)  # 找到_handle_bash方法
result = await handler(tool_args, self.work_dir)  # 调用_handle_bash
```
4. 具体参数传递

常见客户端类型，MCP客户端可以是：

* VS Code插件 - 集成AI助手并通过MCP调用工具
* 命令行工具 - 通过curl或Python客户端发送JSON-RPC

**完整的交互示例**

```
客户端发送:
{
  "jsonrpc": "2.0",
  "id": 123,
  "method": "tools/call",
  "params": {
    "name": "Bash",
    "arguments": {
      "command": "echo 'hello world'",
      "timeout": 60000
    }
  }
}

服务器回复:
{
  "jsonrpc": "2.0", 
  "id": 123,
  "result": {
    "content": [{
      "type": "text",
      "text": "hello world"
    }]
  }
}
```
#### **工作流革新：从本地到远程的无缝操作**
本工具最大的价值在于，它彻底改变了我们与服务器的交互模式：

* **一键部署**：将脚本部署到目标服务器后，**无需登录SSH**。
* **自然语言驱动**：在本地电脑上，即可通过支持MCP协议的AI客户端（如Claude Desktop、Cursor等），使用**自然语言直接指挥远程服务器**。
* **示例场景**：
    * **口头指令**：“请检查远程生产服务器`/opt/logs/`目录下今天最新的错误日志，并统计`ERROR`级别的数量。”
    * **AI理解并调用**：AI会自动组合调用`Glob`定位日志文件 ->`Read`读取内容 ->`Grep`过滤统计 -> 将结果返回给你。
    * **复杂任务**：“在测试服务器上拉取最新代码，安装依赖，并重启服务。” AI将按顺序调用`Bash`命令完成整个流水线。


#### **项目意义与价值**
1. **效率飞跃**：将复杂的命令行操作转化为自然语言对话，极大降低了操作门槛，提升了任务执行速度。
2. **安全可控**：所有操作均在受控的MCP协议下进行，工具集原子化且可审计，避免了手工操作可能引发的误操作风险。
3. **能力内化**：这不仅是部署了一个工具，更是**将核心的服务器运维能力深度内化到了AI工作流中**。AI从一个“建议者”变成了一个“安全的执行者”。
4. **范式转变**：为我们构建更复杂的自动化运维、智能监控、自动化测试等个性化业务工作流，提供了坚实可靠的**底层执行框架**。
5. **价值量化：**将需要中级Shell知识的任务，降低为**只需业务描述能力**即可完成。

```
graph TB
    subgraph 传统认知["❌ 常见误解"]
        W1[只是远程执行工具]
        W2[类似SSH批量管理]
        W3[简单的命令转发]
    end
    
    subgraph 真正价值["✅ 核心价值"]
        R1[语义理解层]
        R2[智能编排层]
        R3[上下文感知层]
        R4[自适应执行层]
    end
    
    R1 -->|"理解测试意图"| R2
    R2 -->|"动态生成执行计划"| R3
    R3 -->|"感知环境状态"| R4
    R4 -->|"反馈优化"| R1
    
    style 传统认知 fill:#fff3e0,stroke:#ff9800
    style 真正价值 fill:#e3f2fd,stroke:#1976d2
```
## **实际测试场景中的使用**
1.在zulu中配置自定义的mcp工具：

* 将完成的mcp_remote_server.py运行在目标机器上
* 配置目标机器的ip以及工具名称

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac82ab1d31db4e6c99f8255939644c00&docGuid=qOql2lj3HdcAWQ "")
2.在测试中，需要先在A机器进行对于构造的数据进行加密，生成加密的bin文件；直接在zulu操作目标机器：

【使用mcp工具，工具名称为encry-machine，执行./cloud_enc】

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aa8cff5d4fbb415e9f7b1ac9364b37ae&docGuid=qOql2lj3HdcAWQ "")
3.再在B机器中，执行shell脚本，获取可用的加密数据：【使用mcp工具，工具名称为remote-tools，执行sh test.sh】

当我们获取到加密数据时，就可以更新加密数据至请求接口的python文件中，进行接口请求，输入以下指令：

【使用mcp工具，工具名称为remote-tools，获取刚刚运行sh test.sh脚本的输出信息，将data的值替换en_decry.py中入参data的值，skey的值替换en_decry.py中入参skey的值。并运行python en_decry.py 注意在使用edit工具时，old string不需要额外的转义字符，不然会导致MCP Tool 执行失败。String not found】

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d7933c518ad045398157528c7ac80bb1&docGuid=qOql2lj3HdcAWQ "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6b2dbe393a8445cdb1f319086af3f8f4&docGuid=qOql2lj3HdcAWQ "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6e45ea3646204ce8805ee9cda08fb673&docGuid=qOql2lj3HdcAWQ "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3af1af1d8e804aa3bd57b22308943def&docGuid=qOql2lj3HdcAWQ "")
 

对于最后一句指令，MCP 客户端将按顺序调用一个**严谨的四步工具链**：首先，调用 `BashOutput` 工具获取 `test.sh` 脚本的运行输出并解析出 `data` 与 `skey` 的值；接着，连续两次调用 `Edit` 工具，分别将解析出的新值精确替换到 `en_decry.py` 文件对应的参数位置（此步骤需严格遵循字符串完全匹配原则，避免因转义导致失败）；最后，调用 `Bash` 工具执行修改后的 `python en_decry.py` 脚本，从而完成从数据提取、文件修改到最终运行的端到端自动化流程。

```
graph TD
    A[用户指令] --> B[第一步获取输出]
    B --> C{判断输出类型}
    
    C -- 异步任务 --> D[调用BashOutput]
    C -- 同步任务 --> E[解析历史Bash]
    
    D --> F[提取data和skey值]
    E --> F
    
    F --> G[第二步修改文件]
    G --> H[Edit工具替换data & skey]
    H --> I[注意完全匹配字符串]
    
    I --> L[第三步运行脚本]
    L --> M[调用Bash工具]
    M --> N[执行python en_decry.py]
    N --> O[返回结果]
    
    style I fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:1px
    style H fill:#ccf,stroke:#333,stroke-width:1px
    style M fill:#ccf,stroke:#333,stroke-width:1px
```


## **总结与反思**
       通过AI技术内化的不断深入，我们正逐渐告别标准化工具的直接套用，转而进入一个更为关键的新阶段：**必须从自身业务的实际需求出发，构建专属的、可迭代的工作流，并深度借助模型能力，开展个性化、场景化的业务测试与验证**。这不仅是技术应用的深化，更是思维与工作方式的主动进化——让AI真正融入业务脉络，成为解决问题的有机部分，而不仅仅是一个外部工具。

       对于脚本能力方面的提升，我们将基于此原子化工具层，进一步：

    * **扩展工具集**：增加如进程管理、性能监控、备份还原等更多原子操作。
    * **构建高阶工作流**：封装针对具体业务场景的复合操作（如“一键上线”、“数据巡检”）。如：“每日上午9点，自动检查所有服务的进程状态与关键日志，并生成健康报告。” → 通过AI工作流编排，定时自动执行一系列 `Bash`、`Grep` 调用。
    * **增强安全性**：增加操作权限分级与相关日志打印，所有通过MCP工具执行的命令、访问的文件路径都应被详细记录（例如记录到 `syslog` 或专用审计文件）。
    * **输入验证与过滤**：在 `_handle_bash` 等函数中，可加入基础的安全校验（如禁止某些高危命令模式），虽然主要依赖权限控制，但可作为额外防护层。





# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
