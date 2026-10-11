---
title: "知识库文档操作（Ku Operator）"
description: "操作百度内部知识库（ku.baidu-int.com）系统的文档。支持文档内容查询、知识库目录查询、新建文档、移动文档等操作。当用户需要在知识库中创建文档、查看文档内容、浏览目录结构、或移动文档位置时使用此 Skill。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\SKILL.md"
name: "ku-operator"
---

# 知识库文档操作（Ku Operator）

操作百度内部知识库系统的文档，支持文档 CRUD 操作。所有操作通过同目录下的 CLI 脚本执行。

## 前置依赖

- **Skill 依赖 `get-ugate-token`**：认证通过 get-ugate-token skill 自动获取个人身份 token
- **环境变量 `COMATE_USERNAME`**：当前用户的百度用户名，认证和创建/移动文档时自动读取
- **Python 依赖**：`requests` 库
- **执行方式**：在 Skill 目录下使用 **`python3`** 直接运行脚本，不要 import 调用
- **`create-doc`** 目前不支持 上传图片/附件 功能，禁止执行 上传图片/附件 的操作


## Skill 路径

- skill 所在的路径是：${COMATE_SKILL_DIR}，
- 执行脚本或是查看文档请先打开 skill 所在路径，导出环境变量，然后再执行脚本
- 示例：cd ${COMATE_SKILL_DIR} && COMATE_USERNAME=${COMATE_USERNAME} && python3 scripts/ku_operator.py args

## 认证说明

本 skill 依赖 `get-ugate-token` skill 进行个人身份认证。调用时自动获取 ugate token：
- 若本地已有有效的 token 缓存文件，直接使用，无需用户介入
- 若 token 不存在或已过期，需要前往 https://uuap.baidu.com/agent/token 页面给 Comate 开通 ugate 授权
- 开通后，token 永久有效，无需重复配置

API 返回 401/403 时，脚本会提示用户重新触发授权流程并以退出码 2 退出。

## 知识库 URL 与 ID 解析（重要）

知识库链接有两种格式：

### 格式一：完整路径链接

```
https://ku.baidu-int.com/knowledge/{spaceGuid}/{groupGuid}/{repoGuid}/{docGuid}
```

| URL 段 | 含义 | 说明 |
|--------|------|------|
| `spaceGuid` | 空间 ID | 一般不需要使用 |
| `groupGuid` | 分组 ID | 一般不需要使用 |
| `repoGuid` | **知识库 ID** | 用于 `--repo-guid` 参数 |
| `docGuid` | **文档 ID** | 用于 `--doc-id` 参数，URL 最后一段 |

**路径段数判断链接类型：**
- **4 段**（含 docGuid）→ 文档链接，可直接 `query-content` 读取
- **3 段**（仅到 repoGuid）→ 知识库链接，需先 `query-repo` 查询目录

### 格式二：短链接

```
https://ku.baidu-int.com/d/{docId}
```

这是文档的短链接格式，`/d/` 后面的部分即为 **文档 ID**（doc-id）。例如 `https://ku.baidu-int.com/d/bLKhnZmWDDm7JH` 中 `bLKhnZmWDDm7JH` 就是 doc-id。

短链接**始终是文档链接**，可直接使用 `query-content --url <短链接>` 或 `query-content --doc-id <docId>` 读取。

### 识别知识库链接

以下域名的 URL 均为知识库链接，应使用本 skill 处理：
- `ku.baidu-int.com/knowledge/...`（完整路径链接）
- `ku.baidu-int.com/d/...`（短链接）

## 重要概念：文档即目录

知识库中**文档和目录是同一个概念**——任何文档都可以拥有子文档。读取文档后应通过 `query-repo --parent-doc-guid <该文档ID>` 检查是否有子文档，按需加载以提供完整结果。

## 写入目标知识库确定策略

当用户要求"写入知识库"但**未指定目标**时，按优先级：

1. **当前会话中提及的知识库**：从 URL 解析 `repoGuid`/`docGuid`
2. **项目关联的默认知识库**：读取 `knowledge/ku_doc/ku_doc_usage.md`（可能不存在）
3. **询问用户**：请用户提供目标知识库文档的 URL

**写入范围约束：**
- 文档链接（4 段路径或短链接 `/d/{docId}`）→ 只能在该文档及其子目录下创建
- 知识库链接（3 段）→ 可在整个知识库范围内创建
- 用户明确指定其他位置时，以用户指令为准

## CLI 子命令一览

统一入口：`python3 scripts/ku_operator.py <子命令> [参数]`

| 子命令 | 功能 | 必填参数 | 常用可选参数 |
|--------|------|----------|-------------|
| `query-content` | 查询文档内容（Markdown 输出） | `--doc-id` 或 `--url`（二选一） | `--save-assets-dir`, `--no-download-assets`, `--raw-json` |
| `query-repo` | 查询知识库目录（文本树形输出） | `--repo-guid` | `--parent-doc-guid`, `--page` |
| `create-doc` | 新建文档 | `--repo-guid` | `--title`, `--content-file`, `--parent-doc-guid` |
| `copy-doc` | 复制文档 | `--doc-id` | `--to-repo-guid`, `--to-parent-guid`, `--new-title` |
| `move-doc` | 移动文档 | `--doc-id` + `--to-repo-guid` | `--to-parent-guid` |
| `delete-doc` | 删除文档 | `--doc-id` | — |
| `query-comment` | 查询文档评论（格式化文本输出） | `--doc-id` | `--type`, `--page`, `--raw-json` |
| `query-user-info` | 查询当前用户信息及个人知识库 | — | — |
| `upload-attachment` | 上传附件到文档正文 | `--doc-id` + `--file` | `--no-insert`, `--view-type` |
| `query-flowchart` | 查询文档流程图数据 | `--doc-id` | `--flowchart-id`, `--output` |
| `query-recent-view` | 查询文档浏览记录（格式化文本输出） | `--doc-id` | `--begin-time`, `--end-time`, `--page`, `--raw-json` |
| `add-member` | 添加文档成员 | `--doc-id` + `--usernames` + `--role` | — |
| `update-member` | 更新文档成员角色 | `--doc-id` + `--username` + `--role` | — |
| `query-permission` | 查询用户文档权限 | `--doc-id` + `--usernames` | — |
| `change-scope` | 修改文档公开/私密范围 | `--doc-id` + `--scope` | — |

**关键用法说明：**
- `query-content` 默认自动下载远程图片/附件到 `./ku_assets/{doc_id}/`，并替换 Markdown 中的 URL。读取文档后注意 stderr 资源下载摘要，按需用 Read 工具查看已下载的图片。
- `create-doc` 使用 `--content-file` 时自动上传本地图片/附件到 BOS。**Markdown 中图片/附件引用必须使用绝对路径**。
- `query-user-info` 返回 `personalRepoGuid`（个人知识库 ID）和 `personalRepoUrl`。
- 创建者/操作者用户名自动从 `COMATE_USERNAME` 读取。

## API 详细文档

各子命令的详细参数、输出格式、使用示例见 `references/` 目录：

| 文档 | 内容 |
|------|------|
| `references/query_content.md` | 文档内容查询详细说明 |
| `references/query_repo.md` | 知识库目录查询详细说明 |
| `references/create_doc.md` | 新建文档详细说明 |
| `references/copy_doc.md` | 复制文档详细说明 |
| `references/move_doc.md` | 移动文档详细说明 |
| `references/delete_doc.md` | 删除文档详细说明 |
| `references/query_comment.md` | 查询文档评论详细说明 |
| `references/query_user_info.md` | 用户信息查询详细说明 |
| `references/upload_attachment.md` | 上传附件到文档正文 |
| `references/query_flowchart.md` | 查询文档流程图数据 |
| `references/query_recent_view.md` | 查询文档浏览记录 |
| `references/add_member.md` | 添加文档成员 |
| `references/update_member.md` | 更新文档成员角色 |
| `references/query_permission.md` | 查询用户文档权限 |
| `references/change_scope.md` | 修改文档公开/私密范围 |

## 错误处理

**可自行修复（重试）：** 参数缺失、ID 格式错误（repoGuid/docGuid 搞反）、页码超出范围

**需告知用户（不重试）：**
- 认证失败（401/403）→ 提示用户前往 https://uuap.baidu.com/agent/token 页面给 Comate 开通 ugate 授权
- 文档不存在（404）→ 告知用户检查文档是否已被删除
- 无操作权限 → 告知用户联系知识库管理员
- 服务端错误（5xx）→ 告知用户稍后再试
