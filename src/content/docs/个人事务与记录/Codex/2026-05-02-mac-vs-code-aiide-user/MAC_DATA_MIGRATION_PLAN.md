---
title: "Mac 个人数据与开发环境迁移计划"
description: "把这台 Mac 上与个人使用、代码开发、VS Code、Codex/AI IDE 相关的数据，尽量完整地迁移到另一台电脑，并保证："
date: "2026-05-02"
category: "个人事务与记录"
source: "F:\\百度工作\\03_documents_keep\\Codex\\2026-05-02-mac-vs-code-aiide-user\\MAC_DATA_MIGRATION_PLAN.md"
---
# Mac 个人数据与开发环境迁移计划

## 1. 目标

把这台 Mac 上与个人使用、代码开发、VS Code、Codex/AI IDE 相关的数据，尽量完整地迁移到另一台电脑，并保证：

- 个人文件可继续访问
- 代码项目和下载资料不丢
- VS Code 配置、插件、工作区习惯尽量延续
- Codex / AI IDE 的本地配置、历史、技能、会话索引尽量保留
- SSH、终端、开发工具配置可继续使用

## 2. 当前机器上已确认的重要目录

### 2.1 个人内容数据

- `~/Desktop` 约 `714M`
- `~/Documents` 约 `6.0G`
- `~/Downloads` 约 `14G`
- `~/Music` 约 `1.3G`
- `~/Pictures` 存在，但照片库需要额外授权检查

### 2.2 代码与项目数据

- `~/code` 约 `21G`
- `~/Agent_learn` 约 `7.6G`
- `~/PycharmProjects` 约 `422M`
- `~/IdeaProjects`
- `~/My_project`
- `~/Documents/Codex`
- `~/Downloads` 里也有项目目录，比如：
  - `~/Downloads/claude-code-main`
  - `~/Downloads/code 2`
  - `~/Downloads/workspace`

### 2.3 VS Code 相关

- `~/Library/Application Support/Code` 约 `11G`
- `~/.vscode` 约 `4.9G`
- 关键目录：
  - `~/Library/Application Support/Code/User/settings.json`
  - `~/Library/Application Support/Code/User/globalStorage`
  - `~/Library/Application Support/Code/User/workspaceStorage`
  - `~/Library/Application Support/Code/Workspaces`
  - `~/.vscode/extensions`

### 2.4 Codex / AI IDE 相关

- `~/.codex` 约 `290M`
- `~/Library/Application Support/Codex`
- `~/Library/Application Support/com.openai.chat`

其中 `~/.codex` 已确认包含：

- `config.toml`
- `auth.json`
- `history.jsonl`
- `session_index.jsonl`
- `sessions/`
- `skills/`
- `memories/`
- `sqlite/`

### 2.5 登录、密钥、终端配置

- `~/.ssh`
- `~/.zshrc`
- `~/.zprofile`
- `~/.gitconfig`
- `~/.config`
- `~/.claude`
- 其他 AI 工具目录很多，分散在 `~/` 下，例如：
  - `~/.cline`
  - `~/.copilot`
  - `~/.gemini`
  - `~/.qwen`
  - `~/.comate`
  - `~/.icode`
  - `~/.opencode`

## 3. 已看到的 VS Code 最近工作区线索

从 `~/Library/Application Support/Code/User/globalStorage/state.vscdb` 中已经能看到最近打开过的路径，包括：

- `file:///Users/zhuji_m4pro/code/baidu/core/core_ori`
- `file:///Users/zhuji_m4pro/code/cs336/assignment1-basics`
- `file:///Users/zhuji_m4pro/code`
- `file:///Users/zhuji_m4pro/comate-zulu-demo-1764051646335`
- `file:///Users/zhuji_m4pro/code/kirin`
- 以及部分远程 SSH 工作区

这说明：如果你想“连打开过哪些目录也尽量延续”，`Code/User` 下的数据值得一起迁移。

## 4. 最推荐的迁移方式

### 方案 A：整机级迁移，优先推荐

如果目标是“尽可能原样搬过去”，优先用 Apple 官方迁移方式：

- `Migration Assistant`
- 或者 `Time Machine` 备份后在新电脑恢复

这种方式最适合你当前这种情况，因为你不只是要文件，还要：

- 用户目录内容
- 应用配置
- 部分应用本地状态
- SSH 密钥
- IDE 工作习惯
- 可能还包括钥匙串、登录项、系统偏好的一部分

适用场景：

- 新电脑也是 Mac
- 你想一次性完整迁移
- 你不想手工逐个目录挑

### 方案 B：手工分层迁移，适合“只迁用户数据”

如果你不想整机迁，只想把用户数据和开发环境搬走，建议按 4 层迁：

1. `个人文件层`
2. `代码项目层`
3. `IDE / AI 工具层`
4. `密钥与配置层`

## 5. 手工迁移时的优先级

### P0：必须先搬

- `~/Desktop`
- `~/Documents`
- `~/Downloads`
- `~/code`
- `~/Agent_learn`
- `~/PycharmProjects`
- `~/IdeaProjects`
- `~/My_project`
- `~/.ssh`
- `~/.gitconfig`
- `~/.zshrc`
- `~/.zprofile`

### P1：开发体验强相关

- `~/Library/Application Support/Code`
- `~/.vscode`
- `~/.codex`
- `~/Library/Application Support/Codex`
- `~/Library/Application Support/com.openai.chat`
- `~/.claude`
- `~/.config`

### P2：按需再搬

- `~/Music`
- `~/Movies`
- `~/Pictures`
- 其他 AI 工具目录，如 `~/.cline`、`~/.copilot`、`~/.gemini`、`~/.qwen` 等

## 6. 不建议只靠“复制应用程序 .app”来迁移

比如只复制：

- `/Applications/Visual Studio Code.app`
- `/Applications/Codex.app`

这是不够的。真正重要的是应用背后的用户数据目录。  
如果只复制 `.app`，通常丢的是：

- 设置
- 插件
- 登录状态
- 会话历史
- 最近打开目录
- 本地缓存和工作区状态

## 7. 推荐执行顺序

### 第一步：先做盘点清单

建议先整理一份最终迁移名单，至少包括：

- 个人文件目录
- 代码目录
- IDE 目录
- AI 工具目录
- SSH / Git / Shell 配置

### 第二步：先备份，再迁移

不要直接“边搬边删”。  
推荐先备份到：

- 外接 SSD
- 或 NAS
- 或另一台电脑的临时目录

### 第三步：先搬最关键目录

建议先搬：

- `~/code`
- `~/Agent_learn`
- `~/Documents`
- `~/Downloads`
- `~/.ssh`
- `~/Library/Application Support/Code`
- `~/.vscode`
- `~/.codex`

### 第四步：新电脑上安装应用，再恢复数据

顺序建议：

1. 新电脑先安装：
   - VS Code
   - Codex
   - Git
   - Python / Node / Java 等常用开发环境
2. 再把对应用户数据目录放回去
3. 最后逐项验收

## 8. 新电脑上的恢复重点

### VS Code

至少恢复这些：

- `~/Library/Application Support/Code/User`
- `~/Library/Application Support/Code/Workspaces`
- `~/.vscode/extensions`

如果要更完整，可直接恢复整个：

- `~/Library/Application Support/Code`
- `~/.vscode`

### Codex / AI IDE

建议恢复：

- `~/.codex`
- `~/Library/Application Support/Codex`
- `~/Library/Application Support/com.openai.chat`

这样可以最大概率保留：

- 本地配置
- 会话索引
- 技能与记忆
- 本地任务状态
- 一部分桌面端状态

### SSH 与终端

恢复：

- `~/.ssh`
- `~/.zshrc`
- `~/.zprofile`
- `~/.gitconfig`

恢复后要执行：

- 检查 `~/.ssh` 权限
- 测试 SSH 登录
- 测试 Git 身份

## 9. 推荐的复制方式

### 方式 1：外接硬盘 + Finder

适合：

- 文档
- 图片
- 视频
- 普通项目目录

优点：

- 简单直观

缺点：

- 隐藏目录容易漏
- 权限和时间戳保留不够稳定

### 方式 2：`rsync`，更适合开发数据

适合：

- 隐藏目录
- 配置目录
- 代码目录
- IDE 状态目录

参考命令模板：

```bash
rsync -aH --info=progress2 "/Users/zhuji_m4pro/code/" "/Volumes/YourDiskBackup/code/"
```

对隐藏目录同理，比如：

```bash
rsync -aH --info=progress2 "/Users/zhuji_m4pro/.codex/" "/Volumes/YourDiskBackup/dotfiles/.codex/"
rsync -aH --info=progress2 "/Users/zhuji_m4pro/.ssh/" "/Volumes/YourDiskBackup/dotfiles/.ssh/"
rsync -aH --info=progress2 "/Users/zhuji_m4pro/Library/Application Support/Code/" "/Volumes/YourDiskBackup/app_support/Code/"
```

## 10. 迁移后验收清单

新电脑上至少检查这些：

- `~/code` 是否完整
- `~/Agent_learn` 是否完整
- `~/Downloads` 是否完整
- `VS Code` 能否看到原来的设置、插件、最近项目
- `Codex` 是否能读取原配置与本地历史
- `ssh` 是否免密可用
- `git config user.name / user.email` 是否正确
- 常用项目能否正常打开和运行

## 11. 这次迁移里最容易漏掉的东西

- `~/.ssh`
- `~/.gitconfig`
- `~/.zshrc`
- `~/.codex`
- `~/.vscode/extensions`
- `~/Library/Application Support/Code/User`
- `~/Library/Application Support/com.openai.chat`
- `~/Downloads` 里的临时代码项目
- `~/Documents/Codex` 里的本地输出物

## 12. 对你当前情况的最实际建议

如果你是“整台工作环境都想复制过去”，最省心的路径是：

1. 先做一份完整外接盘备份
2. 能用 `Migration Assistant` 就优先用它
3. 再额外手工核对这几类目录有没有漏：
   - `~/code`
   - `~/Agent_learn`
   - `~/Downloads`
   - `~/.codex`
   - `~/Library/Application Support/Code`
   - `~/Library/Application Support/com.openai.chat`
   - `~/.ssh`

如果你不是整机迁移，而是“只拿用户数据到另一台电脑”，那就按上面的 `P0 -> P1 -> P2` 顺序分层复制。

## 13. Windows 只搬数据版重计划

这部分更符合你当前的新目标：

- 目标电脑是 `Windows`
- 不搬软件本体
- 只搬数据
- `code` 和 `Agent_learn` 必搬
- `Downloads` 要筛垃圾
- `Documents`、`Desktop` 要先分类
- `PyCharmProjects` 暂时不搬
- `VS Code` 不作为重点
- 重点保留 `百度 AI IDE / Comate` 的配置、最近打开目录、工作区状态

### 13.1 结论先说

对你来说，真正建议搬的是这 4 类：

1. 代码与项目
2. 个人文档与桌面资料
3. 百度 AI IDE / Comate 数据
4. 必要的通用配置

不建议原样全搬的是这 3 类：

1. `VS Code` 大缓存和插件缓存
2. 纯安装包、旧压缩包、未完成下载
3. 你已经明确不想要的 `PycharmProjects`

## 14. 你现在应该搬什么

### A. 必搬

- `~/code`
- `~/Agent_learn`
- `~/Documents/Codex`
- `~/Documents/pics`
- `~/Desktop`
- `~/.ssh`
- `~/.gitconfig`
- `~/.zshrc`
- `~/.zprofile`

### B. 百度 AI IDE / Comate 必搬

这部分是你当前最像“软件里的个人数据”的部分：

- `~/.comate` 约 `637M`
- `~/.icode` 约 `11M`
- `~/Library/Application Support/comate/User` 约 `24M`

其中最关键的是：

- `~/Library/Application Support/comate/User/settings.json`
- `~/Library/Application Support/comate/User/globalStorage`
- `~/Library/Application Support/comate/User/workspaceStorage`
- `~/.comate/config.json`
- `~/.comate/data/globalStorage.json`
- `~/.comate/extensions`
- `~/.icode/config.yml`

这几类数据大概率对应：

- Comate 的用户设置
- 最近打开目录
- 工作区状态
- 扩展信息
- 一部分命令/技能/本地能力配置

### C. 按情况搬

- `~/Documents/ComfyUI`
- `~/Documents/Obsidian Vault`
- `~/ComateProjects`
- `~/Downloads/workspace`
- `~/Downloads/api-smart-ai`
- `~/Downloads/code 2`
- `~/Downloads/core-migrate_ori`
- `~/Downloads/claude-code-main`

### D. 当前不建议搬

- `~/PycharmProjects`
- `~/IdeaProjects`
- `~/.vscode`
- `~/Library/Application Support/Code`
- `~/Library/Application Support/comate/Cache`
- `~/Library/Application Support/comate/CachedData`
- `~/Library/Application Support/comate/CachedExtensionVSIXs`
- `~/Library/Application Support/comate/WebStorage`

## 15. Downloads 目录怎么筛

根据当前盘点，`Downloads` 里建议分成 3 组。

### 15.1 高优先级保留

- `workspace`
- `api-smart-ai`
- `code 2`
- `core-migrate_ori`
- `claude-code-main`
- `ku-docs-export_20260417`
- `知识库文档下载_2026-04-28`
- `个人知识库.tar.gz`
- `wdkns-skills-main`

这些更像：

- 代码项目
- 导出的知识库
- 你后面可能继续用的资料

### 15.2 中优先级，先看内容再决定

- `录屏体验师智能体`
- `GUI显示类缺陷_20250709_2V1_20251009_190803`
- `PromptImageResponse_annotated`
- `灵动岛`
- `敏捷调研`
- `test_data`
- `dianshang`

这些更像：

- 项目产物
- 分析样本
- 某次阶段性资料

如果你知道后面还会用，就搬；不确定就先打包归档再决定。

### 15.3 低优先级，优先视为可不搬

- `06_压缩包`
- `07_安装包`
- `09_未完成下载`
- `BaiduIMInstaller6-1-10-6.app`
- `android-studio-panda4-mac_arm.dmg`
- `LM-Studio-0.4.12-1-arm64.dmg`
- `CC-Switch-v3.14.1-macOS.dmg`
- `i4ToolsDownloads`

这些更像：

- 安装器
- 软件包
- 历史缓存
- 未完成下载

因为你的目标是 Windows，而且你说“不搬软件”，这一组通常可以不搬。

## 16. Documents 里面现在主要是什么

当前看到最主要的是：

- `~/Documents/ComfyUI` 约 `6.0G`
- `~/Documents/pics`
- `~/Documents/Obsidian Vault`
- `~/Documents/Codex`

也就是说，`Documents` 不是传统意义上的纯文档目录，而是混合了：

- 一个很大的 AI / 图像工作目录 `ComfyUI`
- 一些图片素材
- 笔记库
- Codex 产出目录

如果你只搬“自己真正要继续使用的数据”，建议：

- `ComfyUI`：如果你后面在 Windows 上还会继续玩这套工作流，就搬
- `Obsidian Vault`：建议搬
- `Codex`：建议搬
- 杂项文档：按需搬

## 17. Desktop 里面现在主要是什么

当前看到 `Desktop` 更像“临时工作台”：

- `合并数据` 约 `537M`
- `抽奖` 约 `63M`
- `举报材料` 约 `47M`
- 若干 `pptx / docx / png / jpeg`
- `公积金提取材料`
- `简历`

建议处理方式：

- 与工作/个人事务直接相关的材料保留
- 临时截图、临时中间稿、重复稿先人工筛一下
- `Desktop` 不建议整包不看就搬

## 18. PyCharmProjects 是什么，要不要搬

当前看到：

- `~/PycharmProjects/JupyterProject` 约 `359M`
- `~/PycharmProjects/Agno` 约 `57M`
- `~/PycharmProjects/PythonProject` 约 `6.5M`

它不是“只是打开过的文件列表”，而是真实项目目录。  
如果这些项目本身你不要了，那可以不搬。  
如果只是“不想保留 PyCharm 的状态”，那没问题，不搬 `PycharmProjects` 也可以。

## 19. VS Code 为什么会这么大

你问的这个点很关键，结论是：

- `~/.vscode` 的 `4.9G` 几乎全部是 `extensions`
- `~/Library/Application Support/Code` 的 `11G` 里，最大的是：
  - `User` 约 `8.3G`
  - `WebStorage` 约 `1.6G`
  - `CachedExtensionVSIXs` 约 `526M`
  - `Cache` 约 `365M`
  - `CachedData` 约 `257M`

也就是说，VS Code 大不是因为你的代码，而是因为：

- 插件太多
- 插件缓存很多
- AI 对话/任务/工作区状态积累很多
- WebStorage 和 globalStorage 膨胀了

如果你不以 VS Code 为重点，这一整套完全可以不搬，或者只保留极小的一部分设置文件。

## 20. 百度 AI IDE 这套应该怎么搬

如果你只关心“百度这个 AI IDE”，建议分两层：

### 核心必搬

- `~/.comate`
- `~/.icode`
- `~/Library/Application Support/comate/User`

### 可不搬的大缓存

- `~/Library/Application Support/comate/Cache`
- `~/Library/Application Support/comate/CachedData`
- `~/Library/Application Support/comate/CachedExtensionVSIXs`
- `~/Library/Application Support/comate/WebStorage`
- `~/Library/Application Support/comate/GPUCache`
- `~/Library/Application Support/comate/Code Cache`

也就是说，真正值得迁移的 Comate 数据并不大，重点在 `User` 和 `~/.comate`。

## 21. 最近打开目录是否能在 Windows 上“自动对应”

这里要分开说：

### 21.1 代码文件本身

能迁过去，只要目录结构你自己规划好，就可以继续打开使用。

### 21.2 “最近打开目录”历史

Mac 里记录的是这种路径：

- `/Users/zhuji_m4pro/code/...`
- `file:///Users/zhuji_m4pro/Agent_learn`

Windows 里通常会变成：

- `C:\\Users\\你的Windows用户名\\code\\...`
- `D:\\work\\code\\...`

所以这些“最近打开记录”默认不会自动一一对应，因为路径字符串变了。

### 21.3 怎样尽量减少错位

建议 Windows 上尽量保留相同的顶层目录名字：

- `C:\\Users\\<你的用户名>\\code`
- `C:\\Users\\<你的用户名>\\Agent_learn`
- `C:\\Users\\<你的用户名>\\Documents\\Codex`
- `C:\\Users\\<你的用户名>\\Downloads`

这样虽然不是完全相同路径，但你后续重新打开项目时最不容易混乱。

### 21.4 如果你非常在意“最近打开列表”

可以后续做一次“路径重写”：

- 从 `comate/User/globalStorage/state.vscdb`
- 或 `storage.json`

把旧的 Mac 路径替换成新的 Windows 路径。

这一步可以做，但建议放在“文件先迁完并整理好路径”之后。

## 22. 最适合你的 Windows 迁移方案

建议最终按下面方式落地。

### 第一步：在 Windows 先规划目录

建议先建：

- `C:\\Users\\<你自己的用户名>\\code`
- `C:\\Users\\<你自己的用户名>\\Agent_learn`
- `C:\\Users\\<你自己的用户名>\\Documents\\Codex`
- `C:\\Users\\<你自己的用户名>\\Documents\\Obsidian Vault`
- `C:\\Users\\<你自己的用户名>\\Desktop_Migrated`
- `C:\\Users\\<你自己的用户名>\\Downloads_Migrated`
- `C:\\Users\\<你自己的用户名>\\AIIDE_Backup\\comate`

### 第二步：只复制你要的目录

优先复制：

- `~/code`
- `~/Agent_learn`
- `~/Documents/Codex`
- `~/Documents/Obsidian Vault`
- `~/Desktop` 里筛完后保留的内容
- `~/Downloads` 里筛完后保留的内容
- `~/.comate`
- `~/.icode`
- `~/Library/Application Support/comate/User`
- `~/.ssh`

### 第三步：不要直接把 macOS 专属缓存也带过去

尤其不要优先搬：

- `.dmg`
- `.app`
- `Cache`
- `GPUCache`
- `Code Cache`
- `CachedData`
- `CachedExtensionVSIXs`

### 第四步：到 Windows 上重新安装百度 AI IDE

然后再把保留的数据目录放回它对应的位置。  
如果它不完全兼容旧路径，也至少可以：

- 保留设置
- 保留部分工作区状态
- 保留历史数据作参考

## 23. 对你当前问题的直接建议

如果现在就要开始执行，建议你按这个顺序做：

1. 必搬：
   - `code`
   - `Agent_learn`
   - `Documents/Codex`
   - `~/.comate`
   - `~/.icode`
   - `Library/Application Support/comate/User`
2. 半搬半筛：
   - `Downloads`
   - `Desktop`
   - `Documents`
3. 不搬：
   - `PycharmProjects`
   - `IdeaProjects`
   - `VS Code` 全量缓存
   - 各类 `.dmg`、`.app`、未完成下载

## 24. 你刚刚确认后的最终取舍

### 明确不要

- `~/Documents/ComfyUI`
- `~/Documents/Obsidian Vault`
- `~/Desktop/抽奖`
- `~/PycharmProjects` 项目内容本体
- `~/IdeaProjects` 项目内容本体

### 明确保留

- `~/code`
- `~/Agent_learn`
- `~/Desktop/举报材料`
- `~/Desktop/公积金提取材料`
- `~/Desktop/简历`
- `~/Desktop` 上的图片文件
- `~/Documents/Codex`
- `~/.comate`
- `~/.icode`
- `~/Library/Application Support/comate/User`
- `JetBrains` 的最近项目和窗口配置

## 25. `合并数据` 里面是什么

`~/Desktop/合并数据` 当前主要是医学影像/模型相关数据，不像普通文档：

- `xiazhi_0000.nii.gz` 约 `181M`
- `test_fd/` 约 `168M`
- `20250213 彭凤琼/` 约 `95M`
- `simultaneous1/` 约 `89M`
- 多个 `*_merged.nii.gz`
- 多个 `*_artery.nii.gz`

结论：

- 这不是系统垃圾，也不是普通缓存
- 更像某个影像处理或模型实验工作目录

如果你后面不再需要这一类医学影像数据，可以不搬。  
如果你不确定，建议先单独归档，不要混到普通 `Desktop` 材料里。

## 26. JetBrains 你真正要搬什么

你说得对，这里你真正想要的是：

- 打开过哪些项目
- 上次主要开的路径
- 一部分窗口/工作区状态

而不是 `PycharmProjects` 或 `IdeaProjects` 里的项目内容本体。

### 关键配置位置

- `~/Library/Application Support/JetBrains/IntelliJIdea2025.2/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/PyCharm2025.2/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.1/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.2/options/recentProjects.xml`

以及这些可一起保留：

- `~/Library/Application Support/JetBrains/IntelliJIdea2025.2/options/ide.general.xml`
- `~/Library/Application Support/JetBrains/PyCharm2025.2/options/ide.general.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.1/options/ide.general.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.2/options/ide.general.xml`

### 已确认到的最近项目线索

IntelliJ 最近项目里已经看到：

- `$USER_HOME$/code/baidu/qamate-strategy/apismart-code`
- `core-migrate`
- `itp`
- `core`

PyCharm 最近项目里已经看到：

- `$USER_HOME$/code/baidu/ducc`
- `$USER_HOME$/My_project/baidu/qamate-strategy/core`
- `api-smart-ai`
- `apismart_code`
- `Agno`

### 实际建议

如果你只想保留“最近项目和打开习惯”，只搬：

- `~/Library/Application Support/JetBrains/*/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/*/options/ide.general.xml`

就够了。  
`workspace` 目录可以不优先搬，因为它更多是局部窗口状态，而且跨系统兼容性不如 `recentProjects.xml` 稳定。

## 27. Windows 上目录怎么规划最稳

你的目标不是“路径字面完全相同”，而是“迁过去后尽量不乱，IDE 也容易重新接上”。  
最稳的做法是：在 Windows 上保留和 Mac 尽量一致的顶层语义。

### 推荐目录骨架

建议在 Windows 上建立：

- `D:\\code`
- `D:\\Agent_learn`
- `D:\\Documents_Migrated\\Codex`
- `D:\\Documents_Migrated\\Desktop_keep`
- `D:\\Documents_Migrated\\Downloads_keep`
- `D:\\AIIDE_Backup\\comate`
- `D:\\IDE_Config\\JetBrains`

如果你只有 `C` 盘，也可以用：

- `C:\\Users\\<你的用户名>\\code`
- `C:\\Users\\<你的用户名>\\Agent_learn`
- `C:\\Users\\<你的用户名>\\Documents\\Codex`
- `C:\\Users\\<你的用户名>\\Documents\\Desktop_keep`
- `C:\\Users\\<你的用户名>\\Documents\\Downloads_keep`

### 为什么这样摆

- `code` 单独放一层，后面所有 IDE 都好找
- `Agent_learn` 单独保留，避免和普通文档混在一起
- `Desktop`、`Downloads` 搬过去时不要继续叫原生桌面和下载目录，先放进 `*_keep`
- `AIIDE_Backup` 和 `IDE_Config` 单独放，后面恢复配置时不容易弄乱

## 28. 对应恢复建议

### 百度 AI IDE / Comate

Windows 上先安装对应软件，然后再把这些作为“恢复参考源”：

- `~/.comate`
- `~/.icode`
- `Library/Application Support/comate/User`

如果软件的 Windows 配置目录不同，不要硬覆盖未知目录。  
更稳的是：

1. 先让 Windows 版软件自己启动一次
2. 找到它在 Windows 上的配置目录
3. 再把旧配置里的 `settings / recent paths / globalStorage` 按需覆盖或对照迁移

### JetBrains

Windows 上也建议先安装并启动一次 `PyCharm / IDEA`，再恢复：

- `recentProjects.xml`
- `ide.general.xml`

因为 JetBrains 在不同系统下配置根目录不同，先让它生成目录结构最稳。

## 29. 最终迁移名单

这一节按照你现在已经明确的意愿，直接整理成可执行版本。

### 29.1 必搬

#### 核心代码与工作目录

- `~/code`
- `~/Agent_learn`
- `~/Documents/Codex`

#### 百度 AI IDE / Comate

- `~/.comate`
- `~/.icode`
- `~/Library/Application Support/comate/User`

#### JetBrains 配置

- `~/Library/Application Support/JetBrains/IntelliJIdea2025.2/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/IntelliJIdea2025.2/options/ide.general.xml`
- `~/Library/Application Support/JetBrains/PyCharm2025.2/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/PyCharm2025.2/options/ide.general.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.1/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.1/options/ide.general.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.2/options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/PyCharmCE2025.2/options/ide.general.xml`

#### 桌面明确保留

- `~/Desktop/举报材料`
- `~/Desktop/公积金提取材料`
- `~/Desktop/简历`
- `~/Desktop/20250707-162810.jpeg`
- `~/Desktop/23c2ca4d7275ace02f9bcb3bf.jpg`
- `~/Desktop/apismart_pic.png`
- `~/Desktop/Screenshot 2025-09-16 at 17.43.28.png`

### 29.2 明确不搬

#### 医疗与无关实验数据

- `~/Desktop/合并数据`

#### 已明确不要的目录

- `~/Documents/ComfyUI`
- `~/Documents/Obsidian Vault`
- `~/Desktop/抽奖`
- `~/Desktop/Lottery 3`
- `~/PycharmProjects`
- `~/IdeaProjects`

#### 软件安装包与系统无关缓存

- `~/Downloads/07_安装包`
- `~/Downloads/09_未完成下载`
- `~/Downloads/BaiduIMInstaller6-1-10-6.app`
- `~/Downloads/android-studio-panda4-mac_arm.dmg`
- `~/Downloads/LM-Studio-0.4.12-1-arm64.dmg`
- `~/Downloads/CC-Switch-v3.14.1-macOS.dmg`
- `~/Downloads/WPS Office Installer.app`
- `~/Downloads/i4ToolsDownloads`
- `~/.vscode`
- `~/Library/Application Support/Code`

### 29.3 待确认后再决定

#### Documents

- `~/Documents/pics`
- `~/Documents/北京半年会稿子.pdf`
- `~/Documents/无标题-2025-08-04-1830.excalidraw.png`
- `~/Documents/无标题-2025-08-04-1830.excalidraw`
- `~/Documents/记忆框架.excalidraw`
- `~/Documents/无标题-2025-08-04-1830.excalidraw.svg`
- `~/Documents/演示文稿1.pptx`
- `~/Documents/申请补贴信息采集表xlsx-0.xlsx`
- `~/Documents/申请补贴信息采集表xlsx.xlsx`
- `~/Documents/社保证明&无房产证明开具指引.docx`
- `~/Documents/AI_Agent_大模型应用_投递清单.md`

#### Desktop 其他非图片文件

- `~/Desktop/2025EP年终总结 (1).pptx`
- `~/Desktop/香丰阁游戏环节.pptx`
- `~/Desktop/灯火里的中国.docx`
- `~/Desktop/dpmx.docx`
- `~/Desktop/都市的街巷 已燈影婆娑.docx`
- `~/Desktop/都市的街巷 已燈影婆娑.pdf`
- `~/Desktop/年会小游戏环节主持串词.docx`

#### Downloads 里建议保留的代码/知识类数据

- `~/Downloads/workspace`
- `~/Downloads/api-smart-ai`
- `~/Downloads/code 2`
- `~/Downloads/core-migrate_ori`
- `~/Downloads/claude-code-main`
- `~/Downloads/ku-docs-export_20260417`
- `~/Downloads/知识库文档下载_2026-04-28`
- `~/Downloads/个人知识库.tar.gz`
- `~/Downloads/wdkns-skills-main`
- `~/Downloads/knowledge_export_20260427`
- `~/Downloads/knowledge_export_20260427.zip`
- `~/Downloads/ku_export`
- `~/Downloads/ku_backup_20260427`
- `~/Downloads/Docker文档导出_2026-04-27`
- `~/Downloads/testoneknowledge_docs_20260427`

#### Downloads 里建议人工看一眼再决定的项目/资料

- `~/Downloads/录屏体验师智能体`
- `~/Downloads/GUI显示类缺陷_20250709_2V1_20251009_190803`
- `~/Downloads/PromptImageResponse_annotated`
- `~/Downloads/灵动岛`
- `~/Downloads/敏捷调研`
- `~/Downloads/01_文档`
- `~/Downloads/03_演示`
- `~/Downloads/05_音视频`
- `~/Downloads/08_代码_数据`
- `~/Downloads/test_data`
- `~/Downloads/dianshang`
- `~/Downloads/YZQ.seg`
- `~/Downloads/06_压缩包`
- `~/Downloads/04_图片`
- `~/Downloads/downloaded_images`
- `~/Downloads/10_其他`

## 30. Windows 端推荐落地目录

### 方案 A：有 `D` 盘时

- `D:\\code`
- `D:\\Agent_learn`
- `D:\\Documents_Migrated\\Codex`
- `D:\\Documents_Migrated\\Desktop_keep`
- `D:\\Documents_Migrated\\Downloads_keep`
- `D:\\AIIDE_Backup\\comate`
- `D:\\IDE_Config\\JetBrains`

### 方案 B：只有 `C` 盘时

- `C:\\Users\\<你的用户名>\\code`
- `C:\\Users\\<你的用户名>\\Agent_learn`
- `C:\\Users\\<你的用户名>\\Documents\\Codex`
- `C:\\Users\\<你的用户名>\\Documents\\Desktop_keep`
- `C:\\Users\\<你的用户名>\\Documents\\Downloads_keep`
- `C:\\Users\\<你的用户名>\\Documents\\AIIDE_Backup\\comate`
- `C:\\Users\\<你的用户名>\\Documents\\IDE_Config\\JetBrains`

## 31. Windows 上的恢复顺序

1. 先创建上面的目录骨架
2. 先复制 `code`、`Agent_learn`、`Documents/Codex`
3. 再复制 `Desktop_keep` 和 `Downloads_keep`
4. 再复制 `~/.comate`、`~/.icode`、`comate/User`
5. 安装 Windows 版百度 AI IDE，启动一次
6. 找到 Windows 版配置目录后，再把旧配置中的 `settings / globalStorage / recent paths` 对照恢复
7. 安装 Windows 版 `PyCharm / IDEA`，启动一次
8. 再恢复 `recentProjects.xml` 与 `ide.general.xml`

## 32. 你下一步最应该做什么

如果现在就开始执行，顺序建议是：

1. 直接复制：
   - `~/code`
   - `~/Agent_learn`
   - `~/Documents/Codex`
   - `~/.comate`
   - `~/.icode`
   - `~/Library/Application Support/comate/User`
   - JetBrains `options/*.xml`
2. 单独整理：
   - `Desktop` 里保留项
   - `Downloads` 里待确认项
3. 明确丢弃：
   - 医疗数据
   - 安装包
   - VS Code 缓存
   - 不要的 IDE 项目目录
