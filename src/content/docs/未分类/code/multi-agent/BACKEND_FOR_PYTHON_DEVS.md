---
title: "给Python开发者的Java后端指南"
description: "快速上手Java Spring Boot后端开发和调试"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\BACKEND_FOR_PYTHON_DEVS.md"
---
# 给Python开发者的Java后端指南

> 快速上手Java Spring Boot后端开发和调试

---

## 目录

1. [Java后端快速入门](#1-java后端快速入门)
2. [后端核心类地图](#2-后端核心类地图)
3. [配置文件对照](#3-配置文件对照)
4. [如何添加新任务类型](#4-如何添加新任务类型)
5. [常见问题排查](#5-常见问题排查)

---

## 1. Java后端快速入门

### 1.1 Spring Boot是什么？

**对比FastAPI**：

| 概念 | FastAPI (Python) | Spring Boot (Java) |
|------|------------------|-------------------|
| 框架定位 | 轻量级Web框架 | 企业级应用框架 |
| 路由定义 | `@app.get("/api")` | `@GetMapping("/api")` |
| 依赖注入 | `Depends()` | `@Autowired` |
| 数据模型 | `Pydantic BaseModel` | `@Entity` / POJO |
| ORM | SQLAlchemy / Tortoise | MyBatis Plus |
| 启动方式 | `uvicorn main:app` | `java -jar app.jar` |

### 1.2 关键注解含义

#### `@RestController` - 定义API控制器

```java
// Java
@RestController
@RequestMapping("/api")
public class UserController {
    @GetMapping("/users")
    public Response<List<User>> getUsers() { }
}
```

```python
# 对应的Python (FastAPI)
from fastapi import FastAPI
app = FastAPI()

@app.get("/api/users")
async def get_users():
    pass
```

---

#### `@PostMapping` - 定义POST接口

```java
// Java
@PostMapping("/create")
public Response<Long> create(@RequestBody UserReq req) {
    return Response.success(userId);
}
```

```python
# Python
@app.post("/create")
async def create(req: UserReq):
    return {"success": True, "data": user_id}
```

---

#### `@Service` - 业务逻辑层

```java
// Java
@Service
public class UserService {
    public Long createUser(UserReq req) {
        // 业务逻辑
    }
}
```

```python
# Python (不需要装饰器，直接定义类)
class UserService:
    def create_user(self, req: UserReq) -> int:
        # 业务逻辑
        pass
```

---

#### `@Autowired` - 依赖注入

```java
// Java
@RestController
public class UserController {
    @Autowired  // Spring自动注入UserService实例
    private UserService userService;

    @PostMapping("/create")
    public Response<Long> create(@RequestBody UserReq req) {
        return Response.success(userService.createUser(req));
    }
}
```

```python
# Python (FastAPI)
from fastapi import Depends

@app.post("/create")
async def create(
    req: UserReq,
    user_service: UserService = Depends()  # 依赖注入
):
    user_id = await user_service.create_user(req)
    return {"success": True, "data": user_id}
```

---

### 1.3 如何找到API入口（Controller）

#### 方法1: 根据URL路径查找

假设你知道前端调用的URL是：`POST /core/lumos/v2/task/generate/userStoryDoc2TodoFeatureDoc`

**步骤**：
1. 去掉context-path：`/core`
2. 剩余路径：`/lumos/v2/task/generate/userStoryDoc2TodoFeatureDoc`
3. 搜索关键字：`userStoryDoc2TodoFeatureDoc`
4. 找到Controller文件

**实际操作**：
```bash
# 在后端项目目录
cd /Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code/baidu/qamate-server/core
grep -r "userStoryDoc2TodoFeatureDoc" --include="*.java" src/
```

**结果**：
```
src/main/java/com/baidu/qamate/core/v2/lumosgmt/controller/LumosController.java
```

#### 方法2: 根据功能名称查找

假设你想找"生成技术设计"的接口：

1. 猜测可能的关键字：`TodoFeatureDoc`, `TRD`, `Design`
2. 全局搜索Controller类

```bash
find src/ -name "*Controller.java" | xargs grep -l "TodoFeatureDoc"
```

#### 方法3: 查看Swagger文档（推荐）

访问：`https://qamate.baidu-int.com/core/swagger-ui.html`

可视化查看所有接口列表。

---

### 1.4 如何追踪业务逻辑（Service）

找到Controller后，看它调用了哪个Service：

```java
// LumosController.java
@RestController
@RequestMapping("/lumos/v2")
public class LumosController {

    @Autowired
    private TodoFeatureDocService todoFeatureDocService;  // ← 这里注入的Service

    @PostMapping("/task/generate/userStoryDoc2TodoFeatureDoc")
    public Response<Long> generateTask(@RequestBody TaskReq req) {
        // 调用Service方法
        return Response.success(
            todoFeatureDocService.generateUserStoryDoc2TodoFeatureDoc(req)
        );
    }
}
```

**追踪路径**：
1. 找到接口：`LumosController.generateTask()`
2. 看到调用：`todoFeatureDocService.generateUserStoryDoc2TodoFeatureDoc()`
3. 跳转到：`TodoFeatureDocServiceImpl.java`
4. 查看具体实现

**快捷键**（IDEA）：
- Mac: `Cmd + Click` 跳转到方法定义
- Windows: `Ctrl + Click`

---

## 2. 后端核心类地图

### 2.1 KirinServiceImpl - 调用Kirin的核心逻辑

**位置**: `core/src/main/java/com/baidu/qamate/core/v2/lumosgmt/service/impl/KirinServiceImpl.java`

**作用**: 你的Python代码是被这个类调用的！

#### 关键方法

```java
/**
 * 异步调用Kirin平台
 * @param data 业务参数（会转成JSON传给你的Python代码）
 * @param taskEnum 任务类型枚举
 * @return Kirin taskId
 */
public Long asycCall(JSONObject data, KirinTaskEnum taskEnum) {
    // 1. 构造Kirin参数
    JSONObject kirinParam = new JSONObject();
    kirinParam.put("name", KirinConfig.NAME);       // "xiaolihua"
    kirinParam.put("token", KirinConfig.TOKEN);     // 认证token
    kirinParam.put("callback", "");
    kirinParam.put("parameter", data.toJSONString());  // 你的Python代码会收到这个

    // 2. 获取URL（根据环境和任务类型选择Tool ID）
    String url = kirinConfig.getUrl(taskEnum, KirinCallTypeEnum.ASYNC);
    // 例如：http://kirin.baidu-int.com/api/tool/215160

    // 3. POST请求
    var response = restTemplate.postForObject(url, kirinParam, String.class);

    // 4. 解析taskId
    JSONObject responseObject = JSONObject.parseObject(response);
    if (responseObject.getBoolean("status")) {
        return responseObject.getJSONObject("result").getLongValue("taskId");
    }

    return null;
}
```

```java
/**
 * 同步调用Kirin（会等待Python代码执行完成）
 * @return Python返回的结果字符串
 */
public String sycCall(JSONObject data, KirinTaskEnum taskEnum) {
    // 类似异步调用，但Tool ID不同，会阻塞等待结果
}
```

```java
/**
 * 终止Kirin任务
 * @param taskId Kirin任务ID
 */
public Boolean killTask(Long taskId) {
    // 调用Kirin的kill接口
    String url = "http://kirin.baidu-int.com/api/cms/task/kill";
    // POST {taskId: xxx}
}
```

#### Python开发者需要知道的

1. **data参数** → 会变成你的`sys.argv[1]`（JSON字符串）
2. **taskId返回值** → 就是你的`sys.argv[2]`
3. **taskEnum** → 决定使用哪个Tool ID（Test环境215160，Online环境214909）

---

### 2.2 LumosController - 接收你的回调

**位置**: `core/src/main/java/com/baidu/qamate/core/v2/lumosgmt/controller/LumosController.java`

**作用**: 你的`QAMate.callback()`会POST到这里的接口

#### 回调接口列表

| 任务类型 | 回调URL | 对应Python任务 |
|---------|---------|---------------|
| PRD转用户故事 | `/prd2userStoryDoc/callback` | `PRD_TO_STORY` |
| 用户故事转设计 | `/userStoryDoc2TodoFeatureDoc/callback` | `STORY_TO_DESIGN` |
| TODO转代码 | `/todoFeatureDoc2Code/callback` | `TODO_TO_CODE` |
| 设计转TRD | `/todoFeatureDoc2Trd/callback` | `DESIGN_TO_TRD` |
| TRD转模板 | `/trd2Template/callback` | `TRD_TO_TEMPLATE` |
| 构建知识图谱 | `/buildRepoKnowledge/callback` | `BUILD_REPO_KNOWLEDGE` |

#### 典型回调接口实现

```java
@PostMapping("/task/generate/userStoryDoc2TodoFeatureDoc/callback")
public Response<Boolean> userStoryDoc2TodoFeatureDocCallback(
    @RequestBody KirinCommonCallback req) throws Exception {

    // 委托给Service层处理
    return Response.success(
        todoFeatureDocService.userStoryDoc2TodoFeatureDocCallback(req)
    );
}
```

#### Python回调时要传的数据

```java
// Java接收的数据结构
public class KirinCommonCallback {
    private Story2DesignKirinCallbackResp callbackResp;  // 你的回调数据

    public static class Story2DesignKirinCallbackResp {
        private Long docNodeId;      // 文档节点ID
        private Long kirinTaskId;    // Kirin任务ID
        private String username;     // 用户名
        private Integer code;        // 错误码（0=成功）
        private String msg;          // 消息
        private TaskResultDto taskResult;  // 任务结果
    }
}
```

**对应的Python代码**：
```python
data = {
    "callbackResp": {
        "docNodeId": 12345,
        "kirinTaskId": 123456,
        "username": "zhangsan",
        "code": 0,          # 0=成功，非0=失败
        "msg": "SUCCESS",
        "taskResult": {...}  # 你的结果数据
    }
}
```

---

### 2.3 KirinConfig - Tool ID配置

**位置**: `core/src/main/java/com/baidu/qamate/core/v2/lumosgmt/domain/constants/KirinConfig.java`

**作用**: 管理Kirin平台的Tool ID（决定执行哪个Python脚本）

#### 关键配置

```java
public class KirinConfig {
    // 工具名（固定）
    public static final String NAME = "xiaolihua";

    // 认证Token
    public static final String TOKEN = "190df4f275dd42a7b4716d8e56571743";

    // Tool ID配置
    // 测试环境
    private static final Long LUMOS_ASYNC_TOOL_ID_TEST = 215160L;
    private static final Long LUMOS_SYNC_TOOL_ID_TEST = 215208L;

    // 线上环境
    private static final Long LUMOS_ASYNC_TOOL_ID_ONLINE = 214909L;
    private static final Long LUMOS_SYNC_TOOL_ID_ONLINE = 214934L;

    // 获取Tool ID（根据环境和调用类型）
    public Long getToolId(KirinTaskEnum taskEnum, KirinCallTypeEnum callTypeEnum) {
        if ("online".equalsIgnoreCase(taskEnv)) {
            return callTypeEnum == KirinCallTypeEnum.SYNC
                ? LUMOS_SYNC_TOOL_ID_ONLINE
                : LUMOS_ASYNC_TOOL_ID_ONLINE;
        } else {
            return callTypeEnum == KirinCallTypeEnum.SYNC
                ? LUMOS_SYNC_TOOL_ID_TEST
                : LUMOS_ASYNC_TOOL_ID_TEST;
        }
    }
}
```

#### Python开发者需要知道的

1. **Tool ID** → Kirin根据这个找到对应的Python脚本路径
2. **TEST vs ONLINE** → 不同环境使用不同Tool ID
3. **ASYNC vs SYNC** → 异步/同步调用使用不同Tool ID

---

### 2.4 TodoFeatureDocServiceImpl - 处理回调业务

**位置**: `core/src/main/java/com/baidu/qamate/core/v2/lumosgmt/service/impl/TodoFeatureDocServiceImpl.java`

**作用**: 接收你的回调后，更新数据库、发送通知

#### 典型回调处理流程

```java
public Boolean userStoryDoc2TodoFeatureDocCallback(KirinCommonCallback req) {
    // 1. 解析回调数据
    Story2DesignKirinCallbackResp callbackResp = req.getCallbackResp();
    Long kirinTaskId = callbackResp.getKirinTaskId();
    Integer code = callbackResp.getCode();
    String msg = callbackResp.getMsg();

    // 2. 查询Kirin任务记录
    KirinTaskPo kirinTaskPo = kirinTaskService.queryByTaskId(kirinTaskId);

    // 3. 根据code判断成功/失败
    if (code == 0) {
        // ✅ 成功
        // 3.1 更新任务状态
        kirinTaskPo.setTaskStatus(TaskTRDStatusEnum.SUCCESS.getStatus());
        kirinTaskPo.setTaskResult(JSONObject.toJSONString(callbackResp));
        kirinTaskService.updateById(kirinTaskPo);

        // 3.2 保存业务数据（设计文档）
        TodoFeatureDocPo todoFeatureDocPo = ...;
        todoFeatureDocPo.setContent(callbackResp.getTaskResult().getContent());
        todoFeatureDocPo.setStatus(GenerateStatusEnum.DONE.getCode());
        todoFeatureDocService.updateById(todoFeatureDocPo);

        // 3.3 发送飞书通知
        hiGroupService.sendTaskFinishNotice(kirinTaskPo, docNodeId);

    } else {
        // ❌ 失败
        kirinTaskPo.setTaskStatus(TaskTRDStatusEnum.FAIL.getStatus());
        kirinTaskPo.setErrorMsg(msg);
        kirinTaskService.updateById(kirinTaskPo);
    }

    return true;
}
```

#### Python开发者需要关注的

- **code=0** → 后端认为任务成功
- **code≠0** → 后端认为任务失败，不会保存taskResult
- **taskResult** → 你的业务数据会保存到数据库

---

## 3. 配置文件对照

### 3.1 application.yml ↔ config.toml

#### Java后端（application.yml）

```yaml
# 位置: core/src/main/resources/application.yml

server:
  port: 8542                  # 后端服务端口

spring:
  datasource:
    # 数据库配置
    dynamic:
      datasource:
        newsource:            # 主数据库
          url: jdbc:mysql://...
          username: root
          password: xxx

trd:
  taskEnv: test              # 环境标识：test/online
```

#### Python（config.toml）

```toml
# 位置: /Users/zhuji_m4pro/code/multi-agent/baidu/multi-agent/code/conf/config.toml

[kirin]
name = "xiaolihua"
token = "190df4f275dd42a7b4716d8e56571743"
url = "http://kirin.baidu-int.com/api/tool/"

[database.neo4j]
uri = "bolt://neo4j.baidu-int.com:7687"
user = "neo4j"
password = "xxx"

[database.mysql]
host = "mysql.baidu-int.com"
port = 3306
user = "root"
password = "xxx"
database = "qamate_base"
```

---

### 3.2 数据库配置对比

#### Java（多数据源）

```yaml
spring:
  datasource:
    dynamic:
      datasource:
        newsource:              # 数据源1: 核心数据库
          url: jdbc:mysql://mysql1/core
        api-smart-dispatch:     # 数据源2: API调度库
          url: jdbc:mysql://mysql2/api_smart_dispatch
        oldsource:              # 数据源3: 旧数据库
          url: jdbc:mysql://mysql3/qamate_base
```

**使用方式**：
```java
@DS("newsource")  // 指定使用哪个数据源
public List<Entity> queryFromDB() { }
```

#### Python（单数据源）

```toml
[database.mysql]
host = "mysql.baidu-int.com"
port = 3306
database = "qamate_base"

# 如果需要多数据源，自己管理连接池
[database.mysql_secondary]
host = "mysql2.baidu-int.com"
database = "api_smart_dispatch"
```

---

### 3.3 Kirin配置对比

#### Java

```java
// 硬编码在KirinConfig.java
public static final String NAME = "xiaolihua";
public static final String TOKEN = "190df4f275dd42a7b4716d8e56571743";
private static final Long LUMOS_ASYNC_TOOL_ID_TEST = 215160L;
```

#### Python

```toml
# config.toml
[kirin]
name = "xiaolihua"
token = "190df4f275dd42a7b4716d8e56571743"

# Python代码中读取
config = toml.load("conf/config.toml")
KIRIN_NAME = config["kirin"]["name"]
```

---

### 3.4 环境切换对比

#### Java

```bash
# 启动时指定环境
java -jar app.jar --spring.profiles.active=test
java -jar app.jar --spring.profiles.active=online

# 或配置环境变量
export TRD_TASKENV=test
```

**配置文件**：
- `application.yml` - 默认配置
- `application-test.yml` - 测试环境
- `application-online.yml` - 线上环境

#### Python

```bash
# 通过命令行参数传入环境
python main.py '<params>' '<task_id>' 'test'    # 测试环境
python main.py '<params>' '<task_id>' 'online'  # 线上环境

# 或环境变量
export ENV=test
```

---

## 4. 如何添加新任务类型

假设你要添加一个新任务：**代码审查（CODE_REVIEW）**

### 步骤概览

```
1. Java后端：在KirinConfig添加Tool ID（如果需要新的）
2. Java后端：创建回调接口（LumosController）
3. Java后端：实现回调逻辑（Service）
4. Python端：注册任务（registry/code_review.py）
5. Python端：实现Flow（executor/online/code_review.py）
```

---

### 步骤1: 在KirinConfig添加Tool ID（可选）

**如果**新任务可以复用现有Tool ID（215160 for test），可以跳过此步。

**如果**需要新Tool ID（比如需要不同的Python脚本路径）：

```java
// core/src/main/java/.../KirinConfig.java

// 添加新的Tool ID常量
private static final Long CODE_REVIEW_TOOL_ID_TEST = 215999L;
private static final Long CODE_REVIEW_TOOL_ID_ONLINE = 216000L;

// 在getToolId方法中添加判断
public Long getToolId(KirinTaskEnum taskEnum, KirinCallTypeEnum callTypeEnum) {
    // ...existing code...

    // 新增判断
    if (taskEnum.equals(KirinTaskEnum.CODE_REVIEW)) {
        return taskEnv.equals("online")
            ? CODE_REVIEW_TOOL_ID_ONLINE
            : CODE_REVIEW_TOOL_ID_TEST;
    }

    // ...existing code...
}
```

**同时**需要在枚举中添加：
```java
// core/src/main/java/.../KirinTaskEnum.java
public enum KirinTaskEnum {
    CODE_REVIEW,           // 新增
    STORY_TO_DESIGN,
    TODO_TO_CODE,
    // ...
}
```

---

### 步骤2: 创建回调接口（LumosController）

```java
// core/src/main/java/.../LumosController.java

/**
 * 代码审查任务回调
 */
@PostMapping("/task/codeReview/callback")
public Response<Boolean> codeReviewCallback(
    @RequestBody KirinCommonCallback req) throws Exception {

    // 委托给Service层处理
    return Response.success(
        codeReviewService.codeReviewCallback(req)
    );
}
```

---

### 步骤3: 实现回调逻辑（Service）

**创建Service接口**：
```java
// core/src/main/java/.../service/CodeReviewService.java
public interface CodeReviewService {
    Boolean codeReviewCallback(KirinCommonCallback req);
}
```

**实现Service**：
```java
// core/src/main/java/.../service/impl/CodeReviewServiceImpl.java
@Service
public class CodeReviewServiceImpl implements CodeReviewService {

    @Autowired
    private KirinTaskService kirinTaskService;

    @Override
    public Boolean codeReviewCallback(KirinCommonCallback req) {
        // 1. 解析回调数据
        CodeReviewKirinCallbackResp callbackResp = req.getCallbackResp();
        Long kirinTaskId = callbackResp.getKirinTaskId();
        Integer code = callbackResp.getCode();

        // 2. 查询任务记录
        KirinTaskPo kirinTaskPo = kirinTaskService.queryByTaskId(kirinTaskId);

        if (code == 0) {
            // 3. 成功：保存审查结果
            kirinTaskPo.setTaskStatus(TaskTRDStatusEnum.SUCCESS.getStatus());
            kirinTaskPo.setTaskResult(JSONObject.toJSONString(callbackResp));

            // 保存审查报告到数据库
            CodeReviewReportPo reportPo = new CodeReviewReportPo();
            reportPo.setReportContent(callbackResp.getTaskResult().getReportContent());
            codeReviewReportService.save(reportPo);

        } else {
            // 4. 失败：记录错误
            kirinTaskPo.setTaskStatus(TaskTRDStatusEnum.FAIL.getStatus());
            kirinTaskPo.setErrorMsg(callbackResp.getMsg());
        }

        kirinTaskService.updateById(kirinTaskPo);
        return true;
    }
}
```

---

### 步骤4: Python端注册任务

**创建任务注册文件**：
```python
# /Users/zhuji_m4pro/code/multi-agent/baidu/multi-agent/code/registry/code_review.py

from registry.registry import TaskSpec, register_task
from executor.online.code_review import CodeReviewFlow
from schema.executor.online.code_review import CodeReviewReq, CodeReviewResp

register_task(
    TaskSpec(
        name="CODE_REVIEW",
        flow_class=CodeReviewFlow,
        input_schema=CodeReviewReq,
        output_schema=CodeReviewResp
    )
)
```

**定义Schema**：
```python
# schema/executor/online/code_review.py

from pydantic import BaseModel
from typing import List

class CodeReviewReq(BaseModel):
    taskName: str = "CODE_REVIEW"
    serverUrl: str
    callbackUrl: str
    username: str
    docNodeId: int
    repoUrl: str              # 代码仓库URL
    branch: str = "master"    # 分支
    filePaths: List[str]      # 要审查的文件列表

class CodeReviewResp(BaseModel):
    reportContent: str        # 审查报告内容
```

---

### 步骤5: Python端实现Flow

```python
# executor/online/code_review.py

from executor.base import BaseFlow
from schema.executor.online.code_review import CodeReviewReq, CodeReviewResp
from agent.application.code_reviewer import CodeReviewerAgent
from utils.logger import logger
from utils.error_code import ErrorEnum

class CodeReviewFlow(BaseFlow):
    def __init__(self):
        super().__init__()
        self.code_reviewer = CodeReviewerAgent()

    async def execute(self, req: CodeReviewReq, kirin_task_id: int):
        """
        执行代码审查任务
        """
        # 1. 初始化回调对象
        self._init_qamate(req.serverUrl, req.callbackUrl)

        try:
            # 2. 克隆代码仓库
            repo_path = await self._clone_repo(req.repoUrl, req.branch)

            # 3. 读取要审查的文件
            file_contents = []
            for file_path in req.filePaths:
                with open(f"{repo_path}/{file_path}", "r") as f:
                    file_contents.append({
                        "path": file_path,
                        "content": f.read()
                    })

            # 4. 调用Agent执行审查
            review_report = await self.code_reviewer.run(file_contents)

            # 5. 格式化结果
            task_result = {
                "reportContent": review_report
            }

            # 6. 成功回调
            self.qamate.callback(
                task_name="CODE_REVIEW",
                doc_node_id=req.docNodeId,
                kirin_task_id=kirin_task_id,
                code=0,
                msg="SUCCESS",
                username=req.username,
                task_result=task_result
            )

            return CodeReviewResp(**task_result), ErrorEnum.SUCCESS

        except Exception as e:
            logger.error(f"代码审查失败: {e}")

            # 失败回调
            self.qamate.callback(
                task_name="CODE_REVIEW",
                doc_node_id=req.docNodeId,
                kirin_task_id=kirin_task_id,
                code=1001,
                msg=f"代码审查失败: {str(e)}",
                username=req.username
            )

            return None, ErrorEnum.GEN_CODE_REVIEW_ERROR

    async def _clone_repo(self, repo_url, branch):
        # 克隆代码仓库逻辑
        pass
```

---

### 测试新任务

#### 1. 后端调用

```java
// 在某个Controller中
@PostMapping("/task/codeReview")
public Response<Long> triggerCodeReview(@RequestBody CodeReviewReq req) {
    JSONObject data = new JSONObject();
    data.put("taskName", "CODE_REVIEW");
    data.put("serverUrl", "https://qamate.baidu-int.com");
    data.put("callbackUrl", "/core/lumos/v2/task/codeReview/callback");
    data.put("docNodeId", req.getDocNodeId());
    data.put("repoUrl", req.getRepoUrl());
    data.put("branch", req.getBranch());
    data.put("filePaths", req.getFilePaths());

    Long taskId = kirinService.asycCall(data, KirinTaskEnum.CODE_REVIEW);
    return Response.success(taskId);
}
```

#### 2. 手动测试Python代码

```bash
cd /Users/zhuji_m4pro/code/multi-agent/baidu/multi-agent/code

# 构造测试参数
PARAM='{"taskName":"CODE_REVIEW","serverUrl":"https://qamate.baidu-int.com","callbackUrl":"/core/lumos/v2/task/codeReview/callback","docNodeId":12345,"repoUrl":"https://icode.baidu.com/repo","branch":"master","filePaths":["src/main.py"]}'

# 执行
python main.py "$PARAM" "999999" "test"
```

---

## 5. 常见问题排查

### 5.1 回调失败怎么办

#### 症状
Python代码执行完了，但后端没有收到回调，任务状态一直是`RUNNING`。

#### 排查步骤

**1. 检查Python日志**

```bash
# 查看是否有回调成功日志
grep "回调成功" /path/to/logs/app.log

# 查看是否有回调失败日志
grep "回调失败" /path/to/logs/app.log
```

**2. 检查回调URL是否正确**

```python
# utils/qamate.py中打印实际回调的URL
url = f"{self.url_prefix}{self.callback_url}"
logger.info(f"回调URL: {url}")

# 应该是：https://qamate.baidu-int.com/core/lumos/v2/task/.../callback
```

**3. 检查回调数据格式**

```python
# 打印实际发送的数据
logger.info(f"回调数据: {json.dumps(data)}")

# 确认包含callbackResp字段
# 确认code、msg、kirinTaskId都有值
```

**4. 检查后端是否收到请求**

```bash
# 查看后端日志
tail -f /path/to/qamate-server/logs/application.log | grep "callback"
```

**5. 手动测试回调接口**

```bash
curl -X POST https://qamate.baidu-int.com/core/lumos/v2/task/generate/userStoryDoc2TodoFeatureDoc/callback \
  -H "Content-Type: application/json" \
  -H "QAMate-ModuleId: 0" \
  -H "QAMate-Token: super-9a796933bf024ebfa0420dce6f864a51" \
  -d '{
    "callbackResp": {
      "docNodeId": 12345,
      "kirinTaskId": 123456,
      "username": "test",
      "code": 0,
      "msg": "SUCCESS",
      "taskResult": {}
    }
  }'
```

---

### 5.2 如何查看后端日志

#### 线上环境

```bash
# SSH到服务器
ssh user@qamate-server.baidu-int.com

# 查看日志
cd /home/work/logs/
tail -f application.log

# 搜索特定任务ID的日志
grep "123456" application.log
```

#### 本地开发

```bash
# IDEA控制台直接查看
# 或查看日志文件
tail -f target/logs/application.log
```

#### 关键日志关键字

| 关键字 | 说明 |
|--------|------|
| `【POST】url` | Kirin调用日志（KirinServiceImpl） |
| `【RETURN】result` | Kirin返回结果 |
| `callback` | 回调相关日志 |
| `taskId=123456` | 特定任务的日志 |
| `ERROR` | 错误日志 |

---

### 5.3 如何测试回调接口

#### 方法1: 使用Postman

1. 创建POST请求
2. URL: `https://qamate.baidu-int.com/core/lumos/v2/task/generate/userStoryDoc2TodoFeatureDoc/callback`
3. Headers:
   ```
   Content-Type: application/json
   QAMate-ModuleId: 0
   QAMate-Token: super-9a796933bf024ebfa0420dce6f864a51
   ```
4. Body (raw JSON):
   ```json
   {
     "callbackResp": {
       "docNodeId": 12345,
       "kirinTaskId": 123456,
       "username": "test",
       "code": 0,
       "msg": "SUCCESS",
       "taskResult": {
         "todoFeatureList": []
       }
     }
   }
   ```

#### 方法2: 使用curl

```bash
curl -X POST https://qamate.baidu-int.com/core/lumos/v2/task/generate/userStoryDoc2TodoFeatureDoc/callback \
  -H "Content-Type: application/json" \
  -H "QAMate-ModuleId: 0" \
  -H "QAMate-Token: super-9a796933bf024ebfa0420dce6f864a51" \
  -d @callback_data.json
```

**callback_data.json**:
```json
{
  "callbackResp": {
    "docNodeId": 12345,
    "kirinTaskId": 123456,
    "username": "test",
    "code": 0,
    "msg": "SUCCESS",
    "taskResult": {}
  }
}
```

#### 方法3: Python脚本测试

```python
import requests
import json

url = "https://qamate.baidu-int.com/core/lumos/v2/task/generate/userStoryDoc2TodoFeatureDoc/callback"
headers = {
    "Content-Type": "application/json",
    "QAMate-ModuleId": "0",
    "QAMate-Token": "super-9a796933bf024ebfa0420dce6f864a51"
}

data = {
    "callbackResp": {
        "docNodeId": 12345,
        "kirinTaskId": 123456,
        "username": "test",
        "code": 0,
        "msg": "SUCCESS",
        "taskResult": {}
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(f"状态码: {response.status_code}")
print(f"响应: {response.json()}")
```

---

### 5.4 如何调试Python代码

#### 本地运行Python任务

```bash
cd /Users/zhuji_m4pro/code/multi-agent/baidu/multi-agent/code

# 1. 准备测试参数
PARAM='{
  "taskName": "STORY_TO_DESIGN",
  "serverUrl": "https://qamate.baidu-int.com",
  "callbackUrl": "/core/lumos/v2/task/generate/userStoryDoc2TodoFeatureDoc/callback",
  "docNodeId": 12345,
  "username": "test",
  "userStoryList": [
    {
      "title": "测试用户故事",
      "description": "这是一个测试",
      "acceptanceCriteria": ["可以运行"]
    }
  ]
}'

# 2. 执行（不会真正回调）
python main.py "$PARAM" "999999" "test"

# 3. 如果要测试回调，修改callback_url指向本地Mock服务
```

#### 使用pdb调试

```python
# 在代码中添加断点
import pdb

async def execute(self, req, kirin_task_id):
    pdb.set_trace()  # 断点
    # 执行到这里会暂停，可以交互式调试
```

---

### 5.5 常见错误码含义

| 错误码 | 含义 | 可能原因 |
|-------|------|---------|
| 0 | 成功 | - |
| 1001 | 执行错误 | Python代码抛出异常 |
| 1002 | 生成设计失败 | LLM调用失败、Prompt错误 |
| 1003 | 生成代码失败 | 代码生成Agent失败 |
| 1004 | 构建知识图谱失败 | Neo4j连接失败、数据格式错误 |
| 1005 | 参数解析失败 | JSON格式错误、缺少必填字段 |
| 1006 | 回调失败 | 网络问题、回调URL错误 |
| 1007 | 超时 | 任务执行时间过长 |

---

## 总结

### 你现在应该知道的

✅ Java Spring Boot的基本概念（Controller、Service、@Autowired）

✅ 如何找到对应的Java代码（根据URL/功能搜索）

✅ 后端如何调用你的Python代码（KirinServiceImpl）

✅ 你的Python代码如何回调后端（QAMate.callback）

✅ 如何添加新任务类型（5步法）

✅ 如何排查回调失败问题（查日志、测试接口）

---

### 实用命令速查

```bash
# 搜索Java Controller
find src/ -name "*Controller.java" | xargs grep -l "关键字"

# 查看后端日志
tail -f /path/to/logs/application.log | grep "taskId"

# 测试Python任务
python main.py '<json_params>' '999999' 'test'

# 测试回调接口
curl -X POST <callback_url> -H "..." -d @data.json

# 查看Kirin任务状态
curl http://kirin.baidu-int.com/api/cms/task/query?taskId=123456
```

---

**生成时间**: 2026-04-28
**文档版本**: 1.0
**适用对象**: Python开发者
