---
title: "Markdown图片链接检查结果"
description: "检查范围：downloads20260427organized/ 下全部 .md 文件。"
date: "2026-04-28"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\IMAGE_LINK_AUDIT.md"
---
# Markdown图片链接检查结果

检查范围：`downloads_20260427_organized/` 下全部 `.md` 文件。

## 处理结果

- Markdown文件数：1112
- 剩余图片引用：10687
- 本地图片引用：51
- 本地图片可解析：51
- 本地图片坏链：0
- 空图片链接：0

## 已修复内容

- 修复 39 个本地图片路径：
  - `./ku_assets/<docGuid>/image_xxx.png` 改为实际存在的相对目录。
  - `/home/gem/workspace/.ark/output/.../assets/...` 改为当前导出目录内的 `./assets/...`。
- 替换 44 个空图片标记 `![]( "")` 为可见文本提示。
- 替换 8 个本地缺失图片引用为可见文本提示。
- 替换 1 个 `blob:` 图片引用为可见文本提示。

## 未改动内容

第一轮检查时还有 10636 个远程图片链接，主要来自：

- `rte.weiyun.baidu.com`：10467
- `bj.bcebos.com`：54
- `ku.baidu-int.com`：46
- `newicafe.baidu.com`：42
- `ku-open-new.baidu-int.com`：14
- `ai-studio-static-online.cdn.bcebos.com`：12
- `ss1.baidu.com`：1

这些是远程地址，不是本地文件坏链。是否能渲染取决于当前网络、登录态、内网权限和链接有效性。

## 远程图片本地化结果

- 远程图片引用：10636
- 唯一远程URL：5275
- 成功下载唯一图片：5122
- 成功替换Markdown图片引用：10471
- 下载目录：`_remote_images/`
- 下载目录大小：约 3.4G
- 本地化后Markdown图片引用：10522
- 本地化后可解析图片：10522
- 本地化后坏链：0
- 剩余远程图片语法：0

有 153 个唯一远程URL无法下载，涉及 165 处引用。它们都来自 `rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=...`，服务返回 `code=400, msg=参数缺失`，原因是 URL 缺少 `docGuid` 参数，且无法从其他链接推断。已将这些坏图片语法替换为普通文本链接，保留原始URL方便以后补救。

下载清单：

- `_remote_images/manifest_retry_ssl_unverified.json`
- `_remote_images/failed_downloads_retry_ssl_unverified.json`
- `_remote_images/summary_retry_ssl_unverified.json`
