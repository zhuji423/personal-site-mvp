---
title: "1、启动前须知"
description: "⏭️需求&集成&自定义阶段Agent开发文档"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档.md"
---
⏭️需求&集成&自定义阶段Agent开发文档

# 1、启动前须知
## 1.1、基础概念对齐
* 阶段：需求生命周期的一个阶段，目前分成以下几种
    * 需求阶段：需求导入平台自动进入需求阶段
    * 开发阶段：需求卡片变为 “开发中”，平台自动进入开发阶段，调起开发阶段Agent
    * 提测准入：需求处于开发阶段自动点亮，RD开发完成以后，可以选择触发提测准入Agent
    * 测试阶段：RD需求提测准入通过，发送提测报告后自动进入，调起测试阶段Agent
    * 联调阶段：如果需求需要联调，会在详情页展示联调阶段
    * 测试准出：需求处于测试阶段的时候点亮，可点击 测试准出 按钮触发准出Agent
    * 测试完成：需求准出通过以后自动进入该阶段，调起测试完成阶段Agent


![](/personal-site-mvp/img/doc-placeholder.svg "")
* 组件：在需求的每个阶段，平台会提供不同的能力，展示不同的数据。这些一个个独立的功能，都是由一个前端都是进行渲染展示和交互的组件。
* Agent：由业务线自主开发，负责特定阶段的完整交付工作，含风险洞察（基于当前阶段的变更数据，洞察是否有兼容性、稳定性等各类风险，以及给出风险高低）、测试分发/执行（基于风险洞察规划各类测试工具，如QAMate、环境搭建等，并触发执行）、风险决策（是否准出不通过，卡住该阶段不能跳转到下一阶段）等，Agent由两大块组成：
    * 调度层：平台调起业务Agent以后，Agent需要结合平台的触发参数，决定本次需要调起的具体工具列表。工具列表可以是最初一次性选取，也可以在执行过程中根据风险洞察或者测试分发的具体情况动态选取，调度层决定每个工具是并行还是串行执行。每个工具执行完成以后，建议及时将结果通知平台。
    * 工具集：业务自己开发的，或者第三方提供的，供业务选择执行的一系列能力集合。

* 工具：一个工具，也是一个具体的能力。比如兼容性风险分析工具、跨业务风险分析工具、环境搭建工具、Case推荐工具、自动化任务执行工具、准出判定工具等。每个工具执行完成后，都会返回一个前端组件ID以及组件的数据，用于前端展示其执行结果。为了方便管理维护以及前端汇总展示，会把工具分成以下类型（这个分类目前只影响前端的数据聚合展示，不影响功能）：
    * 定制数据：用于展示一些平台没有支持的业务需求定制化数据，比如卡片的一些特有字段信息。
    * 风险洞察：洞察变更风险的工具，用于从各个维度，分析风险高低，具体风险内容是什么。
    * 测试工具：辅助测试的工具，例如 Xmonkey/ITP/LazyOne自动化任务、EOS/XSTP/EOS测试环境部署、测试Case推荐、iPipe流水线等类型
    * 风险决策：用于判断需求是否能够通过当前阶段，涉及到平台的流程卡点，如果不通过会阻塞在当前阶段。提测准入、测试阶段、测试准出阶段必须
    * 报告信息：用于展示需求的提测报告  测试报告等


## 
## 1.2 示例代码
### 1.2.1、背景
为了方便各业务同学自行开发策略，在此提供示例Demo，大家可在此基础上按照业务实际需求定制化开发即可

### 1.2.2、示例代码下载
* iCode地址：[文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/tree/master/agent?t=mention&mt=doc&dt=sdk)
* 注意：由于该代码库作为平台各种公开示例代码的统一管理位置，下面会包含各种公开的示例代码。下载后 agent 目录才是当前示例代码的根目录, 使用pycharm等IDE打开的时候，选择 agent目录，而不是qep_delivery_open_source目录



### 1.2.3、环境准备
IDE：建议使用Pycharm （不建议使用VSCode(资深玩家例外)）

> 别再问我Pycharm怎么破解  我不会  我用的是社区版 不需要破解
> 下载地址：[https://www.jetbrains.com.cn/pycharm/download/?section=mac](https://www.jetbrains.com.cn/pycharm/download/?section=mac)   选择社区版(PyCharm Community Edition) 


Python版本：    3.11 （目前麒麟仅支持3.11）

> 能不能支持python2：目前不支持，未来也没有可能支持。放弃吧，别挣扎了，往前看
> Mac版下载地址：[https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg](https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg)
> 更多版本下载：[https://www.python.org/downloads/](https://www.python.org/downloads/)


依赖安装命令： pip3 install -r requirements.txt -U --index-url [http://pip.baidu.com/root/baidu/+simple/](http://pip.baidu.com/root/baidu/+simple/) --trusted-host pip.baidu.com  --no-cache-dir

> 当前的直接依赖库包括3个
> * qep-delivery-data                各种需求相关的基础数据获取的SDK封装  包括 需求 Case  变更代码  Bug  排期  等等 详见  [📦qep-delivery-data](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI?t=mention&mt=doc&dt=doc)
> * qep-delivery-component      Agent返回数据结果的前端组件化SDK，用于封装用户结果对应的前端展示样式。详见文档附录部分
> * qep-delivery-tools                Agent&Tool输入输出规范定义，以及公共Tool的封装
> 


配置更新：打开 common/constants.py 文件, 

> 更新 TESTONE_USERNAME  TESTONE_TOKEN  KIRIN_USERNAME  KIRIN_TOKEN
```
# 替换你在TestOne平台的用户账号信息, 用于Agent执行结果回调通知平台。获取方式 https://testone.baidu-int.com/api/getToken
TESTONE_USERNAME = 'xxx'
TESTONE_TOKEN = 'xxxxxx'

# 替换你在kirin平台的用户名和token，用于回调麒麟，调用麒麟其他策略。获取方式 https://kirin.baidu-int.com/#/home 
KIRIN_USERNAME = "xxx"
KIRIN_TOKEN = "xxx"
```
### 1.2.4、示例代码解读
#### 1.2.4.1、代码结构介绍
├── agents                      各个阶段的Agent存放位置  

│   ├── integration_exit_test_stage_agent.py                集成-准出阶段(stage=12)

│   ├── integration_core_case_test_stage_agent.py     集成-核心用例回归阶段(stage=11)

│   ├── integration_exploratory_test_stage_agent.py   集成-ET测试阶段(stage=10)

│   ├── integration_new_story_test_stage_agent.py    集成-新需求测试阶段(stage=9)

│   ├── integration_entry_test_stage_agent.py            集成-准入阶段(stage=8)

│   ├── qa_joint_test_stage_agent.py            联调测试(stage=7)阶段的处理Agent                                              

│   ├── qa_test_finish_stage_agent.py          测试完成(stage=6)阶段的处理Agent

│   ├── qa_test_intercept_stage_agent.py     测试准出(stage=5)阶段的处理Agent

│   ├── qa_test_stage_agent.py                     QA测试(stage=4)阶段的处理Agent

│   ├── rd_submit_test_stage_agent.py         提测准入(stage=3)阶段的处理Agent            

│   └── rd_dev_stage_agent.py                      RD开发(stage=2)阶段的处理Agent

├── build.sh          编译打包脚本

├── ci.yml             代码库流水线编译配置

├── common         一些公共的配置

│   ├── __init__.py

│   ├── constants.py                        账号密码 接口地址等常量定义

│   └── testone_utils.py                    TestOne平台常用的数据查询获取工具类

├── main.py                  策略执行入口

├── requirements.txt     依赖管理

├── run_all_unittest_case.sh                        全量执行单测Case

├── tests                                                       单测用例管理

│   ├── ......

├── tools                                                       所有的工具管理

     ├── qa_test_intercept_tool.py                  QA测试准出拦截工具（自己完善策略）

     └──  rd_submittest_intercept_tool.py        RD提测准入拦截工具（自己完善策略）



#### 1.2.4.2、策略运行流程
以RD提测准入阶段Agent为例,

1. 日志初始化  

```
init_log()
```
2. 获取请求参数

```
# 该方法会根据所属的阶段返回两种类型的参数  Parameter:需求维度Agent触发参数   IntegrationParameter: 集成维度的Agent触发参数
# 用户无需关注，底层SDK会自动处理
parameter = load_parameter()  
```
```
# 需求维度Agent触发参数
class Parameter(BaseObject):
    """
    请求参数统一格式
    """

    def __init__(self, kirin_task_id: int, engine_task_id: str, dept_id: int, sub_direction: str, icafe_id: str,
                 stage: int, operator: str, operation_type: int, tool_id: str = None, debug: bool = False):
        """
        初始化
        :param kirin_task_id: 麒麟平台生成的唯一任务ID，必填
        :param engine_task_id: 引擎生成的唯一任务ID，Agent执行完成后，使用此任务ID进行回调，必填
        :param dept_id: 需求所属的业务线ID，必填
        :param sub_direction: 需求所属的业务线子方向，必填
        :param icafe_id: 需求卡片ID，必填
        :param stage: 触发任务的阶段，必填
        :param operator: 触发人，必填
        :param operation_type: 操作类型，必填（首次进入该阶段需要完整触发agent中的所有工具，填0；用户指定agent中的某个工具更新，填1）
        :param tool_id: 用户指定触发的工具ID，operation_type=1时必填
        :param debug: 是否为调试请求，默认False. 如果开发者希望对调试的任务和正式任务进行区别处理,可以基于此字段区分,否则忽略即可<br>
                      True:  开发者在平台进行调试时的请求参数<br>
                      False: 平台正式请求参数
        """
        self.kirin_task_id: int = self.attribute_verify(kirin_task_id, "kirin_task_id", int)

        self.engine_task_id: str = self.attribute_verify(engine_task_id, "engine_task_id", str)

        self.dept_id: int = self.attribute_verify(dept_id, "dept_id", int)

        self.sub_direction: str = self.attribute_verify(sub_direction, "sub_direction", str)

        self.attribute_verify(icafe_id, "icafe_id", str)

        self.icafe_ids: List[str] = icafe_id.split(',')

        self.attribute_verify(stage, "stage", int)
        self.stage: StageEnum = get_stage_enum(stage)

        self.operator: str = self.attribute_verify(operator, "operator", str)

        self.attribute_verify(operation_type, "operation_type", int)
        self.operation_type: OperateTypeEnum = get_operate_type_enum(operation_type)

        self.tool_id: str = self.attribute_verify(tool_id, "tool_id", str)
        
        self.debug: bool = self.attribute_verify(debug, "debug", bool, False)

        # 若operation_type为1，则tool_id必填
        if self.operation_type == OperateTypeEnum.SPECIFY_TRIGGER and not self.tool_id:
            raise Exception(f'Parameter.tool_id must be str when operation_type is 1')


# 集成维度Agent的触发参数
class IntegrationParameter(BaseObject):
    """
    集成Agent请求参数统一格式
    """

    def __init__(self, kirin_task_id: int, engine_task_id: str, dept_id: int, sub_direction: str,
                 client: str, version: str, icafe_id_list: List[str], stage: int, operator: str,
                 operation_type: int, tool_id: str = None, debug: bool = False):
        """
        初始化
        :param kirin_task_id: 麒麟平台生成的唯一任务ID，必填
        :param engine_task_id: 引擎生成的唯一任务ID，Agent执行完成后，使用此任务ID进行回调，必填
        :param dept_id: 需求所属的业务线ID，必填
        :param sub_direction: 需求所属的业务线子方向，必填
        :param client: 集成版本的端类型
        :param version: 集成版本的版本号
        :param icafe_id_list: 当前集成版本的所有卡片列表
        :param stage: 触发任务的阶段，必填
        :param operator: 触发人，必填
        :param operation_type: 操作类型，必填（首次进入该阶段需要完整触发agent中的所有工具，填0；用户指定agent中的某个工具更新，填1）
        :param tool_id: 用户指定触发的工具ID，operation_type=1时必填
        :param debug: 是否为调试请求，默认False. 如果开发者希望对调试的任务和正式任务进行区别处理,可以基于此字段区分,否则忽略即可
                      True:  开发者在平台进行调试时的请求参数
                      False: 平台正式请求参数
        """
        self.kirin_task_id: int = self.attribute_verify(kirin_task_id, "kirin_task_id", int)
        self.engine_task_id: str = self.attribute_verify(engine_task_id, "engine_task_id", str)
        self.dept_id: int = self.attribute_verify(dept_id, "dept_id", int)
        self.sub_direction: str = self.attribute_verify(sub_direction, "sub_direction", str)
        self.client = self.attribute_verify(client, "client", str)
        self.version = self.attribute_verify(version, "version", str)

        self.attribute_verify(stage, "stage", int)
        self.stage: StageEnum = get_stage_enum(stage)

        self.operator: str = self.attribute_verify(operator, "operator", str)

        self.attribute_verify(operation_type, "operation_type", int)
        self.operation_type: OperateTypeEnum = get_operate_type_enum(operation_type)

        self.tool_id: str = self.attribute_verify(tool_id, "tool_id", str)

        self.icafe_id_list = self.attribute_verify(icafe_id_list, 'icafe_id_list', List, [])
        if not self.icafe_id_list:
            raise Exception(f'Parameter.icafe_id_list must be List and not empty')

        self.debug: bool = self.attribute_verify(debug, "debug", bool, False)

        # 若operation_type为1，则tool_id必填
        if self.operation_type == OperateTypeEnum.SPECIFY_TRIGGER and not self.tool_id:
            raise Exception(f'Parameter.tool_id must be str when operation_type is 1')
```
3. 根据请求参数决定当前阶段应该调起那个Agent

```
 agent = self.agents.get(self.parameter.stage)
```
4. 调起Agent执行

```
tools = agent.execute()
```
5. Agent执行顺序
    1. 调用本次选择出来的工具  
        1. 调用工具执行
        2. 通知平台工具执行结果(可以全部一次性通知，也可部分执行完成多次通知)

    2. 汇总最终风险结论（平台会根据该结论进行流程的管控，应用在提测准入、测试阶段、测试准出的流转中）


```
 def execute(self) -> AgentResult:
        """
        Agent 执行工具的入口
        """
        logging.info("agent开始执行")
        # 当前阶段所有的可用工具
        all_tools = [
            RdSubmitTestReport(),  # 提测报告工具
            RdSubmitTestInterceptTool()  # 提测拦截工具
        ]

        logging.info("agent开始选择工具")
        tools = []
        if self.parameter.operation_type == OperateTypeEnum.FULL_TRIGGER:
            # TODO 分析本次请求的需求，该调起哪些工具
            tools = all_tools
        elif self.parameter.operation_type == OperateTypeEnum.SPECIFY_TRIGGER:
            # 指定工具调起
            for tool in all_tools:
                if tool.tool_id == self.parameter.tool_id:
                    tools.append(tool)
                    break
            if len(tools) == 0:
                # TODO 根据请求参数以及需求的特征，决定需要执行哪些工具（如果暂时做不到这么详细，可以全部执行即可，后续完善）
                pass
        logging.info(f"本次调用的工具：{tools}")

        callback_request = ToolResultCallbackRequest(self.parameter.engine_task_id, [])
        has_risk = False
        risk_summary = "低风险，提测准入通过"

        for tool in tools:
            tool_result = tool.execute(self.parameter)
            if tool_result.high_risk:
                has_risk = True
                risk_summary = tool_result.risk_summary

            callback_request.add_tool_result(tool_result)

        # tool全部执行完成，统一回调
        self.callback(callback_request)

        return AgentResult(self.parameter.engine_task_id, has_risk, risk_summary)
```
6. Agent执行结果回调麒麟

```
KirinUtils(KIRIN_USERNAME, KIRIN_TOKEN).callback_kirin(parameter.kirin_task_id, agent_result.to_json(camel_case=True), sys.argv[3])
```
#### 1.2.4.3、Agent执行流程说明
一个阶段，对应一个Agent，这个Agent主要负责以下工作：

* 按照：洞察 -> 规划 -> 执行 -> 决策的思路，串联风险洞察（基于变更代码、需求描述等，定性/定量评估本次变更的风险维度和大小）、测试任务规划（基于风险洞察，选取对应的测试手段）、测试任务执行（串/并行的触发各种工具，如X-Monkey、自动化用例、流水线任务-固定/智能构建/动态等）、测试决策（当前阶段是否可通过，会影响阶段流转等相关动作）。
* 洞察、规划、执行、决策过程中，会调起很多工具支撑，这些工具的结果，可以一次性返回平台，也可以按需分批返回。
* Agent执行到最后，综合各个工具的执行数据，综合决定high_risk、risk_summary字段信息，判断是否该阶段通过还是阻塞。



当前已实现RdDevStageAgent、RdSubmitTestStageAgent、QaTestStageAgent、QaTestInterceptStageAgent、QaTestFinishStageAgent，每个测试阶段都对应一个agent，用户可基于业务需求，修改对应测试阶段的agent中的业务逻辑

执行agent：execute(self) -> AgentResult

① 当operation_type=0时，表示首次进入该测试阶段（该agent），返回首次进入该阶段时待执行的tool列表

用户可基于业务需求确定tool列表，比如基于需求的类型对agent中注册的所有tool进行筛选

② 当operation_type=1时，搭配参数tool_id，表示重新执行该测试阶段（该agent）中的某个指定tool，tool_id是tool注册在平台的唯一id

用户基于业务需求新增tool时，需要先在平台注册，否则可能导致无法调起tool

③agent开始执行时，用户可按照业务需求，并行 或 串行待执行的多个tool

④tool执行完毕后，用户可按照业务需求，待所有tool执行结束后一次性返回所有tool的执行结果给引擎 或 按照tool执行时长分批返回tool的执行结果给引擎，结果需封装成AgentResult， callback(self, result: AgentResult)

⑤tool列表执行结束后，返回所有tool的执行结果给kirin服务入口模块，用于kirin服务入口模块确定agent是否执行结束

#### 1.2.4.4、工具执行流程说明
Tool即一个工具，也是一个具体的能力。比如兼容性风险分析工具、跨业务风险分析工具、环境搭建工具、Case推荐工具、自动化任务执行工具、准出判定工具等。

1）tool执行：execute(self, parameter: Parameter) -> ToolResult

① 用户可基于业务需求，编写tool执行逻辑

② tool执行结果需要进行组件化，用于后续平台前端展示tool结果，封装成ToolResult类型后返回给agents模块



说明：如果需要新增一个Tool，工具的开发流程如下：

* 在平台注册需要实现的这个工具相关信息（工具名、工具类型、工具功能描述等），获取平台分配的工具ID。（工具注册管理地址：[https://testone.baidu-int.com/#/testone/engine/tool](https://testone.baidu-int.com/#/testone/engine/tool) ）
* 根据业务需求，实现需要开发的功能，这个类需要继承自BaseTool
* 将结果按照自己希望的展示的前端样式进行结果的封装，具体相关的组件使用**参考本文档附录部分**
    * 说明：如果组件设计中，没有大家需要的组件类型，联系顾友达（guyouda）咨询新组件开发方案和支持




# 2、Agent开发
下面以自己开发一个用于在测试阶段，展示需求部分字段的功能为例，介绍如何自己开发这个功能

> 对于智能交付平台，每一个功能都会被叫做一个工具(Tool，对应代码tools 下的每一个 xxxTool类)
> 所以要开发这个功能，就需要自己开发实现一个Tool


## 2.1、新增一个Tool
### 2.1.1、Tool注册
为了后续对每一个工具的统计，功能提示，异常报警等，每个工具都需要在平台注册，使用平台分配的唯一标识

注册地址：[https://testone.baidu-int.com/#/testone/engine/tool](https://testone.baidu-int.com/#/testone/engine/tool)

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 2.1.2、Tool代码逻辑实现
如果策略需要依赖需求的各种数据，获取方式可参考 [📦qep-delivery-data](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI?t=mention&mt=doc&dt=doc)

如果数据SDK提供的数据不足，提需（咨询[@顾友达](https://ku.baidu-int.com?t=mention&mt=contact&id=3670aa80-247d-11ef-8306-39d203cb0111)[@汪世涛](https://ku.baidu-int.com?t=mention&mt=contact&id=3c0ea780-247d-11ef-8306-39d203cb0111)）或者共建

在tools 文件夹下新增一个工具   show_story_info_tool.py  实现需要的功能，具体代码以及说明如下代码

```
# !/usr/bin/python3

# -*- coding: utf-8 -*-

"""
@author: GuYouda
@date:   2024/3/20
@desc:   示例代码
"""

from qep_delivery_component import ComponentOperateConfig
from qep_delivery_component import LabelConfig
from qep_delivery_component import LabelTypeEnum
from qep_delivery_component import TableComponent
from qep_delivery_component import TableDetail
from qep_delivery_component import TableHead

from qep_delivery_tools import Parameter
from qep_delivery_tools import ToolResult
from qep_delivery_tools import BaseTool


class ShowStoryInfoTool(BaseTool):
    """
    展示需求信息（示例代码，用于展示一些平台不支持的定制字段信息）
    """

    def __init__(self):
        # TODO 工具初始化， 设置工具的ID。为了后续对每一个工具的统计，功能提示，异常报警等，
        # 每个工具都需要在平台注册，使用平台分配的唯一标识
        # 注册地址：https://testone.baidu-int.com/#/testone/engine/tool
        super().__init__("xxxxxxxxx")

    def execute(self, parameter: Parameter) -> ToolResult:

        # 设置表头 (每一列的标题，以及从数据对象的那个字段取值)
        table_head = [
            TableHead(data_index="kirin_task_id", title="麒麟任务ID", width=100),
            TableHead(data_index="engine_task_id", title="引擎任务ID", type=TableColumnTypeEnum.TEXT, width=150),
            TableHead(data_index="icafe_rich_text", title="富文本", type=TableColumnTypeEnum.RICH_TEXT, width=300),
            TableHead(data_index="icafe_url_blank", title="超链-新页面", type=TableColumnTypeEnum.URL),
            TableHead(data_index="icafe_url_popup", title="超链-弹窗", type=TableColumnTypeEnum.URL),
        ]
        table_body = [
            {
                "kirin_task_id": 12345,
                "engine_task_id": "xxx-xxx",
                "icafe_rich_text": "<font color='green'>绿色的文字</font>",
                "icafe_url_blank": TableInnerUrl(
                    name="链接-新页面打开",
                    url='https://console.cloud.baidu-int.com',
                    target='_blank'
                ),
                "icafe_url_popup": TableInnerUrl(
                    name="链接-浮层打开",
                    url='https://console.cloud.baidu-int.com',
                    target='_popup'
                ),

            },
            {
                "kirin_task_id": 56789,
                "engine_task_id": "yyy-yyy",
                "icafe_rich_text": "<font color='red'>红色的文字;  </font> <font>超链接："
                                   "</font><a href='https://console.cloud.baidu-int.com' target='_blank'>点我打开</a>",
                "icafe_url_blank": TableInnerUrl(
                    name="链接-新页面打开",
                    url='https://console.cloud.baidu-int.com',
                    target='_blank'
                ),
                "icafe_url_popup": TableInnerUrl(
                    name="链接-浮层打开",
                    url='https://console.cloud.baidu-int.com',
                    target='_popup'
                ),
            }
        ]

        table_detail = TableDetail(table_head, table_body)

        # 封装前端组件
        component = TableComponent(  # 表格组件
            component_operate_config=ComponentOperateConfig(),  # 组件操作配置，使用默认值
            component_data=table_detail  # 组件数据
        )

        return ToolResult(self.tool_id, component)

```
### 2.1.3、Tool单测用例编写
补充单测用例，确定当前工具能够正常执行。在tests目录下新增测试用例 test_show_story_info_tool.py

```
# !/usr/bin/python3

# -*- coding: utf-8 -*-

"""
@author: GuYouda
@date:   2024/2/27
@desc:   
"""
import logging
import unittest

from qep_delivery_data import init_log

from qep_delivery_tools import StageEnum
from qep_delivery_tools import Parameter
from tools.show_story_info_tool import ShowStoryInfoTool


class XxxToolTestCase(unittest.TestCase):

    def setUp(self):
        init_log()

    def test_something(self):
        param = Parameter(
            123456, "ef7d078b-1f6a-4d75-9485-455c32afc332",
            26127, "工作台", "megqaend-13479", StageEnum.RD_DEV_STAGE.get_code(), "guyouda", 0
        )

        result = ShowStoryInfoTool().execute(param)
        logging.info(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()

```
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 2.1.4、Agent代码修改
由于这个Tool需要在测试阶段展示，所以需要修改测试阶段的Agent，qa_test_stage_agent.py 添加这个功能

![引入新增的工具](/personal-site-mvp/img/doc-placeholder.svg "引入新增的工具")
![放在需要调起的工具集中](/personal-site-mvp/img/doc-placeholder.svg "放在需要调起的工具集中")
# 3、Agent服务部署
## 3.1、单测
* 执行命令 sh run_all_unittest_case.sh 

> * 该命令会自动获取tests目录下所有单测用例并执行，确保打包前所有单测执行通过
> * 建议后续把相关流程整合到流水线
> 
## 3.2、编译打包
* 执行命令  sh build.sh   (后续自己按需优化build.sh的代码逻辑)

注意:

* qep_delivery_tools, qep_delivery_component 两个依赖包一定要严格按照requirements.txt的版本号和Agent代码打包到一起，避免麒麟公共环境的版本被其他人升降级导致的Agent执行异常问题
* 不建议手动打包
* 打包成功后，会生成 output/agent.zip这个文件

## 3.3、注册到麒麟
> 麒麟平台的使用指南参考相关文档，或者加群1650161咨询 
进入麒麟服务注册页面 [https://kirin.baidu-int.com/#/q-market/0/list/domain-all](https://kirin.baidu-int.com/#/q-market/0/list/domain-all)

选择 添加服务

![](/personal-site-mvp/img/doc-placeholder.svg "")


执行命令  python3.11 main.py

工作目录   ./agent

调用方式：根据自己Agent执行耗时决定同步异步(后续可以更改) 

> 如果能在10s内执行完毕，建议同步。异步服务需要排队，排队时长受各种因素影响，短则毫秒级，长则分钟级
超时时间：根据自己Agent执行耗时决定

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 3.4、审核申请
* Agent部署后，发起审核前，需要先调试能够执行成功。可使用以下参数，可以根据需要修改对应字段

```
{
    "deptId": 26674,
    "subDirection": "工作台",
    "stage": 2,
    "icafeId": "youtrack-754",
    "engineTaskId": "1f20731e-9349-411f-a8cb-4bf556b76c23",
    "operator": "guyouda",
    "operationType": 0,
    "toolId": null,
    "debug": true
}
```
* 调试执行成功以后，点击发起审核

> 麒麟任务执行成功即可，
> * 日志里面显示  code=605  msg=Agent当前状态不允许回调忽略（由于这是个随意构造的参数，对应的Agent任务已经执行完成，所以不允许再次回调更新）
> * 如果日志显示  code=302  msg=username或者token错误，联系[@顾友达](https://ku.baidu-int.com?t=mention&mt=contact&id=7c0235c0-fb27-11ee-8897-231df4a0d723)给添加权限
> 
* 联系kirin同学审核即可 麒麟群 1650161  审核同学[@侯澄](https://ku.baidu-int.com?t=mention&mt=contact&id=034f6550-8a91-11ee-a8ce-b39ed4b78ba5)

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 4、Agent测试验证
## 4.1、Agent注册
所有的Agent都需要在平台注册以后，平台才能调起

注册地址：[https://testone.baidu-int.com/#/testone/engine/agent](https://testone.baidu-int.com/#/testone/engine/agent)

![](/personal-site-mvp/img/doc-placeholder.svg "")
需要的参数如下：

* Agent名字：自己的Agent的名字，最好和阶段&功能对应上
* 阶段：Agent是处理需求哪个阶段的
* 负责人：Agent的负责人，支持多个。方便平台知道每个Agent谁负责的，以及Agent执行异常的时候及时发送消息报警
* 超时时间：Agent最长多久可以执行完成，如果超时，默认执行失败
* 是否异步：和自己部署的麒麟策略保持一致，否则调用会出现异常
* 接口地址：麒麟服务的接口地址，获取方式如下

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 简介：详细介绍自己的Agent的具体能力

## 4.2、Agent调试
调试页面，可以按照需要自行构造参数，调试流量不会影响需求在平台的数据和状态

Agent在真正配置到业务线试用前，需要先在平台调试确认符合预期，避免直接上线影响业务需求流程

调试流程如下：

* 点击 “在线调试”

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 根据需要选择参数
    * 业务线：下拉选择，单选，必填，默认缓存上次选择。 对应参数deptId, subDirection
    * 卡片ID：文本框，用户自行填写，必填  对应参数icafeId
    * 环境类型：选择调试请求的Agent环境，单选，必选。根据选择平台会调用麒麟线上环境或者测试环境
    * 执行类型：下拉选择，必填，默认全部。对应参数operationType, toolId
        * 全部工具，不显示后面工具ID选项
        * 指定工具，自动显示工具ID选项，文本输入，必填


* 点击“执行”。前端间隔5s轮训一次，直至Agent执行完毕

![等待Agent执行结果](/personal-site-mvp/img/doc-placeholder.svg "等待Agent执行结果")
![Agent执行结果展示](/personal-site-mvp/img/doc-placeholder.svg "Agent执行结果展示")


## 4.3、结果验证
根据前端渲染的结果，确认Agent的逻辑是否符合预期。

* 如果不符合预期，重新修改代码，部署到[麒麟平台](https://kirin.baidu-int.com/#/q-market/0/list/domain-all)，然后测试验证直至符合预期后，发布上线

![更新代码](/personal-site-mvp/img/doc-placeholder.svg "更新代码")
![发布上线](/personal-site-mvp/img/doc-placeholder.svg "发布上线")
* 如果结果符合预期，进入第5步，将Agent配置到业务线，正式落地使用（仅首次，后续代码变更上线后无需再次配置）





## 4.4、问题排查
如果前端展示结果不符合预期，或者执行失败了, 可以自行到麒麟平台查看自己的任务的运行情况

![](/personal-site-mvp/img/doc-placeholder.svg "")
****

## 4.5、异常感知
如流搜索并关注服务号“TestOne-MEG智能交付”，后续的Agent执行异常，都会通过服务号实时同步给相关开发者。

![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")
# 5、Agent发布&配置
## 5.1、Agent发布
当Agent被注册到平台时属于"未发布"的状态，此时无法在配置中心将Agent配置到各个测试阶段。点击"发布"完成发布

![](/personal-site-mvp/img/doc-placeholder.svg "")
发布成功的前提条件：必须在**线上环境**调试通过（调试，请转6.3），才能成功完成发布

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 5.2、Agent配置
[https://testone.baidu-int.com/#/testone/configmanage](https://testone.baidu-int.com/#/testone/configmanage)

在平台配置中心页面，选择自己业务每个阶段需要使用哪个Agent进行处理。平台会根据各业务方向的配置调起对应的Agent处理

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 6、日常开发迭代流程
## 6.1、本地修改代码
> 各开发者按需修改代码
## 6.2、单测
* 执行命令 sh run_all_unittest_case.sh 

> * 该命令会自动获取tests目录下所有单测用例并执行，确保打包前所有单测执行通过
> * 建议后续把相关流程整合到流水线
> 
## 6.3、编译打包
* 执行命令  sh build.sh   (后续自己按需优化build.sh的代码逻辑)

注意:

* qep_delivery_tools, qep_delivery_component,qep_delivery_data 这三个依赖包一定要严格按照requirements.txt的版本号和Agent代码打包到一起，避免麒麟公共环境的版本被其他人升降级导致的Agent执行异常问题
* 不建议手动打包
* 打包成功后，会生成 output/agent.zip这个文件

## 6.4、部署测试环境
仅支持部署在麒麟平台上的Agent。麒麟平台，上传安装包以后，需要有解压安装的过程。通常3min内就绪

找到自己的Agent，点击"包更新"，支持部署新包和历史包到测试环境中

![](/personal-site-mvp/img/doc-placeholder.svg "")
新包部署：点击"上传文件"，选择本地Agent包（6.3编译产出的agent.zip）更新到测试环境

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
历史包部署：选中一个历史包更新到测试环境

![](/personal-site-mvp/img/doc-placeholder.svg "")


## 6.5、调试验证
找到自己的Agent

![](/personal-site-mvp/img/doc-placeholder.svg "")
构造调试参数

此时代码还在测试环境，环境记得别选错

![](/personal-site-mvp/img/doc-placeholder.svg "")
等待Agent执行完毕（取决于Agent的执行速度）

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 6.6、上线
仅支持部署在麒麟平台上的Agent。麒麟平台，上传安装包以后，需要有解压安装的过程。通常3min内就绪

找到自己的Agent，点击"调试&更新"，当测试环境有新部署且未上线的包（部署测试环境，请转6.2），点击"上线"完成上线

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
上线成功的前提条件：必须在部署Agent测试环境后，在**测试环境**调试通过（调试，请转6.3），才能成功完成上线



![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 7、Agent和Tool的优化
## 7.1 Agent执行数据可视化
点击左侧『交付引擎-Agent』标签，进入Agent管理页。

### 7.1.1 执行记录
点击任意记录的『执行记录』按钮，会展示悬浮弹框，里面是该Agent的执行记录。

可查看对应执行的卡片信息、业务信息、Agent执行状态等数据，若想详细查看某一条记录，可以点击右侧详情。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
点击右侧详情后，显示该次任务的Tool执行情况，可以看到各个Tool的状态与最终输出的组件参数。

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 7.1.2 统计数据
点击任意Agent的『统计数据』按钮，右侧会展示弹窗，里面显示该Agent的总体执行数据与近10天的详细执行数据统计图表。

数据总揽如下：

* 总调用数 —— 该agent调用总数=agent执行成功数+agent执行失败数
* 执行成功数 —— 该agent执行成功数
* 稳定性 —— agent执行成功数 / agent调用总数
* 平均执行时间（最近10次任务的平均执行时间 单位秒）



工具统计表：

* 统计Agent包含的各类Tool数量，以及对应的召回率



数据统计图：

* 折线图展示最近10天的稳定性数据，对应右侧纵坐标。
* 柱状图展示最近10天的总调用数数据，对应左侧纵坐标。
* 横坐标是日期

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


## 7.2 Tool执行数据可视化
点击左侧『交付引擎-Tool』标签，进入Tool管理页。

### 7.2.1 执行记录
点击任意记录的『执行记录』按钮，会展示悬浮弹框，里面是该Tool的执行记录。

可查看对应执行的Agent信息与组件信息，以及标记结果。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


### 7.2.2 统计数据
点击任意Tool的『统计数据』按钮，右侧会展示弹窗，里面显示该Tool的总体执行数据与近10天的详细执行数据统计图表。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
数据总揽如下：

* 总调用数 —— 该Tool调用总数=Tool执行成功数+Tool执行失败数
* 执行成功数 —— 该Tool执行成功数
* 稳定性 —— Tool执行成功数 / Tool调用总数
* 平均执行时间（最近10次任务的平均执行时间 单位秒）
* 准确率——『标注正确数』/ 『总标注数』

数据统计图表：

* 折线图展示最近10天的稳定性数据，对应右侧纵坐标。
* 柱状图展示最近10天的总调用数数据，对应左侧纵坐标。
* 横坐标是日期



## 7.3 Agent和Tool的数据飞轮 - 用户标注
若认为执行的结果不准确，可以手动点击标注，将错误原因反馈，让算法得到优化



如何下发标签能力

```
# 引入相关依赖
from qep_delivery_component import ComponentOperateConfig
from qep_delivery_component import LabelConfig
from qep_delivery_component import LabelTypeEnum

from qep_delivery_tools import BaseTool
from qep_delivery_tools import Parameter
from qep_delivery_tools import ToolResult


class XxxTool(BaseTool):
    """
    工具
    """

    def __init__(self):
        super().__init__("xxxxxx")

    def execute(self, parameter: Parameter) -> ToolResult:
        """
        执行
        """
        return ToolResult(
            self.tool_id,
            XxxxComponent(                                           # 自己工具结果对应的前端渲染组件类
                component_operate_config=ComponentOperateConfig(         # 组件的操作配置
                    expand=True,                                             # 默认展开/折叠
                    label_config=LabelConfig(                                # 组件结果标注配置 （默认为None, 表示不需要标注，前端不展示任务标注标签）
                        LabelTypeEnum.SINGLE_SELECT,                             # 标注类型，单选， 支持多选(MULTI_SELECT), 文本输入(TEXT)
                        right_items=["正确标签1", "正确标签2"],                     # 正确类型标签，如果工具的执行结果符合预期也想让用户标注可以下发
                        wrong_items=["错误标签1", "错误标签2", "错误标签3"]          # 错误类型标签, 工具结果不符合预期的原因标签
                    )
                ),
                component_data=""                                        # 组件对应的数据
            )
        )

```
效果展示

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 8、附录
以下文档仅提供了表格组件的实现方案，下面前端组件样式的工具返回结果封装参考

[🧩qep-delivery-component](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/jjn5mND5Z9-KEM?t=mention&mt=doc&dt=doc)



[统计]
