---
title: "引用文档与图片本地化报告"
description: "来源目录：/Users/zhujim4pro/Downloads/知识库文档下载2026-04-28"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\99_reports\\REFERENCE_AND_IMAGE_LOCALIZATION_REPORT.md"
---
# 引用文档与图片本地化报告

来源目录：`/Users/zhuji_m4pro/Downloads/知识库文档下载_2026-04-28`

目标目录：`/Users/zhuji_m4pro/Agent_learn/downloads_20260427_organized/08-周洁学习记录`

统一图片目录：`/Users/zhuji_m4pro/Agent_learn/downloads_20260427_organized/_remote_images/08-周洁学习记录`

## 执行结果

- Markdown 文档：201
- 引用文档目录：35
- 图片/图片资源文件总数：1711
- 原导出 `.bin` 图片资源：357

## 文档引用处理

- 按标题匹配改成本地 Markdown 链接：100
- 按 `docGuid` 匹配改成本地 Markdown 链接：13
- 合计改成本地文档链接：113
- 仍保留的远程普通链接：942
- 其中仍保留的 `ku.baidu-int.com/knowledge` 文档链接：406

未匹配的文档链接清单：

- `missing_reference_links.json`
- `remaining_unmatched_ku_doc_links.json`

## 图片处理

- 远程图片唯一 URL：965
- 远程图片引用数：1007
- 成功下载唯一远程图片：931
- 下载失败唯一远程图片：34
- 替换为本地图片引用：952

最终校验：

- 本地图片引用：1816
- 本地图片文件存在：1816
- 本地图片坏链：0
- 剩余远程图片引用：55

## 注意事项

剩余远程图片失败原因仍是 `rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=...` 缺少 `docGuid`，服务返回 `code=400, msg=参数缺失`。这些链接保留原始图片语法。

`.bin` 文件来自原始导出目录，文件内容是服务错误 JSON，不是可渲染图片。因为原始 Markdown 只给了本地 `.bin` 路径，没有可恢复的远程 URL，本次只把这些资源集中移动到统一图片目录并保留引用，同时在此报告中标明。
