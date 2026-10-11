---
title: "AI-Anchor项目 Comate 规则完整指南"
description: "电商-基于rules的后端项目敏捷开发"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\电商-基于rules的后端项目敏捷开发.md"
---
电商-基于rules的后端项目敏捷开发

#### 🧑‍🏫 案例作者：[@徐杰](https://ku.baidu-int.com?t=mention&mt=contact&id=19740d10-fced-11f0-aa3f-1102d394256b)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了电商技术部通过制定和实施.comate/rules规则体系，促进项目组研发规范落地，统一编码风格，提高开发效率，并降低新手上手难度。规则体系涵盖项目结构、语言编码标准、框架使用指南和业务逻辑模式，通过自动和条件应用机制确保规则的有效执行，显著提升开发质量和团队协作效率。
### **一、目标**
1. 开发人员编码风格不一致，通过rules促进项目组研发规范落地，促进风格统一。
2. 简单场景能够完全自动生成代码，复杂场景辅助开发，提高开发效率
3. 通过rules让新手了解项目层次和编码规范，降低新手上手难度

## 二、ai-anchor代码库rules规则
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b925ce4fecee4ad39fde1306d1b540cb&docGuid=CoK90Y1twBZT6u "")
#### 2.1 使用概览
```
# AI-Anchor项目 Comate 规则完整指南

> **最后更新**: 2025-12-08 | **维护团队**: AI-Anchor开发团队

---

## 📖 目录

1. [规则体系概览](#规则体系概览)
2. [规则加载机制](#规则加载机制)
3. [快速开始](#快速开始)
4. [规则文件索引](#规则文件索引)
5. [实际应用场景](#实际应用场景)
6. [最佳实践](#最佳实践)
7. [常见问题](#常见问题)

---

## 规则体系概览

### 什么是 .comate/rules

`.comate/rules` 是项目的代码规范和开发指南目录。当使用AI编码助手时，这些规则会自动被读取并应用到代码生成中，确保：

- ✅ 代码风格统一
- ✅ 框架使用规范
- ✅ 业务逻辑清晰
- ✅ 团队协作高效

### 目录结构

```
.comate/rules/
├── GUIDE.md                       # 本文件：完整指南
├── base/                          # 通用类规则（1个）
│   └── 01-project-structure.mdr   # 项目结构和架构
├── language/                      # 语言类规则（2个）
│   ├── 01-go-standards.mdr        # Go编码标准
│   └── 02-logging.mdr             # 日志记录规范
├── framework/                     # 框架类规则（3个）
│   ├── 01-gdp2-basics.mdr         # GDP2框架基础
│   ├── 02-gorm-database.mdr       # GORM数据库操作
│   └── 03-http-api.mdr            # HTTP API模式
└── biz/                           # 业务类规则（2个）
    ├── 01-business-logic.mdr      # 业务逻辑模式
    └── 02-domain-models.mdr       # 领域模型结构
```

### 规则分类说明

| 分类 | 文件数 | 用途 | 优先级 |
|-----|-------|------|--------|
| **base/** | 1 | 项目整体架构和通用规范 | 最高（总是应用） |
| **language/** | 2 | Go语言编码标准和日志规范 | 高 |
| **framework/** | 3 | GDP2和GORM框架使用指南 | 中 |
| **biz/** | 2 | 业务逻辑和领域模型规范 | 按需 |

---

## 规则加载机制

### 两种应用方式

#### 🔄 自动应用（Always Apply）

设置了 `alwaysApply: true` 的规则会**自动应用**到所有对话中。

**当前配置**：
- `base/01-project-structure.mdr` - 项目结构指南

#### 🎯 条件应用（Conditional Apply）

设置了 `globs` 的规则会**根据文件路径自动匹配**应用。

**匹配规则**：

| Glob模式 | 含义 | 示例 |
|---------|------|------|
| `**/*.go` | 所有Go文件（递归） | `controller/user/list.go` ✅ |
| `model/dao/**/*.go` | dao目录下所有Go文件 | `model/dao/user/db.go` ✅ |
| `controller/*.go` | controller目录直接子文件 | `controller/user.go` ✅ |

### 规则匹配优先级

```
1. alwaysApply: true 的规则（最高优先级）
   └─ base/01-project-structure.mdr

2. 业务类规则（biz/）
   ├─ 01-business-logic.mdr      (model/page/**/*.go, script/**/*.go)
   └─ 02-domain-models.mdr       (model/data/**/*.go, library/types/**/*.go)

3. 框架类规则（framework/）
   ├─ 01-gdp2-basics.mdr         (bootstrap/**/*.go, httpapi/**/*.go)
   ├─ 02-gorm-database.mdr       (model/dao/**/*.go, model/db/**/*.go)
   └─ 03-http-api.mdr            (httpapi/**/*.go, controller/**/*.go)

4. 语言类规则（language/）
   ├─ 01-go-standards.mdr        (**/*.go)
   └─ 02-logging.mdr             (**/*.go)
```

---

## 快速开始

### 第一步：了解项目规则

```bash
# 查看规则目录结构
tree .comate/rules/

# 阅读本指南
cat .comate/rules/GUIDE.md
```

### 第二步：按场景查找规则

#### 新建项目/模块
```
→ base/01-project-structure.mdr
→ language/01-go-standards.mdr
```

#### 编写控制器
```
→ framework/03-http-api.mdr
→ language/02-logging.mdr
```

#### 数据库操作
```
→ framework/02-gorm-database.mdr
→ language/01-go-standards.mdr
```

#### 业务逻辑实现
```
→ biz/01-business-logic.mdr
→ biz/02-domain-models.mdr
```

### 第三步：开始使用

向AI助手提问时，它会自动遵循这些规则！

**示例请求**：
```
请帮我创建一个用户管理的控制器
```

AI会自动遵循：
- 项目整体架构
- Go语言编码规范
- HTTP API控制器模式
- 日志记录规范

---

## 规则文件索引

### base/01-project-structure.mdr
**适用**: 整个项目 | **自动应用**: ✅

**内容**:
- 目录结构说明（bootstrap, controller, model, library等）
- 配置管理（conf, conf_test, conf_online, conf_sandbox）
- 构建部署（Makefile, Docker, CI/CD）
- 环境设置命令

---

### language/01-go-standards.mdr
**适用**: `**/*.go` | **自动应用**: 当编辑Go文件时

**内容**:
- 包声明和导入标准
- 命名约定（变量、常量、函数）
- 注释规范（强制注释要求）
- 类型定义（结构体、接口）
- 函数和方法
- 泛型使用
- 错误处理规范
- 性能优化
- 格式化标准

**示例**:
```go
// ✅ 正确的函数定义
// CreateUser 创建新用户
func CreateUser(ctx context.Context, req *CreateUserRequest) (*User, error) {
    // ...
}

// ❌ 错误的函数定义（缺少注释）
func CreateUser(ctx context.Context, req *CreateUserRequest) (*User, error) {
    // ...
}
```

---

### language/02-logging.mdr
**适用**: `**/*.go` | **自动应用**: 当编辑Go文件时

**内容**:
- 日志级别（Trace, Notice, Warning, Error, Fatal）
- 结构化日志
- 业务日志模式
- 链路追踪
- 安全日志
- 性能监控日志

**示例**:
```go
// ✅ 正确的日志记录
logsafe.Notice(ctx, "用户创建成功",
    "userID", user.ID,
    "username", user.Username)

logsafe.Error(ctx, "创建用户失败",
    "error", err,
    "username", req.Username)
```

---

### framework/01-gdp2-basics.mdr
**适用**: `bootstrap/**/*.go`, `httpapi/**/*.go`

**内容**:
- 应用初始化流程
- HTTP服务配置
- 中间件使用
- 配置管理
- 监控指标

---

### framework/02-gorm-database.mdr
**适用**: `model/dao/**/*.go`, `model/db/**/*.go`

**内容**:
- DB结构体命名（*DB后缀）
- 模型定义（GORM标签）
- CRUD操作
- 事务管理
- 复杂查询
- 性能优化

**示例**:
```go
// ✅ 正确的DAO方法
// GetByID 根据ID查询用户
func (db *UserDB) GetByID(ctx context.Context, id int64) (*data.User, error) {
    var user data.User
    err := db.DB.WithContext(ctx).
        Where("id = ?", id).
        Where("is_del = ?", consts.IsDelNo).
        First(&user).Error

    if err != nil {
        return nil, err
    }
    return &user, nil
}
```

---

### framework/03-http-api.mdr
**适用**: `httpapi/**/*.go`, `controller/**/*.go`

**内容**:
- 路由组织
- 控制器模式
- 请求/响应处理
- 中间件集成
- API版本控制

**示例**:
```go
// httpapi/user.go - 路由定义
func userRouter(router ghttp.Router) {
    group := router.Group("/api/user")
    {
        group.HandleFunc("post", "/create", controller.CreateUser)
        group.HandleFunc("get", "/list", controller.ListUser)
    }
}

// controller/user/create.go - 控制器
func CreateUser(ctx context.Context, req ghttp.Request) ghttp.Response {
    var request zbreq.CreateUserRequest
    return controller.Ret(ctx, req, &request, func() (any, error) {
        return page.UserService.Create(ctx, request)
    })
}
```

---

### biz/01-business-logic.mdr
**适用**: `model/page/**/*.go`, `script/**/*.go`

**内容**:
- 服务层架构
- 业务逻辑结构
- 控制器接口设计
- 领域驱动设计
- 服务组合
- 缓存策略

---

### biz/02-domain-models.mdr
**适用**: `model/data/**/*.go`, `library/types/**/*.go`

**内容**:
- 数据模型分类
- 模型转换（DTO）
- 枚举类型
- JSON处理
- 数据验证
- 数据脱敏

---

## 实际应用场景

### 场景1：创建新的API接口

**需求**: 创建一个获取用户列表的API

**AI提问**:
```
帮我创建一个获取用户列表的API，路径是 /api/user/list
```

**自动应用的规则**:
```
✅ base/01-project-structure.mdr      # 始终应用
✅ language/01-go-standards.mdr       # 匹配 **/*.go
✅ language/02-logging.mdr            # 匹配 **/*.go
✅ framework/03-http-api.mdr          # 匹配 httpapi/*.go, controller/*.go
✅ biz/01-business-logic.mdr          # 匹配 model/page/**/*.go
```

**生成的代码**会自动遵循：
- 三层架构：httpapi → controller → page
- 统一响应格式
- 正确的日志记录
- 规范的注释

---

### 场景2：编辑数据库操作

**文件**: `model/dao/user/user_db.go`

**自动应用的规则**:
```
✅ base/01-project-structure.mdr      # 始终应用
✅ language/01-go-standards.mdr       # 匹配 **/*.go
✅ language/02-logging.mdr            # 匹配 **/*.go
✅ framework/02-gorm-database.mdr     # 匹配 model/dao/**/*.go
```

**AI会遵循**：
- DAO方法命名规范
- WithContext传递上下文
- 错误处理和日志
- 使用常量而非硬编码

---

### 场景3：编写业务逻辑

**文件**: `model/page/payment/service.go`

**自动应用的规则**:
```
✅ base/01-project-structure.mdr      # 始终应用
✅ language/01-go-standards.mdr       # 匹配 **/*.go
✅ language/02-logging.mdr            # 匹配 **/*.go
✅ biz/01-business-logic.mdr          # 匹配 model/page/**/*.go
```

**AI会遵循**：
- 服务层架构模式
- 业务逻辑封装
- 事务处理规范
- 缓存策略

---

## 最佳实践

### 1. 定期更新规则文件

当团队约定新的编码规范时，及时更新规则：

```bash
# 编辑规则文件
vi .comate/rules/language/01-go-standards.mdr

# 提交到Git
git add .comate/rules/
git commit -m "更新Go编码规范：添加泛型使用指南"
git push
```

### 2. 团队协作

**Code Review时引用规则**:
```
这段代码的命名不符合规范，请参考：
.comate/rules/language/01-go-standards.mdr 的命名约定部分
```

**新成员培训**:
```
新同学请先阅读：.comate/rules/GUIDE.md
```

### 3. 规则文件编写技巧

**✅ 好的规则示例**:
```markdown
## 函数命名规范

函数名使用驼峰命名法：
- 导出函数：首字母大写，如 `CreateUser`
- 私有函数：首字母小写，如 `validateUser`

示例：
```go
// ✅ 正确
func CreateUser(ctx context.Context) error { }

// ❌ 错误
func create_user(ctx context.Context) error { }
```
```

**❌ 避免的写法**:
```markdown
函数要写注释，代码要简洁。
```
（太模糊，AI难以理解）

### 4. 验证规则是否生效

**测试方法**:
```
请生成一个数据库查询函数，查询用户表

# 检查生成的代码是否：
- 使用了DAO层模式
- 包含错误日志
- 使用WithContext传递上下文
```

### 5. 手动引用规则

当需要特别强调某个规则时：

```
请按照 framework/01-gdp2-basics.mdr 
中的GDP2初始化流程创建一个新的服务
```

---

## 常见问题

### Q1: 规则文件必须使用 .mdr 后缀吗？

**A**: 是的，`.mdr` 是 Markdown Rule 的缩写，AI助手通过此后缀识别规则文件。

---

### Q2: 如何知道AI是否读取了我的规则？

**A**: 您可以：
1. 在规则中添加独特的命名约定
2. 请AI生成代码时，观察是否遵循这些约定
3. 直接询问AI："当前项目的控制器编写规范是什么？"

---

### Q3: 规则文件中可以包含代码示例吗？

**A**: 强烈建议包含！代码示例让AI更容易理解规则的实际应用。

---

### Q4: 不同团队成员的规则文件不一致怎么办？

**A**: 通过Git进行版本控制：
```bash
# 拉取最新规则
git pull origin main
```

---

### Q5: 规则文件太多，AI会全部读取吗？

**A**: AI会智能选择：
- 根据当前文件路径匹配相关规则
- 优先加载 `alwaysApply: true` 的规则
- 按优先级加载必要的规则文件

---

### Q6: Glob模式不够精确怎么办？

**当前问题**:
```yaml
globs: model/dao/*.go    # 只匹配 model/dao/xxx.go
```

**实际目录**:
```
model/dao/user/user_db.go     ❌ 不匹配！
```

**建议修改**:
```yaml
globs: model/dao/**/*.go      # 递归匹配所有子目录
```

---

## 参考资源

- [GDP2框架文档](http://gdp.baidu-int.com/)
- [GORM文档](https://gorm.io/zh_CN/)
- [Go官方代码审查建议](https://github.com/golang/go/wiki/CodeReviewComments)

---

## 规则体系总结

### 核心价值

✅ **标准化**: 团队代码风格统一  
✅ **效率提升**: AI生成的代码更符合项目规范  
✅ **知识传承**: 新成员快速了解项目规范  
✅ **质量保证**: 减少Code Review中的规范性问题

### 使用流程

```
1. 了解规则体系 → 阅读本指南
2. 查找适用规则 → 使用索引快速定位
3. 开始编码 → AI自动遵循规则
4. 持续优化 → 定期更新规则文件
```

---

**开始使用规则文件，让AI成为您团队编码规范的忠实执行者！** 🚀

---

*维护团队：AI-Anchor开发团队*  
*如有问题或建议，欢迎提出！*
```
#### 2.2 项目整体架构和通用规范(base)
```
---
description: ai-anchor项目结构和架构指南
globs: 
alwaysApply: true
---

# ai-anchor项目结构指南

这是一个基于GDP2框架构建的Go语言ai-anchor服务。项目采用分层架构，职责分离清晰。

## 核心架构

主入口点是 [main.go](mdc:main.go)，使用GDP2框架初始化应用程序。

### 框架和依赖
- **框架**: GDP2 (百度内部Go开发平台)
- **Go版本**: 1.23.0 (最低1.14)
- **HTTP框架**: 基于Gin的ghttp
- **数据库**: MySQL with GORM
- **缓存**: Redis
- **配置**: 环境特定的TOML配置文件

### 目录结构

```
├── bootstrap/          # 应用程序初始化和启动
├── controller/         # HTTP请求处理器和业务逻辑
├── httpapi/           # HTTP API路由定义
├── model/             # 数据访问层
│   ├── dao/           # 数据库访问对象
│   ├── data/          # 数据模型和结构
│   └── page/          # 业务逻辑和服务层
├── library/           # 共享工具和通用代码
├── script/            # 后台脚本和定时任务
├── middleware/        # HTTP中间件
├── conf/              # 配置文件
└── test/              # 测试文件
```

### 配置管理
- **开发环境**: `conf/` 目录
- **测试环境**: `conf_test/` 目录  
- **生产环境**: `conf_online/` 目录
- **沙盒环境**: `conf_sandbox/` 目录

### 关键组件

1. **Bootstrap** ([bootstrap/bootstrap.go](mdc:bootstrap/bootstrap.go)): 应用程序初始化，组件设置
2. **HTTP API** ([httpapi/router.go](mdc:httpapi/router.go)): 路由定义和中间件
3. **控制器**: `controller/` 目录中的业务逻辑处理器
4. **数据访问**: `model/dao/` 目录中的DAO模式
5. **业务逻辑**: `model/page/` 目录中的服务层

### 构建和部署
- **Makefile**: 使用 `make all`、`make compile`、`make test` 进行构建自动化
- **Docker**: 使用 [Dockerfile](mdc:Dockerfile) 进行容器化部署
- **CI/CD**: [ci.yml](mdc:ci.yml) 中的GitHub Actions工作流

### 开发标准
- 必须为所有代码编写注释
- 遵循百度Go编码标准
- 使用适当的错误处理和日志记录
- 为新功能包含单元测试
- 代码必须正确格式化

### 环境设置
```bash
# 开发环境
go run main.go -conf conf/app.toml

# 测试环境  
go run main.go -conf conf_test/app.toml

# 生产环境
go run main.go -conf conf_online/app.toml
```
```
#### 2.3 业务逻辑和领域模型规范(biz)
```
---
description: 业务逻辑和服务层模式
globs: model/page/**/*.go,script/**/*.go
alwaysApply: false
---

# 业务逻辑模式

本规范基于项目实际代码风格，适用于 `model/page/` 和 `script/` 目录。

## Page层架构

### 文件组织模式
每个功能域一个独立的文件或子目录，文件命名清晰表达功能：
```
model/page/
├── script_center/           # 剧本中心业务逻辑
│   ├── script_info.go       # 剧本信息处理
│   ├── script_list.go       # 剧本列表查询
│   └── script_create.go     # 剧本创建逻辑
├── live/                    # 直播相关业务
│   ├── live.go              # 主直播逻辑
│   ├── live_base_check.go   # 基础检查
│   └── room_page.go         # 房间管理
├── open_business/           # 开放业务
│   ├── video_page.go        # 视频处理
│   ├── figure_page.go       # 形象业务
│   └── process_video/       # 视频处理流程
└── scripts/                 # 定时脚本
```

### 代码规范模式

#### 基础函数模式
```go
// 函数式接口设计，直接处理zbreq/zbresp
func FunctionName(ctx context.Context, req zbreq.RequestType) (*zbresp.ResponseType, error) {
    // 直接业务逻辑处理
    result, err := dataLayer.GetData(ctx, req)
    if err != nil {
        return nil, err
    }

    resp := &zbresp.ResponseType{
        Data: result,
    }
    return resp, nil
}
```

#### 接口+实现模式
```go
// 接口定义
type ServiceName interface {
    Method1(ctx context.Context, req Request) (*Response, error)
    Method2(ctx context.Context, req Request) error
}

// 单例模式实现
var ServiceInstance ServiceName = &serviceImpl{}

type serviceImpl struct{}

func (*serviceImpl) Method1(ctx context.Context, req Request) (*Response, error) {
    // 实现逻辑
    return &Response{Data: "result"}, nil
}
```

## 数据流向模式

### 标准数据流
```
HTTP请求 → Controller层 → Page层（业务逻辑） → Data层 → DAO层 → 数据库
```

### 缓存策略
```go
// 常见的缓存-数据库策略
func GetDataWithCacheFirst(ctx context.Context, req Request) ([]Data, error) {
    // 1. 先查缓存
    data, err := cacheLayer.Get(ctx, cacheKey)
    if err == nil && len(data) > 0 {
        return data, nil
    }

    // 2. 缓存未命中，查询数据库
    data, err = dbLayer.Get(ctx, req)
    if err != nil {
        return nil, err
    }

    // 3. 异步更新缓存
    go func() {
        cacheLayer.Set(ctx, cacheKey, data, ttl)
    }()

    return data, nil
}
```

## 错误处理规范

### 错误包装
```go
func BusinessFunction(ctx context.Context, req Request) (*Response, error) {
    result, err := dataLayer.Process(req)
    if err != nil {
        // 使用项目标准的错误包装
        return nil, fmt.Errorf("业务处理失败: %w", err)
    }

    return &Response{Data: result}, nil
}
```

### 业务状态码
```go
// 使用统一的状态码定义
if validationErr := validateRequest(req); validationErr != nil {
    return nil, errno.NewErrModel(
        errno.NewErrStatus(errno.ErrInvalidParam),
        validationErr,
        "参数校验失败",
        errno.LevelNormal,
    )
}
```

## 最佳实践

1. **保持简洁**: 函数职责单一，避免过度抽象
2. **依赖清晰**: 明确的数据流向和依赖关系
3. **错误处理**: 统一的错误包装和状态码
4. **性能考虑**: 合理使用缓存和异步处理
5. **代码复用**: 公共逻辑封装到library或util

## 注意事项

- 遵循项目已有的import顺序和注释规范
- 保持与现有代码风格的一致性
- 为新功能添加适当的单元测试
- 确保业务逻辑的线程安全性
```
```
---
description: 领域模型和数据结构
globs: model/data/**/*.go,library/types/**/*.go
alwaysApply: false
---

# 领域模型和数据结构

## 数据模型分类

### 1. 数据库模型 (model/data/)
数据库表对应的实体模型

```go
// ScriptPage 剧本页数据模型
type ScriptPage struct {
    ID          uint64    `gorm:"primaryKey;column:id" json:"id"`
    ScriptID    int64     `gorm:"column:script_id" json:"script_id"`
    Index       int       `gorm:"column:index" json:"index"`
    SmartAnchor string    `gorm:"column:smart_anchor" json:"smart_anchor"`
    TTS         string    `gorm:"column:tts" json:"tts"`
    Goods       string    `gorm:"column:goods" json:"goods"`
    CreatedAt   time.Time `gorm:"column:ctime;autoCreateTime" json:"ctime"`
    UpdatedAt   time.Time `gorm:"column:mtime;autoUpdateTime" json:"mtime"`
    IsDel       int8      `gorm:"column:is_del" json:"is_del"`
}

// TableName 指定表名
func (ScriptPage) TableName() string {
    return TableNameScriptPage
}

// 表名常量定义
const (
    TableNameScriptPage = "script_page"
)
```

### 2. 请求模型 (library/zbreq/)
HTTP请求参数结构

```go
// CreateScriptRequest 创建剧本请求
type CreateScriptRequest struct {
    Title    string   `json:"title" binding:"required"`
    Content  string   `json:"content" binding:"required"`
    Tags     []string `json:"tags"`
    Category string   `json:"category"`
}

// 实现Param接口
func (r *CreateScriptRequest) FormatParam(ctx context.Context, req ghttp.Request) error {
    // 参数格式化和验证
    if len(r.Title) == 0 {
        return errors.New("title cannot be empty")
    }
    return nil
}
```

### 3. 响应模型 (library/zbresp/)
HTTP响应数据结构

```go
// ScriptResponse 剧本响应
type ScriptResponse struct {
    ID        int64     `json:"id"`
    Title     string    `json:"title"`
    Content   string    `json:"content"`
    Status    string    `json:"status"`
    CreatedAt time.Time `json:"created_at"`
}

// ScriptListResponse 剧本列表响应
type ScriptListResponse struct {
    List  []ScriptResponse `json:"list"`
    Total int64            `json:"total"`
}
```

### 4. 业务模型 (library/types/)
业务领域特定的类型定义

```go
// BusinessType 业务类型目录结构
library/types/
├── businesstype/    # 业务类型
├── scripttypes/     # 剧本类型
├── qatypes/         # 问答类型
└── roomtypes/       # 直播间类型
```

## 枚举类型定义

### 类型化枚举
```go
// StatusEnum 状态枚举
type StatusEnum int8

const (
    StatusPending StatusEnum = 0
    StatusRunning StatusEnum = 1
    StatusSuccess StatusEnum = 2
    StatusFailed  StatusEnum = 3
)

// String 实现Stringer接口
func (s StatusEnum) String() string {
    switch s {
    case StatusPending:
        return "pending"
    case StatusRunning:
        return "running"
    case StatusSuccess:
        return "success"
    case StatusFailed:
        return "failed"
    default:
        return "unknown"
    }
}
```

### 业务常量
```go
// 直播间状态
const (
    RoomStatusTodo     = -1 // 待直播
    RoomStatusReserve  = 0  // 预约
    RoomStatusIng      = 1  // 直播中
    RoomStatusClose    = 2  // 关闭
    RoomStatusPlayback = 3  // 回放
    RoomStatusOffline  = 20 // 下线
)

// 删除状态
type IsDelEnum int8

const (
    DelStatusDeleted IsDelEnum = 1 // 已删除
    DelStatusNormal  IsDelEnum = 0 // 未删除
)
```

## JSON处理

### 自定义JSON序列化
```go
// 时间格式化
type Time time.Time

func (t Time) MarshalJSON() ([]byte, error) {
    return []byte(fmt.Sprintf(`"%s"`, time.Time(t).Format("2006-01-02 15:04:05"))), nil
}

func (t *Time) UnmarshalJSON(data []byte) error {
    str := string(data[1 : len(data)-1])
    parsed, err := time.Parse("2006-01-02 15:04:05", str)
    if err != nil {
        return err
    }
    *t = Time(parsed)
    return nil
}
```

### JSON标签最佳实践
```go
type User struct {
    ID       int64  `json:"id"`                    // 基本序列化
    Username string `json:"username"`    
    Password string `json:"-"`                      // 不序列化
    Email    string `json:"email" binding:"email"` // 验证标签
}
```

## 数据验证

### 使用validator
```go
import "github.com/go-playground/validator/v10"

type CreateUserRequest struct {
    Username string `json:"username" binding:"required,min=3,max=20"`
    Email    string `json:"email" binding:"required,email"`
    Age      int    `json:"age" binding:"gte=0,lte=150"`
}

// 自定义验证器
func validateUsername(fl validator.FieldLevel) bool {
    username := fl.Field().String()
    // 自定义验证逻辑
    return len(username) >= 3
}
```
```
#### 2.4 GDP2和GORM框架使用指南(farmework)
```
---
description: GDP2框架基础使用指南
globs: bootstrap/**/*.go,main.go
alwaysApply: false
---

# GDP2框架使用指南

## 框架概述

GDP2是百度内部的Go开发平台，提供完整的Web应用开发能力。

### 核心组件
- **ghttp**: HTTP服务器和路由
- **mysql**: MySQL数据库客户端
- **redis**: Redis缓存客户端  
- **logit**: 日志组件
- **conf**: 配置管理
- **env**: 环境管理

## 应用初始化

### Bootstrap模式
```go
// main.go
package main

import (
    "flag"
    "log"
    
    _ "icode.baidu.com/baidu/gdp/automaxprocs"
    "icode.baidu.com/baidu/gdp/boot"
    "icode.baidu.com/baidu/gdp/env"
    
    "icode.baidu.com/baidu/huibo/ai-anchor/bootstrap"
)

var config = flag.String("conf", "./conf_test/app.toml", "app config file")

func main() {
    flag.Parse()
    boot.MustLoadAppConfig(*config)
    config, err := bootstrap.ParserAppConfig(*config)
    if err != nil {
        log.Fatalln(err)
    }
    env.Default = config.Env
    
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()
    
    bootstrap.MustInit(ctx, false)
    log.Fatalln("server exit:", bootstrap.Start(ctx, config))
}
```

### 组件初始化顺序
```go
// bootstrap/bootstrap.go
func MustInit(ctx context.Context, needPushLog bool) {
    initLoggers(ctx, needPushLog)      // 1. 日志
    initLogDefaultOpt()                // 2. 日志配置
    InitBrcc(ctx)                      // 3. 配置中心
    initRal(ctx)                       // 4. RAL
    loadServicer(ctx)                  // 5. Servicer
    initMySQL(ctx)                     // 6. MySQL
    initRedis(ctx)                     // 7. Redis
    initBES(ctx)                       // 8. ElasticSearch
    mustInitPassport()                 // 9. 认证
    util.PaymentInit()                 // 10. 支付
    page.MustInit()                    // 11. 业务初始化
    imetrics.MustInit()                // 12. 监控指标
}
```

## HTTP服务

### 路由定义
```go
// httpapi/router.go
func InitRouter(router ghttp.Router) ghttp.Router {
    // 注册中间件
    router.Use(gmetrics.Default().CollectHTTPServer())
    
    // 健康检查
    router.HandleFunc(http.MethodGet, "/alive/ping", alivePing)
    router.HandleFunc(http.MethodGet, "/alive/health", alive.Alive)
    
    // 业务路由分组
    scriptRouter(router)        // 剧本
    ttsRouter(router)          // TTS
    liveRouter(router)         // 开播
    
    return router
}

// 路由组定义
func scriptRouter(router ghttp.Router) {
    group := router.Group("/api/script")
    {
        group.HandleFunc("post", "/create", controller.CreateScript)
        group.HandleFunc("get", "/list", controller.ListScript)
        group.HandleFunc("post", "/update", controller.UpdateScript)
    }
}
```

### HandlerFunc标准模式
```go
// controller方法签名
func HandlerName(ctx context.Context, req ghttp.Request) ghttp.Response {
    // 处理逻辑
    return ghttp.NewJSONResponse(200, data)
}

// 使用controller.Ret简化
func CreateUser(ctx context.Context, req ghttp.Request) ghttp.Response {
    var request CreateUserRequest
    return controller.Ret(ctx, req, &request, func() (any, error) {
        // 业务逻辑
        return userService.Create(ctx, request)
    })
}
```

## 中间件

### 认证中间件
```go
// middleware/auth/simple_auth.go
func HuiBoAPIKey() ghttp.MiddleWareFunc {
    return func(ctx context.Context, w ghttp.Writer, req ghttp.Request, next ghttp.MiddleWareQueue) bool {
        sourceAk := req.QueryDefault("ak", "")
        if hbauth.NewOuter(sourceAk, "").CheckSk(resource.LoggerService, ctx, w, req) {
            return next.Next(ctx, w, req)
        }
        _ = ghttp.HTML403Response.WriteTo(w)
        return false
    }
}
```

### 使用中间件
```go
// 全局中间件
router.Use(middleware.RecoverMiddleware())
router.Use(middleware.LogMiddleware())

// 路由组中间件
authGroup := router.Group("/api/auth", auth.HuiBoAPIKey())
{
    authGroup.HandleFunc("post", "/user", controller.GetUser)
}
```

## 配置管理

### 配置文件结构
```toml
# conf/app.toml
[app]
name = "ai-anchor"
env = "test"
port = 8080

[mysql]
host = "127.0.0.1"
port = 3306
database = "ai_anchor"
username = "root"
password = "password"

[redis]
addr = "127.0.0.1:6379"
password = ""
db = 0
```

### 配置读取
```go
// bootstrap/config.go
type AppConfig struct {
    App   AppSection   `toml:"app"`
    MySQL MySQLSection `toml:"mysql"`
    Redis RedisSection `toml:"redis"`
}

func ParserAppConfig(configPath string) (*AppConfig, error) {
    var config AppConfig
    if err := conf.ParseFile(configPath, &config); err != nil {
        return nil, err
    }
    return &config, nil
}
```

## 数据库连接

### MySQL初始化
```go
func initMySQL(ctx context.Context) {
    // 主数据库
    resource.MySQLClientHuiBo = mysql.NewClient("huibo_db")
    if resource.MySQLClientHuiBo == nil {
        log.Fatal("failed to init mysql client")
    }
}
```

### Redis初始化
```go
func initRedis(ctx context.Context) {
    resource.RedisClient = redis.NewClient("main_redis")
    if resource.RedisClient == nil {
        log.Fatal("failed to init redis client")
    }
}
```

## 日志组件

### 日志初始化
```go
func initLoggers(ctx context.Context, needPushLog bool) {
    if needPushLog {
        // 生产环境：推送到日志中心
        resource.LoggerService = logit.NewLogger("ai-anchor")
    } else {
        // 开发环境：本地输出
        resource.LoggerService = logit.NewDevelopmentLogger()
    }
}
```

## 监控指标

### 指标注册
```go
// 注册HTTP Server指标
router.Use(gmetrics.Default().CollectHTTPServer())

// 注册metrics导出端点
gmetrics.Default().RegisterExporterTo(router)
// 访问: http://ip:port/metrics/process
//      http://ip:port/metrics/service
```

## 性能调优

### GOMAXPROCS自动设置
```go
import _ "icode.baidu.com/baidu/gdp/automaxprocs"
// 自动根据容器CPU配额设置GOMAXPROCS
```

### 连接池配置
```go
// MySQL连接池
[mysql.pool]
max_open_conns = 100
max_idle_conns = 10
conn_max_lifetime = "1h"

// Redis连接池  
[redis.pool]
pool_size = 100
min_idle_conns = 10
```
```
```
---
description: GORM数据库操作规范
globs: model/dao/**/*.go,model/db/**/*.go
alwaysApply: false
---

# GORM数据库操作规范

本规范基于项目现有代码风格和hbgorm库制定，兼容老的ddb逻辑。

## DB结构体命名规范

### 标准命名模式
```go
// 使用 GormDao 后缀命名数据库操作结构体
type ScriptPageGormDao struct {
    *hbgorm.BaseDB
}

func NewScriptPageGormDao(options ...hbgorm.Option) *ScriptPageGormDao {
    return &ScriptPageGormDao{BaseDB: hbgorm.NewBaseDB2(resource.HuiBoDB, options...)}
}
```

## 模型定义规范

### 基础模型结构
```go
type ModelName struct {
    ID        uint64    `gorm:"primaryKey;column:id" json:"id"`
    CreatedAt time.Time `gorm:"column:ctime;autoCreateTime" json:"ctime"`
    UpdatedAt time.Time `gorm:"column:mtime;autoUpdateTime" json:"mtime"`
    IsDel     int8      `gorm:"column:is_del" json:"is_del"` // 软删除标记
}
```

### GORM标签说明
- `gorm:"column:field_name"`: 指定数据库列名
- `gorm:"primaryKey"`: 主键标识
- `gorm:"index"`: 索引字段
- `gorm:"autoCreateTime"`: 自动创建时间
- `gorm:"autoUpdateTime"`: 自动更新时间
- `json:"field_name"`: JSON序列化名称

## CRUD操作规范

### 1. 创建记录
```go
// Create 创建记录（兼容数组参数）
func (db *ModelNameGormDao) Create(ctx context.Context, entities []ModelName) error {
    err := hbgorm.Create(ctx, db.GetDB(), entities)
    return err  // 直接返回错误，由调用方处理
}
```

### 2. 查询操作（简化的GORM风格）

#### 条件查询单条记录
```go
// GetByID 根据ID查询单条记录
func (db *ModelNameGormDao) GetByID(ctx context.Context, id uint64) (*ModelName, error) {
    var result ModelName
    err := db.GetDB().WithContext(ctx).
        Where("id = ?", id).
        Where("is_del = ?", consts.DelStatusNormal).
        First(&result).Error
    return &result, hberr.WrapSingle(err)
}
```

#### 条件查询多条记录
```go
// ListByCondition 条件查询列表
func (db *ModelNameGormDao) ListByCondition(ctx context.Context, column string, value interface{}) ([]ModelName, error) {
    var results []ModelName
    err := db.GetDB().WithContext(ctx).
        Where(column+" = ?", value).
        Where("is_del = ?", consts.DelStatusNormal).
        Find(&results).Error
    return results, hberr.WrapSingle(err)
}

// ListWithMultiCondition 多条件查询
func (db *ModelNameGormDao) ListWithMultiCondition(ctx context.Context, conditions map[string]interface{}) ([]ModelName, error) {
    query := db.GetDB().WithContext(ctx).Where("is_del = ?", consts.DelStatusNormal)
    for key, value := range conditions {
        query = query.Where(key+" = ?", value)
    }
    
    var results []ModelName
    err := query.Find(&results).Error
    return results, hberr.WrapSingle(err)
}
```

#### 复杂查询示例（参考现有实现）
```go
// GetOrderByTPOrderID 根据第三方订单ID获取订单
func (db *HuiBoOrderGormDao) GetOrderByTPOrderID(ctx context.Context, tpOrderID string) (*HuiBoOrder, error) {
    var result HuiBoOrder
    err := db.GetDB().WithContext(ctx).
        Where("order_id = ?", tpOrderID).
        First(&result).Error
    return &result, hberr.WrapSingle(err)
}

// ListNotLiveByAnchorID 根据主播ID查询非直播状态记录
func (db *ScriptReserveRoomGormDao) ListNotLiveByAnchorID(ctx context.Context, anchorID int64) ([]*ScriptReserveRoom, error) {
    var res []*ScriptReserveRoom
    err := db.GetDB().WithContext(ctx).Model(&ScriptReserveRoom{}).
        Where("anchor_id=? and script_status in (?)", anchorID, liveconsts.GetNotLiveScriptStatus()).
        Find(&res).Error
    return res, err
}
```

### 3. 更新操作（简化版）

#### 结构体条件更新
```go
// Update 更新记录（结构体条件）
func (db *ModelNameGormDao) Update(ctx context.Context, where ModelName, data ModelName) error {
    err := hbgorm.Update(ctx, db.GetDB(), &where, data)
    return err  // 直接返回错误
}
```

#### 原生GORM更新
```go
// UpdateByID 根据ID更新指定字段
func (db *ModelNameGormDao) UpdateByID(ctx context.Context, id uint64, updates map[string]interface{}) error {
    err := db.GetDB().WithContext(ctx).
        Model(&ModelName{}).
        Where("id = ?", id).
        Updates(updates).Error
    return err
}
```

#### 回调处理示例（参考现有实现）
```go
// PayCallback 支付回调处理
func (db *HuiBoOrderGormDao) PayCallback(ctx context.Context, payInfo CoinPayCallbackInfo) error {
    where := HuiBoOrder{OrderID: payInfo.TpOrderID}
    data := HuiBoOrder{
        OrderStatus: payInfo.OrderStatus,
        PaymentTime: payInfo.PayTime,
        BDOrderID:   payInfo.BDOrderID,
        BDUserID:    payInfo.BDUserID,
    }
    err := hbgorm.Update(ctx, db.GetDB(), &where, data)
    return err
}
```

## 兼容性规范

### 新表新代码
- 所有新表必须使用GORM实现
- GORM DAO结构体使用`GormDao`后缀
- 使用简化版的CRUD操作模式

### 兼容现有代码
- 保留原有ddb代码，确保向后兼容
- 新增功能优先使用GORM，逐步替换
- 同一模块可以同时存在ddb和gorm实现

### 迁移指导
```go
// 旧的ddb风格（保持兼容）
type OldStyleDB struct {
    *ddb.BaseDB
}

// 新的GORM风格（推荐新代码使用）
type NewStyleGormDao struct {
    *hbgorm.BaseDB
}
```

## 最佳实践

1. **错误处理**: 使用`hberr.WrapSingle(err)`包装错误
2. **事务处理**: 复杂的业务操作使用事务确保一致性
3. **性能优化**: 使用预加载、索引等优化查询性能
4. **代码复用**: 公共查询条件封装为scopes或函数

## 注意事项

- 保持与现有代码风格的一致性
- 优先使用简化版本的GORM操作
- 确保错误处理的完整性
- 新代码必须包含适当的注释
```
```
---
description: HTTP API参数校验规范和控制器结构
globs: httpapi/**/*.go,controller/**/*.go,library/zbreq/**/*.go,library/zbresp/**/*.go
alwaysApply: false
---

# HTTP API

## 请求参数校验

### 1. 枚举值校验
- 必须使用常量定义枚举值
- 校验时使用常量而非硬编码值
- 错误信息应明确说明允许的值

```go
// 正确示例
if param.ScriptType != consts.ScriptTypeContentLiveClue && 
   param.ScriptType != consts.ScriptTypeContentLiveECommerce {
    return errno.WrapSimpleErr(errno.ParamErrCode, 
        errors.New("script_type must be ScriptTypeContentLiveClue(8) or ScriptTypeContentLiveECommerce(9)"))
}

// 错误示例 - 使用硬编码值
if param.ScriptType != 8 && param.ScriptType != 9 {
    return errors.New("invalid script_type")
}
```

### 2. 基础类型校验
- 数字类型检查零值
- 字符串检查空值
- 数组/切片检查长度

```go
// 数字类型校验
if f.JobID <= 0 {
    return hberr.WrapCommonParam("任务ID不能为空")
}

// 字符串校验
if param.Name == "" {
    return hberr.WrapCommonParam("当前主播与脚本不匹配，请刷新页面")
}

// 数组校验
if len(f.Operator) == 0 {
    return hberr.WrapCommonParam("操作人不能为空")
}
```

### 3. 复合校验
- 多个字段关联校验
- 业务规则校验

```go
// 复合校验示例
if param.StartTime.After(param.EndTime) {
    return errno.WrapSimpleErr(errno.ParamErrCode, 
        errors.New("start_time must be before end_time"))
}
```

## 错误处理
- 使用项目定义的错误码
- 错误信息应清晰明确
- 包含必要的上下文信息

```go
// 使用项目错误码
return errno.WrapSimpleErr(errno.ParamErrCode, errors.New(common.ErrMsgMap[errno.ParamErrCode]))

// 自定义错误信息
return errno.WrapSimpleErr(errno.ParamErrCode, 
    errors.New("invalid script_type, must be 8 or 9"))
```

## API路由组织

### 路由结构
路由在 [httpapi/router.go](mdc:httpapi/router.go) 中按功能分组：

```go
// 按功能分组的路由
scriptRouter(router)           // 剧本
ttsRouter(router)             // TTS
liveRouter(router)            // 开播
openapiRouter(router)         // 对外API
auditRouter(router)           // 送审回调
dataRouter(router)            // 数据接口
```

### 路由组模式
```go
func exampleRouter(router ghttp.Router) {
    group := router.Group("/api/example")
    {
        group.HandleFunc("post", "/create", controller.Create)
        group.HandleFunc("get", "/list", controller.List)
        group.HandleFunc("post", "/update", controller.Update)
        group.HandleFunc("post", "/delete", controller.Delete)
    }
}
```

## 控制器模式

### 基础控制器结构
```go
type ExampleController struct {
    controller.BaseController
}

// 标准处理器模式
func (c *ExampleController) HandleRequest(ctx context.Context, req ghttp.Request) ghttp.Response {
    var request RequestStruct
    return controller.Ret(ctx, req, &request, func() (any, error) {
        // 业务逻辑实现
        return businessLogic(ctx, request)
    })
}
```

### 控制器接口模式
```go
type ExampleInterface interface {
    Create(ctx context.Context, req ghttp.Request) ghttp.Response
    List(ctx context.Context, req ghttp.Request) ghttp.Response
    Update(ctx context.Context, req ghttp.Request) ghttp.Response
    Delete(ctx context.Context, req ghttp.Request) ghttp.Response
}

var (
    Example ExampleInterface = new(exampleImpl)
)
```

## 请求/响应模式

### 请求处理
```go
func (c *Controller) Create(ctx context.Context, req ghttp.Request) ghttp.Response {
    var request CreateRequest
    return controller.Ret(ctx, req, &request, func() (any, error) {
        // 参数验证自动进行
        return result, nil
    })
}
```

### 响应结构
```go
type CommonResp struct {
    Errno   int    `json:"errno"`
    Errmsg  string `json:"errmsg"`
    Data    any    `json:"data"`
    Logid   string `json:"logid"`
    LocalIP string `json:"local_ip"`
}
```

## 中间件集成

### 标准中间件
```go
// 指标收集
router.Use(gmetrics.Default().CollectHTTPServer())

// 健康检查
router.HandleFunc(http.MethodGet, "/alive/ping", alivePing)

// 内部IP中间件
pprof.RegisterPProf(router, ghttp.NewInternalIPMiddleWareFunc())
```

## API版本控制

### 版本策略
```go
// V1 API
v1Group := router.Group("/api/v1/example")
{
    v1Group.HandleFunc("post", "/create", v1Controller.Create)
}

// V2 API改进
v2Group := router.Group("/api/v2/example")
{
    v2Group.HandleFunc("post", "/create", v2Controller.Create)
}
```

## API文档示例
```go
// 剧本相关接口
// POST /api/script/create - 创建剧本
// POST /api/script/list - 获取剧本列表
// POST /api/script/update - 更新剧本
func scriptRouter(router ghttp.Router) {
    scriptGroup := router.Group("/api/script")
    {
        scriptGroup.HandleFunc("post", "/create", scriptController.Create)
        scriptGroup.HandleFunc("post", "/list", scriptController.List)
        scriptGroup.HandleFunc("post", "/update", scriptController.Update)
    }
}
```

## 安全考虑

### 身份验证和授权
```go
// 检查访问密钥和业务代码
if !checkAKAndBusiness(ctx, req, request.BusinessCode) {
    return nil, errno.WrapReplaceMsg(errno.ParamDecodeErrCode, "您无权使用该business")
}
```
```
#### 2.5 Go语言编码标准和日志规范(**language**)
```
---
description: 统一Go语言编码标准和风格规范
globs: **/*.go
alwaysApply: false
---

# Go语言编码标准和风格规范

## 基本规范

### 包声明和导入顺序
```go
/*
 * Copyright(C) 2024 Baidu Inc. All Rights Reserved.
 * Author: name (email@baidu.com)
 * Date: 2024/01/01
 * File: filename.go
 */

package packagename

import (
    // 1. 标准库
    "context"
    "errors"
    "fmt"
    
    // 2. 第三方库
    "github.com/spf13/cast"
    "github.com/google/uuid"
    
    // 3. GDP框架
    "icode.baidu.com/baidu/gdp/ghttp"
    "icode.baidu.com/baidu/gdp/logit"
    
    // 4. 百度内部库
    "icode.baidu.com/baidu/huibo/library/hbutil"
    
    // 5. 项目内部
    "icode.baidu.com/baidu/huibo/ai-anchor/library/common"
)
```

### 命名约定

#### 变量命名
- 使用驼峰命名法
- 缩写词保持大写或小写统一: `userID` 而不是 `userId` 
- 布尔值使用 `is`、`has`、`can` 等前缀

#### 常量命名
- 使用大驼峰或全大写加下划线
- 相关常量分组定义

```go
const (
    StatusPending = "pending"
    StatusSuccess = "success"
    StatusFailed  = "failed"
)
```

#### 函数命名
- 导出函数首字母大写
- 私有函数首字母小写
- 使用动词开头: `GetUser`, `CreateOrder`, `ValidateInput`

## 注释规范

### 函数注释
```go
// GetUserByID 根据用户ID获取用户信息
func GetUserByID(ctx context.Context, userID int64) (*User, error) {
    // 实现
}
```

### 结构体注释
```go
// User 用户信息结构体
type User struct {
    ID       int64  `json:"id"`       // 用户ID
    Username string `json:"username"` // 用户名
    Email    string `json:"email"`    // 邮箱地址
}
```

### 必需标准
- **注释**: 所有代码必须有注释（强制要求）
- **格式化**: 使用 `go fmt` 或推荐工具: https://github.com/fsgo/go_fmt
- **命名规范**: 使用清晰、描述性的名称，遵循Go约定

## 类型定义

### 结构体
```go
// User 用户信息结构体
type User struct {
    ID        uint64    `json:"id" gorm:"primaryKey;column:id"`
    Username  string    `json:"username" gorm:"column:username"`
    Email     string    `json:"email" gorm:"column:email"`
    CreatedAt time.Time `json:"created_at" gorm:"column:ctime;autoCreateTime"`
    UpdatedAt time.Time `json:"updated_at" gorm:"column:mtime;autoUpdateTime"`
    IsDel     int8      `json:"is_del" gorm:"column:is_del"` // 软删除标记
}
```

### 接口定义
```go
// UserService 用户服务接口
type UserService interface {
    GetByID(ctx context.Context, id uint64) (*User, error)
    Create(ctx context.Context, user *User) error
    Update(ctx context.Context, user *User) error
    Delete(ctx context.Context, id uint64) error
}
```

### 类型别名和自定义类型
```go
// CallType 调用类型
type CallType int8

const (
    CallTypeIPPort CallType = 1 // IP:PORT 调用
    CallTypeBNS    CallType = 2 // BNS 调用
)

// IsDelEnum 删除状态枚举
type IsDelEnum int8

const (
    DelStatusDeleted IsDelEnum = 1 // 已删除
    DelStatusNormal  IsDelEnum = 0 // 未删除
)
```

## 函数和方法

### 函数命名和注释
```go
// GetUserByID 根据用户ID获取用户信息
func GetUserByID(ctx context.Context, userID uint64) (*User, error) {
    // 参数验证
    if userID == 0 {
        return nil, errors.New("invalid user ID")
    }
    
    // 业务逻辑
    user, err := fetchUserFromDB(ctx, userID)
    if err != nil {
        return nil, fmt.Errorf("failed to fetch user: %w", err)
    }
    
    return user, nil
}
```

### 可变参数
```go
// MergeList 合并多个列表
func MergeList[K any, L []K](lists ...L) L {
    res := make([]K, 0)
    for _, list := range lists {
        res = append(res, list...)
    }
    return res
}
```

## 泛型使用

### 泛型函数
```go
// FindIndex 在切片中查找元素索引
func FindIndex[T comparable](slice []T, target T) int {
    for i, v := range slice {
        if v == target {
            return i
        }
    }
    return -1
}

// Map 映射切片元素
func Map[T, U any](slice []T, fn func(T) U) []U {
    result := make([]U, len(slice))
    for i, v := range slice {
        result[i] = fn(v)
    }
    return result
}
```

### 泛型类型
```go
// Result 通用结果类型
type Result[T any] struct {
    Data  T
    Error error
}

// Option 可选值类型
type Option[T any] struct {
    value *T
}

func (o Option[T]) IsSome() bool {
    return o.value != nil
}
```

## 错误处理和废弃API规范

### 错误常量使用准则
- **禁止使用未定义的错误常量** - 所有错误常量必须来自项目定义的errno包
- **优先使用标准错误码** - 使用项目定义的标准错误码

```go
// ✅ 推荐使用标准的错误常量
errno.ParamErrCode       // 参数错误(10)
errno.ParamDecodeErrCode // 参数解析错误(11)

// ❌ 严禁使用未定义常量
errno.ErrParamInvalid    // 未定义常量（不存在）
```

### 废弃API使用规范
- **禁止使用标记为Deprecated的API** - 所有被`// Deprecated:`注释标记的接口/函数禁止在新代码中使用

```go
// ❌ 避免使用废弃API
errno.WrapErrWithLevel() // Deprecated: use hberr.WrapErrWithLevel

// ✅ 使用替代API  
hberr.WrapErrWithLevel() // 推荐的替代方案
```

### 错误码与业务场景匹配
错误码应与业务场景相匹配，确保语义清晰：
- 参数错误：`ParamErrCode` (code=10)
- 数据库错误：`DBErrCode` (code=2000)  
- Redis错误：`RedisErrCode` (code=3000)

### 代码审查检查项
在代码审查中必须验证：
1. 所有错误常量是否在errno包中有明确定义
2. 是否使用了标记为Deprecated的API
3. 错误码是否与业务场景匹配

### 错误返回
```go
// 总是检查错误
result, err := someOperation()
if err != nil {
    return nil, fmt.Errorf("operation failed: %w", err)
}

// 错误包装提供上下文
if err != nil {
    return nil, fmt.Errorf("failed to process data: %w", err)
}
```

### 错误定义
```go
var (
    ErrNotFound     = errors.New("resource not found")
    ErrInvalidInput = errors.New("invalid input")
)
```

## 性能优化

### 预分配切片
```go
// 好的做法：预分配容量
items := make([]Item, 0, expectedSize)

// 避免：频繁扩容
items := []Item{}
```

### 字符串拼接
```go
// 使用strings.Builder进行高效拼接
var builder strings.Builder
builder.Grow(estimatedSize) // 预分配
for _, s := range parts {
    builder.WriteString(s)
}
result := builder.String()
```
```
```
---
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

**2. 安全日志层 (logsafe)**
```go
import "icode.baidu.com/baidu/huibo/ai-anchor/library/logsafe"

// 自动过滤敏感信息的业务日志
logsafe.Notice(ctx, "业务操作完成", logit.String("operation", "create"))
logsafe.Warning(ctx, "操作警告", logit.Int("error_code", 1001))
```

**3. 服务日志层 (LoggerService)**
```go
import "icode.baidu.com/baidu/huibo/ai-anchor/library/resource"

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
logsafe.Notice(ctx, "operation completed")

// Warning 级别 - 可恢复异常
// 使用场景：数据库操作失败、外部接口异常、业务规则警告
resource.LoggerService.Warning(ctx, "database operation failed")

// Error 级别 - 严重错误
// 使用场景：系统故障、数据不一致、业务流程中断
resource.LoggerService.Error(ctx, "system error occurred")

// Fatal 级别 - 致命错误（慎用）
// 使用场景：系统无法继续运行、关键组件初始化失败
logsafe.Fatal(ctx, "critical system failure")
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
        logsafe.Warning(ctx, "slow database query detected",
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
    logsafe.Warning(ctx, "missing business code")
    return errno.WrapParamErr(errno.ErrParamErr, "business_code lost")
}

// 业务逻辑执行错误
if _, err := scriptDAO.Insert(ctx, params); err != nil {
    resource.LoggerService.Warning(ctx, "insert operation failed", logit.String("err", err.Error()))
    return zbresp.Ret(ctx, req, err, nil)
}
```

### 5. 外部服务调用场景
```go
// 调用前记录
logsafe.Notice(ctx, "calling external service",
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
    logsafe.Notice(ctx, "external service call success",
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
logsafe.Notice(ctx, "request processing",
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
logsafe.Warning(ctx, "database operation failed",
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
// logsafe会自动过滤敏感信息（BDUSS等token）
// 示例：msgFilter函数自动清理敏感数据
logsafe.Notice(ctx, "user operation") // 内部自动过滤
```

### 日志组件选择指南
```go
// 1. 业务逻辑使用logsafe - 自动安全过滤
logsafe.Notice(ctx, "业务操作", logit.String("action", "create"))

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
logsafe.Notice(ctx, "operation completed",
    logit.String("operation", "create"),
    logit.Int64("user_id", userID),
)

// ❌ 避免：字符串拼接
logsafe.Notice(ctx, fmt.Sprintf("operation create completed for user %d", userID))
```

**请求链路追踪**
```go
// 始终包含请求ID
logid := logit.FindLogIDField(ctx).Value()
logsafe.Notice(ctx, "processing request", logit.String("logid", logid))
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
logsafe.Notice(ctx, "user login", logit.String("token", userToken))

// ✅ 安全：使用logsafe自动过滤或手动脱敏
logsafe.Notice(ctx, "user login") // logsafe会自动过滤BDUSS等
```

**过度日志记录**
```go
// ❌ 避免：循环内大量日志
for i := 0; i < 1000; i++ {
    logsafe.Notice(ctx, "processing item", logit.Int("index", i))
}

// ✅ 推荐：批量处理记录
logsafe.Notice(ctx, "batch processing started", logit.Int("total", 1000))
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
logsafe.Notice(ctx, "operation completed",
    logit.Int64("duration_ms", duration.Milliseconds()),
)
```

### 🛡️ 安全注意事项

- **logsafe已内置敏感信息过滤**（BDUSS、token等）
- **生产环境避免Trace级别**，仅用于开发和调试
- **Error级别谨慎使用**，避免过多噪音影响监控
- **Fatal级别会导致程序退出**，仅在系统无法继续时使用
```
## 三、使用示例：简单项目开发（2d -> 0.5h）


#### 3.1 需求概览
需求描述：需要搭建一个运营管理平台页面，对慧播星页面的学习资源进行基础的资源管理

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=86c5aff9d0e54c359808d46a2ef7ad57&docGuid=CoK90Y1twBZT6u "")
#### 3.1 技术详设
接口文档：CRUD四个接口

![接口文档](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ddbd3ba68ed14d0d84317ac415e8a26d&docGuid=CoK90Y1twBZT6u "接口文档")
数据库表设计:course、course_column表

```
CREATE TABLE `course` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `url` text NOT NULL COMMENT '课程链接',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '状态 1生效 0失效',
  `cuser` varchar(64) NOT NULL DEFAULT '' COMMENT '创建人',
  `muser` varchar(64) NOT NULL DEFAULT '' COMMENT '修改人',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=196 DEFAULT CHARSET=utf8 COMMENT='学习中心课程表';

CREATE TABLE `course_column` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `course_id` bigint(20) NOT NULL COMMENT '课程ID,关联course.id',
  `category` varchar(255) NOT NULL DEFAULT '0' COMMENT '栏目',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '状态 1生效 0失效',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8833 DEFAULT CHARSET=utf8 COMMENT='学习中心课程表栏目表';
```


#### 3.3 简单需求全自动生成代码
mcp准备：添加iapi、mysql等mcp

1. 生成dao层代码

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9743f0ebfb5d4c3786d64dc8638e83b9&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=034d3c9170b5400994543b2f2dceb212&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aec0db2c699043ac8b65f864bf6061ef&docGuid=CoK90Y1twBZT6u "")


2. 生成第一个接口代码，并测试可用性

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4113f50e2a0e4c44915da019517d82bb&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b36380db7ddb42699da444cf84edb29b&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=50c09512eed1489b80ef483b7acae86d&docGuid=CoK90Y1twBZT6u "")


测试

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=db237ba434eb4fdd993967b268a759df&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f15787fab5247eb8811b4fe7ddc4d04&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3766fffd11424346b33a95735431aea4&docGuid=CoK90Y1twBZT6u "")


3. 生成其余接口代码、并测试

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=da204311ab604a1fa3e0f7e6839bab20&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b5286df690b54b03b8fd5fe37a4f1cee&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d253a38b5fa3402bbfd96cc8c4a04b8e&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d044506d315c485c85c5f3dd9d425847&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ea3ca993c5d4d91ae8b99d82e0d5586&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01ff09ecc2b24ae1a7c72e8e2baa1e36&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=52cb5af333e847a9b7811de02276ec6c&docGuid=CoK90Y1twBZT6u "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=015b90205a10497998f4d3bfb73c286d&docGuid=CoK90Y1twBZT6u "")


## 四、组内rules经验分享
|**组员**|**业务场景**|**语言**|**心得**|
|-|-|-|-|
|徐杰|zulu实现多表CRUD接口快速生成|go|如果想要生成的接口最终可用。需要定好整个项目的rules项目的文件夹分层rules定义好controller、page、dao层代码的rules定义好日志打印、错误处理、类型定义等的rules接口文档需要描述准确，有功能、必传、非必传等一些信息数据库表和字段的描述清楚，comment定义好需要枚举的字段常量、多张表之间的关联关系等|
|王利顺|对抓取工具的页面进行国际化的改造|python|对于交互页面这种会定义大量展示元素与提示的代码，AI可以在协助开发功能的同时完成国际化的适配，减少大量的人工开发工作。对于AI coding，需要大量明确且适当的rules加以限制和指定，最好还要加上范本示例，否则还需要人工进行改造适配，会减少AI coding的收益。|
|安小艳|以ubc埋点规范实现前端事件的埋点上报|js|1、效率提升：从手动埋点到ai自动理解功能分析事件进行埋点，效率大幅提升2、结果可用性的rules心得：1、清晰的项目结构，2、可用的模板，3、示例场景覆盖，4、埋点的业务功能描述清晰|
|宋天凡|根据历史任务逻辑，指定输入和升级的算法，生成v2版本|python/shell|对于结构清晰的目录和任务，指定明确的rules后，可以大幅减少二次开发的成本|
|王安怡|电商数据后端服务，用于日常监控、数据提效、对外API服务等。|python|在电商数据后端服务中引入规则（Rules）体系后，我最大的感受是开发方式从“写逻辑”转变成了“定义行为”。规则让监控逻辑、告警条件、数据校验、接口规范等能力实现了可配置化，而不是写死在代码里，从而降低了后期维护成本，也提升了迭代速度。更重要的是，规则成为统一的技术语言，让 AI 在协助生成代码和补充逻辑时能够遵循一致的标准，减少歧义和返工，使系统具备可扩展、更易协作、更智能的特征。|
|王晓阳|在多人协同中，通过提供新的input、output、ak、sk等配置，能够基于基线模型的文件结构，快速生成一个新的创意优选模型相关文件。|python/shell|对于人工修改耗时长、规则清晰的脚本，通过多步精心调试的Rules，确实能提高脚本复用和修改效率，且准确率很高。第一次调试Rules有点费时间，通用性不高。|

## 五、总结
#### 5.1 可以解决的问题
1. **编码规范统一化**：依托base、biz、framework、language四大模块的基础rules（如项目结构规范01-project-structure.mdr、Go语言标准01-go-standards.mdr等），明确了从项目架构到日志输出的全链路标准，解决了开发人员编码风格不一致的问题，减少了因规范差异导致的代码评审返工，提升了代码可维护性。
2. **研发效率显著提升**：在简单场景（如慧播星运营平台的资源管理需求）中，通过rules支持的全自动代码生成（涵盖DAO层CRUD、HTTP接口实现），将原本需2人天（2pd）的开发任务压缩至1小时；复杂场景下，rules提供的框架使用指南（如GDP2、GORM）和业务逻辑模板，也降低了重复编码工作量，缩短了功能开发周期。
3. **新手上手成本降低**：rules体系将项目层次（如model/dao、接口设计规范）与编码规范（如SQL表设计、日志格式）以结构化文档（GUIDE.md、各模块mdr文件）形式固化，新手可通过查阅rules快速理解项目架构、掌握开发标准，减少了对老员工的依赖，加速了团队人员融入。

#### 5.2 一些rules使用经验
1. **rules设计需“分层聚焦”**：本次实践将rules按“基础架构（base）-业务逻辑（biz）-框架工具（framework）-语言标准（language）”分层，既保证了通用规范的统一性（如Go语言标准适用于所有Go项目），又能针对业务场景灵活扩展（如biz模块的领域模型规范适配具体业务），避免了rules“一刀切”或“过于零散”的问题。
2. **自动化生成需“衔接场景”**：代码自动生成并非“无差别生成”，而是基于明确的场景输入（如数据库表结构、接口文档定义）——例如慧播星项目中，先通过SQL定义course、course_column表结构，再结合CRUD接口需求，即可精准生成DAO层代码，这一过程需确保rules与实际开发流程（需求-设计-编码-测试）深度衔接，才能最大化自动化价值。
3. **经验沉淀需“全员参与”**：基于不同业务场景，rules规则需要通过“实践-总结-共享”循环放大。后续慧播星组内需建立常态化的经验分享机制，将个体经验转化为团队通用rules，进一步丰富rules体系。

#### 5.3 ai-anchor后续优化方向
1. **扩展rules覆盖场景**：当前rules在简单CRUD、基础框架使用场景覆盖较全，但在复杂业务逻辑（如分布式事务、高并发接口）、跨团队协作（如前后端联调规范、接口版本管理）场景的支持仍需完善，需结合更多业务案例补充相应rules文档。
2. **强化自动化工具能力**：现有代码生成依赖手动触发与基础配置，后续可探索将rules与IDE插件、CI/CD流程集成，实现“需求文档导入-自动生成代码-自动测试-部署”的全链路自动化，进一步减少人工干预。
3. **建立rules迭代机制**：随着技术栈更新（如Go版本升级、框架替换）或业务复杂度提升，需定期Review现有rules（如检查02-gorm-database.mdr是否适配最新GORM版本），淘汰过时规范、补充新增场景，确保rules体系的时效性与实用性。





# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
