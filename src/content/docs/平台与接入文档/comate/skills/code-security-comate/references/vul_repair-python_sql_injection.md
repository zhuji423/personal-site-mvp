---
title: "python sqli 漏洞修复最佳实践"
description: "python sqli 漏洞修复知识"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\code-security-comate\\references\\vul_repair-python_sql_injection.md"
---
python sqli 漏洞修复知识

# python sqli 漏洞修复最佳实践
采用先分析漏洞报告->分析数据传递链路->判断是否存在依赖->分析修复方式（判断是否可以修复、使用哪种修复方式）->修复漏洞->验证修复代码可编译且逻辑正确

注意：**不要做与漏洞修复无关的代码改动**。

---

## I. 漏洞分析
### 1. 不可修复场景
1. SQL 语句由外部包/外部服务直接生成并传入，当前代码无法拆解 SQL 结构。
2. 污点以完整子句（如完整 `WHERE` / `ORDER` / `JOIN` 逻辑）注入，且无法安全结构化拆分。
3. 无法确认修复位置是否在真实数据流 sink 路径上（此时应先回到数据流定位，不盲改）。

### 2. 可修复场景
#### 修复方式选择
1. 污点变量作为「值」（如 `WHERE id = {id}`）→ 使用预编译（占位符 + params 参数）。
2. 污点变量作为「结构」（如 `ORDER BY` / 表名 / 列名）→ 定义过滤函数 safeFilter，使用正则过滤。
3. `IN` 子句参数 → 按元素数量展开占位符（如 `%s,%s,%s`），不允许单占位符绑定数组。
4. DDL/DCL 语句（`CREATE` / `DROP` / `SHOW` / `GRANT`）→ 不支持预编译，必须使用正则过滤。
5. 同一参数只采用一种修复方式，不要叠加"过滤 + 预编译 + 转义"。

#### 修复位置选择
6. Sink 是通用封装函数（如 `execute_sql`、`db.query`）→ 改造该函数支持参数化。
7. Sink 是业务代码直接调用底层 API → 在当前位置直接修复。
8. 若 SQL 在多个函数复用，需一并分析其他调用点，避免只修一处。
9. 同一污点变量流向多个 SQL → 每个 SQL 都要修复。

#### 修复规范
10. 仅在当前数据流相关文件内修复，不创建新的代码文件。
11. 同文件已有过滤函数/正则时优先复用。
12. 需要改函数签名时，要保证现有调用方兼容（加默认参数或同步改调用方）。
13. 修复前先确认当前 DB API 的占位符风格（`%s` / `?` / `:name`），禁止猜测。
14. 禁止直接对完整 SQL 做"整体过滤"，应对拼接进 SQL 的污点参数做防护。
15. 修复后必须重新扫描验证，确认漏洞数归零。

#### 参数类型速查表
|场景|推荐策略|原因|
|-|-|-|
|SQL 标识符（表名/列名/数据库名/索引名）|正则 + 白名单|格式验证 + 值验证，双重保障|
|SELECT 列表|正则 + 白名单|允许通配符 `*` 和多列，列名需白名单验证|
|ORDER BY/GROUP BY|正则 + 白名单|格式验证 + 列名白名单 + 方向关键字（ASC/DESC）|
|LIMIT/OFFSET|严格正则|只允许数字，不需要白名单|
|WHERE 条件|**参数化查询**|正则过滤仍有风险，参数化最安全|
|IN 子句|参数化查询优先|优先参数化，其次严格正则|
|DDL/DCL（CREATE/DROP/SHOW）|正则过滤|不支持预编译|

---

## II. 过滤方式规则（safeFilter / safeValidate）
### 1. 命名规范
* 过滤函数命名建议以 `safeFilter` 或 `safeValidate` 开头。
* 便于规则引擎识别清洗点（仓库已存在对应 sanitizer 规则）。

### 2. 使用规范
1. 过滤结果必须由临时变量承接，后续拼接 SQL 只能使用过滤后的变量。
2. 禁止"先赋值污点变量，再覆盖为安全值"的写法。
3. 非法输入必须抛错/返回错误，不能静默放行。
4. 对对象参数，建议返回安全对象后再向下传递。

具体过滤函数实现见第 IV.4 节。

---

## III. Python 常见修复方案
### 1. DB-API 参数化查询（优先）
```python
# Bad
sql = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(sql)

# Fix（MySQL/PostgreSQL/多数驱动）
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))

# Fix（sqlite3 常见写法）
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```
### 2. IN 子句参数化
```python
ids = request.GET.getlist("ids")
if not ids:
    return []

placeholders = ",".join(["%s"] * len(ids))
sql = f"SELECT * FROM users WHERE id IN ({placeholders})"
cursor.execute(sql, tuple(ids))
rows = cursor.fetchall()
```
### 3. 结构化片段过滤（表名/列名/排序）
结构化 SQL 片段（表名、列名、ORDER BY 等）不支持参数化，必须使用正则过滤。具体实现见第 IV.4 节。

### 4. Django 原生 SQL 场景
```python
from django.db import connection

username = request.GET.get("username")
with connection.cursor() as cursor:
    # Bad: f-string 拼接
    # cursor.execute(f"SELECT * FROM auth_user WHERE username = '{username}'")

    # Fix: 参数化
    cursor.execute("SELECT * FROM auth_user WHERE username = %s", [username])
```
### 5. SQLAlchemy 场景
```python
from sqlalchemy import text

# Bad
# session.execute(text(f"SELECT * FROM users WHERE name = '{name}'"))

# Fix
session.execute(text("SELECT * FROM users WHERE name = :name"), {"name": name})
```
### 6. pandas `read_sql` 场景
```python
import pandas as pd

# Bad
# sql = f"SELECT * FROM users WHERE name = '{user_input}'"
# df = pd.read_sql(sql, conn)

# Fix
sql = "SELECT * FROM users WHERE name = ?"
df = pd.read_sql(sql, conn, params=[user_input])
```
### 7. 公共 DB 封装优先改造（批量修复首选）
适用条件：同一项目存在多个 `cursor.execute(sql)` sink，且调用方式高度相似。

执行步骤：

1. 先改公共数据库封装方法签名，统一支持参数化（如 `query(sql, params=None)` / `execute(sql, params=None)`）。
2. 在封装内部统一走参数化执行（有 `params` 时 `cursor.execute(sql, params)`）。
3. 批量替换调用点：将 f-string / `%` / `.format()` 拼接改为占位符 + `params`。
4. `IN` 子句按元素数量展开占位符，不允许列表绑定到单占位符。
5. 保持最小改动：不改业务语义、不改返回结构、不改事务边界。

```python
def query(self, sql: str, params=None):
    with self.conn.cursor() as cursor:
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        return cursor.fetchall()
```
```python
# Bad
sql = f"SELECT * FROM users WHERE id = '{user_id}'"
rows = db.query(sql)

# Fix
sql = "SELECT * FROM users WHERE id = %s"
rows = db.query(sql, (user_id,))
```
---

## IV. 正则过滤规范与白名单策略
> 本节用于指导修复 SQL 注入漏洞时，如何选择白名单或正则过滤，确保**最小化改动范围**。
### 1. 核心决策树
```
用户输入需要过滤？
│
├─ 是 SQL 标识符（表名/列名/数据库名/索引名）？
│   └─ → 正则验证格式 + 白名单验证（双重保障）
│
├─ 是 SELECT 列表？
│   └─ → 正则验证格式 + 提取列名后白名单验证
│
├─ 是 WHERE 条件/IN 子句？
│   └─ → 使用参数化查询（强烈推荐）
│
├─ 是 ORDER BY/GROUP BY？
│   └─ → 正则验证格式 + 提取列名后白名单验证
│
├─ 是 LIMIT/OFFSET？
│   └─ → 正则验证纯数字
│
└─ 其他场景
    └─ → 根据具体需求选择白名单或精确正则
```
### 2. 白名单数据来源与处理策略
#### 白名单数据从哪里来？
|来源|说明|示例|
|-|-|-|
|**数据库元数据查询**|从数据库系统表查询实际存在的表/列名|`SELECT column_name FROM information_schema.columns WHERE table_name = 'users'`|
|**代码静态分析**|扫描代码中定义的实体类、ORM 模型|JPA `@Entity`、MyBatis mapper、SQLAlchemy Model|
|**配置文件/注解**|从配置文件或注解中提取允许的字段列表|`@AllowedFields({"id", "name", "email"})`|
|**API 文档/接口定义**|从 Swagger/OpenAPI 等文档中提取字段定义||

#### 白名单不完整时的处理策略
```
白名单验证失败？
│
├─ 白名单数据来源明确（如元数据查询、ORM 模型）？
│   └─ → 拒绝输入，记录日志，提示用户
│
├─ 白名单数据来源不明确（如硬编码、不完整）？
│   └─ → 降级为仅正则验证，记录警告日志
│
└─ 无法获取白名单（如动态表名）？
    └─ → 仅正则验证格式，加强输入长度限制
```
**修复决策原则**：

1. **优先获取白名单**：如果代码中有 ORM 模型或实体类定义，优先从中提取字段列表
2. **正则兜底**：当白名单获取困难或不完整时，使用严格正则作为安全底线
3. **记录决策原因**：在代码注释中说明为什么选择正则而非白名单

### 3. 不同数据库的差异说明
|数据库|标识符引用符|参数占位符|特殊注意事项|
|-|-|-|-|
|**MySQL**|反引号 ```|`?` 或 `:name`|支持反引号包裹标识符，如 ``user_name``|
|**PostgreSQL**|双引号 `"`|`$1, $2, ...` 或 `?`|支持双引号包裹标识符，如 `"user_name"`|
|**SQL Server**|方括号 `[` `]`|`@param` 或 `?`|支持方括号包裹标识符，如 `[user_name]`|
|**Oracle**|双引号 `"`|`:name` 或 `?`|标识符默认大写，双引号区分大小写|
|**SQLite**|双引号 `"` 或方括号 `[` `]`|`?` 或 `:name`|兼容多种引用符|

**修复原则**：根据当前使用的数据库类型，选择对应的引用符和参数占位符。

### 4. 各场景正则与实现
#### 5.1 SELECT 列名列表 `__SELECT_FILTER__`
**适用场景**：SELECT 后面的列名列表（如 `SELECT id,name,email FROM users` 或 `SELECT users.id,users.name FROM users`）

**正则（通用版，支持引用符）**：

```
^\*|((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+))*$
```
**支持格式**：

* `*` （通配符）
* `id` （单列）
* `users.id` （表名.列名）
* ``user_name`` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `id,name,email` （多列，逗号分隔）
* `users.id, users.name, users.email` （带表名前缀的多列）
* `id, name, email` （允许逗号前后空格）

**Python 修复示例**：

```python
import re

SELECT_PATTERN = r'^\*|((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+))*$'
ALLOWED_COLUMNS = {"id", "name", "email", "created_at"}  # 白名单，可选

def safeFilterSelect(select: str) -> str:
    select = select.strip()
    if not re.fullmatch(SELECT_PATTERN, select):
        raise ValueError("invalid select")
    if select == "*":
        return select
    # 提取列名并验证白名单（可选）
    if ALLOWED_COLUMNS:
        for part in select.split(","):
            clean = part.strip().strip('`"')
            col = clean.split(".")[-1] if "." in clean else clean
            if col.lower() not in ALLOWED_COLUMNS:
                raise ValueError(f"column {col} not allowed")
    return select
```
#### 5.2 SQL 标识符（表名/列名/数据库名/索引名）`__IDENTIFIER_FILTER__`
**适用场景**：表名、列名、数据库名、索引名、视图名等 SQL 标识符

**正则（通用版，支持引用符）**：

```
^[A-Za-z_][A-Za-z0-9_]{0,127}$|^`[^`]{1,128}`$|^"[^"]{1,128}"$
```
**支持格式**：

* `user` （小写字母开头）
* `User123` （字母数字）
* `user_name` （下划线）
* `_private` （下划线开头，部分数据库支持）
* ``user_name`` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `[user_name]` （SQL Server 方括号）
* 长度限制：1-128 字符

**Python 修复示例**：

```python
import re

IDENTIFIER_PATTERN = r'^[A-Za-z_][A-Za-z0-9_]{0,127}$|^`[^`]{1,128}`$|^"[^"]{1,128}"$|^\[[^\]]{1,128}\]$'
ALLOWED_TABLES = {"users", "orders", "products"}  # 白名单，可选

def safeFilterIdentifier(identifier: str) -> str:
    identifier = identifier.strip()
    if not re.fullmatch(IDENTIFIER_PATTERN, identifier):
        raise ValueError("invalid identifier")
    # 去除引用符后验证白名单（可选）
    clean = re.sub(r'^[`"\[]|[`"\]]$', '', identifier)
    if ALLOWED_TABLES and clean.lower() not in ALLOWED_TABLES:
        raise ValueError(f"identifier {clean} not allowed")
    return identifier
```
#### 5.3 ORDER BY `__ORDER_FILTER__`
**适用场景**：ORDER BY 后的字段（如 `ORDER BY name ASC, id DESC` 或 `ORDER BY users.name ASC, users.id DESC`）

**正则（通用版，支持引用符）**：

```
^((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?)*$
```
**支持格式**：

* `name` （单列）
* `users.name` （表名.列名）
* ``user_name`` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `name ASC` / `name DESC` （带方向）
* `users.name ASC` / `users.name DESC` （带表名前缀和方向）
* `name ASC, id DESC` （多列）

**Python 修复示例**：

```python
import re

ORDER_PATTERN = r'^((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?)*$'

def safeFilterOrderBy(order: str) -> str:
    order = order.strip()
    if not re.fullmatch(ORDER_PATTERN, order, re.IGNORECASE):
        raise ValueError("invalid order by")
    return order
```
#### 5.4 GROUP BY `__GROUP_FILTER__`
**适用场景**：GROUP BY 后的字段（如 `GROUP BY name, age` 或 `GROUP BY users.name, users.age`）

**正则（通用版，支持引用符）**：

```
^((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+))*$
```
**支持格式**：

* `name` （单列）
* `users.name` （表名.列名）
* ``user_name`` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `name, age` （多列）
* `users.name, users.age` （带表名前缀的多列）

#### 5.5 LIMIT/OFFSET `__LIMIT_FILTER__`
**适用场景**：LIMIT、OFFSET 后的数值（如 `LIMIT 10`、`LIMIT 1,10`）

**正则**：`^\d+\s*,\s*\d+$|^\d+$`

**支持格式**：

* `10` （单数字）
* `1,10` （带偏移量）
* `1, 10` （允许逗号前后空格）

**Python 修复示例**：

```python
import re

def safeFilterLimit(limit: str) -> str:
    limit = limit.strip()
    if not re.fullmatch(r'^\d+\s*,\s*\d+$|^\d+$', limit):
        raise ValueError("invalid limit")
    return limit
```
#### 5.6 WHERE 条件 `__WHERE_FILTER__`
**适用场景**：WHERE 子句、条件判断

**策略**：**放弃正则，使用参数化查询**

```python
# ❌ 错误：字符串拼接
sql = f"SELECT * FROM users WHERE name = '{name}'"

# ✅ 正确：参数化查询
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
```
#### 5.7 IN 子句 `__IN_FILTER__`
**适用场景**：IN 后面的值列表（如 `IN (1,2,3)`）

**策略**：优先参数化查询，其次严格正则

**正则**：

* 数字：`^\(\s*\d+(\s*,\s*\d+)*\s*\)$`
* 字符串：`^\(\s*'[^']*'(\s*,\s*'[^']*')*\s*\)$`

**支持格式**：

* `(1,2,3)` （数字列表）
* `('a','b','c')` （字符串列表）
* `(1, 2, 3)` （允许逗号前后空格）

```python
# ✅ 优先：参数化查询
ids = [1, 2, 3]
placeholders = ",".join(["%s"] * len(ids))
cursor.execute(f"SELECT * FROM users WHERE id IN ({placeholders})", tuple(ids))

# ⚠️ 备选：严格正则验证（仅当无法参数化时）
import re
if not re.fullmatch(r'^\(\s*\d+(\s*,\s*\d+)*\s*\)$', in_clause):
    raise ValueError("invalid IN clause")
```
#### 5.8 方向关键字 `__DIRECTION_FILTER__`
**适用场景**：ORDER BY 后的 ASC/DESC

**正则**：`^(asc|desc)$`

**支持格式**：

* `ASC` / `DESC` / `asc` / `desc` （不区分大小写）

```python
import re

def safeFilterDirection(direction: str) -> str:
    if not re.fullmatch(r'^(asc|desc)$', direction, re.IGNORECASE):
        raise ValueError("invalid direction")
    return direction
```
#### 5.9 纯字母数字标识符 `__W_FILTER__`
**适用场景**：简单的表名、列名（无特殊字符）

**正则**：`^[\w-]+$`

**支持格式**：

* `user_name` （下划线）
* `User123` （字母数字）
* `table-1` （连字符）

#### 5.10 路径过滤 `__PATH_FILTER__`
**适用场景**：文件路径、URL 路径

**正则**：`^[\w/-]+$`

**支持格式**：

* `/path/to/file` （绝对路径）
* `path/to/file` （相对路径）

#### 5.11 运算符 `__OP_FILTER__`
**适用场景**：算术运算符（如 `score+1`）

**正则**：`[+\-*/%]`

**支持格式**：

* `+` `-` `*` `/` `%` （基本算术运算符）

### 5. 正则速查表
|过滤器|正则|说明|
|-|-|-|
|`__IDENTIFIER_FILTER__`|`^[A-Za-z_][A-Za-z0-9_]{0,127}$|^`[^`]{1,128}`$\|^"[^"]{1,128}"$`|SQL 标识符，支持反引号/双引号，1-128字符|
|`__SELECT_FILTER__`|`^\*|((`[^`]+`|"[^"]+"|\w+.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+.\w+|\w+))*$`|允许通配符 `*` 和逗号分隔的列名，支持引用符和 `表名.列名`|
|`__ORDER_FILTER__`|`^((`[^`]+`|"[^"]+"|\w+.\w+|\w+)(\s+(ASC|DESC))?(,\s*(`[^`]+`|"[^"]+"|\w+.\w+|\w+)(\s+(ASC|DESC))?)*$`|列名 + 方向关键字，支持引用符和 `表名.列名`|
|`__GROUP_FILTER__`|`^((`[^`]+`|"[^"]+"|\w+.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+.\w+|\w+))*$`|多列，逗号分隔，支持引用符和 `表名.列名`|
|`__LIMIT_FILTER__`|`^\d+\s*,\s*\d+$|^\d+$`|纯数字，允许逗号|
|`__WHERE_FILTER__`|**参数化查询**|不要用正则|
|`__IN_FILTER__`|`^\(\s*\d+(\s*,\s*\d+)*\s*\)$` 或字符串版本|数字或字符串列表|
|`__DIRECTION_FILTER__`|`^(asc|desc)$`|ASC 或 DESC|
|`__W_FILTER__`|`^[\w-]+$`|字母数字+下划线+连字符（通用场景）|
|`__PATH_FILTER__`|`^[\w/-]+$`|路径字符|
|`__OP_FILTER__`|`[+\-*/%]`|算术运算符|

### 6. 正则过滤重要提示
1. **所有正则验证前，务必先 **`trim()`** 去除首尾空白字符**
2. **白名单优先**：列名/表名等固定值优先用白名单
3. **白名单不完整时降级**：当白名单获取困难或不完整时，使用严格正则作为安全底线
4. **参数化优先**：WHERE 条件、IN 子句优先用参数化查询
5. **数据库适配**：根据使用的数据库类型选择对应的引用符和参数占位符
6. **最小化改动**：只修复漏洞点，不重构其他代码

---

## V. 修复后检查点（强检查清单）
1. 参数值是否全部走参数化，是否遗留字符串拼接。
2. 结构化 SQL 片段是否全部走过滤。
3. `IN` 子句占位符数量是否与参数数量一致。
4. 空数组场景是否有兜底（避免 `IN ()` 语法错误）。
5. 是否混用了不兼容的占位符风格（`%s` / `?` / `:name`）。
6. 是否修复了真实 sink 所在函数/文件（不是"改错位置"）。
7. 改动函数签名后，调用方是否同步兼容。
8. 是否出现"新旧 SQL 并存"导致旧拼接逻辑覆盖新逻辑。
9. 是否存在变量作用域问题（分支变量未定义）。
10. 修复代码是否保持原业务语义（避免把 `UPDATE/DELETE` 改成 `SELECT`）。
11. 过滤正则是否兼容所有合法业务数据格式（如日期含 `-`、路径含 `/` 等），避免正则过严导致合法请求被拒。
12. 公共 DB 封装是否已支持 `params` 且被调用点实际使用（不是只改签名）。
13. 真实 sink（`cursor.execute`）是否仍存在外部可控字符串拼接路径。
14. 是否完成同文件/同模块同类拼接点批量替换，而非只修单个样例点。

---

## VI. 高频失败反模式（修复时必须规避）
### 反模式 1：仍使用字符串拼接 SQL
```python
# ❌ 错误：用 f-string / % / format 拼接
sql = f"SELECT * FROM users WHERE id = {user_id}"
sql = "SELECT * FROM users WHERE id = %s" % user_id
sql = "SELECT * FROM users WHERE id = {}".format(user_id)

# ✅ 正确：参数化查询
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```
### 反模式 2：IN 子句直接绑定列表
```python
# ❌ 错误：单占位符绑定列表
ids = [1, 2, 3]
cursor.execute("SELECT * FROM users WHERE id IN (%s)", (ids,))

# ✅ 正确：展开占位符
ids = [1, 2, 3]
placeholders = ",".join(["%s"] * len(ids))
cursor.execute(f"SELECT * FROM users WHERE id IN ({placeholders})", tuple(ids))
```
### 反模式 3：修复一个分支，遗漏其他分支
```python
# ❌ 错误：只修了 if 分支，else 分支遗漏
if action == "select":
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))  # 已修复
else:
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")  # 遗漏！

# ✅ 正确：所有分支都修复
if action == "select":
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
else:
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
```
### 反模式 4：只改调用层，未改 Sink 层通用函数
```python
# ❌ 错误：在调用层加校验，但 insert_helper 仍用拼接
def insert_helper(table, data):
    sql = f"INSERT INTO {table} ..."  # Sink 层仍是拼接！
    cursor.execute(sql)

def add_user(name):
    if not re.match(r'^\w+$', name):  # 调用层校验
        raise ValueError("invalid")
    insert_helper("users", {"name": name})  # 无效，sink 层未改

# ✅ 正确：改造 Sink 层支持参数化
def insert_helper(table, data, params=None):
    # ... 使用 cursor.execute(sql, params)
```
### 反模式 5：新增参数化方法但调用方仍用旧方法
```python
# ❌ 错误：新增了 query_param 但调用方还用旧的 query
class DB:
    def query(self, sql):  # 旧方法，拼接
        cursor.execute(sql)
    
    def query_param(self, sql, params):  # 新方法，参数化
        cursor.execute(sql, params)

# 调用方仍使用旧方法
db.query(f"SELECT * FROM users WHERE id = {user_id}")  # 错误！

# ✅ 正确：调用方也要改用新方法
db.query_param("SELECT * FROM users WHERE id = %s", (user_id,))
```
### 反模式 6：先使用污点变量，后补过滤（数据流已放行）
```python
# ❌ 错误：先用了 user_id，后面才过滤
sql = f"SELECT * FROM users WHERE id = {user_id}"  # 污点已进入 SQL！
safe_id = safeFilter(user_id)  # 过滤太晚，无效

# ✅ 正确：先过滤，再使用
safe_id = safeFilter(user_id)  # 先过滤
sql = f"SELECT * FROM users WHERE id = {safe_id}"  # 用过滤后的变量
```
### 其他反模式（简述）
7. 只加引号不做参数化/过滤（引号可被闭合绕过）
8. 修复一个 sink，遗漏同参数的其他 sink
9. 改造了 `query` 方法，遗漏了 `update`/`insert`/`execute` 方法
10. 修复后未重新扫描验证漏洞是否消除
11. 过滤正则过严拒绝合法输入（如日期 `2024-03-15` 含 `-`，但正则不含 `-`）
12. 调用不存在的 DB API 或错误假设驱动能力
13. 仅做黑名单/前缀校验/`strip()`，未落实参数化或结构化白名单

---

## VII. 最小修复策略（执行建议）
1. 先定位真实数据流 sink，并确认是否可优先下沉到公共 DB 封装层修复。
2. 值参数优先参数化；结构化片段用正则过滤。
3. 若存在多处同类 sink，先改 `query/execute` 封装签名支持 `params`，再批量替换调用点。
4. 使用 `safeFilter/safeValidate` + 临时变量承接，禁止先用污点后补过滤。
5. 完成后按 V 节 14 条逐项自检，再提交。

---