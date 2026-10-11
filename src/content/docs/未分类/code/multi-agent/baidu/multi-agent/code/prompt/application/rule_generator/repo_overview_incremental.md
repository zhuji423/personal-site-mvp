---
title: "业务背景"
description: "你是一名资深架构师。代码库 {{repo}} 已经存在一份完整的RULES文档，现在代码库发生了变更（从 {{oldcommit}} 到 {{newcommit}}），请根据变更的文件，对已有的RULES进行增量更新。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\rule_generator\\repo_overview_incremental.md"
---
你是一名资深架构师。代码库 {{repo}} 已经存在一份完整的RULES文档，现在代码库发生了变更（从 {{old_commit}} 到 {{new_commit}}），请根据变更的文件，对已有的RULES进行增量更新。

---

# 业务背景

* 场景名称：{{module_name}}
* 场景描述：
```
{{module_desc}}
```

---

# 代码变更文件列表
{{changed_files}}

---

# RULE格式要求

## 总体架构RULE（.rules/repo_overview.md）
- 包括以下内容：
    1. 代码库介绍
    2. 目录结构说明
    3. 依赖方向说明
    4. 与外部系统交互说明
- 生成要求：
    1. 所有输出内容，必须基于代码库内容生成，保证客观准确，不得自行编造。
    2. 描述必须简洁清晰，保证可读性，无需引用代码原文，总体内容不得超过400行。
    3. 必须遵守以下模板中的结构生成代码库架构规范，不要随意添加。
- 参考模板如下：
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


# 编码规范（`.rules/code_rule/`文件夹下）

- 每条规则对应生成一个.md文件，统一放到.rules/code_rule/目录下，文件采用中文命名。
- 从代码现有实现中抽象出通用示例，用于指导生成新代码，给出**简洁清晰正确的示例和推荐的做法**，**不要**写入任何错误示例和不推荐的做法。
- 参考模板如下：
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
1. 通用获取规范
使用 gcp.Fetch[T] 方法获取配置或资源对象。
conf, err := gcp.Fetch[T](ctx, appID, key)
T:是目标类型（如 Cash）
ctx 为上下文
appID:通常为业务应用标识（如 constant.GCPMatrixAppID）
key:为GCP 中存储的配置项键（如 gcpConsts.UserCashGCPKey）
2. 异常处理规则
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

---

# 任务说明
当前工作目录中已经存在以下RULES文件：
- `.rules/repo_overview.md` - 代码库总体架构规范
- `.rules/code_rule/` 目录下的编码规范文件

你的任务是：
1. 理解上述变更文件的内容和影响
2. 判断这些变更是否需要更新现有的RULES
3. 如果需要更新，则修改相应的RULES文件
4. 如果变更引入了新的编码规范，则在`.rules/code_rule/`目录下创建新的规范文件

# 增量更新原则
1. **保持一致性**：更新时要保持与现有RULES的风格和结构一致
2. **只更新必要的部分**：只修改受影响的章节，不要重写整个文档
3. **准确性**：所有更新必须基于实际代码变更，不得臆造
4. **简洁性**：描述要简洁清晰，无需引用代码原文

# 更新场景判断

## 场景1：需要更新 `.rules/repo_overview.md` 的情况
- 新增或删除了重要目录
- 目录结构发生了显著变化
- 模块职责发生了变化
- 依赖关系发生了变化
- 外部系统集成方式变化

## 场景2：需要更新 `.rules/code_rule/` 下编码规范的情况
- 现有编码规范的实现方式发生变化
- 引入了新的第三方库调用方式
- 数据库访问方式发生变化
- 错误处理模式发生变化
- 日志记录方式发生变化

## 场景3：需要创建新编码规范的情况
- 引入了新的技术栈或框架
- 新增了新的数据访问方式（如新的数据库、缓存等）
- 新增了新的第三方服务调用
- 引入了新的通用开发模式

## 场景4：无需更新的情况
- 纯业务逻辑变更，不影响架构和规范
- 小范围的bug修复
- 单个功能的新增，不引入新的开发模式
- 测试代码变更

# 输出要求
1. 如果需要更新，直接修改对应的RULES文件
2. 如果不需要更新，进行简要说明即可
3. 更新时要保持原有的文件名，markdown格式和结构
4. 新增的编码规范文件要按照现有规范文件的格式编写
5. 不要生成冗余的编码规范文件，如果可以复用已有的规范文件内容，直接在已有的文件中添加内容

# 特别提醒
- 不要重新生成整个RULES，只更新变更相关的部分
- 保持RULES的完整性，不要删除无关的内容
- 如果不确定是否需要更新，倾向于保守，不做更新