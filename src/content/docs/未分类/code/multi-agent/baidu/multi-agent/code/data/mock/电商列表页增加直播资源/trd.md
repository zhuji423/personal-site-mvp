---
title: "1. 需求背景"
description: "功能点：直播资源点击交互处理 | 目标代码库 | 接口名称 | 接口路径 | 改动类型 | 变更概述 | 备注 | |----------------|----------|----------|---------|--------|---"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\data\\mock\\电商列表页增加直播资源\\trd.md"
---
# 1. 需求背景
* **需求文档**： [【非随】【极速版存钱罐】电商列表页增加直播资源](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-30802/show)
* **背景描述**: 当前线上电商大盘中，电商直播的购买转化率高于商品列表，在电商任务中增加电商直播内容，提升购买转化率
* **预期收益**：

# 2. 设计总览
* **功能点**：`直播资源信息透传`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 电商商品列表接口   | `/baiduboxapp/basic/ddmission/ecommerceList` | 修改             | 获取直播资源信息并进行数据预处理 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 电商直播混排接口   | `/video/external/ecommerce/list` | 修改             | 直播资源与商品信息混排及全Tab适配 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 直播订单状态接口   | `/ecommerce/external/orderchange` | 修改             | 直播订单状态同步与特殊处理 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 直播浏览完成接口   | `/video/external/ecommerce/browseComplete` | 修改             | 直播观看行为记录与专属奖励处理 |          |

* **功能点**：`直播资源点击交互处理`
| **目标代码库** | **接口名称** | **接口路径** | **改动类型** | **变更概述** | **备注** |
|----------------|----------|----------|---------|--------|--------|

* **功能点**：`奖励发放提示处理`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 订单状态变更处理接口    | `/ecommerce/external/orderchange`                          | 修改 | 处理订单状态变更并生成奖励记录 |          |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务面板数据接口   | `/baiduboxapp/basic/ddmission/taskPanel` | 修改             | 整合奖励信息到任务面板 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 浏览任务完成接口   | `/video/external/ecommerce/browseComplete` | 修改             | 处理购买触发的浏览任务奖励 |          |

* **功能点**：`商品和直播下单统计区分`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注**                     |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------------------------|
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 订单状态变更处理器 | `/ecommerce/external/orderchange` | 修改 | 订单数据区分处理、奖励发放逻辑适配、数据存储准备 |          |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 商品列表展示器 | `/video/external/ecommerce/list` | 修改 | 商品来源标识、任务展示区分、数据采集 |          |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 商品数据分类器 | `/baiduboxapp/basic/ddmission/ecommerceList` | 修改 | 数据源分类、列表组织、元数据补充 |          |

* **功能点**：`电商任务报表数据扩展`
| **目标代码库**                                                                                                                   | **接口名称** | **接口路径**                        | **改动类型** | **变更概述** | **备注** |
|-----------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|---------|--------|----------|
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 任务面板数据扩展接口 | `/baiduboxapp/basic/ddmission/taskPanel` | 修改 | 增加电商任务数据分类处理与结果组装 | |
| [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master) | 电商商品数据接口 | `/baiduboxapp/basic/ddmission/ecommerceList` | 修改 | 扩展商品数据返回结构与分页逻辑 | |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 电商任务列表接口 | `/video/external/ecommerce/list` | 修改 | 增强任务奖励数据整合与数据上报 | |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 电商订单状态接口 | `/ecommerce/external/orderchange` | 修改 | 完善订单类型识别与奖励处理逻辑 | |
| [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master) | 电商浏览完成接口 | `/video/external/ecommerce/browseComplete` | 修改 | 任务类型区分与奖励发放优化 | |

# 3. 详细设计
## 3.1 直播资源信息透传
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant SboxBasic as /baiduboxapp/basic/ddmission/ecommerceList
    participant VideoEcommerce as /video/external/ecommerce/list
    participant OrderChange as /ecommerce/external/orderchange
    participant BrowseComplete as /video/external/ecommerce/browseComplete

    Client->>SboxBasic: 获取直播商品列表\n参数: src isSSR categoryName pageNo pageSize productImages productInfo
    Note right of SboxBasic: 数据预处理\n1. 格式校验\n2. 补充扩展字段
    SboxBasic-->>Client: 返回goodsList pageInfo

    alt 需要混排展示
        Client->>VideoEcommerce: 请求混排数据\n透传: src isSSR pageNo pageSize\n新增: callback tabType mixStrategy
        VideoEcommerce->>SboxBasic: 获取原始数据\n参数: src categoryName pageNo pageSize
        SboxBasic-->>VideoEcommerce: 原始goodsList
        Note left of VideoEcommerce: 混排逻辑处理\n1. 智能排序\n2. Tab权重适配
        VideoEcommerce-->>Client: 返回增强goodsList\n新增: showPriority liveBadge interactionParams
    end

    loop 订单状态监听
        Client->>OrderChange: 注册订单监听\n参数: callback src productInfo
        OrderChange-->>Client: 推送orderStatus liveInfo
    end

    Client->>BrowseComplete: 上报浏览行为\n参数: callback src behaviorType rewardInfo
    alt 是直播行为
        BrowseComplete-->>Client: 返回liveRewards\n包含: watchDuration interactionCount
    else 常规行为
        BrowseComplete-->>Client: 返回goodsList\n包含: browseComplete browseDuration
    end
```
### 3.1.1 电商商品列表接口（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/ecommerceList`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 从电商侧获取直播资源信息
   - 获取商品图、商品信息、标签、价格等基础数据
   - 支持按分类和分页参数获取直播商品列表
2. 数据预处理
   - 对直播商品信息进行基础格式校验
   - 补充商品展示所需的扩展字段
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取直播资源\n参数] --> B{参数校验?}
    B -- 是 --> C[请求电商API\n获取商品数据]
    B -- 否 --> D[返回参数错误]
    C --> E{数据格式\n校验?}
    E -- 是 --> F[补充扩展字段]
    E -- 否 --> G[返回数据异常]
    F --> H[返回处理后的\n商品列表]
    D --> I[结束流程]
    G --> I
    H --> I

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,F,H process
    class B,E decision
    class D,G important
```
* **请求参数变更点**: 
```json
{
  "src": "string|required|数据来源标识|MODIFY",
  "isSSR": "bool|是否服务端渲染|MODIFY",
  "categoryName": "string|商品分类名称|MODIFY",
  "pageNo": "int|required|分页页码|MODIFY",
  "pageSize": "int|required|分页大小|MODIFY",
  "productImages": "array|商品图片列表|NEW",
  "productInfo": {
    "title": "string|商品标题|NEW",
    "tags": "array|商品标签|NEW",
    "price": "float|商品价格|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "goodsList": [
    {
      "goodsId": "string|商品ID|NEW",
      "goodsImage": "string|商品图片URL|NEW",
      "goodsTitle": "string|商品标题|NEW",
      "goodsDesc": "string|商品描述|NEW",
      "goodsTags": "[]string|商品标签列表|NEW",
      "goodsPrice": "float64|商品价格|NEW",
      "goodsCategory": "string|商品分类|NEW",
      "isLive": "bool|是否在直播中|NEW",
      "liveStartTime": "int64|直播开始时间戳|NEW",
      "liveEndTime": "int64|直播结束时间戳|NEW"
    }
  ],
  "pageInfo": {
    "pageNum": "int|当前页码|NEW",
    "pageSize": "int|每页数量|NEW",
    "total": "int|总数|NEW"
  }
}
```

### 3.1.2 电商直播混排接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/ecommerce/list`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. 直播资源与商品信息混排
   - 接收电商商品列表接口的原始数据
   - 按业务规则将直播资源与常规商品进行智能混排
2. 全Tab适配
   - 确保混排后的列表支持在所有Tab下展示
   - 处理不同Tab场景下的展示权重差异
3. 结果组装
   - 生成最终客户端所需的展示数据结构
   - 补充直播特有的展示标识和交互参数
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收商品列表数据] --> B{是否包含\n直播资源?}
    B -- 是 --> C[提取直播资源]
    B -- 否 --> D[常规商品处理]
    C --> E[智能混排逻辑]
    D --> E
    E --> F{当前Tab\n类型?}
    F -- 首页 --> G[提高直播权重]
    F -- 其他 --> H[标准权重处理]
    G --> I[组装展示数据]
    H --> I
    I --> J[补充直播参数]
    J --> K[返回客户端数据]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,G,H,I,J,K process
    class B,F decision
    class E,I important
```
* **请求参数变更点**: 
```json
{
  "callback": "string|回调函数名|MODIFY",
  "src": "string|required|数据来源标识|NEW",
  "isSSR": "bool|是否服务端渲染|NEW",
  "pageNo": "int|required|分页页码|NEW",
  "pageSize": "int|required|分页大小|NEW",
  "productImages": "array|商品图片列表|NEW",
  "productInfo": {
    "title": "string|商品标题|NEW",
    "tags": "array|商品标签|NEW",
    "price": "float|商品价格|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "goodsList": [
    {
      "goodsId": "string|商品ID|NEW",
      "goodsImage": "string|商品图片URL|NEW",
      "goodsTitle": "string|商品标题|NEW",
      "goodsDesc": "string|商品描述|NEW",
      "goodsTags": "[]string|商品标签列表|NEW",
      "goodsPrice": "float64|商品价格|NEW",
      "goodsCategory": "string|商品分类|NEW",
      "isLive": "bool|是否在直播中|NEW",
      "liveStartTime": "int64|直播开始时间戳|NEW",
      "liveEndTime": "int64|直播结束时间戳|NEW",
      "showPriority": "int|展示优先级（用于不同Tab权重控制）|NEW",
      "liveBadge": "string|直播角标标识|NEW",
      "interactionParams": "object|直播特有交互参数|NEW"
    }
  ],
  "pageInfo": {
    "pageNum": "int|当前页码|NEW",
    "pageSize": "int|每页数量|NEW",
    "total": "int|总数|NEW"
  },
  "tabType": "string|当前Tab类型标识|NEW",
  "mixStrategy": "string|混排策略标识|NEW"
}
```

### 3.1.3 直播订单状态接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/ecommerce/external/orderchange`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 直播订单状态同步
   - 监听直播场景产生的订单状态变更
   - 特殊处理直播专属商品的订单状态流转
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[监听订单\n状态变更] --> B{是否直播\n专属商品?}
    B -- 是 --> C[获取直播\n专属配置]
    C --> D[校验直播\n订单状态]
    D --> E{状态是否\n合法?}
    B -- 否 --> F[标准订单\n处理流程]
    E -- 是 --> G[更新直播\n订单状态]
    E -- 否 --> H[记录异常\n日志]
    G --> I[通知直播\n系统]
    F --> J[完成标准\n状态同步]
    H --> J
    I --> J
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,F,G,I,J process
    class B,E decision
    class H important
```
* **请求参数变更点**: 
```json
{
  "callback": "string|required|回调函数名|MODIFY",
  "src": "string|required|数据来源标识|NEW",
  "productInfo": {
    "title": "string|商品标题|NEW",
    "tags": "array|商品标签|NEW",
    "price": "float|商品价格|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "orderId": "string|直播订单ID|NEW",
  "goodsId": "string|商品ID|NEW",
  "orderStatus": "string|订单状态（pending/paid/shipped/completed/cancelled）|NEW",
  "isLiveGoods": "bool|是否直播专属商品|NEW",
  "liveInfo": {
    "liveId": "string|关联直播场次ID|NEW",
    "liveStartTime": "int64|直播开始时间戳|NEW",
    "liveEndTime": "int64|直播结束时间戳|NEW"
  },
  "statusUpdateTime": "int64|状态变更时间戳|NEW"
}
```

### 3.1.4 直播浏览完成接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/ecommerce/browseComplete`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. 直播观看行为记录
   - 捕获用户在直播间的商品浏览完成事件
   - 区分常规浏览与直播场景的特殊浏览行为
2. 直播专属奖励处理
   - 处理直播场景特有的奖励规则计算
   - 记录直播相关的用户行为数据
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[捕获浏览事件] --> B{直播场景?\n特殊浏览行为}
    B -- 是 --> C[记录直播\n行为数据]
    B -- 否 --> D[常规浏览\n处理]
    C --> E[计算直播\n专属奖励]
    D --> F[标准奖励\n处理]
    E --> G[更新用户\n奖励数据]
    F --> G
    G --> H[存储行为\n记录]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,H process
    class B decision
```
* **请求参数变更点**: 
```json
{
  "callback": "string|required|回调函数名|MODIFY",
  "src": "string|required|数据来源标识|NEW",
  "isSSR": "bool|是否服务端渲染|NEW",
  "productInfo": {
    "title": "string|商品标题|NEW",
    "tags": "array|商品标签|NEW",
    "price": "float|商品价格|NEW"
  },
  "behaviorType": "string|required|浏览行为类型（常规/直播）|NEW",
  "rewardInfo": {
    "ruleId": "string|奖励规则ID|NEW",
    "amount": "float|奖励金额|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "isLive": "bool|是否直播场景|NEW",
  "goodsList": [
    {
      "goodsId": "string|商品ID|NEW",
      "browseComplete": "bool|商品浏览是否完成|NEW",
      "browseDuration": "int64|浏览持续时间(ms)|NEW"
    }
  ],
  "liveRewards": {
    "rewardType": "string|奖励类型(live_special/normal)|NEW",
    "rewardAmount": "float64|奖励金额|NEW",
    "behaviorData": {
      "watchDuration": "int64|观看时长(ms)|NEW",
      "interactionCount": "int|互动次数|NEW"
    }
  }
}
```

## 3.2 直播资源点击交互处理
```mermaid
sequenceDiagram
    participant client as 客户端
    participant upstream as /api/upstream
    participant downstream as /v1/downstream
    participant policy as /policy/strategy

    client->>upstream: POST /api/upstream\n{userId:123 deviceId:xyz}
    Note right of upstream: 参数校验 & 基础处理
    upstream->>downstream: GET /v1/downstream\n?userId=123
    alt 存在用户数据
        downstream-->>upstream: {status:200 data:{pref:"A"}}
        upstream->>policy: POST /policy/strategy\n{userId:123 pref:"A"}
        policy-->>upstream: {strategy:"custom_A"}
    else 无用户数据
        downstream-->>upstream: {status:404}
        upstream->>policy: POST /policy/strategy\n{userId:123 pref:"default"}
        policy-->>upstream: {strategy:"fallback"}
    end
    upstream-->>client: 200 {result:"success" strategyType}
```

## 3.3 奖励发放提示处理
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant OrderChange as /ecommerce/external/orderchange
    participant TaskPanel as /baiduboxapp/basic/ddmission/taskPanel
    participant BrowseComplete as /video/external/ecommerce/browseComplete

    Client->>OrderChange: POST 订单状态变更\n{orderId productId status...}
    Note right of OrderChange: 1.验证订单状态合法性\n2.匹配商品奖励规则
    alt 订单状态有效
        OrderChange->>OrderChange: 生成奖励记录\n{rewardRecord rewardRule}
        OrderChange->>TaskPanel: 推送奖励通知\n{notification productInfo}
        TaskPanel->>TaskPanel: 组织展示逻辑\n{priority showTime}
        OrderChange->>BrowseComplete: 触发浏览任务检查\n{browseTaskStatus}
        alt 浏览任务完成
            BrowseComplete->>BrowseComplete: 计算额外奖励\n{additionalReward}
            BrowseComplete->>TaskPanel: 更新奖励信息\n{notification priority}
        else 浏览任务未完成
            BrowseComplete->>TaskPanel: 基础奖励通知\n{notification}
        end
        TaskPanel-->>Client: 整合奖励面板数据
    else 订单状态无效
        OrderChange-->>Client: 返回错误响应
    end
```
### 3.3.1 订单状态变更处理接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/ecommerce/external/orderchange`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 接收直播间内购买商品的通知
2. 验证订单状态变更的合法性
3. 根据购买商品信息匹配对应的奖励规则
4. 生成奖励发放记录（包括奖励类型和数量）
5. 构造奖励发放提示信息（包含商品名称、奖励金额等关键要素）
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收购买通知] --> B{订单状态\n合法?}
    B -- 是 --> C[匹配奖励规则]
    B -- 否 --> D[结束流程]
    C --> E[生成奖励记录]
    E --> F[构造提示信息]
    F --> G[发送奖励通知]
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,E,F,G process
    class B decision
    class D important
```
* **请求参数变更点**: 
```json
{
  "callback": {
    "orderId": "string|required|订单ID|NEW",
    "productId": "string|required|商品ID|NEW",
    "productName": "string|商品名称|NEW",
    "rewardType": "string|奖励类型|NEW",
    "rewardAmount": "int64|奖励数量|NEW",
    "status": "string|required|订单状态|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "orderId": "string|直播间订单ID|NEW",
  "orderStatus": "string|订单状态(待支付/已支付/已取消)|NEW",
  "productInfo": {
    "productName": "string|商品名称|NEW",
    "productPrice": "float64|商品价格|NEW"
  },
  "rewardRule": {
    "ruleId": "string|奖励规则ID|NEW",
    "rewardType": "string|奖励类型(积分/优惠券)|NEW",
    "rewardAmount": "float64|奖励数量|NEW"
  },
  "rewardRecord": {
    "recordId": "string|奖励记录ID|NEW",
    "createTime": "string|记录创建时间|NEW"
  },
  "notification": {
    "title": "string|奖励通知标题|NEW",
    "content": "string|奖励通知内容(包含商品名称和奖励金额)|NEW"
  }
}
```

### 3.3.2 任务面板数据接口（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskPanel`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 接收来自订单变更接口的奖励发放通知
2. 将奖励提示信息整合到用户任务面板数据中
3. 组织奖励提示的展示逻辑（包括排序优先级、时效性控制）
4. 补充与奖励相关的运营信息（如倒计时提示）
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收奖励通知] --> B{订单有效?}
    B -- 是 --> C[整合任务数据]
    B -- 否 --> D[丢弃通知]
    C --> E{需补充运营信息?}
    E -- 是 --> F[添加倒计时\n提示信息]
    E -- 否 --> G[设置默认\n展示逻辑]
    F --> H[组织展示逻辑]
    G --> H
    H --> I[更新用户\n任务面板]
    D --> J[流程结束]
    I --> J

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,F,G,H,I process
    class B,E decision
    class D,J important
```
* **请求参数变更点**: 
```json
{
  "callback": {
    "orderId": "string|required|订单ID|NEW",
    "productId": "string|required|商品ID|NEW",
    "productName": "string|商品名称|NEW",
    "rewardType": "string|奖励类型|NEW",
    "rewardAmount": "int64|奖励数量|NEW",
    "status": "string|required|订单状态|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "orderId": "string|直播间订单ID|NEW",
  "orderStatus": "string|订单状态(待支付/已支付/已取消)|NEW",
  "productInfo": {
    "productName": "string|商品名称|NEW",
    "productPrice": "float64|商品价格|NEW"
  },
  "rewardRule": {
    "ruleId": "string|奖励规则ID|NEW",
    "rewardType": "string|奖励类型(积分/优惠券)|NEW",
    "rewardAmount": "float64|奖励数量|NEW"
  },
  "rewardRecord": {
    "recordId": "string|奖励记录ID|NEW",
    "createTime": "string|记录创建时间|NEW",
    "expireTime": "string|奖励过期时间|NEW"
  },
  "notification": {
    "title": "string|奖励通知标题|NEW",
    "content": "string|奖励通知内容(包含商品名称和奖励金额)|NEW",
    "priority": "int|展示优先级(数值越大优先级越高)|NEW",
    "showTime": "string|展示截止时间|NEW"
  }
}
```

### 3.3.3 浏览任务完成接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/ecommerce/browseComplete`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. 接收商品购买完成后的浏览任务状态更新
2. 验证购买行为与浏览任务的关联性
3. 补充处理因购买触发的额外浏览任务奖励
4. 返回整合后的完整奖励提示信息
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收购买状态\n更新请求]
    B{验证购买\n与任务关联?}
    C[查询关联\n浏览任务]
    D[计算基础\n任务奖励]
    E{存在额外\n奖励条件?}
    F[计算额外\n奖励]
    G[整合奖励\n数据]
    H[返回完整\n奖励信息]

    A --> B
    B -- 是 --> C
    B -- 否 --> H
    C --> D
    D --> E
    E -- 是 --> F
    E -- 否 --> G
    F --> G
    G --> H

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,F,G,H process
    class B,E decision
```
* **请求参数变更点**: 
```json
{
  "callback": {
    "orderId": "string|required|订单ID|NEW",
    "productId": "string|required|商品ID|NEW",
    "productName": "string|商品名称|NEW",
    "rewardType": "string|奖励类型|NEW",
    "rewardAmount": "int64|奖励数量|NEW",
    "status": "string|required|订单状态|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "orderId": "string|直播间订单ID|NEW",
  "orderStatus": "string|订单状态(待支付/已支付/已取消)|NEW",
  "productInfo": {
    "productName": "string|商品名称|NEW",
    "productPrice": "float64|商品价格|NEW"
  },
  "rewardRule": {
    "ruleId": "string|奖励规则ID|NEW",
    "rewardType": "string|奖励类型(积分/优惠券)|NEW",
    "rewardAmount": "float64|奖励数量|NEW"
  },
  "rewardRecord": {
    "recordId": "string|奖励记录ID|NEW",
    "createTime": "string|记录创建时间|NEW",
    "expireTime": "string|奖励过期时间|NEW"
  },
  "notification": {
    "title": "string|奖励通知标题|NEW",
    "content": "string|奖励通知内容(包含商品名称和奖励金额)|NEW",
    "priority": "int|展示优先级(数值越大优先级越高)|NEW",
    "showTime": "string|展示截止时间|NEW"
  },
  "browseTaskStatus": "string|浏览任务状态(已完成/未完成)|NEW",
  "additionalReward": {
    "amount": "float64|额外奖励金额|NEW",
    "description": "string|额外奖励描述|NEW"
  }
}
```

## 3.4 商品和直播下单统计区分
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant OrderService as /ecommerce/external/orderchange
    participant VideoService as /video/external/ecommerce/list
    participant BasicService as /baiduboxapp/basic/ddmission/ecommerceList

    Client->>OrderService: POST 订单状态变更\n{orderType rewardRule operationLog.sourceType}
    Note right of OrderService: 根据orderType区分商品/直播订单
    alt 商品订单
        OrderService->>VideoService: GET 商品列表\n{sourceType:常规商品 taskTag rewardDesc}
        VideoService->>BasicService: GET 基础商品数据\n{src:常规商品 sourceType:常规商品}
        BasicService-->>VideoService: 返回常规商品数据\n{sourceType typeTag:常规}
        VideoService-->>OrderService: 返回商品信息\n{sourceType:常规商品 taskInfo.isLiveTask:false}
    else 直播订单
        OrderService->>VideoService: GET 商品列表\n{sourceType:直播商品 taskTag rewardDesc}
        VideoService->>BasicService: GET 基础商品数据\n{src:直播商品 sourceType:直播商品}
        BasicService-->>VideoService: 返回直播商品数据\n{sourceType typeTag:直播}
        VideoService-->>OrderService: 返回商品信息\n{sourceType:直播商品 taskInfo.isLiveTask:true}
    end
    Note left of OrderService: 根据sourceType匹配奖励规则
    OrderService-->>Client: 返回订单变更结果\n{orderSourceType rewardRule orderChangeLogs}
```
### 3.4.1 订单状态变更处理器（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/ecommerce/external/orderchange`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 订单数据区分处理
   - 识别订单来源类型（商品订单/直播订单）
   - 根据订单类型打标并记录到订单变更日志
2. 奖励发放逻辑适配
   - 根据订单类型（商品/直播）匹配不同的奖励规则
   - 在发放奖励时记录订单类型标识
3. 数据存储准备
   - 在订单状态变更记录中增加订单类型字段
   - 确保所有订单操作日志包含来源类型信息
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[接收订单数据] --> B{订单类型?\n商品/直播}
    B -- 商品订单 --> C[打标商品订单]
    B -- 直播订单 --> D[打标直播订单]
    C --> E[记录订单\n变更日志]
    D --> E
    E --> F{奖励规则\n匹配}
    F -- 商品订单 --> G[应用商品\n奖励规则]
    F -- 直播订单 --> H[应用直播\n奖励规则]
    G --> I[记录奖励\n发放日志]
    H --> I
    I --> J[更新订单\n状态记录]
    J --> K[存储完整\n订单日志]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,G,H,I,J,K process
    class B,F decision
```
* **请求参数变更点**: 
```json
{
  "orderType": "string|required|订单来源类型（商品订单/直播订单）|NEW",
  "rewardRule": "string|根据订单类型匹配的奖励规则|NEW",
  "operationLog": {
    "sourceType": "string|required|订单来源类型信息|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "orderSourceType": "string|订单来源类型（商品订单/直播订单）|NEW",
  "rewardRule": "string|奖励规则标识（根据订单类型匹配）|NEW",
  "orderChangeLogs": [
    {
      "orderTypeTag": "string|订单类型标签|NEW",
      "sourceType": "string|订单来源类型（商品/直播）|NEW"
    }
  ]
}
```

### 3.4.2 商品列表展示器（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/ecommerce/list`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. 商品来源标识
   - 在返回的商品数据中明确标注商品来源（常规商品/直播商品）
2. 任务展示区分
   - 对直播商品展示专属任务标识
   - 在任务奖励说明中区分商品类型奖励差异
3. 数据采集
   - 记录用户对不同类型商品的浏览行为
   - 在用户操作日志中标记商品来源类型
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取商品数据]
    B{商品来源\n类型?}
    C[标注常规商品]
    D[标注直播商品]
    E[展示任务标识]
    F[记录浏览行为]
    G[标记操作日志]
    H[返回商品数据]

    A --> B
    B -- 常规 --> C
    B -- 直播 --> D
    D --> E
    C --> F
    D --> F
    F --> G
    G --> H

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,H process
    class B decision
    class E important
```
* **请求参数变更点**: 
```json
{
  "callback": "string|回调函数名|MODIFY",
  "sourceType": "string|required|商品来源类型（常规商品/直播商品）|NEW",
  "taskTag": "string|直播商品专属任务标识|NEW",
  "rewardDesc": "string|根据商品类型区分的奖励说明|NEW",
  "operationLog": {
    "sourceType": "string|required|商品来源类型信息|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "sourceType": "string|商品来源类型（常规商品/直播商品）|NEW",
  "taskInfo": {
    "isLiveTask": "bool|是否直播专属任务|NEW",
    "rewardDesc": "string|奖励说明（根据商品类型展示差异）|NEW"
  },
  "behaviorLog": {
    "viewSourceType": "string|浏览商品来源类型（常规/直播）|NEW"
  },
  "operationLog": {
    "sourceType": "string|操作商品来源类型（常规/直播）|NEW"
  }
}
```

### 3.4.3 商品数据分类器（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/ecommerceList`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 数据源分类
   - 在获取原始商品数据时区分直播商品和常规商品
2. 列表组织
   - 支持按商品类型（直播/常规）进行筛选
   - 在分页逻辑中保持类型一致性
3. 元数据补充
   - 为每个商品附加类型标识字段
   - 确保返回数据结构包含商品分类维度
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取原始商品数据] --> B{直播商品\nor常规商品?}
    B -- 直播 --> C[标记为直播商品]
    B -- 常规 --> D[标记为常规商品]
    C --> E[按类型筛选]
    D --> E
    E --> F{需要分页?}
    F -- 是 --> G[执行分页逻辑]
    F -- 否 --> H[返回全量数据]
    G --> I[补充类型标识]
    H --> I
    I --> J[附加分类维度]
    J --> K[返回结构化数据]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,G,H,I,J,K process
    class B,F decision
    class I,J important
```
* **请求参数变更点**: 
```json
{
  "src": "string|required|数据源分类（直播商品/常规商品）|MODIFY",
  "sourceType": "string|required|商品来源类型（常规商品/直播商品）|NEW",
  "categoryName": "string|商品分类维度|MODIFY"
}
```
* **响应参数变更点**: 
```json
{
  "sourceType": "string|商品来源类型（常规商品/直播商品）|NEW",
  "items": [
    {
      "typeTag": "string|商品类型标签（常规/直播）|NEW",
      "category": "string|商品分类维度|NEW"
    }
  ]
}
```

## 3.5 电商任务报表数据扩展
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant TaskPanel as /baiduboxapp/basic/ddmission/taskPanel
    participant EcommerceList as /baiduboxapp/basic/ddmission/ecommerceList
    participant VideoEcommerce as /video/external/ecommerce/list
    participant OrderChange as /ecommerce/external/orderchange
    participant BrowseComplete as /video/external/ecommerce/browseComplete

    Client->>TaskPanel: 请求电商任务面板数据\n包含ecommerceTaskData参数
    Note right of TaskPanel: 参数组装\nproductOrderCount\nliveOrderCount\ntotalOrderCount
    TaskPanel->>EcommerceList: 获取商品数据\n传递orderType/productType
    alt 商品类型为普通商品
        EcommerceList-->>TaskPanel: 返回productOrderCount
    else 商品类型为直播商品
        EcommerceList-->>TaskPanel: 返回liveOrderCount
    end
    TaskPanel->>VideoEcommerce: 请求任务奖励规则\n传递taskType=product/live
    VideoEcommerce-->>TaskPanel: 返回rewardRules\nproductOrderReward/liveOrderReward
    TaskPanel-->>Client: 返回ecommerceTaskReport\n包含分类统计数据和奖励规则

    Client->>OrderChange: 提交订单状态变更\n传递orderType/taskType
    Note left of OrderChange: 根据orderType\n差异化处理奖励
    OrderChange->>BrowseComplete: 同步浏览状态\n传递taskType
    BrowseComplete-->>OrderChange: 返回browseRecords\nproductBrowseCount/liveBrowseCount
    OrderChange-->>Client: 返回orderStatistics\n和差异化奖励
```
### 3.5.1 任务面板数据扩展接口（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/taskPanel`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 在任务面板数据组装阶段，增加电商任务数据分类处理：
   - 区分商品下单数据和直播下单数据
   - 计算并整合整体下单数据
2. 扩展结果组装逻辑：
   - 在返回数据中新增电商任务报表专用字段
   - 包含商品下单量、直播下单量、总下单量三类核心指标
3. 保持原有任务展示逻辑的同时，确保新增电商数据不影响其他任务类型展示
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取任务面板数据] --> B{电商任务\n类型?}
    B -- 是 --> C[区分商品下单\n和直播下单数据]
    B -- 否 --> D[保持原有\n处理逻辑]
    C --> E[计算商品\n下单量]
    C --> F[计算直播\n下单量]
    E --> G[整合总\n下单量]
    F --> G
    G --> H[组装电商\n报表字段]
    D --> I[原有结果\n组装逻辑]
    H --> J[合并返回\n数据]
    I --> J
    J --> K[返回任务\n面板数据]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,H,I,J,K process
    class B decision
    class H important
```
* **请求参数变更点**: 
```json
{
  "ecommerceTaskData": {
    "productOrderCount": "int64|商品下单量|NEW",
    "liveOrderCount": "int64|直播下单量|NEW",
    "totalOrderCount": "int64|总下单量|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "ecommerceTaskReport": {
    "productOrderCount": "int|商品下单量|NEW",
    "liveOrderCount": "int|直播下单量|NEW",
    "totalOrderCount": "int|总下单量|NEW"
  }
}
```

### 3.5.2 电商商品数据接口（修改）
* **代码库**: [baidu/searchbox/sbox-basic](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/searchbox/sbox-basic/tree/master)
* **接口路径**: `/baiduboxapp/basic/ddmission/ecommerceList`
* **调用方式**: `GET`
* **变更功能描述**: 
```
1. 扩展商品数据返回结构：
   - 在商品基础信息中增加下单类型标识字段（商品/直播）
   - 补充商品关联的下单统计数据
2. 优化分页逻辑：
   - 支持按商品类型（普通商品/直播商品）筛选
3. 数据预处理：
   - 对商品下单数据进行分类汇总计算
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取请求参数] --> B{包含type\n筛选条件?}
    B -- 是 --> C[按type筛选\n商品列表]
    B -- 否 --> D[获取全部\n商品列表]
    C --> E[关联查询\n下单统计数据]
    D --> E
    E --> F[分类汇总\n下单数据]
    F --> G[补充下单类型\n标识字段]
    G --> H[组装分页\n响应结构]
    H --> I[返回扩展后的\n商品数据]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,H,I process
    class B decision
    class F,G important
```
* **请求参数变更点**: 
```json
{
  "orderType": "string|商品/直播下单类型标识|NEW",
  "productType": "string|普通商品/直播商品筛选类型|NEW",
  "ecommerceTaskData": {
    "productOrderCount": "int64|商品下单量|NEW",
    "liveOrderCount": "int64|直播下单量|NEW",
    "totalOrderCount": "int64|总下单量|NEW"
  }
}
```
* **响应参数变更点**: 
```json
{
  "orderType": "string|下单类型标识，取值：product(商品)/live(直播)|NEW",
  "orderStatistics": {
    "productOrderCount": "int|商品下单量|NEW",
    "liveOrderCount": "int|直播下单量|NEW",
    "totalOrderCount": "int|总下单量|NEW"
  },
  "filterType": "string|商品类型筛选条件，取值：product(普通商品)/live(直播商品)/all(全部)|NEW"
}
```

### 3.5.3 电商任务列表接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/ecommerce/list`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. 增强任务奖励数据整合：
   - 区分商品下单和直播下单的任务奖励规则
   - 在返回数据结构中明确标注任务类型
2. 完善数据上报：
   - 记录用户对不同类型电商任务（商品/直播）的交互行为
3. 动态提示优化：
   - 根据任务类型展示差异化的奖励提示信息
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[获取任务数据] --> B{任务类型\n商品下单?}
    B -- 是 --> C[应用商品奖励规则]
    B -- 否 --> D[应用直播奖励规则]
    C --> E[生成奖励数据]
    D --> E
    E --> F[标注任务类型]
    F --> G[记录用户行为]
    G --> H{任务类型\n商品下单?}
    H -- 是 --> I[展示商品奖励提示]
    H -- 否 --> J[展示直播奖励提示]
    I --> K[返回整合数据]
    J --> K
    
    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,E,F,G,K process
    class B,H decision
    class C,D,I,J important
```
* **请求参数变更点**: 
```json
{
  "taskType": "string|required|任务类型（商品/直播）|NEW",
  "interactionType": "string|用户交互行为类型|NEW",
  "rewardHint": "string|差异化奖励提示信息|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "taskType": "string|任务类型标识，取值：product(商品)/live(直播)|NEW",
  "rewardRules": {
    "productOrderReward": "float64|商品下单任务奖励金额|NEW",
    "liveOrderReward": "float64|直播下单任务奖励金额|NEW"
  },
  "interactionRecords": {
    "productOrderCount": "int|商品下单交互次数|NEW",
    "liveOrderCount": "int|直播下单交互次数|NEW"
  },
  "dynamicTips": {
    "productOrderTip": "string|商品下单任务奖励提示文案|NEW",
    "liveOrderTip": "string|直播下单任务奖励提示文案|NEW"
  }
}
```

### 3.5.4 电商订单状态接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/ecommerce/external/orderchange`
* **调用方式**: `POST`
* **变更功能描述**: 
```
1. 完善订单类型识别：
   - 在订单状态变更时识别并记录商品订单与直播订单
2. 扩展奖励处理逻辑：
   - 根据订单类型应用不同的奖励计算规则
3. 数据分类统计：
   - 按订单类型分别记录任务完成状态
4. 异常处理增强：
   - 对不同类型的订单状态变更进行差异化错误处理
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[订单状态变更事件] --> B{订单类型\n识别?}
    B -- 商品订单 --> C[应用商品订单\n奖励规则]
    B -- 直播订单 --> D[应用直播订单\n奖励规则]
    C --> E[记录任务\n完成状态]
    D --> E
    E --> F{状态变更\n成功?}
    F -- 是 --> G[更新统计\n数据]
    F -- 否 --> H[差异化\n错误处理]
    H --> G
    G --> I[流程结束]

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,E,G,I process
    class B,F decision
    class C,D,H important
```
* **请求参数变更点**: 
```json
{
  "orderType": "string|商品/直播订单类型标识|NEW",
  "taskType": "string|required|任务类型（商品/直播）|NEW",
  "rewardHint": "string|差异化奖励提示信息|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "orderType": "string|订单类型标识，取值：product(商品)/live(直播)|NEW",
  "rewardRules": {
    "productOrderReward": "float64|商品订单奖励金额|NEW",
    "liveOrderReward": "float64|直播订单奖励金额|NEW"
  },
  "orderStatistics": {
    "productOrderCount": "int|商品订单数量|NEW",
    "liveOrderCount": "int|直播订单数量|NEW",
    "totalOrderCount": "int|总订单数量|NEW"
  },
  "errorHandling": {
    "productOrderErrorCode": "string|商品订单错误码|NEW",
    "liveOrderErrorCode": "string|直播订单错误码|NEW"
  }
}
```

### 3.5.5 电商浏览完成接口（修改）
* **代码库**: [baidu/jady/ug-duoduo-video](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/jady/ug-duoduo-video/tree/master)
* **接口路径**: `/video/external/ecommerce/browseComplete`
* **调用方式**: `GET,POST`
* **变更功能描述**: 
```
1. 任务类型区分：
   - 在浏览任务完成验证阶段识别商品浏览与直播浏览
2. 奖励发放优化：
   - 根据浏览任务类型匹配对应的奖励策略
3. 数据记录扩展：
   - 在任务完成日志中增加任务类型标识
4. 状态同步增强：
   - 将分类浏览数据同步至报表统计系统
```
* **变更功能流程图**:
```mermaid
flowchart LR
    A[开始任务验证]
    B{浏览类型?}
    C[商品浏览任务]
    D[直播浏览任务]
    E[匹配商品奖励策略]
    F[匹配直播奖励策略]
    G[记录任务类型日志]
    H[同步数据到报表系统]
    I[结束流程]

    A --> B
    B -- 商品 --> C
    B -- 直播 --> D
    C --> E
    D --> F
    E --> G
    F --> G
    G --> H
    H --> I

    %% 样式定义
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:1px  
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef important fill:#ffebee,stroke:#c62828,stroke-width:1px
    
    %% 应用样式
    class A,C,D,E,F,G,H,I process
    class B decision
    class G,H important
```
* **请求参数变更点**: 
```json
{
  "taskType": "string|required|任务类型（商品/直播）|NEW",
  "rewardHint": "string|差异化奖励提示信息|NEW"
}
```
* **响应参数变更点**: 
```json
{
  "taskType": "string|任务类型标识，取值：product(商品)/live(直播)|NEW",
  "rewardRules": {
    "productBrowseReward": "float64|商品浏览任务奖励金额|NEW",
    "liveBrowseReward": "float64|直播浏览任务奖励金额|NEW"
  },
  "browseRecords": {
    "productBrowseCount": "int|商品浏览交互次数|NEW",
    "liveBrowseCount": "int|直播浏览交互次数|NEW"
  },
  "reportStatistics": {
    "productBrowseCount": "int|商品浏览统计量|NEW",
    "liveBrowseCount": "int|直播浏览统计量|NEW",
    "totalBrowseCount": "int|总浏览统计量|NEW"
  }
}
```
