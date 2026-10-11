---
title: "INSERT SQL 执行\"成功\"但数据未入库问题分析"
description: "日期：2026-02-26 报告人：v梁霄鹏 / yangdeqian Case ID：95828827 环境：itp-tasktracker itptasktracknormal 数据库：scm001.bcc-bdbl.baidu.com"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\insert_sql_not_persisted_analysis.md"
---
# INSERT SQL 执行"成功"但数据未入库问题分析

> **日期**：2026-02-26  
> **报告人**：v_梁霄鹏 / yangdeqian  
> **Case ID**：95828827  
> **环境**：itp-tasktracker (itptasktracknormal)  
> **数据库**：scm001.bcc-bdbl.baidu.com:8999（分片中间件）/ ms_mdm

---

## 一、问题描述

用户在 ITP 平台执行 SQL 操作时发现：

1. **INSERT 语句**报告执行成功（`isPass=true`），但数据库中**没有新增数据**
2. **DELETE 语句**执行后数据库中的数据**确实被删除**
3. 两者走的是完全相同的代码路径（Python 脚本执行写操作）

### 执行的 SQL

```sql
-- INSERT（报成功，但数据未入库）
INSERT INTO ms_mdm.product_introduce_machine_expansion_item(order_id,sn,sn_flow,status,create_time,update_time)
VALUES(102126,'DCRTGZ11','s1',1,'2026-02-10 14:30:47','2026-02-11 18:08:21');

-- DELETE（实际生效）
DELETE FROM `product_introduce_machine_expansion_item` WHERE `id`=10992;
```

### 关键日志

**INSERT 执行日志（16:51:34，v_liangxiaopeng）**：
```
[INFO]Get into executor...
[INFO][Execute By Python sql:]sh .../exe.sh .../pymysql_connect.py
      'scm001.bcc-bdbl.baidu.com' '8999' 'root' 'Volatile_Y123456' 'ms_mdm'
      "INSERT INTO ms_mdm.product_introduce_machine_expansion_item(...) VALUES(...);" '2'
[INFO][Response]: Response{statusCode=200, msg=MsgInfo [title=success, msg=success, stackTrace=null],
      resp='null', isPass=true, verifications={}}
[INFO]Process op id: 95828899, name: Operation successful.
```

系统报告 `isPass=true`、`Operation successful`，但数据实际并未入库。

---

## 二、根因结论

**INSERT 在 Python 脚本层实际执行失败**（分片中间件拒绝或返回异常），但由于**三层错误处理的连环缺陷**，系统将真实的失败**误报为成功**。DELETE 能成功是因为分片中间件对 DELETE 的路由策略不同。

---

## 三、详细错误链路分析

### 第一层缺陷：Python 脚本静默吞掉异常

**文件**：`itp/itp-tasktracker/src/main/resources/script/pymysql_connect.py`，`update()` 函数（第 47-72 行）

```python
def update(host, port, user, password, db, sql):
    cursor = None
    conn = None
    try:
      conn = pymysql.connect(...)
      cursor = conn.cursor()
      cursor.execute(sql)        # ← 分片中间件对 INSERT 返回错误，抛出异常
      data = cursor.rowcount     # ← 不会执行
      conn.commit()              # ← 不会执行！数据未提交！
      data = json.dumps(data)
      print(data, end="")
    except:                      # ← 裸 except 捕获所有异常
      print("execute err")       # ← 仅打印到 stdout，无非零退出码
    finally:
      if cursor is not None:
        cursor.close()
      if conn is not None:
        conn.close()             # ← 未 commit 的事务在 close 时自动 rollback
```

**问题**：
| 缺陷 | 说明 |
|------|------|
| `except` 裸捕获 | 捕获所有异常类型，无法区分网络错误、SQL 语法错误、中间件拒绝等 |
| 无非零退出码 | Python 进程正常退出（exit code = 0），Java 无法通过返回码判断失败 |
| 错误输出到 stdout | `"execute err"` 输出到 stdout 而非 stderr，与正常返回值混在一起 |
| `conn.commit()` 未执行 | 异常发生在 `cursor.execute()` 后，`conn.commit()` 永远不会被调用，数据不会持久化 |

### 第二层缺陷：Java `excuteInsertOrUpdateSql` 无法区分成功与失败

**文件**：`itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/sql/JDBCUtil.java`，第 158-164 行

```java
} else {
    String res = executeByPython(dbconf, sql, configPath, 2);
    // 情况A - INSERT 失败时: res = "execute err"
    // 情况B - INSERT 成功时: res = "1"（json.dumps(rowcount)）
    if (StringUtils.isBlank(res) || !JsonParse.isJSONObject(res)) {
        return 0;   // ← 两种情况都走到这里！都返回 0！不抛异常！
    }
    return Integer.parseInt(res);  // ← 永远不会执行到
}
```

**问题**：

`JsonParse.isJSONObject()` 只判断字符串是否以 `{`/`[` 开头并能被解析为 JSON 对象/数组：

| Python 返回值 | `isBlank` | `isJSONObject` | 结果 |
|--------------|-----------|----------------|------|
| `"execute err"`（失败） | false | false | `return 0`（无异常）|
| `"1"`（成功，1行受影响） | false | false | `return 0`（无异常）|
| `""`（空）| true | — | `return 0`（无异常）|
| `null` | true | — | `return 0`（无异常）|

**成功与失败的返回值完全相同（都是 0），根本无法区分。**

### 第三层缺陷：`invokeRequestAndVerify` 无条件报成功

**文件**：`itest-executor/executor/src/main/java/com/baidu/ecom/itest/api/executor/SqlRequestExecutor.java`，第 57-100 行

```java
try {
    // sql 写操作
    responseString = invokeWSqlRequest(sqlRequest, envConfig) + "";  // 返回 "0"
    // invokeWSqlRequest 返回 0，没有抛出异常
} catch (ItestException e) {
    // ...
    returnResp.setPass(false);   // ← 只有 catch 到异常才会设为 false
    return returnResp;
}

// 到达这里 = 没有异常 = 无条件认为成功
returnResp.setPass(true);   // ← INSERT 实际失败，但这里仍然设为 true！
```

**问题**：写操作完全不检查影响行数，只要不抛异常就认为成功。`Response` 类中 `isPass` 默认值就是 `true`（`Response.java` 第 34 行），进一步掩盖了问题。

---

## 四、完整错误链路图

```
┌─ Python 层 ─────────────────────────────────────────────────────────┐
│                                                                     │
│  cursor.execute(INSERT SQL)                                         │
│       │                                                             │
│       ▼                                                             │
│  分片中间件(8999端口)返回错误 → 抛出异常                                │
│       │                                                             │
│       ▼                                                             │
│  except: print("execute err")    ← 吞掉异常，stdout 输出错误信息      │
│  conn.commit() 未执行            ← 数据未提交                        │
│  conn.close()                    ← 未提交的事务自动 rollback          │
│  进程 exit code = 0              ← Java 认为进程正常退出              │
│                                                                     │
└──────────────────────────────────┬──────────────────────────────────┘
                                   │
                                   ▼
┌─ Java CmdUtils 层 ──────────────────────────────────────────────────┐
│                                                                     │
│  returnCode = 0（正常）                                              │
│  infoMsg = "execute err"（stdout）                                   │
│  返回 Tuple2(0, "execute err")                                      │
│                                                                     │
└──────────────────────────────────┬──────────────────────────────────┘
                                   │
                                   ▼
┌─ Java JDBCUtil 层 ──────────────────────────────────────────────────┐
│                                                                     │
│  res = "execute err"                                                │
│  isBlank("execute err") = false                                     │
│  isJSONObject("execute err") = false                                │
│  → return 0    ← 不抛异常，正常成功时也返回 0                         │
│                                                                     │
└──────────────────────────────────┬──────────────────────────────────┘
                                   │
                                   ▼
┌─ Java SqlRequestExecutor 层 ────────────────────────────────────────┐
│                                                                     │
│  invokeWSqlRequest 返回 0，无异常                                     │
│  → setPass(true)  ← 无条件设为成功                                    │
│  → Response{statusCode=200, isPass=true}                            │
│                                                                     │
│  ★ 最终结果：系统误报 INSERT 成功！                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 五、DELETE 为什么能成功

DELETE 和 INSERT 走完全相同的代码路径（Python `update()` → `excuteInsertOrUpdateSql`），但在**分片中间件层面**行为不同：

| 操作 | 分片中间件行为 | 结果 |
|------|---------------|------|
| **INSERT** | 需要根据分片键确定目标分片写入位置。如果中间件无法从 INSERT SQL 中解析分片键，则**拒绝执行** | `cursor.execute()` 抛异常，`commit()` 未调用，数据未入库 |
| **DELETE** | `WHERE id=10992` 提供了明确条件，中间件可通过 `id` 定位目标分片；或对 DELETE 采用**广播策略**（发送到所有分片） | `cursor.execute()` 成功，`commit()` 被调用，数据被删除 |

---

## 六、补充：首次执行时的 `convertUnShardSQlStr error1` 错误

在最初的一次执行（16:05:49）中，SQL 没有使用 `db.table` 格式：

```sql
INSERT INTO product_introduce_machine_expansion_item(order_id,...) VALUES(...);
```

这导致了额外的错误：

1. `JDBCUtil.getTableNameBySql()` 通过 `.` 分割 SQL，因为没有 `.`，`split` 数组只有 1 个元素
2. 访问 `split[1]` 时抛出 `ArrayIndexOutOfBoundsException`（message 为 `"1"`）
3. `LogUtil.error("convertUnShardSQlStr error", e)` 中 bigpipe 日志使用 `str + e.getMessage()` 拼接
4. 最终日志显示为 `convertUnShardSQlStr error1`（即 `"convertUnShardSQlStr error"` + `"1"`）

此异常被 `convertUnShardSQlStr` 方法的 catch 块吞掉，不影响后续执行流程。

---

## 七、代码缺陷汇总

| # | 严重性 | 文件 | 行号 | 缺陷描述 |
|---|--------|------|------|---------|
| 1 | 🔴 高 | `pymysql_connect.py` | 65-66 | `except` 裸捕获所有异常，不设非零退出码，Java 无法判断失败 |
| 2 | 🔴 高 | `pymysql_connect.py` | 66 | 错误信息 `"execute err"` 输出到 stdout 而非 stderr，与正常输出混淆 |
| 3 | 🔴 高 | `JDBCUtil.java` | 160-161 | Python 返回非 JSON 时直接 `return 0`，不检查是否为错误信息，不抛异常 |
| 4 | 🟡 中 | `JDBCUtil.java` | 160-161 | 正常成功返回 `"1"` 也不是 JSON Object，与错误返回值处理路径完全相同，无法区分 |
| 5 | 🟡 中 | `SqlRequestExecutor.java` | 100 | 写操作不校验影响行数，`return 0` 仍然 `setPass(true)` |
| 6 | 🟡 中 | `JDBCUtil.java` | 256-259 | `getTableNameBySql` 检测到 `split.length < 2` 后没有 return，继续执行导致数组越界 |

---

## 八、修复建议

### 8.1 Python 脚本层（优先级最高）

```python
# pymysql_connect.py - update() 函数修复建议
def update(host, port, user, password, db, sql):
    cursor = None
    conn = None
    try:
      conn = pymysql.connect(...)
      cursor = conn.cursor()
      cursor.execute(sql)
      data = cursor.rowcount
      conn.commit()
      data = json.dumps(data)
      print(data, end="")
    except Exception as e:
      # 1. 输出到 stderr 而非 stdout
      print("execute err: " + str(e), file=sys.stderr)
      # 2. 设置非零退出码
      sys.exit(1)
    finally:
      if cursor is not None:
        cursor.close()
      if conn is not None:
        conn.close()
```

### 8.2 Java JDBCUtil 层

```java
// JDBCUtil.java - excuteInsertOrUpdateSql 修复建议
String res = executeByPython(dbconf, sql, configPath, 2);
if (StringUtils.isBlank(res) || "execute err".equals(res.trim())) {
    throw new ItestException(StatusCode.SQL_WRITE_EXE,
        "[DB Write Exception via Python]: " + sql + ", result: " + res, "Python SQL执行失败");
}
// 尝试解析为数字（影响行数）
try {
    return Integer.parseInt(res.trim());
} catch (NumberFormatException e) {
    throw new ItestException(StatusCode.SQL_WRITE_EXE,
        "[DB Write Exception via Python]: unexpected result: " + res, e);
}
```

### 8.3 SqlRequestExecutor 层

```java
// SqlRequestExecutor.java - invokeRequestAndVerify 中写操作结果校验
if (null != sqlRequest.getSqlRequestType()
        && sqlRequest.getSqlRequestType().equals(SqlRequestType.sql_write)) {
    int affectedRows = invokeWSqlRequest(sqlRequest, envConfig);
    responseString = affectedRows + "";
    // 可选：校验影响行数
    if (affectedRows <= 0) {
        LogUtil.warn("SQL write operation affected 0 rows: " + sqlRequest.getSql());
    }
}
```

