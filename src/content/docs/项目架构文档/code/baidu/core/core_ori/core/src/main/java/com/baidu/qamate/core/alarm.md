---
title: "ApiSmart 测试计划报警功能实施计划"
description: "为提升自动化测试的监控效率，需在测试计划执行过程中实现智能化报警机制，当用例执行失败或超时时，通过多渠道通知相关人员，并支持业务系统回调接口实现快速定位。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\core_ori\\core\\src\\main\\java\\com\\baidu\\qamate\\core\\alarm.md"
---
# ApiSmart 测试计划报警功能实施计划

## 背景与目标

为提升自动化测试的监控效率，需在测试计划执行过程中实现智能化报警机制，当用例执行失败或超时时，通过多渠道通知相关人员，并支持业务系统回调接口实现快速定位。

## 现有系统分析

基于对ApiSmart代码结构的分析，现有系统包含：

### 核心实体
- **TestPlan.java** - 测试计划实体
- **TestExecution.java** - 测试执行记录
- **TestCase.java** - 测试用例实体

### 现有架构
- **Controller层**：TestPlanController、TestCaseController
- **Service层**：TestCaseExecutionService等
- **Repository层**：TestPlanRepository等
- **Entity层**：标准的JPA实体类

## 详细实施计划

### 第一阶段：数据库设计和基础实体（预计1周）

#### 1.1 创建枚举类

**文件路径**: `apismartmgt/enums/NotificationChannel.java`
```java
package com.baidu.qamate.core.apismartmgt.enums;

public enum NotificationChannel {
    RULIU_GROUP_MESSAGE("如流群消息"),
    EMAIL("邮件通知"),
    RULIU_PERSONAL_MESSAGE("如流个人消息");

    private final String description;

    NotificationChannel(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }
}
```

**文件路径**: `apismartmgt/enums/AlarmStatus.java`
```java
package com.baidu.qamate.core.apismartmgt.enums;

public enum AlarmStatus {
    PENDING("待处理"),
    SENT("已发送"),
    FAILED("发送失败"),
    RETRY("重试中");

    private final String description;

    AlarmStatus(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }
}
```

#### 1.2 创建报警配置实体类

**文件路径**: `apismartmgt/entity/AlarmConfig.java`
```java
package com.baidu.qamate.core.apismartmgt.entity;

import com.baidu.qamate.core.apismartmgt.enums.NotificationChannel;
import lombok.Data;
import javax.persistence.*;
import java.util.List;

@Entity
@Table(name = "alarm_config")
@Data
public class AlarmConfig {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "test_plan_id")
    private Long testPlanId;

    @Column(name = "continuous_fail_count")
    private Integer continuousFailCount = 3; // 默认3次

    @Column(name = "timeout_threshold")
    private Integer timeoutThreshold = 300; // 默认300秒

    @ElementCollection
    @CollectionTable(name = "alarm_notification_channels",
                    joinColumns = @JoinColumn(name = "alarm_config_id"))
    @Column(name = "channel_type")
    private List<NotificationChannel> notificationChannels;

    @ElementCollection
    @CollectionTable(name = "alarm_channel_configs",
                    joinColumns = @JoinColumn(name = "alarm_config_id"))
    @MapKeyColumn(name = "config_key")
    @Column(name = "config_value")
    private Map<String, String> channelConfigs;

    @Column(name = "callback_url")
    private String callbackUrl;

    @Column(name = "is_kirin_callback")
    private Boolean isKirinCallback = false;

    @Column(name = "enabled")
    private Boolean enabled = true;

    @CreationTimestamp
    @Column(name = "created_time")
    private LocalDateTime createdTime;

    @UpdateTimestamp
    @Column(name = "updated_time")
    private LocalDateTime updatedTime;
}
```

#### 1.3 创建报警记录实体类

**文件路径**: `apismartmgt/entity/AlarmRecord.java`
```java
package com.baidu.qamate.core.apismartmgt.entity;

import com.baidu.qamate.core.apismartmgt.enums.AlarmStatus;
import lombok.Data;
import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "alarm_record")
@Data
public class AlarmRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "alert_id", unique = true)
    private String alertId;

    @Column(name = "test_plan_id")
    private Long testPlanId;

    @Column(name = "test_plan_name")
    private String testPlanName;

    @Column(name = "execution_id")
    private String executionId;

    @Column(name = "fail_count")
    private Integer failCount;

    @Column(name = "alarm_status")
    @Enumerated(EnumType.STRING)
    private AlarmStatus alarmStatus;

    @Column(name = "detail_url")
    private String detailUrl;

    @Column(name = "callback_url")
    private String callbackUrl;

    @Column(name = "retry_count")
    private Integer retryCount = 0;

    @Column(name = "error_message")
    private String errorMessage;

    @CreationTimestamp
    @Column(name = "created_time")
    private LocalDateTime createdTime;

    @UpdateTimestamp
    @Column(name = "updated_time")
    private LocalDateTime updatedTime;
}
```

### 第二阶段：数据访问层开发（预计3天）

#### 2.1 创建Repository接口

**文件路径**: `apismartmgt/repository/AlarmConfigRepository.java`
```java
package com.baidu.qamate.core.apismartmgt.repository;

import com.baidu.qamate.core.apismartmgt.entity.AlarmConfig;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface AlarmConfigRepository extends JpaRepository<AlarmConfig, Long> {

    Optional<AlarmConfig> findByTestPlanId(Long testPlanId);

    void deleteByTestPlanId(Long testPlanId);
}
```

**文件路径**: `apismartmgt/repository/AlarmRecordRepository.java`
```java
package com.baidu.qamate.core.apismartmgt.repository;

import com.baidu.qamate.core.apismartmgt.entity.AlarmRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
public interface AlarmRecordRepository extends JpaRepository<AlarmRecord, Long> {

    List<AlarmRecord> findByTestPlanIdOrderByCreatedTimeDesc(Long testPlanId);

    List<AlarmRecord> findByCreatedTimeBetween(LocalDateTime startTime, LocalDateTime endTime);

    List<AlarmRecord> findByAlarmStatus(AlarmStatus alarmStatus);
}
```

### 第三阶段：业务逻辑层开发（预计1周）

#### 3.1 报警配置服务

**文件路径**: `apismartmgt/service/AlarmConfigService.java`
```java
package com.baidu.qamate.core.apismartmgt.service;

import com.baidu.qamate.core.apismartmgt.entity.AlarmConfig;
import com.baidu.qamate.core.apismartmgt.repository.AlarmConfigRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.Optional;

@Slf4j
@Service
@RequiredArgsConstructor
public class AlarmConfigService {

    private final AlarmConfigRepository alarmConfigRepository;

    public AlarmConfig saveAlarmConfig(AlarmConfig alarmConfig) {
        log.info("保存报警配置，测试计划ID: {}", alarmConfig.getTestPlanId());
        return alarmConfigRepository.save(alarmConfig);
    }

    public Optional<AlarmConfig> getAlarmConfigByTestPlanId(Long testPlanId) {
        return alarmConfigRepository.findByTestPlanId(testPlanId);
    }

    public void deleteAlarmConfig(Long testPlanId) {
        alarmConfigRepository.deleteByTestPlanId(testPlanId);
        log.info("删除报警配置，测试计划ID: {}", testPlanId);
    }

    public AlarmConfig updateChannelConfig(Long testPlanId, Map<String, String> channelConfigs) {
        Optional<AlarmConfig> configOpt = alarmConfigRepository.findByTestPlanId(testPlanId);
        if (configOpt.isPresent()) {
            AlarmConfig config = configOpt.get();
            config.setChannelConfigs(channelConfigs);
            return alarmConfigRepository.save(config);
        }
        throw new RuntimeException("未找到测试计划的报警配置");
    }
}
```

#### 3.2 通知服务

**文件路径**: `apismartmgt/service/NotificationService.java`
```java
package com.baidu.qamate.core.apismartmgt.service;

import com.baidu.qamate.core.apismartmgt.entity.AlarmConfig;
import com.baidu.qamate.core.apismartmgt.entity.AlarmRecord;
import com.baidu.qamate.core.apismartmgt.enums.NotificationChannel;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.Map;

@Slf4j
@Service
@RequiredArgsConstructor
public class NotificationService {

    private final RuLiuNotificationService ruLiuNotificationService;
    private final EmailNotificationService emailNotificationService;

    public void sendNotifications(AlarmRecord alarmRecord, AlarmConfig alarmConfig) {
        if (!alarmConfig.getEnabled() || alarmConfig.getNotificationChannels() == null) {
            log.info("报警配置未启用或未配置通知渠道");
            return;
        }

        Map<String, String> channelConfigs = alarmConfig.getChannelConfigs();

        for (NotificationChannel channel : alarmConfig.getNotificationChannels()) {
            try {
                switch (channel) {
                    case RULIU_GROUP_MESSAGE:
                        sendRuLiuGroupMessage(alarmRecord, channelConfigs);
                        break;
                    case EMAIL:
                        sendEmail(alarmRecord, channelConfigs);
                        break;
                    case RULIU_PERSONAL_MESSAGE:
                        sendRuLiuPersonalMessage(alarmRecord, channelConfigs);
                        break;
                    default:
                        log.warn("不支持的通知渠道: {}", channel);
                }
            } catch (Exception e) {
                log.error("发送{}通知失败: {}", channel.getDescription(), e.getMessage(), e);
            }
        }
    }

    private void sendRuLiuGroupMessage(AlarmRecord alarmRecord, Map<String, String> configs) {
        String groupId = configs.get("ruliu_group_id");
        String mentionedUsers = configs.get("mentioned_users");
        String message = buildAlarmMessage(alarmRecord);
        ruLiuNotificationService.sendGroupMessage(groupId, mentionedUsers, message);
    }

    private void sendEmail(AlarmRecord alarmRecord, Map<String, String> configs) {
        String recipients = configs.get("email_recipients");
        String subject = "测试计划报警: " + alarmRecord.getTestPlanName();
        String content = buildAlarmMessage(alarmRecord);
        emailNotificationService.sendEmail(recipients, subject, content);
    }

    private void sendRuLiuPersonalMessage(AlarmRecord alarmRecord, Map<String, String> configs) {
        String userId = configs.get("ruliu_user_id");
        String message = buildAlarmMessage(alarmRecord);
        ruLiuNotificationService.sendPersonalMessage(userId, message);
    }

    private String buildAlarmMessage(AlarmRecord alarmRecord) {
        return String.format(
            "【测试计划报警】\n" +
            "计划名称: %s\n" +
            "执行ID: %s\n" +
            "报警原因: %s\n" +
            "失败次数: %d\n" +
            "报警时间: %s\n" +
            "详情链接: %s",
            alarmRecord.getTestPlanName(),
            alarmRecord.getExecutionId(),
            alarmRecord.getAlarmStatus().getDescription(),
            alarmRecord.getFailCount(),
            alarmRecord.getCreatedTime(),
            alarmRecord.getDetailUrl()
        );
    }
}
```

#### 3.3 如流通知服务

**文件路径**: `apismartmgt/service/RuLiuNotificationService.java`
```java
package com.baidu.qamate.core.apismartmgt.service;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Slf4j
@Service
public class RuLiuNotificationService {

    private final RestTemplate restTemplate;

    public RuLiuNotificationService() {
        this.restTemplate = new RestTemplate();
    }

    public void sendGroupMessage(String groupId, String mentionedUsers, String message) {
        try {
            // TODO: 调用如流API发送群消息
            String url = "https://api.ruliu.baidu.com/group/message";
            Map<String, Object> request = Map.of(
                "group_id", groupId,
                "mentioned_users", mentionedUsers,
                "message", message
            );

            // String response = restTemplate.postForObject(url, request, String.class);
            log.info("发送如流群消息成功, 群ID: {}, 消息: {}", groupId, message);
        } catch (Exception e) {
            log.error("发送如流群消息失败: {}", e.getMessage(), e);
            throw new RuntimeException("发送群消息失败", e);
        }
    }

    public void sendPersonalMessage(String userId, String message) {
        try {
            // TODO: 调用如流API发送个人消息
            String url = "https://api.ruliu.baidu.com/personal/message";
            Map<String, Object> request = Map.of(
                "user_id", userId,
                "message", message
            );

            // String response = restTemplate.postForObject(url, request, String.class);
            log.info("发送如流个人消息成功, 用户ID: {}, 消息: {}", userId, message);
        } catch (Exception e) {
            log.error("发送如流个人消息失败: {}", e.getMessage(), e);
            throw new RuntimeException("发送个人消息失败", e);
        }
    }
}
```

#### 3.4 邮件通知服务

**文件路径**: `apismartmgt/service/EmailNotificationService.java`
```java
package com.baidu.qamate.core.apismartmgt.service;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class EmailNotificationService {

    @Autowired
    private JavaMailSender mailSender;

    public void sendEmail(String recipients, String subject, String content) {
        try {
            SimpleMailMessage message = new SimpleMailMessage();
            message.setTo(recipients.split(","));
            message.setSubject(subject);
            message.setText(content);

            mailSender.send(message);
            log.info("邮件发送成功，收件人: {}, 主题: {}", recipients, subject);
        } catch (Exception e) {
            log.error("邮件发送失败: {}", e.getMessage(), e);
            throw new RuntimeException("邮件发送失败", e);
        }
    }
}
```

#### 3.5 回调服务

**文件路径**: `apismartmgt/service/CallbackService.java`
```java
package com.baidu.qamate.core.apismartmgt.service;

import com.baidu.qamate.core.apismartmgt.entity.AlarmRecord;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.Map;

@Slf4j
@Service
@RequiredArgsConstructor
public class CallbackService {

    private final RestTemplate restTemplate;
    private final ObjectMapper objectMapper;

    public void sendCallback(AlarmRecord alarmRecord, String callbackUrl, boolean isKirinCallback) {
        try {
            Map<String, Object> callbackData = buildCallbackData(alarmRecord, isKirinCallback);

            restTemplate.postForObject(callbackUrl, callbackData, String.class);
            log.info("回调发送成功, URL: {}, 报警ID: {}", callbackUrl, alarmRecord.getAlertId());
        } catch (Exception e) {
            log.error("回调发送失败: {}", e.getMessage(), e);
            throw new RuntimeException("回调发送失败", e);
        }
    }

    private Map<String, Object> buildCallbackData(AlarmRecord alarmRecord, boolean isKirinCallback) {
        if (isKirinCallback) {
            // Kirin平台规范格式
            return Map.of(
                "alert_id", alarmRecord.getAlertId(),
                "plan_name", alarmRecord.getTestPlanName(),
                "exe_id", alarmRecord.getExecutionId(),
                "fail_count", alarmRecord.getFailCount(),
                "status", alarmRecord.getAlarmStatus().getDescription(),
                "timestamp", alarmRecord.getCreatedTime().toEpochSecond(ZoneOffset.of("+8")),
                "detail_url", alarmRecord.getDetailUrl(),
                "kirin_format", true
            );
        } else {
            // 标准格式
            return Map.of(
                "alert_id", alarmRecord.getAlertId(),
                "plan_name", alarmRecord.getTestPlanName(),
                "exe_id", alarmRecord.getExecutionId(),
                "fail_count", alarmRecord.getFailCount(),
                "status", alarmRecord.getAlarmStatus().getDescription(),
                "timestamp", alarmRecord.getCreatedTime().toEpochSecond(ZoneOffset.of("+8")),
                "detail_url", alarmRecord.getDetailUrl()
            );
        }
    }
}
```

#### 3.6 报警核心服务

**文件路径**: `apismartmgt/service/AlarmService.java`
```java
package com.baidu.qamate.core.apismartmgt.service;

import com.baidu.qamate.core.apismartmgt.entity.AlarmConfig;
import com.baidu.qamate.core.apismartmgt.entity.AlarmRecord;
import com.baidu.qamate.core.apismartmgt.enums.AlarmStatus;
import com.baidu.qamate.core.apismartmgt.repository.AlarmRecordRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.UUID;

@Slf4j
@Service
@RequiredArgsConstructor
public class AlarmService {

    private final AlarmConfigService alarmConfigService;
    private final NotificationService notificationService;
    private final CallbackService callbackService;
    private final AlarmRecordRepository alarmRecordRepository;

    public void checkAndTriggerAlarm(Long testPlanId, String testPlanName, String executionId,
                                   Integer currentFailCount, AlarmStatus status) {

        // 获取报警配置
        AlarmConfig alarmConfig = alarmConfigService.getAlarmConfigByTestPlanId(testPlanId)
            .orElse(null);

        if (alarmConfig == null || !alarmConfig.getEnabled()) {
            log.info("测试计划{}未启用报警配置", testPlanId);
            return;
        }

        // 检查触发条件
        boolean shouldAlarm = checkAlarmCondition(alarmConfig, currentFailCount, status);

        if (shouldAlarm) {
            log.info("触发报警，测试计划ID: {}, 失败次数: {}, 状态: {}",
                    testPlanId, currentFailCount, status);

            // 创建报警记录
            AlarmRecord alarmRecord = createAlarmRecord(testPlanId, testPlanName, executionId,
                                                       currentFailCount, status, alarmConfig);

            // 发送通知
            try {
                notificationService.sendNotifications(alarmRecord, alarmConfig);
                alarmRecord.setAlarmStatus(AlarmStatus.SENT);
            } catch (Exception e) {
                log.error("发送通知失败: {}", e.getMessage(), e);
                alarmRecord.setAlarmStatus(AlarmStatus.FAILED);
                alarmRecord.setErrorMessage(e.getMessage());
            }

            // 发送回调
            if (alarmConfig.getCallbackUrl() != null && !alarmConfig.getCallbackUrl().isEmpty()) {
                try {
                    callbackService.sendCallback(alarmRecord, alarmConfig.getCallbackUrl(),
                                               alarmConfig.getIsKirinCallback());
                } catch (Exception e) {
                    log.error("发送回调失败: {}", e.getMessage(), e);
                    alarmRecord.setErrorMessage(e.getMessage());
                }
            }

            // 保存报警记录
            alarmRecordRepository.save(alarmRecord);
        }
    }

    private boolean checkAlarmCondition(AlarmConfig config, Integer failCount, AlarmStatus status) {
        return failCount >= config.getContinuousFailCount() ||
               status == AlarmStatus.FAILED ||
               status == AlarmStatus.RETRY;
    }

    private AlarmRecord createAlarmRecord(Long testPlanId, String testPlanName, String executionId,
                                        Integer failCount, AlarmStatus status, AlarmConfig config) {
        AlarmRecord record = new AlarmRecord();
        record.setAlertId(UUID.randomUUID().toString());
        record.setTestPlanId(testPlanId);
        record.setTestPlanName(testPlanName);
        record.setExecutionId(executionId);
        record.setFailCount(failCount);
        record.setAlarmStatus(AlarmStatus.PENDING);
        record.setDetailUrl(buildDetailUrl(executionId));
        record.setCallbackUrl(config.getCallbackUrl());

        return record;
    }

    private String buildDetailUrl(String executionId) {
        // TODO: 构建详情页URL，需要根据实际前端路由调整
        return "http://your-domain/test-execution/detail?executionId=" + executionId;
    }
}
```

### 第四阶段：控制器层开发（预计3天）

#### 4.1 报警控制器

**文件路径**: `apismartmgt/controller/AlarmController.java`
```java
package com.baidu.qamate.core.apismartmgt.controller;

import com.baidu.qamate.core.apismartmgt.entity.AlarmConfig;
import com.baidu.qamate.core.apismartmgt.entity.AlarmRecord;
import com.baidu.qamate.core.apismartmgt.service.AlarmConfigService;
import com.baidu.qamate.core.apismartmgt.service.AlarmService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@Slf4j
@RestController
@RequestMapping("/api/alarm")
@RequiredArgsConstructor
public class AlarmController {

    private final AlarmConfigService alarmConfigService;
    private final AlarmService alarmService;

    @PostMapping("/config")
    public ResponseEntity<AlarmConfig> saveAlarmConfig(@RequestBody AlarmConfig alarmConfig) {
        try {
            AlarmConfig saved = alarmConfigService.saveAlarmConfig(alarmConfig);
            return ResponseEntity.ok(saved);
        } catch (Exception e) {
            log.error("保存报警配置失败: {}", e.getMessage(), e);
            return ResponseEntity.badRequest().build();
        }
    }

    @GetMapping("/config/{testPlanId}")
    public ResponseEntity<AlarmConfig> getAlarmConfig(@PathVariable Long testPlanId) {
        Optional<AlarmConfig> config = alarmConfigService.getAlarmConfigByTestPlanId(testPlanId);
        return config.map(ResponseEntity::ok)
                   .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/config/{testPlanId}")
    public ResponseEntity<Void> deleteAlarmConfig(@PathVariable Long testPlanId) {
        try {
            alarmConfigService.deleteAlarmConfig(testPlanId);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("删除报警配置失败: {}", e.getMessage(), e);
            return ResponseEntity.badRequest().build();
        }
    }

    @GetMapping("/records/{testPlanId}")
    public ResponseEntity<List<AlarmRecord>> getAlarmRecords(@PathVariable Long testPlanId) {
        // TODO: 实现获取报警记录的逻辑
        return ResponseEntity.ok(List.of());
    }
}
```

#### 4.2 修改测试计划控制器

**文件路径**: `apismartmgt/controller/TestPlanController.java`
在现有的TestPlanController中添加报警配置相关接口：

```java
// 在现有TestPlanController中添加以下方法

@Autowired
private AlarmConfigService alarmConfigService;

@PostMapping("/{testPlanId}/alarm-config")
public ResponseEntity<AlarmConfig> setTestPlanAlarmConfig(
    @PathVariable Long testPlanId,
    @RequestBody AlarmConfig alarmConfig) {

    alarmConfig.setTestPlanId(testPlanId);
    AlarmConfig saved = alarmConfigService.saveAlarmConfig(alarmConfig);
    return ResponseEntity.ok(saved);
}

@GetMapping("/{testPlanId}/alarm-config")
public ResponseEntity<AlarmConfig> getTestPlanAlarmConfig(@PathVariable Long testPlanId) {
    Optional<AlarmConfig> config = alarmConfigService.getAlarmConfigByTestPlanId(testPlanId);
    return config.map(ResponseEntity::ok).orElse(ResponseEntity.notFound().build());
}
```

### 第五阶段：与现有系统集成（预计1周）

#### 5.1 修改测试计划执行流程

需要在现有的测试执行服务中集成报警逻辑。找到TestCaseExecutionService或类似的执行服务，添加报警触发点：

```java
// 在测试执行失败时调用报警服务
@Autowired
private AlarmService alarmService;

public void handleTestExecutionFailure(Long testPlanId, String testPlanName,
                                     String executionId, Integer failCount) {
    AlarmStatus status = AlarmStatus.FAILED;
    alarmService.checkAndTriggerAlarm(testPlanId, testPlanName, executionId,
                                    failCount, status);
}

public void handleTestExecutionTimeout(Long testPlanId, String testPlanName,
                                     String executionId) {
    AlarmStatus status = AlarmStatus.RETRY;
    alarmService.checkAndTriggerAlarm(testPlanId, testPlanName, executionId,
                                    1, status);
}
```

#### 5.2 提供失败详情查询接口

**文件路径**: `apismartmgt/controller/TestExecutionController.java`
```java
@GetMapping("/execution/{executionId}/detail")
public ResponseEntity<Object> getExecutionDetail(@PathVariable String executionId) {
    // TODO: 实现获取执行详情的逻辑
    // 返回包含执行状态、失败用例、错误信息等详情
    return ResponseEntity.ok(Map.of(
        "executionId", executionId,
        "status", "failed",
        "failedCases", List.of(),
        "errorMessages", List.of()
    ));
}
```

### 第六阶段：配置和部署（预计2天）

#### 6.1 添加邮件配置

在`application.yml`中添加邮件配置：

```yaml
spring:
  mail:
    host: smtp.baidu.com
    port: 587
    username: your-email@baidu.com
    password: your-password
    properties:
      mail:
        smtp:
          auth: true
          starttls:
            enable: true
```

#### 6.2 添加如流API配置

```yaml
ruliu:
  api:
    base-url: https://api.ruliu.baidu.com
    token: your-ruliu-token
```

### 第七阶段：测试验证（预计3天）

#### 7.1 单元测试

为每个服务类编写单元测试，确保业务逻辑正确。

#### 7.2 集成测试

测试完整的报警流程：触发条件检查 → 报警记录创建 → 通知发送 → 回调调用。

#### 7.3 功能测试

通过API测试工具验证所有接口功能正常。

## 新手开发指导

### 开发环境准备
1. 确保已安装JDK 8+
2. 安装Maven 3.6+
3. 使用IDE（推荐IntelliJ IDEA）
4. 配置数据库连接

### 开发步骤
1. 按阶段顺序开发，完成一个阶段再进行下一个阶段
2. 每个类创建后立即编写对应的测试
3. 遇到问题时查看日志文件获取详细错误信息
4. 参考现有代码的命名规范和架构模式

### 注意事项
- 所有新增的实体类需要添加`@Entity`注解
- 使用Lombok的`@Data`注解简化getter/setter
- 使用`@Slf4j`注解进行日志记录
- 异常处理要捕获具体异常类型
- 数据库操作要考虑事务性

## 代码修改原理详解

### 第一阶段：数据库设计和基础实体

#### 1.1 创建枚举类

**修改原理**：枚举类用于定义固定常量，提高代码可读性和类型安全性。

**NotificationChannel.java 修改原理**：
- 使用枚举定义三种通知渠道，避免魔法字符串
- 每个枚举项都有对应的中文描述，便于前端显示
- 使用`getDescription()`方法返回描述信息

**AlarmStatus.java 修改原理**：
- 定义报警记录的四种状态
- 状态变化遵循：PENDING → SENT/FAILED → RETRY
- 便于报警记录的状态管理和查询

#### 1.2 创建报警配置实体类

**AlarmConfig.java 修改原理**：
- `@Entity`注解告诉JPA这是一个数据库表对应的实体类
- `@Table(name = "alarm_config")`指定数据库表名
- `@Id`和`@GeneratedValue`定义主键和自增策略
- `@Column`注解自定义数据库列名和属性
- `@ElementCollection`用于存储集合类型的配置（通知渠道列表、渠道配置映射）
- `@CollectionTable`指定集合数据的存储表
- `@CreationTimestamp`和`@UpdateTimestamp`自动记录创建和更新时间

#### 1.3 创建报警记录实体类

**AlarmRecord.java 修改原理**：
- 记录每次报警触发的详细信息
- `alertId`使用UUID确保唯一性
- 存储测试计划基本信息，便于查询和展示
- `retryCount`字段用于记录重试次数
- `errorMessage`字段记录失败原因，便于问题排查

### 第二阶段：数据访问层开发

#### 2.1 创建Repository接口

**AlarmConfigRepository.java 修改原理**：
- 继承`JpaRepository`获得基本CRUD操作
- `findByTestPlanId`方法根据测试计划ID查询配置
- `deleteByTestPlanId`方法删除指定测试计划的配置
- Spring Data JPA会自动实现这些方法

**AlarmRecordRepository.java 修改原理**：
- 提供多种查询方法，满足不同的业务需求
- 时间范围查询用于报警统计
- 状态查询用于重试机制

### 第三阶段：业务逻辑层开发

#### 3.1 报警配置服务

**AlarmConfigService.java 修改原理**：
- 封装报警配置的CRUD操作
- 使用`Optional`处理可能为空的查询结果
- 添加日志记录便于问题追踪
- 异常处理保证系统的健壮性

#### 3.2 通知服务

**NotificationService.java 修改原理**：
- 统一管理多种通知渠道的发送逻辑
- 使用策略模式处理不同的通知方式
- 每种通知方式独立处理，避免相互影响
- 消息模板统一管理，便于维护

**RuLiuNotificationService.java 修改原理**：
- 封装如流API的调用逻辑
- 使用`RestTemplate`进行HTTP请求
- 异常处理和日志记录保证可追踪性
- TODO注释提示需要配置实际的API地址

**EmailNotificationService.java 修改原理**：
- 使用Spring的`JavaMailSender`发送邮件
- `SimpleMailMessage`用于简单文本邮件
- 批量发送支持多个收件人
- 邮件配置通过Spring的自动配置完成

#### 3.3 回调服务

**CallbackService.java 修改原理**：
- 支持两种回调格式：标准格式和Kirin格式
- 使用`ObjectMapper`处理JSON序列化
- HTTP异常处理确保网络问题不会影响主流程
- 回调数据构建逻辑独立，便于扩展

#### 3.4 报警核心服务

**AlarmService.java 修改原理**：
- 报警触发的主入口点
- 条件检查逻辑：失败次数、超时等
- 异步通知和回调发送
- 报警记录的生命周期管理
- 详情URL构建逻辑

### 第四阶段：控制器层开发

#### 4.1 报警控制器

**AlarmController.java 修改原理**：
- RESTful API设计，使用标准HTTP方法
- 统一异常处理和响应格式
- 参数验证确保数据完整性
- 日志记录便于API调用追踪

#### 4.2 修改测试计划控制器

**TestPlanController.java 修改原理**：
- 在现有控制器中集成报警配置功能
- URL路径设计遵循RESTful规范
- 测试计划ID作为路径参数传递
- 保持与现有API的一致性

### 第五阶段：与现有系统集成

#### 5.1 修改测试计划执行流程

**集成原理**：
- 在测试执行的关键节点添加报警触发
- 失败处理逻辑中增加报警调用
- 超时处理中集成报警机制
- 保持原有执行逻辑不变，只添加报警功能

#### 5.2 提供失败详情查询接口

**TestExecutionController.java 修改原理**：
- 提供执行详情的查询接口
- 返回结构化的失败信息
- 支持报警详情链接的跳转
- 数据格式便于前端展示

### 第六阶段：配置和部署

#### 6.1 添加邮件配置

**配置原理**：
- Spring Boot自动配置邮件发送器
- SMTP服务器配置用于邮件发送
- 认证和TLS配置确保安全性
- 可通过环境变量或配置文件管理敏感信息

#### 6.2 添加如流API配置

**配置原理**：
- 自定义配置项便于API调用
- 基础URL和Token配置统一管理
- 支持不同环境的配置切换

### 第七阶段：测试验证

#### 7.1 单元测试

**测试原理**：
- 每个服务类对应的测试类
- Mock外部依赖，专注业务逻辑测试
- 边界条件测试确保健壮性
- 异常场景测试保证错误处理正确

#### 7.2 集成测试

**测试原理**：
- 完整流程的端到端测试
- 数据库操作验证
- 外部API调用的模拟测试
- 异常情况的处理验证

#### 7.3 功能测试

**测试原理**：
- API接口的功能验证
- 前后端交互测试
- 用户体验测试
- 性能和压力测试

## 现有文件修改说明

### 需要修改的现有文件

#### 1. TestPlan.java
**修改原理**：添加报警配置的关联关系
```java
// 在TestPlan实体类中添加
@OneToOne(mappedBy = "testPlanId", cascade = CascadeType.ALL)
private AlarmConfig alarmConfig;
```

#### 2. TestCaseExecutionService.java
**修改原理**：在测试执行的关键位置添加报警触发逻辑
- 在测试失败处理方法中添加：`alarmService.checkAndTriggerAlarm(...)`
- 在超时处理方法中添加报警调用
- 确保报警触发不影响原有执行流程

#### 3. application.yml
**修改原理**：添加必要的系统配置
- 邮件服务器配置
- 如流API配置
- 数据库表自动创建配置

### 新增依赖项说明

#### pom.xml需要添加的依赖
```xml
<!-- Lombok：简化getter/setter -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
</dependency>

<!-- 邮件发送支持 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-mail</artifactId>
</dependency>

<!-- HTTP客户端 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

### 数据库变更说明

#### 新增表结构
1. **alarm_config表**：存储报警配置
2. **alarm_notification_channels表**：存储通知渠道配置
3. **alarm_channel_configs表**：存储渠道详细配置
4. **alarm_record表**：存储报警历史记录

#### 变更影响
- 新增表不会影响现有数据
- 通过外键关联确保数据完整性
- 支持数据迁移和版本升级

## 部署注意事项

### 1. 数据库迁移
- 使用Flyway或Liquibase管理数据库版本
- 创建迁移脚本确保表结构正确
- 测试数据迁移确保不丢失现有数据

### 2. 配置管理
- 敏感配置使用环境变量
- 不同环境的配置分离
- 配置验证确保启动正确

### 3. 监控和日志
- 报警功能的调用监控
- 异常情况的详细日志
- 性能指标收集和报警

### 4. 安全考虑
- API接口的权限控制
- 回调URL的安全性验证
- 敏感信息的加密存储

## 总体时间安排

- 第一阶段：1周
- 第二阶段：3天
- 第三阶段：1周
- 第四阶段：3天
- 第五阶段：1周
- 第六阶段：2天
- 第七阶段：3天

**总计：约4-5周**

## 后续扩展

完成后可以考虑的功能扩展：
1. 报警记录的前端展示页面
2. 报警统计分析功能
3. 更多的通知渠道（短信、钉钉等）
4. 报警规则的更复杂配置
5. 报警降噪和聚合策略