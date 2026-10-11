---
title: "1、数字员工维度短期记忆"
description: "平台内置基于key-value的核心结构化记忆数据存储"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🤖如流&ducc&skills&沙箱开发接入指南\\📁 🧠怎么管理记忆\\📄 [平台内置]基于key-value的核心结构化记忆数据存储.md"
---
[平台内置]基于key-value的核心结构化记忆数据存储

# 1、数字员工维度短期记忆
* 平台提供了默认的，数字员工维度的记忆能力，基于K-V键值对存储
* 针对用户的sessionId taskId  当前数字员工可用的沙箱列表等轻量级的数据，可以直接使用
* 默认存储30天，最大90天(针对90天内无任何更新，则自动清理，每次更新自动续期对应的过期时长)

```
self.set_aiworker_memory("KEY", "VALUE")
self.get_aiworker_memory("KEY")
self.del_aiworker_memory("KEY")
self.del_aiworker_all_memory()
```
# 2、任务维度短期记忆
* 平台提供了默认的，基于Redis的任务维度短期记忆能力，基于K-V键值对存储
* 针对任务对应的sessionId、taskId、任务状态、目标状态等轻量级的数据，可以直接使用
* 默认存储24小时，最大7天(针对7天内无任何更新，则自动清理，每次更新自动续期对应的过期时长)

```
self.set_task_memory("KEY", "VALUE")
self.get_task_memory("KEY")
self.del_task_memory("KEY")
self.del_task_all_memory()
```
