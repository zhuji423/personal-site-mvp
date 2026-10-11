---
title: "业务背景"
description: "你是一名资深架构师。请理解当前代码库 {{repo}} ，根据任务要求编写RULES用于规范后续的代码生成。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\rule_generator\\repo_overview.md"
---
你是一名资深架构师。请理解当前代码库 {{repo}} ，根据任务要求编写RULES用于规范后续的代码生成。

---

# 业务背景

* 场景名称：{{module_name}}
* 场景描述：
```
{{module_desc}}
```

---
# 任务说明
- `.rules/repo_overview.md` - 代码库总体架构规范
- `.rules/code_rule/` 目录下的编码规范文件

## 任务一：提取代码库{{repo}}的总体架构RULE
请从代码库 {{repo}} 中理解并总结所有架构相关规则，生成一份完整的项目架构说明文档，作为指导后续代码开发的规范，包括以下内容：
- 1. 代码库介绍
- 2. 目录结构说明
- 3. 依赖方向说明
- 4. 与外部系统交互说明

总体架构RULE模板：
<repo_overview>
## 1. 代码库介绍
本代码库为 XX 业务 的核心实现，主要职责包括 XX、XX、XX，提供核心功能点（简要说明）:
- **A**：...
- **B**：...

## 2. 目录结构说明
- 要求1：列出项目目录结构，并且针对每个关键目录进行说明
示例：
.
├── controller/         # HTTP 请求处理层（无业务逻辑）
├── model/              # 业务模型与业务逻辑层
│   ├── service/        # 核心业务逻辑与服务编排
│   ├── data/           # 数据聚合、数据处理逻辑
│   └── dao/            # 数据库访问逻辑
├── httpapi/            # 路由注册与接口定义
├── conf/               # 测试环境相关配置
├── conf_online/        # 生产环境相关配置
├── middlewares/        # 中间件层（日志、跨域、鉴权等）
├── library/            # 工具库（通用方法封装）
└── thirdparty/         # 第三方与下游服务封装（如 RAL）

- 要求2：针对 httpapi、controller、model、service 等关键目录，说明该层级的职责和规范，要求描述简练，不超过两句话。
— 示例：
### 2.1 httpapi：接口定义层
注册所有路由。
- 定义接口 path、method、请求结构及基础校验。
- 将请求委托至 controller。

### 2.2 controller：请求接入层
- 负责 HTTP 请求入口、路由转发、参数校验。
- 禁止编写业务逻辑。
调用 model/service 提供的业务方法。

### 2.3 model：业务逻辑层
service（核心业务）
- 实现业务流程、业务规则、策略编排。
- 对 controller 暴露统一且稳定的业务接口。
data（数据聚合）
- 负责跨模块的数据整合、转换、校验。
- 处理 service 和 dao 之间的数据格式。
dao（数据访问）
- 提供面向数据库或存储层的访问接口。
- 禁止向上泄漏数据库结构细节。
...

## 3. 依赖方向
示例：
代码库严格遵循什么样的分层架构：
controller → service → data → dao


## 4. 与外部系统交互
- 下游服务调用规范
</repo_overview>


总体架构RULE生成要求：
1. 按照以上模板生成代码库架构规范，必须遵守模板中的结构，不要随意添加。
2. 所有输出内容，必须基于代码库内容生成，保证客观准确，不得自行编造。
3. 描述必须简洁清晰，无需引用代码原文，总体内容不得超过400行。
4. 最终输出一个 .rules/repo_overview.md 文档。


## 任务二：提取代码库{{repo}}的编码规范
请从代码库 {{repo}} 中自动分析通用的编码规范，输出：

### 1. 典型开发 RULES，例如
- 错误处理规范
- 硬编码字符串规范
- mysql/redis/gcp/pdcms 等数据访问规范
- 第三方调用（如ral）规范
- 日志写法规范

### 2. 每个 RULE 包含以下内容
- 从代码现有实现中抽象出通用示例，用于指导生成新代码，给出**简洁清晰正确的示例和推荐的做法**，**不要**写入任何错误示例和不推荐的做法。
- 参考示例如下：
<code_rule>
```markdown
# gcp 编码规则
**gcp主要是针对配置的数据获取进行请求的封装**  
gcp相关写法可以参考以下示例：
```go
conf, err := gcp.Fetch[Cash](ctx, constant.GCPMatrixAppID, gcpConsts.UserCashGCPKey)
if err != nil {
	logger.ErrWF(ctx, errno.ConfInitError,
		"gcp.Fetch err, appID=%s key=%s err=%v", constant.GCPMatrixAppID, gcpConsts.UserCashGCPKey, err)
	return conf, err
}
if conf == nil {
	err = errno.ConfInitError
	logger.WarnfingF(ctx, err,
		"gcp.Fetch err, conf is nil, appID=%s key=%s", constant.GCPMatrixAppID, gcpConsts.UserCashGCPKey)
	return nil, err
}
```
1.通用获取规范
使用 gcp.Fetch[T] 方法获取配置或资源对象。
conf, err := gcp.Fetch[T](ctx, appID, key)
T:是目标类型（如 Cash）
ctx 为上下文
appID:通常为业务应用标识（如 constant.GCPMatrixAppID）
key:为GCP 中存储的配置项键（如 gcpConsts.UserCashGCPKey）
2.错误处理规则
若 err != nil，必须： 打日志（带上下文、错误码、appID、key、err）,返回错误。
```go
if err != nil {
    logger.WarnfingF(ctx, errno.ConfInitError,
        "gcp.Fetch err, appID=%s key=%s err=%v", appID, key, err)
    return conf, err
}
```
3.空值校验规则
若 conf == nil，视为配置获取失败。
处理逻辑：
    设置统一错误码（如 errno.ConfInitError）
    打印错误日志（包含 appID、key）
    返回 nil 和错误
```
</code_rule>

### 3. 最后写入.rules/code_rule/文件夹下
每条规则对应生成一个.md文件，统一放到.rules/code_rule/目录下，文件采用中文命名。