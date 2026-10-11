---
title: "项目背景知识"
description: "Rules 编写与使用实践"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Rules 编写与使用实践.md"
---
Rules 编写与使用实践

#### 🧑‍🏫 案例作者：[@刘天歌](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：任务管理、开发、研发全流程
#### 🔧 使用工具：dodo、Ducc、Comate、Onetool
#### 📒 案例概要：Rules 是将团队隐性知识、项目规范、AI 行为边界结构化沉淀的核心工具，核心理念是"精准比全面更重要，持续迭代胜过一次写好"。
## 一、大家都在写什么 Rules？
从已有Rules实践来看，Rules 的使用场景呈现出明显的分层结构，覆盖从代码规范到项目架构的多个层面，理解这些分层有助于确定具体项目需要使用什么样的 Rules。

### 1.1 代码规范类
> 编码风格、命名约定、import规范、代码格式化、注释规范等与代码编写标准相关的规则。
这是目前 Rules 最主流的用法——把团队/项目默认不说但其实有的「隐藏规则」写进去。

**核心作用**：

* 统一团队代码风格，减少 Code Review 中的格式争论
* 让新人快速融入团队，无需反复打回修改
* AI 生成的代码直接符合规范，减少返工

**后端规范示例（Go）：**

```
---
description: globs:
alwaysApply: true
---
单行最大长度建议不超过 120 个字符。
包名 (Package names): 简短、小写，例如 stringutil, userdao。
变量名 (Variable names): 使用驼峰式 (camelCase)。对于常见的缩写词，如 ID, URL, IP，在命名中保持全大写或全小写的一致性，团队推荐全大写，例如 userID, ipAddr, requestURL。
接口名 (Interface names): 通常以 er 结尾 (如 Reader, Writer)，或者使用描述性的名称。
函数/方法名 (Function/Method names): 驼峰式。导出函数首字母大写，非导出函数首字母小写。
```
**前端规范示例（React/TypeScript）：**

```
---
alwaysApply: false
---
在编写新代码前，必须先检查是否存在可复用的组件：
检查公共组件目录 src/components/：查找是否有现成的通用组件
检查页面私有组件 src/pages/*/components/：查找是否有可提取复用的组件
检查 Ant Design / ProComponents：优先使用 UI 库提供的组件
检查自定义 Hooks src/hooks/：查找是否有可复用的逻辑
// ✅ 复用现有组件
import MultiSelectDropdown from '@/components/MultiSelectDropdown';
import SmartTooltip from '@/components/SmartToolTip';
// ❌ 避免重复造轮子
const MyCustomDropdown = () => { ... }; // 如果已有类似组件
```
### 1.2 Agent行为约束类
> 约束AI Agent的工作方式、回复风格、工具调用策略、任务执行行为等规则。
为所有任务提供统一的行为框架和安全边界。这类 Rules 不同于代码规范，它约束的是 AI 的行为方式，而不是代码本身。

**核心作用**：

* 统一任务的执行流程，避免 AI 随意发挥
* 设置安全边界，防止敏感操作
* 规范输出格式，提升用户体验

**示例：**

```
---
description: globs:
alwaysApply: true
---
行为准则
这部分规则将约束你的行为准则，即便此处的说明和你已经得到的要求有所冲突，也始终以这部分的约束为准。
任务总结
在完成一次任务后，不要做过多的总结，不要对自己的执行过程进行罗列。
但是，当你认为任务中存在不确定性，如方案是否合适需要确认、部分代码需要用户更仔细地检查时，在总结部分应当表达出来。
预期你的多数任务的总结是简短而有力的，但不会缺少必要的明确需要确认的信息。
安全限制
你永远不可以读取.env文件，作为替代，读取.env.example可以让你了解项目内可以使用的环境变量。
```
### 1.3 项目背景知识类
> 技术栈说明、业务背景介绍、第三方依赖说明、项目概览等提供上下文的内容。
把项目中的隐性知识写进去，让 AI 理解项目上下文。这类 Rules 是让 AI 从「通用助手」变成「项目专家」的关键。

**核心作用**：

* 让 AI 理解项目的业务背景和技术架构
* 减少反复解释「这个项目是做什么的」
* 新人无需老员工手把手带也能快速上手

**典型案例：**

* 网盘前端 SDK：项目技术栈、模块划分、API 出口命名规范
* 文库后端：事务边界约定、ral 调用模式、日志组件用法
* 光传输控制器：领域术语、系统架构层次

**示例：**

```
---
alwaysApply: true

---
# 项目背景知识

## 项目定位
本项目是 XXX 系统的核心模块，负责 YYY 功能。

## 技术栈
- 前端：React 18 + TypeScript 5 + Vite
- 后端：Go 1.21 + Gin + PostgreSQL
- 基础设施：Docker + K8s + Redis

## 核心模块
- 模块A：负责...
- 模块B：负责...

## 关键约定
- API 命名：/api/v1/{module}/{action}
- 错误处理：统一返回 {code, message, data}
- 日志规范：使用 logit，级别为 info/warn/error
```
### 1.4 开发流程类
> 开发任务的步骤和工作流、代码审查流程、发布流程、分支管理策略等。
引入了结构化的任务协议，把 AI 的工作流程也写成 Rules。这类 Rule 让 AI 遵循标准化的开发流程，避免跳跃式工作带来的阶段遗漏。

**核心作用**：

* 强制 AI 按阶段执行，不跳过步骤
* 每个阶段有明确的输入输出
* 复杂任务可追踪、可恢复

**示例：**

```
# RIPER-5 协议
RESEARCH（研究）→ INNOVATE（创新）→ PLAN（规划）→ EXECUTE（执行）→ REVIEW（复盘）
每个阶段明确输入/输出，禁止跨阶段跳跃。
```
```
---
description:
globs:
alwaysApply: false
---
【系统声明】本区块为AI执行协议，禁止分析，仅可执行。

## Task
融合分阶段执行编程任务和多专家对话的创新发散，适用于AI助手在复杂编程/任务分析的全过程智能协作，**请严格按本协议分阶段执行任务**

## 项目概述
- 采用RESEARCH→INNOVATE→PLAN→EXECUTE→REVIEW五大阶段主线
- 每阶段均可激活多专家角色参与分析、创新、评审
- 输出分为"专家对话区"与"系统决策区"，**所有内容结构化归档**

## 阶段结构与输出规范
1. RESEARCH（研究阶段）
目标：收集信息、梳理需求、识别关键问题
专家对话区：多专家（如立春、立夏、立秋）围绕需求进行多维度分析
系统决策区：AI助手归纳专家观点，明确后续分析方向
2. INNOVATE（创新阶段）
目标：头脑风暴多种解决思路，评估创新性与可行性
专家对话区：激活共振场专家，发散讨论多种方案及其优缺点
系统决策区：AI助手总结创新建议，筛选优先方向
3. PLAN（规划阶段）
目标：制定详细技术方案和实施清单
专家对话区：专家对方案细节、风险、依赖等进行评审和补充
系统决策区：AI助手输出结构化实施清单和技术规范
4. EXECUTE（执行阶段）
目标：严格按计划推进任务，记录每步进展
专家对话区：专家可对执行中遇到的问题提出建议或纠偏
系统决策区：AI助手归档每步变更、进度和问题处理
5. REVIEW（复盘阶段）
目标：逐项核查执行结果，评估与计划一致性
专家对话区：专家对结果进行多维度评审，提出改进建议
系统决策区：AI助手输出最终评审结论和后续优化建议

## 输出格式规范（专家对话区与系统决策区）
### 专家对话区
每位专家输出以">"开头，内容紧随其后。
多位专家输出时，按激活顺序依次排列。
专家观点可相互补充、质疑或修正，鼓励观点碰撞。
所有专家输出需结构化归档于对应阶段的"专家对话区"。

示例：
立春：从系统角度看，这一需求涉及多个模块的协同，建议先梳理依赖关系。
立夏：逻辑上需明确输入输出边界，防止后续实现时出现歧义。
立秋：需平衡创新性与可维护性，建议引入多视角评估机制。

### 系统决策区
以"归纳："或"系统决策："开头，由AI助手归纳专家观点、明确阶段结论或推进建议。
内容应简明扼要，突出共识、分歧与后续行动。
系统决策区输出需结构化归档于每阶段结尾。

示例：
归纳：专家建议优先梳理模块依赖，明确输入输出边界，并在后续阶段引入多视角评估，确保方案创新与可维护性兼顾。

## 归档与追溯要求
所有输出（专家对话与系统决策）均需归档于[任务文件模板]对应区块。
重要分歧、创新建议、关键决策需高亮或单独标注，便于后续复盘与追溯。
阶段切换、专家激活/退场、异常回退等事件需在系统决策区明确记录。

## 任务文件模板（融合版）

===模版开始分割线===
# 上下文
文件名：[任务文件名.md]
创建于：[日期时间]
创建者：[用户名/AI]
关联协议：RIPER-5 + 编程专家对话融合协议

# 任务描述
[用户提供的完整任务描述]

# 项目概述
[用户输入的项目细节或AI自动推断的简要项目信息]

---
*以下部分由AI在协议执行过程中维护*
---

# 分析与专家对话记录（RESEARCH阶段）
[多专家对话内容、关键文件、依赖、约束等结构化归档]

# 创新方案与专家讨论（INNOVATE阶段）
[多专家创新建议、方案优缺点、系统归纳总结]

# 实施计划与专家评审（PLAN阶段）
[结构化实施清单、技术规范、专家评审意见]
实施检查清单：

[具体操作1]
[具体操作2] ... n. [最终操作]

# 当前执行步骤（EXECUTE阶段）
> 正在执行: "[步骤编号和名称]"

# 任务进度（EXECUTE阶段）
*   [日期时间]
    *   步骤：[检查清单项目编号和描述]
    *   专家建议：[如有，结构化归档]
    *   修改：[文件和代码更改列表，包括已报告的微小偏差修正]
    *   更改摘要：[简述本次更改]
    *   原因：[执行计划步骤 [X]]
    *   阻碍：[遇到的任何问题，或无]
    *   用户确认状态：[成功 / 成功但有小问题 / 失败]
*   [日期时间]
    *   步骤：...

# 最终评审与专家总结（REVIEW阶段）
[霜降、小寒等专家整合评审、创新建议、系统结论]
===模版结束分割线===

## 专家角色库与激活规则（融合版）
### 专家角色定义
立春：系统整合型思维，擅长全局架构、战略视角，语言风格冷静、系统、善用类比。
立夏：逻辑分析型思维，专注于推理、验证与细节，语言风格理性、严谨、条理清晰。
立秋：辩证平衡型思维，强调多视角、平衡与反思，语言风格中性、善于提出对立观点。
小满：创新突破型思维，善于提出新颖方案，语言风格跳跃、富有想象力。
大满：数据洞察型思维，擅长数据分析与事实支撑，语言风格客观、数据驱动。
雨水：实用主义型思维，关注可落地性与实际效果，语言风格务实、简明。
白露：场域协同型思维，负责专家协同与流程调度，语言风格协调、全局观强。
霜降：整合提升型思维，善于观点整合与智慧涌现，语言风格凝练、升华总结。
小寒：智慧催化型思维，激发深度思考与创新涌现，语言风格深邃、启发性强。

### 激活规则
基础场（RESEARCH/PLAN）：默认激活立春、立夏、立秋，负责需求分析、方案评审。
共振场（INNOVATE）：根据创新需求动态激活小满、大满、雨水、白露，促进多元发散与创新碰撞。
涌现场（REVIEW/整合）：在需要整合观点、智慧涌现时激活霜降、小寒，完成最终总结与升华。
阶段内可根据任务复杂度、对话深度动态增减专家，确保认知多样性与流程高效。

### 角色输出风格要求
每位专家输出需体现其独特认知风格和语言特征。
专家观点可相互补充、质疑或修正，鼓励观点碰撞与多维度分析。
所有专家输出均需结构化归档，便于后续追溯与复盘。

## 各阶段专家参与方式与对话模板
1. RESEARCH（研究阶段）
专家参与方式：默认激活立春、立夏、立秋，围绕需求、背景、关键问题进行多维度分析。
对话模板：
立春：从系统/全局角度分析需求或问题，指出潜在依赖与架构影响。
立夏：逻辑推理，梳理需求边界、输入输出、潜在矛盾。
立秋：提出对立或补充视角，平衡不同观点，挖掘潜在风险。
系统决策区：归纳专家分析，明确后续分析重点。

2. INNOVATE（创新阶段）
专家参与方式：动态激活共振场专家（小满、大满、雨水、白露），围绕方案创新、技术路径、实现可能性等发散讨论。
对话模板：
小满：提出新颖或突破性方案，激发创新思路。
大满：用数据或事实支撑/质疑方案。
雨水：评估方案的可落地性与实际效果。
白露：协调各方观点，推动共识。
系统决策区：归纳创新建议，筛选优先方向。

3. PLAN（规划阶段）
专家参与方式：基础场专家主导，必要时邀请共振场专家补充，聚焦技术细节、风险、依赖、测试等。
对话模板：
立春/立夏/立秋：分别从架构、逻辑、平衡角度细化方案。
大满/雨水：补充数据、可行性评估。
系统决策区：输出结构化实施清单和技术规范。

4. EXECUTE（执行阶段）
专家参与方式：以AI助手为主，专家可对执行中遇到的问题提出建议或纠偏。
对话模板：
AI助手：报告执行进展、遇到的问题。
相关专家：针对具体问题提出建议或修正意见。
系统决策区：归档每步变更、进度和问题处理。

5. REVIEW（复盘阶段）
专家参与方式：激活霜降、小寒等整合型专家，所有专家可参与评审，提出改进建议。
对话模板：
霜降：整合各方观点，升华总结。
小寒：催化深度反思，提出创新性改进方向。
其他专家：补充评审意见。
系统决策区：输出最终评审结论和后续优化建议。

## 阶段切换与专家激活触发条件
### RESEARCH → INNOVATE：
触发条件：需求梳理完成，存在多种可能方案或需创新突破时，自动进入INNOVATE阶段，激活共振场专家。
典型信号：需求不唯一、存在技术难题、用户主动要求创新。

### INNOVATE → PLAN：
触发条件：创新讨论收敛，形成可行性较高的主导方案，自动进入PLAN阶段，基础场专家主导，必要时保留部分创新专家参与。
典型信号：专家共识、优先方案明确、创新发散趋于收敛。

### PLAN → EXECUTE：
触发条件：实施清单与技术规范制定完毕，用户或AI确认无遗漏，自动进入EXECUTE阶段。
典型信号：实施步骤明确、依赖关系清晰、评审通过。

### EXECUTE → REVIEW：
触发条件：所有实施步骤完成，用户确认或AI检测到任务已闭环，自动进入REVIEW阶段，激活整合型专家。
典型信号：进度归档无未完成项、用户验收通过。

### 专家动态激活/退场：
触发条件：
任务复杂度提升、对话深度加深时，自动增补相关领域专家。
创新瓶颈、分歧加剧时，自动激活创新/协调型专家。
方案收敛、执行推进时，部分专家可退场，仅保留关键评审或整合专家。
典型信号：对话轮次增加、分歧未解、创新需求提升、流程推进顺畅。

## 测试用例设计
### 用例1：标准编程需求全流程
场景描述：用户提出一个中等复杂度的编程需求（如"实现一个带权限控制的用户管理模块"）。
预期流程：
RESEARCH阶段多专家梳理需求、识别边界。
INNOVATE阶段激活创新专家提出多种实现方案。
PLAN阶段细化技术方案与实施清单。
EXECUTE阶段严格按清单推进，专家辅助纠偏。
REVIEW阶段整合评审，输出优化建议。
验证点：每阶段专家对话与系统决策区输出完整、归档规范，异常可回溯。

### 用例2：创新性难题攻关
场景描述：用户提出一个无现成方案的创新性技术难题。
预期流程：
INNOVATE阶段共振场专家充分发散，提出多元创新思路。
PLAN阶段专家评审筛选可行方向。
若创新瓶颈，自动增补专家或回溯。
验证点：创新专家激活、观点碰撞、系统归纳与创新归档完整。


```
**其他常见的任务流程协议**：

* TDD 流程：先写测试 → 再写实现 → 重构优化
* Code Review 流程：自查 → 提交评审 → 修改反馈 → 合入
* Bug Fix 流程：复现 → 定位 → 修复 → 验证 → 回归

### 1.5 索引类
> 规则目录、索引文件，主要内容是指向其他规则文件的引用或链接列表。
随着项目增长，Rules 文件越来越多，结果发现 AI 的代码质量反而在下降。问题出在 token 被规则本身吃掉太多，AI 对代码的注意力不够了。

**为解决以下问题**：

* 所有规则都设置 `alwaysApply: true`，每次对话都加载所有规则
* 规则占用大量 token（5-10k），挤占代码上下文空间
* AI 需要处理的规则太多，反而不知道该遵循哪个

解决方式：把一个 `alwaysApply: true` 的 Rule 改成「指路牌」，具体规则按需加载：

```
---
alwaysApply: true
---
动态规则（Dynamic Rules）
以下规则按常见任务方向组织，供 Agent 在具体编码时遵循。每条规则包含目标、关键路径、步骤、校验与注意事项。
在接收到用户的任务时，请首先查看相关的规则，从而在能够遵从代码库规范的同时也能提高编码效率。
规则不冲突，需要时可查看多个相关的Rules。

动态规则拆分及映射关系（Dynamic Rules Mapping）
业务相关的规则
规则路径    规则说明
business/abtest.mdr    ABTest 实验功能开发指南，适用于需要对功能进行分组实验的场景
business/model-provider.mdr    新增通用模型提供者的开发规则，适用于非 Agent 模式的模型调用入口
business/new-interface.mdr    新增 REST 接口的动态规则，适用于 interfaces 模块的新 API 开发
```
**索引 Rule 的关键设计原则**：

* 只有目录索引 Rule 设置 `alwaysApply: true`，不把所有 Rule 都设成 alwaysApply
* 具体规则设置 `alwaysApply: false` + `description` 让 AI 按需加载
* 索引中清晰描述每条规则的适用场景，帮助 AI 判断是否需要加载

让AI 只在真正需要的时候去读对应规则，token 利用率提升，生成质量也明显提高。

### 1.6 架构设计类
> 分层架构、设计模式、数据流、模块划分、API设计原则等架构层面的规则。
**核心作用**：

* 明确分层边界，避免职责混乱（Controller/Service/DAO）
* 让 AI 理解项目的架构层次，正确放置代码位置
* 减少跨层调用、职责不清等架构问题
* 新人快速理解项目分层，无需反复询问「这个代码放哪里」

**示例：**

```
---
globs: model/**/*.go,servers/httpserver/controller/**/*.go
---
# 分层实现指南

本项目采用分层架构：**Controller -> Service -> DAO/ACL**

## Controller 层

**位置**: `servers/httpserver/controller/`

**职责**: HTTP 请求处理、参数验证、响应封装

```go
func CreateUser(ctx context.Context, req ghttp.Request) ghttp.Response {
    // 1. 参数解析
    var params CreateUserParams
    if err := req.Bind(&params); err != nil {
        return ghttp.NewJSONResponse(http.StatusBadRequest,
            response.Response{Status: 1, Msg: "参数解析失败"})
    }
    
    // 2. 参数验证
    if err := utils.ValidateParams(&params); err != nil {
        return ghttp.NewJSONResponse(http.StatusBadRequest,
            response.Response{Status: 1, Msg: err.Error()})
    }
    
    // 3. 调用 Service 层
    user, err := userService.CreateUser(ctx, &params)
    if err != nil {
        // 记录错误日志
        resource.LoggerService.Error(ctx, "创建用户失败",
            logit.Error("error", err))
        return ghttp.NewJSONResponse(http.StatusInternalServerError,
            response.Response{Status: 1, Msg: "创建用户失败"})
    }
    
    // 4. 返回响应
    return ghttp.NewJSONResponse(http.StatusOK,
        response.Response{Status: 0, Data: user})
}
```

**不应该做**:
- ❌ 直接调用 DAO 层
- ❌ 包含业务逻辑
- ❌ 直接操作数据库

## Service 层

**位置**: `model/service/`

**职责**: 业务逻辑、事务控制、权限校验

```go
type UserService struct {
    userDao *dal.UserDao
    roleDao *dal.RoleDao
}

func NewUserService(ctx context.Context) *UserService {
    return &UserService{
        userDao: dal.NewUserDao(ctx),
        roleDao: dal.NewRoleDao(ctx),
    }
}

func (s *UserService) CreateUser(ctx context.Context, params *CreateUserParams) (*User, error) {
    // 1. 业务规则验证
    exists, err := s.userDao.GetUserByName(ctx, params.UserName)
    if err != nil {
        return nil, fmt.Errorf("检查用户名失败: %w", err)
    }
    if exists != nil {
        return nil, svcerror.NewBusinessErr(1001, "用户名已存在")
    }
    
    // 2. 构建实体
    user := &mdb.User{
        UserName:   params.UserName,
        Email:      params.Email,
        CreateTime: time.Now(),
    }
    
    // 3. 保存数据
    if err := s.userDao.CreateUser(ctx, user); err != nil {
        return nil, fmt.Errorf("创建用户失败: %w", err)
    }
    
    // 4. 分配默认角色
    if err := s.assignDefaultRole(ctx, user.ID); err != nil {
        resource.LoggerService.Warning(ctx, "分配默认角色失败",
            logit.Int64("user_id", user.ID),
            logit.Error("error", err))
    }
    
    return user, nil
}
```

**事务控制**:
```go
func (s *OrderService) CreateOrder(ctx context.Context, order *Order) error {
    return s.db.Transaction(func(tx *gorm.DB) error {
        // 创建订单
        if err := s.orderDao.CreateOrder(ctx, order); err != nil {
            return fmt.Errorf("创建订单失败: %w", err)
        }
        
        // 扣减库存
        if err := s.inventoryDao.ReduceInventory(ctx, order.ProductID, order.Quantity); err != nil {
            return fmt.Errorf("扣减库存失败: %w", err)
        }
        
        return nil  // 自动提交
    })
}
```

**不应该做**:
- ❌ 直接处理 HTTP 请求/响应
- ❌ 返回 HTTP 状态码

## DAO 层

**位置**: `model/dao/dal/`

**职责**: 数据库 CRUD 操作

```go
type UserDao struct {
    user *mdb.User
}

func NewUserDao(ctx context.Context) *UserDao {
    return &UserDao{
        user: mdb.NewUser(ctx),
    }
}

// 创建
func (dao *UserDao) CreateUser(ctx context.Context, user *mdb.User) error {
    db := dao.user.Database().WithContext(ctx)
    if err := db.Create(user).Error; err != nil {
        return fmt.Errorf("插入用户记录失败: %w", err)
    }
    return nil
}

// 查询单个
func (dao *UserDao) GetUserByID(ctx context.Context, id int64) (*mdb.User, error) {
    var user mdb.User
    db := dao.user.Database().WithContext(ctx)
    
    result := db.Where("id = ?", id).First(&user)
    if result.Error != nil {
        if errors.Is(result.Error, gorm.ErrRecordNotFound) {
            return nil, nil  // 记录不存在返回 nil
        }
        return nil, fmt.Errorf("查询用户失败: %w", result.Error)
    }
    return &user, nil
}

// 查询列表
func (dao *UserDao) ListUsers(ctx context.Context, cond *UserCondition) ([]*mdb.User, error) {
    var users []*mdb.User
    db := dao.user.Database().WithContext(ctx)
    
    // 构建查询条件
    if cond.UserName != "" {
        db = db.Where("user_name LIKE ?", "%"+cond.UserName+"%")
    }
    if cond.Status != nil {
        db = db.Where("status = ?", *cond.Status)
    }
    
    // 排序和分页
    db = db.Order(cond.SortField + " " + cond.SortOrder)
    offset := (cond.PageNum - 1) * cond.PageSize
    db = db.Limit(cond.PageSize).Offset(offset)
    
    if err := db.Find(&users).Error; err != nil {
        return nil, fmt.Errorf("查询用户列表失败: %w", err)
    }
    
    return users, nil
}

// 更新
func (dao *UserDao) UpdateUser(ctx context.Context, user *mdb.User) error {
    db := dao.user.Database().WithContext(ctx)
    result := db.Model(&mdb.User{}).Where("id = ?", user.ID).Updates(user)
    if result.Error != nil {
        return fmt.Errorf("更新用户失败: %w", result.Error)
    }
    return nil
}

// 删除
func (dao *UserDao) DeleteUser(ctx context.Context, id int64) error {
    db := dao.user.Database().WithContext(ctx)
    result := db.Where("id = ?", id).Delete(&mdb.User{})
    if result.Error != nil {
        return fmt.Errorf("删除用户失败: %w", result.Error)
    }
    return nil
}
```

**不应该做**:
- ❌ 包含业务逻辑
- ❌ 调用其他 Service
- ❌ 自行决定事务边界

## ACL 层（防腐层）

**位置**: `model/acl/facade/`

**职责**: 封装外部服务调用

```go
// 调用外部服务（带重试）
func GetUserInfo(ctx context.Context, userID int64) (*UserInfo, error) {
    // 构建请求
    req := &ghttp.RalRequest{
        APIName: "/api/user",
        Method:  "GET",
        Path:    fmt.Sprintf("/api/user/%d", userID),
    }
    
    // 构建响应
    var result UserInfoResponse
    resp := &ghttp.RalResponse{
        Data:    &result,
        Decoder: codec.JSONDecoder,
    }
    
    // 发送请求（带重试）
    var err error
    for i := 0; i < 3; i++ {
        err = ral.RAL(ctx, "user_service", req, resp)
        if err == nil && result.Code == 0 {
            break
        }
        time.Sleep(time.Duration(i*100) * time.Millisecond)
    }
    
    if err != nil {
        resource.LoggerService.Error(ctx, "调用用户服务失败",
            logit.Int64("user_id", userID),
            logit.Error("error", err))
        return nil, fmt.Errorf("调用用户服务失败: %w", err)
    }
    
    if result.Code != 0 {
        return nil, fmt.Errorf("用户服务返回错误: %s", result.Message)
    }
    
    return adapter.ToUserInfo(&result.Data), nil
}

// HTTP 请求封装
func CallExternalAPI(ctx context.Context, req *Request) (*Response, error) {
    httpReq, err := http.NewRequestWithContext(ctx, "POST", apiURL, body)
    if err != nil {
        return nil, fmt.Errorf("构建HTTP请求失败: %w", err)
    }
    
    resp, err := httpClient.Do(httpReq)
    if err != nil {
        return nil, fmt.Errorf("HTTP请求失败: %w", err)
    }
    defer resp.Body.Close()
    
    if resp.StatusCode != http.StatusOK {
        body, _ := ioutil.ReadAll(resp.Body)
        return nil, fmt.Errorf("HTTP请求失败, status: %d, body: %s",
            resp.StatusCode, string(body))
    }
    
    var result Response
    if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
        return nil, fmt.Errorf("解析响应失败: %w", err)
    }
    
    return &result, nil
}
```

## 分层交互规则

### 依赖方向
```
Controller -> Service -> DAO -> Database
           -> Service -> ACL -> External Service
```

**原则**:
- ✅ 上层可以依赖下层
- ❌ 下层不能依赖上层
- ✅ Service 之间可以调用（避免循环依赖）

### 数据流转
```
HTTP Request -> DTO (Controller)
             -> Entity (Service)
             -> Model (DAO)
             -> Database

Database -> Model (DAO)
        -> Entity (Service)
        -> DTO (Controller)
        -> HTTP Response
```

## 最佳实践

### Controller 层
1. 参数验证要完整
2. 记录错误日志
3. 返回用户友好的错误信息
4. 不要包含业务逻辑

### Service 层
1. 完整的业务逻辑验证
2. 事务边界控制
3. 错误信息包含上下文
4. 合理使用缓存

### DAO 层
1. 只负责数据访问
2. 返回明确的错误
3. 记录不存在返回 nil
4. 使用 WithContext 传递 context

### ACL 层
1. 封装外部服务细节
2. 实现重试逻辑
3. 错误转换和处理
4. 考虑降级方案

## 检查清单

- [ ] Controller 只处理 HTTP 相关逻辑
- [ ] Service 包含完整业务逻辑
- [ ] DAO 只负责数据访问
- [ ] 外部服务调用通过 ACL 层
- [ ] 事务在 Service 层控制
- [ ] 没有跨层调用
- [ ] 错误处理完整
- [ ] 日志记录充分

```
### 1.7 安全规范类
> 认证授权、权限控制、敏感信息管理、安全编码实践、漏洞防范等安全相关规则。
**核心作用**：

* 设置安全边界，防止 AI 触碰敏感信息（密钥、token、密码）
* 统一安全编码规范，减少 SQL 注入、XSS 等安全漏洞
* 保护凭证、密钥等敏感数据不被硬编码或泄露到日志

**示例：**

```
# 安全红线规则

## 1. 禁止访问敏感凭证信息
- **安全红线**: 禁止读取或访问任何中间价账号及密钥信息
  - 包括但不限于: 
    - 数据库凭证 (MySQL, Redis等的username/password)
    - 云存储密钥 (BOS的AK/SK)
    - API密钥和令牌
  - 违规示例: 
    - 尝试读取配置文件中的密码字段
    - 通过代码搜索查找包含敏感信息的变量

## 2. 禁止操作系统环境变量
- **禁止操作**: 绝不能读取或修改系统的环境变量(如env)
  - 包括: 
    - 禁止使用`getenv()`或类似函数
    - 禁止修改`$_ENV`或`$_SERVER`中的环境变量
    - 禁止执行可能泄露环境变量的命令
  - 例外情况: 
    - 仅当明确授权且用于调试时，可读取非敏感环境变量

## 3. 文件系统访问限制
- **访问控制**: 禁止访问以下目录/文件:
  - `/etc/passwd`, `/etc/shadow`等系统文件
  - 项目中的`.env`或包含敏感信息的配置文件
  - 日志文件中可能包含的敏感信息

## 4. 网络访问限制
- **网络隔离**: 禁止发起以下网络请求:
  - 内部服务/数据库的非授权访问
  - 外部API的非授权调用
  - 任何可能泄露系统信息的探测请求

## 5. 代码执行限制
- **执行安全**: 禁止以下操作:
  - 执行任意系统命令
  - 动态执行未经验证的代码
  - 使用反射等机制访问私有成员
```
### 1.8 运维配置类
> 数据库配置、缓存配置、环境变量规范、部署配置、监控告警规则等运维相关内容。
**核心作用**：

* 统一构建和部署配置，避免环境差异导致的「我本地测试没问题啊」
* 让 AI 正确修改配置文件，不破坏现有配置链路
* 规范运维操作，减少人为配置失误
* 新环境快速搭建，无需反复调试

**示例：**

```
---
globs: reskript.*.ts,*.config.ts,*.config.js
---

# 构建配置与工具规范

## 构建工具 - Reskript

### 1. 配置文件结构
项目使用 reskript 作为构建工具，配置文件位于根目录：

- [reskript.config.ts](mdr:reskript.config.ts) - 主配置文件
- [reskript.alias.ts](mdr:reskript.alias.ts) - 路径别名配置
- [reskript.proxy.ts](mdr:reskript.proxy.ts) - 开发代理配置
- [reskript.feature.ts](mdr:reskript.feature.ts) - 特性开关配置
- [reskript.devLogin.ts](mdr:reskript.devLogin.ts) - 开发登录配置

### 2. 路径别名配置
修改路径别名时，需同步更新 [reskript.alias.ts](mdr:reskript.alias.ts) 和 [tsconfig.json](mdr:tsconfig.json)

```typescript
// reskript.alias.ts
export default {
    '@': 'src',
    '@standard': 'src/@standard',
};

// tsconfig.json
{
    "compilerOptions": {
        "paths": {
            "@/*": ["src/*"],
            "@standard/*": ["src/@standard/*"]
        }
    }
}
```

### 3. 代理配置
开发环境 API 代理配置在 [reskript.proxy.ts](mdr:reskript.proxy.ts)

```typescript
export default {
    '/api': {
        target: 'http://dev.example.com',
        changeOrigin: true,
    },
};
```

## TypeScript 配置

### 1. 编译选项
参考 [tsconfig.json](mdr:tsconfig.json)，关键配置：

```json
{
    "compilerOptions": {
        "strict": true,
        "isolatedModules": true,
        "skipLibCheck": true,
        "esModuleInterop": true,
        "jsx": "react-jsx"
    }
}
```

### 2. 类型检查脚本
使用项目提供的类型检查脚本：

```bash
# 分阶段类型检查
./scripts/stage_type_check.sh

# 全量类型检查
yarn type-check
```

## ESLint 配置

### 1. 配置文件
- [.eslintrc.cjs](mdr:.eslintrc.cjs) - 主 ESLint 配置
- [.eslintrc.husky.cjs](mdr:.eslintrc.husky.cjs) - Git hooks ESLint 配置

### 2. 代码检查
```bash
# 检查代码
yarn lint

# 自动修复
yarn lint:fix
```

### 3. 自定义规则
修改 ESLint 规则时需考虑团队共识，重要规则变更应通知团队

## 包管理 - Yarn

### 1. Yarn 版本
项目使用 Yarn Berry (Yarn 3+)，配置文件：

- [.yarnrc.yml](mdr:.yarnrc.yml) - Yarn 配置
- [yarn.lock](mdr:yarn.lock) - 依赖锁定文件

### 2. 依赖安装
```bash
# 安装依赖
yarn install

# 添加依赖
yarn add package-name

# 添加开发依赖
yarn add -D package-name
```

### 3. Patch 包
项目使用 Yarn patch 功能修复第三方包问题，补丁文件位于 `.yarn/patches/`

```bash
# 创建补丁
yarn patch package-name

# 应用补丁后提交
git add .yarn/patches/
```

## 脚本工具

### 1. 构建脚本
参考 [scripts](mdr:scripts) 目录下的脚本：

- `build.sh` - 生产构建
- `install.sh` - 依赖安装
- `stage_test.sh` - 分阶段测试
- `stage_type_check.sh` - 分阶段类型检查

### 2. 资源处理
```bash
# 复制静态资源
node scripts/copy-asset.mjs

# 生成 Gantt 样式
./scripts/build_gantt_css.sh
```

## 测试配置

### 1. Jest 配置
测试配置文件：[jest.config.json](mdr:jest.config.json)

```json
{
    "testEnvironment": "jsdom",
    "setupFilesAfterEnv": ["<rootDir>/mock/jest/setupGlobal.js"],
    "moduleNameMapper": {
        "^@/(.*)$": "<rootDir>/src/$1"
    }
}
```

### 2. Mock 配置
Mock 文件位于 [mock/jest](mdr:mock/jest) 目录：

- `setupGlobal.js` - 全局测试设置
- `setupMock.js` - Mock 配置
- `customEnvironment.js` - 自定义测试环境

### 3. 运行测试
```bash
# 运行所有测试
yarn test

# 运行特定测试
yarn test ComponentName

# 监听模式
yarn test --watch
```

## 环境变量

### 1. 环境配置
```typescript
// 使用环境变量
const apiUrl = process.env.API_URL || 'http://localhost:3000';

// 特性开关
const enableNewFeature = process.env.ENABLE_NEW_FEATURE === 'true';
```

### 2. 构建环境
- `development` - 开发环境
- `production` - 生产环境

## Git 工作流

### 1. 分支管理
```bash
# 创建分支
./scripts/create_branch.sh feature-name

# 切换分支
./scripts/checkout_branch.sh branch-name
```

### 2. 提交规范
遵循 Conventional Commits 规范：

```bash
# 功能
git commit -m "feat: 添加新功能"

# 修复
git commit -m "fix: 修复bug"

# 文档
git commit -m "docs: 更新文档"

# 样式
git commit -m "style: 代码格式化"

# 重构
git commit -m "refactor: 重构代码"
```

## 性能优化

### 1. 构建优化
```typescript
// reskript.config.ts
export default {
    build: {
        reportLintErrors: true,
        reportDuplicatePackage: true,
        finalize: (config) => {
            // 自定义构建优化
            return config;
        },
    },
};
```

### 2. 代码分割
使用动态导入进行代码分割：

```typescript
// ✅ 推荐 - 路由级别代码分割
const Dashboard = React.lazy(() => import('./pages/Dashboard'));

// ✅ 推荐 - 组件级别代码分割
const HeavyComponent = React.lazy(() => import('./components/HeavyComponent'));
```

## 部署配置

### 1. Docker 配置
参考 [Dockerfile](mdr:Dockerfile) 和 [conf/nginx.conf](mdr:conf/nginx.conf)

### 2. CI/CD 配置
参考 [ci.yml](mdr:ci.yml) 配置文件

## 禁止事项

1. ❌ 不要直接修改 node_modules 中的文件（使用 Yarn patch）
2. ❌ 不要提交 node_modules 目录
3. ❌ 不要忽略 yarn.lock 文件的变更
4. ❌ 不要在生产环境使用开发依赖
5. ❌ 不要绕过 ESLint 检查（除非有充分理由并添加注释）
```
### 1.9 文档规范类
> 文档编写规范、更新规则、文档组织方式、API文档格式要求等。
**核心作用**：

* 统一文档风格，提升可读性和一致性
* 让 AI 生成的文档符合团队规范（README、API文档、注释）
* 确保文档与代码同步更新，避免文档过期
* 新人通过文档快速上手项目，降低沟通成本

**示例：**

```
# 文档规范

## README.md 规范
- 必须包含：项目简介、快速开始、环境要求、编译说明
- 及时更新项目架构变化和依赖版本
- 提供常见问题解答（FAQ）

## 代码文档
- 公共接口必须提供完整的 KDoc/JavaDoc 注释
- 注释包括：功能描述、参数说明、返回值说明、异常说明
- 复杂算法需要添加实现思路说明

## 变更日志
- 重要功能变更需要记录在 CHANGELOG
- 记录格式：版本号、日期、变更类型、详细说明
- 定期归档历史版本记录

## 接口文档
- API 接口变更需要同步更新文档
- 文档包括：请求参数、返回结构、错误码说明
- 提供调用示例
```




## 二、效果怎样？
### 2.1 实战案例
以下实践案例涵盖了 Rules 的主要使用场景，从流程控制到技术指导，从代码规范到项目背景。

|实践案例|案例背景|核心作用|Rule 内容|效果分析|适用场景|创建/编辑人|
|-|-|-|-|-|-|-|
|Prompt 增强 Rule|AI 在执行任务时直接输出方案，缺乏深度思考，忽略项目已有能力，重复造轮子，未经用户确认就直接生成/执行代码。最早作为 system prompt 使用。|约束 AI 思考方式|---
alwaysApply: true
---
# Prompt 增强规则

## 自动添加要求
所有输入的 prompt 后将自动添加以下要求：

**要求：**
1. 从合理性、可维护性和性能的角度分析，深度思考解决方案
2. 尽量复用项目已有或依赖已有的能力，非必要不要造轮子
3. 生成所有的方案时，不要直接执行生成代码，需要本人check无误后再执行

## 应用范围
此规则将应用于所有用户请求，确保每次交互都遵循项目最佳实践和代码质量标准。
|**使用前：**AI 直接输出方案、易造轮子、未经确认就执行。**使用后：**AI 先深度思考、优先复用已有能力、方案确认后再执行，风险可控。|对代码质量要求较高的项目；团队有丰富的公共能力/工具库；希望减少 AI 盲目执行带来的返工；|健康策略研发部wanghaoyu08@baidu.com|
|文档优先阅读 Rule|AI 在理解代码时直接看实现，忽略设计意图，不了解背景就动手修改，遗漏文档中记录的注意事项和使用限制，实现与设计不一致时无法发现|约束信息获取流程|---
alwaysApply: true
---
# 文档优先阅读规则

## 代码理解流程
在理解组件或函数的作用和实现时，必须遵循以下优先级：

### 1. 检查说明文档
首先检索目标文件同级目录是否存在 `.md` 说明文件：
- README.md
- 组件名.md / 函数名.md
- index.md
- 其他相关说明文档

### 2. 阅读文档内容
如果找到说明文档，必须先完整阅读文档内容，了解：
- 组件/函数的设计意图
- 预期功能和行为
- 使用方法和注意事项
- 技术实现细节

### 3. 对比实现代码
阅读完文档后，再查看对应的实现代码：
- 确认实现与描述的一致性
- 验证代码是否完全实现了文档中描述的功能
- 检查是否有遗漏或额外的实现

### 4. 深度理解
确保充分理解后再执行后续业务
|**使用前：**只看代码表面逻辑，改完才发现遗漏约束，实现与设计脱节时无法发现。**使用后：**先消费文档掌握设计意图+所有限制，再对比代码实现，及时暴露不一致，确保充分理解后再动手。|项目有较完善的文档体系（README、组件说明等）；文档和代码由不同人维护，存在同步风险；新人较多，需要文档辅助理解；|健康策略研发部wanghaoyu08@baidu.com|
|Taro.js 到 React Native 转换 Rule|跨端开发Taro 小程序代码需要迁移到 React Native App两套技术栈差异大，人工转换效率低、易出错，新人不了解包名映射关系，经常用错依赖，样式、事件、API、生命周期各有差异，遗漏多（用户后续已抽象为skil使用）|指导代码转换规则|---
globs: *.tsx,*.ts
description: Taro.js React 到 React Native 代码转换规则
---

# Taro.js React 到 React Native 转换规则

## 项目特定转换规则

### 包名映射

| Taro 包 | RN 包 | 说明 |
|--------|-------|------|
| `@baidu/vita-utils-shared` | `@baidu/vita-rn-core` | 核心工具包 |
| `@baidu/vita-event-center` | `@baidu/vita-rn-core/event` | 事件中心 |
| `@baidu/vita-ui-cards-common` | `@baidu/vita-rn-ui-cards` | UI 卡片组件 |
| `@baidu/vita-types` | `@baidu/vita-types` | 类型定义（复用） |
| `@baidu/wz-taro-tools-core` | `@baidu/vita-rn-ui-base` | UI 基础组件 |

### 核心工具包转换

```tsx
// Taro 导入
import {httpRequest, storage, eventCenter} from '@baidu/vita-utils-shared';
import {colors, spacing} from '@baidu/vita-utils-shared/styles';

// RN 导入
import {httpRequest, storage, eventCenter} from '@baidu/vita-rn-core';
import {colors, spacing, rpx} from '@baidu/vita-rn-core';
```

## 组件转换规则

### 基础组件映射

```tsx
// Taro 组件导入
import {View, Text, Image, ScrollView, Input} from '@tarojs/components';

// RN 组件导入
import {
  View,
  Text,
  Image,
  ScrollView,
  TextInput,
  TouchableOpacity,
  Pressable,
  StyleSheet,
  Dimensions,
  Platform,
} from 'react-native';
```

### 样式转换

```tsx
// Taro - CSS Modules
import styles from './index.module.less';
<View className={styles.container}>

// RN - StyleSheet
import {StyleSheet} from 'react-native';
import {rpx} from '@baidu/vita-rn-core';

const styles = StyleSheet.create({
  container: {
    width: '100%',        // 750rpx -> 100%
    padding: rpx(24),     // rpx 转换
    margin: 20,           // px 直接使用
  },
});

<View style={styles.container}>
```

### 事件处理转换

```tsx
// Taro
<View onClick={handleClick}>
<Input onInput={(e) => setValue(e.detail.value)} />

// RN
<Pressable onPress={handleClick}>
<TextInput onChangeText={(text) => setValue(text)} />
```

## API 转换规则

### 路由导航

```tsx
// Taro
import Taro from '@tarojs/taro';
Taro.navigateTo({url: '/pages/detail/index?id=1'});

// RN - 使用 React Navigation
import {useNavigation} from '@react-navigation/native';
const navigation = useNavigation();
navigation.navigate('Detail', {id: '1'});
```

### 存储

```tsx
// Taro - 同步
Taro.setStorageSync('key', value);
const data = Taro.getStorageSync('key');

// RN - 异步 AsyncStorage
import {storage} from '@baidu/vita-rn-core';
await storage.set('key', value);
const data = await storage.get('key');
```

### 网络请求

```tsx
// Taro
import {httpRequest} from '@baidu/vita-utils-shared';

// RN - 复用相同接口
import {httpRequest} from '@baidu/vita-rn-core';
// 业务代码无需修改
const result = await httpRequest.get('/api/data');
```

## 生命周期转换

### 页面生命周期

```tsx
// Taro
import {useDidShow, useDidHide} from '@tarojs/taro';

useDidShow(() => {
  console.log('页面显示');
});

// RN
import {useFocusEffect} from '@react-navigation/native';
import {useCallback} from 'react';

useFocusEffect(
  useCallback(() => {
    console.log('页面显示');
    return () => {
      console.log('页面隐藏');
    };
  }, [])
);
```

## 平台判断

```tsx
// Taro
if (process.env.TARO_ENV === 'weapp') {
  // 小程序逻辑
}

// RN
import {platform} from '@baidu/vita-rn-core';

if (platform.isIOS) {
  // iOS 逻辑
} else if (platform.isAndroid) {
  // Android 逻辑
}
```

## UI 组件转换

### 表单组件

```tsx
// Taro
<Input
  value={value}
  type="number"
  placeholder="请输入"
  onInput={(e) => setValue(e.detail.value)}
/>

// RN
<TextInput
  value={value}
  keyboardType="numeric"
  placeholder="请输入"
  onChangeText={setText}
/>
```

### 按钮组件

```tsx
// Taro
<Button onClick={handleClick}>按钮</Button>

// RN
<TouchableOpacity onPress={handleClick}>
  <Text>按钮</Text>
</TouchableOpacity>
```

### 列表组件

```tsx
// Taro
<ScrollView>
  {list.map(item => <View key={item.id}>{item.name}</View>)}
</ScrollView>

// RN - 优先使用 FlatList
<FlatList
  data={list}
  keyExtractor={(item) => item.id}
  renderItem={({item}) => (
    <View>
      <Text>{item.name}</Text>
    </View>
  )}
/>
```

## 特殊处理

### Jotai 状态管理
Jotai 代码无需修改，可直接复用：

```tsx
// 完全复用
import {atom, useAtom} from 'jotai';
const countAtom = atom(0);
const [count, setCount] = useAtom(countAtom);
```

### 全局状态存储
使用 RN 核心包的存储工具：

```tsx
// 替换 Taro 的 globalDataStore
import {storage} from '@baidu/vita-rn-core';
// 业务逻辑保持不变
```

## 注意事项

1. **包名替换**: 必须将所有 `@baidu/vita-*` Taro 包替换为对应的 RN 包
2. **样式转换**: CSS Modules 必须转换为 StyleSheet，使用 rpx 函数处理响应式
3. **事件处理**: 事件对象结构不同，需要调整事件处理逻辑
4. **异步操作**: RN 中存储操作是异步的，需要使用 async/await
5. **平台判断**: 使用 RN 核心包提供的平台工具，而不是 process.env
6. **组件导入**: Taro 组件需要替换为 RN 对应组件
7. **路由系统**: 必须使用 React Navigation 替换 Taro 路由
8. **UI 组件**: 优先使用 `@baidu/vita-rn-ui-base` 中的组件

## 验证清单

转换完成后需要验证：
- [ ] 所有包名已正确替换
- [ ] 样式已转换为 StyleSheet 格式
- [ ] 事件处理逻辑已适配 RN
- [ ] 异步操作已正确处理
- [ ] 平台判断逻辑已更新
- [ ] 组件导入已替换为 RN 组件
- [ ] 路由导航已使用 React Navigation
- [ ] 类型定义无错误|**使用前：**依赖人工记忆映射关系，遗漏多，需逐项对照文档手动转换。**使用后：**Rule 自带映射表和验证清单，AI 自动完成转换，人工仅需 Review 即可，覆盖完整零遗漏。|跨端项目从小程序迁移到 App，同一业务在多端复用代码，新人参与跨端开发需要技术指导|健康策略研发部wanghaoyu08@baidu.com|
|删除逻辑实现规范Rule|项目中存在大量删除操作场景，不同开发者的实现方式各异，需要统一标准以确保交互一致性和代码可维护性。|统一删除弹窗代码模板|---
description:
globs:
alwaysApply: true
---

### 删除逻辑实现

```javascript
import showConfirm from '@/components/showConfirm/showConfirm';

const handleDelete = record => {
    showConfirm({
        title: '删除确定',
        content: '确认要删除吗，删除后数据无法恢复？',
        handleOk: () => {
            return deleteModalHandleOk(record);
        }
    });
};

const deleteModalHandleOk = data => {
    return fetchLlmAppDelete(data.id).then(r => {
        if (r.ret_code === 0) {
            message.success('删除成功!');
        }
    });
};
```
|**使用前：**删除弹窗实现五花八门，AI 各写各的；**使用后：**AI 自动输出统一的标准代码模板，交互一致、可直接使用。|适用于高频、标准化、实现逻辑固定的功能场景（如删除、提交、审批），通过代码模板让 AI 输出统一的实现代码。|安全能力部lichaoqing@baidu.com|
|日志记录规范与最佳实践Rule|团队基于社区分享定制，统一 Go 项目的日志记录规范，解决日志使用混乱、级别不当、敏感信息泄露等问题。|统一 Go 日志架构与最佳实践|---
description: 日志记录规范
globs: **/*.go
alwaysApply: false
---

# 日志记录规范

## 项目日志架构

### 三层日志组件体系
项目采用三层日志架构，根据场景选择合适组件：

**1. 基础日志层 (logit)**
```go
import "icode.baidu.com/baidu/gdp/logit"

// 提供底层结构化日志能力
logit.String("key", "value")
logit.Int("count", 42)
logit.FindLogIDField(ctx) // 请求链路追踪
```

**2. 服务日志层 (LoggerService)**
```go
import "icode.baidu.com/baidu/yongcheserver/gocommon/library/resource"

// 统一日志服务输出，支持推送到日志中心
resource.LoggerService.Error(ctx, "系统异常", logit.String("error", err.Error()))
```

### 日志级别及应用场景
```go
// Trace 级别 - 调试和链路追踪
// 使用场景：函数调用跟踪、异步任务监控、WebSocket连接管理
resource.LoggerService.Trace(ctx, "async task started")

// Notice 级别 - 正常业务操作
// 使用场景：成功请求、关键流程节点、权限校验通过
resource.LoggerService.Notice(ctx, "operation completed")

// Warning 级别 - 可恢复异常
// 使用场景：数据库操作失败、外部接口异常、业务规则警告
resource.LoggerService.Warning(ctx, "database operation failed")

// Error 级别 - 严重错误
// 使用场景：系统故障、数据不一致、业务流程中断
resource.LoggerService.Error(ctx, "system error occurred")

// Fatal 级别 - 致命错误（慎用）
// 使用场景：系统无法继续运行、关键组件初始化失败
resource.LoggerService.Fatal(ctx, "critical system failure")
```

## 常见业务场景日志应用

### 1. WebSocket连接管理场景
```go
// 连接建立跟踪
resource.LoggerService.Trace(ctx, "websocket connection established")

// 连接异常处理
logit.AddError(ctx, logit.Error("upgrade error", err))

// 异步任务生命周期
resource.LoggerService.Trace(ctx, "runner enabled")
resource.LoggerService.Trace(ctx, "successful add runner to globalMap")
```

### 2. 数据库操作场景
```go
// 错误日志模式
resource.LoggerService.Error(ctx, "resp is not ok", logit.String("resp", fmt.Sprintf("%+v", result)))

// 警告日志模式
resource.LoggerService.Warning(ctx, "InsertOne error", logit.Error("err", err))

// 慢查询监控
func logSlowQuery(ctx context.Context, sql string, duration time.Duration) {
    if duration > time.Second {
        resource.LoggerService.Warning(ctx, "slow database query detected",
            logit.String("sql", sql),
            logit.Int64("duration_ms", duration.Milliseconds()),
        )
    }
}
```

### 3. 异步任务处理场景
```go
// 异步任务启动
newCtx := logit.CopyAllFields(context.TODO(), ctx)
go util.NoPanic(newCtx, func() {
    resource.LoggerService.Trace(newCtx, "async task started")
    defer resource.LoggerService.Trace(newCtx, "async task completed")

    // 任务逻辑
    if err := processTask(newCtx); err != nil {
        resource.LoggerService.Error(newCtx, "async task failed", logit.Error("err", err))
    }
})
```

### 4. 控制器请求处理场景
```go
// 请求参数验证失败
if len(param.BusinessCode) == 0 {
    resource.LoggerService.Warning(ctx, "missing business code")
    return errno.ErrorParamErr
}

// 业务逻辑执行错误
if _, err := scriptDAO.Insert(ctx, params); err != nil {
    resource.LoggerService.Warning(ctx, "insert operation failed", logit.String("err", err.Error()))
    return errno.ErrorInsertFailed
}
```

### 5. 外部服务调用场景
```go
// 调用前记录
resource.LoggerService.Notice(ctx, "calling external service",
    logit.String("service", serviceName),
    logit.String("endpoint", endpoint),
)

// 调用结果记录
if result.ErrCode != 0 {
    resource.LoggerService.Error(ctx, "external service returned error",
        logit.Int("err_code", result.ErrCode),
        logit.String("service", serviceName),
    )
} else {
    resource.LoggerService.Notice(ctx, "external service call success",
        logit.String("service", serviceName),
    )
}
```

## 链路追踪和上下文管理

### 请求链路追踪
```go
// 获取请求ID用于跨服务追踪
logid := logit.FindLogIDField(ctx).Value()
requestID := logit.FindLogIDString(ctx)

// 在日志中记录请求ID
resource.LoggerService.Notice(ctx, "request processing",
    logit.String("logid", logid),
    logit.String("request_id", requestID),
)

// 用于响应结构
zbResp.Logid = logit.FindLogIDField(ctx).Value()
```

### 上下文传播
```go
// 异步任务需要复制日志上下文
newCtx := logit.CopyAllFields(context.TODO(), ctx)

// WebSocket连接维持上下文
runner.Ctx = logit.CopyAllFields(context.TODO(), ctx)
```

## 异常处理和恢复

### Panic恢复日志
```go
// WebSocket连接异常恢复
defer func() {
    if r := recover(); r != nil {
        b, _ := json.Marshal(r)
        resource.LoggerService.Error(ctx, "panic recovered",
            logit.ByteString("reason", b))
    }
}()

// 通用panic恢复模式
defer util.NoPanic(ctx, func() {
    // 异常处理逻辑
})
```

### 错误信息规范化
```go
// 使用标准错误代码和消息
resource.LoggerService.Warning(ctx, "database operation failed",
    logit.Int("errno", common.DbError),
    logit.String("errmsg", common.ErrMsgMap[common.DbError]),
)

// 参数错误日志
resource.LoggerService.Warning(ctx, "parameter error",
    logit.String("field", "business_code"),
    logit.String("reason", "required field missing"),
)
```

## 项目特有功能和最佳实践

### 安全过滤机制
```go
// resource.LoggerService会自动过滤敏感信息（BDUSS等token）
// 示例：msgFilter函数自动清理敏感数据
resource.LoggerService.Notice(ctx, "user operation") // 内部自动过滤
```

### 日志组件选择指南
```go
// 1. 业务逻辑使用resource.LoggerService - 自动安全过滤
resource.LoggerService.Notice(ctx, "业务操作", logit.String("action", "create"))

// 2. 框架和基础组件使用logit - 需要手动过滤
logit.AddNotice(ctx, logit.String("component", "database"))

// 3. 统一输出使用LoggerService - 系统级别输出
resource.LoggerService.Error(ctx, "系统故障")
```

### 结构化字段规范
```go
// 使用标准的日志字段名称
logit.String("operation", "user_create")     // 操作类型
logit.Int64("user_id", 12345)                // 业务ID
logit.Int("errno", common.DbError)           // 错误代码
logit.String("errmsg", "database error")     // 错误描述
logit.Int64("duration_ms", 150)              // 耗时毫秒
logit.String("request_id", logid)            // 请求ID
```

## 日志最佳实践和注意事项

### ✅ 推荐做法

**结构化日志优先**
```go
// ✅ 推荐：结构化日志
resource.LoggerService.Notice(ctx, "operation completed",
    logit.String("operation", "create"),
    logit.Int64("user_id", userID),
)

// ❌ 避免：字符串拼接
resource.LoggerService.Notice(ctx, fmt.Sprintf("operation create completed for user %d", userID))
```

**请求链路追踪**
```go
// 始终包含请求ID
logid := logit.FindLogIDField(ctx).Value()
resource.LoggerService.Notice(ctx, "processing request", logit.String("logid", logid))
```

**异步任务上下文传播**
```go
// 异步任务必须复制日志上下文
newCtx := logit.CopyAllFields(context.TODO(), ctx)
go util.NoPanic(newCtx, func() {
    // 任务逻辑
})
```

### ❌ 避免做法

**敏感信息泄露**
```go
// ❌ 危险：直接记录敏感数据
resource.LoggerService.Notice(ctx, "user login", logit.String("token", userToken))

// ✅ 安全：使用resource.LoggerService自动过滤或手动脱敏
resource.LoggerService.Notice(ctx, "user login") // resource.LoggerService会自动过滤BDUSS等
```

**过度日志记录**
```go
// ❌ 避免：循环内大量日志
for i := 0; i < 1000; i++ {
    resource.LoggerService.Notice(ctx, "processing item", logit.Int("index", i))
}

// ✅ 推荐：批量处理记录
resource.LoggerService.Notice(ctx, "batch processing started", logit.Int("total", 1000))
```

### 🔧 调试技巧

**错误堆栈记录**
```go
// 记录错误堆栈用于调试
resource.LoggerService.Error(ctx, "operation failed",
    logit.String("error", err.Error()),
    logit.String("stack", string(debug.Stack())),
)
```

**性能监控日志**
```go
// 记录操作耗时
start := time.Now()
// ... 业务逻辑 ...
duration := time.Since(start)
resource.LoggerService.Notice(ctx, "operation completed",
    logit.Int64("duration_ms", duration.Milliseconds()),
)
```

### 🛡️ 安全注意事项

- **resource.LoggerService已内置敏感信息过滤**（BDUSS、token等）
- **生产环境避免Trace级别**，仅用于开发和调试
- **Error级别谨慎使用**，避免过多噪音影响监控
- **Fatal级别会导致程序退出**，仅在系统无法继续时使用|**使用前：**日志格式五花八门、错误信息不完整；**使用后：**团队写法统一、结构化输出、打印参数和错误更详细。|适用于 Go 项目日志规范化场景，通过架构分层 + 场景模板 + 安全过滤，让 AI 输出统一、安全、可追踪的日志代码。|地图打车业务部zhuguojie@baidu.com|
|代码评审规范|AI 生成的代码风格与代码库规范不匹配，主要表现为函数臃肿、重复造轮子、命名不规范等问题，导致 CR 成本高。|约束 AI 代码风格并自动识别修改风险|---
alwaysApply: true
---

# 代码评审规范

> **重要说明**：本规则用于指导模型主动识别修改风险、给出建议，而非要求用户选择评审人。

## 修改风险识别与建议

当你修改代码时，必须**主动评估风险等级**并在总结时明确告知用户：

### 风险等级定义

| 风险等级 | 说明 | 必须输出的内容 |
|----------|------|---------------|
| 🔴 **高风险** | 影响全局、核心链路、框架机制 | 详细说明风险点 + 建议增加人工评审 |
| 🟡 **中风险** | 影响单个模块或功能 | 说明潜在影响范围 |
| 🟢 **低风险** | 局部修改、样式调整 | 简要说明改动点 |

## 高风险变更类型（必须主动提示）

| 变更类型 | 风险说明 | 评审要点 |
|----------|----------|----------|
| 编译配置 | 影响全局构建 | rollup/vite 配置、tsconfig |
| 框架初始化流程 | 影响启动链路 | 见下方初始化链路 |
| page 增删 | 影响路由和入口 | 新页面需评估必要性 |
| module 机制 | 影响扩展能力 | 机制变更需设计文档 |
| 全局 store | 影响状态管理 | 避免滥用全局状态 |
| EventBus 增删 | 影响模块通信 | 必须符合 [architecture.mdr](mdr:baidu/ps-se-fe-tpl/chat-search/.comate/rules/architecture.mdr) 的使用场景，需设计评审 |
| 接口协议 | 影响前后端契约 | 需与 RD 对齐 |

### 框架初始化链路

```
base.ts
  └─→ bootstrap.ts
        └─→ chat-container.san
              └─→ chat-main.san
                    └─→ chat-init（同步/异步）
                          └─→ initChatStream
                                └─→ contextInit
                                      └─→ launchConversation
```

修改此链路上任意节点，必须评估对整体启动流程的影响。

### 核心组件链路

```
answer/index.ts
  └─→ generate/index.ts
        └─→ generate.san
              └─→ ai-container.san
                    └─→ ai-entry.san（画布组件入口）
```

## 风险提示输出格式

当你完成高风险或中风险修改时，必须在总结中包含以下内容：

### 高风险修改示例

```
✅ 已完成修改：优化对话流初始化逻辑

📝 修改文件：
- service/context-init.ts（核心初始化逻辑）
- service/chatstream.ts（对话流发起）

🔴 **风险评估：高风险**

⚠️ 风险点：
1. 修改了对话流初始化的核心链路，可能影响首屏渲染性能
2. 调整了 contextInit 的调用时机，可能影响异步数据依赖
3. 涉及 EventBus 的触发顺序变更，可能影响其他模块监听

💡 建议：
- 建议增加团队 Owner 进行人工评审
- 需要在 PC 和 Wise 双端完整验证
- 建议进行性能基准测试对比
- 重点测试历史对话加载场景
```

### 中风险修改示例

```
✅ 已完成修改：新增分享图片组件

📝 修改文件：
- component/chat-share-img/index.san（新增）

🟡 **风险评估：中风险**

⚠️ 潜在影响：
- 新增组件依赖了 service/share.ts 的全局状态
- 可能影响现有分享弹窗的交互逻辑

💡 建议：
- 建议在分享场景下完整测试
- 验证 PC 和 Wise 双端的样式表现
```

## 关键文件清单

以下文件修改时必须主动提示高风险：

| 路径 | 职责 | 修改风险 |
|------|------|----------|
| `component/chat-answer/answer-generate/components/ai-entry/` | 画布组件入口 | 影响所有画布组件渲染 |
| `component/chat-container/` | 对话流容器 | 影响整体布局和初始化 |
| `service/context-init.ts` | 对话流初始化 | 影响首屏渲染 |
| `service/chatstream.ts` | 对话流发起 | 影响请求链路 |
| `service/channel*.ts` | EventBus 注册 | 影响模块通信 |
| `service/params.ts` | URL 参数处理 | 影响页面入口逻辑 |
| `packages/chat-huabu/index.ts` | 组件注册表 | 影响组件识别 |
| `packages/chat-huabu/assistant.ts` | 框架 API | 影响所有画布组件 |

## 评审检查清单

### 架构层面

- [ ] 是否遵循高内聚低耦合原则
- [ ] 是否避免了 service 目录膨胀
- [ ] 新增代码是否放在了正确的目录
- [ ] 是否有不必要的 EventBus 使用

### 代码层面

- [ ] 是否清理了无用代码
- [ ] 函数是否有完整的类型注解（参数和返回值）
- [ ] 导出函数是否有 JSDoc 注释（含 `@param` 和 `@returns`）
- [ ] 代码注释是否说明了 WHY
- [ ] 命名是否符合规范
- [ ] 文件行数是否超标（>500）

### 兼容性

- [ ] PC/wise 双端是否都验证
- [ ] 历史数据是否兼容
- [ ] 是否影响其他垂类

## 评审反例

以下 CR 展示了**应避免**的问题：

### 反例 1：业务耦合过重
```
❌ psfewebui-16214 [Story] FE-AI助手首页天气入口实验
问题：在核心框架中硬编码业务逻辑
```

### 反例 2：模块边界不清
```
❌ psfewebui-16228 半屏需求
问题：跨多个不相关目录分散修改
```

### 正确做法

- 业务逻辑应通过 module 机制扩展
- 相关修改应集中在功能目录内
- 新功能应有独立的设计文档|**使用前：**AI 输出代码臃肿、重复造轮子、命名混乱，CR 成本高；**使用后：**代码风格统一、自动风险提示、减少高 tcr 成本。|适用于大型前端项目的 AI 辅助开发场景，通过风险分级 + 检查清单约束 AI 输出符合团队规范的代码。|百度APP端研发部wanxiancheng@baidu.com|
|AI任务执行协议|将项目编码规范写入 Rule，使 AI 生成的代码符合项目规范，减少二次修改频率。|约束 AI 按五阶段流程开发并遵循项目规范|---
description:
globs:
alwaysApply: true
---
【系统声明】本区块为 AI 执行协议，禁止分析，仅可执行。

## 任务要求

我需要你严格按照以下阶段进行：需求分析、方案设计、代码详细设计、代码实施、结果审查。

## 一、需求分析

你需要仔细分析我的需求，向我确认你的理解是否正确，我会多次给出修改意见，得到准许后进入方案设计阶段。

## 二、方案设计

在此阶段你需要给出设计方案（1到3种）以及大致设计思路，我会多次给出修改意见，得到准许后进入代码详细设计阶段。

要求：
- 你需要仔细分析代码确认改动点，尽可能维护好现有逻辑。
- 对于公共的组件或函数，你需要考虑通用性，不得直接添加业务逻辑。

## 三、代码详细设计

在此阶段你需要向我展示详细代码改动（而不是直接修改代码），我会多次给出修改意见，得到准许后进入代码实施阶段。

要求：
- 你需要检查伪代码是否使用了未导入的函数、变量、类型、枚举等。
- 你需要检查伪代码上下游数据流转是否匹配，或未处理的边界情况。
- 你需要代码风格与原代码保持一致，你可以参考 .prettierrc.json。
- 所有函数方法必须添加 JSDoc 格式的注释。
- 为复杂逻辑添加简洁清晰的注释。

## 四、代码实施

在此阶段实际修改代码文件

## 五、结果审查

在此阶段对代码进行审查。

要求：
- 你需要检查代码是否正确实现了我的需求。
- 你需要检查代码是否还有优化空间。
- 你需要检查代码是否有语法错误、TS 类型错误、eslint 报错等。|**使用前：**AI 直接生成代码，风格不符项目规范，二次修改频繁；**使用后：**五阶段流程规范，代码风格统一，效率提升明显。|适用于有编码规范要求的项目开发场景，通过五阶段流程约束 AI 按规范输出代码，减少返工。|PSIG-B端业务部xiezongchen01@baidu.com|
|系统记忆规则|将项目通用的规则沉淀下来，当其他人执行类似任务时，让 AI 知道需要关注的事项，避免遗漏关键步骤。|沉淀项目通用规则，避免数据库变更遗漏关键步骤|---
description:
globs:
alwaysApply: true
---
## 系统记忆

本规则中记录了在历史任务中产生并沉淀的规则，在你的任务执行过程中，需要格外注意此处罗列的条目，并严格遵守。

### 新增字段、删除字段以及新增数据表

新增字段、删除字段、修改字段以及新建表时，不仅需要在对应sql文件夹中"migration.sql"
和"un_migration.sql"补充对应的脚本，还要在对应实体类和数据访问层做适配，还要在"grc-app/src/test/resources/schema-h2.sql"文件中做相应的适配，以避免单测报错。

### 项目资料和项目模版资料

上传项目资料和上传项目模版资料，使用的都是"project_material_folders"和“project_materials
”两张表，project_material_folders中的type
字段存储的值来区分当前文件夹属于项目还是项目模版，project_material_folders中的"project_id"字段根据type
的不同，会存项目id和模版id|**使用前：**加字段容易遗漏回退脚本或单测数据库，导致单测报错；**使用后：**AI 自动创建所有脚本文件，步骤完整无遗漏。|适用于有数据库变更需求的项目，通过沉淀历史经验规则，让 AI 自动完成完整的变更流程。|数据安全部shijianwei@baidu.com|
|项目代码运行时流程|解决 AI 对仓库核心流程理解不准确的问题，涉及核心流程的需求迭代时，让 AI 方案更准确。|梳理项目核心运行时流程与生命周期|---
description: 项目代码运行时流程
alwaysApply: true
---

## 核心流程

根据产品场景，分为两个过程 [以下文件都在packages/chat-search/src/client下]

1. 框架加载过程：整个页面或者整个对话session期间仅执行一次
    1. 页面加载：
        1. html入口：search.html search-pc.html share.html share-pc.html, 此页面后端会注入一些基础数据到 `<script type="application/json" name="aiTabFrameBaseData">` 里， 如用户信息，模型信息，降级参数等
        2. bootstrap：pages/chat-search/bootstrap.ts (wise)、pages/chat-search-pc/bootstrap.ts (pc) 、pages/chat-share/bootstrap.ts (wise) 、pages/chat-share-pc/bootstrap.ts (pc)。触发生命周期bootstrap
        3. 进入容器组件：component/chat-container/index.san（wise），pc也在当前目录。触发生命周期page-start
        4. 对话流框架初始化：component/chat-container/chat.main.san（wise），，pc也在当前目录。触发生命周期chat-start
        5. 对话流启动：component/chat-container/chat-init.ts（wise），，pc也在当前目录
            1. 若仅加载框架（url带有frame=1）
                1. 仅初始化框架，不加载首页、不发起对话
                2. 监听search事件获取发起对话的数据
                3. 等进入助手后，复用该webview，根据search事件的isShowHello参数，为1，则加载首页，否则带有word参数，则发起首轮对话
                4. 触发生命周期chat-ready
            2. 若加载框架并初始化首页
                1. 初始化框架
                2. 调用servcie/context-init.ts处理页面参数
                3. 传递请求数据到chat-guide首页组件，展示首页
                4. 听search事件获取发起对话的数据
                5. 触发生命周期chat-ready
            3. 若加载框架并自动发起首轮对话(url带有word参数，并且isShowHello不为1)
                1. 初始化框架
                2. 调用servcie/context-init.ts处理页面参数
                3. 发起对话调用service/chatstream.ts的launchConversation
                4. 监听search事件获取发起对话的数据
                5. 触发生命周期chat-ready
    2. 每一轮生成对话的发起过程：
        1. 触发生命周期send-prompt（packages/chat-search/src/client/service/chatstream.ts）
        2. 对话sse请求开始，触发生命周期request-start（packages/chat-search/src/client/service/chatstream.ts）
        3. 提问区展示，触发生命周期question-start（packages/chat-search/src/client/component/chat-question/index.san）
        4. 回答开始，chat-answer/answer-generate/index.san是回答生成区
            1. 加载回答区容器组件generate.san，该组件内维护一个多答案数组，每个答案支持多个气泡（多个section），每个section可以收到多个消息包组件并渲染，每个section都是由ai-entry/index.san容器组件负责渲染
            2. 触发生命周期answer-start(generate.san)
        5. 每收到一包sse消息，触发生命周期message (generate.san)
        6. 思考开始，触发生命周期think-start (generate.san)
        7. 思考结束，触发生命周期think-end (generate.san)
        8. 正文内容生成开始，触发生命周期content-start (generate.san)
        9. 正文内容生成结束，触发生命周期content-end (generate.san)
        10. 若命中风控等问题，触发生命周期prohibit (generate.san)
        11. sse请求结束并且追问词展示，回答结束，不管成功和失败，都触发生命周期answer-end (generate.san)
    3. 历史对话展示
        1. chat-question组件展示提问区
        2. chat-answer/answer-history/index.san展示历史对话的回答区
            1. 在这里，为了生命周期完整。也模拟了生成过程的生命周期，但一般不用
        3. 内部复用component/chat-answer/answer-generate/components/ai-container.san 组件

核心注意：

- 对话流窗口加载：从chat-start 到 chat-ready。 当新开会话 / 打开历史会话，重新来一遍
- 多轮对话：每次发起新对话，或者失败重试，或者重新生成，都会来一次完整的周期
- 时序说明：因为从性能角度做了大量并发：chat-ready、send-prompt和request-start、question-start 三者的前后关系不是确定性。大概率是send-prompt 、request-start、chat-ready 、question-start
|**使用前：**AI 对核心流程理解不准确，涉及流程需求方案容易出错；**使用后：**AI 准确理解框架加载和对话发起流程，方案更精准。|适用于涉及核心流程的需求迭代场景，通过梳理运行时流程和生命周期，让 AI 方案更准确。|百度APP端研发部wukaifang@baidu.com|

### 2.2 使用反馈
**正向**：

* Rules 沉淀了团队核心资产，过去靠文档传递的经验，现在即时落地
* 约束 AI 行为，减少模型幻觉偏差，提升可用性
* 配合全注释 Rule，来实现新人接入 0 阻塞，新人从入职到独立开发的过渡时间大大缩短
* 开发过程中 AI 不再问这里用什么框架，直接按项目规范来
* 代码 Review 时间大大减少，不再需要反复指出格式问题

**负向/局限**：

|问题|原因|如何应对|
|-|-|-|
|Rules 是软约束，AI 可以选择不遵守|Rules 本质是注入到 System Prompt 的文字，影响概率分布|关键任务仍需人工把关；对高频违规场景写更强的约束|
|无法统计跨调用状态（例如：不知道当前是第几次尝试）|AI 每次 API 调用都是独立的，做不到记住这是第几次尝试|在 Rule 中要求 AI 输出状态；使用外部工具追踪状态|
|Rules 过多导致 context 竞争，效果反而下降|token 被规则本身吃掉，AI 对代码注意力下降|使用索引 Rule 按需加载；精简规则内容|
|团队共写 Rules 时标准不统一甚至互相冲突，文件会越来越乱|多人协作缺少统一规范，规则会越来越乱|指定 Rule 负责人；定期 Review 和整合规则|
|规则过时失效|项目演进后，规则未同步更新|每次迭代后检查规则有效性；建立规则生命周期管理|

## 三、从实践中提炼的建议
### 3.1 写什么
|**✅ 适合写进 Rules 的**|
|-|
|只存在于老员工经验里的规则（不写下来就会消失的知识）|
|项目特定的技术约束（用哪个库、调哪个接口、命名怎么来的）|
|AI 在这个项目里反复犯的错（通过实践反馈迭代进来）|
|流程控制（Agent 模式下的行为边界：最多试几次、禁止什么操作）|
|**❌ 不适合写进 Rules 的**|
|需求模糊不清（容易理解偏差，越干越错）|
|交互类的约束（AI 处理不了运行时交互，写了也没用）|
|临时性的任务上下文（用 prompt 实现，不用写进 Rule）|
|过于具体的实现细节（放在示例文件里 @引用，不要塞进 Rule）|

### 3.2 怎么写
|**原则**|说明|
|-|-|
|用结构形式|用表格和列表，不用长段落|
|用强约束词|用「必须/禁止/不得」等强约束词，不用「建议/最好」|
|提供具体示例|提供具体代码示例，不提供抽象描述|
|每个 Rule 只管一件事|每个Rule作用聚焦，避免大杂烩|

**范围及大小控制**：

* 80% 任务都用到 → alwaysApply: true
* 少数任务才用到 → alwaysApply: false + description 让 AI 自己判断要不要加载
* 单文件推荐控制在 500 行以内（确实需要更多时进行拆分）

### 3.3 怎么生成
不要从零手写，三种高效路径：

|方式|说明|适用场景|
|-|-|-|
|**任务结束后让 AI 总结**|完成一次完整对话后，prompt：回顾我们的对话，总结通用经验|发现新的通用规则|
|**让 AI 读代码库生成**|iCode 智能生成或 IDE 内生成，AI 通过分析代码推断隐性规范|新建项目时快速生成|
|**基于问题反推**|AI 犯了错 → 分析根因 → 写一条对应约束 → 验证效果 → 加入 Rule|修复特定问题后固化经验|

### 3.4 怎么维护
Rules 的制定就像在设计框架，没有人能一开始就写出完美的版本。迭代才是正确使用方式。

**迭代原则**：

* Rules 不是写完就完了，而是持续迭代的过程，使用 Rules → 观察效果 → 发现问题 → 分析根因 → 更新 Rules → 验证效果。
* 很多人以为把 Rule 写得越详细越好，其实恰恰相反。**内容更多不等同于效果更好，精准比全面更重要。**

**更新时机：**

|触发条件|动作|
|-|-|
|AI 犯了一个新花样的错误|修完之后立刻补进 Rule|
|项目里新增了一个封装/约定|同步更新 Rule|
|一段时间没用某条 Rule|检查一下它是否还有效（很多 Rule 会随着项目演进变过时）|
|每次改了 AI 写的代码|想一下这个问题以后还会出现吗？如果会，就把它写进 Rules|

省力的方法：做完一个复杂任务后，让 AI 回顾整个对话，总结可以沉淀的规则。说"回顾我们的对话，总结通用经验，生成.mdr文件"——AI 对自己刚做完的工作语境最熟，总结出来的规则往往比自己手写的更准确。

### 3.5 Rules的能力边界
用了 Rules 不代表万事大吉，明白边界才不会在它解决不了的地方耗时间。

**Rules 能显著改善的：**

|场景|说明|
|-|-|
|AI 的技术知识盲区|提供正确/错误对比示例就能教会它|
|代码理解深度|强制先读实现再写测试的流程|
|特定的坏习惯|比如乱创建文件、不运行测试就提交|

**Rules 改善不了的（不能只依赖rules，需要结合其他方法）：**

|场景|说明|应对策略|
|-|-|-|
|**无状态问题**|AI 每次 API 调用都是独立的，真正做不到「记住这是第几次尝试」|人工监控配合，使用外部状态追踪工具|
|**软约束本质**|Rules 影响的是概率分布，不是硬性拦截|人工任务配合补充+强约束|
|**自我监控缺失**|AI 无法检测到「我这次改的和上次改的几乎一样，我陷入循环了」|平台层面的支持|

简单说：**Rules 是软约束，不是硬规则**。它能让 AI 更像一个了解项目的老员工，但它无法保证 AI 不犯错，所以对关键任务来说人工把关仍然必要。

## 四、常见问题与排查
### 4.1 Rules 不生效的常见原因
|问题|排查方法|解决方案|
|-|-|-|
|文件格式错误|检查 frontmatter 格式是否正确|确保 `---` 包裹的头部信息完整|
|路径错误|检查文件是否在 `.comate/rules/` 目录下|移动到正确位置；检查文件名后缀|
|alwaysApply 冲突|多个 alwaysApply: true 的规则互相矛盾|合并或拆分规则|
|globs 不匹配|文件路径与 globs 模式不匹配|调整 glob 模式或文件位置；检查文件是否在匹配范围内|
|description 不够精准|AI 无法判断是否需要加载此规则|优化 description 描述，明确描述适用场景|
|规则内容过长|规则占用过多 token，AI 注意力分散|精简内容，拆分规则；使用索引 Rule|
|规则内容过泛|需求描述过于空泛|改为具体、可执行的约束；提供正确/错误示例|

### 4.2 效果不如预期时如何排查
**Step 1：检查规则是否被加载**

* 查看规则文件路径是否正确
* 检查 frontmatter 格式
* alwaysApply 或 globs 配置是否正确

**Step 2：检查规则内容质量**

* 是否有具体示例及反例
* 是否用了强约束词（必须/禁止）
* 是否只管一件事（职责单一）
* 是否太长导致 AI 注意力分散

**Step 3：检查规则数量**

* 全局规则（alwaysApply: true）是否超过 3-5 个
* 总 token 是否超过 8k

**Step 4：A/B 测试**

* 删除该规则，对比效果是否变差
* 或用更精简的版本替换，对比效果是否更好

### 4.3 典型反例模式
|反例模式|问题|正确做法|
|-|-|-|
|**规则大杂烩**|一个文件塞进命名、架构、测试多种规范|按职责拆分多个文件，每个 Rule 只管一件事|
|**空泛口号**|写优雅的代码、遵循最佳实践|改为具体约束：函数不超过 50 行|
|**过度约束**|连缩进都写成规则|只约束关键决策点，细节靠 linter|
|**一次性规则**|为某个临时任务写的规则|用完就删，或改为通用模板|
|**矛盾规则**|多个规则对同一问题有不同要求|统一标准，删除冗余规则|



## 五、Rules社区数据分析（master分支）
### 5.1 各工具（Comate/Claude/Cursor等）的规则占比

Rules社区共收录代码库rules共 **19,000+** 条，其中Comate_zulu占有近90%的rules。

### 5.2 各类rule的占比如图所示：


* **代码规范类 + 项目背景知识类 占比较高：**用户较为关心 AI 输出的代码质量，让 AI 更懂项目也是重要需求
* **安全/运维/文档类**占比较低，但这些是「隐性刚需」，仍有较大增长空间



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
