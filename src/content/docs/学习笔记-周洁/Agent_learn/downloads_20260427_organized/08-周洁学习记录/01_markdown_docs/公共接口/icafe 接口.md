---
title: "icafe 接口"
description: "icafe 接口"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\公共接口\\icafe 接口.md"
---
icafe 接口

1、获取卡片信息

```
get http://icafeapi.baidu-int.com/api/spaces/{story_id_name}/cards/{story_id_num}?u={icafe_u}&pw={icafe_pw}
```
其中 icafe_pw访问 [链接](https://console.cloud.baidu-int.com/api/icafe/users/virtual) 获取

举个例子：datastrategy-772

http://icafeapi.baidu-int.com/api/spaces/datastrategy/cards/772?u=zhoujie19&pw=VV1n8Ugxxxx

![](/personal-site-mvp/img/doc-placeholder.svg "")
