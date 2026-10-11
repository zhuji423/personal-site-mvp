---
title: "Windows C 盘迁移 README"
description: "把当前 Mac 上你真正需要的数据迁移到只有 C: 盘的 Windows 电脑，并尽量做到："
date: "2026-05-02"
category: "个人事务与记录"
source: "F:\\百度工作\\03_documents_keep\\Codex\\2026-05-02-mac-vs-code-aiide-user\\WINDOWS_C_DRIVE_MIGRATION_README.md"
---
# Windows C 盘迁移 README

## 1. 目标

把当前 Mac 上你真正需要的数据迁移到只有 `C:` 盘的 Windows 电脑，并尽量做到：

- 代码目录清晰
- 百度 AI IDE / Comate 的配置可恢复
- PyCharm / IDEA 的最近项目记录可恢复
- 桌面和下载资料不乱
- 后续能重新打开项目

## 2. 先说结论

### 不建议的做法

不建议把所有数据压成一个超大的总压缩包。

原因：

- 你的代码和资料体量大
- 一个大压缩包出错后不好修
- 中途断掉很难续传
- 后续只想取某一部分时很麻烦

### 最推荐的做法

按“分类目录”复制，再对“小而重要的配置”单独压缩。

也就是：

1. 大目录直接复制
2. 配置目录单独打包
3. 每个大类放一个 `README`

## 3. Windows 上建议创建的目录

在 Windows 上先建这些目录：

```text
C:\Users\<你的Windows用户名>\workspace
C:\Users\<你的Windows用户名>\workspace\code
C:\Users\<你的Windows用户名>\workspace\Agent_learn
C:\Users\<你的Windows用户名>\workspace\Codex
C:\Users\<你的Windows用户名>\workspace\Desktop_keep
C:\Users\<你的Windows用户名>\workspace\Downloads_keep
C:\Users\<你的Windows用户名>\workspace\IDE_Config
C:\Users\<你的Windows用户名>\workspace\IDE_Config\Comate
C:\Users\<你的Windows用户名>\workspace\IDE_Config\JetBrains
C:\Users\<你的Windows用户名>\workspace\SSH_Backup
```

## 4. 为什么这样规划

- `workspace\code`
  用来承接 Mac 上的 `~/code`

- `workspace\Agent_learn`
  用来承接 `~/Agent_learn`

- `workspace\Codex`
  用来承接 `~/Documents/Codex`

- `workspace\Desktop_keep`
  用来承接桌面里你确认保留的资料

- `workspace\Downloads_keep`
  用来承接下载目录里保留的数据

- `workspace\IDE_Config\Comate`
  用来放百度 AI IDE / Comate 配置备份

- `workspace\IDE_Config\JetBrains`
  用来放 PyCharm / IDEA 的最近项目配置

- `workspace\SSH_Backup`
  用来放 `.ssh` 之类的重要账号配置备份

## 5. 迁移时建议怎么打包

### A. 直接复制，不压缩

这些目录建议直接复制：

- `~/code`
- `~/Agent_learn`
- `~/Documents/Codex`
- 桌面保留资料
- 下载目录保留资料

原因：

- 目录大
- 文件多
- 以后要直接用
- 不适合全塞进一个大压缩包

### B. 单独压缩

这些“小而关键”的配置建议单独压缩：

- `~/.comate`
- `~/.icode`
- `~/Library/Application Support/comate/User`
- `~/Library/Application Support/JetBrains/.../options/recentProjects.xml`
- `~/Library/Application Support/JetBrains/.../options/ide.general.xml`
- `~/.ssh`

推荐打成几个小包：

- `comate_config.zip`
- `jetbrains_config.zip`
- `ssh_backup.zip`

## 6. 你应该准备的迁移包结构

建议在 Mac 上先整理出这样一个总目录，再复制到移动硬盘或 Windows：

```text
MacToWindows_Migration/
  README-Windows-Setup.md
  code/
  Agent_learn/
  Codex/
  Desktop_keep/
  Downloads_keep/
  IDE_Config/
    comate_config.zip
    jetbrains_config.zip
  SSH_Backup/
    ssh_backup.zip
```

## 7. Desktop_keep 里建议放什么

放这些：

- `举报材料`
- `公积金提取材料`
- `简历`
- `20250707-162810.jpeg`
- `23c2ca4d7275ace02f9bcb3bf.jpg`
- `apismart_pic.png`
- `Screenshot 2025-09-16 at 17.43.28.png`

不要放这些：

- `合并数据`
- `抽奖`
- `Lottery 3`

## 8. Downloads_keep 里优先放什么

建议优先放：

- `workspace`
- `api-smart-ai`
- `code 2`
- `core-migrate_ori`
- `claude-code-main`
- `ku-docs-export_20260417`
- `知识库文档下载_2026-04-28`
- `个人知识库.tar.gz`
- `wdkns-skills-main`

其余待确认资料可后续再加。

## 9. Comate 怎么恢复

### 先做什么

1. 先在 Windows 安装百度 AI IDE / Comate
2. 启动一次
3. 登录一次

### 再做什么

然后把你备份出来的这些内容作为恢复源：

- `~/.comate`
- `~/.icode`
- `Library/Application Support/comate/User`

### 注意

Mac 和 Windows 的配置目录位置通常不同，所以：

- 不要在不知道目标目录前直接乱覆盖
- 先让 Windows 版软件生成自己的目录
- 再把旧配置里的 `settings`、`globalStorage`、`recent paths` 对照迁移

## 10. JetBrains 怎么恢复

### 先做什么

1. 安装 Windows 版 `PyCharm / IntelliJ IDEA`
2. 启动一次后退出

### 再做什么

把这些文件作为恢复源：

- `recentProjects.xml`
- `ide.general.xml`

### 目的

主要是恢复：

- 最近打开过哪些项目
- 默认项目打开位置
- 一部分通用 IDE 行为设置

## 11. 为什么有些项目可能不会自动打开

因为 Mac 里记录的是这种路径：

```text
/Users/zhuji_m4pro/code/...
```

Windows 里会变成：

```text
C:\Users\<你的Windows用户名>\workspace\code\...
```

所以恢复配置后：

- 最近项目列表可能会显示旧路径
- 你需要第一次手工重新打开一次
- 重新打开后，Windows 版本的 IDE 会记住新路径

## 12. 代码目录在 Windows 上怎么对应

Mac:

- `~/code`
- `~/Agent_learn`
- `~/Documents/Codex`

Windows:

- `C:\Users\<你的Windows用户名>\workspace\code`
- `C:\Users\<你的Windows用户名>\workspace\Agent_learn`
- `C:\Users\<你的Windows用户名>\workspace\Codex`

## 13. 建议的实际迁移顺序

1. 在 Windows 创建目录骨架
2. 复制大目录：
   - `code`
   - `Agent_learn`
   - `Codex`
3. 复制人工筛过的：
   - `Desktop_keep`
   - `Downloads_keep`
4. 复制配置压缩包：
   - `comate_config.zip`
   - `jetbrains_config.zip`
   - `ssh_backup.zip`
5. 安装 Windows 版软件：
   - 百度 AI IDE / Comate
   - PyCharm
   - IntelliJ IDEA
6. 启动一次再恢复配置
7. 手工重新打开最常用的几个项目

## 14. 最后的建议

对你这次迁移来说，最稳的不是“一个总压缩包”，而是：

- 大目录直接复制
- 小配置单独打包
- 保留一份 README

这样最容易恢复，也最不容易在 Windows 上打不开。
