---
title: "示例代码"
description: "Markdown组件"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🛠️TestOne-SDK\\📁 🧩qep-delivery-component\\📄 Markdown组件.md"
---
Markdown组件

qep-delivery-component >= 0.4.0

# 示例代码
```
from qep_delivery_component import ComponentOperateConfig
from qep_delivery_component import MarkdownComponent
from qep_delivery_tools import Parameter
from qep_delivery_tools import ToolResult
from qep_delivery_tools import BaseTool


class XxxTool(BaseTool):
    """
    Xxx工具
    """

    def __init__(self):
        super().__init__(自己注册的ToolId)


    def execute(self, parameter: Parameter) -> ToolResult:
        """
        Markdown展示组件结果封装
        """
        content = """
        ### 测试方案
        需求概述: 该需求主要涉及在 RANKER 模块中引入 UMS 服务，并新增相关服务配置、handler、策略以及类，用于支持 UMS 服务的调度和响应数据解析。
        #### 详细测试方案,
        1. **服务引入验证**
           - 检查 UMS 服务是否成功引入，并验证其相关功能是否正常。
        2. **服务配置测试**
           - 测试新增的服务配置，包括 BNS、超时配置等，确保配置生效且正确。
        3. **handler 功能测试**
           - 验证 handler 是否能够正确调度 UMS 服务的请求和响应。
        4. **策略测试**
           - 测试新增的策略 `StrategyRecUms` 是否能够正确传入 UMS 请求相关信息，并构造请求数据。
           - 验证策略是否能够正确解析 UMS 响应包，并保存 UMS 原始响应数据。
        5. **类测试**
           - 测试新增的类 `UmsFeatureQueryData` 是否能够正确保存各 feature 解析出来的响应数据，并验证其供策略使用的功能。
        6. **兼容性测试**
           - 验证引入 UMS 服务及相关改动后，是否对现有功能产生影响。
        7. **性能测试**
           - 对引入 UMS 服务后的系统进行性能测试，确保性能符合预期。
        8. **边缘场景测试**
           - 测试涉及 UMS 服务的边缘场景，确保系统在这些场景下能够正确处理。
        9. **安全性测试**
           - 验证引入 UMS 服务后，系统的安全性是否受到影响。
        10. **回归测试**
            - 在完成上述测试后，进行全面的回归测试，确保所有功能正常。
        """
        component_info = MarkdownComponent(component_operate_config=None, component_data=content)
        return ToolResult(self.tool_id, component_info)
```
# 展示效果
![](/personal-site-mvp/img/doc-placeholder.svg "")
