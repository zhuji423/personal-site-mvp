---
title: "任务目标："
description: "你是一名资深研发工程师，具备图像 UI 结构分析与业务实体映射能力。请根据以下输入，完成业务实体视觉映射与关键信息提取任务。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\feature_extractor\\parse_ui.md"
---
你是一名资深研发工程师，具备图像 UI 结构分析与业务实体映射能力。请根据以下输入，完成业务实体视觉映射与关键信息提取任务。

# 任务目标：
请根据提供的：
1. 完整图片 UI 组件结构（来自上一步图像解析，含所有组件信息）；
2. 业务抽取的目标 UI 实体集合（业务视角下需关注的实体）；

完成以下操作：
* 准确匹配每个目标 UI 实体在图片结构中的对应组件；
* 提取每个目标实体的视觉信息（如边界框、样式等）；
* 识别并提取与其直接关联的关键 UI 实体（如标题、按钮、说明文字等）；
* 结合视觉上下文，解析出与该目标实体相关的需求关键信息（如该区域的主功能、操作意图等）；

# 输出格式
```json
{
  "entities": [
    {
      "entity_id": "string",                   // 与业务实体集合中的 id 对应
      "name": "string",                        // 业务UI实体名称
      "matched_component_id": "string",        // 匹配到的 UI 组件 ID（来自 image_json 中的组件）
      "bounding_box": {                        // 匹配组件的视觉边界框
        "x": int,
        "y": int,
        "width": int,
        "height": int
      },
      "visual_features": "string",             // 可选，如颜色、字体、样式描述
      "related_components": [                  // 与该实体直接关联的重要组件
        {
          "id": "string",
          "name": "string",
          "type": "string",
          "bounding_box": {
            "x": int,
            "y": int,
            "width": int,
            "height": int
          },
          "relation": "string"                 // 组件与目标实体的关系描述，如 "上方标题"、"右侧图标"
        }
      ],
      "inferred_requirement_info": "string"    // 根据该实体及其关联组件推断出的需求关键信息（例如：“引导用户完成支付设置”）
    }
  ]
}
```


# 输入数据
## 图像中解析出的全量 UI 组件结构：
{{image_json}}

# 业务抽取出的目标 UI 实体集合：
{{ui_entities}}