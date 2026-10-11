---
title: "硬编码漏洞修复与凭证托管"
description: "硬编码修复有四个步骤：凭证配置 → 代码修复 → 用户确认 → 凭证托管。"
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\code-security\\references\\credential_hosting.md"
---
# 硬编码漏洞修复与凭证托管

硬编码修复有四个步骤：凭证配置 → 代码修复 → 用户确认 → 凭证托管。

## 步骤一：打开凭证配置网页

输出可点击的链接让用户打开凭证托管助手网页，网页 URL 格式及输出示例如下：
```
请点击以下链接打开凭证托管助手，配置凭证信息：

[打开凭证托管助手](//command:simpleBrowser.api.open?https%3A%2F%2Fcomate-sec-test.baidu-int.com%2Fapp%2Fcredential%3FchatID%3D${COMATE_SESSION_ID}%26comateUID%3D<COMATE_UID>%26version%3D2.9.1%26repo%3D<REPO>%26ideType%3D${COMATE_IDE_NAME})

配置完成后请在网页中点击「生成代码」按钮，我会自动检测到配置完成并继续执行修复。
```

其中：
- `COMATE_UID` 为 `${COMATE_USERNAME}` 的 MD5 字符串的前 12 位，使用 `python3 -c "import hashlib; print(hashlib.md5('${COMATE_USERNAME}'.encode()).hexdigest()[:12])"` 计算
- `REPO` 是代码库标识，可以从项目目录的 git remote 获取（如 `baidu/scan/cnap-test`），如果没有 git 信息则使用项目目录名

要使用实际构造的字符串来替换上述的 url 参数，url 中的%26不要解码，避免 & 符号影响 markdown 链接。

## 步骤二：等待凭证配置完成

打开网页后，立即执行轮询脚本等待用户配置，使用 `--output` 将结果保存到临时目录：

```bash
python3 scripts/credential_poll.py --chat-id ${COMATE_SESSION_ID} --username ${COMATE_USERNAME} --output <临时目录>/poll_result.json
```

`<临时目录>` 使用与 `scan_result.json` 同一目录（即 `.tmp/<项目名>_<哈希>/`）。

该脚本通过 WebSocket 连接服务端，等待用户在网页完成配置并点击「生成代码」。收到数据后输出到标准输出并保存到 `--output` 指定的文件。配置数据包含以下关键字段：

- `data.files`：待修复文件列表（含 vulList 和 extra.secret 信息）
- `data.credentials`：凭证名值对列表
- `data.deployment`：托管平台信息（platform、platformName）
- `data.repo`：代码库语言和框架信息
- `data.succMsg`：托管成功提示信息
- `data.errorMsg`：托管失败提示信息
- `chatUUID`：此次会话 ID

## 步骤三：修复硬编码代码

收到凭证配置数据后，在本地直接修复硬编码漏洞，不调用后端修复服务。修复流程参考 `references/vul_repair_sensitive.md` 文档中的详细说明。

修复输入数据来自 `poll_result.json` 文件（由步骤二保存），其中 `data.files`、`data.repo`、`data.deployment` 包含了修复所需的全部信息。

修复流程：
1. 读取 `references/vul_repair_sensitive.md` 中的修复规则
2. 遍历 `data.files` 中的每个文件，根据文件类型（代码文件/配置文件）、语言（`data.repo.language`）、框架（`data.repo.framework`）和平台（`data.deployment.platform`）确定修复策略
3. 根据每个漏洞的 `extra.secret.credentialName`、`extra.secret.start`、`extra.secret.end` 定位敏感信息并替换为环境变量读取方式
4. 如果 `data.deployment.platform` 为 4，还需引入 keyless-sdk（参考 `references/vul_repair_sensitive.md` 的「引入SDK」章节）

## 步骤四：凭证托管

代码修复完成后，提示用户确认修复结果，然后提供托管选项：

```
代码修复已完成，请 Review 修复后的代码。确认无误后，选择「托管凭证」将凭证托管到平台。
1. 托管凭证 - 将凭证托管到 {platformName} 平台
2. 跳过托管 - 仅完成代码修复，不托管凭证
```

用户选择托管后执行：

```bash
python3 scripts/credential_hosting.py --poll-result <poll_result.json路径> --username ${COMATE_USERNAME}
```

脚本自动从 `poll_result.json` 中提取 `chatUUID`、`deployment.platformName`、`data.credentials`，无需手动传递这些参数。

托管完成后，从 `poll_result.json` 中读取 `data.succMsg` 展示给用户。如果失败，展示 `data.errorMsg`。

托管成功后，通过 Questions 组件提示用户进行历史 commit 清理。`succMsg` 中包含清理平台地址，需要从中提取链接并突出展示。提示格式：

```
凭证托管已完成。由于历史 commit 中可能仍残留硬编码凭证，建议立即清理 Git 历史记录，防止凭证泄露。

{succMsg}

请确认：
1. 已完成清理 - 我已清理历史 commit，继续后续流程
2. 稍后处理 - 跳过清理，继续后续流程
```

用户选择后继续执行复测扫描。

## 复测扫描

托管成功后，自动执行一次复测扫描（流程与「漏洞扫描」章节一致），对比修复前后的硬编码漏洞数量，向用户说明修复效果。复测结果同样需要静默执行数据上报。展示格式：

```
托管完成，正在执行复测扫描验证修复效果...

**复测结果**：修复前共 N 个硬编码漏洞，修复后剩余 M 个，本次修复 X 个漏洞。
```

如果复测仍存在未修复的硬编码漏洞，展示剩余漏洞列表（格式同漏洞报告），并提示用户可以选择继续修复或忽略。

## 清理临时文件

复测完成后，清理临时文件：`python3 -c "import shutil; shutil.rmtree('<临时目录绝对路径>')"` 删除该项目的临时目录（即 `.tmp/<项目名>_<哈希>/` 整个目录）。然后进入单元测试阶段（流程见「单元测试」章节）。
