---
title: "📄 qep-ai-agent 使用说明"
description: "qep-ai-agent 使用说明"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🤖如流&ducc&skills&沙箱开发接入指南\\📁 🛠️SDK_qep-ai-agent\\📄 qep-ai-agent 使用说明.md"
---
qep-ai-agent 使用说明

## BaseAiAgent
> 基础 Agent 类，所有 Agent 的核心基类，定义在 `base_ai_agent.py` 中。
> * 参考案例：
>     * [文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/quick_start.py?t=mention&mt=doc&dt=sdk)
> 
> 
#### 构造方法
```
def __init__(self, parameter: TaskParameter)
```
|属性|类型|说明|
|-|-|-|
|`parameter`|`TaskParameter`|任务参数对象|
|`_form_dict`|`Dict[str, Dict]`|表单提交场景的字段缓存|

#### 核心方法（抽象）
|方法|返回值|说明|
|-|-|-|
|`execute()`|`AgentResult`|**抽象方法**，子类必须实现。Agent 执行业务逻辑的入口|

#### 任务信息获取
|方法|返回值|说明|
|-|-|-|
|`get_operator()`|`str`|获取操作人|
|`get_task_id()`|`str`|获取任务 ID|
|`get_task_index()`|`str`|获取任务索引（需求卡片 ID）|
|`get_query()`|`str`|获取用户 Query，兼容所有触发场景（QUERY/INFOFLOW_USER_QUERY/AIWORKER_CRONJOB 等）|
|`get_group_id()`|`Optional[int]`|获取如流群聊 ID（非群聊场景返回 None）|

#### 流式数据推送
|方法|参数|说明|
|-|-|-|
|`push_think_stream_data(think_stream_data, to_infoflow=False)`|`think_stream_data`: 思考过程数据切片; `to_infoflow`: 是否推送到如流|推送思考过程数据|
|`push_result_stream_data(result_stream_data, to_infoflow=False)`|`result_stream_data`: 结果数据切片; `to_infoflow`: 是否推送到如流|推送模型执行结果|
|`push_func_call_data(func_name, func_arguments, buttons=None, icon="", to_infoflow=False)`|`func_name`: 函数名; `func_arguments`: 函数参数; `buttons`: 操作按钮列表; `icon`: 图标([lucide](https://lucide.dev/icons/armchair))|推送函数调用数据|
|`push_func_response_data(func_name, func_response, buttons=None, icon="", response_type=JSON, to_infoflow=False)`|`func_name`: 函数名; `func_response`: 函数返回结果; `response_type`: 响应格式(JSON/MARKDOWN/HTML)|推送函数调用返回结果|
|`push_infoflow_md_stream_data(md_stream_data)`|`md_stream_data`: MARKDOWN 格式数据|推送如流 MARKDOWN 格式的流式数据|
|`push_iframe_stream_data(name, url, show_in_dialog=False, height=500, icon="", to_infoflow=False)`|`name`: 名字; `url`: 链接; `show_in_dialog`: 是否在对话框展示; `height`: 展示高度|推送内嵌 URL 类型的消息卡|
|`push_component_stream_data(name, description, component, show_in_dialog=False, height=500, expand=False)`|`name`: 名字; `description`: 描述; `component`: BaseComponent 组件; `expand`: 默认是否展开|推送 TestOne 公共组件|
|`push_todo_write_stream_data(todos)`|`todos`: `List[TodoItem]` TODO 列表|推送 TodoWrite 工具的流式卡片|
|`push_attachment_data(name, url, mime, to_infoflow=True)`|`name`: 名称; `url`: 链接; `mime`: MIME 类型; `to_infoflow`: 是否推送到如流|推送单个附件数据（如流场景下同时发送 MARKDOWN 消息）|
|`push_attachments_data(attachments, to_infoflow=True)`|`attachments`: `List[AttachmentItem]` 附件列表; `to_infoflow`: 是否推送到如流|推送附件列表（如流场景下同时发送 MARKDOWN 消息）|

#### Claude Code 消息解析
|方法|参数|说明|
|-|-|-|
|`get_cc_tool_name(tool_msg, ducc_workspace=None)`|`tool_msg`: ToolUseBlock 或 ToolResultBlock; `ducc_workspace`: DUCC 工作目录（用于文件路径转相对路径）|获取 Claude Code 调用的工具名称，自动转换为中文可读描述（如 `执行命令(...)`、`读取文件(...)`、`内容查找(...)`），文件类工具路径自动转为相对路径|
|`parse_cc_msg_and_push_to_testone(msg, push_tool_to_testone=True, push_tool_call_to_infoflow=True, push_tool_result_to_infoflow=False, ducc_workspace=None)`|`msg`: Claude 消息; `push_tool_to_testone`: 是否推送工具消息; `push_tool_call_to_infoflow`: 是否推送工具调用到如流; `push_tool_result_to_infoflow`: 是否推送工具结果到如流; `ducc_workspace`: DUCC 工作目录|解析 DUCC（Claude Code）的消息并推送到 TestOne，自动处理 UserMessage/SystemMessage/AssistantMessage/ResultMessage 等各类型消息；TodoWrite 工具自动推送 Todo 卡片而非普通函数调用卡片|
|`get_relative_path(file_path, base)`|`file_path`: 文件路径; `base`: 基准目录|`str` 获取文件相对于基准目录的路径，异常时返回原路径|
|`is_todo_write(tool)`|`tool`: ToolUseBlock|`bool` 判断工具是否为 TodoWrite|
|`push_cc_todo_data(tool)`|`tool`: ToolUseBlock|解析 CC 的 TodoWrite 工具消息并推送 Todo 流式卡片|

#### 文件上传（BOS）
|方法|参数|返回值|说明|
|-|-|-|-|
|`upload_text_to_bos(content, file_name="content.txt")`|`content`: 文本内容; `file_name`: 文件名|`Optional[str]` BOS 链接|上传文本内容到 BOS|
|`upload_file_to_bos(file_path)`|`file_path`: 本地文件路径|`Optional[str]` BOS 链接|上传本地文件到 BOS，自动检测 MIME 类型|
|`upload_dir_to_bos(dir_path)`|`dir_path`: 目录路径|`Optional[str]` BOS 链接|将目录压缩为 zip 后上传到 BOS（目录为空或不存在时不执行）|
|`get_preview_url(file_url)`|`file_url`: 原始文件下载 URL（BOS）|`str` 预览页面 URL|生成文件预览页面 URL，用于侧边栏预览|

#### 内存管理 — 任务级（默认 24 小时过期，最大 7 天）
|方法|参数|返回值|说明|
|-|-|-|-|
|`set_task_memory(key, value, expire_time=86400)`|`key`: 键; `value`: 值; `expire_time`: 过期时间（秒）|`bool`|设置任务级内存|
|`get_task_memory(key)`|`key`: 键|`Optional[str]`|获取任务级内存|
|`get_task_all_memory()`|-|`Optional[Dict]`|获取任务的所有内存|
|`del_task_memory(key)`|`key`: 键|`bool`|删除指定任务级内存|
|`del_task_all_memory()`|-|`bool`|删除任务的全部内存|

#### 内存管理 — Agent 级（默认 30 天过期，最大 90 天）
|方法|参数|返回值|说明|
|-|-|-|-|
|`set_aiworker_memory(key, value, expire_days=30)`|`key`: 键; `value`: 值; `expire_days`: 过期天数|`bool`|设置数字员工级内存（每次 set 重置过期时间）|
|`get_aiworker_memory(key)`|`key`: 键|`Optional[str]`|获取数字员工级内存|
|`get_aiworker_all_memory()`|-|`Optional[Dict]`|获取数字员工的所有内存|
|`del_aiworker_memory(key)`|`key`: 键|`bool`|删除指定数字员工级内存|
|`del_aiworker_all_memory()`|-|`bool`|删除数字员工的全部内存|

#### 表单处理
|方法|参数|返回值|说明|
|-|-|-|-|
|`get_input_form_data(field_name)`|`field_name`: 字段名|`Optional[Dict]`|获取表单字段详细数据（仅 FORM_FINISH 场景可用）|
|`get_input_form_value(field_name)`|`field_name`: 字段名|`Optional[Any]`|获取表单字段的值|

#### 子任务管理
|方法|参数|返回值|说明|
|-|-|-|-|
|`create_sub_task(ai_id, task_name, task_target, detail, timeout=300, hidden=False)`|`ai_id`: 目标 Agent ID; `task_name`: 子任务名称; `task_target`: 任务目标; `detail`: 目标详情; `timeout`: 超时秒数(1~86400); `hidden`: 前端是否隐藏子任务|`TaskRecord`|创建子任务（当前任务不能是子任务）|
|`get_sub_task_by_id(sub_task_id)`|`sub_task_id`: 子任务 ID|`Optional[TaskRecord]`|根据子任务 ID 获取子任务信息|
|`callback_sub_task_result(result)`|`result`: SubTaskResult 对象|-|子任务结果回调（线下模式自动跳过）|

#### 任务目标管理
|方法|参数|返回值|说明|
|-|-|-|-|
|`get_task_target(task_id)`|`task_id`: 任务 ID|`Optional[TaskTarget]`|根据任务 ID 获取任务目标信息|
|`get_all_task_target(task_index)`|`task_index`: 任务索引|`List[TaskTarget]`|根据任务索引获取任务目标信息列表|
|`get_main_task_target()`|-|`TaskTarget`|获取主任务目标信息|
|`update_task_target_status(target_status)`|`target_status`: TargetStatusEnum|`bool`|更新任务目标状态|
|`get_task_description()`|-|`str`|获取任务顶部的描述信息|
|`update_task_description(description)`|`description`: MARKDOWN 格式描述|`bool`|更新任务顶部的描述信息|

#### 消息通知
|方法|参数|返回值|说明|
|-|-|-|-|
|`send_card_to_group(group_id, app_key, app_secret, notify_text, head, title, sub_title, description, url="", pc_open_type="session", mobile_open_type="bottom_sheet", btn_name="查看详情", at_users=None)`|详见源码注释|-|发送默认工作卡到群聊，支持 @用户（`["*"]` 为 @全员）|
|`send_card_to_user(username, app_key, app_secret, notify_text, head, title, sub_title, description, url="", pc_open_type="session", mobile_open_type="bottom_sheet", btn_name="查看详情")`|详见源码注释|`bool`|发送默认工作卡给指定用户|
|`send_msg_with_testone(usernames, content, msg_type)`|`usernames`: 用户名列表（邮箱前缀）; `content`: 消息内容; `msg_type`: 消息类型(MARKDOWN/TEXT/IMAGE)|`bool`|利用 TestOne 服务号给用户发消息|
|`send_md_msg_to_group(group_id, app_key, app_secret, msg, at_users=None)`|`group_id`: 群组 ID; `app_key`: 机器人/数字员工/服务号的 appKey; `app_secret`: 机器人/数字员工/服务号的 appSecret; `msg`: 需要发送的消息，markdown 格式; `at_users`: @的用户列表（邮箱前缀），`["*"]` 为 @全员|`bool`|使用机器人发送 Markdown 消息到群聊（[详情](https://ku.baidu-int.com/d/O7gUd6RJUGn7Ix)）|
|`send_md_msg_to_user(users, app_key, app_secret, msg)`|`users`: 用户名（邮箱前缀）列表; `app_key`: 机器人/数字员工/服务号的 appKey; `app_secret`: 机器人/数字员工/服务号的 appSecret; `msg`: 需要发送的消息，markdown 格式|`bool`|发送 Markdown 消息给个人（[详情](https://ku.baidu-int.com/d/UfS-RM_SnVkDGv)）|

---

## BaseDuccAgent
> Ducc Agent 类，继承自 BaseAiAgent。如果你希望直接使用 ducc（claude code）作为背后的 Agent，建议继承自此类。
> 参考案例：
> * [文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/quick_start_with_ducc.py?t=mention&mt=doc&dt=sdk)
> * [文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/quick_start_with_ducc_memory.py?t=mention&mt=doc&dt=sdk)
> 
#### 构造方法
```
def __init__(self, parameter: TaskParameter, ducc_bin_path: str, ducc_workspace: str)
```
|属性|类型|说明|
|-|-|-|
|`ducc_bin_path`|`str`|DUCC 二进制文件路径|
|`ducc_workspace`|`str`|DUCC 工作目录|

#### 方法列表
|方法|返回值|说明|
|-|-|-|
|`execute()`|`AgentResult`|**抽象方法**，子类必须实现|
|`async call_ducc()`|-|调用 DUCC 执行用户 Query。内部使用 `ClaudeSDKClient` 配置权限模式为 `acceptEdits`，允许 Read/Write/Edit/Grep/Glob/Bash/Skill 工具，自动注册 PreToolUse/PostToolUse Hook，异步流式接收消息并推送到 TestOne|

#### call_ducc 内部配置
```
ClaudeAgentOptions(
    permission_mode='acceptEdits',
    setting_sources=["user", "project"],
    allowed_tools=["Read", "Write", "Edit", "Grep", "Glob", "Bash", "Skill"],
    cwd=self.ducc_workspace,
    cli_path=self.ducc_bin_path,
    hooks={
        "PreToolUse": [HookMatcher(matcher="Bash", hooks=[self.validate_bash_command], timeout=180)],
        "PostToolUse": [HookMatcher(hooks=[self.log_tool_use])],
    }
)
```
#### 危险命令拦截
`BaseDuccAgent` 内置危险命令正则规则集（`DANGEROUS_COMMAND_PATTERNS`），通过 PreToolUse Hook 自动拦截 Bash 工具中的危险删除操作，无需子类额外配置。

覆盖范围：`rm -rf`、`rm -r`、`rm -f`、`rm` 通配符、`find -delete`、`find -exec rm`、`rmdir`、`unlink`、`shred`、`truncate -s 0`、重定向清空、`perl unlink`、`python os.remove/shutil.rmtree` 等变体。

|方法|参数|返回值|说明|
|-|-|-|-|
|`validate_bash_command(input_data, tool_use_id, context)`|`input_data`: 工具输入; `tool_use_id`: 工具使用 ID; `context`: HookContext|`dict` Hook 响应|PreToolUse Hook，检测到危险命令时返回 deny 决策并记录错误日志|
|`log_tool_use(input_data, tool_use_id, context)`|同上|`dict` Hook 响应|PostToolUse Hook，以 DEBUG 级别记录所有工具使用情况|
|`_detect_dangerous_command(command)`|`command`: 命令字符串|`List[Dict]` 匹配结果|类方法，返回命中的危险规则列表（含 name/desc/match）|

#### Session 管理（默认策略）
|方法|返回值|说明|
|-|-|-|
|`get_mem_session_key()`|`str`|获取记忆中存储的 session KEY。默认策略：如流单聊按用户名+天级别复用会话；群聊按群聊 ID+天级别复用会话；其他渠道按 TestOne 任务索引复用会话|
|`get_mem_session_id()`|`Optional[str]`|获取记忆中的 session ID|
|`update_mem_session_id(session_id)`|-|更新 session ID 到记忆中（如流场景会同时设置 TestOne 场景的 session）|
|`del_mem_session_id()`|-|删除对应用户的聊天 session ID|

---

## BaseSandboxAgent
> 基础沙箱 Agent 类，继承自 BaseAiAgent。如果希望具体的逻辑放到沙箱去执行，可以继承自此类，此类提供了远程操作沙箱的各种基础能力封装。
> 参考案例：
> * [文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/quick_start_with_sandbox_ducc_memory.py?t=mention&mt=doc&dt=sdk)
> 
#### 构造方法
```
def __init__(self, parameter: TaskParameter, sbx_expire_time: int = 3600,
             sbx_template: str = "deck", sbx_request_timeout: int = 60)
```
|属性|类型|说明|
|-|-|-|
|`sbx_expire_time`|`int`|沙箱过期时间（秒），默认 3600，最大 86400|
|`sbx_template`|`str`|沙箱模板名称，默认 `"deck"`|
|`sbx_request_timeout`|`int`|请求超时时间（秒），默认 60|
|`sbx`|`Optional[Sandbox]`|沙箱实例，使用前需先通过 `connect_existed_sandbox` 或 `apply_new_sandbox` 初始化|

#### 沙箱生命周期
|方法|参数|返回值|说明|
|-|-|-|-|
|`connect_existed_sandbox(sbx_id)`|`sbx_id`: 沙箱 ID|`Sandbox`|连接已有的沙箱环境|
|`apply_new_sandbox()`|-|`Sandbox`|申请新的沙箱环境（涉及代码权限注入等场景可在子类中重写）|
|`kill_sandbox()`|-|`bool`|销毁沙箱|

#### 沙箱状态检查
|方法|参数|返回值|说明|
|-|-|-|-|
|`is_sandbox_expired()`|-|`bool`|判断沙箱是否已过期|
|`is_sandbox_running()`|-|`bool`|判断沙箱是否正在运行|
|`is_sandbox_valid()`|-|`bool`|判断沙箱是否有效（存在且运行中）|

#### 沙箱时间管理
|方法|参数|返回值|说明|
|-|-|-|-|
|`get_expire_time()`|-|`datetime`|获取沙箱过期时间|
|`get_start_time()`|-|`datetime`|获取沙箱启动时间|
|`get_remaining_time()`|-|`int`|获取剩余时间（秒）|
|`extend_timeout(minutes)`|`minutes`: 延长的分钟数|-|延长沙箱过期时间（沙箱未过期时才有效）|
|`set_timeout(timeout_str)`|`timeout_str`: 过期时间，格式 `"2026-01-01 00:00:00"`|-|直接设置沙箱过期时间（不可小于启动时间）|

#### 文件操作
|方法|参数|返回值|说明|
|-|-|-|-|
|`upload_file_to_sandbox(local_path, remote_path=None)`|`local_path`: 本地路径; `remote_path`: 远程路径（不填则上传到主目录）|`dict` 如 `{"name":"task.py","path":"task.py","type":"file"}`|上传文件到沙箱，目录不存在会自动创建|
|`download_file_from_sandbox(remote_path, local_path)`|`remote_path`: 沙箱文件路径; `local_path`: 本地保存路径|-|从沙箱下载文件到本地（多文件建议先压缩为 zip）|

#### 命令执行
|方法|参数|返回值|说明|
|-|-|-|-|
|`execute_command(command, push_to_testone=False)`|`command`: 命令; `push_to_testone`: 是否推送输出到 TestOne|-|在沙箱中执行命令（后台运行，监听 stdout/stderr）|
|`execute_in_sandbox(command, sbx_id=None, push_to_testone=False)`|`command`: 命令; `sbx_id`: 已有沙箱 ID（不传则申请新沙箱）; `push_to_testone`: 是否推送输出|-|完整的沙箱执行流程：连接/申请沙箱 → `before_execute_in_sandbox` → 执行命令 → `after_execute_in_sandbox`|

#### 输出解析
|方法|参数|说明|
|-|-|-|
|`parse_stdout(std_out, push_to_testone, pust_type="think")`|`std_out`: 标准输出; `push_to_testone`: 是否推送; `pust_type`: 推送类型(think/result)|解析标准输出并按需推送到 TestOne|
|`parse_stderr(std_err, push_to_testone, pust_type="think")`|`std_err`: 错误输出; `push_to_testone`: 是否推送; `pust_type`: 推送类型(think/result)|解析错误输出并按需推送到 TestOne|

#### 生命周期钩子（抽象方法）
|方法|说明|
|-|-|
|`before_execute_in_sandbox()`|**抽象方法**，执行前准备。用于：上传代码、安装依赖、初始化环境等|
|`after_execute_in_sandbox()`|**抽象方法**，执行后处理。用于：清理沙箱、上传结果文件（建议通过 `upload_file_to_bos` 持久化）、发送通知等|

#### 访问链接
|方法|返回值|说明|
|-|-|-|
|`get_sbx_web_ide_url()`|`str`|获取沙箱网页版 IDE 访问链接（端口 8200）|
|`get_sbx_aio_url()`|`str`|获取 AIO（AllInOne）4 合 1 视图链接（Code/Browser/Terminal/Jupyter，端口 8080）|
|`get_sbx_log_url()`|`str`|获取沙箱日志访问链接|

---
