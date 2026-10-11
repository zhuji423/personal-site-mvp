---
title: "为三个仓库生成整体架构梳理并写成本地 Markdown"
description: "Rollout context: 用户在 /Users/zhujim4pro/code/baidu/qamate-strategy/apismart-code 下，先后询问了三个代码库的 Java 版本、pom.xml 是否相当于 Pyth"
date: "2026-05-05"
category: "项目架构文档"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-28T01-30-56-a7dN-qamate_itp_architecture_md.md"
---
thread_id: 019dd1b5-f746-7d13-8edf-f7233ead1693
updated_at: 2026-04-28T06:41:55+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/28/rollout-2026-04-28T09-30-56-019dd1b5-f746-7d13-8edf-f7233ead1693.jsonl
cwd: /Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code
git_branch: kirin_batowl

# 为三个仓库生成整体架构梳理并写成本地 Markdown

Rollout context: 用户在 `/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code` 下，先后询问了三个代码库的 Java 版本、`pom.xml` 是否相当于 Python 的 `requirements.txt`，最后要求“对这三个项目有整体性的了解”，并明确要“使用 mermeid 代码进行构造”，随后又要求“写成一个md文件在本地”。

## Task 1: 快速识别三个仓库的 Java 版本

Outcome: success

Preference signals:

- 用户要求“快速回答” -> 这类仓库/配置类问题最好先给结论，再补证据，不要先长篇铺垫。
- 用户用中文持续提问，并且后续追问 Java 框架整体认识 -> 未来类似场景应默认用中文解释，并尽量面向 Java 初学者/ Python 背景做类比。

Key steps:

- 先在当前目录和相邻父目录里找 `pom.xml`、`build.gradle`、`.java-version` 等构建/版本文件。
- 进一步定位到三个 Git 仓库：`baidu/qamate-server/core`、`baidu/qamate-server/apiExecutor`、`baidu/inner-os/itp`。
- 从各自 `pom.xml` 中确认 Java 版本：`core=21`、`apiExecutor=17`、`itp` 主要是 `1.8`，且 `itest-executor/stargater` 单独用了 `1.6`。

Reusable knowledge:

- 这组仓库的 Java 版本分层明显：新服务是 Java 17/21，老平台主要是 Java 8，局部还能看到 Java 6。
- 对这类多仓库版本识别，优先看 `pom.xml` 里的 `<java.version>`、`maven.compiler.source/target`，再看是否有 `.java-version` / Gradle toolchain。

References:

- `baidu/qamate-server/core/pom.xml`: `<java.version>21</java.version>`
- `baidu/qamate-server/apiExecutor/pom.xml`: `<maven.compiler.source>17</maven.compiler.source>`, `<maven.compiler.target>17</maven.compiler.target>`, `<java.version>17</java.version>`
- `baidu/inner-os/itp/itp/itp-intelli/pom.xml`: `<java.version>1.8</java.version>`
- `baidu/inner-os/itp/itest-executor/stargater/pom.xml`: `<maven.compiler.source>1.6</maven.compiler.source>`, `<maven.compiler.target>1.6</maven.compiler.target>`

## Task 2: 解释 pom.xml 与 Python requirements.txt 的关系

Outcome: success

Preference signals:

- 用户说“我只有python 的基础，对于java 了解不多” -> 后续解释应主动做 Python 类比，降低 Java/Maven 术语门槛。
- 用户问“pom 这几个文件的相当于 requirements.txt 吗” -> 说明他希望先建立整体框架感，而不是只看单个字段。

Key steps:

- 解释 `pom.xml` 不只是依赖列表，而是包含项目身份、Java 版本、依赖、构建规则、多模块管理。
- 用 `requirements.txt`、`pyproject.toml`、`pip install`、Python 版本、包版本等做类比。

Reusable knowledge:

- 对 Python 背景用户，`pom.xml` 最接近“依赖管理 + 构建配置 + 多模块配置”的组合体，而不是单纯的 `requirements.txt`。
- Spring Boot 项目可用 `Controller -> Service -> Mapper` 解释成 route / business logic / DAO。

References:

- 类比总结：`requirements.txt` ≈ `pom.xml` 的 `<dependencies>` 部分；整个 `pom.xml` 更像 `pyproject.toml + requirements.txt + build script` 的组合。

## Task 3: 生成三个项目的整体架构分析并输出 Markdown 文件

Outcome: success

Preference signals:

- 用户明确要求：“我希望对这三个项目有整体性的了解” -> 后续应按项目级别给全局视图，而不是只回答局部字段。
- 用户要求：“使用mermeid 代码进行构造” -> 未来类似任务应默认补 Mermaid 架构图。
- 用户进一步要求：“写成一个md文件在本地” -> 说明最终交付应落地为本地文档文件，而不是只在聊天里解释。

Key steps:

- 扫描三个仓库的目录结构、启动类、Controller/Service/Mapper 以及配置文件。
- 识别出 `core`、`apiExecutor`、`itp` 三者的职责分工与调用关系。
- 结合 `application.yml` / `application-dev.yml` 等配置，整理技术栈、数据流向、核心配置项。
- 用 `apply_patch` 新建 `ARCHITECTURE_OVERVIEW.md`，只新增文档不改代码。

Failures and how to do differently:

- 过程中配置文件里出现了明文 token、密码和内部服务地址；最终写文档时没有展开这些敏感值，只保留配置类别。以后遇到类似仓库分析，应默认避免在输出里复写敏感配置。
- 一开始尝试从父目录混扫多个仓库，后面才明确到三个主仓库并按模块梳理；类似多仓库场景应尽早确认每个仓库边界，减少无效扫描。

Reusable knowledge:

- `core` 是 Spring Boot 3.2 / Java 21 的业务中台，主入口在 `com.baidu.qamate.core.App`，并启用了 `Feign`、`Scheduling`、`TransactionManagement`、`MethodCache`、`Retry`。
- `apiExecutor` 是 Spring Boot 3.5 / Java 17 的执行器，主入口在 `com.baidu.qamate.server.App`，启用了 `Feign`、`Scheduling`、`MapperScan`、`ServletComponentScan`。
- `apiExecutor` 的 `QAMateCoreClient` 通过 Feign 回调 `core`，典型接口包括调试结果回传、case info 拉取、环境参数查询、执行开始通知、step report 回传、脚本详情查询。
- `apiExecutor` 的 `TaskController` 以 `/task/case/submit`、`/task/case/debugByJson`、`/task/case/cancel` 为主入口，先转成 `RunnerTask` 再交给 `TaskSubmitService`。
- `itp` 是老平台，多模块且老技术栈混杂：`itp-web`（大量 Action）、`itp-dataio`、`itp-tasktracker`、`itp-core`、`itp-intelli`、`lts/*`、`itest-executor`。
- `itp` 里 `itp-web`/`itp-tasktracker` 这类模块是传统 Java Web / 执行平台风格，和 `core`/`apiExecutor` 的 Spring Boot 风格明显不同。
- 本地生成的文档文件名是 `ARCHITECTURE_OVERVIEW.md`，位于当前工作区根目录。

References:

- 新建文件：`ARCHITECTURE_OVERVIEW.md`
- `core` 启动类：`baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/App.java`
- `apiExecutor` 启动类：`baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/App.java`
- `apiExecutor` Feign 客户端：`baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/common/conf/feign/client/QAMateCoreClient.java`
- `apiExecutor` 任务入口：`baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/controller/TaskController.java`
- 最终落地文件路径：`/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code/ARCHITECTURE_OVERVIEW.md`
