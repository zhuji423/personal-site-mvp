---
title: "config_example"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\harmony_gen\\knowledges\\single_xml\\examples\\config_example.md"
---
### 输入配置示例
* 输入颜色配置示例
```test-styles/src/main/res/values/colors.xml
<color name="testColor1">#1E1F24</color>
<color name="testColor2">#3C3D45</color>
```
```test-styles/src/main/res/values-night/colors.xml
<color name="testColor3">#0D000000</color>
```
* 输入文本配置示例
```test-template/src/main/res/values/strings.xml
<string name="test_text">TestTextTemp</string>
```
```test-styles/src/main/res/values/strings.xml
<string name="test_text">TestTextStyle</string>
```
* 输入数值配置示例
```test-styles/src/main/res/values/dimens.xml
<dimen name="test_num_15dp">15dp</dimen>
<dimen name="test_num2">30dp</dimen>
```
### 输出配置示例
* 颜色配置路径示例：`entry/src/main/resources/base/element/test_styles_color.json`
* 颜色配置内容示例：
```json
{
  "color" : [
    {
      "name": "testColor1",
      "value": "#1E1F24"
    },
    {
      "name": "testColor2",
      "value": "#3C3D45"
    }
  ]
}
```
* 颜色配置路径示例（夜间）：`entry/src/main/resources/dark/element/test_styles_color.json`
* 颜色配置内容示例（夜间）：
```json
{
  "color": [
    {
      "name": "testColor3",
      "value": "#0D000000"
    }
  ]
}
```
* 文本配置路径示例：`entry/src/main/resources/base/element/test_template_string.json`
* 文本配置内容示例：
```json
{
  "string": [
    {
      "name": "test_text",
      "value": "TestTextTemp"
    }
  ]
}
```
* 文本配置路径示例：`entry/src/main/resources/base/element/test_styles_string.json`
* 文本配置内容示例：
```json
{
  "string": [
    {
      "name": "test_text",
      "value": "TestTextStyle"
    }
  ]
}
```
* 数值配置路径示例：`entry/src/main/resources/base/element/test_styles_float.json`
* 数值配置内容示例：
```json
{
  "float": [
    {
      "name": "test_num_15vp",
      "value": "15vp"
    },
    {
      "name": "test_num2",
      "value": "30vp"
    }
  ]
}
```