---
title: "PHP SQL 注入漏洞修复最佳实践"
description: "php sqli 漏洞修复知识"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\code-security-comate\\references\\vul_repair-php_sql_injection.md"
---
php sqli 漏洞修复知识

# PHP SQL 注入漏洞修复最佳实践
采用先分析漏洞报告 -> 分析数据传递链路 -> 判断依赖与副作用 -> 选择修复方式 -> 修复 -> 校验的流程。

注意：**不要做与漏洞修复无关的代码改动**。

---

## I. 核心修复分析逻辑
在开始修改代码前，仅需确认以下四点：

1. **分析修复方式**

    * **值绑定**：数据值（如 `id=1`, `name='test'`）-> 必须预编译/参数绑定。
    * **结构定义**：表名、列名、排序方向等结构化 SQL 片段 -> 必须过滤。

2. **分析数据链路**

    * 确认变量从哪里进入、在哪个 sink 执行。
    * 检查是否跨函数、跨文件、跨层（Controller -> Service -> DAO）。

3. **依赖与副作用**

    * 修改函数签名后，调用方是否需要同步。
    * 同一 SQL 在其他位置是否复用，修复是否会影响其他逻辑。

4. **框架能力确认（修复前必做）**

    * 确认当前 DB/DAO 是否支持：`prepare`、`query($sql, $params)`、`execute($sql, $params)`。
    * **禁止猜测 API**：若代码库中不存在该方法，不可直接使用。
    * 修复前先查当前类同文件/同包已有调用方式，优先复用项目内已验证的安全写法。

---

## II. Yii (Yii2) 框架修复方案
Yii 提供了较完善的防注入机制，核心原则：**优先使用数组语法（Hash Format）代替字符串拼接**。

### 1. ActiveRecord / Query Builder（推荐）
Yii 的 `ActiveRecord` 和 `Query` 在数组条件场景会自动进行参数绑定。

**场景 A：普通条件查询**

```php
// Bad
$user = User::find()->where("name = '" . $name . "'")->one();

// Fix
$user = User::find()->where(['name' => $name])->one();

// 复杂条件
$users = User::find()->where(['>', 'age', $age])->all();
```
**场景 B：IN 查询**

```php
// Bad
$ids = $_GET['ids'];
$users = User::find()->where("id IN ($ids)")->all();

// Fix
$ids = explode(',', $_GET['ids']);
$users = User::find()->where(['id' => $ids])->all();
```
### 2. DAO / 原生 SQL（createCommand）
```php
// Bad
$sql = "SELECT * FROM post WHERE id=" . $id;
$posts = Yii::$app->db->createCommand($sql)->queryAll();

// Fix
$sql = "SELECT * FROM post WHERE id=:id";
$posts = Yii::$app->db->createCommand($sql)
    ->bindValue(':id', $id)
    ->queryAll();
```
### 3. `findBySql` 修复
```php
// Bad
$sql = "SELECT * FROM user WHERE status=" . $status;
$users = User::findBySql($sql)->all();

// Fix
$sql = "SELECT * FROM user WHERE status=:status";
$users = User::findBySql($sql, [':status' => $status])->all();
```
### 4. 无法预编译场景（Order By / Table Name）
```php
$sort = $_GET['sort'];
$regex = '/^[\w\s\[\]`\$.,*]+$/';

if (!preg_match($regex, $sort)) {
    throw new \yii\web\BadRequestHttpException("Invalid sort parameter");
}

$users = User::find()->orderBy($sort)->all();
```
### 5. Yii 常见错误（必须规避）
1. `execute()`** 返回值误用**：Yii2 `execute()` 返回影响行数（int），不能继续 `->queryAll()`。
2. **提前创建 Command**：必须先拼完 SQL，再 `createCommand($sql)`。
3. **Yii1 **`criteria->params`** 覆盖**：`$criteria->params = [...]` 会覆盖已设置参数，需合并而非覆盖。
4. **Yii1 命名参数与位置参数混用**：Yii 1.x 的 `bindValues` 根据 `isset($values[0])` 判断参数模式，混用会导致绑定失败。

### 6. Yii1 vs Yii2 差异
|差异点|Yii 1.x|Yii 2.x|
|-|-|-|
|参数绑定判断|`isset($values[0])` 判断模式|支持混合模式|
|`criteria->params`|覆盖式赋值需注意|`addParams()` 可用|
|`execute()` 返回|影响行数|影响行数|

**Yii1 混用错误示例**：

```php
// 错误：命名参数 :uid 与位置参数数组混用
$params = array_merge([':uid' => $uid], $requestIdList);  // $requestIdList 是 0-indexed
$model->findAllBySql($sql, $params);
// bindValues 检测到 isset($params[0]) 为 true，进入位置模式，忽略 :uid

// 正确：全部使用命名参数
$params = [':uid' => $uid];
foreach ($requestIdList as $i => $id) {
    $params[":id$i"] = $id;
}
```
---

## III. ODP 框架修复方案
适用于 `Bd_Db_ConnMgr` 等 DB 封装。

### 1. SQL 模板方式（推荐）
```php
$template = "SELECT * FROM users WHERE id={id:n} AND name={name:s}";
$sqlTemplate = new Bd_Db_SQLTemplate($db);
$sqlTemplate->prepare($template);
$sqlTemplate->bindParam('id', $userId);
$sqlTemplate->bindParam('name', $userName);
$sql = $sqlTemplate->getSQL();
```
### 2. SQL 组合器方式
```php
// 安全
$result = $db->select(
    'users',
    ['id', 'name', 'email'],
    ['id' => $userId, 'status' => 1]
);

// 危险
$result = $db->select('users', '*', "id = $userId AND name = '$userName'");
```
### 3. 预处理语句方式（以项目实际 API 为准）
```php
$stmt = $db->prepare("SELECT * FROM users WHERE id = ? AND name = ?");
$stmt->bindParam('is', $userId, $userName);
$result = $stmt->execute();
```
### 4. 使用前先确认 API 存在
* 仅在代码库确认存在 `Bd_Db_SQLTemplate` / `queryf` / `prepare` 等 API 时才可使用。
* 若当前项目 DB 类仅支持 `query($sql)`，不可硬改成不存在的方法。

---

## III.1 safeFilter / safeValidate 过滤函数规范
### 1. 命名与目标
* 过滤函数命名必须以 `safeFilter` 或 `safeValidate` 开头。
* 目的：

    1. 统一修复风格；
    2. 便于规则引擎识别清洗点（已存在对应 sanitizer 规则）。

### 2. 使用规则
1. **必须使用临时变量承接过滤结果**，后续 SQL 只能使用安全变量。
2. 禁止"过滤后继续使用原变量"。
3. 非法输入必须返回错误/中断，不允许静默放行。
4. 对对象参数，优先提供"对象级过滤函数"，返回安全对象后再下传。
5. **定义过滤函数后必须在 sink 前调用**，禁止只定义不调用。

```php
// 错误：定义了但未调用
function safeFilterTablePrefix($input) { ... }
$sql = "SELECT * FROM {$tableprefix}_data";  // 仍直接使用污点变量

// 正确：定义并调用
$safePrefix = safeFilterTablePrefix($tableprefix);
$sql = "SELECT * FROM {$safePrefix}_data";
```
### 3. 示例（标量）
```php
function safeFilterOrderBy($input) {
    $regex = '/^[\w\s\[\]"`\$.,*]+$/';
    if (!is_string($input) || !preg_match($regex, $input)) {
        throw new InvalidArgumentException('Invalid order by');
    }
    return $input;
}

$safeOrderBy = safeFilterOrderBy($orderBy);
$sql = "SELECT * FROM t ORDER BY {$safeOrderBy}";
```
### 4. 示例（对象）
```php
function safeValidateQuery($query) {
    $regex = '/^[\w\s\[\]"`\$.,*]+$/';
    if (isset($query['sort']) && !preg_match($regex, $query['sort'])) {
        throw new InvalidArgumentException('Invalid sort');
    }
    return $query;
}

$safeQuery = safeValidateQuery($query);
$sort = $safeQuery['sort'] ?? 'id DESC';
```
---

## IV. 原生 PHP / PDO 修复方案（通用）
### 1. 预编译修复（跨函数/数据流）
当 SQL 在一个函数构建、另一个函数执行时，可通过默认参数兼容改造。

```php
// Bad
function getInfo($id) {
    $sql = "SELECT * FROM news WHERE id = $id";
    return fetchAll($sql);
}

function fetchAll($sql) {
    global $conn;
    return $conn->query($sql);
}

// Fix
function getInfo($id) {
    $sql = "SELECT * FROM news WHERE id = ?";
    return fetchAll($sql, [$id]);
}

function fetchAll($sql, $params = []) {
    global $conn;
    $stmt = $conn->prepare($sql);
    $stmt->execute($params);
    return $stmt->fetchAll();
}
```
### 2. IN 子句修复（原生 PDO）
```php
$ids = explode(',', $inputIds);
if (empty($ids)) {
    return [];
}

$inQuery = implode(',', array_fill(0, count($ids), '?'));
$sql = "SELECT * FROM table WHERE id IN ($inQuery)";
$stmt = $pdo->prepare($sql);
$stmt->execute($ids);
$rows = $stmt->fetchAll();
```
### 3. IN 子句强约束（必须满足）
1. 禁止 `IN (:ids)` 直接绑定数组。
2. 占位符数量必须与参数数量一致。
3. 空数组必须有兜底逻辑（返回空结果或显式中断）。
4. 禁止出现参数翻倍、错位绑定。

### 4. PDO 常见错误（必须规避）
1. `execute()` 返回 bool，不能当 Statement 使用。
2. `prepare + bindValue` 后必须 `execute()` 再 `fetch/fetchAll`。
3. 禁止同一 SQL 中混用 `?` 与 `:name`。
4. **PDO 位置参数 0-based 键问题**：`array_merge` 产生 0-based 索引数组，PDO `?` 占位符期望连续数组。

```php
// 错误：array_merge 产生 0-based 索引数组
$params = array_merge($arr1, $arr2);  // [0 => 'a', 1 => 'b', ...]

// 正确：使用 array_values 确保连续数组
$params = array_values(array_merge($arr1, $arr2));
$stmt->execute($params);
```
### 5. mysqli 修复方案
`mysqli_stmt::execute()` 返回 `bool`，不能直接调用 `fetch_array()`。

```php
// 错误
$stmt = $mysqli->prepare($sql);
$stmt->bind_param('s', $param);
$result = $stmt->execute();  // $result 是 bool
$row = $result->fetch_array();  // Fatal Error

// 正确
$stmt = $mysqli->prepare($sql);
$stmt->bind_param('s', $param);
$stmt->execute();
$result = $stmt->get_result();  // 获取 mysqli_result
$row = $result->fetch_array();
```
---

## V. 必须使用正则过滤的场景
以下场景不支持预编译，必须使用正则过滤：

1. 动态表名/库名：`FROM $tableName`
2. 动态列名：`SELECT $columnName`
3. Order By：`ORDER BY $field $direction`
4. DDL/DCL：`CREATE`, `DROP`, `GRANT`, `SHOW`

**代码复用提示**

* 若文件头/类常量已定义类似正则（如 `SAFE_SQL_PATTERN`），直接复用。

##### SQLi 正则过滤规范
###### 核心决策树
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
---

###### 白名单数据来源与处理策略
###### 白名单数据从哪里来？
|来源|说明|示例|
|-|-|-|
|**数据库元数据查询**|从数据库系统表查询实际存在的表/列名|`SELECT column_name FROM information_schema.columns WHERE table_name = 'users'`|
|**代码静态分析**|扫描代码中定义的实体类、ORM 模型|JPA `@Entity`、MyBatis mapper、SQLAlchemy Model|
|**配置文件/注解**|从配置文件或注解中提取允许的字段列表|`@AllowedFields({"id", "name", "email"})`|
|**API 文档/接口定义**|从 Swagger/OpenAPI 等文档中提取字段定义||

###### 白名单不完整时的处理策略
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
**AI 修复决策原则**：

1. **优先获取白名单**：如果代码中有 ORM 模型或实体类定义，优先从中提取字段列表
2. **正则兜底**：当白名单获取困难或不完整时，使用严格正则作为安全底线
3. **记录决策原因**：在代码注释中说明为什么选择正则而非白名单

---

###### 不同数据库的差异说明
|数据库|标识符引用符|参数占位符|特殊注意事项|
|-|-|-|-|
|**MySQL**|反引号 ```|`?` 或 `:name`|支持反引号包裹标识符，如 `user_name`|
|**PostgreSQL**|双引号 `"`|`$1, $2, ...` 或 `?`|支持双引号包裹标识符，如 `"user_name"`|
|**SQL Server**|方括号 `[` `]`|`@param` 或 `?`|支持方括号包裹标识符，如 `[user_name]`|
|**Oracle**|双引号 `"`|`:name` 或 `?`|标识符默认大写，双引号区分大小写|
|**SQLite**|双引号 `"` 或方括号 `[` `]`|`?` 或 `:name`|兼容多种引用符|

**AI 修复原则**：根据当前使用的数据库类型，选择对应的引用符和参数占位符。

---

###### 选择策略对比
|场景|推荐策略|原因|
|-|-|-|
|SQL 标识符（表名/列名/数据库名/索引名）|正则 + 白名单|格式验证 + 值验证，双重保障|
|SELECT 列表|正则 + 白名单|允许通配符 `*` 和多列，列名需白名单验证|
|ORDER BY/GROUP BY|正则 + 白名单|格式验证 + 列名白名单 + 方向关键字（ASC/DESC）|
|LIMIT/OFFSET|严格正则|只允许数字，不需要白名单|
|WHERE 条件|**参数化查询**|正则过滤仍有风险，参数化最安全|
|IN 子句|参数化查询优先|优先参数化，其次严格正则|

---

###### 各场景正则与实现
###### 1. SELECT 列名列表 `__SELECT_FILTER__`
**适用场景**：SELECT 后面的列名列表（如 `SELECT id,name,email FROM users` 或 `SELECT users.id,users.name FROM users`）

**正则（通用版，支持引用符）**：

```
^(\*|((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+))*))$
```
**支持格式**：

* `*` （通配符）
* `id` （单列）
* `users.id` （表名.列名）
* `user_name` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `id,name,email` （多列，逗号分隔）
* `users.id, users.name, users.email` （带表名前缀的多列）
* `id, name, email` （允许逗号前后空格）

**AI 修复指引**：

```php
function safeFilterSelect($select, $allowedColumns = []) {
    // 1. 先 trim() 去除首尾空白
    $select = trim($select);
    // 2. 正则验证格式（支持引用符）
    $regex = '/^(\*|((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+))*))$/';
    if (!preg_match($regex, $select)) {
        return false;
    }
    // 3. 如果是通配符 *，直接允许
    if ($select === '*') {
        return $select;
    }
    // 4. 提取列名并验证白名单
    $parts = preg_split('/\s*,\s*/', $select);
    foreach ($parts as $part) {
        // 去除引用符
        $cleanPart = preg_replace('/^[`"]|[`"]$/', '', $part);
        // 处理表名.列名格式，提取列名部分
        $column = strpos($cleanPart, '.') !== false
            ? substr($cleanPart, strrpos($cleanPart, '.') + 1)
            : $cleanPart;
        // 白名单验证（如果白名单不完整，跳过此步仅使用正则）
        if (!empty($allowedColumns)) {
            if (!in_array(strtolower(trim($column)), $allowedColumns, true)) {
                return false;
            }
        }
    }
    return $select;
}
```
---

###### 2. SQL 标识符（表名/列名/数据库名/索引名）`__IDENTIFIER_FILTER__`
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
* `user_name` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `[user_name]` （SQL Server 方括号）
* 长度限制：1-128 字符

**AI 修复指引**：

```php
function safeFilterIdentifier($identifier, $allowedIdentifiers = []) {
    // 1. 先 trim() 去除首尾空白
    $identifier = trim($identifier);
    // 2. 正则验证格式（支持引用符）
    $regex = '/^[A-Za-z_][A-Za-z0-9_]{0,127}$|^`[^`]{1,128}`$|^"[^"]{1,128}"$|^\[[^\]]{1,128}\]$/';
    if (!preg_match($regex, $identifier)) {
        return false;
    }
    // 3. 去除引用符
    $cleanIdentifier = preg_replace('/^[`"\[]|[`"\]]$/', '', $identifier);
    // 4. 白名单验证（如果白名单不完整，跳过此步仅使用正则）
    if (!empty($allowedIdentifiers)) {
        if (!in_array(strtolower($cleanIdentifier), $allowedIdentifiers, true)) {
            return false;
        }
    }
    return $identifier;
}
```
**说明**：

* 表名、列名、数据库名、索引名等标识符都遵循相同的命名规范
* 正则验证格式 + 白名单验证允许的值，双重保障
* 如果白名单不完整或无法获取，可省略步骤 4，仅使用正则验证

---

###### 3. ORDER BY `__ORDER_FILTER__`
**适用场景**：ORDER BY 后的字段（如 `ORDER BY name ASC, id DESC` 或 `ORDER BY users.name ASC, users.id DESC`）

**正则（通用版，支持引用符）**：

```
^((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?)*)$
```
**支持格式**：

* `name` （单列）
* `users.name` （表名.列名）
* `user_name` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `name ASC` / `name DESC` （带方向）
* `users.name ASC` / `users.name DESC` （带表名前缀和方向）
* `name ASC, id DESC` （多列）
* `users.name ASC, users.id DESC` （带表名前缀的多列）

**AI 修复指引**：

```php
function safeFilterOrderBy($order, $allowedColumns = []) {
    // 1. 正则验证格式（不区分大小写）
    $regex = '/^((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?)*)$/i';
    if (!preg_match($regex, $order)) {
        return false;
    }
    // 2. 提取列名并验证白名单
    $parts = preg_split('/\s*,\s*/', $order);
    foreach ($parts as $part) {
        // 提取列名部分（处理表名.列名格式）
        $columnPart = preg_split('/\s+/', $part)[0];
        // 去除引用符
        $cleanPart = preg_replace('/^[`"]|[`"]$/', '', $columnPart);
        $column = strpos($cleanPart, '.') !== false
            ? substr($cleanPart, strrpos($cleanPart, '.') + 1)
            : $cleanPart;
        // 白名单验证（如果白名单不完整，跳过此步仅使用正则）
        if (!empty($allowedColumns)) {
            if (!in_array(strtolower($column), $allowedColumns, true)) {
                return false;
            }
        }
    }
    return $order;
}
```
---

###### 4. GROUP BY `__GROUP_FILTER__`
**适用场景**：GROUP BY 后的字段（如 `GROUP BY name, age` 或 `GROUP BY users.name, users.age`）

**正则（通用版，支持引用符）**：

```
^((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+))*)$
```
**支持格式**：

* `name` （单列）
* `users.name` （表名.列名）
* `user_name` （MySQL 反引号）
* `"user_name"` （PostgreSQL/Oracle 双引号）
* `name, age` （多列）
* `users.name, users.age` （带表名前缀的多列）

**AI 修复指引**：

```php
function safeFilterGroupBy($group, $allowedColumns = []) {
    // 1. 正则验证格式
    $regex = '/^((`[^`]+`|"[^"]+"|\w+\.\w+|\w+)(,\s*(`[^`]+`|"[^"]+"|\w+\.\w+|\w+))*)$/';
    if (!preg_match($regex, $group)) {
        return false;
    }
    // 2. 提取列名并验证白名单
    $parts = preg_split('/\s*,\s*/', $group);
    foreach ($parts as $part) {
        // 去除引用符
        $cleanPart = preg_replace('/^[`"]|[`"]$/', '', $part);
        // 提取列名部分（处理表名.列名格式）
        $column = strpos($cleanPart, '.') !== false
            ? substr($cleanPart, strrpos($cleanPart, '.') + 1)
            : $cleanPart;
        // 白名单验证（如果白名单不完整，跳过此步仅使用正则）
        if (!empty($allowedColumns)) {
            if (!in_array(strtolower(trim($column)), $allowedColumns, true)) {
                return false;
            }
        }
    }
    return $group;
}
```
---

###### 5. LIMIT/OFFSET `__LIMIT_FILTER__`
**适用场景**：LIMIT、OFFSET 后的数值（如 `LIMIT 10`、`LIMIT 1,10`）

**正则**：`^\d+\s*,\s*\d+$|^\d+$`

**支持格式**：

* `10` （单数字）
* `1,10` （带偏移量）
* `1, 10` （允许逗号前后空格）

**AI 修复指引**：

```php
function safeFilterLimit($limit) {
    // 1. 先 trim() 去除首尾空白
    $limit = trim($limit);
    // 2. 正则验证纯数字
    if (preg_match('/^\d+\s*,\s*\d+$|^\d+$/', $limit)) {
        return $limit;
    }
    return false;
}
```
---

###### 6. WHERE 条件 `__WHERE_FILTER__`
**适用场景**：WHERE 子句、条件判断

**策略**：**放弃正则，使用参数化查询**

**AI 修复指引**：

```php
// ❌ 错误：字符串拼接
$sql = "SELECT * FROM users WHERE name = '" . $name . "'";

// ✅ 正确：参数化查询（PDO 使用 ?）
$sql = "SELECT * FROM users WHERE name = ?";
$stmt = $pdo->prepare($sql);
$stmt->execute([$name]);

// ✅ 正确：参数化查询（PDO 使用命名参数）
$sql = "SELECT * FROM users WHERE name = :name";
$stmt = $pdo->prepare($sql);
$stmt->bindValue(':name', $name);
$stmt->execute();

// ✅ 正确：参数化查询（mysqli）
$stmt = $mysqli->prepare("SELECT * FROM users WHERE name = ?");
$stmt->bind_param('s', $name);
$stmt->execute();
$result = $stmt->get_result();
```
---

###### 7. IN 子句 `__IN_FILTER__`
**适用场景**：IN 后面的值列表（如 `IN (1,2,3)`）

**策略**：优先参数化查询，其次严格正则

**正则**：

* 数字：`^\(\s*\d+(\s*,\s*\d+)*\s*\)$`
* 字符串：`^\(\s*'[^']*'(\s*,\s*'[^']*')*\s*\)$`

**支持格式**：

* `(1,2,3)` （数字列表）
* `('a','b','c')` （字符串列表）
* `(1, 2, 3)` （允许逗号前后空格）

**AI 修复指引**：

```php
// ✅ 优先：参数化查询（PDO 使用 ?）
$ids = [1, 2, 3];
$placeholders = implode(',', array_fill(0, count($ids), '?'));
$sql = "SELECT * FROM users WHERE id IN ($placeholders)";
$stmt = $pdo->prepare($sql);
$stmt->execute($ids);

// ✅ 优先：参数化查询（PDO 使用命名参数）
$ids = [1, 2, 3];
$params = [];
$placeholders = [];
foreach ($ids as $i => $id) {
    $key = ":id$i";
    $placeholders[] = $key;
    $params[$key] = $id;
}
$sql = "SELECT * FROM users WHERE id IN (" . implode(',', $placeholders) . ")";
$stmt = $pdo->prepare($sql);
$stmt->execute($params);

// ⚠️ 备选：严格正则验证（仅当无法参数化时）
function safeFilterInClause($inClause) {
    $inClause = trim($inClause);
    if (preg_match('/^\(\s*\d+(\s*,\s*\d+)*\s*\)$/', $inClause)) {
        return $inClause;
    }
    return false;
}
```
---

###### 8. 方向关键字 `__DIRECTION_FILTER__`
**适用场景**：ORDER BY 后的 ASC/DESC

**正则**：`^(asc|desc)$`

**支持格式**：

* `ASC` / `DESC` / `asc` / `desc` （不区分大小写）

**AI 修复指引**：

```php
function safeFilterDirection($direction) {
    // 正则验证（不区分大小写）
    if (preg_match('/^(asc|desc)$/i', $direction)) {
        return strtoupper($direction);
    }
    return false;
}
```
---

###### 9. 纯字母数字标识符 `__W_FILTER__`
**适用场景**：简单的表名、列名（无特殊字符）

**正则**：`^[\w-]+$`

**支持格式**：

* `user_name` （下划线）
* `User123` （字母数字）
* `table-1` （连字符）

**AI 修复指引**：

```php
function safeFilterSimpleIdentifier($identifier) {
    if (preg_match('/^[\w-]+$/', $identifier)) {
        return $identifier;
    }
    return false;
}
```
---

###### 10. 路径过滤 `__PATH_FILTER__`
**适用场景**：文件路径、URL 路径

**正则**：`^[\w/-]+$`

**支持格式**：

* `/path/to/file` （绝对路径）
* `path/to/file` （相对路径）

**AI 修复指引**：

```php
function safeFilterPath($path) {
    if (preg_match('/^[\w\/-]+$/', $path)) {
        return $path;
    }
    return false;
}
```
---

###### 11. 运算符 `__OP_FILTER__`
**适用场景**：算术运算符（如 `score+1`）

**正则**：`[+\-*/%]`

**支持格式**：

* `+` `-` `*` `/` `%` （基本算术运算符）

**AI 修复指引**：

```php
function safeFilterOperator($operator) {
    if (preg_match('/^[+\-*\/%]$/', $operator)) {
        return $operator;
    }
    return false;
}
```
---

###### 正则速查表
|过滤器|正则|说明|
|-|-|-|
|`__IDENTIFIER_FILTER__`|`/^[A-Za-z_][A-Za-z0-9_]{0,127}$\|^`[^`]{1,128}`$\|^"[^"]{1,128}"$/`|SQL 标识符，支持反引号/双引号，1-128字符|
|`__SELECT_FILTER__`|`/^(\*\|((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+))*))$/`|允许通配符 `*` 和逗号分隔的列名|
|`__ORDER_FILTER__`|`/^((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(\s+(ASC\|DESC))?(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(\s+(ASC\|DESC))?)*)$/i`|列名 + 方向关键字|
|`__GROUP_FILTER__`|`/^((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+))*)$/`|多列，逗号分隔|
|`__LIMIT_FILTER__`|`/^\d+\s*,\s*\d+$\|^\d+$/`|纯数字，允许逗号|
|`__WHERE_FILTER__`|**参数化查询**|不要用正则|
|`__IN_FILTER__`|`/^\(\s*\d+(\s*,\s*\d+)*\s*\)$/`|数字列表|
|`__DIRECTION_FILTER__`|`/^(asc\|desc)$/i`|ASC 或 DESC|
|`__W_FILTER__`|`/^[\w-]+$/`|字母数字+下划线+连字符|
|`__PATH_FILTER__`|`/^[\w\/-]+$/`|路径字符|
|`__OP_FILTER__`|`/^[+\-*\/%]$/`|算术运算符|

---

###### 重要提示
1. **所有正则验证前，务必先 **`trim()`** 去除首尾空白字符**
2. **白名单优先**：列名/表名等固定值优先用白名单
3. **白名单不完整时降级**：当白名单获取困难或不完整时，使用严格正则作为安全底线
4. **参数化优先**：WHERE 条件、IN 子句优先用参数化查询
5. **数据库适配**：根据使用的数据库类型选择对应的引用符和参数占位符
6. **最小化改动**：只修复漏洞点，不重构其他代码

### 补充：操作符/排序方向建议枚举校验（不替换现有正则）
在保留上述正则前提下，建议叠加枚举校验：

```php
$direction = strtoupper(trim($direction));
if (!in_array($direction, ['ASC', 'DESC'], true)) {
    throw new InvalidArgumentException('Invalid sort direction');
}

$op = strtoupper(trim($op));
$validOps = ['=', '!=', '<', '<=', '>', '>=', 'LIKE', 'IN'];
if (!in_array($op, $validOps, true)) {
    throw new InvalidArgumentException('Invalid operator');
}
```
---

## VI. 不可修复场景
遇到以下情况，标记为不可修复，不强行修改：

1. 外部生成整段 SQL（第三方 Jar/Extension/Service），无法拆解参数。
2. 污点作为复杂动态子句拼入（例如完整 WHERE 逻辑），无法安全结构化。

### 不可修复判定模板（建议）
* **数据流结论**：指出 taint 来源、传播路径、sink。
* **不可修复原因**：明确是“外部整段 SQL”还是“复杂子句不可拆解”。
* **风险说明**：说明为什么强修会破坏业务或产生误修。
* **建议动作**：补输入侧网关校验、人工评审、上游接口收敛。

---

## VII. 修复后检查点（强检查清单）
1. 是否优先使用框架安全写法（Yii 数组语法等）。
2. 是否遗留旧拼接 SQL（避免新旧并存导致覆盖）。
3. 是否存在 `prepare/bind` 后漏 `execute()`。
4. 是否误用 `execute()` 返回值。
5. 占位符数量是否与参数数量一致。
6. 条件分支中的参数绑定是否一致、变量是否已定义。
7. 若改动公共函数签名，调用方是否全部兼容。
8. 修复位置是否与真实数据流文件/函数一致（避免改错位置）。
9. 是否引入语法错误、死代码或不可达代码。
10. 正则与枚举校验是否按预期拦截非法输入。
11. **新增函数是否插入在正确位置**。
12. **正则表达式中的特殊符号是否正确转义或置于边界位置**。
13. **IN 子句的占位符数量是否与参数数组长度一致**。
14. **扫描报告指出的所有 sink 是否都已修复**（仅修复报告中的 sink，不主动扩展修复 AI 发现的其他分支）。
15. **新定义的过滤函数是否在 sink 前被调用**。
16. **PDO 位置参数绑定的数组索引是否正确**（注意 `array_merge` 产生 0-based 索引）。
17. **修复前后代码是否确实有差异**（避免无效修复提交）。
18. **框架的 **`query()`** 参数数组维度是否正确**（如 CodeIgniter 期望一维数组）。
19. **自定义白名单正则是否意外允许了单引号等 SQL 元字符**。
20. **占位符名称是否与 SQL 中一致**（`:name` 对应 `bindValue(':name', $val)`）。

---

## VIII. 高频修复失败反模式
以下为高频失败原因，修复时必须逐项自检：

1. **调用不存在 API**：如盲目使用 `prepare/queryf/execute($sql,$params)`。修复前必须在项目中**全局搜索**确认函数存在或框架支持该函数。
2. **修错文件或修错函数**：与 SARIF 数据流路径不一致。
3. **部分修复**：只修一个分支或一部分参数，扫描报告指出的 sink 仍可注入。**注意：仅修复漏洞扫描报告中明确指出的 sink，不主动修复 AI 自行发现的其他分支问题**。
4. **新旧 SQL 并存**：参数化查询后仍保留旧拼接查询。
5. **变量作用域错误**：分支变量在另一分支未定义即绑定。
6. **过滤顺序错误**：先拼接 SQL 后过滤/转义。
7. **仅加引号不转义**：`'$input'` 不是安全修复。
8. **IN 数组绑定错误**：单占位符绑定数组或空数组未兜底。PDO/Yii 的 `bindValue` **不支持**将单个参数展开为 IN 子句多值。
9. **过度依赖"看起来安全"**：未验证框架/DAO 真实能力。
10. **占位符与变量不匹配**：`bindValue()` 的占位符名称与 SQL 中不一致，或绑定的变量未定义。
11. **PHP 语法错误**：在函数声明与函数体之间插入代码，破坏类结构。
12. **数组直接字符串插值**：PHP 数组在字符串插值中输出 "Array"，导致 SQL 语法错误。
13. **定义了过滤函数但未调用**：业务代码中未调用新定义的 `safeFilter*` 函数。
14. **无效修复提交**：修复的 `newContent` 与 `originalContent` 完全相同。

### 占位符不匹配典型错误
```php
// 错误示例：$param 未定义，SQL 中无 :param 占位符
$sql = "SELECT * FROM table WHERE id = {$id}";  // 仍为直接拼接
$stmt = $db->createCommand($sql)->bindValue('param:', $param)->queryAll();

// 正确做法
$sql = "SELECT * FROM table WHERE id = :id";
$stmt = $db->createCommand($sql)->bindValue(':id', $id)->queryAll();
```
---

## IX. 最小修复策略（执行建议）
为提高修复成功率，可按以下顺序执行：

1. 找到真实 sink 位置，确认是否可参数化。
2. 可参数化则优先参数化；不可参数化则走正则过滤。
3. 对结构化参数叠加枚举校验（方向、操作符等）。
4. 使用 `safeFilter/safeValidate` + 临时变量截断数据流。
5. 做 VII 节 20 条强检查后再提交。