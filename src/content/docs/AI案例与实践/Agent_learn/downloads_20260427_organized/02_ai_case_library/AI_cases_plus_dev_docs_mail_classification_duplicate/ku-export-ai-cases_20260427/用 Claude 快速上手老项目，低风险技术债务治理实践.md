---
title: "用 Claude 快速上手老项目，低风险技术债务治理实践"
description: "用 Claude 快速上手老项目，低风险技术债务治理实践"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\用 Claude 快速上手老项目，低风险技术债务治理实践.md"
---
用 Claude 快速上手老项目，低风险技术债务治理实践

#### 🧑‍🏫 案例作者：[@吴建业](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、测试、需求
#### 🔧 使用工具：Claude
#### 📒 案例概要：用Claude辅助老项目重构，低风险治理技术债务，快速认知、精准定位、增量改造。
# 用 Claude 快速上手老项目，低风险技术债务治理实践
## 摘要
接手一个运行多年的老项目，往往意味着面对数千行注释稀少的代码、散落各处的业务约定、以及长期积累的技术债务。传统做法是花费数周阅读代码、反复询问老同事，效率极低且风险极高——一旦理解偏差，重构就可能引入更严重的问题。

本文以百度内部 BIOS-Control（DCOS 变更平台）为真实案例，介绍如何将 Claude 作为"老项目领航员"，在不依赖完整文档、不破坏现有逻辑的前提下，快速建立项目认知、精准定位技术债务热点、并以低风险方式完成增量重构。核心主张是：**Claude 不是替代工程师的自动化系统，而是让工程师以更低成本、更高置信度做出正确决策的协作工具。**

## 1. 困境：接手老项目的真实挑战
### 1.1 BIOS-Control：一个典型的老项目
BIOS-Control 是百度 DCOS 团队维护的变更管理平台，负责调度大规模机器组的 BIOS/系统策略配置变更任务，已稳定运行数年。当新成员接手时，面对的是：

* **代码规模**：Python 代码 8,000+ 行，30+ 个核心模块，无完整设计文档
* **技术栈**：Python 2.7 + Flask 0.10.1 + SQLAlchemy 1.0.12，依赖版本严重落后
* **核心流程**：Dispatcher → Worker → Checker → LifecycleTracker 四进程协作，进程间通过共享队列和数据库传递状态
* **业务压力**：每日处理数千个机器变更任务，SLA 要求 99.5%，容错极低

最让人头疼的是几个"巨型文件"：

|**文件**|**行数**|**承担职责**|
|-|-|-|
|`lifecycle_tracker.py`|1403 行|生命周期追踪、告警聚合、超时检测、心跳管理|
|`checker.py`|970+ 行|并发检查、阈值判断、状态更新、结果汇集|
|`dispatcher.py`|820 行|任务分发、进程池管理、冲突检测、审批检查|

这类代码的典型问题不是"写错了"，而是"写对了但没人敢动"——逻辑正确，但职责混乱、测试覆盖率极低（核心模块平均不足 15%），任何修改都可能牵一发动全身。

### 1.2 技术债务的真实影响
以近期最典型的案例为例：DCOS-3497 需求（告警噪声处理）在 5 次迭代中产生了 5 个连续提交（`5a621c7`、`9f82ae5`、`11efebd`、`fff9e9c`、`4bd24dd`），每次修改都在"打补丁"，根本原因是 `lifecycle_tracker.py` 中的告警聚合逻辑（第 1235-1302 行）将"查库"、"构建文案"、"发 HTTP 请求"、"更新状态"四种职责混在一个 68 行的方法里，圈复杂度达到 18，任何人改动都如履薄冰。

**技术债务的代价不是抽象的**，在 BIOS-Control 上体现为：

* 新成员上手周期超过 2 周，且仍然"不敢随便改"
* 告警相关 Bug 的平均修复时间（MTTR）超过 2 小时
* 每次需求迭代，工程师需要在上千行代码中反复确认影响范围

## 2. 转变：用 Claude 建立项目认知
### 2.1 第一步：让 Claude 读懂项目，而不是你独自硬啃
接手老项目的第一个障碍是"不知道从哪里开始读"。传统做法是从 `main` 或入口文件开始，逐层追踪，费时且容易迷失。使用 Claude 的正确姿势是**提供结构性上下文，让 Claude 帮你构建认知框架**。

**第一轮对话：理解整体架构**

将项目的目录结构、关键文件列表以及 README 提供给 Claude，要求它描述系统的核心流程：

```
我接手了一个 Python 项目，请根据以下文件结构和关键代码帮我理解：
1. 这个系统的核心业务是什么？
2. 数据/任务的流转路径是什么（从触发到完成）？
3. 哪些模块是核心模块，哪些是辅助模块？
4. 存在哪些明显的架构风险？

[粘贴目录结构 + bc/service/ 下各文件的类名和方法签名]
```
Claude 的回答帮助快速建立了这样的认知框架：

```
核心任务流：
  HTTP 请求 (views/)
    → 创建 BiosTask 记录 (models/task.py)
    → Dispatcher 轮询 READY 状态任务入队 (service/dispatcher.py)
    → Worker 从队列取任务，执行 BaseTask.process() (service/worker.py)
    → 执行结果写回数据库
    → Checker 异步验证策略变更结果 (service/checker.py)
    → LifecycleTracker 追踪机器同步状态 (service/lifecycle_tracker.py)

架构风险：
  - LifecycleTracker 职责过重，单文件 1403 行
  - 进程间状态共享依赖数据库轮询，存在竞态风险
  - Python 2.7 依赖约束限制重构空间
```
这个认知框架用传统方式需要 1-2 天，使用 Claude 只需要 30 分钟。

**第二轮对话：深入理解关键模块的隐性约定**

老项目最危险的不是复杂逻辑，而是**隐性约定**——那些没有注释、但所有人"都知道"的规则。`base_task.py` 中有一个典型例子：

```
def __setattr__(self, k, v):
    if k == 'appender':
        if v:
            self.error_list.append(v)
            self.logger.warn(v)
    else:
        super(BaseTask, self).__setattr__(k, v)
```
将这段代码提供给 Claude，询问：

```
这个 __setattr__ 重写有什么特殊含义？
为什么用 'appender' 作为错误收集的触发器，而不是直接调用方法？
这对子类有什么隐性约束？
```
Claude 的分析揭示了关键约定：`appender`** 是全项目约定的错误上报接口**，所有继承 `BaseTask` 的子类（`MachineTask`、`GroupTask`、`StrategyTask`）都通过 `self.appender = error_msg` 上报错误。任何重构如果破坏了这个机制，就会导致错误静默丢失。

这类隐性约定，传统方式需要"踩坑"后才能发现，Claude 帮助在动手前就识别了风险。

### 2.2 快速定位技术债务：让 Claude 做"第一轮诊断"
不需要搭建复杂的分析系统，可以直接将可疑文件交给 Claude 进行初步诊断：

```
请分析以下代码文件，指出：
1. 违反单一职责原则的方法（一个方法做了多件事）
2. 圈复杂度可能偏高的方法（大量嵌套 if/for）
3. 难以单元测试的逻辑（副作用与业务逻辑混合）
4. Python 2.7 特有的遗留写法

[粘贴 lifecycle_tracker.py 的核心部分]
```
Claude 针对 `lifecycle_tracker.py` 的诊断结果（节选）：

```
高风险方法：_send_aggregated_alerts（第 1235-1302 行）
该方法同时承担四种职责：数据库查询、告警文案构建、HTTP 发送、状态更新。这使得它：
不可单独测试：测试任何一个逻辑分支都需要 mock 数据库和 HTTP 请求
修改风险高：每次修改都必须理解所有四种职责的交互
圈复杂度估计 ≥ 15：存在多层 if-else 和循环嵌套
建议优先级：高（结合你提到的近期 5 次迭代仍未解决告警噪声问题，说明此处是根因）
```
这份诊断与实际情况高度吻合，而且 Claude 自动将"近期高频变更"与"代码质量问题"关联起来，给出了优先级判断，这是静态扫描工具无法做到的。

## 3. 核心：低风险的增量重构实践
### 3.1 重构的最大风险不是"改错"，而是"改了什么不知道"
老项目重构失败的最常见原因不是技术能力不足，而是**边界不清**：不知道这段代码还被谁调用、不知道某个特殊值的含义、不知道某个异常分支对应什么业务场景。

使用 Claude 辅助重构的核心价值，在于在每次动手前**把边界说清楚**。

### 3.2 实战：重构告警聚合逻辑（低风险四步法）
以 `_send_aggregated_alerts` 为例，演示完整的低风险重构流程。

**第一步：让 Claude 描述现有代码的行为（建立基线）**

在重构之前，先让 Claude 用自然语言描述现有代码做了什么：

```
请用自然语言，以"当...时，系统会..."的格式，
完整描述以下方法的行为逻辑，包括所有分支和边界条件。
不要解释代码，只描述行为。

[粘贴 _send_aggregated_alerts 完整代码]
```
Claude 的描述（节选）：

```
当系统扫描到有已过期、尚未发送的告警聚合记录时：
对每条记录，根据其 agent_status 字段构建不同格式的告警文案：
若为 ERROR/DEAD，文案包含机器 IP 和时间戳
否则，使用简略文案
向外部群（alert_receiver）发送 basic 格式告警
向内部群（alert_internal_receiver）发送 enhanced 格式告警（含更多元数据）
仅当两个群都发送成功时，才将该记录标记为已发送
若任意发送失败，记录保持未发送状态，下次巡检时重试
```
**这个"两个群都成功才标记"的细节至关重要**——如果重构时遗漏了这个约束，就会出现"只发了内部群、外部群没收到，但记录被标记为已发送"的静默故障。Claude 的行为描述在重构前就把这个风险暴露出来了。

**第二步：让 Claude 提出重构方案，并要求它识别风险**

```
基于上述行为描述，请提出一个重构方案，目标是：
1. 将四种职责拆分为独立方法
2. 使告警文案构建逻辑可以独立单元测试（无需 mock HTTP）
3. 保持所有行为不变，特别是"两群都成功才标记"的原子性语义

请同时指出：
- 重构中最容易出错的地方
- 哪些逻辑绝对不能改变
- 建议的测试验证方案

约束：必须兼容 Python 2.7
```
Claude 给出的重构方案（核心部分）：

```
def _fetch_pending_agg_records(self, now):
    """职责：数据访问层，查询待发送记录"""
    return lifecycle_iface.list_expired_pending_aggs(now)

def _build_alert_payload(self, agg, mode='basic'):
    """职责：纯函数，构建告警请求体（无副作用，可独立测试）
    
    注意：这里有意设计为纯函数——
    不依赖 self 以外的外部状态，便于 mock agg 对象进行单元测试
    """
    description = self._build_alert_description(agg, mode)
    receiver = (self.alert_receiver if mode == 'basic'
                else self.alert_internal_receiver)
    return {
        'appId': self.alert_app_id,
        'token': self.alert_token,
        'alertList': [{
            'channel': self.alert_channel,
            'description': description,
            'receiver': receiver,
        }]
    }

def _dispatch_dual_alert(self, agg_id, basic_payload, enhanced_payload):
    """职责：发送双通道告警，返回是否全部成功
    
    关键约束（来自原始逻辑）：
    两个通道都发送成功才返回 True，保持原子性语义
    """
    headers = self._get_alert_headers()
    basic_ok = self._do_send_alert(basic_payload, headers, agg_id, 'basic')
    enhanced_ok = self._do_send_alert(enhanced_payload, headers, agg_id, 'enhanced')
    return basic_ok and enhanced_ok

def _send_aggregated_alerts(self):
    """协调者：编排告警发送流程（圈复杂度：18 → 4）"""
    now = datetime.datetime.now()
    for agg in self._fetch_pending_agg_records(now):
        basic_payload = self._build_alert_payload(agg, mode='basic')
        enhanced_payload = self._build_alert_payload(agg, mode='enhanced')
        if self._dispatch_dual_alert(agg.id, basic_payload, enhanced_payload):
            lifecycle_iface.mark_agg_sent(agg.id)
```
Claude 同时指出了三个最容易出错的地方：

1. `_dispatch_dual_alert` 必须保持 `and` 而非 `or` 的逻辑
2. `_build_alert_description` 中对 `agent_status` 的判断逻辑必须原样保留，不要"顺手优化"
3. Python 2.7 下字符串拼接使用 `%` 而非 f-string

**第三步：让 Claude 生成验证测试（先有测试，再执行重构）**

重构前先让 Claude 根据行为描述生成测试，作为"安全网"：

```
请根据第一步的行为描述，为重构后的 _build_alert_payload 生成单元测试。
要求：
1. 覆盖 basic 和 enhanced 两种 mode
2. 覆盖 agent_status 为 ERROR/DEAD 和其他值的分支
3. 不依赖真实数据库或网络请求
4. 使用 Python 2.7 的 unittest 语法
```
生成的测试示例：

```
import unittest
from mock import MagicMock, patch

class TestBuildAlertPayload(unittest.TestCase):

    def _make_tracker(self):
        tracker = LifecycleTracker.__new__(LifecycleTracker)
        tracker.alert_app_id = 'test_app'
        tracker.alert_token = 'test_token'
        tracker.alert_channel = 'test_channel'
        tracker.alert_receiver = 'external_group'
        tracker.alert_internal_receiver = 'internal_group'
        return tracker

    def _make_agg(self, agent_status='ERROR'):
        agg = MagicMock()
        agg.agent_status = agent_status
        agg.machine_count = 5
        return agg

    def test_basic_mode_routes_to_external_receiver(self):
        tracker = self._make_tracker()
        payload = tracker._build_alert_payload(self._make_agg(), mode='basic')
        self.assertEqual(payload['alertList'][0]['receiver'], 'external_group')

    def test_enhanced_mode_routes_to_internal_receiver(self):
        tracker = self._make_tracker()
        payload = tracker._build_alert_payload(self._make_agg(), mode='enhanced')
        self.assertEqual(payload['alertList'][0]['receiver'], 'internal_group')

    def test_app_id_and_token_present(self):
        tracker = self._make_tracker()
        payload = tracker._build_alert_payload(self._make_agg(), mode='basic')
        self.assertEqual(payload['appId'], 'test_app')
        self.assertEqual(payload['token'], 'test_token')
```
**先写测试再重构**，确保每一步都有可验证的安全网，这是低风险重构的关键。

**第四步：执行重构 → 运行测试 → 让 Claude 做 diff 审查**

完成代码修改后，将 diff 发给 Claude 做最终检查：

```
以下是重构前后的 diff，请确认：
1. 行为是否与第一步的描述完全一致
2. 是否有任何遗漏的边界条件
3. "两群都成功才标记"的原子性是否被保留

[粘贴 git diff 输出]
```
这一步相当于一次"AI Code Review"，专注于行为等价性，而非代码风格，是传统 Code Review 中最难做好的部分。

### 3.3 重构效果
完成 `_send_aggregated_alerts` 的重构后，可量化的改善：

|**指标**|**重构前**|**重构后**|
|-|-|-|
|圈复杂度（CC）|18|4|
|方法行数|68 行（单体）|4 个方法，各 8-15 行|
|单元测试覆盖率|12%（需 mock 数据库+HTTP）|78%（`_build_alert_payload` 是纯函数）|
|DCOS-3497 后续需求修改时间|平均 3 小时（含理解时间）|平均 40 分钟|

## 4. 进阶：Claude 辅助技术债务的系统性治理
### 4.1 用 Claude 制定有优先级的治理计划
不要试图一次性重构所有模块。用 Claude 帮助排优先级：

```
以下是 BIOS-Control 项目近期的 git log 和各文件的代码行数：

[粘贴 git log --stat 输出]
[粘贴各文件行数统计]

请根据"变更频率 × 代码复杂度 = 治理优先级"的原则，
给出一个按优先级排列的重构计划，并说明每个模块的重构风险等级。
```
Claude 综合代码结构和变更历史，给出的优先级排序：

```
优先级 1（立即治理）：lifecycle_tracker.py 告警聚合逻辑
  - 近 30 天变更 5 次（DCOS-3497 系列），说明在持续被修改
  - 圈复杂度高，测试覆盖率低
  - 重构风险：中（可通过先写测试降低风险）

优先级 2（下个迭代）：dispatcher.py 任务冲突检测逻辑
  - __load_status_task_list 方法过长，职责混合
  - 变更频率中等，但任何 bug 直接影响任务调度 SLA
  - 重构风险：高（建议拆分前先补充集成测试）

优先级 3（季度级）：整体 Python 2→3 迁移
  - 影响全局，风险最高
  - 建议先完成模块级重构，再推进运行时迁移
  - 重构风险：极高（建议渐进式迁移策略）
```
### 4.2 让 Claude 识别"危险的相似代码"
老项目中常见的另一类技术债务是**重复逻辑散落各处**，修复一处而遗漏其他处。

```
以下两段代码来自 worker.py 和 dispatcher.py，
请分析它们是否有重复的业务逻辑，
并建议是否可以安全地提取为公共函数：

[粘贴两段代码]
```
Claude 分析发现 `worker.py` 的邮件通知逻辑与 `dispatcher.py` 的告警逻辑存在约 70% 的结构相似度，但同时指出了一个关键差异：worker 发送的是"任务完成"通知，dispatcher 发送的是"系统异常"告警，虽然代码结构相似，但语义不同，**不建议强行合并**，而是提取公共的 HTTP 发送基础设施，保留各自的业务逻辑。

这类"看起来像重复，但不应该合并"的判断，是 Claude 超越传统相似性分析工具的核心能力。

### 4.3 处理 Claude 的局限性：如何让它更准确
Claude 并非万能，在老项目的特殊上下文中会出现误判。以下是实践中总结的几个关键技巧：

**技巧一：主动告知项目约定**

在每次重要对话开始时，提供一段"项目约定说明"：

```
在分析以下代码前，请了解以下项目约定：
1. self.appender = msg 是错误上报的约定接口，不能改为普通方法调用
2. pre_task_id == -1 表示无前置任务依赖，而非错误值
3. TaskStatus.RUNNING/FINISH/SUCCESS/FAILURE 是状态机的合法状态，
   FINISH 与 SUCCESS 的区别是...
4. 本项目使用 Python 2.7，不支持 f-string、type hints 等 Python 3 特性
```
**技巧二：要求 Claude 说明假设**

```
在给出重构建议前，请列出你对这段代码所做的假设，
特别是那些你不确定的地方。
```
这迫使 Claude 暴露其不确定性，工程师可以针对性地确认或纠正。

**技巧三：分段提交，每次只改一件事**

不要一次性让 Claude 重构整个文件。每次聚焦一个方法的一个问题，改完验证后再进行下一个。这不仅降低风险，也让 Claude 的输出更精准。

### 4.4 将 Claude 融入日常开发流程
技术债务治理不应该是一次性的"大重构"，而应融入日常：

**PR 创建时**：将改动文件发给 Claude，询问"这次修改是否引入了新的技术债务？是否有更简洁的写法？"

**接手陌生模块时**：先让 Claude 生成该模块的行为描述，再开始修改，建立理解基线。

**发现 Bug 后**：让 Claude 分析"这个 Bug 是由哪类代码结构性问题导致的？类似结构在其他地方还有吗？"

## 5. 实践效果与经验总结
### 5.1 量化收益
经过约 3 个月将 Claude 融入 BIOS-Control 的日常开发，主要改善如下：

|**指标**|**引入前**|**引入后**|**改善**|
|-|-|-|-|
|新成员理解核心流程时间|2 周|3 天|-79%|
|告警相关 Bug MTTR|2.1 小时|0.6 小时|-71%|
|核心模块（告警）测试覆盖率|12%|78%|+550%|
|重构引入新 Bug 次数（季度）|3 次|0 次|-100%|
|最大方法圈复杂度|18|7|-61%|

值得强调的是：**重构引入新 Bug 次数降至 0** 并非因为减少了重构量，而是因为"先让 Claude 描述行为再重构"的工作方式让工程师在动手前就清楚了边界，避免了因理解偏差导致的回归。

### 5.2 核心经验：Claude 改变的不是技术，而是工作方式
总结实践经验，Claude 带来的最大价值不在于生成了多少行代码，而在于**改变了工程师面对老项目时的工作方式**：

|**旧工作方式**|**新工作方式**|
|-|-|
|独自硬啃代码，建立理解需要数天|Claude 辅助快速建立认知框架，数小时内|
|凭感觉判断重构优先级|结合变更历史和代码结构，有依据地排序|
|重构前靠经验估算风险|重构前让 Claude 显式描述行为，消除不确定性|
|先改代码，后补测试（或不补）|先生成验证测试，再执行重构|
|Code Review 关注风格，行为等价靠人肉验证|AI diff 审查专注行为等价性|

### 5.3 边界：什么情况下不应该依赖 Claude
Claude 并非银弹，以下场景需要保持谨慎：

* **涉及分布式一致性的逻辑**：`dispatcher.py` 中的任务队列竞态处理、`checker.py` 中的并发检查逻辑，Claude 有时会给出"看起来正确"但在并发场景下有微妙问题的建议。这类代码的重构必须辅以充分的并发测试。
* **业务含义极其特殊的代码**：类似 `TaskStatus.FINISH` 和 `TaskStatus.SUCCESS` 的细微语义区分，Claude 无法从代码本身推断，必须由领域专家确认。
* **Python 2/3 兼容性边界**：Claude 偶尔会生成 Python 3 语法，需要人工审查。建议在 Prompt 中重复强调运行时约束。

## 6. 总结
用 Claude 治理技术债务，**不是把重构交给 AI 自动完成，而是让工程师以更低风险、更高置信度做好每一个决策**。

核心方法论可以归纳为四点：

1. **先理解，再动手**：用 Claude 建立项目认知框架和行为基线，消除"不知道改了什么"的最大风险来源
2. **先测试，再重构**：让 Claude 根据行为描述生成验证测试，重构前就建好安全网
3. **小步快跑**：每次只聚焦一个方法的一个问题，改完验证后再进行下一个
4. **人机协作**：Claude 提方案、识别风险，工程师做决策、确认边界，AI 的输出永远需要人的审查

对于 BIOS-Control 这样的老项目，这套方法论将技术债务治理从"高风险大工程"变成了"可持续的日常实践"，让每个工程师都能在不依赖完整文档、不熟悉全局代码的情况下，安全地改善代码质量。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
