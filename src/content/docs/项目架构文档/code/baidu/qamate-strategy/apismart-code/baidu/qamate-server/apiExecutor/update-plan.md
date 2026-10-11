---
title: "升级计划（基于 diff-test 大版本的框架升级）"
description: "本代码库在原版基础上已完成 diff 测试大版本升级（新增 json-unit-core、jsonassert、java-diff-utils、protobuf 等依赖及对应业务代码）。 本次升级目标是在此基础上叠加 Java/框架版本升级"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\baidu\\qamate-server\\apiExecutor\\update-plan.md"
---
# 升级计划（基于 diff-test 大版本的框架升级）

## 背景说明

本代码库在原版基础上已完成 **diff 测试大版本升级**（新增 json-unit-core、jsonassert、java-diff-utils、protobuf 等依赖及对应业务代码）。
本次升级目标是在此基础上叠加 Java/框架版本升级，不能影响已有的 diff 测试功能。

参考实现：`/Users/gaolizhe/workspace/gaolizhe/baidu/qamate-server/apiExecutor`

---

## 目标版本

| 组件                 | 当前              | 目标       |
|----------------------|-------------------|------------|
| Java                 | 11（实际编译）    | 17         |
| Spring Boot          | 2.3.2.RELEASE     | 3.5.9      |
| Spring Cloud         | Hoxton.SR8        | 2025.0.1   |
| Spring Cloud Alibaba | 2.2.3.RELEASE     | 彻底删除   |
| MapStruct            | 1.5.0.Beta2       | 1.5.5.Final |
| MyBatis-Plus         | mybatis-plus-boot-starter | mybatis-plus-spring-boot3-starter |
| MySQL Driver         | mysql-connector-java | mysql-connector-j |
| Swagger              | springfox-boot-starter 3.0.0 | springdoc-openapi-starter-webmvc-ui 2.8.8 |

---

## 阶段一：pom.xml 改造

### 1.1 根 pom.xml

**版本属性——修改：**
```xml
<spring-boot.version>3.5.9</spring-boot.version>
<spring-cloud.version>2025.0.1</spring-cloud.version>
<mapstruct.version>1.5.5.Final</mapstruct.version>
```

**版本属性——删除（整个 Alibaba Cloud 生态及冗余属性）：**
```
alibaba-cloud.version
nacos-config-spring-boot-starter.version
sentinel-starter.version
sentinel.version
alibaba-cloud.version
dozer.version
log4j2.version
springfox-swagger.version
springfox.version
es.version（已注释，直接删除）
timing-task.version
bos.version
nacos.version
ONS.version
itp-common.version
```

**dependencyManagement——修改 spring-cloud-dependencies 版本：**
```xml
<!-- 旧 -->
<version>Hoxton.SR8</version>
<!-- 新 -->
<version>2025.0.1</version>
```

**dependencyManagement——删除：**
```xml
<!-- 删除以下三块 -->
<dependency> spring-cloud-alibaba-dependencies </dependency>
<dependency> spring-cloud-starter-alibaba-nacos-config </dependency>
<dependency> net.sf.dozer:dozer </dependency>
```

---

### 1.2 executor-server/pom.xml

**删除的依赖：**
```
1. com.alibaba.cloud:spring-cloud-starter-alibaba-nacos-config
2. com.alibaba.cloud:spring-cloud-starter-alibaba-nacos-discovery
3. com.alibaba.nacos:nacos-client
4. com.alibaba.cloud:spring-cloud-starter-alibaba-sentinel（两处）
5. net.sf.dozer:dozer
6. org.hibernate.validator:hibernate-validator（6.0.13.Final，Boot 3.x 自带 jakarta 版本）
7. com.baidu.itp:itp-common
8. org.springframework:spring-test（5.0.4.RELEASE，与 Boot 3.x 冲突）
9. junit:junit（4.13，spring-boot-starter-test 已包含 JUnit 5）
10. org.mortbay.jetty:jetty-util（6.1.26，冲突）
11. io.springfox:springfox-boot-starter（替换为 springdoc）
12. cn.afterturn:easypoi-base（3.2.0 → 4.4.0）
13. cn.afterturn:easypoi-annotation（3.2.0 → 4.4.0）
14. mysql:mysql-connector-java（替换）
```

**新增/替换的依赖：**
```xml
<!-- 1. 替换 Swagger -->
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.8.8</version>
</dependency>

<!-- 2. 替换 MySQL 驱动（版本由 Spring Boot 3.x 统一管理） -->
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
</dependency>

<!-- 3. 替换 MyBatis-Plus starter（Spring Boot 3.x 专用） -->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
</dependency>

<!-- 4. easypoi 升级至 4.4.0（解决 javax 兼容问题） -->
<dependency>
    <groupId>cn.afterturn</groupId>
    <artifactId>easypoi-base</artifactId>
    <version>4.4.0</version>
</dependency>
<dependency>
    <groupId>cn.afterturn</groupId>
    <artifactId>easypoi-annotation</artifactId>
    <version>4.4.0</version>
</dependency>

<!-- 5. 显式声明 fastjson（不再通过 itp-common 传递） -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
</dependency>
```

**保留不动（diff 测试升级带入的依赖）：**
```
net.javacrumbs.json-unit:json-unit-core 2.38.0
org.skyscreamer:jsonassert 1.5.3
io.github.java-diff-utils:java-diff-utils 4.12
com.google.protobuf:protobuf-java 3.25.3
com.google.protobuf:protobuf-java-util 3.25.3
```

**maven-compiler-plugin——修复编译目标版本：**
```xml
<!-- 旧 -->
<source>11</source>
<target>11</target>
<!-- 新 -->
<source>17</source>
<target>17</target>
```

**删除 profiles 中的 mysql.connector.version**（Spring Boot 统一管理后不再需要按环境区分驱动版本）

---

## 阶段二：Java 代码改造

### 2.1 javax → jakarta 迁移

| 文件 | 旧 import | 新 import |
|------|-----------|-----------|
| RestInterceptor.java | `javax.servlet.http.HttpServletRequest` | `jakarta.servlet.http.HttpServletRequest` |
| RestInterceptor.java | `javax.servlet.http.HttpServletResponse` | `jakarta.servlet.http.HttpServletResponse` |
| JSONConfig.java | `javax.annotation.PostConstruct` | `jakarta.annotation.PostConstruct` |
| RedisKeyUtils.java | `javax.annotation.PostConstruct` | `jakarta.annotation.PostConstruct` |
| TaskController.java | `javax.annotation.Nonnull` | `org.springframework.lang.NonNull` |
| TaskController.java | `javax.validation.constraints.NotEmpty` | `jakarta.validation.constraints.NotEmpty` |
| RunnerTask.java | `javax.annotation.Nonnull` | `org.springframework.lang.NonNull` |
| DebugExecuteCaseTaskDto.java | `javax.annotation.Nonnull` | `org.springframework.lang.NonNull` |
| DebugExecuteCaseTaskInfoDto.java | `javax.annotation.Nonnull` | `org.springframework.lang.NonNull` |
| ApacheHttpClientTest.java | `javax.annotation.Resource` | `jakarta.annotation.Resource` |
| QAMateDeviceClientTest.java | `javax.annotation.Resource` | `jakarta.annotation.Resource` |

---

### 2.2 移除 itp-common（4 处）

**① 新建本地 IExceptionEnum 接口**
路径：`executor-server/src/main/java/com/baidu/qamate/server/common/conf/exception/IExceptionEnum.java`
```java
package com.baidu.qamate.server.common.conf.exception;

public interface IExceptionEnum {
    Integer getCode();
    String getMsg();
}
```

**② ServiceExceptionEnum.java**
```java
// 删除
import com.baidu.itp.common.IExceptionEnum;
// 添加
import com.baidu.qamate.server.common.conf.exception.IExceptionEnum;
```

**③ TaskController.java**
```java
// 删除
import com.baidu.itp.global.vo.CommonResult;
// 添加
import com.baidu.qamate.server.controller.result.ApiCommonResult;
// 返回类型 CommonResult → ApiCommonResult<Boolean>
// CommonResult.build(() -> finalResult) → ApiCommonResult.success(finalResult)
```

**④ ApiCommonResult.java**
```java
// 删除
import static com.baidu.itp.global.vo.CommonResult.CODE_SUCCESS;
// 改为类内定义
private static final Integer CODE_SUCCESS = 0;
```

**⑤ DbCostInterceptor.java**
```java
// 删除 itp-common 的 InterfaceLog 相关导入和使用
import com.baidu.itp.interfacelog.aspect.InterfaceLogAspect;
import com.baidu.itp.interfacelog.entity.InterfaceLogEntity;
@Autowired
private InterfaceLogAspect interfaceLogAspect;
// intercept 方法简化为只保留 SQL 耗时日志，删除 entity 写入逻辑
```

---

### 2.3 移除 Nacos 工具类引用

**JRedisConnector.java：**
```java
// 删除（nacos 内部工具类，随 nacos 依赖一并消失）
import com.alibaba.nacos.client.utils.IPUtil;

// 旧写法
if (IPUtil.isIPV4(request.getHost()) || IPUtil.isIPV6(request.getHost())) { ... }

// 新写法（改用 commons-validator，该依赖在 executor-server/pom.xml 中已有）
import org.apache.commons.validator.routines.InetAddressValidator;
if (InetAddressValidator.getInstance().isValid(request.getHost())) { ... }
```

---

### 2.4 修复 OKHttp 内部 API 变更

**OKHttpParseRemoteIpInterceptor.java**（升级 OKHttp 后，旧内部 API `Transmitter`/`RealConnection` 已被移除）：
```java
// 删除
import okhttp3.internal.connection.RealConnection;
import okhttp3.internal.connection.Transmitter;

// 旧写法
Transmitter transmitter = realChain.transmitter();
RealConnection connection = transmitter.connection;
remoteIp = connection.route().socketAddress().getAddress().getHostAddress();

// 新写法（使用公开 API）
import okhttp3.Connection;
Connection connection = realChain.connection();
if (connection != null) {
    remoteIp = connection.route().socketAddress().getAddress().getHostAddress();
}
```

---

### 2.5 移除 Ribbon 和 Nacos Discovery

**App.java：**
```java
// 删除
import com.baidu.qamate.server.common.conf.ribbon.MyLoadBalanceConfig;
import org.springframework.cloud.netflix.ribbon.RibbonClient;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@RibbonClient(name = "qamate-api-executor", configuration = {MyLoadBalanceConfig.class})
@EnableDiscoveryClient
```

**整个文件删除：**
- `common/conf/ribbon/MyLoadBalanceConfig.java`

---

### 2.4 移除 Sentinel 依赖

**ExecutorConfiguration.java：**
```java
// 删除
import com.alibaba.csp.sentinel.util.HostNameUtil;

// 旧写法
private String namePrefix = HostNameUtil.getIp() + "-job-executor-";

// 新写法
private static String getLocalIp() {
    try {
        return InetAddress.getLocalHost().getHostAddress();
    } catch (Exception e) {
        return "unknown";
    }
}
private String namePrefix = getLocalIp() + "-job-executor-";
// 同时添加 import java.net.InetAddress;
```

---

### 2.5 Swagger 代码替换

**SwaggerConfig.java——整体替换：**
```java
package com.baidu.qamate.server.common.conf.swagger;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SwaggerConfig {
    @Bean
    public OpenAPI openAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("qamate api 执行器接口文档")
                        .version("v1.0")
                        .description("qamate api 执行器接口文档"));
    }
}
```

**其余文件注解替换：**

| 旧注解（springfox）         | 新注解（springdoc）              |
|-----------------------------|----------------------------------|
| `@Api(value="...")`         | `@Tag(name="...")`               |
| `@ApiOperation("...")`      | `@Operation(summary="...")`      |
| `@ApiModel`                 | `@Schema`                        |
| `@ApiModelProperty("...")` | `@Schema(description="...")`     |

涉及文件（import 路径由 `io.swagger.annotations.*` 改为 `io.swagger.v3.oas.annotations.*`），共 7 个：
- `controller/TaskController.java` — `@Api` → `@Tag`，`@ApiOperation` → `@Operation`
- `controller/EnvController.java` — `@Api` → `@Tag`，`@ApiOperation` → `@Operation`
- `controller/ScriptController.java` — `@Api` → `@Tag`，`@ApiOperation` → `@Operation`
- `controller/KirinController.java` — `@ApiOperation` → `@Operation`
- `controller/dto/EnvDto.java` — `@ApiModel` → `@Schema`，`@ApiModelProperty` → `@Schema`
- `runner/bo/RunnerTask.java` — `@ApiModel` → `@Schema`，`@ApiModelProperty` → `@Schema`
- `common/dto/caseexe/DebugExecuteCaseTaskDto.java` — `@ApiModel` → `@Schema`，`@ApiModelProperty` → `@Schema`
- `common/dto/caseexe/DebugExecuteCaseTaskInfoDto.java` — `@ApiModel` → `@Schema`，`@ApiModelProperty` → `@Schema`
- `common/dto/caseexe/DebugExecuteCaseTaskExtInfoDto.java` — `@ApiModel` → `@Schema`，`@ApiModelProperty` → `@Schema`

**SpringMVCConfiguration.java——更新 Swagger 路径排除：**
```java
// 旧
"/swagger-resources/**", "/webjars/**", "/v2/**", "/v3/**", "/swagger-ui.html/**"
// 新
"/v3/api-docs/**", "/swagger-ui/**", "/swagger-ui.html"
```

---

### 2.8 Spring Boot 3.x Bean 注入歧义修复（新增 @Qualifier）

Spring Boot 3.x 对构造器注入中存在多个候选 Bean 时更加严格，需显式加 `@Qualifier`：

- **CaseProcessor.java**
```java
import org.springframework.beans.factory.annotation.Qualifier;
// 旧
public CaseProcessor(StepProcessor stepProcessor) { ... }
// 新
public CaseProcessor(@Qualifier("stepProcessor") StepProcessor stepProcessor) { ... }
```

- **PlanProcessor.java**
```java
import org.springframework.beans.factory.annotation.Qualifier;
// 旧
public PlanProcessor(StepProcessor stepProcessor) { ... }
// 新
public PlanProcessor(@Qualifier("stepProcessor") StepProcessor stepProcessor) { ... }
```

- **CaseRunner.java**
```java
import org.springframework.beans.factory.annotation.Qualifier;
// 旧
public CaseRunner(CaseProcessor caseProcessor, CaseDebugService caseDebugService) { ... }
// 新
public CaseRunner(@Qualifier("caseProcessor") CaseProcessor caseProcessor, CaseDebugService caseDebugService) { ... }
```

---

## 阶段三：配置文件改造

### 3.1 文件重命名

Spring Boot 3.x 不再支持 bootstrap 上下文（已移除 Spring Cloud Context 的 bootstrap 机制），直接使用标准 application.yml：

| 旧文件名              | 新文件名              |
|-----------------------|-----------------------|
| bootstrap.yml         | application.yml       |
| bootstrap-dev.yml     | application-dev.yml   |
| bootstrap-test.yml    | application-test.yml  |
| bootstrap-prod.yml    | application-prod.yml  |
| bootstrap-sandbox.yml | application-sandbox.yml |

---

### 3.2 配置内容清理

每个环境配置文件中删除以下 Nacos/Sentinel 块：
```yaml
spring:
  cloud:
    nacos:          # 整块删除
    sentinel:       # 整块删除

feign:
  sentinel:
    enabled: true   # 删除

management:
  health:
    sentinel:
      enabled: false  # 删除
```

**MySQL 驱动类名修改（每个用到的环境配置文件）：**
```yaml
# 旧
driver-class-name: com.mysql.jdbc.Driver
# 新
driver-class-name: com.mysql.cj.jdbc.Driver
```

**静态资源配置键修改（Spring Boot 3.x 变更）：**
```yaml
# 旧
spring:
  resources:
    add-mappings: false
# 新
spring:
  web:
    resources:
      add-mappings: false
```

---

### 3.3 Nacos 配置迁移

将各环境 Nacos 中存储的配置内容导出，合并到对应 application-{env}.yml 中（包括数据库连接信息、Redis、等需要从 Nacos 读取的配置）。

---

## 阶段四：验证步骤

```bash
# 1. 编译验证
mvn clean compile

# 2. 本地启动
mvn spring-boot:run -pl executor-server -Pdev

# 3. Swagger 文档
curl http://localhost:8080/swagger-ui/index.html

# 4. 核心接口验证
curl -X POST http://localhost:8080/task/case/submit

# 5. diff 测试功能验证（验证 diff 升级功能未被破坏）
# 运行 diff 相关测试用例

# 6. 部署 test 环境验证
```

---

## 风险项汇总

| 风险 | 级别 | 说明 |
|------|------|------|
| `netty-websocket-spring-boot-starter:0.12.0` | 中 | 基于 Boot 2.x，需确认是否实际使用了 WebSocket；若未用可删除 |
| `json-unit-core 2.38.0`（diff 测试引入）| 低 | 需确认与 Boot 3.x 的兼容性；该库为标准 Java 库，预计兼容 |
| `feign-form SpringFormEncoder` | 低 | Spring Cloud 2025.0.x 中需确认版本，若有问题升级到最新 |
| `bookkeeper-common-allocator` / `aircompressor` | 低 | 较小众依赖，注意 Boot 3.x 下的版本冲突 |
| Nacos 配置迁移 | 中 | 各环境 Nacos 中的配置必须完整迁出，否则启动时缺少配置 |
| `itp-common` 中的 `CommonResult.build()` 语义 | 低 | 替换为 `ApiCommonResult.success()` 时注意异常场景返回值一致性 |
