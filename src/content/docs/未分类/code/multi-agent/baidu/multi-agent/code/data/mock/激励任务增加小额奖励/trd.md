---
title: "1. 需求背景"
description: "功能点：新增激励视频任务小额现金奖励逻辑 | 目标代码库 | 接口名称 | 接口路径 | 改动类型 | 变更概述 | 备注 | |-------------------------------------------------------"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\data\\mock\\激励任务增加小额奖励\\trd.md"
---
# 1. 需求背景
* **需求文档**： [【非随】【极速版存钱罐】激励视频任务增加小额奖励](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-30227/show)
* **背景描述**: 任务列表激励视频任务增加小额发放，激励用户完成激励视频任务，提升激励视频收入
* **预期收益**：

# 2. 设计总览
* **功能点**：`原有激励视频任务金豆奖励逻辑`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 激励视频任务完成接口    | /video/external/task/adVideoComplete                          | 修改 | 新增用户等级校验与金豆奖励计算逻辑 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 任务列表查询接口   | /video/external/task/list                          | 修改             | 新增用户等级透传与任务限额展示 |          |

* **功能点**：`新增激励视频任务小额现金奖励逻辑`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 激励视频任务完成接口    | /video/external/task/adVideoComplete                          | 修改 | 根据用户等级和任务完成节点计算小额现金奖励 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 任务列表查询接口    | /video/external/task/list                          | 修改 | 在任务列表中展示用户等级对应的奖励节点信息 |          |

# 3. 详细设计
## 3.1 原有激励视频任务金豆奖励逻辑
```mermaid
sequenceDiagram
    participant client as 客户端
    participant taskList as /video/external/task/list
    participant taskComplete as /video/external/task/adVideoComplete
    participant strategy as 策略服务

    client->>taskList: GET /video/external/task/list
    Note right of taskList: 请求参数: userLevel dailyCompletedCount isFirstToday rewardFactor
    taskList->>strategy: 获取用户策略(userLevel)
    strategy-->>taskList: 返回dailyLimit rewardMultiplier
    taskList-->>client: 响应: userLevel dailyLimit completedCount rewardMultiplier isFirstToday

    client->>taskComplete: POST /video/external/task/adVideoComplete
    Note right of taskComplete: 请求参数: userLevel dailyCompletedCount isFirstToday rewardFactor
    alt 校验次数未超限
        taskComplete->>strategy: 获取奖励策略(userLevel)
        strategy-->>taskComplete: 返回rewardMultiplier
        alt isFirstToday=true
            taskComplete->>taskComplete: 计算奖励(rewardAmount*2*rewardMultiplier)
        else isFirstToday=false
            taskComplete->>taskComplete: 计算奖励(rewardAmount*rewardMultiplier)
        end
        taskComplete-->>client: 响应: userLevel dailyLimit completedCount rewardAmount isFirstToday rewardMultiplier
    else 校验次数超限
        taskComplete-->>client: 返回错误(已达当日上限)
    end
```
### 3.1.1 激励视频任务完成接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/adVideoComplete`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. **用户等级校验与次数限制**
   - 根据用户等级（L1/L2/L3/L4）动态设置单日激励视频任务上限次数（15/25/35次）
   - 校验当前用户已完成次数是否超过当日上限
2. **金豆奖励计算**
   - 生成随机金豆奖励值（范围600-1000）
   - 判断是否为当日首次完成，若是则奖励翻倍
   - 叠加奖励系数逻辑（如实验策略或活动加成）
3. **任务状态更新**
   - 记录当前任务完成次数+1
   - 标记首次完成状态（仅当日首次触发时）
4. **结果返回**
   - 返回用户等级、单日上限次数、当前完成次数、实际发放金豆值、是否首次完成、奖励系数等核心字段
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户等级] --> B{等级校验\n通过?}
    B -- 是 --> C[获取当日\n完成次数]
    B -- 否 --> Z[返回错误]
    C --> D{次数超\n上限?}
    D -- 否 --> E[生成随机\n金豆600-1000]
    D -- 是 --> Z
    E --> F{当日首次\n完成?}
    F -- 是 --> G[奖励翻倍]
    F -- 否 --> H[应用奖励\n系数]
    G --> H
    H --> I[更新任务\n完成次数]
    I --> J[标记首次\n完成状态]
    J --> K[返回结果数据]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,E,G,H,I,J,K process
    class B,D,F decision
    class Z important
```
* **请求参数变更点**: 
```json
{
  "userLevel": "string|required|用户等级(L1/L2/L3/L4)|NEW",
  "dailyCompletedCount": "int32|required|当日已完成次数|NEW",
  "isFirstToday": "bool|required|是否当日首次完成|NEW",
  "rewardFactor": "float32|奖励系数(实验策略或活动加成)|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "userLevel": "string|用户等级(L1/L2/L3/L4)|NEW",
  "dailyLimit": "int|单日激励视频任务上限次数|NEW",
  "completedCount": "int|当前已完成次数|NEW",
  "rewardAmount": "int|实际发放金豆值(600-1000)|NEW",
  "isFirstToday": "bool|是否当日首次完成|NEW",
  "rewardMultiplier": "float64|奖励系数(实验策略或活动加成)|NEW"
}
```

### 3.1.2 任务列表查询接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/list`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. **用户等级透传**
   - 获取用户基础信息时需包含用户等级字段
2. **任务限额展示**
   - 在激励视频任务项中动态显示当前等级对应的单日上限次数（15/25/35次）
   - 实时返回用户当日已完成的激励视频任务次数
3. **奖励系数预加载**
   - 根据实验策略预计算可能的奖励系数范围
4. **首次完成状态同步**
   - 标记用户当日是否已触发过首次完成奖励翻倍
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户\n基础信息] --> B{是否包含\n用户等级?}
    B -- 是 --> C[透传用户\n等级字段]
    B -- 否 --> D[补充查询\n等级数据]
    C --> E[查询任务\n限额配置]
    D --> E
    E --> F[获取当日\n已完成次数]
    F --> G[计算剩余\n可完成次数]
    G --> H{是否首次\n完成今日?}
    H -- 是 --> I[触发奖励\n翻倍逻辑]
    H -- 否 --> J[预加载\n奖励系数]
    I --> J
    J --> K[返回任务\n限额数据]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,J,K process
    class B,H decision
    class I important
```
* **请求参数变更点**: 
```json
{
  "userLevel": "string|required|用户等级(L1/L2/L3/L4)|NEW",
  "dailyCompletedCount": "int32|required|当日已完成次数|NEW",
  "isFirstToday": "bool|required|是否当日首次完成|NEW",
  "rewardFactor": "float32|奖励系数(实验策略或活动加成)|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "userLevel": "string|用户等级(L1/L2/L3/L4)|NEW",
  "dailyLimit": "int|单日激励视频任务上限次数|NEW",
  "completedCount": "int|当前已完成次数|NEW",
  "rewardMultiplier": "float64|奖励系数(实验策略或活动加成)|NEW",
  "isFirstToday": "bool|是否当日首次完成|NEW"
}
```

## 3.2 新增激励视频任务小额现金奖励逻辑
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant AdVideoComplete as /video/external/task/adVideoComplete
    participant TaskList as /video/external/task/list
    participant StrategyService as 策略服务

    Client->>AdVideoComplete: POST /video/external/task/adVideoComplete\n{userId userLevel taskNode rewardConfig}
    Note right of AdVideoComplete: 1. 接收激励视频任务完成请求
    AdVideoComplete->>TaskList: GET /video/external/task/list\n{userLevel rewardConfig rewardRule}
    Note right of TaskList: 2. 获取用户任务列表及奖励配置
    TaskList->>StrategyService: 查询奖励策略\n{userLevel taskNode}
    alt 用户等级为L1
        StrategyService-->>TaskList: L1奖励策略\n{node6:0.01 node15:0.02}
    else 用户等级为L2/L3
        StrategyService-->>TaskList: L2_L3奖励策略\n{node10:0.01 node25:0.02}
    else 用户等级为L4
        StrategyService-->>TaskList: L4奖励策略\n{node35:0.02}
    end
    TaskList-->>AdVideoComplete: 返回任务列表\n{userLevel completedCount rewardNodes rewardRule}
    AdVideoComplete->>AdVideoComplete: 计算实际奖励值\n0.01元→1元 0.02元→2元
    Note right of AdVideoComplete: 3. 根据策略计算实际奖励
    AdVideoComplete-->>Client: 返回奖励结果\n{userLevel completedCount nodeReward actualReward}
```
### 3.2.1 激励视频任务完成接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/adVideoComplete`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. 接收用户激励视频任务完成请求
2. 获取用户基础信息（包括用户等级）
3. 根据用户等级和任务完成节点，向策略服务查询小额现金奖励配置
   - L1等级：6次节点奖励0.01元，15次节点奖励0.02元
   - L2/L3等级：10次节点奖励0.01元，25次节点奖励0.02元
   - L4等级：35次节点奖励0.02元
4. 计算奖励实际值（0.01元对应最高1元，0.02元对应最高2元）
5. 更新用户任务完成次数和奖励记录
6. 返回奖励结果，包括：用户等级、当前完成次数、节点奖励金额、奖励实际值
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收任务完成请求] --> B[获取用户信息\n及等级]
    B --> C{查询奖励配置\n根据等级?}
    C -- L1 --> D[6次:0.01\n15次:0.02]
    C -- L2/L3 --> E[10次:0.01\n25次:0.02]
    C -- L4 --> F[35次:0.02]
    D --> G[计算奖励\n实际值]
    E --> G
    F --> G
    G --> H[更新任务\n完成次数]
    H --> I[返回奖励结果\n等级/次数/金额]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,B,D,E,F,G,H,I process
    class C decision
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID|NEW",
  "userLevel": "int64|required|用户等级|NEW",
  "taskNode": "int64|required|任务完成节点|NEW",
  "rewardConfig": {
    "L1": {
      "node6": "float64|6次节点奖励金额|NEW",
      "node15": "float64|15次节点奖励金额|NEW"
    },
    "L2_L3": {
      "node10": "float64|10次节点奖励金额|NEW",
      "node25": "float64|25次节点奖励金额|NEW"
    },
    "L4": {
      "node35": "float64|35次节点奖励金额|NEW"
    }
  }
}
```
* **响应参数变更点**: 
```json
{
  "userLevel": "int|用户等级|NEW",
  "completedCount": "int|当前完成次数|NEW",
  "nodeReward": "float64|节点奖励金额|NEW",
  "actualReward": "float64|奖励实际值|NEW"
}
```

### 3.2.2 任务列表查询接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/list`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 在返回任务列表时，包含激励视频任务的小额现金奖励配置信息
2. 根据用户等级展示对应的奖励节点信息
   - L1等级：显示6次和15次节点奖励
   - L2/L3等级：显示10次和25次节点奖励
   - L4等级：显示35次节点奖励
3. 在任务详情中展示奖励实际值计算规则（0.01元对应最高1元，0.02元对应最高2元）
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取任务列表] --> B{用户等级?}
    B -- L1 --> C[展示6次\n15次奖励]
    B -- L2/L3 --> D[展示10次\n25次奖励]
    B -- L4 --> E[展示35次奖励]
    C --> F[返回任务列表]
    D --> F
    E --> F
    F --> G[获取任务详情]
    G --> H[计算奖励值\n0.01元=1元\n0.02元=2元]
    H --> I[返回详情数据]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,F,G,H,I process
    class B decision
    class C,D,E important
```
* **请求参数变更点**: 
```json
{
  "userLevel": "int64|required|用户等级|NEW",
  "rewardConfig": {
    "L1": {
      "node6": "float64|6次节点奖励金额|NEW",
      "node15": "float64|15次节点奖励金额|NEW"
    },
    "L2_L3": {
      "node10": "float64|10次节点奖励金额|NEW",
      "node25": "float64|25次节点奖励金额|NEW"
    },
    "L4": {
      "node35": "float64|35次节点奖励金额|NEW"
    }
  },
  "rewardRule": "string|奖励实际值计算规则（0.01元对应最高1元，0.02元对应最高2元）|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "userLevel": "int|用户等级，用于控制奖励节点展示逻辑|NEW",
  "completedCount": "int|当前完成次数，用于计算节点奖励|NEW",
  "rewardNodes": {
    "L1": "array|L1等级展示的节点次数[6,15]|NEW",
    "L2_L3": "array|L2/L3等级展示的节点次数[10,25]|NEW",
    "L4": "array|L4等级展示的节点次数[35]|NEW"
  },
  "rewardRule": "string|奖励实际值计算规则说明（0.01元对应最高1元，0.02元对应最高2元）|NEW",
  "nodeReward": "float64|节点奖励金额|NEW",
  "actualReward": "float64|奖励实际值|NEW"
}
```
