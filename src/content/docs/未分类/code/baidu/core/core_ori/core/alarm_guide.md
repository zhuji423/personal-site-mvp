---
title: "ApiSmart 测试计划报警功能 - 新人开发指南"
description: "更新日期：2025-12-05 目标读者：Java后端新人 难度等级：⭐⭐☆☆☆（中等但步骤清晰）"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\core_ori\\core\\alarm_guide.md"
---
# ApiSmart 测试计划报警功能 - 新人开发指南

> 更新日期：2025-12-05
> 目标读者：Java后端新人
> 难度等级：⭐⭐☆☆☆（中等但步骤清晰）


## 一、需求理解（大白话版）

你们有一个自动化测试平台，现在要加一个"考试不及格自动通知家长"的功能：

### 什么时候触发报警？
- **连续失败**：一个测试计划连续几次执行失败（比如连续3次不及格）
- **超时**：测试计划执行时间太长，超过了设定的时间（比如超过300秒）

### 触发后做什么？
1. **记录报警**：把这次报警存到数据库，方便以后查
2. **发通知**：
    - 如流群消息（像微信群通知）
    - 发邮件
    - 单独给某些如流账号发消息
3. **回调业务**：告诉外部系统"出问题了"，让它们也做点什么

---

## 二、技术环境准备

### 2.1 你需要的工具
- ✅ IntelliJ IDEA Ultimate（已安装）
- ✅ 数据库连接（10.138.47.50:8331，已连接成功）
- ✅ MySQL 8.0.32（已连接）

### 2.2 现有代码结构
```
src/main/java/com/baidu/qamate/core/apismartmgt/
├── controller/
│   └── ApiPlanController.java          # 接口入口
├── entity/
│   ├── ApiPlanEntity.java              # 测试计划表实体
│   └── ApiPlanExeEntity.java           # 执行记录表实体
├── mapper/
│   ├── ApiPlanMapper.java
│   └── ApiPlanExeMapper.java
├── service/
│   ├── ApiPlanService.java
│   └── impl/
│       └── ApiPlanServiceImpl.java     # 核心业务逻辑
└── manager/
    └── HTTPRequestManager.java         # HTTP请求工具
```

### 2.3 核心流程图
```
┌─────────────────────────────────────────┐
│  测试计划执行完成                        │
│  (ApiPlanServiceImpl.planExeEnd)       │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│  1. 检查是否满足报警条件                │
│     - 连续失败次数 >= 阈值？            │
│     - 执行时长 >= 超时阈值？            │
└──────────┬──────────────────────────────┘
           │ 不满足
           │
           │ 满足
           ▼
┌─────────────────────────────────────────┐
│  2. 生成报警记录                        │
│     - 写入 apismart_api_plan_alert_history  │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  3. 发送通知（并行）                    │
│     - 如流群消息                        │
│     - 邮件通知                          │
│     - 如流个人消息                      │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  4. 调用业务回调接口                    │
│     - POST /callback                    │
│     - 成功: 标记成功                    │
│     - 失败: 加入重试队列                │
└─────────────────────────────────────────┘
```

---

## 三、数据库设计

### 3.1 SQL 建表语句

```sql
-- 在 IDEA Database Console 中执行

USE core;

CREATE TABLE IF NOT EXISTS apismart_api_plan_alert_history (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
    alert_id VARCHAR(50) NOT NULL COMMENT '报警唯一标识',
    plan_id BIGINT NOT NULL COMMENT '测试计划ID',
    plan_name VARCHAR(200) COMMENT '测试计划名称',
    exe_id VARCHAR(50) COMMENT '执行ID',
    exe_status VARCHAR(20) COMMENT '执行状态',
    fail_count INT DEFAULT 0 COMMENT '连续失败次数',
    trigger_reason VARCHAR(20) COMMENT '触发原因(fail/timeout)',
    alert_channels TEXT COMMENT '触发的报警渠道JSON',
    callback_url TEXT COMMENT '回调接口地址',
    callback_status VARCHAR(20) DEFAULT 'pending' COMMENT '回调状态',
    callback_response TEXT COMMENT '回调响应内容',
    retry_count INT DEFAULT 0 COMMENT '重试次数',
    alert_time BIGINT COMMENT '报警时间戳(毫秒)',
    created_time BIGINT COMMENT '创建时间戳(毫秒)',
    
    INDEX idx_plan_id (plan_id),
    INDEX idx_exe_id (exe_id),
    INDEX idx_alert_time (alert_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='API测试计划报警历史表';
```

### 3.2 验证表创建成功

```sql
-- 1. 查看表是否存在
SHOW TABLES LIKE '%alert%';
-- 应该返回：apismart_api_plan_alert_history

-- 2. 查看表结构
DESC apismart_api_plan_alert_history;
-- 应该看到 id, alert_id, plan_id 等字段

-- 3. 插入一条测试数据
INSERT INTO apismart_api_plan_alert_history (
    alert_id, plan_id, plan_name, exe_id, exe_status, 
    fail_count, trigger_reason, alert_channels, callback_status, 
    retry_count, alert_time, created_time
) VALUES (
    'test_alert_' || UNIX_TIMESTAMP(), 
    1, 
    '测试计划示例', 
    'exe_123456',
    'FAILED',
    3,
    'fail',
    '{"riyuuGroup":true,"email":true}',
    'pending',
    0,
    UNIX_TIMESTAMP() * 1000,
    UNIX_TIMESTAMP() * 1000
);

-- 4. 查询验证
SELECT * FROM apismart_api_plan_alert_history;
-- 应该看到刚才插入的数据
```

### 3.3 你需要确认的数据字典

**非常重要！执行下面的 SQL，把结果发给我！**

```sql
-- 1. 查看执行记录表的所有状态值
SELECT DISTINCT status FROM core_api_plan_exe;
/* 可能的结果：
   SUCCESS
   FAILED
   RUNNING
   TIMEOUT
   我需要知道哪个代表"失败"，哪个代表"运行中"
*/

-- 2. 查看时间戳单位
SELECT start_time, end_time FROM core_api_plan_exe LIMIT 1;
/* 可能的结果：
   1701686400         → 这是秒（10位）
   1701686400123      → 这是毫秒（13位）
   我需要知道单位，代码里要用
*/

-- 3. 查看 plan_params 的内容示例
SELECT plan_params FROM core_api_plan WHERE id = 1;
/* 我需要知道这个JSON的结构，才知道怎么解析
*/
```

---

## 四、Java代码实现（一步一步来）

### 4.1 Step 1: 创建报警历史实体类

**文件位置：** `src/main/java/com/baidu/qamate/core/apismartmgt/entity/`

**文件名：** `AlertHistoryEntity.java`

**操作步骤：**

1. 在 IDEA 左侧 Project 窗口，找到 `apismartmgt/entity` 目录
2. 右键 → New → Java Class
3. 输入文件名：`AlertHistoryEntity`
4. 复制下面的代码，粘贴进去
5. 按 **⌘ + S** (Mac) 或 **Ctrl + S** (Win) 保存

```java
package com.baidu.qamate.core.apismartmgt.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;

/**
 * API测试计划报警历史表
 * 对应数据库表：apismart_api_plan_alert_history
 * 
 * @author 你的名字
 * @date 2025-12-05
 */
@Getter
@Setter
@TableName("apismart_api_plan_alert_history")
public class AlertHistoryEntity implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 主键ID
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    /**
     * 报警唯一标识
     * 格式：alert_ + 时间戳 + 随机数
     * 示例：alert_1701686400123_abc123
     */
    @TableField("alert_id")
    private String alertId;

    /**
     * 测试计划ID
     * 关联 core_api_plan.id
     */
    @TableField("plan_id")
    private Long planId;

    /**
     * 测试计划名称
     * 冗余存储，方便查询
     */
    @TableField("plan_name")
    private String planName;

    /**
     * 执行ID
     * 关联 core_api_plan_exe.id
     */
    @TableField("exe_id")
    private String exeId;

    /**
     * 执行状态
     * 值：SUCCESS / FAILED / TIMEOUT 等
     */
    @TableField("exe_status")
    private String exeStatus;

    /**
     * 连续失败次数
     * 达到阈值才会触发报警
     */
    @TableField("fail_count")
    private Integer failCount;

    /**
     * 触发原因
     * fail: 连续失败触发
     * timeout: 执行超时触发
     */
    @TableField("trigger_reason")
    private String triggerReason;

    /**
     * 触发的报警渠道JSON
     * 格式：{"riyuuGroup":{"enabled":true,"groupId":"123"},"email":{"enabled":true,"recipients":["a@baidu.com"]}}
     */
    @TableField("alert_channels")
    private String alertChannels;

    /**
     * 回调接口地址
     * 如果配置了，就会调用这个URL
     */
    @TableField("callback_url")
    private String callbackUrl;

    /**
     * 是否是Kirin接口
     * true: 按Kirin规范封装请求
     * false: 普通JSON格式
     */
    @TableField("is_kirin")
    private Boolean isKirin;

    /**
     * 回调状态
     * pending: 待回调
     * success: 回调成功
     * failed: 回调失败
     */
    @TableField("callback_status")
    private String callbackStatus;

    /**
     * 回调响应内容
     * 存储回调接口返回的内容
     */
    @TableField("callback_response")
    private String callbackResponse;

    /**
     * 重试次数
     * 回调失败时会重试，最多3次
     */
    @TableField("retry_count")
    private Integer retryCount;

    /**
     * 报警时间戳（毫秒）
     * 13位数字，如：1701686400123
     */
    @TableField("alert_time")
    private Long alertTime;

    /**
     * 创建时间戳（毫秒）
     * 13位数字，如：1701686400123
     */
    @TableField("created_time")
    private Long createdTime;
}
```

**验证：**
- 代码没有红色报错
- 所有 import 语句都能自动导入（如有红字，按 ⌥+Enter 自动导入）

---

### 4.2 Step 2: 创建 Mapper 接口

**文件位置：** `src/main/java/com/baidu/qamate/core/apismartmgt/mapper/`

**文件名：** `AlertHistoryMapper.java`

**操作步骤：**

1. 右键 `mapper` 目录 → New → Java Class
2. 输入文件名：`AlertHistoryMapper`
3. 复制下面的代码
4. 保存

```java
package com.baidu.qamate.core.apismartmgt.mapper;

import com.baidu.qamate.core.apismartmgt.entity.AlertHistoryEntity;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;

/**
 * 报警历史 Mapper 接口
 * 
 * 继承 BaseMapper 后，自动拥有以下方法：
 * - insert(entity)          # 插入
 * - selectById(id)          # 按ID查询
 * - updateById(entity)      # 按ID更新
 * - deleteById(id)          # 按ID删除
 * - selectList(wrapper)     # 条件查询列表
 * 
 * 不需要手写 SQL！
 */
@Mapper
public interface AlertHistoryMapper extends BaseMapper<AlertHistoryEntity> {
    // 如果有特殊的查询需求，可以在下面添加方法
    // 方法名要符合 MyBatis Plus 的约定
    
    /**
     * 根据执行ID查询报警历史
     */
    // List<AlertHistoryEntity> selectByExeId(String exeId);
    // 这个方法只需要在这里声明，MyBatis Plus 会自动生成实现
}
```

---

### 4.3 Step 3: 创建 Service 接口和实现类

**3.1 创建 Service 接口**

**文件位置：** `src/main/java/com/baidu/qamate/core/apismartmgt/service/`

**文件名：** `AlertHistoryService.java`

```java
package com.baidu.qamate.core.apismartmgt.service;

import com.baidu.qamate.core.apismartmgt.entity.AlertHistoryEntity;

/**
 * 报警历史 Service 接口
 * 定义报警历史的业务操作
 */
public interface AlertHistoryService {

    /**
     * 记录报警历史
     * 
     * @param history 报警历史实体
     * @return 是否成功
     */
    boolean recordAlertHistory(AlertHistoryEntity history);
    
    /**
     * 更新回调状态
     * 
     * @param alertId 报警ID
     * @param status 回调状态 (success/failed/pending)
     * @param response 回调响应
     * @param retryCount 重试次数
     * @return 是否成功
     */
    boolean updateCallbackStatus(String alertId, String status, String response, Integer retryCount);
    
    /**
     * 根据执行ID查询报警历史
     * 
     * @param exeId 执行ID
     * @return 报警历史列表
     */
    // List<AlertHistoryEntity> getAlertHistoryByExeId(String exeId);
}
```

**3.2 创建 Service 实现类**

**文件位置：** `src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/`

**文件名：** `AlertHistoryServiceImpl.java`

```java
package com.baidu.qamate.core.apismartmgt.service.impl;

import com.baidu.qamate.core.apismartmgt.entity.AlertHistoryEntity;
import com.baidu.qamate.core.apismartmgt.mapper.AlertHistoryMapper;
import com.baomidou.mybatisplus.core.conditions.update.LambdaUpdateWrapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * 报警历史 Service 实现类
 * 实现具体的业务逻辑
 */
@Slf4j
@Service
public class AlertHistoryServiceImpl implements AlertHistoryService {

    @Autowired
    private AlertHistoryMapper alertHistoryMapper;

    /**
     * 记录报警历史
     */
    @Override
    public boolean recordAlertHistory(AlertHistoryEntity history) {
        try {
            // 生成alertId
            history.setAlertId(generateAlertId());

            // 设置时间戳
            long currentTime = System.currentTimeMillis();
            history.setAlertTime(currentTime);
            history.setCreatedTime(currentTime);

            // 设置默认值
            if (history.getCallbackStatus() == null) {
                history.setCallbackStatus("pending");
            }
            if (history.getRetryCount() == null) {
                history.setRetryCount(0);
            }

            // 插入数据库
            int rows = alertHistoryMapper.insert(history);

            if (rows > 0) {
                log.info("报警历史记录成功, alertId: {}, planId: {}",
                        history.getAlertId(), history.getPlanId());
                return true;
            } else {
                log.error("报警历史记录失败, alertId: {}", history.getAlertId());
                return false;
            }
        } catch (Exception e) {
            log.error("报警历史记录异常, alertId: {}",
                    history.getAlertId(), e);
            return false;
        }
    }

    /**
     * 更新回调状态
     */
    @Override
    public boolean updateCallbackStatus(String alertId, String status,
                                        String response, Integer retryCount) {
        try {
            LambdaUpdateWrapper<AlertHistoryEntity> wrapper =
                    new LambdaUpdateWrapper<>();
            wrapper.eq(AlertHistoryEntity::getAlertId, alertId)
                    .set(AlertHistoryEntity::getCallbackStatus, status)
                    .set(AlertHistoryEntity::getCallbackResponse, response)
                    .set(AlertHistoryEntity::getRetryCount, retryCount);

            int rows = alertHistoryMapper.update(null, wrapper);

            if (rows > 0) {
                log.info("回调状态更新成功, alertId: {}, status: {}",
                        alertId, status);
                return true;
            } else {
                log.error("回调状态更新失败, alertId: {}", alertId);
                return false;
            }
        } catch (Exception e) {
            log.error("回调状态更新异常, alertId: {}", alertId, e);
            return false;
        }
    }

    /**
     * 生成报警唯一标识
     */
    private String generateAlertId() {
        return String.format("alert_%d_%s",
                System.currentTimeMillis(),
                java.util.UUID.randomUUID().toString().substring(0, 8)
        );
    }
}
```

---

### 4.4 Step 4: 在计划执行结束时调用报警（核心！）

**修改文件：** `src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ApiPlanServiceImpl.java`

**完整代码：**

```java
@Override
public void planExeEnd(DispatchExeRequestVo dispatchExeRequestVo) {
    // ===== 原有的逻辑（保留） =====
    log.info("planExeEnd: {}", dispatchExeRequestVo);

    var plan = apiPlanMapper.selectById(dispatchExeRequestVo.getPlanId());
    if (plan == null || plan.getIsDel()) {
        throw new CoreException(StatusEnum.PLAN_NOT_EXIST);
    }

    if (StringUtils.isNotEmpty(dispatchExeRequestVo.getExeId())) {
        var planExe = apiPlanExeMapper.selectById(dispatchExeRequestVo.getExeId());
        if (planExe == null) {
            throw new CoreException(StatusEnum.EXECUTION_NOT_EXIST);
        }

        if (!PlanExeStatus.RUNNING.name().equals(planExe.getStatus())) {
            throw new CoreException(StatusEnum.EXECUTION_STATUS_ERROR);
        }

        LambdaUpdateWrapper<ApiPlanExeEntity> updateWrapper = new LambdaUpdateWrapper<>();
        updateWrapper.eq(ApiPlanExeEntity::getId, dispatchExeRequestVo.getExeId())
                .set(ApiPlanExeEntity::getEndTime, System.currentTimeMillis())
                .set(ApiPlanExeEntity::getStatus, dispatchExeRequestVo.getStatus())
                .set(ApiPlanExeEntity::getExecResult, dispatchExeRequestVo.getExecResult());
        apiPlanExeMapper.update(null, updateWrapper);
    }

    // ... 可能还有其他逻辑 ...
    
    // ===== 新增的报警检查（添加到这里） =====
    try {
        log.info("执行完成，开始报警检查, planId: {}, exeId: {}", 
            dispatchExeRequestVo.getPlanId(), 
            dispatchExeRequestVo.getExeId());
        
        alertCheckService.checkAndTriggerAlert(
            dispatchExeRequestVo.getPlanId(),
            dispatchExeRequestVo.getExeId()
        );
        
        log.info("报警检查完成");
        
    } catch (Exception e) {
        log.error("报警检查异常, planId: {}, exeId: {}", 
            dispatchExeRequestVo.getPlanId(), 
            dispatchExeRequestVo.getExeId(), e);
        // 报警失败不影响主流程，不要 throw
    }
}
```

**需要在类开头注入：**

```java
@Autowired
private AlertCheckService alertCheckService;
```

---


---

## 后续测试计划

### 一、测试方案总览（从简到繁）

我将为你设计三个层级的测试：

1. **Level 1: 数据层测试** - 验证报警记录能存进数据库
2. **Level 2: 代码层测试** - 验证业务逻辑正确
3. **Level 3: 全流程测试** - 验证完整报警流程

---

### 二、Level 1: 数据层测试（30分钟）

#### 2.1 验证数据库表结构

```sql
-- 测试 1: 表是否存在
SHOW TABLES LIKE '%alert%';
-- 预期结果: apismart_api_plan_alert_history

-- 测试 2: 表结构是否正确
DESC apismart_api_plan_alert_history;
-- 预期结果: 能看到 id, alert_id, plan_id 等所有字段
```

#### 2.2 验证数据插入

```sql
-- 测试 3: 插入一条测试数据
INSERT INTO apismart_api_plan_alert_history (
    alert_id, plan_id, plan_name, exe_id, exe_status, 
    fail_count, trigger_reason, alert_channels, 
    callback_url, callback_status, retry_count, 
    alert_time, created_time
) VALUES (
    'test_alert_' || REPLACE(UUID(), '-', ''),  -- 生成唯一ID
    1,                                          -- plan_id (改为你的测试计划ID)
    '测试计划名称',                              
    'exe_test_001',
    'FAILED',
    3,
    'fail',
    '{"riyuuGroup":{"enabled":true,"groupId":"12345"},"email":{"enabled":true,"recipients":["test@baidu.com"]}}',
    'https://your-service.com/callback',
    'pending',
    0,
    UNIX_TIMESTAMP() * 1000,
    UNIX_TIMESTAMP() * 1000
);

-- 测试 4: 查询验证
SELECT * FROM apismart_api_plan_alert_history 
WHERE plan_id = 1 
ORDER BY created_time DESC 
LIMIT 1;
-- 预期结果: 看到刚才插入的数据，所有字段都有值

-- 测试 5: 查询性能测试
SELECT * FROM apismart_api_plan_alert_history 
WHERE plan_id = 1 
ORDER BY alert_time DESC 
LIMIT 100;
-- 预期结果: 查询速度快，不卡顿（< 100ms）
```

---

### 三、Level 2: 代码层测试（1小时）

#### 3.1 测试 Mapper 接口

```java
// 在 test 目录下创建测试类
// src/test/java/com/baidu/qamate/core/apismartmgt/mapper/AlertHistoryMapperTest.java

@SpringBootTest
public class AlertHistoryMapperTest {
    @Autowired
    private AlertHistoryMapper alertHistoryMapper;

    @Test
    public void testInsert() {
        AlertHistoryEntity history = new AlertHistoryEntity();
        history.setPlanId(1L);
        history.setPlanName("测试计划");
        history.setExeId("exe_test_001");
        history.setExeStatus("FAILED");
        history.setFailCount(3);
        history.setTriggerReason("fail");
        history.setAlertChannels("{\"riyuuGroup\":true}");
        history.setCallbackStatus("pending");
        
        int rows = alertHistoryMapper.insert(history);
        assertTrue(rows > 0);
        assertNotNull(history.getId()); // 插入后ID应该被回填
    }

    @Test
    public void testSelectById() {
        // 先插入
        AlertHistoryEntity history = new AlertHistoryEntity();
        history.setPlanId(1L);
        history.setAlertId("alert_test_001");
        alertHistoryMapper.insert(history);
        
        // 再查询
        AlertHistoryEntity result = alertHistoryMapper.selectById(history.getId());
        assertNotNull(result);
        assertEquals(1L, result.getPlanId());
        assertEquals("alert_test_001", result.getAlertId());
    }
}
```

#### 3.2 测试 Service 接口

```java
// src/test/java/com/baidu/qamate/core/apismartmgt/service/AlertHistoryServiceTest.java

@SpringBootTest
public class AlertHistoryServiceTest {
    @Autowired
    private AlertHistoryService alertHistoryService;

    @Test
    public void testRecordAlertHistory() {
        AlertHistoryEntity history = new AlertHistoryEntity();
        history.setPlanId(1L);
        history.setPlanName("测试计划");
        history.setExeId("exe_test_001");
        history.setExeStatus("FAILED");
        history.setFailCount(3);
        history.setTriggerReason("fail");
        history.setAlertChannels("{\"riyuuGroup\":true}");
        history.setCallbackUrl("https://test.com/callback");
        history.setIsKirin(false);

        boolean result = alertHistoryService.recordAlertHistory(history);
        assertTrue(result);
        assertNotNull(history.getAlertId());
    }
}
```

#### 3.3 测试配置解析

```java
// src/test/java/com/baidu/qamate/core/apismartmgt/utils/AlertConfigUtilsTest.java

public class AlertConfigUtilsTest {
    @Test
    public void testParseAlertConfig() {
        String planParams = "{\n" +
            "  \"alertConfig\": {\n" +
            "    \"enabled\": true,\n" +
            "    \"failThreshold\": 3,\n" +
            "    \"timeoutThreshold\": 300,\n" +
            "    \"callbackUrl\": \"https://test.com\"\n" +
            "  }\n" +
            "}";

        AlertConfig config = AlertConfigUtils.parseAlertConfig(planParams);
        
        assertNotNull(config);
        assertTrue(config.getEnabled());
        assertEquals(3, config.getFailThreshold());
        assertEquals(300, config.getTimeoutThreshold());
        assertEquals("https://test.com", config.getCallbackUrl());
    }

    @Test
    public void testParseAlertConfig_Null() {
        // 测试空值
        AlertConfig config = AlertConfigUtils.parseAlertConfig(null);
        assertNull(config);
        
        // 测试无alertConfig
        config = AlertConfigUtils.parseAlertConfig("{\"other\":123}");
        assertNull(config);
    }
}
```

---

### 四、Level 3: 全流程测试（2小时）

#### 4.1 前置准备

##### 4.1.1 准备一个测试计划

```sql
-- 找一个现有的测试计划，或者创建测试数据
SELECT id, plan_name, plan_params FROM core_api_plan WHERE id = 1;

-- 如果这个计划没有报警配置，手动更新它的 plan_params
UPDATE core_api_plan 
SET plan_params = '{
  "originalConfig": {...},
  "alertConfig": {
    "enabled": true,
    "failThreshold": 1,
    "timeoutThreshold": 300,
    "channels": {
      "riyuuGroup": {"enabled": true, "groupId": "12345"},
      "email": {"enabled": false, "recipients": []}
    },
    "callbackUrl": "",
    "isKirin": false
  }
}'
WHERE id = 1;
```

##### 4.1.2 查看执行记录

```sql
-- 查看这个计划的执行情况
SELECT id, plan_id, status, start_time, end_time 
FROM core_api_plan_exe 
WHERE plan_id = 1 
ORDER BY start_time DESC 
LIMIT 5;
```

---

#### 4.2 场景驱动测试

##### 场景 1：连续失败触发报警

**测试步骤：**

1. **清空历史数据**（测试前清理）
```sql
DELETE FROM apismart_api_plan_alert_history 
WHERE plan_id = 1;
```

2. **执行一次失败的测试**
```java
// 在页面上执行测试计划，让用例失败
// 或者调用接口：POST /apismart/plan/run
```

3. **查看日志**
```
日志中应该看到：
"【报警】执行完成，开始报警检查, planId: 1, exeId: exe_xxx"
"【报警】检查是否满足报警条件"
"【报警】满足报警条件，开始触发报警"
"【报警】报警记录成功, alertId: alert_xxxxx"
```

4. **验证数据库**
```sql
-- 报警记录应该多了1条
SELECT COUNT(*) as count FROM apismart_api_plan_alert_history WHERE plan_id = 1;
-- 结果: 1

-- 查看详情
SELECT * FROM apismart_api_plan_alert_history 
WHERE plan_id = 1 
ORDER BY created_time DESC 
LIMIT 1;
-- 应该看到: trigger_reason='fail', fail_count=1
```

##### 场景 2：不触发报警（报警禁用）

**测试步骤：**
1. 将报警配置改为 `"enabled": false`
2. 执行失败的测试
3. 验证：数据库中不应该有新记录

```sql
-- 验证
SELECT COUNT(*) FROM apismart_api_plan_alert_history WHERE plan_id = 1;
-- 结果应该和上一步相同，没有新增
```
4. 查看日志，应该能看到： `"【报警】报警已禁用"`

##### 场景 3：不触发报警（未达到阈值）

**测试步骤：**
1. 设置 `failThreshold: 3`
2. 只执行1次失败的测试
3. 验证：不触发报警

##### 场景 4：超时触发报警

**测试步骤：**
1. 设置 `timeoutThreshold: 1`（1秒）
2. 执行一个耗时超过1秒的测试
3. 验证：触发报警，trigger_reason='timeout'

---

#### 4.3 自动化测试脚本

```groovy
// 在 src/test/groovy 下创建自动化测试脚本
// AlertCheckIntegrationTest.groovy

@SpringBootTest
class AlertCheckIntegrationTest extends Specification {

    @Autowired
    private AlertCheckService alertCheckService
    
    @Autowired
    private AlertHistoryMapper alertHistoryMapper
    
    @Autowired
    private ApiPlanMapper apiPlanMapper

    def "连续失败后触发报警"() {
        given: "一个配置了报警的测试计划"
        Long planId = 1L
        String exeId = "exe_integration_test_" + System.currentTimeMillis()
        
        when: "执行完成并调用报警检查"
        alertCheckService.checkAndTriggerAlert(planId, exeId)
        
        then: "数据库中应该有一条报警记录"
        def histories = alertHistoryMapper.selectList(
            new LambdaQueryWrapper<AlertHistoryEntity>()
                .eq(AlertHistoryEntity::getPlanId, planId)
                .orderByDesc(AlertHistoryEntity::getCreatedTime)
        )
        histories.size() > 0
        
        and: "报警记录的字段都正确"
        def latest = histories[0]
        latest.alertId.startsWith("alert_")
        latest.exeId == exeId
        latest.triggerReason == "fail" || latest.triggerReason == "timeout"
    }

    def "报警禁用时不触发"() {
        given: "一个禁用报警的测试计划"
        Long planId = 2L  // 假设这个计划的alertConfig.enabled=false
        
        when: "执行完成"
        alertCheckService.checkAndTriggerAlert(planId, "exe_test_002")
        
        then: "不应该有报警记录"
        def count = alertHistoryMapper.selectCount(
            new LambdaQueryWrapper<AlertHistoryEntity>()
                .eq(AlertHistoryEntity::getPlanId, planId)
        )
        count == 0
    }
}
```

---

### 五、测试用例清单（测试矩阵）

| 编号 | 场景描述 | 触发条件 | 预期结果 | 优先级 | 状态 |
|------|----------|----------|----------|--------|------|
| TC01 | 连续失败达到阈值 | failThreshold=3, 第3次失败 | 触发报警 | P0 | ☐ |
| TC02 | 连续失败未达阈值 | failThreshold=3, 第2次失败 | 不触发 | P0 | ☐ |
| TC03 | 执行超时 | timeoutThreshold=1秒 | 触发报警 | P0 | ☐ |
| TC04 | 执行正常 | 成功，不超时 | 不触发 | P0 | ☐ |
| TC05 | 报警禁用 | alertConfig.enabled=false | 不触发 | P0 | ☐ |
| TC06 | 无报警配置 | plan_params无alertConfig | 不触发 | P0 | ☐ |
| TC07 | 回调失败 | 回调URL返回500 | 状态failed，重试+1 | P1 | ☐ |
| TC08 | 回调成功 | 回调URL返回200 | 状态success | P1 | ☐ |
| TC09 | 多渠通知测试 | riyuuGroup+email启用 | 都收到通知 | P2 | ☐ |
| TC10 | 数据库异常 | 插入失败 | 日志记录，不阻塞主流程 | P1 | ☐ |

---

### 六、验证清单（自测检查表）

#### 数据库层 [ ]
- [ ] 表创建成功
- [ ] 能插入数据
- [ ] 能查询数据
- [ ] 索引生效

#### 代码层 [ ]
- [ ] Mapper注入成功
- [ ] Service注入成功
- [ ] 配置解析正确
- [ ] 报警触发逻辑正确
- [ ] 异常不影响主流程

#### 业务层 [ ]
- [ ] 连续失败触发报警
- [ ] 超时触发报警
- [ ] 不触发条件验证
- [ ] 报警记录入库
- [ ] 日志信息完整

---

### 七、测试报告模板

```markdown
# 报警功能测试报告

## 测试时间
2025-12-05 10:00-12:00

## 测试环境
- 数据库：10.138.47.50:8331
- 代码分支：dev_alert_feature
- 测试计划ID：1

## 测试场景
1. TC01-连续失败触发
   - 结果：✓ 通过
   - 数据：生成alertId=alert_1701686400_abc123
   - 日志：完整

2. TC02-不触发报警
   - 结果：✓ 通过
   - 数据：无新增记录
   - 日志：显示"警告已禁用"

## 问题汇总
- 无

## 结论
功能正常，可以上线
```

---

### 八、如果测试失败了怎么办？

#### 现象1：没有报警记录

**排查步骤：**

1. **检查 planExeEnd 是否被调用**
   ```
   日志中应该能看到：
   "planExeEnd: DispatchExeRequestVo(...)"
   
   如果没有，说明执行流程有问题
   ```

2. **检查报警检查是否执行**
   ```
   日志中应该能看到：
   "执行完成，开始报警检查, planId: ..., exeId: ..."
   
   如果没有，说明代码没走到
   ```

3. **检查是否满足触发条件**
   ```
   日志中应该能看到：
   "不满足报警条件" 或 "满足报警条件，开始触发报警"
   
   如果不满足，检查配置和状态
   ```

4. **检查数据库是否有异常**
   ```
   日志中应该能看到：
   "报警历史记录成功" 或 "报警历史记录失败"
   
   如果失败，查看异常堆栈
   ```

#### 现象2：报警记录字段为空

**排查步骤：**

1. 检查 `AlertHistoryEntity` 对象是否 set 了值
2. 检查 `@TableField` 注解的字段名是否正确
3. 检查数据库表字段名是否正确

#### 现象3：重复触发报警

**排查步骤：**

1. 检查是否每次执行都触发
2. 检查触发条件逻辑（应该是：失败次数 >= 阈值）
3. 检查 `getContinuousFailCount` 实现是否正确

#### 现象4：回调没有执行

**排查步骤：**

1. 检查 `callbackUrl` 是否为空
2. 检查回调服务的代码是否完成（可能是TODO）
3. 查看回调相关的日志

---

### 九、测试小技巧

#### 1. 快速清空测试数据

```sql
-- 清空所有测试数据（小心！）
TRUNCATE TABLE apismart_api_plan_alert_history;
```

#### 2. 快速插入大量测试数据

```sql
-- 插入100条测试数据
INSERT INTO apismart_api_plan_alert_history (/* fields */)
SELECT /* values */
FROM information_schema.tables 
LIMIT 100;
```

#### 3. 快速查看最近的记录

```sql
-- 只看最近10条
SELECT * FROM apismart_api_plan_alert_history 
ORDER BY created_time DESC 
LIMIT 10;

-- 只看特定计划的最近报警
SELECT * FROM apismart_api_plan_alert_history 
WHERE plan_id = 1
ORDER BY alert_time DESC 
LIMIT 5;
```

#### 4. 统计触发频率

```sql
-- 每小时触发多少次
SELECT 
    DATE_FORMAT(FROM_UNIXTIME(alert_time / 1000), '%Y-%m-%d %H') as hour,
    COUNT(*) as count
FROM apismart_api_plan_alert_history
WHERE alert_time > UNIX_TIMESTAMP() - 86400000 -- 最近24小时
GROUP BY hour
ORDER BY hour DESC;
```

---

### 十、终极目标

#### 完全自测通过的标准：

1. **数据库验证通过** ✓
    - 表结构正确
    - 数据插入/查询正常

2.  **代码逻辑验证通过**  ✓
- 配置解析正确
- 触发逻辑正确
- 异常处理正确

3.  **业务场景验证通过**  ✓
- 连续失败触发报警
- 超时触发报警
- 配置禁用不触发
- 记录入库成功

4. **日志验证通过** ✓
    - 关键步骤都有日志
    - 错误日志包含详细信息
    - 日志级别合理

5.  **性能验证通过**  ✓
- 数据库查询 < 100ms
- 主流程不受影响
- 无死循环、无阻塞

---

### 十一、快速开始你的第一次测试

#### 现在做：

1. **打开 IDEA Database Console**
2. **执行**：
   ```sql
   CREATE TABLE IF NOT EXISTS apismart_api_plan_alert_history ( ... );
   SHOW TABLES LIKE '%alert%';
   ```
3. **验证表创建成功**
4. **执行**：
   ```sql
   INSERT INTO apismart_api_plan_alert_history VALUES ( ... );
   SELECT * FROM apismart_api_plan_alert_history;
   ```
5. **验证数据插入成功**

✅ 如果都成功了，说明数据库层面没问题！

接下来开始创建 Java 类...

---

有问题随时告诉我哪个环节失败了，我会帮你一步步排查！

