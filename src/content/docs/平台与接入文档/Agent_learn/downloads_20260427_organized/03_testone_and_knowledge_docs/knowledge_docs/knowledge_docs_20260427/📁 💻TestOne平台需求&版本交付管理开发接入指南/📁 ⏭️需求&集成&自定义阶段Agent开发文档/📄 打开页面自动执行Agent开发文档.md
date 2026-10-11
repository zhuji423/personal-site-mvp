---
title: "1、背景"
description: "打开页面自动执行Agent开发文档"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📄 打开页面自动执行Agent开发文档.md"
---
打开页面自动执行Agent开发文档

# 1、背景
目前TestOne各阶段调起Agent有两种方式

* 主动触发（前端页面触发/基于API触发）
* 被动触发（根据上一个阶段Agent的执行结果自动触发下一阶段）



存在的问题：

> 用户打开页面看到的数据都是上一次(可能是几个小时/几天前)的执行结果，针对部分对时效性要求较高的工具不太友好


# 2、方案
为了解决次问题，允许开发者在各个阶段的Agent内自行控制各阶段打开页面的时候是否支持自动调起Agent，如果开发者设置为允许打开页面的时候自动触发Agent，用户打开前端页面的时候就会自动触发该阶段的Agent。

注意：

前端是否自动触发，除了开发者打开对应的开关，还得遵循以下原则

* 当前状态下，该阶段的Agent允许触发（比如卡片已经到了准出阶段，开发阶段/准入阶段的Agent也不会自动触发）
* 为了避免用户切换阶段之类的操作，导致的该阶段刚执行完又马上再次触发执行等问题影响体验，距离上次执行<5min的不自动触发，如有必要请手动触发执行

注意：

由于用户打开页面，切换到对应阶段的时候，就会自动触发该阶段的Agent。建议开发者仅重新执行部分对时效性要求比较高且速度较快的Tool（之前执行过的Tool本次不执行也不影响，TestOne会自动展示之前的结果），否则可能会严重影响到用户体验。

同时为了保障用户体验，在自动触发执行前，之前的执行结果会展示在前端页面，新的Tool执行完毕以后会提示用户刷新结果

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.1、接入步骤
升级Agent依赖的SDK（大于等于以下版本均可）

```
qep-delivery-data==0.2.8
qep-delivery-component==0.2.16
qep-delivery-tools==0.4.14
```


怎么控制下发该阶段允许自动执行？

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


调起Agent的时候怎么区分是自动调起的执行，方便开发者区分执行不同的逻辑？

> 调起Agent的时候，请求参数有个字段 operate_type，可以基于此字段区分：
> * 0：全量执行
> * 1：指定单个Tool自行
> * 2：打开页面自动触发执行，具体需要执行哪些Tool开发者自行决策
> 
![](/personal-site-mvp/img/doc-placeholder.svg "")


由于本次只执行了部分工具，不知道其他工具的风险情况，如何控制Agent的风险高低，避免影响流程？

> 1、拿到当前阶段其他工具的风险情况
> 2、拿到本次执行的工具的风险情况
> 3、综合判断最终的风险高低
```
class XxxxStageAgent(BaseAgent):
    """
    Xxx阶段Agent
    """

    def __init__(self, parameter: Parameter):
        super().__init__(parameter)
    
    def analysis_risk(self, tool_results: List[ToolResult]):
        """
        综合分析风险（注：以下只是一个通用的思路参考，具体请结合业务实际情况处理）
        @param tool_results: 本次执行工具的结果
        """
        high_risk = False
        risk_summary = "低风险"
        # 如果是全量工具执行，则只要有一个工具高风险就认为高风险
        if self.parameter.operation_type == OperateTypeEnum.FULL_TRIGGER:
            for item in tool_results:
                if item is not None and item.high_risk:
                    high_risk = True
                    risk_summary = "整体风险较高，主要风险项请参考下方高风险工具详情"
                    break
        else:
            # 如果指定工具执行，或者自动触发执行了某些工具。需求结合这些工具的结果和之前已经执行过的工具结果，综合给出风险
            # 获取历史执行结果
            result = self.get_execute_result(TESTONE_USERNAME, TESTONE_TOKEN, self.parameter.icafe_ids[0],
                                             self.parameter.stage, ONLINE_ENV)
    
            # 将工具的执行风险信息放到一个Map里面，先放之前的执行结果，再放本次的执行结果，这样相同工具的结果即为最新一次
            risk_map = {}
            for tool_result in result.tool_result_list:
                risk_map[tool_result.tool_id] = tool_result.high_risk
            for tool_result in tool_results:
                risk_map[tool_result.tool_id] = tool_result.high_risk
    
            for _, risk in risk_map.items():
                if risk:
                    high_risk = True
                    risk_summary = "整体风险较高，主要风险项请参考下方高风险工具详情"
                    break
        return high_risk, risk_summary
        
    def execute(self) -> AgentResult:
        """
        Agent 执行工具的入口，这里可以添加一些业务逻辑
        """
    
        # 当前阶段全部可用工具集合
        all_tools = [
            abc(),
            xxxxx(),
            yyyyy(),
            zzzz(),
        ]
        
        logging.info("分析该选择哪些工具")
        tools = []
        if self.parameter.operation_type == OperateTypeEnum.FULL_TRIGGER:
            # 分析本次请求的需求，该调起哪些工具
            # TODO 可以在这实现部分业务逻辑，对一些无需执行的工具进行裁剪，并不是针对每个需求，所有的工具都需要执行
            tools = all_tools
        elif self.parameter.operation_type == OperateTypeEnum.SPECIFY_TRIGGER:
            # 指定工具调起
            for tool in all_tools:
                if tool.tool_id == self.parameter.tool_id:
                    tools.append(tool)
                    break
            if len(tools) == 0:
                raise Exception("未找到指定工具")
        elif self.parameter.operation_type == OperateTypeEnum.AUTO_EXECUTE:
            tools = [
                abc(),
                zzzz()
            ]
        logging.info(f"本次调用的工具：{tools}")
        
        # 自行决定调用顺序，串行，并行
        # 调用tool
        all_tool_results = []
        for tool in tools:
            tool_result = tool.execute(self.parameter)
            all_tool_results.append(tool_result)
            # 执行完成一个工具，回调一次, 如果Agent执行特别耗时，可以在期间部分Tool执行完毕以后，提前回调通知平台，
            # 平台可以提前展示部分已经执行完毕的Tool结果，提高用户体验
            callback_request = ToolResultCallbackRequest(self.parameter.engine_task_id, [tool_result])
            self.callback(TESTONE_USERNAME, TESTONE_TOKEN, callback_request, ONLINE_ENV)
        
        # 打开自动触发执行，自行控制
        enable_auto_execute = False
        
        # 综合分析风险情况
        high_risk, risk_summary = self.analysis_risk(all_tool_results)
        
        return AgentResult(
            self.parameter.engine_task_id,
            high_risk=high_risk,
            risk_summary=risk_summary,
            enable_auto_execute=enable_auto_execute
        )

```



