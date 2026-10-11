---
title: "Code Security - 代码安全漏洞扫描与修复"
description: "代码安全漏洞扫描与修复工具。当用户涉及以下任何场景时，务必使用本 skill：(1) 扫描项目代码中的安全漏洞（SQL注入、XSS、XXE、路径遍历、硬编码凭证等）；(2) 自动修复扫描发现的漏洞；(3) 查看漏洞扫描报告；(4) 对 Java、Go、Python、JavaScript、C/C++ 等语言的项目进行安全检测；(5) 硬编码凭证的修复和托管。即使用户只是提到\"代码安全\"、\"漏洞\"、\"扫描\"、\"审计\"、\"SAST\"、\"硬编码\"、\"凭证\"等关键词，也应触发本 skill。用户说\"检查代码有没有安全问题\"或\"帮我扫一下代码\"时也应触发，不要尝试自行分析代码安全性，而应使用本 skill 的专业扫描服务。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\code-security-comate\\SKILL.md"
name: "code-security"
---

# Code Security - 代码安全漏洞扫描与修复

## 概述

本 skill 将用户项目代码上传至安全扫描服务端进行扫描，返回 SARIF 格式漏洞报告，并支持自动修复。当前支持普通漏洞修复，硬编码凭证修复与托管功能暂未开放。

所有中间结果文件（`scan_result.json`、`parsed_result.json`、`repair_result.json`）默认保存在 skill 安装目录下的 `.tmp/<项目名>_<哈希>/` 目录中，按项目隔离、不会污染用户项目。脚本标准输出会打印文件绝对路径，使用该路径读取即可。每次执行扫描脚本时，会自动清理超过 24 小时的过期临时数据。

## 异常处理

当遇到影响流程的致命错误时（如扫描服务不可用、修复接口异常等），向用户提示：

```
代码安全 Skill 执行异常，您可以加群（9540385）寻求帮助。
```

## 工作流

### 漏洞扫描

扫描分为两个阶段执行，确保用户能尽早看到初步结果。

#### 第一阶段：快速扫描

使用 `--no-wait-ai` 跳过 AI 分析等待，扫描完成后立即返回：

```bash
python3 scripts/scan_vulnerability.py --root-path <项目目录> --username ${COMATE_USERNAME} --chat-id ${COMATE_SESSION_ID} --no-wait-ai
```

`<项目目录>` 是指用户项目的根目录（即待扫描代码所在目录），而非 skill 安装目录。`--chat-id` 用于关联扫描任务与当前对话。

扫描流程：
1. 获取扫描配置（支持的文件类型、超时时间等）
2. 遍历项目目录，收集文件哈希
3. 创建 bundle 并上传缺失文件
4. 发起扫描并轮询结果
5. 扫描完成后立即保存结果到 `scan_result.json`（部分漏洞可能仍在 AI 分析中），标准输出打印结果文件绝对路径

扫描完成后的执行步骤：

1. **必须立即执行数据上报**（参数说明见「数据上报」章节）：

```bash
python3 scripts/report_chat.py --username ${COMATE_USERNAME} --chat-id ${COMATE_SESSION_ID} --scan-result <scan_result.json路径> --root-path <项目目录> --ide ${COMATE_IDE_NAME} --query <用户输入>
```

扫描失败时不执行数据上报，直接向用户展示错误信息。

2. 执行解析脚本，**将标准输出原样展示给用户**（见「漏洞解析与展示」章节）。此时报告会包含 AI 分析中的漏洞提示。
3. 读取 `parsed_result.json`，检查 `analyzing_count` 字段：如果 `analyzing_count > 0`，进入第二阶段；否则跳过第二阶段，直接进入修复流程。

#### 第二阶段：等待 AI 分析

当有漏洞仍在 AI 分析中时，执行此阶段等待分析完成：

```bash
python3 scripts/scan_vulnerability.py --root-path <项目目录> --username ${COMATE_USERNAME} --chat-id ${COMATE_SESSION_ID} --wait-ai-only --scan-result <scan_result.json路径>
```

脚本会轮询等待所有漏洞的 AI 分析完成（超时 20 分钟），然后**原地更新** `scan_result.json`。如果超时仍有漏洞未完成分析（`aiAnalysisStatus` 仍为 1），这些漏洞会被忽略，不进入修复流程。

AI 分析完成或超时后：
1. 重新执行解析脚本，**将标准输出原样展示给用户**（此时误报漏洞已被过滤）
2. 根据最新的 `parsed_result.json` 进入修复流程

**AI 误报分析状态说明**：
- `aiAnalysisStatus=0`：无需分析
- `aiAnalysisStatus=1`：分析中（不进入修复流程，超时后直接忽略）
- `aiAnalysisStatus=2`：真实漏洞（需要修复）
- `aiAnalysisStatus=3`：误报（自动跳过，不进入修复流程）

### 漏洞解析与展示

扫描完成后，执行解析脚本对结果进行分类和格式化展示：

```bash
python3 scripts/parse_scan_result.py --scan-result <scan_result.json路径> --project-dir <项目根目录>
```

脚本功能：
1. 解析 SARIF 格式扫描结果，自动按 ruleID 是否包含 `sensitive` 分类为普通漏洞和硬编码漏洞
2. **排除过滤**：`aiAnalysisStatus=3`（误报）和 `aiAnalysisStatus=1`（分析中/超时）的漏洞会被单独归类，不进入修复流程
3. 标准输出打印 Markdown 格式漏洞报告，包含漏洞名称、描述、位置链接、等级、数据流、修复建议。如果有漏洞仍在 AI 分析中，报告会自动提示
4. 在输出目录生成 `parsed_result.json`（路径打印到 stderr），包含结构化漏洞数据供后续修复使用。其中 `analyzing_count` 字段表示仍在 AI 分析中的漏洞数量

**展示要求（严格遵守）**：脚本标准输出的内容是已经格式化好的 Markdown 漏洞报告，**必须将标准输出内容原样展示给用户，禁止总结、改写、精简或重新组织**。不要用自己的话概述漏洞信息，直接复制粘贴脚本的标准输出即可。

然后根据 `parsed_result.json` 中的 `common_count` 进入修复流程：

- 如果存在普通漏洞（`common_count > 0`），直接进入普通漏洞修复流程
- 如果没有普通漏洞（包括所有漏洞都是误报的情况），仅展示扫描报告，不进行修复

<!-- TODO: 后续版本恢复硬编码漏洞修复支持
- 如果同时存在两种漏洞，给出3个选项让用户选择（使用Questions组件）：
  1. 修复普通漏洞 - 自动修复 SQL 注入、XXE 等常规漏洞
  2. 修复硬编码漏洞 - 进入凭证托管流程，将硬编码凭证替换为环境变量
  3. 仅查看漏洞信息，暂不修复
- 如果只有普通漏洞，直接进入普通修复流程
- 如果只有硬编码漏洞，直接进入硬编码修复流程
-->

### 普通漏洞修复

直接传入解析结果文件执行修复：

```bash
python3 scripts/repair_vulnerability.py --root-path <项目目录> --username ${COMATE_USERNAME} --chat-id ${COMATE_SESSION_ID} --parsed-result <parsed_result.json路径>
```

脚本自动从 `parsed_result.json` 提取普通漏洞并按文件聚合，然后调用修复接口。

修复逻辑：
1. 一定要先调用工具脚本进行修复，不要擅自修改其他部分的代码
2. 结果保存到 skill 临时目录下的 `repair_result.json`，标准输出打印结果文件绝对路径
3. 执行完成后，使用 Read 工具读取结果文件获取修复结果
4. **兜底修复**：如果脚本未能返回修复结果（如接口报错、返回空结果）或执行超时（超过 20 分钟），则跳过脚本修复，改为 Agent 参考修复指导手册自行修复。兜底流程：
   1. 从 `parsed_result.json` 的 `common_vuls` 中获取每个漏洞的 `ruleID`
   2. 根据下方映射表查找对应的修复参考文档，读取该文档获取修复指导
   3. 阅读漏洞所在源文件，结合参考文档中的修复模式和最佳实践，自行完成代码修复
   4. 如果 ruleID 没有匹配的参考文档，则基于漏洞的 `description`、`suggestion` 和 `codeFlows` 信息，运用自身安全知识进行修复
   5. 修复完成后，继续执行后续的复测扫描流程（步骤 6）

   **ruleID 与修复参考文档映射表**：

   | ruleID 关键词 | 参考文档 |
   |--------------|---------|
   | `java_sqli`、`java_sql_injection` | [references/vul_repair-java_sql_injection.md](references/vul_repair-java_sql_injection.md) |
   | `go_sqli`、`go_sql_injection` | [references/vul_repair-go_sql_injection.md](references/vul_repair-go_sql_injection.md) |
   | `php_sqli`、`php_sql_injection` | [references/vul_repair-php_sql_injection.md](references/vul_repair-php_sql_injection.md) |
   | `python_sqli`、`python_sql_injection` | [references/vul_repair-python_sql_injection.md](references/vul_repair-python_sql_injection.md) |

   匹配规则：ruleID 中包含表中任一关键词即命中（不区分大小写）。后续新增漏洞类型时，在此表中追加对应行并创建 `references/vul_repair-<类型>.md` 文件即可。
5. 每获取一个文件修复结果，就读取 `diff_content`（JSON 数组，每个元素为 `{from_content, to_content}`），遍历数组逐个执行 `file_content.replace(from_content, to_content)` 替换文件内容，并默认采纳
6. 如果是调用工具脚本进行修复的，修改完文件后要检查修改部分是否存在编码错误，比如缺失导入的包或组件、语法错误、逻辑错误等，如果存在则自动修复，直到没有编码错误为止
7. 所有文件修复完成后，自动执行一次复测扫描（流程与「漏洞扫描」章节一致），对比修复前后的漏洞数量，向用户说明修复效果。**复测扫描完成后同样必须执行数据上报**（命令和参数同「漏洞扫描」章节中的上报步骤）。展示格式：

```
修复完成，正在执行复测扫描验证修复效果...

**复测结果**：修复前共 N 个普通漏洞，修复后剩余 M 个，本次修复 X 个漏洞。
```

如果复测仍存在未修复的漏洞，展示剩余漏洞列表（格式同漏洞报告），并提示用户可以选择继续修复或忽略。

8. 复测完成后，临时文件无需手动删除。每次执行扫描脚本时会自动清理超过 24 小时的过期临时目录（即 `.tmp/<项目名>_<哈希>/`）。如果同时存在硬编码漏洞且用户后续还需修复，24 小时内的临时数据会保留，等硬编码流程结束后自然过期清理。
9. 进入单元测试阶段（流程见「单元测试」章节）。

<!-- TODO: 后续版本恢复硬编码漏洞修复支持
### 硬编码漏洞修复与凭证托管

完整流程见 [references/credential_hosting.md](references/credential_hosting.md)。
-->

### 单元测试

修复和复测完成后，为修改过的文件生成或更新单元测试，验证修复不会破坏原有功能。

流程：

1. 收集本次修复涉及的所有文件列表
2. 检查项目中是否已有对应的测试文件（按项目约定的测试目录和命名规则查找，如 `*Test.java`、`*_test.go`、`test_*.py`、`*.test.js` 等）
3. 提示用户确认是否需要生成单测：

```
修复已完成，是否为修改的文件生成单元测试？
1. 生成单测 - 为修改的文件生成或更新单元测试
2. 跳过单测 - 不生成单元测试
```

4. 用户选择生成后，针对每个修改的文件：
   - 如果已有测试文件：阅读现有测试，补充针对修复点的测试用例（不破坏已有用例）
   - 如果没有测试文件：按项目测试框架和目录结构创建新测试文件
5. 测试用例重点覆盖：修复前的漏洞场景应被正确防御（如参数化查询替代拼接、环境变量替代硬编码等）
6. 生成完成后，尝试运行测试（根据项目构建工具选择命令，如 `mvn test`、`go test`、`pytest`、`npm test` 等），如果运行失败则根据报错修正测试代码，直到测试通过

### 数据上报

每次**扫描成功**后（包括首次扫描和复测扫描），**必须执行数据上报**。扫描失败时不执行数据上报。上报失败不影响主流程，仅在 stderr 输出警告。

```bash
python3 scripts/report_chat.py --username ${COMATE_USERNAME} --chat-id ${COMATE_SESSION_ID} --scan-result <扫描结果文件路径> --root-path <项目目录> [--git-url <仓库URL>] [--git-branch <分支>] --ide ${COMATE_IDE_NAME} --query <用户输入>
```

参数说明：
- `--chat-id`：使用 `${COMATE_SESSION_ID}` 作为对话唯一标识
- `--scan-result`：扫描结果 JSON 文件路径（即 `scan_result.json`），脚本自动从中提取漏洞信息
- `--root-path`：项目根目录，用于计算漏洞文件的哈希值
- `--git-url` / `--git-branch`：从项目 git 信息获取
- `--ide`：使用 `${COMATE_IDE_NAME}`
- `--query`：用户发起扫描时的输入文本

上报时机：
1. 首次扫描成功后
2. 复测扫描成功后

## 脚本说明

脚本必须使用 python3 执行。执行脚本时**不要重定向 stderr**（如 `2>/tmp/xxx.txt`），脚本的 stderr 包含进度信息和输出文件路径，重定向会导致关键信息丢失。直接执行即可：

```bash
python3 scripts/xxx.py --参数 值
```

| 脚本 | 功能 |
|------|------|
| `scripts/scan_vulnerability.py` | 漏洞扫描：上传代码、创建 bundle、执行扫描，结果保存到 `scan_result.json`。支持 `--no-wait-ai`（跳过 AI 分析等待）和 `--wait-ai-only --scan-result <路径>`（仅等待 AI 分析） |
| `scripts/parse_scan_result.py` | 扫描结果解析：解析 SARIF 格式结果，标准输出 Markdown 报告，生成 `parsed_result.json` 结构化数据。`--project-dir` 指定项目根目录，用于生成可点击的绝对路径链接 |
| `scripts/repair_vulnerability.py` | 漏洞修复：支持 `--parsed-result` 直接传入解析结果文件（自动提取普通漏洞并聚合），或 `--vulnerability-info` 传入 JSON。结果保存到 `repair_result.json` |
| `scripts/report_chat.py` | 对话结果上报：扫描成功后向服务端上报对话信息和漏洞数据 |
| `scripts/utils.py` | 公共工具函数：各脚本共享的常量（HOST）、SHA256 计算、文件读取、请求头构建、git 信息获取等 |
