---
title: "📄 Raycast介绍"
description: "Raycast介绍"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🧰【必看】工欲善必先利其器\\📁 【墙裂推荐】极致提效快捷键工具-Raycast\\📄 Raycast介绍.md"
---
Raycast介绍

> 🔗 原文链接：[https://blog.csdn.net/xiaosha799/article/details/142289204](https://blog.csdn.net/xiaosha799/article/details/142289204)
> ✂️ 本文由 [超级助理Web端](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/EOebV5HeCA/XZFdnhZMp5uINC#anchor-12b0b880-e295-11ee-8bc1-51db081e8926) 一键剪存
![](/personal-site-mvp/img/doc-placeholder.svg "")
[Raycast](https://raycast.com/?via=TechLifeShare) 是一款 [MacOS](https://so.csdn.net/so/search?q=MacOS&spm=1001.2101.3001.7020) 生产力工具，使用方式和 Alfred、uTools 一样，通过一个快捷输入框完成多数操作，提高工作效率，

 完全替代 Mac 自带的 Spotlight，帮助用户专注于核心任务。它不仅提供丰富使用的功能，还通过开放平台支持开发者扩展。

 随着融入 AI 功能，效率体验更强👍🏻。

如果是 Pro 用户可以享受云同步 cloud、自定义主题 theme、无限制剪切版历史记录、开放更多 API，以及[Raycast](https://raycast.com/?via=TechLifeShare) AI 功能（可以有 14 天试用期）。

我也是从 Alfred 和 [uTools](https://so.csdn.net/so/search?q=uTools&spm=1001.2101.3001.7020) 摸过来的，选择使用 Raycast 的理由如下：

* **视觉风格现代**：[Raycast](https://raycast.com/?via=TechLifeShare) 的 UI 设计能够很好地融入 MacOS 全新视觉风格，与系统原生应用的感觉一致。
* **开发人员定制**：符合开发人员设计的生产力工具，帮助开发者高效地管理软件开发相关的任务。
* **功能全面**：Raycast 不仅可以启动程序或搜索文件，还能在多个第三方服务如 Asana、GitHub、Jira 等中创建、搜索和关闭 issues，以及批准、合并和关闭 GitHub 的拉取请求（哪怕没有这些平台，也算参考思路自己去集成开发）。
* **系统快捷设置和脚本命令**：[Raycast](https://raycast.com/?via=TechLifeShare) 内置了一些系统功能调节，并支持加载命令脚本（Script），提高复杂任务操作效率。
* **拓展商店**（Extension Store）：通过扩展商店，用户可安装丰富扩展，构建个性化的强大生产力工具平台。

用上 [Raycast](https://raycast.com/?via=TechLifeShare) 后，我卸载了很多功能软件，如 Spectacle（窗口管理）、Xnip（截图）、Paste（剪贴板管理）等，因为 Raycast 已经可以满足我的大部分需求，保持精简。以下介绍 Raycast 的常用功能。

#### 替换聚焦 Spotlight
默认呼出 Spotlight 的热键是 `⌘ + Space`，因为 Raycast 能完全替代它，更改下配置。

 我的 MacOS 版本是 Ventura 界面会与之前的版本有差异，但操作基本一致。详见官方操作手册 https://manual.raycast.com/hotkey?via=TechLifeShare

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 搜索栏 Search Bar
Search Bar 中可以直接搜索`applications`、`extensions`、`scripts`，

 [Raycast](https://raycast.com/?via=TechLifeShare) 的搜索对`中文`和`拼音`支持很好，且支持优秀的`模糊搜索`算法。

 在 `Raycast Settings > Advanced > Root Search Sensitivity` 还能调整模糊程度。

![](/personal-site-mvp/img/doc-placeholder.svg "")
`High`将使算法更严格，搜索值要求更精确。`Low`允许匹配字母，最大化模糊搜索。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 文件搜索 Search Files
对于文件和目录的检索需要明确指定，输入`sf`回车进入，这样可以更好的掌控搜索结果。

![](/personal-site-mvp/img/doc-placeholder.svg "")
搜索结果默认按更新时间倒序展示。

![](/personal-site-mvp/img/doc-placeholder.svg "")
还支持以下搜索语法：

* 文件后缀 `.png`
* 部分文件名 + 搜索范围 `.png xxx in ~/Document`

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 浏览器书签搜索 Search Browser Bookmarks
输入`sbb`回车进入，搜索浏览器书签并直接打开，还可以设定搜索源自哪个浏览器。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 历史粘贴板 Clipboard History
这项内置的功能可以做到，历史记录（至多 256 条），数据保存本地（数据上云的话，密码或涉及隐私的信息你敢放进去吗？😘），

 还能将重要常用内容固定住（pinned），使用更方便。

![](/personal-site-mvp/img/doc-placeholder.svg "")
产品设计上真是贴心实用，准备了额外的快捷键操作历史记录，如`cmd + shift + p`固定内容，再次触发便取消。

![](/personal-site-mvp/img/doc-placeholder.svg "")
因为这是我高频使用功能，设置快捷键`ctrl + opt + p`直接呼出`Clipboard History`。

#### 计算器 Calculator
除了数学计算，还支持汇率、日期、单位转换等。并且直接在搜索框输入即可计算。

更多用法参考官方文档 https://manual.raycast.com/calculator?via=TechLifeShare，一股开发味儿🧑‍💻。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### [Raycast](https://www.raycast.com/?TechLifeShare) 快捷键
[Raycast](https://raycast.com/?via=TechLifeShare) 的设计理念就是缩短操作路径，其自身的鼠标操作也设计了好用的快捷键：

* `esc` 回到上一页
* `⌘ esc` 返回主搜索页面
* `⌘ W` 关闭 Raycast 窗口
* `⌘ ,` 打开 Raycast 配置页
* `⌃ N` or `⌃ P` 可用于在任何列表视图中向下或向上移动（取代鼠标移动和滚轮）

`⌘ ⇧ ,` 打开选定项目的配置页

 `⌘ ⇧ F` 将选定项目加入或移出收藏夹

 `⌘ ⌥ ↑ | ↓` and ⌘ ⌥ ↓ to move a favorite item up and down the list

#### 系统操作命令
[Raycast](https://raycast.com/?via=TechLifeShare) 内置了控制系统命令插件`System` Extension，可以通过搜索框控制调整声音、锁屏、清空回收站等。

* Eject All Disks: 弹出所有挂载的磁盘
* Empty Trash: 清空回收站
* Hide All Apps Except Frontmost: 专注于最前面的应用程序并隐藏所有其他应用程序
* Lock Screen: 锁定Mac的屏幕
* Log Out: 注销帐户
* Quit All Applications: 关闭所有正在运行的应用程序
* Restart: 重启Mac
* Set Volume to 0/25/50/75/100%: 调整音量
* Show Desktop: 显示桌面
* Shut Down: 退出所有打开的应用程序并关闭系统
* Sleep: Mac进入睡眠
* Sleep Displays: 将Mac的显示器置于睡眠状态
* Toggle Bluetooth: 打开和关闭蓝牙
* Toggle Hidden Files: 选择是否能够在Mac上看到隐藏文件
* Toggle Mute: 打开/关闭Mac的声音（静音🔇）
* Toggle System Appearance: 在系统上的亮/暗模式之间切换
* Turn Volume Down/Up: 将Mac的音量微调几个百分比
* Unhide All Hidden Apps: 将我们所有隐藏和正在运行的应用程序带回来并取消隐藏它们

> 更多 `Script Commands` 脚本命令参看官方地址 `https://github.com/raycast/script-commands`
#### 窗口管理 Window Management
[Raycast](https://raycast.com/?via=TechLifeShare) 能帮你轻松地调整窗口大小、重新排列它们，还能移动你正在用的窗口，一切操作都在搜索栏中完成。

满足不同习惯：输入对应的窗口操作命令，或设置命令的简称，或设置快捷键。

![](/personal-site-mvp/img/doc-placeholder.svg "")
[订阅 Pro](https://www.raycast.com/pro?via=TechLifeShare) 还有更好的操作设置，这里基础功能对我已足够使用。

#### 命令别名和热键 Command Aliases and Hotkeys
通过 `Raycast Settings → Extensions` 可以设置所有命令的别名和热键，极限操作的福音。

 这类设置可以让我只使用键盘完成大部分操作🐙。

![](/personal-site-mvp/img/doc-placeholder.svg "")
> 不用的功能可以在 `Raycast Settings → Extensions → Enabled` 中关闭，减少干扰搜索结果。
#### 拓展商店 Store & Extensions
[Raycast 的拓展商店](https://www.raycast.com/store?via=TechLifeShare)，可以安装丰富的扩展，满足各种需求，如：翻译、天气、时间、日历、笔记、待办事项、文件管理、系统工具、网络工具、媒体工具、社交工具、开发工具等等。

![](/personal-site-mvp/img/doc-placeholder.svg "")
[Raycast](https://raycast.com/?via=TechLifeShare) 拓展商店 `https://www.raycast.com/store?via=TechLifeShare` 已有 1600+ 拓展，且还在不断更新中。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 脚本片段 Snippets
常用文本、代码、短语等内容可以使用 Snippets 功能存起来，使用时通过简单记忆的符号轻松调用。

![](/personal-site-mvp/img/doc-placeholder.svg "")
对比 Mac 自定义短语，Raycast Snippets 的设置更灵活。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 快速链接 Quicklinks
可以快速打开 google 搜索等页面，动态入参。也可以快速打开指定目录。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 脚本命令 Script Commands
灵活的拓展能力，通过自定义脚本（shell,python,javascript等等），实现自己的工作流，对有一定开发能力的用户来说。

![](/personal-site-mvp/img/doc-placeholder.svg "")
逛逛社区贡献的脚本有没你想要的，也可以参考他们的写法，`https://github.com/raycast/script-commands`。

#### 最后
[Raycast](https://raycast.com/?via=TechLifeShare) 的设计理念是：`Make your Mac work for you`，让 Mac 为你工作，而不是你为 Mac 工作。

更多使用参看官方手册 https://manual.raycast.com/ai?via=TechLifeShare。
