---
title: "Code Connect指南"
description: "1. 解析【设计稿html】包含 组件标记（Component Markers）的注释,明确需要引入的组件列表。 组件标记格式如下： \\\\\\html <-- START: ComponentName -- <div connect-comp"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\figma2code-comate\\references\\codeConnect.md"
---
# Code Connect指南
应当严格按下列步骤分析设计稿中使用的组件：

1. 解析【设计稿html】包含 **组件标记（Component Markers）**的注释,明确需要引入的组件列表。
组件标记格式如下：
\`\`\`html
<!-- [START: ComponentName] -->
<div connect-component="ComponentName" connect-props="属性json">
</div>
<!-- [END: ComponentName] -->
\`\`\`

2. 分析【设计稿图片】，识别其中未标记的可复用组件作为补充。请逐个检查是否包含下面这几个未标记的组件：
- 表单与表单项 (Form + Form-item)
- 表格 (Table)
- 按钮 (Button)
- 输入框 (Input)
- 单选框 (Radio)
- 多选框 (Checkbox)
- 模态框 (Modal)
如果标记的组件与自动识别需要使用的组件不匹配，以标记的组件优先。如果有明显标记错误应当以友好方式提示用户。

3. 确定需要引入的组件后，使用read_file工具在.comate/components目录下读取对应的组件文档。
- 如果识别到的组件对应的文档在项目中不存在或无法找到，回退到根据 Figma HTML 实现。
- 非用户要求禁止读取无关的组件知识。
- 非用户要求禁止在.comate/components目录以外全局检索组件知识。

4. 结合组件文档，正确引入组件，并根据原html的特征正确使用组件属性。