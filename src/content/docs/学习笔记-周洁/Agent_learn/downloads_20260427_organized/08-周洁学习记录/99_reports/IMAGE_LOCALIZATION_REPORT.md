---
title: "学习记录压缩包检查与图片本地化报告"
description: "来源压缩包：/Users/zhujim4pro/Downloads/知识库文档下载2026-04-28.tar.gz"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\99_reports\\IMAGE_LOCALIZATION_REPORT.md"
---
# 学习记录压缩包检查与图片本地化报告

来源压缩包：`/Users/zhuji_m4pro/Downloads/知识库文档下载_2026-04-28.tar.gz`

整理目录：`downloads_20260427_organized/08-周洁学习记录/`

## 压缩包检查

- `gzip -t`：通过
- tar路径安全检查：通过，未发现绝对路径或 `..` 路径
- SHA-256：`c31987970e90d2a2c99313b79078b1124bb8948d75b4585e38190d322b846aa7`
- 解压后文件数：620
- Markdown：130
- PNG：171

## 图片检查

初始扫描：

- Markdown图片引用：532
- 本地图片引用：465
- 本地图片可解析：465
- 本地图片坏链：0
- 远程图片引用：67
- 唯一远程URL：62

本地化结果：

- 成功下载唯一远程图片：28
- 写入目录：`../_remote_images/08-周洁学习记录/remote_downloads/`
- 下载目录大小：约 6.9M
- 替换Markdown引用：33
- 修改Markdown文件：10

后续整理：

- 所有本地图片和图片资源已统一移动到：`../_remote_images/08-周洁学习记录/`
- Markdown 图片链接已改为指向外层统一图片目录。

最终校验：

- 本地图片引用：498
- 本地图片可解析：498
- 本地图片坏链：0
- 剩余远程图片引用：34
- 剩余唯一远程URL：34

剩余 34 个远程图片均来自 `rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=...`。服务返回 `code=400, msg=参数缺失`，缺少 `docGuid` 参数，且无法从其他链接推断，因此保留原始远程图片语法。

## 清单文件

- `99_reports/manifest.json`
- `99_reports/failed_downloads.json`
