---
title: "ITP API 实时任务 vs 定时任务调度路径对比"
description: "本文档详细对比了通过 API 触发实时任务和定时计划任务的调度路径差异。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\api_realtime_vs_scheduled_execution.md"
---
# ITP API 实时任务 vs 定时任务调度路径对比

本文档详细对比了通过 API 触发实时任务和定时计划任务的调度路径差异。

## 一、API 触发实时任务执行路径

### 1.1 触发场景
- **手动执行计划**：用户在 Web 界面点击"运行"按钮，或通过 API 调用 `/itp/testplan/{id}/run`
- **目的**：立即执行测试计划，需要快速响应

### 1.2 完整调度路径

```
API/Web 请求
    ↓
ITP-Web (TestPlanAction.run)
    ↓
TestPlanService.makeRecord (创建 PlanExecution 记录)
    ↓
LtsClientFacade.runPlan
    ↓
ItpJobClient.submitRealtimeJob
    ↓
LTS JobClient.submitJob (提交实时任务)
    ↓
【LTS JobTracker】
    ├─ 接收任务
    ├─ 持久化到 ExecutableJobQueue（可执行任务队列）
    └─ 根据负载进行任务调度
    ↓
【LTS TaskTracker】
    ├─ 从 JobTracker 拉取/接收任务
    ├─ ItpJobRunner 执行任务
    └─ 回报执行结果
```

### 1.3 关键代码路径

#### 入口：TestPlanAction.run
```java
// 文件：itp-web/src/main/java/com/baidu/itp/web/action/TestPlanAction.java
@RequestMapping(value = "/{id}/run", method = RequestMethod.GET)
public ResponseEntity<Map<String, Object>> run(@PathVariable Integer id, ...) {
    // 1. 生成 record
    PlanExecution record = testPlanService.makeRecord(executeBo, record);
    
    // 2. 执行风险检查（异步）
    riskTaskAsyncService.doAsyncForPlan(record, executeBo, report);
    
    return success();
}
```

#### 核心调度：LtsClientFacade.runPlan
```java
// 文件：itp-web/src/main/java/com/baidu/itp/web/facade/LtsClientFacade.java
public TaskResult runPlan(Integer planId, String user, ...) {
    TestPlan plan = testPlanService.queryTestPlanById(planId);
    
    // 提交实时任务到 LTS
    String taskId = itpJobClient.submitRealtimeJob(
        planId, 
        record.getId(), 
        plan.getMachineGroup(),
        runLastTag, 
        runType, 
        newVersionMap, 
        versionName, 
        traceId, 
        user
    );
    
    if (taskId != null) {
        // 更新计划状态
        plan.setRunStatus(1);
        testPlanService.updateById(plan, true);
        planExecutionService.updateLtsInfoById(recordId, taskId);
    }
}
```

#### 任务提交：ItpJobClient.submitRealtimeJob
```java
// 文件：itp-web/src/main/java/com/baidu/itp/jobclient/ItpJobClient.java
public String submitRealtimeJob(Integer id, Integer recordId, ...) {
    JobClient jobClient = factoryBean.getObject();
    Job job = new Job();
    
    // 生成任务 ID
    job.setTaskId(genRealtimeTaskId(id));
    job.setParam("id", id.toString());
    job.setParam("recordId", recordId.toString());
    job.setParam("parallel", "1");
    
    // 设置 TaskTracker 节点组
    job.setTaskTrackerNodeGroup(
        taskTrackerGroupService.queryGroupName(machineGroup)
    );
    
    // 提交到 LTS（进入 ExecutableJobQueue）
    jobClient.submitJob(job);
    
    return job.getTaskId();
}
```

### 1.4 特点总结
- ✅ **经过 LTS JobTracker**：任务会进入 LTS 的 ExecutableJobQueue
- ✅ **任务持久化**：保证任务不丢失
- ✅ **负载均衡**：JobTracker 根据 TaskTracker 负载分配任务
- ✅ **容错能力**：执行节点宕机时可自动重试
- ⚠️ **不使用 Dubbo**：不走 Dubbo 直连通道
- ⚠️ **有排队延迟**：需要等待 JobTracker 调度

---

## 二、API 触发定时计划执行路径

### 2.1 触发场景
- **配置定时任务**：用户在 Web 界面保存计划时设置 Cron 表达式
- **自动触发**：LTS JobTracker 内置的 Cron 调度器定时触发

### 2.2 完整调度路径

```
【配置阶段】
API/Web 请求
    ↓
ITP-Web (TestPlanAction.updateById)
    ↓
ItpJobClient.submitCrontabJob
    ↓
LTS JobClient.submitJob (设置 CronExpression)
    ↓
【LTS JobTracker】
    └─ 持久化到 CronJobQueue（定时任务队列）

【执行阶段】
【LTS JobTracker - 内置 Cron Timer】
    ├─ 定时检查 CronJobQueue
    ├─ 到达执行时间
    ├─ 生成执行任务
    └─ 提交到 ExecutableJobQueue
    ↓
【LTS TaskTracker】
    ├─ 从 JobTracker 拉取/接收任务
    ├─ ItpJobRunner 执行任务
    └─ 回报执行结果
```

### 2.3 关键代码路径

#### 配置入口：TestPlanAction.updateById
```java
// 文件：itp-web/src/main/java/com/baidu/itp/web/action/TestPlanAction.java
@RequestMapping(value = "/{id}", method = RequestMethod.PUT)
public ResponseEntity<Map<String, Object>> updateById(@RequestBody TestPlan testPlan, ...) {
    TestPlan preTestPlan = testPlanService.queryTestPlanById(id);
    
    if (testPlan.getTimeType() != null && testPlan.getTimeType() == 1) {
        // 定时任务配置
        if (!Strings.isNullOrEmpty(testPlan.getTimePlan())) {
            // 提交定时任务到 LTS CronJobQueue
            ltsResponse = jobClient.submitCrontabJob(
                id,
                testPlan.getTimePlan(),
                testPlan.getMachineGroup(),
                preTestPlan.getProductId()
            );
        }
    }
}
```

#### 定时任务提交：ItpJobClient.submitCrontabJob
```java
// 文件：itp-web/src/main/java/com/baidu/itp/jobclient/ItpJobClient.java
public Response submitCrontabJob(Integer id, String cronExpression, ...) {
    JobClient jobClient = factoryBean.getObject();
    Job job = new Job();
    
    // 生成定时任务 ID
    job.setTaskId(genCrontabTaskId(id));
    job.setParam("id", id.toString());
    job.setParam("parallel", "1");
    
    // 设置 Cron 表达式（关键！）
    job.setCronExpression(cronExpression);
    
    // 添加随机秒数和分钟数，实现削峰
    // 例如：将 "0 0 * * * ?" 随机化为 "23 5 * * * ?"
    
    job.setTaskTrackerNodeGroup(
        taskTrackerGroupService.queryGroupName(machineGroup)
    );
    
    // 先删除旧的定时任务
    jobClient.cancelJob(genCrontabTaskId(id), groupName);
    
    // 提交到 LTS（进入 CronJobQueue）
    return jobClient.submitJob(job);
}
```

### 2.4 特点总结
- ✅ **两阶段提交**：
  - **配置阶段**：任务提交到 CronJobQueue
  - **执行阶段**：Cron Timer 触发后提交到 ExecutableJobQueue
- ✅ **准时触发**：LTS 内置 Cron 调度器保证准时执行
- ✅ **削峰处理**：随机化秒数和分钟数，避免同一时刻大量任务
- ✅ **分布式调度**：保证不重复、不漏跑
- ⚠️ **不使用 Dubbo**：完全依赖 LTS 调度
- ⚠️ **配置与执行分离**：配置时不立即执行

---

## 三、调试任务执行路径（对比参考）

### 3.1 触发场景
- **用例调试**：用户在 Web 界面点击"调试"按钮
- **目的**：立即看到单个用例的执行结果，要求毫秒级响应

### 3.2 完整调度路径

```
API/Web 请求
    ↓
ITP-Web (TestNodeAction.run / DebugAction)
    ↓
LtsClientFacade（判断为调试模式）
    ↓
【绕过 LTS】直接调用 Dubbo RPC
    ↓
【ITP-TaskTracker】
    ├─ ItpJobDirectRunner (Dubbo Service 实现)
    ├─ 本机线程池立即执行
    └─ ItpJobRunner.run
```

### 3.3 特点总结
- ❌ **不经过 LTS JobTracker**：完全绕过 LTS 调度
- ✅ **使用 Dubbo 直连**：通过 `com.baidu.itp.core.submit.JobSubmit` 接口
- ✅ **毫秒级响应**：直接在 TaskTracker 本机线程池执行
- ⚠️ **无容错保证**：TaskTracker 宕机则任务丢失
- ⚠️ **无负载均衡**：直连到指定 TaskTracker

---

## 四、三种执行方式对比表

| 维度 | **API 实时任务** | **定时计划任务** | **调试任务** |
|:---|:---|:---|:---|
| **触发方式** | API/Web 手动触发 | LTS Cron Timer 自动触发 | Web 调试按钮 |
| **入口** | `TestPlanAction.run` | `TestPlanAction.updateById` | `TestNodeAction.run` |
| **调度通道** | LTS (Realtime) | LTS (Cron) | Dubbo (Direct) |
| **队列** | ExecutableJobQueue | CronJobQueue → ExecutableJobQueue | 无队列（直连） |
| **是否经过 JobTracker** | ✅ 是 | ✅ 是（两阶段） | ❌ 否 |
| **是否使用 Dubbo** | ❌ 否 | ❌ 否 | ✅ 是 |
| **任务持久化** | ✅ 是 | ✅ 是 | ❌ 否 |
| **负载均衡** | ✅ 是 | ✅ 是 | ❌ 否 |
| **容错能力** | ✅ 高（自动重试） | ✅ 高（自动重试） | ❌ 低（无重试） |
| **响应延迟** | 中（需排队） | 不适用（定时触发） | 低（毫秒级） |
| **适用场景** | 批量任务、长时间运行 | 定时自动化测试 | 单用例快速验证 |
| **核心考量** | 稳定性、容错 | 准确性、削峰 | 低延迟、快速反馈 |

---

## 五、核心组件说明

### 5.1 LTS (Light Task Scheduler)
- **JobClient**：任务提交客户端（ITP-Web 使用）
- **JobTracker**：调度中心，负责任务分发和调度
  - **CronJobQueue**：定时任务队列
  - **ExecutableJobQueue**：可执行任务队列
  - **Cron Timer**：内置定时触发器
- **TaskTracker**：任务执行节点（ITP-TaskTracker）

### 5.2 ITP 核心组件
- **ITP-Web**：前端接口层
  - `TestPlanAction`：计划管理入口
  - `ItpJobClient`：封装 LTS JobClient
  - `LtsClientFacade`：任务提交门面
- **ITP-TaskTracker**：任务执行层
  - `ItpJobRunner`：LTS 任务执行器
  - `ItpJobDirectRunner`：Dubbo 直连执行器

### 5.3 Dubbo 接口
- **接口定义**：`com.baidu.itp.core.submit.JobSubmit`
- **实现类**：`ItpJobDirectRunner`
- **用途**：仅用于调试任务的快速通道

---

## 六、关键差异总结

### API 实时任务 vs 定时任务

| 对比项 | API 实时任务 | 定时任务 |
|:---|:---|:---|
| **提交阶段** | 立即提交到 ExecutableJobQueue | 提交到 CronJobQueue |
| **执行阶段** | JobTracker 立即调度 | Cron Timer 定时触发后调度 |
| **调用链路** | Web → JobClient → ExecutableJobQueue → TaskTracker | Web → JobClient → CronJobQueue<br>Timer → ExecutableJobQueue → TaskTracker |
| **是否插队** | 否（排队执行） | 否（定时触发） |
| **典型延迟** | 秒级～分钟级 | 按 Cron 表达式精确触发 |

### 核心结论
✅ **API 触发实时任务** 和 **定时计划任务** 都严格遵循 **LTS 标准调度路径**  
✅ 两者都经过 **LTS JobTracker** 进行调度  
✅ 两者都**不使用 Dubbo** 直连通道  
❌ **只有调试任务**使用 Dubbo 绕过 LTS 实现毫秒级响应

---

## 七、流程图总结

```
┌─────────────────────────────────────────────────────────────────────┐
│                         ITP 任务调度架构                              │
└─────────────────────────────────────────────────────────────────────┘

【调试任务 - Dubbo 直连通道】
Web (Debug) ──Dubbo RPC──> TaskTracker (ItpJobDirectRunner) ──线程池──> 立即执行

【实时任务 - LTS 标准通道】
Web (Run) ──submitRealtimeJob──> JobTracker (ExecutableJobQueue) ──调度──> TaskTracker

【定时任务 - LTS Cron 通道】
Web (Config) ──submitCrontabJob──> JobTracker (CronJobQueue)
                                          ↓
                                    Cron Timer 定时触发
                                          ↓
                              ExecutableJobQueue ──调度──> TaskTracker
```

---

## 八、代码关键位置索引

| 功能 | 文件路径 | 关键方法 |
|:---|:---|:---|
| **实时任务入口** | `itp-web/.../TestPlanAction.java` | `run(@PathVariable Integer id)` |
| **定时任务配置** | `itp-web/.../TestPlanAction.java` | `updateById(...)` |
| **实时任务提交** | `itp-web/.../ItpJobClient.java` | `submitRealtimeJob(...)` |
| **定时任务提交** | `itp-web/.../ItpJobClient.java` | `submitCrontabJob(...)` |
| **调度门面** | `itp-web/.../LtsClientFacade.java` | `runPlan(...)` |
| **Dubbo 实现** | `itp-tasktracker/.../ItpJobDirectRunner.java` | `submit(JobWrapper)` |
| **LTS 执行器** | `itp-tasktracker/.../ItpJobRunner.java` | `run(...)` |

---

**文档版本**：v1.0  
**更新时间**：2026-01-28  
**维护者**：ITP 架构组
