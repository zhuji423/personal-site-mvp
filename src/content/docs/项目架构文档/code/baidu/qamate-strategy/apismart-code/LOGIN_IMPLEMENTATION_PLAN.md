---
title: "密码登录和Cookie登录功能实现计划"
description: "- 新系统（QAMate）: - Core 模块：Spring Boot 3.2.0 + Java 21，已有 UUAP SSO 和 OpenAPI Token 认证，代码位于 apismartmgt 包 - Executor 模块：Spr"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\LOGIN_IMPLEMENTATION_PLAN.md"
---
# 密码登录和Cookie登录功能实现计划

## Context（上下文）

### 为什么需要这个功能
QAMate 新系统需要支持**密码登录**和**Cookie登录**两种方式，以便在测试执行过程中自动完成身份认证。老系统（ITP）已有成熟的 Passport 登录实现，我们将复刻其核心逻辑，简化为只支持这两种登录方式。

### 当前状态
- **老系统（ITP）**: 位于 `/baidu/inner-os/itp/itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/login/`
  - `AbstractLogin`：模板方法模式，定义 `init() → check() → doLogin()` 流程
  - `PassportLogin`：调用 Passport API（`http://10.143.152.33:8110/passqa/api/mkbduss`）获取 BDUSS 和 STOKEN
  - `BaseLoginConf`：配置类，支持 username/password 或直接提供 cookie

- **新系统（QAMate）**:
  - **Core 模块**：Spring Boot 3.2.0 + Java 21，已有 UUAP SSO 和 OpenAPI Token 认证，代码位于 `apismartmgt` 包
  - **Executor 模块**：Spring Boot 3.5.9 + Java 17，通过 OpenFeign 调用 Core 服务，代码组织为 Controller → Service → Feign Client

### 目标
实现**统一的登录接口**，根据提供的参数智能选择登录方式：
- **提供 cookie**：直接使用 cookie（优先级最高）
- **提供 username + password**：调用 Passport API 获取 cookie
- **都提供**：优先使用 cookie
- **都不提供**：返回错误

采用双层实现：
- **Core 提供 REST API**：`/apismart/login`（单一接口）
- **Executor 调用 Core API**：`/auth/login`（单一接口）

---

## 架构设计

### 模块职责划分

#### Core 模块（认证服务层）
**位置**: `/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code/baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/`

**职责**:
1. 提供 REST API：`/apismart/login`（统一接口）
2. 调用 Passport API 获取 BDUSS/STOKEN（仅密码登录）
3. 数据库存储（基于 ITP `tb_login_info` 表设计）
4. 返回统一的登录结果

**不实现**:
- ❌ 复杂的会话管理（Redis）
- ❌ RequestFilter 集成（可作为后续扩展）
- ❌ 多个登录接口（只有一个统一接口）

#### Executor 模块（执行器层）
**位置**: `/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code/baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/`

**职责**:
1. 提供本地 REST API 供测试脚本调用
2. 通过 Feign Client 调用 Core 登录接口
3. 将获取的 Cookie 注入到后续的 HTTP 测试请求
4. 简单的内存缓存（避免同一用户重复登录）

---

## 实现方案

### Phase 1: 数据库设计（Week 1）

#### 数据库信息
- **数据源名称**: `newsource`（主数据源）
- **数据库名**:
  - Dev 环境: `core`
  - Test 环境: `test_qamate`
  - 线上环境: `qamate`

#### 表结构设计（基于 ITP `tb_login_info` 表）

**表名**: `apismart_auth_credentials`

```sql
CREATE TABLE `apismart_auth_credentials` (
    -- 主键
    `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '自增主键',

    -- 登录类型
    `type` INT(2) NOT NULL DEFAULT 0 COMMENT '登录类型：0=UC, 1=Passport, 2=UUAP, 3=EAP, 4=BCE',

    -- 账号信息
    `name` VARCHAR(100) DEFAULT NULL COMMENT '账号名称/描述（用于识别账号用途）',

    -- 登录凭证
    `login_name` VARCHAR(100) DEFAULT NULL COMMENT '登录用户名',
    `login_pwd` VARCHAR(255) DEFAULT NULL COMMENT '登录密码（加密存储：encrypt::密文）',

    -- 关联信息
    `module_id` BIGINT NOT NULL COMMENT '业务模块ID',

    -- 可见性（软删除）
    `is_visible` TINYINT NOT NULL DEFAULT 0 COMMENT '可见性：0=可见, 1=不可见',

    -- Cookie 和配置参数
    `cookies` TEXT DEFAULT NULL COMMENT 'Cookie 信息（JSON 格式）',
    `params` TEXT DEFAULT NULL COMMENT '其他配置参数（JSON 格式，如 uuapUrl, serviceUrl）',

    -- 环境标识
    `is_online` TINYINT NOT NULL DEFAULT 0 COMMENT '环境标识：0=线下, 1=线上',

    -- 登录方式
    `login_method` INT(2) DEFAULT NULL COMMENT '登录方式：0=账号密码登录, 1=Cookie登录',

    -- 账户类型和角色
    `account_type` VARCHAR(32) DEFAULT NULL COMMENT '账户类型',
    `role` VARCHAR(32) DEFAULT NULL COMMENT '权限角色：admin/normal',

    -- 审计字段
    `create_user` VARCHAR(64) DEFAULT NULL COMMENT '创建人',
    `create_time` BIGINT DEFAULT NULL COMMENT '创建时间（毫秒时间戳）',
    `update_user` VARCHAR(64) DEFAULT NULL COMMENT '更新人',
    `update_time` BIGINT DEFAULT NULL COMMENT '更新时间（毫秒时间戳）',
    `is_del` TINYINT DEFAULT 0 COMMENT '是否删除：0=否, 1=是',

    -- 主键和索引
    PRIMARY KEY (`id`, `is_online`),
    KEY `idx_module_id` (`module_id`),
    KEY `idx_type` (`type`),
    KEY `idx_is_visible` (`is_visible`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='API Smart 认证凭据表（基于 ITP tb_login_info 设计）';
```

#### 加密机制

**兼容 ITP 的 DES-CBC 加密**：
- 存储格式：`encrypt::DES_CBC_密文`
- 使用 MyBatis TypeHandler 自动加解密
- 与 ITP 数据库保持兼容，便于数据迁移

---

### Phase 2: Core 模块实现（Week 1-2）

#### 文件结构
```
/core/src/main/java/com/baidu/qamate/core/apismartmgt/
├── controller/
│   └── LoginController.java                      # REST API（新增）
├── service/
│   ├── LoginService.java                         # 业务逻辑接口（新增）
│   ├── AuthCredentialService.java                # 数据访问接口（新增）
│   └── impl/
│       ├── LoginServiceImpl.java                 # 业务逻辑实现（新增）
│       └── AuthCredentialServiceImpl.java        # 数据访问实现（新增）
├── entity/
│   └── AuthCredentialEntity.java                 # 数据库实体（新增）
├── mapper/
│   └── AuthCredentialMapper.java                 # MyBatis Mapper（新增）
├── vo/
│   └── login/                                    # 登录相关VO（新增）
│       ├── LoginRequest.java                     # 统一登录请求
│       └── LoginResponse.java                    # 登录响应
└── util/
    ├── PassportHttpClient.java                   # Passport API调用工具（新增）
    └── PasswordEncryptHandler.java               # 密码加解密 TypeHandler（新增）
```

---

### Phase 3: Executor 模块实现（Week 2）

#### 文件结构
```
/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/
├── controller/
│   └── AuthController.java                       # 登录接口控制器（新增）
├── service/
│   ├── AuthService.java                          # 接口（新增）
│   └── impl/
│       └── AuthServiceImpl.java                  # 本地缓存+调用Core（新增）
├── common/conf/feign/
│   ├── client/
│   │   └── QAMateAuthClient.java                 # Feign客户端（新增）
│   ├── request/
│   │   └── AuthLoginRequest.java                 # 统一登录请求（新增）
│   └── response/
│       └── AuthLoginResponse.java                # 登录响应（新增）
└── controller/dto/
    └── LoginDto.java                              # Controller层DTO（新增）
```

---

## API 设计

### REST 端点

#### Core 模块
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/apismart/login` | 无 | 统一登录接口 |

#### Executor 模块
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/auth/login` | 无 | 统一登录接口（调用Core） |

### 请求格式

**统一登录请求**（三种场景）:

场景1：**密码登录**
```json
{
  "username": "testuser",
  "password": "Asd123"
}
```

场景2：**Cookie登录**
```json
{
  "username": "testuser",
  "cookie": "__cas__st__=NLI;BDUSS=xxx"
}
```

场景3：**同时提供（优先使用Cookie）**
```json
{
  "username": "testuser",
  "password": "Asd123",
  "cookie": "__cas__st__=NLI;BDUSS=xxx"
}
```

---

## 关键文件清单

### Core 模块（优先实现）
1. `/core/src/main/resources/sql/apismart_auth_credentials.sql` - 建表SQL（新增）
2. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/entity/AuthCredentialEntity.java` - 数据库实体（新增）
3. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/mapper/AuthCredentialMapper.java` - MyBatis Mapper（新增）
4. `/core/src/main/resources/mapper/AuthCredentialMapper.xml` - Mapper XML（新增）
5. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/util/PasswordEncryptHandler.java` - 密码加解密（新增）
6. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/AuthCredentialService.java` - 数据访问接口（新增）
7. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/AuthCredentialServiceImpl.java` - 数据访问实现（新增）
8. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/LoginController.java` - REST API（新增）
9. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/LoginService.java` - 业务逻辑接口（新增）
10. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/LoginServiceImpl.java` - 业务逻辑实现（新增）
11. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/vo/login/LoginRequest.java` - 统一请求VO（新增）
12. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/vo/login/LoginResponse.java` - 响应VO（新增）
13. `/core/src/main/java/com/baidu/qamate/core/apismartmgt/util/PassportHttpClient.java` - HTTP工具（新增）

### Executor 模块
14. `/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/controller/AuthController.java` - API入口（新增）
15. `/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/service/AuthService.java` - 服务接口（新增）
16. `/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/service/impl/AuthServiceImpl.java` - 服务实现（新增）
17. `/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/common/conf/feign/client/QAMateAuthClient.java` - Feign客户端（新增）
18. `/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/common/conf/feign/request/AuthLoginRequest.java` - 统一请求DTO（新增）
19. `/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/common/conf/feign/response/AuthLoginResponse.java` - 响应DTO（新增）
20. `/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/controller/dto/LoginDto.java` - Controller DTO（新增）

---

## 验证计划

### 端到端测试流程
1. **执行建表 SQL**:
   ```bash
   mysql -h 10.138.47.50 -P 8331 -u root -pAsd@123 core
   source /path/to/apismart_auth_credentials.sql
   ```

2. **启动 Core 服务并测试**:
   ```bash
   cd /Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code/baidu/qamate-server/core
   mvn spring-boot:run

   # 测试密码登录
   curl -X POST http://localhost:8080/core/apismart/login \
     -H "Content-Type: application/json" \
     -d '{"username":"testuser","password":"Asd123"}'
   ```

3. **验证数据库存储**:
   ```bash
   mysql -h 10.138.47.50 -P 8331 -u root -pAsd@123 -e \
     "SELECT id, login_name, login_pwd, cookies FROM core.apismart_auth_credentials"
   ```

---

## 总结

### 核心特性
- ✅ **数据库存储**：基于 ITP `tb_login_info` 表设计
- ✅ **密码加密**：兼容 ITP 的 DES-CBC 加密（`encrypt::密文`）
- ✅ **环境隔离**：复合主键（id + is_online）支持线上线下
- ✅ **统一接口**：智能判断登录方式（cookie优先）
- ✅ **自动加解密**：MyBatis TypeHandler 自动处理
- ✅ **复用 ITP 逻辑**：Passport API 调用 80% 复用

### 文件组织
- **Core**: 新增在 `apismartmgt` 包下（13个文件）
- **Executor**: 遵循现有模式（7个文件）

预计 **2-3周** 完成全部开发和测试。
