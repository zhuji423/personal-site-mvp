---
title: "1、背景"
description: "Agent执行中各个工具结果支持流式渲染"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\Agent执行中各个工具结果支持流式渲染.md"
---
Agent执行中各个工具结果支持流式渲染

# 1、背景
随着各业务能力建设的深入，各个阶段的Agent功能越来越丰富，随之而来的就是执行速度的问题。用户主动触发执行以后，即使其他工具都已经就绪，由于部分工具执行过慢，用户还是需要长时间等待



# 2、方案
为了提升用户的使用体验，平台支持了流式渲染的能力，在Agent执行过程中。针对已经执行完毕的工具，可以提前返回给平台。平台支持提前渲染已经就绪的工具。

![](http://bj.bcebos.com/rte-file/kuResource/353194ceeb864547bbd1beb3c50c9a1f "")


## 2.1、流式渲染模式
如果这个阶段整个Agent执行很快，几秒钟就能完成的话，不建议分多次返回，因为每次回调都是额外的时间开销，回调次数越多，Agent整体完成时间越长

修改各个阶段Agent的执行工具逻辑，针对已经执行完成的工具，提前返回给平台

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
                                             self.parameter.stage)
    
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
        # 此处省略Tool的选择逻辑
        logging.info(f"本次调用的工具：{tools}")
        
        # 调用tool
        all_tool_results = []
        for tool in tools:
            tool_result = tool.execute(self.parameter)
            all_tool_results.append(tool_result)
            
            # 执行完成一个工具，回调一次, 如果Agent执行特别耗时，可以在期间部分Tool执行完毕以后，提前回调通知平台，
            # 平台可以提前展示部分已经执行完毕的Tool结果，提高用户体验
            # 只有是线上运行环境, 才需要回调; 本地测试模式,不需要回调通知TestOne执行结果,即使回调也会被拒绝
            callback_request = ToolResultCallbackRequest(self.parameter.engine_task_id, [tool_result])
            if RUN_MODE == "ONLINE":
                self.callback(TESTONE_USERNAME, TESTONE_TOKEN, callback_request)
        
        # 综合分析风险情况
        high_risk, risk_summary = self.analysis_risk(all_tool_results)
        
        return AgentResult(
            self.parameter.engine_task_id,
            high_risk=high_risk,
            risk_summary=risk_summary
        )

```


## 2.2、整体渲染模式
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
                                             self.parameter.stage)
    
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
        # 此处省略Tool的选择逻辑
        logging.info(f"本次调用的工具：{tools}")
        
        # 调用tool
        all_tool_results = []
        for tool in tools:
            tool_result = tool.execute(self.parameter)
            all_tool_results.append(tool_result)
            
        # 所有工具全部执行完成，统一回调通知平台
        # 只有是线上运行环境, 才需要回调; 本地测试模式,不需要回调通知TestOne执行结果,即使回调也会被拒绝
        callback_request = ToolResultCallbackRequest(self.parameter.engine_task_id, all_tool_results)
        if RUN_MODE == "ONLINE":
            self.callback(TESTONE_USERNAME, TESTONE_TOKEN, callback_request)
        
        # 综合分析风险情况
        high_risk, risk_summary = self.analysis_risk(all_tool_results) 
        return AgentResult(
            self.parameter.engine_task_id,
            high_risk=high_risk,
            risk_summary=risk_summary
        )

```
