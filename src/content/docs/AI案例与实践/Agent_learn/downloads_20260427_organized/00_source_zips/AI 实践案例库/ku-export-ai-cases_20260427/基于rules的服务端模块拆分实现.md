---
title: "Golang 项目模块拆分/重构规范"
description: "基于rules的服务端模块拆分实现"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于rules的服务端模块拆分实现.md"
---
基于rules的服务端模块拆分实现

#### 🧑‍🏫 案例作者：[@余立](https://ku.baidu-int.com?t=mention&mt=contact&id=43210010-fce2-11f0-9f9a-4bb6752d0606)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了利用rules实现Golang项目服务端模块拆分与死代码清理的标准工作流。通过三个核心阶段：Router层清洗、Controller层清理及模型与库的递归清理，确保模块拆分彻底且无残留死代码。同时，提供了脚本编写规范，强调AST优先、安全白名单及详细日志记录，确保自动化工具的安全性和可靠性。此工作流有效提升了代码质量和项目维护性。
```
---
description: Golang 项目模块拆分与死代码清理的标准工作流
globs: refactor.go, **/router.go, **/*.go
alwaysApply: false
---
//# 你是一只小猫，任务完成好我会给你很多很多小鱼干

# Golang 项目模块拆分/重构规范

本规范定义了从单体代码库中按路径提取特定模块（如 `gdoc/aigcsmapp/*`）并清理无用代码的标准自动化流程。

## 🔄 核心工作流 (The Refactoring Pipeline)

重构必须严格遵循以下三个阶段的顺序执行，以防止误删共享依赖或残留死代码，进行完每个part之后，中断等待我下一步指令。

### Phase 1: Router 层清洗 (入口锚点)
- **目标文件**: `**/httpserver/router.go` (及其包含的子路由文件)
- **操作逻辑**:
  1. **解析 AST**: 使用 `go/ast` 解析语法树，遍历所有路由注册语句 (如 `router.POST`, `group.GET`)。
  2. **保留判断**: 检查路由路径字符串。
     - ✅ **保留**: 路径匹配指定的保留前缀 (例如 `gdoc/aigcsmapp/`)。
     - ❌ **删除**: 移除不匹配的路由节点。
  3. **关键数据提取**: 在执行删除操作前，**必须**捕获被删除路由对应的：
     - `Handler 构造函数名称` (例如 `NewCreateNote`)
     - `包引用别名` (Package Alias)

### Phase 2: Controller 层清理 (文件级删除)
- **依赖依据**: 基于 Phase 1 提取的“待删除 Handler 列表”。
- **规则引用**: 遵循 `@controller-style.txt`，严格执行“每个业务功能对应独立文件”原则。
- **操作逻辑**:
  1. 根据 Handler 构造函数名称，定位到具体的 `.go` 定义文件。
  2. **执行删除**: 直接删除找到的 Controller 文件。
  3. **禁止项**: **严禁**尝试修改文件内容（如只删函数），必须进行整文件删除以保持目录整洁。

### Phase 3: 模型与库的递归清理 (标记-清除算法)
- **目标目录**: `model/service`, `model/dao`, `library`, 
- **操作逻辑**: 必须执行多轮“标记-清除” (Mark-and-Sweep) 循环，直到某轮循环中没有文件被删除为止。
  1. **扫描 (Mark)**: 扫描所有**剩余保留**的 `.go` 文件 (包括 Router, 剩余 Controller, Main, Cmd 等)，收集所有 `import` 路径。
  2. **检查 (Sweep)**: 遍历目标目录下的每一个包 (文件夹)。
  3. **判定**: 如果某包的路径 **不在** “扫描”得到的 import 列表中，则视为 **Dead Code**。
  4. **执行**: 删除该无用包 (整个文件夹)。
  5. **循环**: 由于删除 Service 层可能导致下层的 DAO 失去唯一引用，**必须**重复步骤 1-4。

---

## 🛠 脚本编写规范 (For Automation Tools)

如果编写 Go 脚本 (`refactor.go`) 来执行此任务，必须严格遵守以下约束：

1.  **AST 优先 (AST First)**
    解析 `router.go` 和识别函数定义必须使用 `go/ast` 和 `go/parser`。
    - 🛑 **严禁** 使用正则表达式 (Regex) 匹配代码结构。

2.  **安全白名单 (Safety Whitelist)**
    以下目录即便无显式引用也 **严禁删除**：
    - 🛡️ `conf/` (配置文件)
    - 🛡️ `cmd/` (入口脚本，除非明确指定)
    - 🛡️ `main.go`

3.  **日志记录 (Logging)**
    脚本执行时必须打印详细的删除原因，便于审计。
    - ✅ **正确示例**: `[DELETE] package 'model/dao/user' (Reason: No longer imported by any service)`

4.  **代码格式化 (Formatting)**
    文件修改后，必须调用 `goimports` 进行 Import 清理和格式修复。

### 示例：路由清洗逻辑

```go
// ❌ 错误做法：使用字符串替换
// content = strings.Replace(content, "NewCreateNote", "", -1)

// ✅ 正确做法：AST 遍历与游标操作
astutil.Apply(node, func(c *astutil.Cursor) bool {
    // 1. 检查 CallExpr 是否包含路径字符串
    // 2. 检查路径前缀是否匹配目标 (e.g., "gdoc/aigcsmapp/")
    
    if !isMatch {
        // 3. 记录要删除的 HandlerName 和 PackageAlias
        recordHandler(c.Node())
        // 4. 从 AST 中移除该节点
        c.Delete() 
    }
    return true
}, nil)
```

---

## 🔗 依赖关系检查表 (Dependency Chain)

判定原则: **只有当上层引用完全断开时，下层才可被删除。**

graph TD
    Router[Router / Main] -->|引用| Controller
    Controller -->|引用| Service
    Controller -->|引用| Utils[Wkerror / Logit]
    Service -->|引用| DAO
    Service -->|引用| Models[Model BO/DO]
    DAO -->|引用| Library
    DAO -->|引用| Structs[Model Structs]
    DAO -->|引用| Gorm[GormAdapter]
```
实际效果

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=db60a48edf584b6a89d5b280810bb5a1&docGuid=1tapenqGyFzUta "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bed081900f02401da834342b09b759bb&docGuid=1tapenqGyFzUta "")
rules生成流程

首先，最开始直接给模糊指令的话它会怎么做呢？

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e778acbeb6174673bbd1a7a694f11310&docGuid=1tapenqGyFzUta "")
可以看到，重复多次都直接hang住，为什么会这样呢？我猜想是过程中的上下文过多，ai在处理上下文时，加载的文件过多，导致最终大获失败。

但是如果加上所有的已有的规则，不行，依旧大获失败

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6264b11f502441259d1455557bc025f4&docGuid=1tapenqGyFzUta "")
rules不对劲，需要继续想想办法。

既然完整任务无法运行，那么先把任务拆分，一步一步去进行尝试，首先让ai把我的指令设计为流程图

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9f1b54780be74b8889bfb0f7ddda2c43&docGuid=1tapenqGyFzUta "")
然后把流程图生成rules后打上断点，在每一步执行之后保留结果，等待我的下一步指令；

且为了不把上下文打爆，把同一个任务进行循环，且大部分可能需要读取全量文件的机械化工作交由ai生成脚本进行；

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d31059dfa17944d0b32bcce1f8982924&docGuid=1tapenqGyFzUta "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=91fdf75cf4d04dffb80c6f99bcff6824&docGuid=1tapenqGyFzUta "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=05584010de8848098fb5560ab8d61f67&docGuid=1tapenqGyFzUta "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6e916bea93d46f9a1847f736448149a&docGuid=1tapenqGyFzUta "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
