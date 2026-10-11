---
title: "vul_repair-go_sql_injection"
description: "go sqli 漏洞修复知识"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\code-security-comate\\references\\vul_repair-go_sql_injection.md"
---
go sqli 漏洞修复知识

## Go sqli 漏洞修复最佳实践
采用先分析漏洞报告->分析数据传递链路->判断是否存在依赖->分析修复方式（判断是否可以修复、使用哪种修复方式）->修复漏洞->**验证修复代码可编译且逻辑正确**（检查 import、函数重复定义、变量作用域、占位符数量匹配等）（注意：**不要做与漏洞修复无关的代码改动**）。

## 漏洞分析
### 不可修复场景
1. sql 语句为外部包生成或者传入，不是当前数据流链路的函数或者源码中定义生成，无法确定 sql 语句的信息，该场景需要进行 sql 语法检查，拆解整个 sql 语句，才可能保证安全且不干扰原始业务运行，所以这里作为不可修复场景，不进行漏洞修复。
2. 污点数据拼接到 sql 语句时，是作为 sql 语句中 select、update、delete 等子句，且无法确定子句具体信息，也是不可修复场景，不进行漏洞修复。

### 可修复场景
1. 漏洞修复必须在 **SQL 执行语句（sink 点）所在的文件和函数内**完成，不要创建新的代码文件。
2. 同个文件进行参数过滤时，可以在文件头定义过滤正则，如果定义已经存在，可以直接复用。
3. 对于 where 列名（操作符）之后的 value、insert 的values、like 的 value，需要使用**预编译/参数绑定**的方式进行漏洞修复。**注意**：LIKE 子句的值虽然可以预编译，但 `%` 和 `_` 是 SQL 通配符，若用户输入包含这些字符可能导致非预期的模糊匹配。如需精确匹配，应先转义这些字符：

```go
// LIKE 值转义示例
import "strings"

func escapeLikeValue(s string) string {
    s = strings.ReplaceAll(s, "\\", "\\\\")
    s = strings.ReplaceAll(s, "%", "\\%")
    s = strings.ReplaceAll(s, "_", "\\_")
    return s
}
// 使用示例：WHERE name LIKE ?
db.Query("SELECT * FROM users WHERE name LIKE ?", "%"+escapeLikeValue(keyword)+"%")
```
4. 表名、列名、视图名称、DataBase 名称等拼接进入SQL 语句时需要进行白名单或者过滤的方式修复漏洞。
5. show、create 、drop、grant 语句场景不支持预编译参数方式修复漏洞，需要使用对污点参数进行白名单或者过滤的方法进行修复。
6. 对于 limit、SortBy、orderBy 等子句无法使用预编译，需要使用白名单或者正则过滤的方式修复。
7. 当前框架支持安全写法时，优先使用框架安全写法，在无法使用安全写法时，才使用过滤等方案进行漏洞修复（注意不可修复场景不需要强行进行过滤修复）。
8. 几何函数例如ST_GeometryN,第一个参数为列名，不支持预编译，如果污点数据传入，需要白名单或者正则过滤的方式修复 ，第二个参数支持预编译，使用预编译方式修复。
9. SQL 语句拼接 in 的参数时，需要对其中的每个子项进行过滤或者预编译，如果适合修改成预编译，则进行参数个数的?替换，将参数放入查询参数中，优先进行预编译参数绑定。注意事项：(1) 过滤 IN 子项时，如果所有子项都被过滤，必须有兜底逻辑（如返回空结果或返回错误），不能生成空的 `IN ()`，否则会导致 SQL 语法错误；(2) 动态构建 IN 列表时，建议先收集合法项到新切片，再用 `strings.Join` 拼接，避免基于原始索引判断逗号导致的尾随逗号问题；(3) 某些数据库对单条 SQL 的参数数量有限制（如 SQLite 默认 999 个），大量 IN 参数需分批处理。

**IN 子句预编译示例：**

```go
import (
    "fmt"
    "strings"
)

// 动态生成 IN 子句的占位符
func buildInClause(ids []int64) (string, []interface{}) {
    if len(ids) == 0 {
        return "", nil
    }
    placeholders := make([]string, len(ids))
    args := make([]interface{}, len(ids))
    for i, id := range ids {
        placeholders[i] = "?"
        args[i] = id
    }
    return strings.Join(placeholders, ","), args
}

// 使用示例
func queryByIDs(db *sql.DB, ids []int64) ([]User, error) {
    if len(ids) == 0 {
        return []User{}, nil // 兜底：空列表直接返回空结果
    }
    placeholders, args := buildInClause(ids)
    query := fmt.Sprintf("SELECT * FROM users WHERE id IN (%s)", placeholders)
    rows, err := db.Query(query, args...)
    // ...
}
```
10. 当污点拼接进入 sql 语句时，在分析确认需要通过预编译修复的时候，需要考虑 sql 语句的所在位置，例如有时 sql 语句为全局变量赋值到局部变量，改成预编译执行时，需要将当前函数变更为预编译方式，且需要变更全局 sql 语句为预编译方式，避免遗漏导致用户执行出错。
11. 注意：一定是已经修改 sql 语句为预编译方式时，才对查询代码进行预编译方式修改，否则考虑使用过滤的方式进行漏洞修复。
12. 同一个参数进行漏洞修复时，只需要采取一种修复方式即可，不要同时进行预编译、参数绑定和过滤。
13. 当污点数据拼接进入到 sql ，需要详细分析当前函数是否还存在其他地方使用了该 sql，避免因为采用预编译修复方案，导致其他使用该 sql 的场景存在异常；如果其他使用的场景在当前文件中，可以统一进行预编译方式修改，不过得考虑使用的函数需要重载，保障其他文件调用正常。
14. 修复时尽量保持原有函数调用链路完整。不允许为了简化修复而跳过或删除原有的函数调用，应在原有调用链路的基础上进行安全修复（如对传入参数进行过滤或预编译），而不是用新的内联代码替换整个函数调用。例如原函数 A 调用函数 B 完成操作，修复后必须仍然调用 B，不能将 B 的逻辑内联到 A 中从而丢失 B 的调用。
15. 修复时只能使用代码中已存在的函数或标准库/已导入依赖中的函数或修复时新定义的函数。严禁在修复方案中调用不存在且在修复方案中没有定义的函数。**修复前必须检查同包内是否已存在同名函数**。若函数不存在，必须在修复代码中完整定义该函数，不能仅调用而不定义。
16. 修复前必须确认框架方法是否支持参数化绑定。GORM 的 `Order()`、`Group()`、`Select()` 等方法不支持参数化绑定（不接受额外的绑定参数），对这些方法中的污点数据只能使用正则过滤方式修复，不能尝试传入额外参数进行绑定。补充说明：(1) GORM `.Where(string)` 单参数形式（无 `?` 占位符）等同于直接拼接，必须改为 `.Where("col = ?", val)` 形式；(2) GORM `.Table(string)` 中的表名不支持参数化，必须使用正则过滤；(3) GORM `.Joins(string)` 中的表名同样不支持参数化，必须使用正则过滤。
17. SQL 原文中已存在 `?` 字符时（如 PostgreSQL jsonb 路径表达式 `@?`、`?`），改为预编译方式前必须确认不会与参数占位符冲突。如果原始 SQL 中包含非占位符用途的 `?`（例如 `answer::jsonb @? '$.content[*] ? (@.type == "rich-text")'`），必须对原有 `?` 进行转义或采用其他方式避免占位符位置错乱，否则会导致参数绑定位置偏移、运行时报错。
18. 当污点参数作为 SQL 操作符（如 `=`, `LIKE`, `IN`）拼入 SQL 时，不适合使用正则过滤，应使用白名单枚举精确匹配合法操作符值。示例：

```go
import (
    "fmt"
    "strings"
)
var validOperators = map[string]bool{
    "=": true, "!=": true, "<>": true,
    "<": true, ">": true, "<=": true, ">=": true,
    "LIKE": true, "NOT LIKE": true,
    "IN": true, "NOT IN": true,
}

func safeValidateOperator(op string) (string, error) {
    upperOp := strings.ToUpper(strings.TrimSpace(op))
    if !validOperators[upperOp] {
        return "", fmt.Errorf("invalid SQL operator")
    }
    return upperOp, nil
}
```
上述白名单为常见操作符示例，应根据实际业务需要扩展（如 `BETWEEN`、`IS NULL`、`ILIKE` 等）。

19. **修复代码必须检查并补充必要的 import 导入**。当修复方案引入新的函数调用时，必须确认对应的包已在文件 import 块中声明，若未声明则必须添加。常见修复场景需要导入的包：

* 使用正则过滤 `regexp.MatchString`、`regexp.MustCompile` 时：需导入 `"regexp"`
* 使用 `fmt.Errorf`、`fmt.Sprintf` 时：需导入 `"fmt"`
* 使用 `strings.Join`、`strings.TrimSpace`、`strings.ToUpper` 时：需导入 `"strings"`
* 使用 `strconv.Itoa`、`strconv.Atoi` 时：需导入 `"strconv"`

**修复完成后，必须检查文件头部 import 块是否包含所有新引入的依赖包，确保代码能够通过编译（**`go build`**）。**

20. **避免同包内重复定义函数**。在定义 `safeFilterXxx` 等辅助函数前，必须先检查同一 Go 包（同目录下所有 `.go` 文件）中是否已存在同名函数。若已存在，直接复用；若不存在，才在当前文件中定义。
21. **注意变量作用域，避免遮蔽问题**。

* 不要在 `if`/`for` 等块内使用 `:=` 声明变量后在块外使用，会导致 `undefined` 错误
* 避免在内层作用域用 `:=` 重新声明与外层同名的变量，导致外层变量被遮蔽、值始终为零值
* 正确做法：在外层先声明变量（`var safeSortBy string`），内层使用 `=` 赋值而非 `:=`

22. **确保修复代码无编译问题**。

* 不要引入声明后未使用的变量（Go 编译器会报错）
* SQL 语句拼接时注意语法正确性，如 `args := []interface{}{}` 不能写成 `args = []interface{}`
* 不要将多条语句写在同一行（除非用分号分隔），避免格式错误

23. **大小写比较必须一致**。在白名单校验时，如果对输入做了大小写转换（如 `strings.ToUpper`），白名单常量也必须使用相同大小写，否则永远无法匹配。示例：

```go
// 错误：转大写后与小写比较，永远为 false
input = strings.ToUpper(input)
if input == "asc" || input == "desc" { ... }

// 正确：统一使用大写
input = strings.ToUpper(input)
if input == "ASC" || input == "DESC" { ... }
```
24. **xorm/sqlx 的 IN 查询必须正确处理多值参数**。`session.SQL("... IN (?)", args...)` 中单个 `?` 无法自动展开为多值列表。正确做法：

* 使用 xorm 的 `.In("column", slice)` 方法
* 或动态生成与切片长度匹配的占位符 `?,?,?`，然后展开参数 `args...`

**xorm IN 查询示例：**

```go
// 方式1：使用 In 方法（推荐）
var users []User
err := engine.Where("status = ?", 1).In("id", ids).Find(&users)

// 方式2：动态生成占位符
placeholders := strings.Repeat("?,", len(ids))
placeholders = strings.TrimSuffix(placeholders, ",")
query := fmt.Sprintf("SELECT * FROM users WHERE id IN (%s)", placeholders)
// 将 []int64 转换为 []interface{}
args := make([]interface{}, len(ids))
for i, v := range ids {
    args[i] = v
}
err := engine.SQL(query, args...).Find(&users)
```
25. **过滤函数必须包含实际的过滤逻辑**。新增的安全过滤函数必须真正实现过滤或校验，不能仅复制原有拼接逻辑。过滤函数应包含：正则匹配/白名单校验 + 非法时返回错误或空值。
26. **过滤函数的错误返回必须正确**。当参数非法时，必须返回非 nil 的 error，调用方才能通过 `if err != nil` 拦截。禁止在非法分支返回 `("", nil)`，这会导致恶意输入被放行。
27. **修复代码插入位置必须正确**。不要将 `return` 语句或其他中断逻辑插入到循环体之前，否则会导致循环被跳过、函数提前返回空结果。修复代码应插入到数据使用点之前、但在必要业务逻辑之后。
28. **占位符数量必须与参数数量严格匹配**。修改为参数化查询后，SQL 中 `?` 的数量必须与传入的参数个数完全一致，否则会导致参数错位或运行时报错。特别注意：

* `append(args, args...)` 会导致参数翻倍
* INSERT 语句的 VALUES 中 `?` 数量必须与字段数一致

29. **修复必须覆盖完整数据流路径**。同一文件或函数中如果存在多个使用同一污点参数的 sink 点，必须全部修复，不能只修复扫描工具指出的单个 sink。检查所有 `fmt.Sprintf`、字符串拼接、`db.Where`/`db.Raw` 等调用点。**特别注意**：当污点来源是结构体（如 `filter` 对象）时，必须检查该结构体的所有字段是否都被用于 SQL 拼接，例如同时存在 `filter.Field` 和 `filter.Operator` 两个污点字段时，必须对两者都进行校验，不能只修复其中一个。
30. **避免验证前的冗余赋值**。不要在验证通过之前将原始污点值赋给业务变量，否则静态分析工具会沿此赋值路径追踪到 sink，认为污点链未断开。正确做法：先验证/过滤，通过后才将安全值赋给业务变量。**这是导致修复失败的常见原因之一，必须严格遵守**。示例：

```go
// 错误：先赋值后验证，污点已传播（静态分析工具会追踪第一行的赋值）
conds.Order = param.OrderBy           // 污点已传播到 conds.Order
if conds.Order != "" {
    safeOrder, err := safeFilter(param.OrderBy)
    if err != nil { return err }
    conds.Order = safeOrder           // 覆写，但工具仍追踪到上面的赋值
}

// 正确：先验证，通过后才赋值（污点链被完全阻断）
if param.OrderBy != "" {
    safeOrder, err := safeFilter(param.OrderBy)
    if err != nil { return err }
    conds.Order = safeOrder           // 仅此一次赋值，且是安全值
} else {
    conds.Order = "default_value"
}
```
### 过滤方式规则
1.对于需要通过正则过滤进行防护的污点参数，需根据其使用方式区分处理：

* 如果污点参数后续是以普通变量直接拼接或传递，可直接对该变量进行正则过滤。
* 如果污点数据来源于某个对象的成员方法调用（如 `req.GetSortField()`）或可迭代对象的元素，**不能过滤后仍使用原对象的方法调用**，必须用临时变量承接过滤后的结果，后续使用该临时变量进行拼接或传递，以确保数据流检测工具能识别到安全截断。过滤函数命名以 `safeFilter` 或 `safeValidate` 开头，**若当前文件中不存在该函数则必须在当前文件中定义（文件级别，非嵌套在其他函数内部），严禁调用未定义的函数**。示例：

错误写法：过滤后仍使用原对象方法调用，数据流未截断

```go
if match, _ := regexp.MatchString(`^[\w\s\[\]"` + "`$.,*]+$", req.GetSortField()); !match {
    return fmt.Errorf("invalid sort field")
}
tx = tx.Order(req.GetSortField() + " DESC") // 数据流检测无法识别防护
```
正确写法：在文件级别定义过滤函数（注意先判断是否已经存在同名函数，不能定义在其他函数体内部，Go 不支持具名嵌套函数）

```go
import (
    "fmt"
    "regexp"
)

func safeFilterField(field string) (string, error) {
    if match, _ := regexp.MatchString(`^[\w\s\[\]"` + "`$.,*]+$", field); !match {
        return "", fmt.Errorf("invalid field value")
    }
    return field, nil
}
```
在业务函数中调用，用临时变量承接结果

```go
safeSortField, err := safeFilterField(req.GetSortField())
if err != nil { return err }
tx = tx.Order(safeSortField + " DESC")
```
2.如果传入下层函数的参数是一个结构体对象，而污点数据仅存在于其某个字段，应通过过滤函数对整个对象进行过滤处理，返回一个安全的新对象，并用临时变量承接，后续使用该临时对象向下层函数传递。过滤函数命名以 `safeFilter` 或 `safeValidate` 开头，**该函数必须在当前文件中以文件级别函数定义（非嵌套在其他函数内部），严禁调用不存在的函数**。示例：

错误写法：仅过滤字段后仍传递原对象，数据流未截断

```go
if match, _ := regexp.MatchString(`^[\w\s\[\]"` + "`$.,*]+$", params.TableName); !match {
    return fmt.Errorf("invalid table name")
}
result, err := queryData(db, params) // 原对象传递，数据流检测无法识别防护
```
正确写法：在文件级别定义过滤函数（注意先判断是否已经存在同名函数，不能定义在其他函数体内部，Go 不支持具名嵌套函数）

```go
import (
    "fmt"
    "regexp"
)

func safeFilterQueryParams(p QueryParams) (QueryParams, error) {
    if match, _ := regexp.MatchString(`^[\w\s\[\]"` + "`$.,*]+$", p.TableName); !match {
        return QueryParams{}, fmt.Errorf("invalid table name")
    }
    return p, nil
}
```
在业务函数中调用，用临时变量承接结果

```go
safeParams, err := safeFilterQueryParams(params)
if err != nil { return err }
result, err := queryData(db, safeParams)
```
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

```go
import (
    "fmt"
    "regexp"
    "strings"
)

// safeFilterSelect 过滤 SELECT 列名列表
// allowedColumns 为可选白名单，传入 nil 则仅做正则校验
func safeFilterSelect(selectStr string, allowedColumns map[string]bool) (string, error) {
    // 1. 先 TrimSpace 去除首尾空白
    selectStr = strings.TrimSpace(selectStr)
    // 2. 正则验证格式（支持引用符）
    regex := `^(\*|(` + "`[^`]+`" + `|"[^"]+"|\w+\.\w+|\w+)(,\s*(` + "`[^`]+`" + `|"[^"]+"|\w+\.\w+|\w+))*))$`
    matched, _ := regexp.MatchString(regex, selectStr)
    if !matched {
        return "", fmt.Errorf("invalid select columns")
    }
    // 3. 如果是通配符 *，直接允许
    if selectStr == "*" {
        return selectStr, nil
    }
    // 4. 提取列名并验证白名单
    parts := regexp.MustCompile(`\s*,\s*`).Split(selectStr, -1)
    for _, part := range parts {
        // 去除引用符
        cleanPart := strings.Trim(part, "`\"")
        // 处理表名.列名格式，提取列名部分
        column := cleanPart
        if idx := strings.LastIndex(cleanPart, "."); idx != -1 {
            column = cleanPart[idx+1:]
        }
        // 白名单验证（如果白名单不为空）
        if allowedColumns != nil && len(allowedColumns) > 0 {
            if !allowedColumns[strings.ToLower(strings.TrimSpace(column))] {
                return "", fmt.Errorf("column not in whitelist: %s", column)
            }
        }
    }
    return selectStr, nil
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

```go
import (
    "fmt"
    "regexp"
    "strings"
)

// safeFilterIdentifier 过滤 SQL 标识符（表名/列名/数据库名/索引名）
// allowedIdentifiers 为可选白名单，传入 nil 则仅做正则校验
func safeFilterIdentifier(identifier string, allowedIdentifiers map[string]bool) (string, error) {
    // 1. 先 TrimSpace 去除首尾空白
    identifier = strings.TrimSpace(identifier)
    // 2. 正则验证格式（支持引用符）
    regex := `^[A-Za-z_][A-Za-z0-9_]{0,127}$|^` + "`[^`]{1,128}`" + `$|^"[^"]{1,128}"$|^\[[^\]]{1,128}\]$`
    matched, _ := regexp.MatchString(regex, identifier)
    if !matched {
        return "", fmt.Errorf("invalid identifier")
    }
    // 3. 去除引用符
    cleanIdentifier := strings.Trim(identifier, "`\"[]")
    // 4. 白名单验证（如果白名单不为空）
    if allowedIdentifiers != nil && len(allowedIdentifiers) > 0 {
        if !allowedIdentifiers[strings.ToLower(cleanIdentifier)] {
            return "", fmt.Errorf("identifier not in whitelist: %s", cleanIdentifier)
        }
    }
    return identifier, nil
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

```go
import (
    "fmt"
    "regexp"
    "strings"
)

// safeFilterOrderBy 过滤 ORDER BY 子句
// allowedColumns 为可选白名单，传入 nil 则仅做正则校验
func safeFilterOrderBy(order string, allowedColumns map[string]bool) (string, error) {
    // 1. 正则验证格式（不区分大小写）
    regex := `(?i)^((` + "`[^`]+`" + `|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?(,\s*(` + "`[^`]+`" + `|"[^"]+"|\w+\.\w+|\w+)(\s+(ASC|DESC))?)*)$`
    matched, _ := regexp.MatchString(regex, order)
    if !matched {
        return "", fmt.Errorf("invalid order by clause")
    }
    // 2. 提取列名并验证白名单
    parts := regexp.MustCompile(`\s*,\s*`).Split(order, -1)
    for _, part := range parts {
        // 提取列名部分（处理表名.列名格式）
        columnPart := regexp.MustCompile(`\s+`).Split(part, -1)[0]
        // 去除引用符
        cleanPart := strings.Trim(columnPart, "`\"")
        column := cleanPart
        if idx := strings.LastIndex(cleanPart, "."); idx != -1 {
            column = cleanPart[idx+1:]
        }
        // 白名单验证（如果白名单不为空）
        if allowedColumns != nil && len(allowedColumns) > 0 {
            if !allowedColumns[strings.ToLower(column)] {
                return "", fmt.Errorf("column not in whitelist: %s", column)
            }
        }
    }
    return order, nil
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

```go
import (
    "fmt"
    "regexp"
    "strings"
)

// safeFilterGroupBy 过滤 GROUP BY 子句
// allowedColumns 为可选白名单，传入 nil 则仅做正则校验
func safeFilterGroupBy(group string, allowedColumns map[string]bool) (string, error) {
    // 1. 正则验证格式
    regex := `^((` + "`[^`]+`" + `|"[^"]+"|\w+\.\w+|\w+)(,\s*(` + "`[^`]+`" + `|"[^"]+"|\w+\.\w+|\w+))*)$`
    matched, _ := regexp.MatchString(regex, group)
    if !matched {
        return "", fmt.Errorf("invalid group by clause")
    }
    // 2. 提取列名并验证白名单
    parts := regexp.MustCompile(`\s*,\s*`).Split(group, -1)
    for _, part := range parts {
        // 去除引用符
        cleanPart := strings.Trim(part, "`\"")
        // 提取列名部分（处理表名.列名格式）
        column := cleanPart
        if idx := strings.LastIndex(cleanPart, "."); idx != -1 {
            column = cleanPart[idx+1:]
        }
        // 白名单验证（如果白名单不为空）
        if allowedColumns != nil && len(allowedColumns) > 0 {
            if !allowedColumns[strings.ToLower(strings.TrimSpace(column))] {
                return "", fmt.Errorf("column not in whitelist: %s", column)
            }
        }
    }
    return group, nil
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

```go
import (
    "fmt"
    "regexp"
    "strings"
)

// safeFilterLimit 过滤 LIMIT/OFFSET 参数
func safeFilterLimit(limit string) (string, error) {
    // 1. 先 TrimSpace 去除首尾空白
    limit = strings.TrimSpace(limit)
    // 2. 正则验证纯数字
    regex := `^\d+\s*,\s*\d+$|^\d+$`
    matched, _ := regexp.MatchString(regex, limit)
    if matched {
        return limit, nil
    }
    return "", fmt.Errorf("invalid limit value")
}
```
---

###### 6. WHERE 条件 `__WHERE_FILTER__`
**适用场景**：WHERE 子句、条件判断

**策略**：**放弃正则，使用参数化查询**

**AI 修复指引**：

```go
import "database/sql"

// ❌ 错误：字符串拼接
sql := fmt.Sprintf("SELECT * FROM users WHERE name = '%s'", name)

// ✅ 正确：参数化查询（database/sql 使用 ?）
rows, err := db.Query("SELECT * FROM users WHERE name = ?", name)

// ✅ 正确：参数化查询（PostgreSQL 使用 $1, $2）
rows, err := db.Query("SELECT * FROM users WHERE name = $1", name)

// ✅ 正确：GORM 参数绑定
db.Where("name = ?", name).First(&user)
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

```go
import (
    "fmt"
    "regexp"
    "strings"
)

// ✅ 优先：参数化查询（动态生成占位符）
func queryByIDs(db *sql.DB, ids []int64) ([]User, error) {
    if len(ids) == 0 {
        return []User{}, nil // 兜底：空列表直接返回空结果
    }
    placeholders := make([]string, len(ids))
    args := make([]interface{}, len(ids))
    for i, id := range ids {
        placeholders[i] = "?"
        args[i] = id
    }
    query := fmt.Sprintf("SELECT * FROM users WHERE id IN (%s)", strings.Join(placeholders, ","))
    rows, err := db.Query(query, args...)
    // ...
}

// ⚠️ 备选：严格正则验证（仅当无法参数化时）
func safeFilterInClause(inClause string) (string, error) {
    inClause = strings.TrimSpace(inClause)
    regex := `^\(\s*\d+(\s*,\s*\d+)*\s*\)$`
    matched, _ := regexp.MatchString(regex, inClause)
    if matched {
        return inClause, nil
    }
    return "", fmt.Errorf("invalid IN clause")
}
```
---

###### 8. 方向关键字 `__DIRECTION_FILTER__`
**适用场景**：ORDER BY 后的 ASC/DESC

**正则**：`^(asc|desc)$`

**支持格式**：

* `ASC` / `DESC` / `asc` / `desc` （不区分大小写）

**AI 修复指引**：

```go
import (
    "fmt"
    "regexp"
    "strings"
)

// safeFilterDirection 过滤排序方向（ASC/DESC）
func safeFilterDirection(direction string) (string, error) {
    // 正则验证（不区分大小写）
    regex := `(?i)^(asc|desc)$`
    matched, _ := regexp.MatchString(regex, direction)
    if matched {
        return strings.ToUpper(direction), nil
    }
    return "", fmt.Errorf("invalid direction")
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

```go
import (
    "fmt"
    "regexp"
)

// safeFilterSimpleIdentifier 过滤简单标识符（字母数字下划线连字符）
func safeFilterSimpleIdentifier(identifier string) (string, error) {
    regex := `^[\w-]+$`
    matched, _ := regexp.MatchString(regex, identifier)
    if matched {
        return identifier, nil
    }
    return "", fmt.Errorf("invalid identifier")
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

```go
import (
    "fmt"
    "regexp"
)

// safeFilterPath 过滤文件路径/URL路径
func safeFilterPath(path string) (string, error) {
    regex := `^[\w/-]+$`
    matched, _ := regexp.MatchString(regex, path)
    if matched {
        return path, nil
    }
    return "", fmt.Errorf("invalid path")
}
```
---

###### 11. 运算符 `__OP_FILTER__`
**适用场景**：算术运算符（如 `score+1`）

**正则**：`[+\-*/%]`

**支持格式**：

* `+` `-` `*` `/` `%` （基本算术运算符）

**AI 修复指引**：

```go
import (
    "fmt"
    "regexp"
)

// safeFilterOperator 过滤算术运算符
func safeFilterOperator(operator string) (string, error) {
    regex := `^[+\-*/%]$`
    matched, _ := regexp.MatchString(regex, operator)
    if matched {
        return operator, nil
    }
    return "", fmt.Errorf("invalid operator")
}
```
---

###### 正则速查表
|过滤器|正则|说明|
|-|-|-|
|`__IDENTIFIER_FILTER__`|`` ^[A-Za-z_][A-Za-z0-9_]{0,127}$\|^`[^`]{1,128}`$\|^"[^"]{1,128}"$ ``|SQL 标识符，支持反引号/双引号，1-128字符|
|`__SELECT_FILTER__`|`` ^(\*\|((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+))*))$ ``|允许通配符 `*` 和逗号分隔的列名|
|`__ORDER_FILTER__`|`` (?i)^((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(\s+(ASC\|DESC))?(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(\s+(ASC\|DESC))?)*)$ ``|列名 + 方向关键字|
|`__GROUP_FILTER__`|`` ^((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+))*)$ ``|多列，逗号分隔|
|`__LIMIT_FILTER__`|`^\d+\s*,\s*\d+$\|^\d+$`|纯数字，允许逗号|
|`__WHERE_FILTER__`|**参数化查询**|不要用正则|
|`__IN_FILTER__`|`^\(\s*\d+(\s*,\s*\d+)*\s*\)$`|数字列表|
|`__DIRECTION_FILTER__`|`(?i)^(asc\|desc)$`|ASC 或 DESC|
|`__W_FILTER__`|`^[\w-]+$`|字母数字+下划线+连字符|
|`__PATH_FILTER__`|`^[\w/-]+$`|路径字符|
|`__OP_FILTER__`|`^[+\-*/%]$`|算术运算符|

**Go 语言正则使用示例**：
```go
import "regexp"

// =====================================================
// 重要：Go 正则字符串的两种写法（必须二选一，不能混用）
// =====================================================

// 方式1：原始字符串（推荐）- 反斜杠不需要转义
regex := `^[\w\s\[\]"` + "`" + `$.,*]+$`
matched, _ := regexp.MatchString(regex, input)

// 方式2：普通字符串 - 反斜杠必须双重转义
regex := "^[\\w\\s\\[\\]\"`$.,*]+$"
matched, _ := regexp.MatchString(regex, input)

// ❌ 错误写法（会导致编译错误或运行时错误）：
// regex := "^[\w\s]+$"  // \w \s 不是有效的 Go 字符串转义！

// 使用预编译正则（性能更好，适合多次使用）
var identifierRegex = regexp.MustCompile(`^[\w-]+$`)
matched := identifierRegex.MatchString(identifier)

// 不区分大小写：在正则开头加 (?i)
matched, _ := regexp.MatchString(`(?i)^(asc|desc)$`, direction)
```

**Go 正则转义对照表**：
|正则元字符|原始字符串写法|普通字符串写法|
|-|-|-|
|`\w`|`` `\w` ``|`"\\w"`|
|`\s`|`` `\s` ``|`"\\s"`|
|`\d`|`` `\d` ``|`"\\d"`|
|`\.`|`` `\.` ``|`"\\."`|
|`\[`|`` `\[` ``|`"\\["`|
|反引号 `` ` ``|需拼接：`` `a` + "`" + `b` ``|`"\`"`|

---

###### 重要提示
1. **所有正则验证前，务必先 `strings.TrimSpace()` 去除首尾空白字符**
2. **白名单优先**：列名/表名等固定值优先用白名单
3. **白名单不完整时降级**：当白名单获取困难或不完整时，使用严格正则作为安全底线
4. **参数化优先**：WHERE 条件、IN 子句优先用参数化查询
5. **数据库适配**：根据使用的数据库类型选择对应的引用符和参数占位符
6. **最小化改动**：只修复漏洞点，不重构其他代码
7. **Go 正则特点**：Go 使用 RE2 引擎，不支持回溯，用 `(?i)` 实现大小写不敏感
8. **Go 正则字符串写法（关键）**：
   - 使用原始字符串 `` `...` `` 时，`\w` `\s` 等直接写，不需要转义
   - 使用普通字符串 `"..."` 时，必须写成 `\\w` `\\s`（双重转义）
   - **绝对不能**在普通字符串中写 `"\w"` `"\s"`，这会导致编译错误或运行时错误

## 各框架SQL注入风险与防护
### 1. 标准库 database/sql
#### 风险示例
```go
// 危险: 表名列名和参数直接拼接SQL
query := fmt.Sprintf("SELECT id,%s,book FROM users WHERE username = '%s'", addr, username)
rows, err := db.Query(query)
```
#### 风险描述
直接拼接用户输入到SQL语句中会导致SQL注入漏洞，攻击者可构造恶意输入改变SQL语义。

#### 修复方案
使用参数化查询(Prepared Statements), 对于表名列名等无法参数化查询的做正则过滤。

#### 修复示例
```go
// 安全: 对于危害的表名列名做过滤
if match, _ := regexp.MatchString("^[\\w\\s\\[\\]\"`$.,*]+$", addr); !match {
    return nil, fmt.Errorf("invalid field name")
}
// 安全: 使用参数化查询
query := fmt.Sprintf("SELECT id,%s,book FROM users WHERE username = ?", addr)
rows, err := db.Query(query, username)
```
### 2. GORM
#### 风险示例
```go
// 危险: 使用Raw方法直接拼接
db.Raw(fmt.Sprintf("SELECT * FROM %s WHERE username = '%s'", tableName, username)).Scan(&result)

// 危险: 使用Where条件拼接
db.Where("username = '" + username + "'").First(&user)
```
#### 风险描述
GORM虽然提供了安全的查询构建方法，但如果开发者直接拼接SQL字符串，仍然存在注入风险。

#### 修复方案
使用GORM的参数绑定功能(预编译)或模型查询,对于表名列名等无法参数化查询的做正则过滤。注意使用支持参数绑定的函数。

#### 修复示例
```go
// 安全: 对于表名列名等无法参数化查询的做正则过滤。
if match, _ := regexp.MatchString("^[\\w\\s\\[\\]\"`$.,*]+$", tableName); !match {
    return nil, fmt.Errorf("invalid table name")
}
// 安全: 使用参数绑定
db.Raw(fmt.Sprintf("SELECT * FROM %s WHERE username = ?", tableName), username).Scan(&result)

// 安全: 使用模型查询
db.Where("username = ?", username).First(&user)
```
### 3. sqlx
#### 风险示例
```go
// 危险: 直接拼接SQL
query := fmt.Sprintf("SELECT * FROM users WHERE username = '%s'", username)
err := db.Get(&user, query)
```
#### 风险描述
sqlx是标准库的扩展，同样存在拼接SQL导致注入的风险。

#### 修复方案
使用命名参数或位置参数。

#### 修复示例
```go
// 安全: 对于表名列名等无法参数化查询的做正则过滤。
if match, _ := regexp.MatchString("^[\\w\\s\\[\\]\"`$.,*]+$", tableName); !match {
    return nil, fmt.Errorf("invalid table name")
}
// 安全：使用命名参数
query := fmt.Sprintf("SELECT * FROM %s WHERE username = :username", tableName)
nstmt, err := db.PrepareNamed(query)
if err != nil {
    return nil, err
}
err = nstmt.Get(&result, map[string]interface{}{"username": username})

// 安全: 对于表名列名等无法参数化查询的做正则过滤。
if match, _ := regexp.MatchString("^[\\w\\s\\[\\]\"`$.,*]+$", tableName); !match {
    return nil, fmt.Errorf("invalid table name")
}
// 安全: 使用位置参数, 预编译
query := fmt.Sprintf("SELECT * FROM %s WHERE username = ?", tableName)
err := db.Get(&result, query, username)
```
### 4. ent
#### 风险示例
```go
// ent本身设计上更安全，但错误使用仍有风险
client.User.Query().
    Where(func(s *sql.Selector) {
        s.Where(sql.Expr(fmt.Sprintf("username = '%s'", username)))
    }).All(ctx)
```
#### 风险描述
ent框架设计上更安全，但直接使用sql.Expr拼接字符串仍有风险。

#### 修复方案
使用ent提供的类型安全查询方法。

#### 修复示例
```go
// 安全: 使用类型安全方法
user, err := client.User.Query().
    Where(user.Username(username)).
    Only(ctx)
```
### 5. XORM
#### 风险示例
```go
// 危险: 直接拼接SQL
engine.SQL(fmt.Sprintf("SELECT * FROM users WHERE username = '%s'", username)).Get(&user)
```
#### 风险描述
XORM提供了安全的查询方法，但直接拼接SQL字符串仍会导致注入。

#### 修复方案
使用参数化查询或XORM的构建器方法。

#### 修复示例
```go
// 安全: 使用参数化查询
engine.SQL("SELECT * FROM users WHERE username = ?", username).Get(&user)

// 安全: 使用构建器方法
engine.Where("username = ?", username).Get(&user)
```
### 6. Beego ORM
#### 风险示例
```go
// 危险: 直接拼接SQL
o.Raw(fmt.Sprintf("SELECT * FROM users WHERE username = '%s'", username)).QueryRow(&user)
```
#### 风险描述
Beego ORM同样存在直接拼接SQL导致注入的风险。

#### 修复方案
使用参数化查询。

#### 修复示例
```go
// 安全: 使用参数化查询
o.Raw("SELECT * FROM users WHERE username = ?", username).QueryRow(&user)
```
##