---
title: "修改方案说明：适配流式输出的分隔符检测"
description: "当前的实现存在一个致命问题："
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\streaming_fix_explanation.md"
---
# 修改方案说明：适配流式输出的分隔符检测

## 问题分析

当前的实现存在一个致命问题：

```
消息1: "好的，我来帮你..." 
  → 累积到 _accumulated_text
  → 没有分隔符，推送到 TestOne
  ✓ TestOne 看到："好的，我来帮你..."

消息2: "让我查询数据库..." 
  → 累积到 _accumulated_text（现在是 "好的，我来帮你...让我查询数据库...")
  → 没有分隔符，推送到 TestOne
  ✓ TestOne 看到："让我查询数据库..."（重复推送了！）

消息3: "----回复----问题原因是..."
  → 累积到 _accumulated_text
  → 检测到分隔符！分割内容
  → process_part = "好的，我来帮你...让我查询数据库..."
  → 推送 process_part 到 TestOne（又重复了！）
  ✗ TestOne 看到重复内容
```

**问题根源**：第 154-159 行每次都无条件推送内容到 TestOne，导致当检测到分隔符后，中间过程的内容会被重复推送。

## 解决方案

使用状态机方式，只在两种情况下推送：
1. **已检测到分隔符**：所有后续内容直接推送到如流
2. **结束时未检测到分隔符**：通过兜底机制处理

```
状态1: 寻找分隔符阶段（_phase = "searching"）
  消息1-N: 只累积，不推送
  
  ↓ 检测到 ----回复----
  
状态2: 已找到分隔符阶段（_phase = "found"）
  消息N+1+: 直接推送到如流
  
  ↓ 收到 ResultMessage
  
兜底: 如果整个过程没检测到分隔符
  推送所有累积内容到如流
```

## 完整修复代码

将 task.py 中的 MyDuccUtil 类替换为：

```python
class MyDuccUtil(DuccUtil):
    """
    重写parse_msg_and_push_to_testone方法，支持通过分隔符控制推送到如流的内容
    适配流式输出场景
    """

    def __init__(self, parameter):
        super().__init__(parameter)
        # 状态标记：'searching' = 寻找分隔符，'found' = 已找到分隔符
        self._phase = "searching"
        # 用于兜底：记录是否已经推送过任何消息到如流
        self._has_pushed_to_infoflow = False
        # 只在 searching 阶段累积文本（用于最后推送）
        self._accumulated_text = ""

    def parse_msg_and_push_to_testone(self, msg):
        """
        解析消息并推送到TestOne
        支持通过 ----回复---- 分隔符来区分中间过程和最终结论
        
        流程：
        1. searching 阶段（未找到分隔符）：只累积文本，不推送
        2. 检测到分隔符：进入 found 阶段，后续内容直接推送到如流
        3. 结束时：如果仍在 searching，触发兜底机制
        
        :param msg: claude的messages
        :return:
        """
        logging.info(str(msg))
        if isinstance(msg, UserMessage):
            msg_content = msg.content[0]
            if isinstance(msg_content, TextBlock):
                pass
            elif isinstance(msg_content, ToolUseBlock):
                super().push_func_call_data(
                    func_name=self.get_tool_name(msg_content),
                    func_arguments=msg_content.input
                )
            elif isinstance(msg_content, ToolResultBlock):
                super().push_func_response_data(
                    func_name=self.get_tool_name(msg_content),
                    func_response=msg_content.content,
                    to_infoflow=False
                )
            elif isinstance(msg_content, ThinkingBlock):
                super().push_think_stream_data(think_stream_data=msg_content.thinking, to_infoflow=False)
            else:
                super().push_result_stream_data(result_stream_data=str(msg_content), to_infoflow=False)
        elif isinstance(msg, SystemMessage):
            super().push_think_stream_data(think_stream_data=str(msg), to_infoflow=False)
        elif isinstance(msg, AssistantMessage):  ## 助手回复
            msg_content = msg.content[0]
            if isinstance(msg_content, TextBlock):
                text = msg_content.text
                
                if self._phase == "searching":
                    # 寻找分隔符阶段：累积文本
                    self._accumulated_text += text
                    
                    # 检查是否包含分隔符
                    separator = '----回复----'
                    if separator in self._accumulated_text:
                        # 找到分隔符！分割内容
                        parts = self._accumulated_text.split(separator, 1)
                        before_separator = parts[0]
                        after_separator = parts[1] if len(parts) > 1 else ""
                        
                        # 推送分隔符之前的内容到 TestOne
                        if before_separator.strip():
                            super().push_result_stream_data(
                                result_stream_data=before_separator,
                                to_infoflow=False
                            )
                        
                        # 进入 found 阶段
                        self._phase = "found"
                        
                        # 推送分隔符之后的内容到如流 + TestOne
                        if after_separator.strip():
                            super().push_result_stream_data(
                                result_stream_data=after_separator,
                                to_infoflow=True
                            )
                            self._has_pushed_to_infoflow = True
                        
                        # 清空累积文本
                        self._accumulated_text = ""
                elif self._phase == "found":
                    # 已找到分隔符：直接推送到如流
                    super().push_result_stream_data(
                        result_stream_data=text,
                        to_infoflow=True
                    )
                    self._has_pushed_to_infoflow = True
                    
            elif isinstance(msg_content, ToolUseBlock):
                super().push_func_call_data(
                    func_name=self.get_tool_name(msg_content),
                    func_arguments=msg_content.input,
                    to_infoflow=False
                )
            elif isinstance(msg_content, ToolResultBlock):
                super().push_func_response_data(
                    func_name=self.get_tool_name(msg_content),
                    func_response=msg_content.content,
                    to_infoflow=False
                )
            elif isinstance(msg_content, ThinkingBlock):
                super().push_think_stream_data(think_stream_data=msg_content.thinking, to_infoflow=False)
            else:
                super().push_result_stream_data(result_stream_data=str(msg_content), to_infoflow=False)
        elif isinstance(msg, ResultMessage):
            # 结束处理：兜底机制
            if not self._has_pushed_to_infoflow:
                # 整个过程没有推送过任何内容到如流
                if self._phase == "searching" and self._accumulated_text.strip():
                    # 说明没有找到分隔符，推送所有累积的文本
                    logging.info("触发兜底机制：未检测到分隔符，推送所有累积内容到如流")
                    super().push_result_stream_data(
                        result_stream_data=self._accumulated_text.strip(),
                        to_infoflow=True
                    )
                    self._has_pushed_to_infoflow = True
                elif msg.result:
                    # 使用 ResultMessage 的 result 字段
                    logging.info("触发兜底机制：使用 ResultMessage 推送最终结论到如流")
                    super().push_result_stream_data(
                        result_stream_data=msg.result,
                        to_infoflow=True
                    )
                    self._has_pushed_to_infoflow = True
            
            # 清理状态
            self._accumulated_text = ""
```

## 关键改进

| 方面 | 旧逻辑 | 新逻辑 |
|------|-------|-------|
| 推送时机 | 每次都推送到 TestOne | 只在找到分隔符后推送 |
| 重复问题 | ❌ 中间内容会重复推送 | ✅ 无重复 |
| 流式适配 | ❌ 不适合流式 | ✅ 完全适合流式 |
| 状态管理 | 简单但有缺陷 | 使用状态机，清晰可靠 |
| 累积内容 | 每次都推送后继续累积 | 只在 searching 阶段累积 |

## 工作流程示例

**输入流**:
```
消息1: "好的，我来帮你排查..." 
消息2: "让我查询数据库..."
消息3: "找到了原因"
消息4: "----回复----"
消息5: "🔍 问题分析"
消息6: "..."
```

**执行流**:
```
消息1-3: phase=searching → 累积，不推送
消息4: 检测到分隔符 → phase=found，推送消息3之前的内容到TestOne，推送消息4之后的内容到如流
消息5-6: phase=found → 直接推送到如流
```

**结果**:
- TestOne: 显示 "好的，我来帮你排查..." 等中间过程
- 如流: 显示 "🔍 问题分析" 等最终结论

```

## 需要更新的文件位置

file: `/Users/zhuji_m4pro/code/baidu/ducc/baidu/qamate-strategy/api-smart-ai/sandbox_agent/ai-agent_kirin/agents/sbx_code/task.py`
lines: 80-195 (MyDuccUtil 类)

