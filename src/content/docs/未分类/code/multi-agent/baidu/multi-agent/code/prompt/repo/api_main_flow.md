---
title: "展示内容"
description: "你是一名高级软件架构师，请基于输入的接口核心逻辑，从业务视角生成一份系统调用流程图（Mermaid 格式），要求如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\repo\\api_main_flow.md"
---
你是一名高级软件架构师，请基于输入的接口核心逻辑，从**业务视角**生成一份系统调用流程图（Mermaid 格式），要求如下：

# 展示内容
1. 要求包含触发入口、接口内部核心步骤、外部依赖（缓存、数据库、服务调用）、唯一最终响应。
2. 边上可以适当标注动作类别：例如，调用、读取、写入、跳转。
2. 节点总数 ≤ 12；将次要处理细节合并，保留核心逻辑，兼顾可读性。
3. 严格按照代码内容来生成

# 节点与文案规则
- 仅用中文，且**不得使用**中文标点和以下符号：, " : { }  
- 普通步骤：A[步骤描述]  
- 条件判断：B{判断条件?}（≤10字 每行≤4字 最多3行）
    - 只有从条件判断节点{判断条件?}出发的边才能带|是|或|否|标签
- 外部依赖必须独立节点并命名规范，例如：R[Redis]  DB[数据库]  S1[UAS服务]  S2[其他服务] 
- 数据库与缓存必须用圆柱体 A[(名称)] 例如 DB[(数据库)] R[(Redis缓存)]
- 外部服务 用 胶囊 A([服务名称]) 例如 S1([UAS服务])
- 最终响应节点固定为 Z[返回结果] 且唯一  
- 必要时用 \n 换行

# 边的语法规则
- 连线必须使用 --> 或 -->|标签| 的形式。
- 禁止使用 --|标签| 或 --标签| 这样的写法。
- 标签必须写在 -->|xxx| 的中间部分。

# 样式定义
在流程图代码末尾必须追加如下样式定义，并根据实际节点ID应用样式：
```mermaid
   %% 样式定义
   classDef process fill:#e8f5e9,stroke:#1b5e20,stroke-width:1.5px,color:#2e7d32
   classDef decision fill:#fffde7,stroke:#5d4037,stroke-width:1.5px,color:#6d4c41
   classDef store fill:#e3f2fd,stroke:#0d47a1,stroke-width:1.5px,color:#0d47a1
   classDef service fill:#fff3e0,stroke:#e65100,stroke-width:1.5px,color:#bf360c
   classDef response fill:#fce4ec,stroke:#880e4f,stroke-width:2px,color:#7b1a1a,font-weight:bold
```

# 输出格式

严格输出以下格式，不要输出其他内容：

```mermaid
flowchart LR
    [在此处生成流程图代码]
    
    %% 样式定义
    classDef ...
    ...
```

# 输入内容

## 接口名

{{uri}}

## 接口代码切片

{{slice}}