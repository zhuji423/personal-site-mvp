---
title: "v0.9.3（2025-12-11）"
description: "Release log"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🛠️TestOne-SDK\\📁 🚀qep-delivery-tools\\📄 Release log.md"
---
Release log

# v0.9.3（2025-12-11）
* 动态调整右侧首个Tab的工具展示顺序，使用方式详见 [动态调整右侧首个Tab的工具展示顺序](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/rkvAFgeP8NcAx1?t=mention&mt=doc&dt=doc)

# v0.9.2（2025-12-10）
* BaseAiqaAgent 推送工具执行卡片 tool_execute 新增 `status` 可选参数，枚举支持 success | error | warning, 分别对应低风险、高风险、警告三种状态, 默认为空

![](/personal-site-mvp/img/doc-placeholder.svg "")
# v0.9.1（2025-12-08）
* BaseAiqaAgent新增一下方法
    * 支持获取&更新任务描述，详见：[获取/更新任务描述](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/uVd5sW_zzMhzjv?t=mention&mt=doc&dt=doc)
    * 支持获取&更新&删除 任务顶部卡片，详见：[任务顶部悬浮卡](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/jxYECsOHllEYLu?t=mention&mt=doc&dt=doc)


# v0.9.0（2025-12-04）
* 新增如流单聊&群聊场景机器人直接调起Agent，使用方式详见 [Agent接入如流单聊/群聊场景](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/jbgUWpFMpnoW00?t=mention&mt=doc&dt=doc)

# v0.8.9 (2025-11-27)
* **提交hash**: bbc1702
* **需求单**: megqaend-20620, megqaend-20581
* **主要改动**:
    * 推送工具结果函数新增 `response_type` 枚举类型，支持 json（默认）、md、html
    * 推送的COMPONENT类型新增 `expand` 支持对话中默认展开
    * 修改文件: `common/entity/stream_data.py`, `common/enums/response_type_enum.py` (新增), `aiqa_agent/base_aiqa.py`


# v0.8.8 (2025-11-24)
* **提交hash**: 4fe6e55
* **需求单**: megqaend-20603
* **主要改动**:
    * 支持开发者主动删除记忆
    * 修改文件: `aiqa_agent/base_aiqa.py` (+26行)


# v0.8.6 (2025-10-27)
* **提交hash**: 0aecada
* **需求单**: megqaend-20368
* **主要改动**:
    * 【Story】【SDK】支持嵌套Step
    * 修改文件: `__init__.py`, `common/entity/stream_data.py` (2行调整)


# v0.8.5 (2025-09-22)
* **提交hash**: 80f193a
* **需求单**: megqaend-20207
* **主要改动**:
    * 支持对话框直接展示组件数据
    * 修改文件: `aiqa_agent/base_aiqa.py` (8行调整)


# v0.8.4 (2025-09-15)
* **提交hash**: 6b52ead
* **需求单**: megqaend-20137
* **主要改动**:
    * 支持Agent框架直接读写任务短期记忆数据
    * 修改文件: `aiqa_agent/base_aiqa.py` (+62行)


# v0.8.3 (2025-09-09)
* **提交hash**: 99f5b4e
* **需求单**: megqaend-20048
* **主要改动**:
    * 请求参数新增来源字段
    * 修改文件: `common/entity/parameter.py` (+11行)


# 0.8.2
* BaseAiqaAgent 新增以下能力，支持开发者在在Agent执行过程中存取任务级别的临时记忆数据，详见SDK内定义
    * set_memory
    * get_memory
    * get_all_memory


# v0.7.4 (2025-07-30) 
* **提交hash**: 9959ee0
* **需求单**: megqaend-19646
* **主要改动**:
    * 新增Step类型消息组件
    * 支持操作按钮定义&下发
    * 流式会话推送异常管理
    * 修改文件: 6个文件 (+197行, -48行)


# v0.7.3 (2025-07-25)
* **提交hash**: 975a274
* **需求单**: megqaend-19618
* **主要改动**:
    * 支持直接打开如流对话框
    * 修改文件: `infoflow_sidebar/base_card.py` (+22行)


# v0.7.2 (2025-07-21)
* **提交hash**: e66bab3
* **需求单**: megqaend-19580
* **主要改动**:
    * SDK-支持AIQA侧边栏配置工具
    * 新增文件: `aiqa_agent/base_tool_card.py` (28行)
    * 新增文件: `common/entity/aiqa_sidebar_card_parameter.py` (67行)


# v0.7.1 (2025-07-17)
* **提交hash**: 9d71705
* **需求单**: megqaend-19562
* **主要改动**:
    * 支持如流侧边栏调用系统浏览器打开页面
    * 修改文件: `infoflow_sidebar/base_card.py` (+27行)


# v0.7.0 (2025-07-09)
* **提交hash**: ea37fd4
* **需求单**: megqaend-19485
* **主要改动**:
    * 支持通用自定义侧边栏组件SDK


# v0.7.0.dev1 (2025-07-07)
* **提交hash**: 921c386
* **需求单**: megqaend-19464
* **主要改动**:
    * SDK参数解析逻辑升级
    * 侧边栏开发SDK建设
    * 新增模块: `infoflow_sidebar/` (+9个文件)
    * 修改文件: 9个文件 (+162行, -47行)


# ⚠️0.6.0
此版本为不兼容的大升级版本，请参考下发说明升级Agent代码，并在测试环境调试通过以后在上线，否则Agent代码逻辑会有异常

此版本为不兼容的大升级版本，请参考下发说明升级Agent代码，并在测试环境调试通过以后在上线，否则Agent代码逻辑会有异常

此版本为不兼容的大升级版本，请参考下发说明升级Agent代码，并在测试环境调试通过以后在上线，否则Agent代码逻辑会有异常

升级RdSubmitTestReportTool 

升级QaTestReportTool



AIQA表单支持业务控制是否阻塞流程

* ⚠️调整AIQA会话表单下发逻辑，删除 self.push_form_data()
* 升级后，表单结果改为和Aiqa任务执行结束后一起返回

```

def execute():
    # 生成需要下发的表单
    form = self.generate_form()
    
    sug_list = [
        "推荐Query1",
        "推荐Query2",
        "推荐Query3",
        "推荐Query4",
        "推荐Query5",
        "推荐Query6",
        "推荐Query7",
        "推荐Query8",
        "推荐Query9",
        "推荐Query10",
    ]
    return AiqaAgentResult(
        record_id=self.parameter.record_id,
        task_id=self.parameter.task_id,
        status=AiqaAgentStatus.SUCCESS,
        msg="success",
        sug_list=sug_list[],
        input_form=form
    )

def generate_form(self) -> Optional[AiqaInputForm]:
    formList = [
        SingleSelectFormDetail(
            name="singleSelect",
            display_value="是否影响下单流程",
            required=True,
            select_items=["是", "否"],
            default_value=["是"],
            tip="请选择是否影响下单流程，如果涉及下单流程，必须由用户实际回归验证"
        ),
        MultiSelectFormDetail(
            name="multiSelect",
            display_value="可能影响的其他功能",
            required=True,
            select_items=["主页FEED流", "用户登录", "用户注销", "下单流程"],
            default_value=["用户注销"]
        ),
        DigitalFormDetail(
            name="digital",
            display_value="实验用户比例",
            required=True,
            min=20,
            max=100,
            default_value=30
        ),
        DateFormDetail(
            name="date",
            display_value="提测日期",
            required=True,
        ),
        DatetimeFormDetail(
            name="datetime",
            display_value="上线时间",
            required=True,
        ),
        RadioSelectFormDetail(
            name="radio",
            display_value="自主测试",
            select_items=[
                SelectItem(label="是", value=True), SelectItem(label="否", value=True),
            ]
        ),
        UserSelectFormDetail(name="users", display_value="模块负责人", required=False, default_value=["guyouda"]),
    ]


    return AiqaInputForm(
        form_list=formList,
        block=False  # 是否阻塞（不提交表单不允许触发Agent继续执行）
    )

```


# v0.5.4 (2025-06-12)
* **提交hash**: 9b1a80b
* **需求单**: megqaend-19135
* **主要改动**:
    * 优化子任务回调逻辑
    * 修改文件: `aiqa_agent/base_aiqa.py` (+1行)


# v0.5.3 (2025-06-05)
* **提交hash**: cd24517
* **需求单**: megqaend-19192
* **主要改动**:
    * 支持Query动态推荐
    * 修改文件: `common/entity/aiqa_result.py` (+7行)


# v0.5.2 (2025-06-03)
* **提交hash**: bd92460
* **需求单**: megqaend-19147
* **主要改动**:
    * 优化部分类的导入路径
    * 修改文件: 3个__init__.py文件 (+29行, -20行)


# v0.5.2.dev5 (2025-05-28)
* **提交hash**: 98de9ce
* **需求单**: megqaend-19125
* **主要改动**:
    * 根据任务类型限制不合法的工具组件回传


# v0.5.2.dev4 (2025-05-26)
* **提交hash**: abf3bd0
* **需求单**: megqaend-19125
* **主要改动**:
    * 表单处理服务SDK参数解析升级
    * 修改文件: `common/entity/form_parameter.py` (+41行)


# v0.5.2.dev3 (2025-05-23)
* **提交hash**: fd14b88
* **需求单**: megqaend-19022
* **主要改动**:
    * 操作类型新增定时任务触发


# v0.5.2.dev2 (2025-05-22)
* **提交hash**: c85d5be
* **需求单**: megqaend-18990
* **主要改动**:
    * 初始化的时候新增运行环境信息
    * 修改文件: 5个文件 (+75行, -8行)


# v0.5.2.dev1 (2025-05-16)
* **提交hash**: c585fe3
* **需求单**: megqaend-18990
* **主要改动**:
    * 调整测试版本命名规范


# v0.5.2-SNAPSHOT (2025-05-16)
* **提交hash**: 3e84b13
* **需求单**: megqaend-18990
* **主要改动**:
    * AIQA模块初始开发版本


# v0.5.1 (2025-04-24)
* **提交hash**: d6ece43
* **需求单**: megqaend-18799
* **主要改动**:
    * 组件SDK升级,支持配置单选多选属性
    * 修改文件: `common_tools/test_tool/qamate_case_generate_tool.py` (+9行, -5行)


# ⚠️0.5.0
此版本为不兼容的大升级版本，请参考下发说明升级Agent代码，并在测试环境调试通过以后在上线，否则Agent代码逻辑会有异常

此版本为不兼容的大升级版本，请参考下发说明升级Agent代码，并在测试环境调试通过以后在上线，否则Agent代码逻辑会有异常

此版本为不兼容的大升级版本，请参考下发说明升级Agent代码，并在测试环境调试通过以后在上线，否则Agent代码逻辑会有异常



## 1、升级兼容新版本
为了简化部分公共参数的传递逻辑，方便后续调起Agent的时候提供更丰富的上下文数据，本次针对SDK参数传递做了改造，请参考一下方式进行适配



示例代码：[文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/agent/main.py?t=mention&mt=doc&dt=sdk)

## 1.1、在Agent的麒麟策略执行入口升级，通过SDK完成Agent运行环境变量的初始化
```
from qep_delivery_tools import init_agent_run_env

from common.constants import RUN_MODE
from common.constants import KIRIN_TOKEN
from common.constants import KIRIN_USERNAME
from common.constants import TESTONE_TOKEN
from common.constants import TESTONE_USERNAME

def run():
    """
    执行入口
    """
    # 初始化日志
    init_log()

    # 加载参数
    parameter = load_parameter()
    logging.info("parameter: %s", parameter.to_json())
    init_agent_run_env(RUN_MODE, TESTONE_USERNAME, TESTONE_TOKEN, KIRIN_USERNAME, KIRIN_TOKEN, parameter)

```
## 1.2、各阶段的Agent里面，依赖的父类以下函数存在升级
统一删除了参数里面的 username  token  online 字段，业务全局搜索涉及到相关的调用地方删除对应参数即可

|BaseAgent升级前|BaseAgent升级后|
|-|-|
|def callback(self, username: str, token: str, result: ToolResultCallbackRequest, online: bool = True)|def callback(self,result: ToolResultCallbackRequest)|
|def get_execute_result(self, username: str, token: str, icafe_id: str, stage: StageEnum, online: bool = True)|def get_execute_result(self, icafe_id: str, stage: StageEnum)|
|||

|BaseTool 升级前|BaseTool 升级后|
|-|-|
| def get_execute_history(self, username: str, token: str, icafe_id: str, stage: StageEnum, online: bool = True, debug=False)|def get_execute_history(self, icafe_id: str, stage: StageEnum, debug=False)|
|def get_tool_execute_history(self, username: str, token: str, icafe_id: str, stage: StageEnum, tool_list: List[str], online: bool = True, debug=False)|def get_tool_execute_history(self, icafe_id: str, stage: StageEnum, tool_list: List[str], debug=False)|
|||

## 1.3、使用TestOne服务号发消息的地方也删除对应的username  token
|升级前|升级后|
|-|-|
|def send_msg(username: str, token: str, msg: InfoflowMsg):|def send_msg(msg: InfoflowMsg)|



# 0.4.17
* 优化平台统一提供的Go&Js覆盖率工具，获取数据异常场景使用兜底的富文本组件提示异常，避免工具直接崩溃退出导致任务失败



# 0.4.16
* 去除自定义模式调用参数中iCafe卡片列表不能为空的限制

# v0.4.15 (2025-03-07)
* **提交hash**: afe6332
* **需求单**: megqaend-18223
* **主要改动**:
    * 表单处理结果SDK升级,支持控制是否替换
    * SDK升级,支持开发者指定覆盖策略
    * SDK-升级支持表单表格输入组件支持超链类型
    * 修改文件: `common/entity/form_process_result.py` (+7行)


# v0.4.14 (2025-02-17)
* **提交hash**: 9f9e013
* **需求单**: megqaend-18013
* **主要改动**:
    * 质量度模型补充无效卡片异常信息


# v0.4.13 (2025-02-13)
* **提交hash**: 0a5cc5e
* **需求单**: megqaend-18019
* **主要改动**:
    * 支持集成场景使用服务型Tool自定义扩展参数和业务配置参数


# v0.4.12 (2024-12-16)
* **提交hash**: 4b7b5db
* **需求单**: megqaend-17545
* **主要改动**:
    * qep-delivery-tools升级支持解析表单接口debug参数


# v0.4.11 (2024-12-13)
* **提交hash**: 93d4246
* **需求单**: megqaend-17516
* **主要改动**:
    * 优化QaMate Case生成任务ID生成方式


# v0.4.10 (2024-12-04)
* **提交hash**: 3430ba3
* **需求单**: megqaend-17332
* **主要改动**:
    * 质量度模型工具异常支持重试
    * 支持用户指定异常场景默认风险高低


# v0.4.9 (2024-12-03)
* **提交hash**: 763f84d
* **需求单**: megqaend-17231
* **主要改动**:
    * **性能优化**: 风险分析改为异步服务,避免超时异常


# v0.4.8 (2024-11-28)
* **提交hash**: 5d7d13d
* **需求单**: megqaend-17214
* **主要改动**:
    * 新增自主测试风险分析模型2.0
    * 新增QA测试准出拦截工具2.0


# v0.4.7 (2024-11-25)
* **提交hash**: adc50a1
* **需求单**: megqaend-17032
* **主要改动**:
    * 接口用例生成公共Tools新增参数


# v0.4.6 (2024-11-07)
* **提交hash**: 4ccf986
* **需求单**: megqaend-16434
* **主要改动**:
    * 支持服务型Tool传递业务配置参数deptParam


# v0.4.5 (2024-10-30)
* **提交hash**: ec75b44
* **需求单**: megqaend-16601
* **主要改动**:
    * 表单参数解析支持自定义阶段


# v0.4.4 (2024-10-22)
* **提交hash**: 9fb184e
* **需求单**: megqaend-16462
* **主要改动**:
    * 脑图用例生成函数型工具升级为QAMate3.0


# v0.4.3 (2024-09-28)
* **提交hash**: 796572e
* **需求单**: megqaend-16234
* **主要改动**:
    * Go覆盖率不基于base_revision区分
    * 前端展示覆盖率获取时间


# v0.4.2 (2024-09-23)
* **提交hash**: 4602334
* **需求单**: megqaend-16184
* **主要改动**:
    * 自定义阶段公共函数工具sdk
    * 新增: QA测试报告工具/客户端代码函数覆盖率工具/内置Bug工具/QaMate测试用例工具


# v0.4.1 (2024-09-20)
* **提交hash**: 11758f7
* **需求单**: megqaend-16122
* **主要改动**:
    * 自定义agent相关sdk升级


# v0.4.0 (2024-08-23)
* **提交hash**: 1a87b8f
* **需求单**: megqaend-15770
* **主要改动**:
    * 公共工具SDK升级-支持统一质量度模型展示更多策略数据
    * **重构**: 质量度模型命名升级 ClientRiskModel→RiskModel


# v0.3.9 (2024-08-22)
* **提交hash**: c05f23f
* **需求单**: megqaend-15721
* **主要改动**:
    * PHP/GO/JS覆盖率展示-富文本参数升级


# v0.3.8 (2024-08-21)
* **提交hash**: a0ad260
* **需求单**: megqaend-15683
* **主要改动**:
    * 获取工具执行历史记录,需要默认过滤调试结果
    * SDK调用NewCaseUtils新增警告提示,方便后续下线


# v0.3.7 (2024-08-21)
* **提交hash**: 9e3f3bc
* **需求单**: megqaend-15721
* **主要改动**:
    * PHP/GO/JS覆盖率展示-富文本参数升级


# v0.3.6 (2024-08-19)
* **提交hash**: 7a09e3a
* **需求单**: megqaend-15644
* **主要改动**:
    * PHP/GO/JS覆盖率展示-表格版增加story覆盖率和分支覆盖率的筛选字段


# v0.3.5 (2024-08-06)
* **提交hash**: f2dd0a5
* **需求单**: megqaend-15334
* **主要改动**:
    * 支持用户使用TestOne服务号发送消息
    * 支持用户选择(USER_SELECT)/日期(DATE)/日期时间(DATE_TIME)类型
    * 支持表单输入项禁用


# v0.3.4 (2024-08-01)
* **提交hash**: b9d0cc6
* **需求单**: megqaend-15323
* **主要改动**:
    * 服务型tool支持阶段流转控制


# v0.3.3 (2024-07-26)
* **提交hash**: 549842f
* **需求单**: megqaend-15265
* **主要改动**:
    * **架构升级**: SDK升级,支持业务自定义参数解析


# v0.3.2 (2024-07-25)
* **提交hash**: 371c3e9
* **需求单**: MEG-qa-ep-58804
* **主要改动**:
    * JS语言的覆盖率,增加icafeId参数


# v0.3.1 (2024-07-23)
* **提交hash**: 2041c17
* **需求单**: megqaend-15309
* **主要改动**:
    * SDK升级,新增默认兜底的需求详情工具
    * 支持风险识别矩阵能力接入


# v0.3.0 (2024-07-19)
* **提交hash**: 4c4160e
* **需求单**: megqaend-15259
* **主要改动**:
    * 数据SDK支持新建iCafe卡片的时候绑定父卡片/关联/评论卡片


# v0.2.9 (2024-07-18)
* **提交hash**: 2a57fc5
* **需求单**: megqaend-15240
* **主要改动**:
    * 支持Agent&Tool获取历史执行结果
    * 辅助业务策略根据历史结果动态决定本次执行逻辑


# v0.2.8 (2024-07-11) 
* **提交hash**: 71f8437
* **需求单**: megqaend-15080
* **主要改动**:
    * **安全加固**: SDK日志升级,避免直接打印输出用户的token信息
    * SDK升级新增表单提交数据参数规范定义


# v0.2.7 (2024-07-11)
* **提交hash**: 900d4c2
* **需求单**: megqaend-15083
* **主要改动**:
    * Agent调用平台Header添加相关SDK的版本信息
    * 方便后续统计以及推动业务升级


# v0.2.6 (2024-07-08)
* **提交hash**: 3e4fa86
* **需求单**: MEG-qa-ep-58577
* **主要改动**:
    * 代码覆盖率展示工具-Php/Go/JS等,优化异常边界条件,修复判空条件


# v0.2.5 (2024-07-08)
* **提交hash**: 2cf660a
* **需求单**: MEG-qa-ep-58577
* **主要改动**:
    * 代码覆盖率展示工具-Php/Go/JS等,优化异常边界条件


# v0.2.4 (2024-07-07)
* **提交hash**: b1691e3
* **需求单**: MEG-qa-ep-58577
* **主要改动**:
    * 代码覆盖率展示工具-Php/Go/JS等,优化异常边界条件


# v0.2.3 (2024-07-04)
* **提交hash**: 01a4949
* **需求单**: megqaend-14973
* **主要改动**:
    * covTableTool的报告地址改为富文本渲染


# v0.2.2 (2024-07-04)
* **提交hash**: 65c7cc4
* **需求单**: megqaend-14973
* **主要改动**:
    * covTableTool的报告地址改为富文本渲染


# v0.2.1 (2024-07-04)
* **提交hash**: 38ce89a
* **需求单**: megqaend-14973
* **主要改动**:
    * covTableTool的报告地址改为富文本渲染


# v0.2.0 (2024-06-26) 
* **提交hash**: b5115e9
* **需求单**: megqaend-14692
* **主要改动**:
    * **架构升级**: 集成Agent依赖SDK开发
    * 新增IntegrationBaseAgent基类


# v0.1.3 (2024-06-27)
* **提交hash**: 5f8a3cf
* **需求单**: MEG-qa-ep-58514
* **主要改动**:
    * 服务端代码变更信息获取公共工具-表格展示


# v0.1.2 (2024-06-27)
* **提交hash**: dfc741f
* **需求单**: MEG-qa-ep-58514
* **主要改动**:
    * 服务端代码变更信息获取公共工具-表格展示


# v0.1.1 (2024-06-11)
* **提交hash**: 78efb24
* **需求单**: megqaend-14693
* **主要改动**:
    * 优化URL内嵌组件SDK异常提示


# v0.1.0 (2024-06-05)
* **提交hash**: debc9be
* **需求单**: megqaend-14365
* **主要改动**:
    * URL内嵌组件,支持内嵌多个页面,工具内顶部tab切换
    * 获取UT/SA问题列表公共工具


# v0.0.9 (2024-05-30)
* **提交hash**: a30abbb
* **需求单**: megqaend-14519
* **主要改动**:
    * 联调阶段Agent SDK发布


# v0.0.8 (2024-05-29)
* **提交hash**: 855fb5d
* **需求单**: megqaend-14519
* **主要改动**:
    * QTEST平台质量度模型工具迁移


# v0.0.7 (2024-05-10)
* **提交hash**: 21f9acd
* **需求单**: megqaend-14287
* **主要改动**:
    * 公共工具sdk发版0.0.7: 新增QAMate接口用例生成工具


# v0.0.6 (2024-05-08)
* **提交hash**: 028a0d5
* **需求单**: megqaend-14212
* **主要改动**:
    * Agent输出协议升级,支持用户指定是否自动进入下一阶段


# v0.0.5 (2024-04-26)
* **提交hash**: 0f24576
* **需求单**: megqaend-14197
* **主要改动**:
    * tools发布版本0.0.5
    * 新增状态[执行中]
    * 区分QA测试准出拦截工具和客户端质量度风险模型工具的工具id


# v0.0.4 (2024-04-18)
* **提交hash**: 4231eaf
* **需求单**: megqaend-14155
* **主要改动**:
    * 解析回调结果


# v0.0.3 (2024-04-15) 
* **提交hash**: c7df197
* **需求单**: megqaend-14133
* **主要改动**:
    * 需求Agent公共工具&输入输出规范统一发布成SDK
    * BaseAgent/BaseTool基类建立


# v0.0.2 (2024-01-11)
* **提交hash**: c3a2a6a
* **需求单**: MEG-qa-ep-56291
* **主要改动**:
    * 提示词工程,EE侧要升级,对应调整
    * 完善提示,同时解决包依赖问题


# v0.0.1 (2023-12-28) 
* **提交hash**: 8fe262e
* **需求单**: MEG-qa-ep-56520
* **主要改动**:
    * 智能交付引擎-代码风险tool示例
    * SDK框架搭建

