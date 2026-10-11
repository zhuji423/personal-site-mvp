---
title: "1. 需求背景"
description: "功能点：浏览任务倒计时控制 | 目标代码库 | 接口名称 | 接口路径 | 改动类型 | 变更概述 | 备注 | |--------------------------------------------------------------"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\data\\mock\\电商任务（下单+浏览）\\trd.md"
---
# 1. 需求背景
* **需求文档**： [【非随】【极速版存钱罐】电商任务](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-28341/show)
* **背景描述**: 存钱罐与电商结合，引导用户完成下单任务，提升收入
* **预期收益**：

# 2. 设计总览
* **功能点**：`任务状态管理`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务面板管理   | `/baiduboxapp/basic/ddmission/taskPanel` | 修改             | 展示任务列表、进度、奖励领取、个性化展示、权限检查 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频任务列表   | `/video/external/task/list` | 修改             | 展示视频任务列表、状态、奖励信息、身份校验、任务过滤 |          |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务状态管理   | `/baiduboxapp/basic/ddmission/taskStatus` | 新增             | 管理任务状态、处理状态变更、状态查询、异常处理 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频任务状态   | `/video/external/task/status` | 新增             | 管理视频任务状态、处理状态变更、状态查询、异常处理 |          |

* **功能点**：`浏览任务倒计时控制`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注** |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务面板管理 | `/baiduboxapp/basic/ddmission/taskPanel` | 修改 | 展示任务列表、进度及奖励，支持倒计时控制和个性化展示 | |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频任务列表 | `/video/external/task/list` | 修改 | 展示任务列表及状态，支持倒计时控制和任务过滤 | |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 倒计时任务管理 | `/baiduboxapp/basic/ddmission/taskTimer` | 新增 | 管理倒计时任务状态，处理状态变更和异常情况 | |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频倒计时任务 | `/video/external/task/timer` | 新增 | 管理视频倒计时任务状态，处理状态变更和异常情况 | |

* **功能点**：`下单任务处理`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务面板管理   | `/baiduboxapp/basic/ddmission/taskPanel` | 修改             | 展示用户可参与的下单任务列表，显示进度和奖励，提供领取功能 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频任务列表   | `/video/external/task/list` | 修改             | 展示用户可参与的下单任务列表，提供关键信息，激励用户参与 |          |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 下单任务状态管理   | `/baiduboxapp/basic/ddmission/taskStatus` | 新增             | 管理用户下单任务状态，处理状态变更事件，提供查询功能 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频下单任务状态管理   | `/video/external/task/status` | 新增             | 管理视频下单任务状态，处理状态变更事件，提供查询功能 |          |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 下单任务倒计时管理   | `/baiduboxapp/basic/ddmission/taskTimer` | 新增             | 管理浏览下单任务的倒计时状态，处理状态变更事件，提供查询功能 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频下单任务倒计时管理   | `/video/external/task/timer` | 新增             | 管理视频浏览下单任务的倒计时状态，处理状态变更事件，提供查询功能 |          |

* **功能点**：`退单奖励扣除`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务面板管理接口   | `/baiduboxapp/basic/ddmission/taskPanel` | 修改             | 新增退单奖励扣除任务相关功能 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频任务列表接口   | `/video/external/task/list` | 修改             | 新增退单奖励扣除任务相关功能 |          |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 退单奖励扣除接口   | `/baiduboxapp/basic/ddmission/refundReward` | 新增             | 处理退单奖励扣除请求 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频退单奖励扣除接口   | `/video/external/task/refundReward` | 新增             | 处理视频退单奖励扣除请求 |          |

* **功能点**：`风控逻辑处理`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务面板管理   | `/baiduboxapp/basic/ddmission/taskPanel` | 修改             | 增加权限检查、实验分组处理、任务分类展示逻辑 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频任务列表   | `/video/external/task/list` | 修改             | 增加身份校验、任务配置过滤、状态排序逻辑 |          |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 风控逻辑处理   | `/baiduboxapp/basic/ddmission/riskControl` | 新增             | 新增用户行为风险检查、任务状态处理功能 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 视频任务风控处理   | `/video/external/task/riskControl` | 新增             | 新增视频任务风险检查、状态处理功能 |          |

# 3. 详细设计
## 3.1 任务状态管理
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant TaskPanel as /baiduboxapp/basic/ddmission/taskPanel
    participant VideoTaskList as /video/external/task/list
    participant TaskStatus as /baiduboxapp/basic/ddmission/taskStatus
    participant VideoTaskStatus as /video/external/task/status

    Client->>TaskPanel: POST 请求任务面板数据\n参数: userId userGroup taskType\nantiCheatCheck priorityTasks
    alt 反作弊检查通过
        TaskPanel->>VideoTaskList: GET 获取视频任务列表\n透传: userId deviceId\n新增: scene version
        VideoTaskList-->>TaskPanel: 返回视频任务数据\ntaskList userInfo permission
        TaskPanel->>TaskStatus: POST 查询任务状态\n参数: userId taskId\neventType timestamp
        TaskStatus-->>TaskPanel: 返回任务状态\ntaskStatus rewardInfo
        TaskPanel-->>Client: 返回整合任务面板\ntaskList userInfo categoryList
    else 反作弊检查失败
        TaskPanel-->>Client: 返回空面板\npermission.hasAccess=false
    end

    Client->>VideoTaskStatus: POST 更新视频任务状态\n参数: userId taskId\neventType progress
    alt 视频观看完成
        VideoTaskStatus->>TaskStatus: POST 同步任务状态\n参数: taskId taskStatus\nrewardStatus
        TaskStatus-->>VideoTaskStatus: 确认状态更新\nrewardInfo
        VideoTaskStatus-->>Client: 返回奖励信息\nrewardInfo eventInfo
    else 观看中断
        VideoTaskStatus-->>Client: 返回中断状态\ntaskStatus.isInterrupted=true
    end
```
### 3.1.1 任务面板管理（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskPanel`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 展示用户可参与的任务列表，包括视频观看、签到等任务
2. 显示用户当前的任务进度和奖励情况
3. 提供任务完成后的奖励领取功能
4. 根据用户身份和属性进行个性化任务展示
5. 用户访问权限检查，包括登录状态、实验分组等
6. 反作弊检查，命中则返回空面板
7. 任务分类处理，特殊任务优先展示，普通任务根据条件过滤
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[权限检查] --> B{通过校验?}
    B -- 否 --> C[返回空面板]
    B -- 是 --> D[获取用户身份\n及属性]
    D --> E[反作弊检查]
    E --> F{命中规则?}
    F -- 是 --> C
    F -- 否 --> G[获取任务池]
    G --> H[分类处理任务]
    H --> I[特殊任务\n优先展示]
    I --> J[普通任务\n条件过滤]
    J --> K[组装任务列表]
    K --> L[获取用户\n进度数据]
    L --> M[合并展示数据]
    M --> N[奖励领取\n功能挂载]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    class A,D,G,H,I,J,K,L,M,N process
    class B,F decision
    class C,E important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID，用于身份校验和个性化展示|NEW",
  "userGroup": "string|用户实验分组信息|NEW",
  "taskType": "string|任务类型（video/signin等）|NEW",
  "taskStatus": "string|任务完成状态|NEW",
  "rewardStatus": "string|奖励领取状态|NEW",
  "antiCheatCheck": "bool|反作弊检查标记|NEW",
  "priorityTasks": "[]string|特殊任务优先展示列表|NEW",
  "filterCondition": "string|普通任务过滤条件|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskType": "string|任务类型(视频观看/签到等)|NEW",
      "taskName": "string|任务名称|NEW",
      "taskDesc": "string|任务描述|NEW",
      "taskIcon": "string|任务图标URL|NEW",
      "progress": "int|当前进度|NEW",
      "target": "int|目标进度|NEW",
      "rewardAmount": "float64|奖励金额|NEW",
      "rewardType": "string|奖励类型|NEW",
      "canClaim": "bool|是否可领取|NEW",
      "isSpecial": "bool|是否特殊任务|NEW",
      "expireTime": "string|过期时间|NEW"
    }
  ],
  "userInfo": {
    "userId": "string|用户ID|NEW",
    "isLogin": "bool|是否登录|NEW",
    "userGroup": "string|实验分组|NEW",
    "isCheat": "bool|是否作弊|NEW"
  },
  "permission": {
    "hasAccess": "bool|是否有访问权限|NEW",
    "blockReason": "string|拦截原因|NEW"
  },
  "categoryList": [
    {
      "categoryId": "string|分类ID|NEW",
      "categoryName": "string|分类名称|NEW",
      "priority": "int|展示优先级|NEW"
    }
  ]
}
```

### 3.1.2 视频任务列表（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/list`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 展示用户可参与的视频任务列表
2. 提供任务状态、奖励金额、完成进度等关键信息
3. 用户身份校验，包括登录状态和设备标识
4. 任务列表获取与过滤，根据设备、版本号、场景参数过滤不匹配的任务
5. 任务状态计算，判断任务是否可领取
6. 资产与提现信息整合，包括现金和金豆余额、提现倒计时等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[用户请求任务列表] --> B{登录状态校验?}
    B -- 是 --> C[获取设备信息\n和版本号]
    B -- 否 --> D[返回未登录错误]
    C --> E[查询可用任务池]
    E --> F{设备/版本\n匹配过滤?}
    F -- 是 --> G[计算任务状态\n和进度]
    F -- 否 --> H[过滤掉不匹配任务]
    G --> I[整合用户资产\n和提现信息]
    H --> I
    I --> J[组装返回数据]
    J --> K[返回任务列表]
    D --> K

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,E,G,H,I,J,K process
    class B,F decision
    class D important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID，用于身份校验和个性化展示|NEW",
  "deviceId": "string|required|设备标识，用于设备过滤|NEW",
  "version": "string|required|客户端版本号，用于版本过滤|NEW",
  "scene": "string|场景参数，用于场景过滤|NEW",
  "taskStatus": "string|任务完成状态|NEW",
  "rewardAmount": "float64|奖励金额|NEW",
  "progress": "int32|任务完成进度|NEW",
  "cashBalance": "float64|现金余额|NEW",
  "beanBalance": "int32|金豆余额|NEW",
  "withdrawCountdown": "int64|提现倒计时(秒)|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskType": "string|任务类型(视频观看/签到等)|NEW",
      "taskName": "string|任务名称|NEW",
      "taskDesc": "string|任务描述|NEW",
      "taskIcon": "string|任务图标URL|NEW",
      "progress": "int|当前进度|NEW",
      "target": "int|目标进度|NEW",
      "rewardAmount": "float64|奖励金额|NEW",
      "rewardType": "string|奖励类型|NEW",
      "canClaim": "bool|是否可领取|NEW",
      "isSpecial": "bool|是否特殊任务|NEW",
      "expireTime": "string|过期时间|NEW"
    }
  ],
  "userInfo": {
    "userId": "string|用户ID|NEW",
    "isLogin": "bool|是否登录|NEW",
    "userGroup": "string|实验分组|NEW",
    "isCheat": "bool|是否作弊|NEW",
    "deviceId": "string|设备标识|NEW"
  },
  "permission": {
    "hasAccess": "bool|是否有访问权限|NEW",
    "blockReason": "string|拦截原因|NEW"
  },
  "assetInfo": {
    "cashBalance": "float64|现金余额|NEW",
    "beanBalance": "int|金豆余额|NEW",
    "withdrawCountdown": "string|提现倒计时|NEW"
  },
  "filterParams": {
    "deviceType": "string|设备类型|NEW",
    "appVersion": "string|应用版本号|NEW",
    "scene": "string|场景参数|NEW"
  }
}
```

### 3.1.3 任务状态管理（新增）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskStatus`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理用户任务状态，包括任务开始、进行中、完成等状态
2. 处理任务状态变更事件，如任务完成、奖励领取等
3. 与任务面板管理接口和视频任务列表接口协同工作，确保状态一致性
4. 提供任务状态查询功能，支持按任务类型、状态等条件过滤
5. 处理任务状态异常情况，如任务中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收任务请求] --> B{请求类型?}
    B -- 状态变更 --> C[验证任务状态]
    B -- 状态查询 --> D[构建查询条件]
    C --> E{允许变更?}
    E -- 是 --> F[更新任务状态]
    E -- 否 --> G[返回错误信息]
    F --> H[同步任务面板]
    H --> I[同步视频列表]
    D --> J[查询任务状态]
    J --> K[返回结果集]
    G --> L[结束流程]
    I --> L
    K --> L
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,F,H,I,J,K process
    class B,E decision
    class G important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID，用于身份校验",
  "deviceId": "string|required|设备标识，用于设备过滤",
  "taskId": "string|required|任务唯一标识",
  "taskType": "string|required|任务类型（video/signin等）",
  "taskStatus": "string|required|任务完成状态",
  "rewardStatus": "string|奖励领取状态",
  "progress": "int32|任务完成进度",
  "eventType": "string|required|状态变更事件类型（start/progress/finish/reward等）",
  "timestamp": "int64|required|事件发生时间戳",
  "antiCheatCheck": "bool|反作弊检查标记",
  "filterCondition": {
    "statusFilter": "string|任务状态过滤条件",
    "typeFilter": "string|任务类型过滤条件"
  },
  "errorInfo": {
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskStatus": {
    "taskId": "string|任务ID",
    "taskType": "string|任务类型(视频观看/签到等)",
    "currentStatus": "string|当前状态(started/in_progress/completed)",
    "progress": "int|当前进度",
    "target": "int|目标进度",
    "lastUpdateTime": "string|最后状态更新时间",
    "expireTime": "string|过期时间",
    "canClaim": "bool|是否可领取奖励",
    "isInterrupted": "bool|是否被中断",
    "interruptReason": "string|中断原因",
    "isDuplicate": "bool|是否重复提交"
  },
  "rewardInfo": {
    "rewardAmount": "float64|奖励金额",
    "rewardType": "string|奖励类型",
    "isClaimed": "bool|是否已领取",
    "claimTime": "string|领取时间"
  },
  "userInfo": {
    "userId": "string|用户ID",
    "userGroup": "string|实验分组",
    "isCheat": "bool|是否作弊"
  },
  "errorInfo": {
    "hasError": "bool|是否有错误",
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息"
  },
  "filterParams": {
    "taskTypeFilter": "string|任务类型过滤条件",
    "statusFilter": "string|状态过滤条件",
    "timeRange": "string|时间范围过滤条件"
  }
}
```

### 3.1.4 视频任务状态（新增）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/status`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理视频任务状态，包括视频观看进度、完成状态等
2. 处理视频任务状态变更事件，如视频观看完成、奖励领取等
3. 与视频任务列表接口协同工作，确保状态一致性
4. 提供视频任务状态查询功能，支持按任务ID、状态等条件过滤
5. 处理视频任务状态异常情况，如观看中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收状态变更请求] --> B{请求类型?}
    B -- 进度更新 --> C[更新观看进度]
    B -- 完成上报 --> D[标记任务完成]
    B -- 奖励领取 --> E[发放任务奖励]
    C --> F[校验进度有效性]
    D --> F
    E --> F
    F --> G{状态异常?}
    G -- 是 --> H[记录异常日志]
    G -- 否 --> I[同步任务列表]
    H --> I
    I --> J[返回处理结果]
    K[接收查询请求] --> L{条件过滤?}
    L -- 任务ID --> M[查询单任务]
    L -- 状态筛选 --> N[批量查询]
    M --> O[返回任务数据]
    N --> O

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,I,J,K,L,M,N,O process
    class B,G decision
    class H important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID，用于身份校验",
  "deviceId": "string|required|设备标识，用于设备过滤",
  "taskId": "string|required|任务唯一标识",
  "taskType": "string|required|任务类型（video/signin等）",
  "taskStatus": "string|required|任务完成状态",
  "rewardStatus": "string|奖励领取状态",
  "progress": "int32|任务完成进度",
  "eventType": "string|required|状态变更事件类型（start/progress/finish/reward等）",
  "timestamp": "int64|required|事件发生时间戳",
  "antiCheatCheck": "bool|反作弊检查标记",
  "filterCondition": {
    "statusFilter": "string|任务状态过滤条件",
    "typeFilter": "string|任务类型过滤条件"
  },
  "errorInfo": {
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskStatus": {
    "taskId": "string|任务ID",
    "taskType": "string|任务类型(视频观看/签到等)",
    "currentStatus": "string|当前状态(started/in_progress/completed)",
    "progress": "int|当前进度",
    "target": "int|目标进度",
    "lastUpdateTime": "string|最后状态更新时间",
    "expireTime": "string|过期时间",
    "canClaim": "bool|是否可领取奖励",
    "isInterrupted": "bool|是否被中断",
    "interruptReason": "string|中断原因",
    "isDuplicate": "bool|是否重复提交",
    "videoDuration": "int|视频总时长(秒)",
    "watchedDuration": "int|已观看时长(秒)",
    "playbackRate": "float64|播放速率",
    "isMuted": "bool|是否静音",
    "resolution": "string|视频分辨率"
  },
  "rewardInfo": {
    "rewardAmount": "float64|奖励金额",
    "rewardType": "string|奖励类型",
    "isClaimed": "bool|是否已领取",
    "claimTime": "string|领取时间",
    "rewardDesc": "string|奖励描述"
  },
  "userInfo": {
    "userId": "string|用户ID",
    "userGroup": "string|实验分组",
    "isCheat": "bool|是否作弊",
    "deviceId": "string|设备标识"
  },
  "errorInfo": {
    "hasError": "bool|是否有错误",
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息",
    "retryable": "bool|是否可重试"
  },
  "filterParams": {
    "taskTypeFilter": "string|任务类型过滤条件",
    "statusFilter": "string|状态过滤条件",
    "timeRange": "string|时间范围过滤条件",
    "videoId": "string|视频ID过滤条件"
  },
  "eventInfo": {
    "eventType": "string|事件类型(watch_start/watch_progress/watch_complete/reward_claim)",
    "eventTime": "string|事件发生时间",
    "eventData": "object|事件相关数据"
  }
}
```

## 3.2 浏览任务倒计时控制
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant TaskPanel as /baiduboxapp/basic/ddmission/taskPanel
    participant VideoTaskList as /video/external/task/list
    participant TaskTimer as /baiduboxapp/basic/ddmission/taskTimer
    participant VideoTimer as /video/external/task/timer
    participant Strategy as 策略服务

    Client->>TaskPanel: POST {userId taskType taskStatus countdown rewardInfo priority}
    Note right of TaskPanel: 组装用户任务查询参数
    TaskPanel->>Strategy: GET 用户策略(userId)
    Strategy-->>TaskPanel: 返回个性化策略
    alt 有视频任务
        TaskPanel->>VideoTaskList: POST {userId taskType taskStatus countdown}
        VideoTaskList-->>TaskPanel: 返回videoTaskList
        TaskPanel->>TaskTimer: POST {userId taskType eventType:start timestamp}
        TaskTimer-->>TaskPanel: 返回countdownStatus
    else 无视频任务
        TaskPanel->>TaskTimer: POST {userId taskType eventType:query timestamp}
        TaskTimer-->>TaskPanel: 返回现有任务状态
    end
    TaskPanel-->>Client: 返回taskList userIdentity userAttributes

    Client->>VideoTimer: POST {userId taskId taskType eventType:progress progress}
    VideoTimer->>Strategy: GET 视频策略(userId deviceInfo)
    Strategy-->>VideoTimer: 返回视频奖励策略
    VideoTimer-->>Client: 返回videoProgress countdownStatus

    alt 倒计时结束
        Client->>VideoTimer: POST {userId taskId eventType:end timestamp}
        VideoTimer->>TaskTimer: POST {userId taskType eventType:sync timestamp}
        TaskTimer-->>VideoTimer: 同步成功
        VideoTimer-->>Client: 返回canReceive:true
    end
```
### 3.2.1 任务面板管理（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskPanel`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 展示用户可参与的任务列表，包括浏览任务倒计时控制
2. 显示用户当前的任务进度和奖励情况，包含倒计时信息
3. 提供任务完成后的奖励领取功能，支持倒计时结束后的奖励处理
4. 根据用户身份和属性进行个性化任务展示，包括倒计时任务的优先级调整
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户身份\n属性] --> B{是否VIP\n用户?}
    B -- 是 --> C[优先展示\nVIP任务]
    B -- 否 --> D[展示普通\n任务列表]
    C --> E[加载任务\n倒计时]
    D --> E
    E --> F[显示任务\n进度奖励]
    F --> G{任务是否\n完成?}
    G -- 是 --> H[领取奖励]
    G -- 否 --> I[更新倒计时\n显示]
    H --> J[奖励发放\n处理]
    I --> K{倒计时\n结束?}
    K -- 是 --> H
    K -- 否 --> I
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,I process
    class B,G,K decision
    class H,J important
```
* **请求参数变更点**: 
```json
{
  "tversion": "string|required|版本信息|MODIFY",
  "userId": "string|required|用户ID|NEW",
  "taskType": "string|任务类型|NEW",
  "taskStatus": "string|任务状态|NEW",
  "countdown": "int64|倒计时信息|NEW",
  "rewardInfo": {
    "rewardType": "string|奖励类型|NEW",
    "rewardAmount": "int64|奖励数量|NEW"
  },
  "priority": "int64|任务优先级|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskName": "string|任务名称|NEW",
      "taskType": "string|任务类型|NEW",
      "taskStatus": "string|任务状态|NEW",
      "progress": "string|任务进度|NEW",
      "rewardAmount": "float64|奖励金额|NEW",
      "countdown": "int64|倒计时(秒)|NEW",
      "priority": "int|任务优先级|NEW",
      "canReceive": "bool|是否可领取奖励|NEW",
      "receiveStatus": "string|领取状态|NEW"
    }
  ],
  "userIdentity": "string|用户身份标识|NEW",
  "userAttributes": "map[string]string|用户属性|NEW"
}
```

### 3.2.2 视频任务列表（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/list`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 向用户展示可参与的任务列表，包括浏览任务倒计时控制
2. 提供与任务相关的关键信息，如任务状态、奖励金额、完成进度及倒计时信息
3. 根据用户设备、版本号、场景参数过滤不匹配的任务，优先下发倒计时任务
4. 查询用户任务完成记录，判断倒计时任务是否可领取
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户信息\n设备/版本/场景] --> B{过滤\n匹配任务?}
    B -- 是 --> C[查询用户\n任务记录]
    B -- 否 --> D[返回空列表]
    C --> E{存在\n倒计时任务?}
    E -- 是 --> F[优先处理\n倒计时任务]
    E -- 否 --> G[加载常规\n任务列表]
    F --> H[计算任务\n剩余时间]
    G --> H
    H --> I[组装任务\n状态信息]
    I --> J[返回任务列表\n含倒计时/奖励]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,F,G,H,I,J process
    class B,E decision
    class F important
```
* **请求参数变更点**: 
```json
{
  "callback": "string|回调函数名|MODIFY",
  "tversion": "string|required|版本信息|NEW",
  "userId": "string|required|用户ID|NEW",
  "taskType": "string|任务类型|NEW",
  "taskStatus": "string|任务状态|NEW",
  "countdown": "int64|倒计时信息|NEW",
  "rewardInfo": {
    "rewardType": "string|奖励类型|NEW",
    "rewardAmount": "int64|奖励数量|NEW"
  },
  "priority": "int64|任务优先级|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskName": "string|任务名称|NEW",
      "taskType": "string|任务类型|NEW",
      "taskStatus": "string|任务状态|NEW",
      "progress": "string|任务进度|NEW",
      "rewardAmount": "float64|奖励金额|NEW",
      "countdown": "int64|倒计时(秒)|NEW",
      "priority": "int|任务优先级|NEW",
      "canReceive": "bool|是否可领取奖励|NEW",
      "receiveStatus": "string|领取状态|NEW"
    }
  ],
  "userIdentity": "string|用户身份标识|NEW",
  "userAttributes": "map[string]string|用户属性|NEW",
  "deviceInfo": "map[string]string|设备信息|NEW",
  "version": "string|版本号|NEW",
  "scene": "string|场景参数|NEW"
}
```

### 3.2.3 倒计时任务管理（新增）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskTimer`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理浏览任务的倒计时状态，包括倒计时开始、进行中、结束等状态
2. 处理倒计时任务状态变更事件，如倒计时结束、奖励领取等
3. 与任务面板管理接口和视频任务列表接口协同工作，确保倒计时状态一致性
4. 提供倒计时任务状态查询功能，支持按任务类型、状态等条件过滤
5. 处理倒计时任务状态异常情况，如倒计时中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收倒计时\n状态变更请求] --> B{请求类型?}
    B -- 开始 --> C[创建倒计时任务]
    B -- 结束 --> D[标记任务完成]
    B -- 领取奖励 --> E[发放任务奖励]
    C --> F[更新任务面板]
    D --> F
    E --> F
    F --> G[同步视频任务列表]
    H[查询倒计时\n任务状态] --> I{过滤条件?}
    I -- 按类型 --> J[返回对应\n任务列表]
    I -- 按状态 --> J
    G --> K[状态一致性校验]
    J --> K
    K --> L{发现异常?}
    L -- 是 --> M[处理异常状态]
    L -- 否 --> N[返回正常结果]
    M --> N

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,H,J,M,N process
    class B,I,L decision
    class K important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID",
  "taskType": "string|required|任务类型",
  "taskStatus": "string|required|任务状态",
  "countdown": "int64|倒计时信息",
  "eventType": "string|required|事件类型（倒计时开始/结束/奖励领取等）",
  "timestamp": "int64|required|事件发生时间戳",
  "rewardInfo": {
    "rewardType": "string|奖励类型",
    "rewardAmount": "int64|奖励数量"
  },
  "queryCondition": {
    "statusFilter": "string|状态过滤条件",
    "typeFilter": "string|任务类型过滤条件"
  },
  "exceptionInfo": {
    "exceptionType": "string|异常类型（中断/重复提交等）",
    "exceptionTime": "int64|异常发生时间"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID",
      "taskName": "string|任务名称",
      "taskType": "string|任务类型",
      "taskStatus": "string|任务状态",
      "progress": "string|任务进度",
      "rewardAmount": "float64|奖励金额",
      "countdown": "int64|倒计时(秒)",
      "priority": "int|任务优先级",
      "canReceive": "bool|是否可领取奖励",
      "receiveStatus": "string|领取状态",
      "countdownStatus": "string|倒计时状态(start/processing/end)",
      "countdownStartTime": "int64|倒计时开始时间戳",
      "countdownEndTime": "int64|倒计时结束时间戳",
      "isInterrupted": "bool|是否中断",
      "interruptReason": "string|中断原因",
      "isRepeated": "bool|是否重复提交"
    }
  ],
  "userIdentity": "string|用户身份标识",
  "userAttributes": "map[string]string|用户属性",
  "currentTime": "int64|当前服务器时间戳",
  "version": "string|接口版本号",
  "scene": "string|场景参数"
}
```

### 3.2.4 视频倒计时任务（新增）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/timer`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理视频浏览任务的倒计时状态，包括视频观看进度、倒计时完成状态等
2. 处理视频倒计时任务状态变更事件，如倒计时结束、奖励领取等
3. 与视频任务列表接口协同工作，确保倒计时状态一致性
4. 提供视频倒计时任务状态查询功能，支持按任务ID、状态等条件过滤
5. 处理视频倒计时任务状态异常情况，如观看中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取视频任务\n状态变更事件]
    B{事件类型\n判断?}
    C[更新倒计时\n进度状态]
    D[标记任务\n为已完成]
    E[触发奖励\n发放流程]
    F[更新任务列表\n缓存状态]
    G[记录异常\n状态信息]
    H[返回最新\n任务状态]
    I[查询任务\n状态请求]
    J{状态是否\n有效?}
    K[返回错误\n状态信息]

    A --> B
    B -- 进度更新 --> C
    B -- 倒计时结束 --> D
    D --> E
    C --> F
    B -- 异常事件 --> G
    F --> H
    I --> J
    J -- 是 --> H
    J -- 否 --> K
    E --> F
    G --> F

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    class A,C,D,E,F,G,H,I,K process
    class B,J decision
    class D,E important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID",
  "taskId": "string|required|任务ID",
  "taskType": "string|required|任务类型",
  "taskStatus": "string|required|任务状态",
  "progress": "int64|视频观看进度",
  "countdown": "int64|倒计时信息",
  "eventType": "string|required|事件类型（倒计时开始/结束/奖励领取等）",
  "timestamp": "int64|required|事件发生时间戳",
  "rewardInfo": {
    "rewardType": "string|奖励类型",
    "rewardAmount": "int64|奖励数量"
  },
  "queryCondition": {
    "taskIdFilter": "string|任务ID过滤条件",
    "statusFilter": "string|状态过滤条件"
  },
  "exceptionInfo": {
    "exceptionType": "string|异常类型（中断/重复提交等）",
    "exceptionTime": "int64|异常发生时间"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID",
      "taskName": "string|任务名称",
      "taskType": "string|任务类型",
      "taskStatus": "string|任务状态",
      "progress": "string|任务进度",
      "rewardAmount": "float64|奖励金额",
      "countdown": "int64|倒计时(秒)",
      "priority": "int|任务优先级",
      "canReceive": "bool|是否可领取奖励",
      "receiveStatus": "string|领取状态",
      "countdownStatus": "string|倒计时状态(start/processing/end)",
      "countdownStartTime": "int64|倒计时开始时间戳",
      "countdownEndTime": "int64|倒计时结束时间戳",
      "isInterrupted": "bool|是否中断",
      "interruptReason": "string|中断原因",
      "isRepeated": "bool|是否重复提交",
      "videoProgress": "float64|视频观看进度(0-1)",
      "videoDuration": "int64|视频总时长(秒)",
      "lastWatchTime": "int64|最后观看时间戳"
    }
  ],
  "userIdentity": "string|用户身份标识",
  "userAttributes": "map[string]string|用户属性",
  "currentTime": "int64|当前服务器时间戳",
  "version": "string|接口版本号",
  "scene": "string|场景参数",
  "deviceInfo": "map[string]string|设备信息",
  "errorCode": "string|异常状态码",
  "errorMsg": "string|异常信息"
}
```

## 3.3 下单任务处理
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant TaskPanel as /baiduboxapp/basic/ddmission/taskPanel
    participant VideoTaskList as /video/external/task/list
    participant TaskStatus as /baiduboxapp/basic/ddmission/taskStatus
    participant VideoTaskStatus as /video/external/task/status
    participant TaskTimer as /baiduboxapp/basic/ddmission/taskTimer
    participant VideoTaskTimer as /video/external/task/timer
    participant StrategyService as 策略服务

    Client->>TaskPanel: POST 获取任务面板\n{userId taskStatus rewardInfo personalizedTasks}
    TaskPanel->>StrategyService: GET 获取用户策略\n{userId userLevel userTags}
    StrategyService-->>TaskPanel: 返回个性化策略\n{isPersonalized taskRules}
    alt 有视频任务
        TaskPanel->>VideoTaskList: POST 获取视频任务\n{userId taskStatus rewardInfo personalizedTasks}
        VideoTaskList-->>TaskPanel: 返回视频任务列表\n{taskList userIdentity eventHandlers}
    end
    TaskPanel-->>Client: 返回任务面板数据\n{taskList userIdentity userAttributes eventHandlers}

    Client->>TaskStatus: POST 更新任务状态\n{userId taskId taskType taskStatus eventType rewardInfo}
    TaskStatus->>StrategyService: GET 验证任务策略\n{userId taskId}
    StrategyService-->>TaskStatus: 返回策略验证结果\n{isValid rewardRules}
    alt 状态变更为已完成
        TaskStatus->>TaskTimer: POST 同步倒计时状态\n{userId taskId countdownStatus eventType countdownInfo}
        TaskTimer-->>TaskStatus: 返回倒计时状态\n{taskCountdownInfo}
    end
    TaskStatus-->>Client: 返回状态更新结果\n{taskStatusInfo userInfo eventHandlers}

    Client->>VideoTaskStatus: POST 更新视频任务状态\n{userId taskId videoInfo taskStatus eventType rewardInfo}
    VideoTaskStatus->>StrategyService: GET 验证视频策略\n{userId taskId videoInfo}
    StrategyService-->>VideoTaskStatus: 返回视频策略验证\n{isValid videoRules}
    alt 状态变更为已完成
        VideoTaskStatus->>VideoTaskTimer: POST 同步视频倒计时\n{userId taskId countdownStatus eventType videoInfo countdownInfo}
        VideoTaskTimer-->>VideoTaskStatus: 返回倒计时状态\n{taskCountdownInfo}
    end
    VideoTaskStatus-->>Client: 返回状态更新结果\n{taskStatusInfo userInfo eventHandlers}

    Note right of StrategyService: 策略服务根据用户等级/标签<br/>动态生成任务规则和奖励策略
```
### 3.3.1 任务面板管理（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskPanel`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 展示用户可参与的下单任务列表
2. 显示用户当前的下单任务进度和奖励情况
3. 提供下单任务完成后的奖励领取功能
4. 根据用户身份和属性进行个性化下单任务展示
5. 处理下单任务的状态变更事件
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户身份信息] --> B{是否有效用户?}
    B -- 是 --> C[查询可参与任务]
    B -- 否 --> D[返回错误信息]
    C --> E[过滤个性化任务]
    E --> F[组装任务列表数据]
    F --> G[展示任务列表]
    G --> H{用户选择任务?}
    H -- 是 --> I[查询任务进度]
    H -- 否 --> G
    I --> J[展示进度奖励]
    J --> K{任务完成?}
    K -- 是 --> L[发放奖励]
    K -- 否 --> G
    L --> M[更新任务状态]
    M --> G

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,E,F,G,I,J,L,M process
    class B,H,K decision
    class D important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户唯一标识|NEW",
  "taskStatus": "string|任务状态（进行中/已完成/未开始等）|NEW",
  "rewardInfo": {
    "amount": "int64|奖励金额|NEW",
    "type": "string|奖励类型|NEW"
  },
  "personalizedTasks": {
    "userLevel": "int64|用户等级|NEW",
    "userTags": "[]string|用户标签列表|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskName": "string|任务名称|NEW",
      "taskDesc": "string|任务描述|NEW",
      "taskStatus": "int|任务状态(0-未开始 1-进行中 2-已完成 3-已领取)|NEW",
      "taskProgress": "int|当前任务进度|NEW",
      "taskTarget": "int|任务目标值|NEW",
      "rewardAmount": "float64|奖励金额|NEW",
      "rewardStatus": "int|奖励状态(0-未达成 1-可领取 2-已领取)|NEW",
      "startTime": "string|任务开始时间|NEW",
      "endTime": "string|任务结束时间|NEW",
      "isPersonalized": "bool|是否个性化任务|NEW"
    }
  ],
  "userIdentity": "string|用户身份标识|NEW",
  "userAttributes": "object|用户属性信息|NEW",
  "eventHandlers": {
    "statusChange": "string|状态变更事件处理器|NEW",
    "rewardClaim": "string|奖励领取事件处理器|NEW"
  }
}
```

### 3.3.2 视频任务列表（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/list`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 展示用户可参与的下单任务列表
2. 提供与下单任务相关的关键信息（如任务状态、奖励金额、完成进度等）
3. 激励用户参与下单任务并提升活跃度
4. 处理下单任务的状态计算和过滤
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户ID] --> B{用户\n是否有效}
    B -- 是 --> C[查询用户\n任务数据]
    B -- 否 --> D[返回错误\n提示]
    C --> E[计算任务\n完成状态]
    E --> F[过滤有效\n任务列表]
    F --> G[补充任务\n奖励信息]
    G --> H[排序任务\n优先级]
    H --> I[返回任务\n列表数据]
    D --> J[结束流程]
    I --> J

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,E,F,G,H,I,J process
    class B decision
    class D important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户唯一标识|NEW",
  "taskStatus": "string|任务状态（进行中/已完成/未开始等）|NEW",
  "rewardInfo": {
    "amount": "int64|奖励金额|NEW",
    "type": "string|奖励类型|NEW"
  },
  "personalizedTasks": {
    "userLevel": "int64|用户等级|NEW",
    "userTags": "[]string|用户标签列表|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务唯一标识|NEW",
      "taskName": "string|任务名称|NEW",
      "taskDesc": "string|任务详细描述|NEW",
      "taskStatus": "int|任务状态(0-未开始 1-进行中 2-已完成 3-已领取)|NEW",
      "taskProgress": "int|当前完成进度值|NEW",
      "taskTarget": "int|任务目标值|NEW",
      "rewardAmount": "float64|可获得的奖励金额|NEW",
      "rewardStatus": "int|奖励领取状态(0-未达成 1-可领取 2-已领取)|NEW",
      "startTime": "string|任务开始时间(yyyy-MM-dd HH:mm:ss)|NEW",
      "endTime": "string|任务截止时间(yyyy-MM-dd HH:mm:ss)|NEW"
    }
  ],
  "userIdentity": "string|用户唯一标识|NEW",
  "eventHandlers": {
    "statusChange": "string|任务状态变更回调地址|NEW",
    "rewardClaim": "string|奖励领取回调地址|NEW"
  }
}
```

### 3.3.3 下单任务状态管理（新增）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskStatus`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理用户下单任务状态，包括任务开始、进行中、完成等状态
2. 处理下单任务状态变更事件，如任务完成、奖励领取等
3. 与任务面板管理接口和视频任务列表接口协同工作，确保状态一致性
4. 提供下单任务状态查询功能，支持按任务类型、状态等条件过滤
5. 处理下单任务状态异常情况，如任务中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收任务请求] --> B{请求类型?}
    B -- 状态变更 --> C[验证任务状态]
    B -- 状态查询 --> D[构建查询条件]
    C --> E{状态合法?}
    E -- 是 --> F[更新任务状态]
    E -- 否 --> G[记录异常日志]
    F --> H[同步任务面板]
    D --> I[获取任务列表]
    H --> J[返回处理结果]
    I --> J
    G --> K[返回错误信息]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,F,H,I,J,K process
    class B,E decision
    class G important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户唯一标识",
  "taskId": "string|required|任务唯一标识",
  "taskType": "string|required|任务类型",
  "taskStatus": "string|required|任务状态（未开始/进行中/已完成/已中断）",
  "eventType": "string|required|状态变更事件类型（开始/完成/领取奖励/中断）",
  "rewardInfo": {
    "amount": "int64|奖励金额",
    "type": "string|奖励类型",
    "received": "bool|是否已领取"
  },
  "queryCondition": {
    "taskType": "string|查询条件-任务类型",
    "taskStatus": "string|查询条件-任务状态",
    "startTime": "int64|查询条件-任务开始时间范围起始",
    "endTime": "int64|查询条件-任务开始时间范围结束"
  },
  "errorInfo": {
    "code": "string|异常错误码",
    "message": "string|异常描述信息",
    "retryable": "bool|是否可重试"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskStatusInfo": {
    "taskId": "string|任务ID",
    "taskName": "string|任务名称",
    "taskDesc": "string|任务描述",
    "currentStatus": "int|当前任务状态(0-未开始 1-进行中 2-已完成 3-已领取)",
    "progress": "int|当前任务进度",
    "target": "int|任务目标值",
    "rewardInfo": {
      "amount": "float64|奖励金额",
      "status": "int|奖励状态(0-未达成 1-可领取 2-已领取)"
    },
    "startTime": "string|任务开始时间",
    "endTime": "string|任务结束时间",
    "isPersonalized": "bool|是否个性化任务"
  },
  "userInfo": {
    "userId": "string|用户唯一标识",
    "userAttributes": "object|用户属性信息"
  },
  "eventHandlers": {
    "statusChange": "string|状态变更事件处理器",
    "rewardClaim": "string|奖励领取事件处理器",
    "errorHandler": "string|异常处理回调地址"
  },
  "errorInfo": {
    "hasError": "bool|是否发生异常",
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息"
  },
  "timestamp": "string|接口响应时间戳"
}
```

### 3.3.4 视频下单任务状态管理（新增）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/status`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理视频下单任务状态，包括视频观看进度、完成状态等
2. 处理视频下单任务状态变更事件，如视频观看完成、奖励领取等
3. 与视频任务列表接口协同工作，确保状态一致性
4. 提供视频下单任务状态查询功能，支持按任务ID、状态等条件过滤
5. 处理视频下单任务状态异常情况，如观看中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收状态变更事件] --> B{事件类型?}
    B -- 观看进度更新 --> C[更新观看进度]
    B -- 视频完成 --> D[标记任务完成]
    B -- 奖励领取 --> E[更新奖励状态]
    C --> F[同步任务列表]
    D --> F
    E --> F
    F --> G{状态异常?}
    G -- 是 --> H[记录异常日志]
    G -- 否 --> I[返回成功响应]
    J[接收查询请求] --> K{过滤条件?}
    K -- 按任务ID --> L[查询单任务]
    K -- 按状态 --> M[批量查询]
    L --> N[返回任务详情]
    M --> N
    H --> I

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,H,I,J,L,M,N process
    class B,G,K decision
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户唯一标识",
  "taskId": "string|required|任务唯一标识",
  "videoInfo": {
    "progress": "int64|视频观看进度（百分比）",
    "duration": "int64|视频总时长（秒）",
    "currentPosition": "int64|当前播放位置（秒）"
  },
  "taskStatus": "string|required|任务状态（未开始/进行中/已完成/已中断）",
  "eventType": "string|required|状态变更事件类型（开始/完成/领取奖励/中断）",
  "rewardInfo": {
    "amount": "int64|奖励金额",
    "type": "string|奖励类型",
    "received": "bool|是否已领取"
  },
  "queryCondition": {
    "taskId": "string|查询条件-任务ID",
    "taskStatus": "string|查询条件-任务状态",
    "startTime": "int64|查询条件-任务开始时间范围起始",
    "endTime": "int64|查询条件-任务开始时间范围结束"
  },
  "errorInfo": {
    "code": "string|异常错误码",
    "message": "string|异常描述信息",
    "retryable": "bool|是否可重试"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskStatusInfo": {
    "taskId": "string|任务ID",
    "taskName": "string|任务名称",
    "taskDesc": "string|任务描述",
    "currentStatus": "int|当前任务状态(0-未开始 1-进行中 2-已完成 3-已领取)",
    "progress": "int|当前任务进度",
    "target": "int|任务目标值",
    "videoInfo": {
      "videoId": "string|视频ID",
      "videoDuration": "int|视频总时长(秒)",
      "watchedDuration": "int|已观看时长(秒)",
      "watchProgress": "float64|观看进度百分比",
      "isCompleted": "bool|是否观看完成"
    },
    "rewardInfo": {
      "amount": "float64|奖励金额",
      "status": "int|奖励状态(0-未达成 1-可领取 2-已领取)"
    },
    "startTime": "string|任务开始时间",
    "endTime": "string|任务结束时间",
    "isPersonalized": "bool|是否个性化任务"
  },
  "userInfo": {
    "userId": "string|用户唯一标识",
    "userAttributes": "object|用户属性信息"
  },
  "eventHandlers": {
    "statusChange": "string|状态变更事件处理器",
    "rewardClaim": "string|奖励领取事件处理器",
    "errorHandler": "string|异常处理回调地址"
  },
  "errorInfo": {
    "hasError": "bool|是否发生异常",
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息",
    "errorType": "string|错误类型(watch_interrupted-观看中断 duplicate_submission-重复提交)"
  },
  "timestamp": "string|接口响应时间戳"
}
```

### 3.3.5 下单任务倒计时管理（新增）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskTimer`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理浏览下单任务的倒计时状态，包括倒计时开始、进行中、结束等状态
2. 处理倒计时下单任务状态变更事件，如倒计时结束、奖励领取等
3. 与任务面板管理接口和视频任务列表接口协同工作，确保倒计时状态一致性
4. 提供倒计时下单任务状态查询功能，支持按任务类型、状态等条件过滤
5. 处理倒计时下单任务状态异常情况，如倒计时中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[开始倒计时] --> B{倒计时\n结束?}
    B -- 否 --> C[更新倒计时状态]
    C --> B
    B -- 是 --> D[触发结束事件]
    D --> E{奖励\n可领取?}
    E -- 是 --> F[发放奖励]
    E -- 否 --> G[标记任务完成]
    F --> G
    G --> H[同步任务面板]
    H --> I[更新视频任务列表]
    J[查询任务状态] --> K{状态\n异常?}
    K -- 是 --> L[处理异常状态]
    K -- 否 --> M[返回状态数据]
    L --> M
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,F,G,H,I,J,L,M process
    class B,E,K decision
    class D,F important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户唯一标识",
  "taskId": "string|required|任务唯一标识",
  "taskType": "string|required|任务类型",
  "countdownStatus": "string|required|倒计时状态（未开始/进行中/已结束）",
  "eventType": "string|required|状态变更事件类型（开始/结束/领取奖励/中断）",
  "countdownInfo": {
    "startTime": "int64|倒计时开始时间",
    "endTime": "int64|倒计时结束时间",
    "remainingTime": "int64|剩余时间（秒）"
  },
  "rewardInfo": {
    "amount": "int64|奖励金额",
    "type": "string|奖励类型",
    "received": "bool|是否已领取"
  },
  "queryCondition": {
    "taskType": "string|查询条件-任务类型",
    "countdownStatus": "string|查询条件-倒计时状态",
    "startTime": "int64|查询条件-任务开始时间范围起始",
    "endTime": "int64|查询条件-任务开始时间范围结束"
  },
  "errorInfo": {
    "code": "string|异常错误码",
    "message": "string|异常描述信息",
    "retryable": "bool|是否可重试"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskCountdownInfo": {
    "taskId": "string|任务ID",
    "taskName": "string|任务名称",
    "taskDesc": "string|任务描述",
    "currentStatus": "int|当前任务状态(0-未开始 1-进行中 2-已完成 3-已领取)",
    "countdownStatus": "int|倒计时状态(0-未开始 1-进行中 2-已结束)",
    "remainingTime": "int|剩余时间(秒)",
    "progress": "int|当前任务进度",
    "target": "int|任务目标值",
    "rewardInfo": {
      "amount": "float64|奖励金额",
      "status": "int|奖励状态(0-未达成 1-可领取 2-已领取)"
    },
    "startTime": "string|任务开始时间",
    "endTime": "string|任务结束时间",
    "isPersonalized": "bool|是否个性化任务"
  },
  "userInfo": {
    "userId": "string|用户唯一标识",
    "userAttributes": "object|用户属性信息"
  },
  "eventHandlers": {
    "statusChange": "string|状态变更事件处理器",
    "rewardClaim": "string|奖励领取事件处理器",
    "countdownEnd": "string|倒计时结束事件处理器",
    "errorHandler": "string|异常处理回调地址"
  },
  "errorInfo": {
    "hasError": "bool|是否发生异常",
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息",
    "errorType": "string|错误类型(countdown_interrupted-倒计时中断 duplicate_submission-重复提交)"
  },
  "timestamp": "string|接口响应时间戳"
}
```

### 3.3.6 视频下单任务倒计时管理（新增）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/timer`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 管理视频浏览下单任务的倒计时状态，包括视频观看进度、倒计时完成状态等
2. 处理视频倒计时下单任务状态变更事件，如倒计时结束、奖励领取等
3. 与视频任务列表接口协同工作，确保倒计时状态一致性
4. 提供视频倒计时下单任务状态查询功能，支持按任务ID、状态等条件过滤
5. 处理视频倒计时下单任务状态异常情况，如观看中断、重复提交等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收任务状态变更事件] --> B{事件类型?}
    B -- 倒计时结束 --> C[更新任务状态\n为已完成]
    B -- 奖励领取 --> D[标记奖励已发放]
    B -- 观看中断 --> E[记录中断时间\n更新进度]
    C --> F[同步状态到\n任务列表]
    D --> F
    E --> F
    F --> G{状态异常?}
    G -- 是 --> H[触发异常处理\n流程]
    G -- 否 --> I[返回处理结果]
    H --> I
    J[接收查询请求] --> K{过滤条件?}
    K -- 按任务ID --> L[查询单个任务\n状态]
    K -- 按状态 --> M[批量查询\n任务列表]
    L --> N[返回任务详情]
    M --> N
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,H,I,J,L,M,N process
    class B,G,K decision
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户唯一标识",
  "taskId": "string|required|任务唯一标识",
  "taskType": "string|required|任务类型",
  "countdownStatus": "string|required|倒计时状态（未开始/进行中/已结束）",
  "eventType": "string|required|状态变更事件类型（开始/结束/领取奖励/中断）",
  "videoInfo": {
    "progress": "int64|视频观看进度（百分比）",
    "duration": "int64|视频总时长（秒）",
    "currentPosition": "int64|当前播放位置（秒）"
  },
  "countdownInfo": {
    "startTime": "int64|倒计时开始时间",
    "endTime": "int64|倒计时结束时间",
    "remainingTime": "int64|剩余时间（秒）"
  },
  "rewardInfo": {
    "amount": "int64|奖励金额",
    "type": "string|奖励类型",
    "received": "bool|是否已领取"
  },
  "queryCondition": {
    "taskId": "string|查询条件-任务ID",
    "taskStatus": "string|查询条件-任务状态",
    "countdownStatus": "string|查询条件-倒计时状态",
    "startTime": "int64|查询条件-任务开始时间范围起始",
    "endTime": "int64|查询条件-任务开始时间范围结束"
  },
  "errorInfo": {
    "code": "string|异常错误码",
    "message": "string|异常描述信息",
    "retryable": "bool|是否可重试"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskCountdownInfo": {
    "taskId": "string|任务ID",
    "taskName": "string|任务名称",
    "taskDesc": "string|任务描述",
    "currentStatus": "int|当前任务状态(0-未开始 1-进行中 2-已完成 3-已领取)",
    "countdownStatus": "int|倒计时状态(0-未开始 1-进行中 2-已结束)",
    "remainingTime": "int|剩余时间(秒)",
    "progress": "int|当前任务进度",
    "target": "int|任务目标值",
    "videoInfo": {
      "videoId": "string|视频ID",
      "videoDuration": "int|视频总时长(秒)",
      "watchedDuration": "int|已观看时长(秒)",
      "watchProgress": "float64|观看进度百分比",
      "isCompleted": "bool|是否观看完成"
    },
    "rewardInfo": {
      "amount": "float64|奖励金额",
      "status": "int|奖励状态(0-未达成 1-可领取 2-已领取)"
    },
    "startTime": "string|任务开始时间",
    "endTime": "string|任务结束时间",
    "isPersonalized": "bool|是否个性化任务"
  },
  "userInfo": {
    "userId": "string|用户唯一标识",
    "userAttributes": "object|用户属性信息"
  },
  "eventHandlers": {
    "statusChange": "string|状态变更事件处理器",
    "rewardClaim": "string|奖励领取事件处理器",
    "countdownEnd": "string|倒计时结束事件处理器",
    "errorHandler": "string|异常处理回调地址"
  },
  "errorInfo": {
    "hasError": "bool|是否发生异常",
    "errorCode": "string|错误码",
    "errorMsg": "string|错误信息",
    "errorType": "string|错误类型(watch_interrupted-观看中断 duplicate_submission-重复提交 countdown_interrupted-倒计时中断)"
  },
  "timestamp": "string|接口响应时间戳"
}
```

## 3.4 退单奖励扣除
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant TaskPanel as /baiduboxapp/basic/ddmission/taskPanel
    participant VideoTaskList as /video/external/task/list
    participant RefundReward as /baiduboxapp/basic/ddmission/refundReward
    participant VideoRefund as /video/external/task/refundReward
    participant PolicyService as 策略服务

    Client->>TaskPanel: GET 任务面板数据\n{tversion userId userType showRefundTask taskProgress}
    TaskPanel->>PolicyService: 获取用户策略\n{userId userType}
    PolicyService-->>TaskPanel: 返回策略\n{userIdentity userAttributes}
    alt showRefundTask=true
        TaskPanel->>RefundReward: 查询退单状态\n{userId refundOrderId}
        RefundReward-->>TaskPanel: 返回扣除状态\n{deductionStatus remainingBalance}
    else showRefundTask=false
        TaskPanel->>VideoTaskList: 获取视频任务\n{userId userType}
        VideoTaskList-->>TaskPanel: 返回任务列表\n{taskList}
    end
    TaskPanel-->>Client: 返回任务面板\n{taskList userIdentity userAttributes}

    Client->>RefundReward: POST 退单奖励扣除\n{userId refundOrderId deductAmount}
    RefundReward->>PolicyService: 验证扣除权限\n{userId userIdentity}
    PolicyService-->>RefundReward: 返回验证结果\n{canDeduct maxAmount}
    alt canDeduct=true
        RefundReward->>RefundReward: 执行扣除\n{deductAmount}
        RefundReward-->>Client: 返回扣除结果\n{deductionResult deductionStatus}
    else canDeduct=false
        RefundReward-->>Client: 返回错误\n{error: 无扣除权限}
    end

    Client->>VideoRefund: POST 视频退单扣除\n{userId videoOrderId deductAmount}
    VideoRefund->>PolicyService: 验证视频扣除\n{userId userIdentity}
    PolicyService-->>VideoRefund: 返回视频策略\n{canDeductVideo}
    alt canDeductVideo=true
        VideoRefund->>VideoRefund: 执行视频扣除\n{deductAmount}
        VideoRefund-->>Client: 返回视频扣除结果\n{deductionResult videoInfo}
    else canDeductVideo=false
        VideoRefund-->>Client: 返回错误\n{error: 视频扣除失败}
    end
```
### 3.4.1 任务面板管理接口（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskPanel`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 展示用户可参与的任务列表，包括退单奖励扣除任务
2. 显示用户当前的任务进度和奖励情况，包括退单奖励扣除状态
3. 提供任务完成后的奖励领取功能，包括退单奖励扣除的领取
4. 根据用户身份和属性进行个性化任务展示，包括退单奖励扣除任务的展示
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户身份\n属性] --> B{是否展示\n退单任务?}
    B -- 是 --> C[加载常规任务\n+退单任务]
    B -- 否 --> D[仅加载常规任务]
    C --> E[合并任务列表]
    D --> E
    E --> F[获取用户\n任务进度]
    F --> G[计算可领\n取奖励]
    G --> H{用户点击\n领取奖励?}
    H -- 是 --> I[校验任务\n完成状态]
    H -- 否 --> J[结束流程]
    I --> K{包含退单\n奖励扣除?}
    K -- 是 --> L[执行奖励\n扣除逻辑]
    K -- 否 --> M[发放常规\n奖励]
    L --> N[更新奖励\n记录]
    M --> N
    N --> O[返回领取\n结果]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,I,J,L,M,N,O process
    class B,H,K decision
    class L important
```
* **请求参数变更点**: 
```json
{
  "tversion": "string|required|版本信息|MODIFY",
  "userId": "string|required|用户ID|NEW",
  "userType": "string|用户类型|NEW",
  "showRefundTask": "bool|是否展示退单奖励扣除任务|NEW",
  "taskProgress": {
    "refundDeductionStatus": "string|退单奖励扣除状态|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskName": "string|任务名称|NEW",
      "taskType": "string|任务类型(常规任务/退单奖励扣除任务)|NEW",
      "taskStatus": "string|任务状态(未开始/进行中/已完成)|NEW",
      "progress": "string|当前任务进度|NEW",
      "rewardAmount": "float64|奖励金额|NEW",
      "deductionStatus": "string|退单奖励扣除状态(未扣除/已扣除)|NEW",
      "canReceive": "bool|是否可领取奖励|NEW",
      "isPersonalized": "bool|是否个性化展示|NEW"
    }
  ],
  "userIdentity": "string|用户身份标识|NEW",
  "userAttributes": "object|用户属性信息|NEW"
}
```

### 3.4.2 视频任务列表接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/list`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 展示用户可参与的任务列表，包括退单奖励扣除任务
2. 显示用户当前的任务进度和奖励情况，包括退单奖励扣除状态
3. 提供任务完成后的奖励领取功能，包括退单奖励扣除的领取
4. 根据用户身份和属性进行个性化任务展示，包括退单奖励扣除任务的展示
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户身份\n属性] --> B{是否包含\n退单记录?}
    B -- 是 --> C[加载退单奖励\n扣除任务]
    B -- 否 --> D[加载常规任务]
    C --> E[合并任务列表]
    D --> E
    E --> F[展示任务列表\n及进度]
    F --> G{用户点击\n领取奖励?}
    G -- 是 --> H{是否退单\n奖励任务?}
    G -- 否 --> F
    H -- 是 --> I[执行奖励扣除\n逻辑]
    H -- 否 --> J[发放常规奖励]
    I --> K[更新任务状态]
    J --> K
    K --> F

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,I,J,K process
    class B,G,H decision
    class I important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID|NEW",
  "userType": "string|用户类型|NEW",
  "showRefundTask": "bool|是否展示退单奖励扣除任务|NEW",
  "taskProgress": {
    "refundDeductionStatus": "string|退单奖励扣除状态|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskName": "string|任务名称|NEW",
      "taskType": "string|任务类型(常规任务/退单奖励扣除任务)|NEW",
      "taskStatus": "string|任务状态(未开始/进行中/已完成)|NEW",
      "progress": "string|当前任务进度|NEW",
      "rewardAmount": "float64|奖励金额|NEW",
      "deductionStatus": "string|退单奖励扣除状态(未扣除/已扣除)|NEW",
      "canReceive": "bool|是否可领取奖励|NEW",
      "isPersonalized": "bool|是否个性化展示|NEW"
    }
  ],
  "userIdentity": "string|用户身份标识|NEW",
  "userAttributes": "object|用户属性信息|NEW"
}
```

### 3.4.3 退单奖励扣除接口（新增）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/refundReward`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 处理用户退单奖励扣除请求
2. 检查用户退单奖励扣除条件
3. 扣除用户奖励
4. 更新用户奖励状态
5. 返回扣除结果
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收退单请求]
    B{满足扣除\n条件?}
    C[扣除用户奖励]
    D[更新奖励状态]
    E[返回操作结果]
    F[返回失败原因]

    A --> B
    B -- 是 --> C --> D --> E
    B -- 否 --> F

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F process
    class B decision
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID",
  "userType": "string|用户类型",
  "refundOrderId": "string|required|退单ID",
  "deductAmount": "int64|required|扣除奖励金额",
  "deductReason": "string|扣除原因",
  "taskProgress": {
    "refundDeductionStatus": "string|退单奖励扣除状态"
  }
}
```
* **响应参数变更点**: 
```json
{
  "deductionResult": {
    "success": "bool|扣除是否成功",
    "deductedAmount": "float64|实际扣除金额",
    "remainingBalance": "float64|扣除后剩余余额"
  },
  "deductionStatus": "string|退单奖励扣除状态(未扣除/已扣除/部分扣除)",
  "orderInfo": {
    "orderId": "string|退单订单ID",
    "originalReward": "float64|原始奖励金额",
    "deductionReason": "string|扣除原因"
  },
  "userInfo": {
    "userId": "string|用户ID",
    "userIdentity": "string|用户身份标识",
    "rewardBalance": "float64|当前奖励余额"
  },
  "timestamp": "int64|扣除操作时间戳"
}
```

### 3.4.4 视频退单奖励扣除接口（新增）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/refundReward`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 处理用户视频退单奖励扣除请求
2. 检查用户视频退单奖励扣除条件
3. 扣除用户视频奖励
4. 更新用户视频奖励状态
5. 返回扣除结果
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收退单请求] --> B{满足\n扣除条件?}
    B -- 是 --> C[扣除视频奖励]
    B -- 否 --> D[返回失败结果]
    C --> E[更新奖励状态]
    E --> F[返回成功结果]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,E,F process
    class B decision
    class D important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID",
  "userType": "string|用户类型",
  "videoOrderId": "string|required|视频订单ID",
  "deductAmount": "int64|required|扣除奖励金额",
  "deductReason": "string|扣除原因",
  "taskProgress": {
    "refundDeductionStatus": "string|退单奖励扣除状态"
  }
}
```
* **响应参数变更点**: 
```json
{
  "deductionResult": {
    "success": "bool|扣除是否成功",
    "deductedAmount": "float64|实际扣除金额",
    "remainingBalance": "float64|扣除后剩余余额"
  },
  "deductionStatus": "string|退单奖励扣除状态(未扣除/已扣除/部分扣除)",
  "videoInfo": {
    "videoId": "string|视频ID",
    "originalReward": "float64|原始奖励金额",
    "deductionReason": "string|扣除原因"
  },
  "userInfo": {
    "userId": "string|用户ID",
    "userIdentity": "string|用户身份标识",
    "rewardBalance": "float64|当前奖励余额"
  },
  "timestamp": "int64|扣除操作时间戳"
}
```

## 3.5 风控逻辑处理
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant TaskPanel as /baiduboxapp/basic/ddmission/taskPanel
    participant VideoTask as /video/external/task/list
    participant RiskControl as /baiduboxapp/basic/ddmission/riskControl
    participant VideoRisk as /video/external/task/riskControl

    Client->>TaskPanel: POST 请求任务面板数据\n参数: tversion talosLiteParams city experimentGroup
    Note right of TaskPanel: 1. 检查用户访问权限\n2. 解析实验分组信息
    TaskPanel->>RiskControl: GET 风控检查\n参数: userId actionType=check checkParams
    alt 存在风险行为
        RiskControl-->>TaskPanel: 返回风险等级及限制措施\nriskLevel riskControlActions
        TaskPanel-->>Client: 返回受限任务面板\nisRiskUser taskList=[]
    else 正常用户
        TaskPanel->>VideoTask: GET 获取视频任务\n参数: tversion talosLiteParams experimentGroup
        VideoTask->>VideoRisk: GET 视频风控检查\n参数: userId actionType=query
        VideoRisk-->>VideoTask: 返回视频任务状态\nvideoTaskStatus watchBehavior
        VideoTask-->>TaskPanel: 返回过滤后任务列表\ntaskList userAssets
        TaskPanel-->>Client: 返回完整任务面板\ntaskList userAssets personalizedConfig
    end

    Note left of RiskControl: 风控状态变更时同步流程
    RiskControl->>TaskPanel: POST 状态同步\n参数: taskStatusSync=true
    RiskControl->>VideoRisk: POST 状态同步\n参数: taskStatusSync=true
    VideoRisk->>VideoTask: POST 状态同步\n参数: syncStatus=true
```
### 3.5.1 任务面板管理（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskPanel`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 检查用户访问权限，包括苹果审核状态、访问渠道和登录状态
2. 解析请求参数并记录用户实验分组信息
3. 获取基础任务数据并进行反作弊检查
4. 按任务类型分类处理，优先展示特殊任务
5. 组装展示信息，包括用户资产信息、任务状态和进度、可领取奖励提示等
6. 根据用户所在城市和实验分组进行个性化处理
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[检查用户权限\n苹果审核/渠道/登录]
    B{权限有效?}
    C[解析请求参数\n记录实验分组]
    D[获取基础任务数据\n反作弊检查]
    E{任务类型\n为特殊任务?}
    F[优先处理\n特殊任务]
    G[处理普通任务]
    H[组装展示信息\n资产/状态/奖励]
    I{需要城市\n个性化?}
    J[应用城市\n个性化配置]
    K[返回结果数据]

    A --> B
    B -- 是 --> C
    B -- 否 --> K
    C --> D
    D --> E
    E -- 是 --> F
    E -- 否 --> G
    F --> H
    G --> H
    H --> I
    I -- 是 --> J
    I -- 否 --> K
    J --> K

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    class A,C,D,F,G,H,J,K process
    class B,E,I decision
```
* **请求参数变更点**: 
```json
{
  "tversion": "string|required|版本信息|MODIFY",
  "talosLiteParams": {
    "appleReviewStatus": "string|苹果审核状态|NEW",
    "accessChannel": "string|访问渠道|NEW",
    "loginStatus": "string|required|登录状态|NEW"
  },
  "city": "string|用户所在城市|NEW",
  "experimentGroup": "string|用户实验分组信息|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "isAppleReview": "bool|是否苹果审核状态|NEW",
  "accessChannel": "string|访问渠道(web/app等)|NEW",
  "isLogin": "bool|是否已登录|NEW",
  "expGroup": "string|用户实验分组信息|NEW",
  "userAssets": {
    "balance": "float64|用户余额|NEW",
    "points": "int|用户积分|NEW"
  },
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskType": "string|任务类型|NEW",
      "priority": "int|任务优先级|NEW",
      "status": "string|任务状态|NEW",
      "progress": "int|任务进度|NEW",
      "rewardTips": "string|可领取奖励提示|NEW"
    }
  ],
  "cityCode": "string|用户所在城市编码|NEW",
  "personalizedConfig": "string|个性化配置信息|NEW"
}
```

### 3.5.2 视频任务列表（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/list`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 校验用户身份和设备标识
2. 从配置系统加载所有任务配置并根据用户设备、版本号、场景参数过滤
3. 查询用户任务完成记录并判断任务是否可领取
4. 获取用户当前现金和金豆余额并计算提现倒计时
5. 根据A/B实验调整任务排序和文案
6. 按任务状态排序并返回结构化数据
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[校验用户身份\n设备标识]
    B{校验通过?}
    C[加载任务配置\n过滤条件]
    D[查询用户\n任务记录]
    E{任务可领取?}
    F[获取用户\n余额信息]
    G[计算提现\n倒计时]
    H[应用A/B实验\n调整内容]
    I[按状态排序\n任务数据]
    J[返回结构化\n响应数据]

    A --> B
    B -- 是 --> C
    B -- 否 --> J
    C --> D
    D --> E
    E -- 是 --> F
    E -- 否 --> H
    F --> G
    G --> H
    H --> I
    I --> J

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,F,G,H,I,J process
    class B,E decision
```
* **请求参数变更点**: 
```json
{
  "callback": "string|回调函数名|MODIFY",
  "tversion": "string|required|版本信息|NEW",
  "talosLiteParams": {
    "appleReviewStatus": "string|苹果审核状态|NEW",
    "accessChannel": "string|访问渠道|NEW",
    "loginStatus": "string|required|登录状态|NEW"
  },
  "city": "string|用户所在城市|NEW",
  "experimentGroup": "string|用户实验分组信息|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "isLogin": "bool|是否已登录|NEW",
  "deviceId": "string|设备唯一标识|NEW",
  "userAssets": {
    "balance": "float64|用户现金余额|NEW",
    "points": "int|用户金豆余额|NEW",
    "withdrawCountdown": "int|提现倒计时(秒)|NEW"
  },
  "expGroup": "string|用户A/B实验分组信息|NEW",
  "taskList": [
    {
      "taskId": "string|任务ID|NEW",
      "taskType": "string|任务类型|NEW",
      "priority": "int|任务优先级(受实验影响)|NEW",
      "status": "string|任务状态(未开始/进行中/可领取/已完成)|NEW",
      "progress": "int|任务当前进度|NEW",
      "targetProgress": "int|任务目标进度|NEW",
      "rewardTips": "string|奖励文案(受实验影响)|NEW",
      "configSource": "string|任务配置来源|NEW"
    }
  ],
  "filterParams": {
    "deviceType": "string|设备类型|NEW",
    "version": "string|客户端版本号|NEW",
    "scene": "string|场景参数|NEW"
  }
}
```

### 3.5.3 风控逻辑处理（新增）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/riskControl`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 检查用户行为风险，包括异常任务完成频率、奖励领取频率等
2. 处理高风险用户的任务状态，如暂停任务参与资格
3. 与任务面板管理接口和视频任务列表接口协同工作，确保风控状态一致性
4. 提供风控状态查询功能，支持按用户ID、风险等级等条件过滤
5. 处理风控状态变更事件，如风险解除、重新开放任务参与资格等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收用户行为数据]
    B{存在风险行为?}
    C[更新风控状态]
    D[同步任务面板状态]
    E[同步视频任务状态]
    F[记录风控日志]
    G[触发状态变更通知]
    H{风险解除?}
    I[解除风控限制]
    J[查询风控状态]
    K[返回过滤结果]

    A --> B
    B -- 是 --> C
    B -- 否 --> J
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H -- 是 --> I
    H -- 否 --> J
    I --> J
    J --> K

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    class A,C,D,E,F,G,I,J,K process
    class B,H decision
    class C,F important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID",
  "riskLevel": "int64|风险等级",
  "actionType": "string|required|操作类型（check/update/query）",
  "checkParams": {
    "taskCompleteFrequency": "int64|任务完成频率",
    "rewardClaimFrequency": "int64|奖励领取频率"
  },
  "updateParams": {
    "taskStatus": "string|任务状态（suspend/resume）",
    "riskStatus": "string|风险状态（resolved/reopened）"
  },
  "queryParams": {
    "filterByRiskLevel": "boolean|是否按风险等级过滤",
    "filterByUserId": "boolean|是否按用户ID过滤"
  },
  "tversion": "string|required|版本信息",
  "talosLiteParams": {
    "accessChannel": "string|访问渠道",
    "loginStatus": "string|required|登录状态"
  }
}
```
* **响应参数变更点**: 
```json
{
  "riskLevel": "string|风险等级(low/medium/high)",
  "riskType": "string|风险类型(abnormal_frequency/reward_abuse/suspicious_behavior)",
  "isRiskUser": "bool|是否高风险用户",
  "riskControlActions": {
    "suspendTask": "bool|是否暂停任务参与资格",
    "limitReward": "bool|是否限制奖励领取",
    "banDuration": "int|封禁时长(秒)"
  },
  "riskDetails": [
    {
      "behaviorType": "string|行为类型(task_completion/reward_claim)",
      "frequency": "int|行为频率(次/小时)",
      "threshold": "int|风控阈值(次/小时)",
      "lastTriggerTime": "string|最后一次触发时间"
    }
  ],
  "taskStatusSync": {
    "taskPanelSync": "bool|是否需要同步任务面板状态",
    "videoTaskSync": "bool|是否需要同步视频任务状态"
  },
  "recoveryInfo": {
    "estimatedRecoveryTime": "string|预计恢复时间",
    "autoRecovery": "bool|是否自动恢复"
  },
  "queryParams": {
    "userId": "string|用户ID",
    "deviceId": "string|设备ID",
    "riskLevelFilter": "string|风险等级过滤条件"
  }
}
```

### 3.5.4 视频任务风控处理（新增）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/task/riskControl`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 检查视频任务相关风险，包括异常视频观看行为、奖励领取频率等
2. 处理高风险用户的视频任务状态，如暂停视频任务参与资格
3. 与视频任务列表接口协同工作，确保风控状态一致性
4. 提供视频任务风控状态查询功能，支持按用户ID、风险等级等条件过滤
5. 处理视频任务风控状态变更事件，如风险解除、重新开放视频任务参与资格等
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取用户视频\n任务数据] --> B{存在风险\n行为?}
    B -- 是 --> C[标记高风险\n用户]
    B -- 否 --> D[更新正常\n状态]
    C --> E[暂停任务\n资格]
    D --> F[同步任务\n列表状态]
    E --> F
    F --> G{需要查询\n风控状态?}
    G -- 是 --> H[返回过滤后\n结果]
    G -- 否 --> I[结束流程]
    H --> I
    J[接收状态\n变更事件] --> K{风险解除?}
    K -- 是 --> L[恢复任务\n资格]
    K -- 否 --> M[保持限制\n状态]
    L --> N[同步更新\n风控状态]
    M --> N
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,H,J,L,M,N process
    class B,G,K decision
    class C,E,L important
```
* **请求参数变更点**: 
```json
{
  "userId": "string|required|用户ID",
  "riskLevel": "int64|风险等级",
  "actionType": "string|required|操作类型（check/update/query）",
  "checkParams": {
    "videoWatchBehavior": "string|视频观看行为",
    "rewardClaimFrequency": "int64|奖励领取频率",
    "taskCompleteFrequency": "int64|任务完成频率"
  },
  "updateParams": {
    "taskStatus": "string|任务状态（suspend/resume）",
    "riskStatus": "string|风险状态（resolved/reopened）"
  },
  "queryParams": {
    "filterByRiskLevel": "boolean|是否按风险等级过滤",
    "filterByUserId": "boolean|是否按用户ID过滤"
  },
  "tversion": "string|required|版本信息",
  "talosLiteParams": {
    "accessChannel": "string|访问渠道",
    "loginStatus": "string|required|登录状态"
  }
}
```
* **响应参数变更点**: 
```json
{
  "riskLevel": "string|风险等级(low/medium/high)",
  "riskType": "string|风险类型(abnormal_frequency/reward_abuse/suspicious_behavior)",
  "isRiskUser": "bool|是否高风险用户",
  "riskControlActions": {
    "suspendTask": "bool|是否暂停任务参与资格",
    "limitReward": "bool|是否限制奖励领取",
    "banDuration": "int|封禁时长(秒)"
  },
  "riskDetails": [
    {
      "behaviorType": "string|行为类型(task_completion/reward_claim)",
      "frequency": "int|行为频率(次/小时)",
      "threshold": "int|风控阈值(次/小时)",
      "lastTriggerTime": "string|最后一次触发时间"
    }
  ],
  "taskStatusSync": {
    "taskPanelSync": "bool|是否需要同步任务面板状态",
    "videoTaskSync": "bool|是否需要同步视频任务状态"
  },
  "recoveryInfo": {
    "estimatedRecoveryTime": "string|预计恢复时间",
    "autoRecovery": "bool|是否自动恢复"
  },
  "queryParams": {
    "userId": "string|用户ID",
    "deviceId": "string|设备ID",
    "riskLevelFilter": "string|风险等级过滤条件"
  },
  "videoTaskStatus": {
    "isSuspended": "bool|是否暂停视频任务参与资格",
    "suspendedReason": "string|暂停原因",
    "suspendedTime": "string|暂停时间",
    "reopenTime": "string|重新开放时间"
  },
  "watchBehavior": {
    "abnormalCount": "int|异常观看次数",
    "lastAbnormalTime": "string|最后一次异常观看时间",
    "watchFrequency": "int|观看频率(次/小时)"
  },
  "rewardClaim": {
    "claimCount": "int|奖励领取次数",
    "lastClaimTime": "string|最后一次领取时间",
    "claimFrequency": "int|领取频率(次/小时)"
  },
  "syncStatus": {
    "taskListSync": "bool|是否需要同步视频任务列表状态",
    "lastSyncTime": "string|最后一次同步时间"
  }
}
```
