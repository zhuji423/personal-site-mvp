---
title: "📁 🛠️SDK_qep-ai-agent"
description: "🛠️SDK:qep-ai-agent"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🤖如流&ducc&skills&沙箱开发接入指南\\📁 🛠️SDK_qep-ai-agent.md"
---
🛠️SDK:qep-ai-agent

具体功能参考：[qep-ai-agent 使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/U2QtrWOvMmtLmf?t=mention&mt=doc&dt=doc)

## 0.0.8
* 发布时间：2026-03-30 17:52:07
* 是否完全兼容上一个版本：是
* 主要更新点
    * 新增实体类
        * `TodoItem`              TODO列表条目（name/description/status）
        * `TodoWriteStreamData`   TODO更新流式卡片数据
        * `AttachmentItem`        附件条目（name/url/mime）
        * `AttachmentStreamData`  附件流式卡片数据

    * `StreamDataEnum` 新增枚举值
        * `TODO_WRITE(14)`         任务 TODO 列表
        * `ATTACHMENT(15)`         附件
        * `TASK_CRON_JOB(16)`      任务维度定时任务
        * `AIWORKER_CRON_JOB(17)`  数字员工维度定时任务
        * `API(18)`                API 触发
        * `PIPELINE_SUBMIT_TEST(19)` 流水线提测

    * `BaseAiAgent` 新增
        * `push_todo_write_stream_data`  推送 TodoWrite 工具的流式卡片
        * `push_attachment_data`         推送单个附件数据
        * `push_attachments_data`        推送附件列表数据
        * `push_cc_todo_data`            处理 CC 的 TodoWrite 工具消息并推送卡片
        * `is_todo_write`                判断工具是否为 TodoWrite

    * `BaseAiAgent.parse_cc_msg_and_push_to_testone` 行为变更
        * TodoWrite 工具调用时改为推送 Todo 卡片（不再推送普通函数调用卡片）

    * `stream_data_utils` 新增
        * `push_todo_data`        推送 TODO 列表流式数据
        * `push_attachment_data`  推送附件流式数据（支持同步推送如流 MARKDOWN 消息）



## 0.0.7
* 发布时间：2026-03-26 13:58:01
* 是否完全兼容上一个版本：是
* 主要更新点
    * `BaseDuccAgent` 新增危险命令拦截能力
        * `DANGEROUS_COMMAND_PATTERNS`  内置危险命令正则规则集（覆盖 rm/find/rmdir/unlink/shred/truncate 等变体）
        * `validate_bash_command`       PreToolUse Hook，自动拦截危险 Bash 命令
        * `log_tool_use`                PostToolUse Hook，记录所有工具使用日志
        * `_detect_dangerous_command`   检测命令中的危险操作（类方法）
        * `call_ducc` 中自动注册上述 Hook（无需子类手动配置）

    * `BaseAiAgent.get_cc_tool_name` 增强
        * 工具名称中文化：Bash→执行命令，Skill→调用技能，Read→读取文件，Write→写入文件，Edit→编辑文件
        * 新增 Grep（内容查找）、Glob（文件查找）、TodoWrite（更新TODO）工具识别
        * 新增 `ducc_workspace` 参数，文件路径自动转换为相对路径展示

    * `BaseAiAgent` 新增
        * `get_relative_path`  获取文件相对于基准目录的路径

    * `BaseAiAgent.parse_cc_msg_and_push_to_testone` 新增 `ducc_workspace` 参数
    * `TaskParameter.get_user_query` 增强，兼容各触发场景
        * `INFOFLOW_USER_QUERY`：支持 quoteUser/@用户、ai-markdown、image 等多种 query 类型拼接
        * `AIWORKER_CRONJOB`：返回 detail.description
        * 其他场景：返回完整 detail 的 JSON 字符串



## 0.0.6
* 发布时间：2026-03-17 11:39:19
* 是否完全兼容上一个版本：是
* 主要更新点
    * `BaseAiAgent.get_cc_tool_name`
        * 修复部分场景下 Bash 工具没有返回 `description` 字段导致的 KeyError 解析异常（改用 `.get()` 安全访问）



## 0.0.5
* 发布时间：2026-03-16 14:08:42
* 是否完全兼容上一个版本：是
    * `TaskParameter` 新增必传字段 `ai_worker_username`，`load_task_parameter` 同步支持

* 主要更新点
    * `TaskParameter` 新增
        * `ai_worker_username`  数字员工用户名（邮箱前缀），从请求参数 `aiWorkerUsername`/`aiqaUsername` 解析

    * `TaskParameter.get_user_query` 优化，兼容 `description` 和 `query` 两种 key 格式


## 0.0.4
* 发布时间：2026-02-27 20:40:00
* 是否完全兼容上一个版本：是
* 主要更新点
    * BaseAiAgent新增
        * get_preview_url       获取文件预览URL
        * send_md_msg_to_group 方法新增 `at_users` 参数，支持群聊消息 @用户

    * BaseAiAgent新增
        * get_mem_session_key   默认的session KEY生成策略
        * get_mem_session_id    获取记忆中的session ID
        * del_mem_session_id    删除记忆中的session ID
        * update_mem_session_id 更新记忆中的session ID



## 0.0.3
* 发布时间：2026-02-27 20:40:00
* 是否完全兼容上一个版本：是
* 主要更新点
    * BaseAiAgent新增
        * send_md_msg_to_user   给用户发送MARKDOWN消息
        * send_md_msg_to_group 给群聊发送MARKDOWN消息



## 0.0.2
* 发布时间：2026-02-10 10:20:21
* 是否完全兼容上一个版本：否
    * 将ducc_utils中相关的方法统一迁移至BaseDuccAgent (若之前未直接使用ducc_utils，直接忽略即可)

* 主要更新点
    * `ducc_utils`
        * ⚠️之前的各种消息推送、文件上传相关的方法统一迁移至`BaseDuccAgent` ``BaseAiAgent`` 
        * 新增 `is_session_exists`、`get_session_file_path`、`get_session_file_name` 方法，聚焦于 ducc session 文件管理

    * `BaseAiAgent`
        *  新增 `upload_dir_to_bos` 方法，支持将目录压缩为 zip 并上传至 BOS
        * ⚠️`upload_text_bos` 重命名为 `upload_text_to_bos`
        * ⚠️`upload_file_bos` 重命名为 `upload_file_to_bos`





## 0.0.1
* 发布时间：2026-02-04 11:10:42
* 是否完全兼容上一个版本：是
* 主要升级点
    * 首次发布



