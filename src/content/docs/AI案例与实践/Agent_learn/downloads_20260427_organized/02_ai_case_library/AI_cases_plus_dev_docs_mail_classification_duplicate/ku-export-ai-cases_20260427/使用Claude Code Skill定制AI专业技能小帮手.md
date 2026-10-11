---
title: "如何快速开发Skill"
description: "使用Claude Code Skill定制AI专业技能小帮手"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\使用Claude Code Skill定制AI专业技能小帮手.md"
---
使用Claude Code Skill定制AI专业技能小帮手

#### 🧑‍🏫 案例作者：[@夏冰](https://ku.baidu-int.com?t=mention&mt=contact&id=73262840-fceb-11f0-84fa-a9cfe6d0b11f)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Claude Code
#### 📒 案例概要：本文介绍了Claude Code Skill的定制方法，通过封装特定功能的指令和资源，使AI能精准响应需求，实现端到端自动化任务处理。详细阐述了Skill与Rules的区别、编写方式及实际效果，展示了Skill在代码审查、测试用例生成等场景中的应用，提高了开发效率和代码质量。
# 如何快速开发Skill
## 项目级别和用户级别设定
```
# 项目级别, 在项目根目录启动claude时生效，仅在项目中生效，优先级最高
./.claude/skills/


# 用户级别，默认启动生效
 ~/.claude/skills
```
skill技能包目录示例和说明

```
skills/
├── pdf-processor/
│   ├── SKILL.md
│   ├── reference.md (可选)
│   └── scripts/ (可选)
└── code-reviewer/
    └── SKILL.md
```
## SKILL.md
name与description为技能的定义，这部分信息会长期存储在claude的大脑中，按用户的输入需求自动调用，和langraph的tool定义有些类似。

name：需要简洁明了，仅代表技能名称

description：此部分的内容决定了是否会被认为符合该技能的范围，进而启用该技能。

```
---
name: 技能名称
description: 技能描述
---

# 技能名称

## 技能介绍

## 使用示例

```


skill.md的内容会被全部作用在上下文中，整体内容建议不超过500行，如任务较为简单可直接编写在SKILL.md中



## 文献引用
当需要加载较长文献内容时，使用引用的方式写在SKILL.md中，可实现按需加载，精简上下文内容。

目录结构：

```
skills/
├── test-knowledge-generator/
│   ├── SKILL.md
│   ├── reference/
│       ├── 接口测试知识/
│           ├── 接口测试知识梳理.md
│           ├── 接口定义提取.md
│           ├── 接口上下游链路分析.md
│           ├── 字段关联分析.md
│           ├──后端测试知识梳理.md
│   └── scripts/ (可选)
```
一级文献引用示例， 此文件为SKILL.md

```
---
name: 梳理业务测试知识
description: 梳理业务测试知识点，提炼业务测试流程和测试要点等
---


# 业务测试知识梳理

## 知识梳理

### 1 判断测试知识点类型并梳理知识点
- 根据用户输入的内容，判断测试知识点的类型
- 测试知识点类型主要分为以下几种：
  - 接口测试：以api接口为主的测试
  - 后端测试：调用sdk或者命令行等操作为主的测试
  - 前端测试：以web页面为主的测试

### 2 梳理测试知识点
- 根据测试知识点类型，分别读取对应的文档进行知识点梳理
 - 接口测试：请参阅[reference/接口测试知识/接口测试知识梳理.md]
 - 后端测试：请参阅[reference/后端测试知识/后端测试知识梳理.md]
 - 前端测试：请参阅[reference/前端测试知识/前端测试知识梳理.md]

### 3 测试知识点更新与整合
- 当用户输入多个文件或者目录是，将多个文件中的测试知识点汇总成

## 使用方式

当用户说"梳理当前代码库的测试点"时，你应该：

1. 使用 TodoWrite 工具创建任务列表
2. 读取用户输入的内容，当文档内容过多时，分批读取, 判断测试知识点类型
3. 根据测试指点类型，参阅文档进行梳理测试知识点，梳理完成后保存知识点
4. 修正知识点是否按参阅文档中的要求进行整合和保存
6. 向用户输出知识点摘要信息
```
在一级文献引用中也可继续引用其他文献。

```
### 步骤 3: 提炼知识点

#### 3.1 接口定义提取
参考[接口定义提取.md]提取

#### 3.2 上下游链路分析
参考[接口上下游链路分析.md]提取

#### 3.3 字段关联分析
参考[字段关联分析.md]提取

#### 3.4 业务流程提取
参考[业务流程提取.md]提取

#### 3.5 测试参数提取
参考[测试参数提取.md]提取

```


## 创建方式
**方式一**：手写需求的prompt内容，然后打开claude或者ducc命令行，参考以下格式输入即可：

输入内容：请把以下内容帮我写成claude code skill： {这里是你的prompt内容，内容需要清晰，如果是工作流，写上流程}



此方式如缺失name与description，可按照上文的SKILL.md中的补充



**方式二**：使用工具[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)创建，将此skill复制到.skill目录下，启动claude或者ducc后使用

输入内容：使用[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)工具，请把以下内容帮我写成skill： {这里是你的prompt内容，内容需要清晰，如果是工作流，写上流程}

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 我们开始来解决业务的实际需求吧
# 业务实践： 实现秒哒产品接口自动化一键式测试执行
## 背景
秒哒产品迭代频次较快，日常测试迭代排期较短，接口测试压力较大，常规自动化用例编写提效是在IDE中交互式代码补全等方式，可在编码时有一定的提效但无法自主测试与分析。



基于此思路，通过claude code的skill设计思路，针对秒哒产品特定的接口测试场景需求打造一键式的接口测试任务执行功能。



## 落地效果
15分钟内可完成100+用例的设计与自动化代码编写，包括用例代码自我修复与执行。

单接口自动化用例代码目前采纳率达100%

## 设计
### 基础信息
skill 基础信息，claude启动时即加载在大脑中，按用户输入自动识别是否启动skill，触发方式和function call有些类似

```
---
name: 秒哒API自动化测试用例生成
description: 你是一个专业的 API 自动化测试用例生成助手。当用户提供模块名称时，你将自动完成接口用例生成与测试任务
---
```
### 任务流程说明
写明各阶段事务的标准处理方式，可按自定义需求追加数据说明，用例代码和报告保存路径等，

可设定用例生成范围和测试参数化替换，代码修正规则

```
# 秒哒API自动化测试用例生成

## 任务流程

### 1. 接口信息提取
- 阅读 `api-data/{模块名}/` 目录下的接口文件
- 提取每个接口的信息（如果文件过大，分段阅读）
- 接口数据说明：
  - `requestHeaders`: 请求体 headers
  - `requestParams`: 请求体 body
  - `responseHeaders`: 返回体 headers
  - `responseParams`: 返回体 body
- 接口重复检查规则：只有path和method的值完全一致，包含path中的param参数等相同时才算是重复接口，部分内容重复的不算重复接口，有重复结果输出重复的接口信息，不对重复接口进行去重

### 2. 测试用例生成
参考下文中的测试用例模板结构的文件格式，使用 pytest 框架设计自动化测试用例：

**代码规范：**
- 用例存放路径：
    - 如果是正常用例：`test_cases/{模块名}-normal/`
    - 如果是异常用例：`test_cases/{模块名}-exception/`
- 每个接口生成Python 文件的规则:
    - 如果是正常用例，文件名格式：`test_{接口名称}_{接口method}_nomal.py`
    - 如果是异常用例，文件名格式：`test_{接口名称}_{接口method}_exception.py`
- 测试地址和 cookie 等配置从 `global_test_data.py` 读取（数据驱动方式）
- 生成用例时将接口信息中的url，path，requestHeaders，requestParams中的变量，按以下规则做替换，注意python代码格式
    - {test_env_url}替换为TEST_ENV_URL引用
    - {cookie}替换为COOKIE引用
    - {appid}替换为APPID引用
    - {pageid}替换为PAGEID引用
    - {userid}替换为USERID引用
    - {question_id}替换为QUESTIONID引用
    - {object_id}替换为OBJECTID引用
    
**用例设计规则：**
- ✅ 当用户没有要求设计异常用例时，仅设计正常用例
- ✅ 当用户要求设计正常用例时，设计正常用例
    - ✅ 使用接口原始参数，不做修改
    - ✅ 断言仅校验：HTTP 状态码 == 200 且 返回体 status == 0
- ✅ 当用户要求设计异常用例时，设计异常用例
    - ✅ 仅需要设计字段缺失，字段值为null，字段值类型错误的异常用例
    - ✅ 如果参数有多个，请参考示例代码文件中的数据驱动实现，设计数据驱动时，仅修改被测参数值，其他参数保持不变
    - ✅ 断言仅校验：HTTP 状态码 == 400，不需要校验其他
    
### 3. 代码生成注意事项
- 处理 JSON 布尔值转换（true/false → True/False）
- 处理 JSON null转换（如 null → None）
- 清理文件名中的特殊字符
- 处理类名中的连字符（替换为下划线）
- 转义请求头中的特殊字符（如单引号）
```
### 追加执行命令
按用户输入可自由判断走正常还是异常的命令执行分支

可设定代码修复规则

```
### 4. 测试执行与校正

**执行前准备：**
- 创建必要的目录结构：
  - `test_cases/{模块名}/`
  - `results/{模块名}-normal/`
  - `results/{模块名}-exception/`
  - `logs/`
  - `test_cases/{模块名}-normal/`
  - `test_cases/{模块名}-exception/`

**代码修正规则：**
- ✅ 直接修正代码格式错误（语法错误、缩进等）
- ❌ 不修改业务逻辑失败的测试（status ≠ 0 时保持断言和失败状态）
- ✅ 修正测试代码中请求体未正确替换为全局变量的问题：
  - 如将"{appid}" 替换为 APPID
  - 如将"{question_id}" 替换为 QUESTIONID
  - 如将"{object_id}" 替换为 OBJECTID

**执行命令：**
- 正常用例：
```bash
pytest ./test_cases/{模块名}-normal/ --tb=short --log-cli-level=INFO -q --html=./results/{模块名}-normal/report-{时间戳}.html --self-contained-html 2>&1 | tee ./logs/test_case-{模块名}-normal-{时间戳}.log
```
- 异常用例：
```bash
pytest ./test_cases/{模块名}-exception/ --tb=short --log-cli-level=INFO -q --html=./results/{模块名}-exception/report-{时间戳}.html --self-contained-html 2>&1 | tee ./logs/test_case-{模块名}-exception-{时间戳}.log
```

### 5. 异常处理
- 如果出现鉴权错误（401），立即通知用户

```
### 设定代码模版
确保测试代码按用户要求生成，避免大模型生成的随机性

```
## 测试用例模板结构

```python
import pytest
import requests
import json
import logging
from global_test_data import TEST_ENV_URL, COOKIE, APPID

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestAppRelease:
    """app_release 接口测试"""

    def setup_method(self):
        """测试用例前置准备"""
        self.url = f"{TEST_ENV_URL}/api/v1/app/release"
        self.headers = {
            'content-type': 'application/json',
            'cookie': COOKIE,
            'jt': '31$eyJrIj4iNiI0Iix5IkciQEdHRklKSU9NUUpKTCJJIkFqIjwiNTw8Oz4/PkRCRj8/QSI+IjYzIlEiSlFRUFNUUzg5Ozk5NiIzIit5IkYiQz9AQSI/xxxxxxxxxxxxx',
            'x-app-id': APPID,
        }
        logger.info(f"测试接口URL: {self.url}")

    def teardown_method(self):
        """测试用例后置清理"""
        logger.info("测试结束，无需数据清理")

    def test_normal_scenario(self):
        """测试正常查询场景"""
        logger.info("执行测试: {接口名称}")

        data = {
            "appId": APPID,
            "appEnv": "PRODUCE",
            "appName": None,
            "enableWeappMiniProgram": True,
            "isReleaseAppSquare": False,
            "enableExclusiveMiniProgram": False
}
        response = requests.post(self.url, headers=self.headers, json=data)

        # 记录请求和响应信息
        logger.info(f"请求URL: {self.url}")
        logger.info(f"请求头: {self.headers}")
        # 如有data 则记录请求体
        logger.info(f"请求体: {data}")
        logger.info(f"响应状态码: {response.status_code}")
        logger.info(f"响应体: {response.text}")

        # 如果认证失败，跳过断言
        if response.status_code == 401:
            logger.error(f"认证失败: {response.text}")
            pytest.skip("认证失败，跳过该测试")

        # 断言响应状态码
        assert response.status_code == 200, f"HTTP状态码异常: {response.status_code}"

        # 解析响应数据
        response_data = response.json()

        # 断言响应结构
        assert "status" in response_data, "响应缺少status字段"

        # 断言状态码为成功
        assert response_data["status"] == 0, f"业务状态码异常: {response_data['status']}, 消息: {response_data.get('msg', '')}"

        logger.info("测试通过: {接口名称}")

```

```
### 设定使用方式
自动识别工作流

```
## 使用方式

当用户说"为 {模块名} 生成测试用例"时，你应该：

1. 使用 TodoWrite 工具创建任务列表
2. 读取 api-data/{模块名}/ 目录下的接口文件
3. 提取接口信息，有重复的接口提示重复的信息，但是不对重复的接口做去重处理
4. 按代码规范中的用例存放路径按需新建目录，然后批量生成测试用例文件
5. 执行测试并生成报告
6. 修正代码格式错误（如有）
7. 提供执行结果摘要

## 示例对话

**用户**: 为 workspace 模块生成测试用例

**助手**:
1. 创建任务列表
2. 读取并提取接口（发现 46 个唯一接口）
3. 生成 46 个测试文件
4. 修复类名语法错误（7 个文件）
5. 执行测试：21 passed, 20 failed
6. 生成报告和日志

完成！
```
## 使用方式
```
为workspace生成用例并执行
为workspace生成异常用例并执行，异常用例保存在test_cases/workspace-exception/下

多轮用法：如生成的用例执行后发现时代码错误导致的问题，可以继续对话来修正代码错误
```


```
使用技能包miaoda-api-test-generator，为access模块生成正常场景测试用例并执行

将刚才生成的用例代码中的params，data中的"{object_id}" 替换为OBJECTID， "{question_id}" 替换为 QUESTIONID

重新执行测试，需要保存html的报告，测试报告保存在results/access-normal中，报告后缀用时间戳区别开


重新开始对话
# 清理上下文
/clear   
使用技能包miaoda-api-test-generator，为access模块生成异常场景测试用例并执行


# 清理上下文
/clear 
使用技能包miaoda-api-test-generator，读取api-data/asscess目录的文件，为access模块生成异常场景测试用例并执行
```


完整skill示例见：[文件页：baidu/acg2b-ep/acg-test  *claude-code-skills](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/acg2b-ep/acg-test/blob/claude-code-skills/.claude/skills/miaoda-api-test-generator/SKILL.md?t=mention&mt=doc&dt=sdk)

## 效果展示
运行过程摘要：

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
测试报告摘要：

![](/personal-site-mvp/img/doc-placeholder.svg "")
测试代码摘要：

![](/personal-site-mvp/img/doc-placeholder.svg "")


执行正常用例的测试结果摘要：

![](/personal-site-mvp/img/doc-placeholder.svg "")
执行异常用例的测试摘要

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 可以做的还有很多
## 接口用例设计
**解决需求**：手动编写接口用例耗时较长，并且还需手动添加到gitcase上

**解决方案**：编写接口用例设计skill来批量生成接口测试用例，输出格式按gitcase的excel模版输出，直接可导入到gitcase平台

**实现方式**：

1. 上文中的skill创建方式一，追加输入： 你是一个接口测试专家，负责设计接口测试用例并输出测试用例结果
2. 调整SKILL.md文件中的用例输出内容，添加参考文件即可

```
### 阶段3：用例输出
参考[reference/测试用例模版.xlsx]格式输出测试用例，
测试用例默认保存路径：api-test-case-output/API测试用例设计-{时间戳}.xlsx
```
**效果**：

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


## 代码性能专项优化小助手
解决需求：服务出现性能问题时，问题定义与回归测试时间均较久，是否可在编码阶段直接审计代码的性能，并给出优化方案。

解决方案：使用上文中的创建方式二的skill-creator工具，分阶段提出性能优化技能包的功能需求。

实现方案：由于skil-creator工具为官方英文，默认创建的skill也是英文，可在创建时追加此内容：skill的内容必须用中文编写； 或者在skill创建完毕后和他说：把这个skill的内容改成中文

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
效果：

输入： perform_test/views.py下的PerformTaskResultInfo视图的get接口审计下代码性能

输出：

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
200条大文本数据下

优化前本机测试平均耗时：647.9ms，优化后本机测试平均耗时：565.7ms，接口性能有明显提升。





更多的技能在等待你开发～



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
