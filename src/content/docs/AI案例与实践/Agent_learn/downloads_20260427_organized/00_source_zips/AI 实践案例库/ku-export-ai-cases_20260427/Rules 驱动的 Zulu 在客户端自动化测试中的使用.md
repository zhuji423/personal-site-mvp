---
title: "实践简介"
description: "Rules 驱动的 Zulu 在客户端自动化测试中的使用"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Rules 驱动的 Zulu 在客户端自动化测试中的使用.md"
---
Rules 驱动的 Zulu 在客户端自动化测试中的使用

#### 🧑‍🏫 案例作者：[@白郅昊](https://ku.baidu-int.com?t=mention&mt=contact&id=7b0ea090-fce2-11f0-9854-27ef6d2a6b67)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了利用Rules驱动的Zulu智能体在Comate UI自动化测试项目中的应用。通过定义项目规则，Zulu理解了复杂测试框架架构，自动生成符合规范的测试代码和用例，极大提升了测试效率。项目采用高度解耦的架构设计，使得测试用例编写简洁且易于维护，展示了AI在自动化测试领域的巨大潜力。
[文档目录]
# 实践简介
## 案例概述
Rules 驱动的 Zulu 智能体在 Comate UI 自动化测试项目中的应用，体现了 Coding Agent 在提升测试效率方面的巨大潜力。通过与项目的深度集成，Zulu 不仅理解了复杂的测试框架架构，还能根据既定规则高效生成测试代码和测试用例，成为测试团队的得力助手。

## 项目架构特点
Comate UI 自动化测试项目采用了高度解耦的架构设计，将**执行框架**（Python 代码）与**测试用例**（YAML 文件）完全分离：

* **执行框架层**：基于 Playwright 的 Python 测试引擎，负责浏览器自动化、元素操作和测试执行
* **测试用例层**：使用 YAML 格式描述测试逻辑，支持变量替换、组件调用和断言验证
* **UI 元素层**：封装页面元素为可复用的组件类，继承自统一的 Element 基类

这种架构设计使得测试用例编写更加简洁，同时保持了框架的扩展性和维护性。

## 关键词
Coding Agent, 自动化测试, Playwright, YAML, UI 测试, 测试框架, 代码生成, 测试用例开发, 智能体辅助开发, DevOps

# 具体实施
## Rules 驱动的开发模式
Zulu 的核心优势在于能够理解和应用项目中的 `.mdr` 规则文件，这些规则定义了项目的开发约定和最佳实践。通过规则驱动的方式，Zulu 能够：

1. **理解项目架构**：快速掌握项目结构和组件关系
2. **遵循编码规范**：自动应用项目的代码风格和约定
3. **复用最佳实践**：基于历史经验生成高质量代码
4. **保持一致性**：确保生成的代码符合团队标准



### 规则的编写方法
代码库的规则由 **Zulu自动生成的规则**** 和 ****我在使用中补充的规则**** **共同构成。

1. **自动生成**

在输入框中输入`/`，选择“规则生成”，可以获得 Zulu 阅读代码库后自行梳理的项目结构和部分最佳实践。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f285358046f64b65a5a3d6dfea8b0e5e&docGuid=npB6_R8Nd_OUU7 "")
2. **自己补充**

在使用过程中发现执行不符合自己的想法的地方，如：步骤遗漏、格式不符合习惯，在对应的规则中进行补充。



## 1. 测试框架编写加速
```
---
globs: **/*.py
description: Python代码开发规范和项目特定约定
---

# Python开发规范

## 代码结构约定

### 文件开头约定
所有文件的开头都需要编写以下内容
```python
# !/usr/bin/env python3
"""
# 当前文件的描述
Author: # 作者名称，默认为 baizhihao@baidu.com
"""
```

### UI元素类开发
所有 UI 元素类都继承自 [Element](mdr:comate_ui_automation/elements/element.py) 基类，也可以继承自继承了 Element 基类的类：
```python
from elements.element import Element
from playwright.sync_api import Locator
from globals import global_context

class MyElement(Element):
    def __init__(self):
        self.elements: List[Locator] = []  # 定义需要检查的元素
        self.wait_for_load()

    def wait_for_load(self):
        """等待页面加载完成，初始化所有元素定位器"""
        # 实现元素定位逻辑
        pass
```
UI 元素类的类名与其文件名可以不一致。引用这些类时，请通过代码中的类名确认要引用的类名。

### 引用规范
由于元素类都在所在目录的__init__.py中注册，如果在目录外 import 该类，可以在引用时只填写到包名：
```python
from elements.path.to.package import MyElement
```

如果在目录内部 import 该类，为防止循环引用，需要在引用时填写到文件名：
```python
from elements.path.to.package.my_element import MyElement
```

### 全局上下文使用
使用[global_context](mdr:comate_ui_automation/globals.py)访问全局资源：

```python
from globals import global_context

# 记录日志
global_context.logger.info("操作信息")

# 访问页面和浏览器
global_context.page.click("selector")
global_context.browser.close()

# 存储和获取变量
global_context.add_variable("key", value)
value = global_context.variables.get("key")
```

## 项目特定约定

### 配置管理
使用[config.cfg](mdr:comate_ui_automation/config.cfg)管理配置：

```python
import configparser
from globals import global_context

config = configparser.ConfigParser()
config.read('config.cfg')

vscode_path = config['VSCode']['path']
debug_port = config['VSCode']['debug_port']
```

### 日志记录
- 使用global_context.logger进行日志记录
- 日志文件自动保存在logs目录下
- 支持同时输出到文件和控制台

### 错误处理
测试执行失败时自动：
1. 保存截图到test_errors目录
2. 记录详细错误日志
3. 包含完整的堆栈跟踪信息

## Playwright集成

### 页面操作
```python
# 等待元素
global_context.page.wait_for_selector("selector")

# 点击元素
element.click()

# 获取文本内容
text = element.text_content()

# 截图
global_context.page.screenshot(path="screenshot.png")
```

### 元素定位
- 使用Playwright的Locator API
- 支持CSS选择器和XPath
- 优先使用稳定的定位策略

## 测试用例执行

### 执行引擎
[executor.py](mdr:comate_ui_automation/executor/executor.py)是核心执行引擎：
- 解析YAML测试用例
- 动态加载组件类
- 处理变量替换
- 执行测试步骤

### 组件注册
新开发的 UI 元素类需要执行以下步骤：

1. 在所在目录的 __init__.py 中注册：
```python
from .my_new_element import MyNewElement

__all__ = [
    'MyNewElement',
    # 其他组件...
]
```

2. 在 executor.py 中注册：
```python
from elements.xxx.xxx import MyNewElement

self.components = {
    "MyNewElement": MyNewElement,
    # 其他组件...
}
```

## 依赖管理

### 核心依赖
- `playwright~=1.42.0` - 浏览器自动化
- `PyYAML>=6.0` - YAML解析
- `build>=1.0.3` - 构建工具

### 开发依赖
- `pytest` - 单元测试
- `mock` - 模拟对象

## 最佳实践

1. **元素检查**：在操作前调用element_check()确保元素可见
2. **等待策略**：使用适当的等待时间处理页面加载
3. **异常处理**：捕获并记录详细的错误信息
4. **代码复用**：通过继承Element基类复用通用功能
5. **日志记录**：记录关键操作和状态信息
6. **配置外部化**：使用配置文件管理环境相关设置

```
通过 `python-development.mdr` 规则，Zulu 能够深入理解测试框架的编写流程和架构约定：

### UI 元素类继承关系理解
```
# Zulu 自动生成的 UI 元素类示例
from elements.element import Element
from playwright.sync_api import Locator
from globals import global_context

class MyElement(Element):
    def __init__(self):
        self.elements: List[Locator] = []  # 定义需要检查的元素
        self.wait_for_load()

    def wait_for_load(self):
        """等待页面加载完成，初始化所有元素定位器"""
        # 实现元素定位逻辑
        pass
```
Zulu 能够准确理解：

* 所有 UI 元素类必须继承自 Element 基类
* 需要实现 `wait_for_load()` 方法进行元素初始化
* 使用 `elements` 列表定义需要检查的页面元素



### 组件注册流程自动化
当创建新的 UI 元素类后，Zulu 会自动执行两步注册流程：

1. **在 **`__init__.py`** 中注册**：

```
from .my_new_element import MyNewElement

__all__ = [
    'MyNewElement',
    # 其他组件...
]
```
2. **在 **`executor.py`** 中注册**：

```
from elements.xxx.xxx import MyNewElement

self.components = {
    "MyNewElement": MyNewElement,
    # 其他组件...
}
```
这种自动化的注册流程确保了新组件能够被测试框架正确识别和调用。



### 全局资源智能访问
Zulu 通过 `global_context` 智能访问和管理全局资源：

```
from globals import global_context

# 记录日志
global_context.logger.info("操作信息")

# 访问页面和浏览器
global_context.page.click("selector")
global_context.browser.close()

# 存储和获取变量
global_context.add_variable("key", value)
value = global_context.variables.get("key")
```
Zulu 能够根据上下文智能选择合适的全局资源，如：

* 使用 `global_context.logger` 进行结构化日志记录
* 通过 `global_context.page` 和 `global_context.browser` 操作浏览器
* 利用变量系统实现测试数据的传递和存储



### 编写测试框架实战
编写用于测试【网络检索工具】的 UI 元素类。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e7d72d01e098416aad873128fa1e16eb&docGuid=npB6_R8Nd_OUU7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7e5ed240dea54d5e9f9e19f2f5decb53&docGuid=npB6_R8Nd_OUU7 "")


## 2. 测试用例编写加速
通过 `test-case-development.mdr` 规则，Zulu 掌握了测试用例的编写步骤和格式规范：

### 智能步骤解析与代码检索
当用户提供测试步骤描述时，Zulu 能够：

1. **理解操作意图**：分析用户描述的测试目标和操作流程
2. **检索相关组件**：在 `elements` 目录中查找合适的 UI 元素类和方法
3. **验证实现可行性**：读取组件代码，确认方法能否实现所需操作
4. **生成格式化用例**：按照 YAML 格式编写符合规范的测试用例

### YAML 测试用例生成示例
基于用户描述："点击 Zulu Tab 中的第一个推荐问题"，Zulu 生成：

```
test_cases:
  - name: "点击第 1 个推荐问题"
    description: |
      1. 切换到Zulu Tab
      2. 点击新建聊天按钮
      3. 点击第一个推荐问题
    versions:
      - "SaaS"
    IDE:
      - "VSCode"
    steps:
      - class: "ComateWebviewTabBar"
        function: "switch_tab"
        args:
          tab: "zulu"
      - class: "ComateTitleBar"
        property: "btn_create_new_chat"
        function: "click"
      - class: "ComateZuluTab"
        function: "click_user_guide"
        args:
          index: 0
```
### 高级功能支持
Zulu 还能处理复杂的测试场景：

1. **变量替换**：使用 `${variable_name}` 格式实现测试数据的动态传递
2. **属性断言**：验证 UI 元素的状态和属性值
3. **函数返回值断言**：检查方法调用的返回结果
4. **变量存储**：将测试过程中的数据保存供后续使用

```
# 变量存储示例
- class: "ComateChatTab"
  store:
    property: "selected_agent"
    variable: "current_agent"

# 变量引用示例
- class: "ComateChatTab"
  assert:
    property: "selected_agent"
    value: "${current_agent}"
```


### 测试用例编写实战
测试用例迁移：随着客户端功能的演进，将一个测试用例进行迁移。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cf723abc51764745acd95e848e360adb&docGuid=npB6_R8Nd_OUU7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3ef0135fa4c54990aacdb8465df2fa3f&docGuid=npB6_R8Nd_OUU7 "")
# 总结
Zulu 在 Comate UI 自动化测试项目中的成功应用，展示了 AI 智能体在软件开发领域的巨大潜力。通过规则驱动的开发模式，Zulu 不仅提高了开发效率，还确保了代码质量和一致性。这种人机协作的模式将成为未来软件开发的重要趋势，让开发者能够专注于更有创造性的工作，同时让 AI 处理重复性和规范性的任务。

通过本案例的实践，我们证明了：

1. **规则驱动**是 AI 辅助开发的有效模式
2. **架构解耦**为 AI 理解和生成代码提供了良好基础
3. **持续学习**使 AI 能够不断适应项目演进
4. **人机协作**是提升软件开发效率的最佳途径

**

## 彩蛋
**这篇文档也是我在我实践的代码库里用 Zulu 生成的**。在规则的加持下，Zulu 可以很好地理解项目结构和实践方法。

在此分享一下我的 prompt。

```
恭喜你！你和这个代码库的优秀配合成为了智能体的优秀实践案例。我希望你帮我写一篇 markdown 文档，介绍 Zulu 在客户端自动化测试中的使用。核心思想包括如何使用 rules 提升测试用例和测试框架编写的效率。在这个过程中，你可以读取任何文件和编写 markdown 文档，但不要修改任何代码文件。

文档的结构如下：
- 实践简介
首先，帮我简述一下我的实践案例；然后，介绍一下代码库的基本架构，提现执行框架（代码）和测试用例（yaml 文件）解耦。关于项目结构的内容在  #project-structure.mdr 中，你也可以通过阅读任何项目中的文件来辅助你撰写这部分。

- 关键词
Coding Agent, 自动化测试
你可以补充一些你认为合适的关键词。

- 具体实施
请重点介绍 rules 如何加速自动化测试的编写。在这其中，可以引用.mdr文件中的任何内容，使讲解更加详尽。
主要涉及两类任务：
1. 测试框架的编写。通过 #python-development.mdr这个规则，Zulu 能够理解测试框架的编写流程。例如：UI 元素类与 Element 基类的继承关系；新建一个 UI 元素类之后，要在 __init__.py 和 executor.py 中注册；在编写代码的过程中，通过 global_context 找到可以使用的全局资源，如 logger。
2.  测试用例的编写。通过 #test-case-development.mdr这个规则，Zulu 能够理解测试用例的编写步骤和用例格式。当用户提供一个用例的操作步骤后，能够按照步骤检索和查阅代码，并编写符合格式要求的测试用例。
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=66a5a48188314cb88b3145de46c5899c&docGuid=npB6_R8Nd_OUU7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7d75757cf1024fdbbda5d78b8b309b2b&docGuid=npB6_R8Nd_OUU7 "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
