---
title: "Java sqli 漏洞修复最佳实践"
description: "JAVA SQL 注入漏洞修复知识"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\code-security-comate\\references\\vul_repair-java_sql_injection.md"
---
JAVA SQL 注入漏洞修复知识

# Java sqli 漏洞修复最佳实践
采用先分析漏洞报告->分析数据传递链路->判断是否存在依赖->分析修复方式（判断是否可以修复、使用哪种修复方式）->修复漏洞->验证是否存在语法问题和依赖问题（注意：**不要做与漏洞修复无关的代码改动**）。

## 漏洞分析
### 不可修复场景
1. sql 语句为外部包生成或者传入(例如：request 参数、用户文件上传后读取等)，无法通过当前数据流链路的函数或者源码中找到定义或者生成方法，无法确定 sql 语句的信息，这里作为不可修复场景，不进行漏洞修复。
2. 污点数据以select、update、delete 等子句拼接到 sql 语句时，且无法确定污点数据子句具体信息，为不可修复场景，不进行漏洞修复。
3. 明确的知道传入的数据为表名、列名或列名列表等，表示可修复，参考可修复场景进行修复。

示例：

```java
//sql 从外部 form requestbody 或者 request 请求数据 中直接输入
public StreamingResponseBody queryDataBySql(@RequestBody MetaDataSqlForm form){
    String sql = form.sql; //sql 语句直接通过外部参数传递进来，无法知道 sql 具体内容，所以不能简单的进行过滤修复，返回不可修复
    PreparedStatement stmt = conn.prepareStatement(sql);
}

//Condition 从外部 form requestbody 或者 request 请求数据 中直接输入
public StreamingResponseBody queryDataBySql(@RequestBody MetaDataSqlForm form){
    String whereCondition = form.condition; 
    String sql = "select * from user " + whereCondition; //外部输入了新的子句，但是子句无法知道具体内容，无法通过过滤修复，返回不可修复
    PreparedStatement stmt = conn.prepareStatement(sql);
} 
// 从外部文件输入
public void processFileToSql(MultipartFile file, int recordId) throws Exception {
        String fileContent;
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(file.getInputStream()))) {
            fileContent = reader.lines().collect(Collectors.joining("\n"));
        }
        String sql = fileContent; //sql 语句直接通过外部参数传递进来，无法知道 sql 具体内容，所以不能简单的进行过滤修复，返回不可修复
        PreparedStatement stmt = conn.prepareStatement(sql);
} 
```
### 可修复场景
1. 基于当前数据流代码文件中进行漏洞修复，不要创建新的用于代码过滤的工具类文件，例如：在需要过滤表名列名的情况下，直接在当前 java 文件中建立通用的过滤函数，并在需要过滤的地方使用。（过滤方式参考过滤方式规则）
2. 同个文件进行参数过滤时，可以在文件头定义过滤正则或者过滤函数，如果定义已经存在，直接复用。
3. 当修复需要对**函数签名修改时，需要对函数进行重载**，避免修改函数签名导致原业务编译使用异常。
4. 污点表名、列名、视图名称、DataBase 名称、order 信息、orderby 信息等拼接进入SQL 语句时需要进行过滤的方式修复漏洞。
5. show、create 、drop、grant 语句场景不支持预编译参数方式修复漏洞，需要使用对污点参数进行过滤的方法进行修复。
6. SQL 语句拼接 in 的参数时，需要对其中的每个子项进行过滤或者预编译，如果适合修改成预编译，则**按照参数个数的对 in () 中的内容进行 ? 替换**（**即每个子项均进行参数预编译，NamedParameterJdbcTemplate和**`JPQL`**支持 in (:ids) 的除外**），将每个参数放入查询参数中，优先进行预编译参数绑定。
7. 在 where 语句场景 field 操作符 value，如果 field 或者 操作符为污点信息，则进行过滤，如果 value 为污点数据，则进行预编译操作。
8. 当污点拼接进入 sql 语句时，在分析确认需要通过预编译修复的时候，需要考虑 sql 语句的所在位置，例如有时 sql 语句为全局变量赋值到局部变量，改成预编译执行时，需要将当前函数变更为预编译方式，且需要变更全局 sql 语句为预编译方式，避免遗漏导致用户执行出错。
9. mybatis 场景下，漏洞触发为 xml 文件时，需要通过参数传递链路，从 java 代码文件层面找到合适的位置，对污点参数进行过滤。例如表名、列名、orderby 和 in 等参数场景，无法直接通过将 $ 改为 # 绑定参数或预编译。
10. 对于同一个参数进行漏洞修复时，只需要采取一种修复方式即可，不要同时对一个参数进行预编译、参数绑定和过滤等多种方式。
11. 当污点数据拼接进入到 sql ，需要详细分析当前函数是否还存在其他地方使用了该 sql，避免因为采用预编译修复方案，导致其他使用该 sql 的场景存在异常；如果其他使用的场景在当前文件中，可以统一进行预编译方式修改，得对函数需要重载，保障其他文件调用正常。

#### 过滤方式规则
1、对于需要过滤或者正则校验进行防护的参数在后续使用时为直接拼接或者传递，可以直接通过正则过滤；如果使用的是某个对象的成员或者可迭代对象时，后续直接使用的是『对象.成员函数()』的，**使用临时变量承接过滤函数过滤后的结果, 函数起名以 safeFilter 或者safeValidate 开头（如果不存在需要在当前文件中定义，只有存在的函数才能使用），过滤后使用新的对象进行传递（保障后续数据流检测可以识别到该防护，即用安全的函数截断数据流）**。例如：

```java
//原始代码
       if (CollectionUtils.isNotEmpty(param.getOrgIdList())) {
            sb.append(" AND txf.org_id IN " + SqlUtils.getInSql(param.getOrgIdList())); // 原始代码，param.getOrgIdList() 外部传入的误点参数
        }
....
// 定义过滤函数，返回一个新的 list 对象
    public static List<String> safeFilterOrgIdList(List<String> input) {
        if (input == null) return null;
        Pattern ID_PATTERN = Pattern.compile("^\\d+$");
        return input.stream()
                .filter(item -> item != null && !item.trim().isEmpty()) // 判空
                .filter(item -> ID_PATTERN.matcher(item).matches())    // 正则匹配
                .collect(Collectors.toList());
    }
// 修复后的代码
    if (CollectionUtils.isNotEmpty(param.getOrgIdList())) {
        // 1. 先过滤非法参数
        List<String> cleanList = safeFilterOrgIdList(param.getOrgIdList());
        
        // 2. 只有过滤后仍有值，才拼接 SQL，其他地方使用 param.getOrgIdList()，也需要使用 cleanList
        if (CollectionUtils.isNotEmpty(cleanList)) {
            // 使用清洗后的 cleanList，避免注入风险
            sb.append(" AND txf.org_id IN " + SqlUtils.getInSql(cleanList)); //使用过滤后的参数传递，确保orgid 的传递是通过了清洗函数的，这里的清洗函数为 safeFilterOrgIdList
        }
    }

```
2、如果传入下层函数的为一个对象，有污点的是其中一个属性，使用过滤函数过滤整个对象，**函数起名以 safeFilter 或者safeValidate 开头，并通过临时变量承接过滤函数产生的过滤后的对象，使用临时对象向下层调用传递**。例如：

```java
//原始代码
       if (CollectionUtils.isNotEmpty(param.getOrgIdList())) {
            return xxx.selectOrg(param);
        }
....
// 定义过滤函数，返回一个新的 CourseQuery 对象，用安全的函数截断数据流
    public static CourseQuery safeFilterOrgIdList(CourseQuery param) {
        if (param == null) return null;
        Pattern ID_PATTERN = Pattern.compile("^\\d+$");
        for (String item : param.getOrgIdList()) {
            if (item != null && !ID_PATTERN.matcher(item).matches()) {
                throw new IllegalArgumentException("Invalid OrgIdList contains invalid item: " + item);
            }
        }
        return param;
    }
// 修复后的代码
       if (CollectionUtils.isNotEmpty(param.getOrgIdList())) {
            CourseQuery tmpParam = safeFilterOrgIdList(param); //通过 safeFilterOrgIdList 函数过滤
            return xxx.selectOrg(tmpParam); // 向下传递过滤后的
        }

```
3、**MyBatis/ORM 场景下对象属性过滤的特殊处理**：当污点数据通过对象属性传递到 MyBatis XML（如 `${page.orderBy}`、`${entity.tableName}` 等）时，需要根据赋值和读取方式选择正确的过滤位置：

|赋值方式|读取方式|过滤位置|
|-|-|-|
|调用 setter|MyBatis `${obj.field}` 隐式访问|**setter 中过滤**|
|调用 setter|代码显式调用 getter|**setter 和 getter 都过滤**|
|构造函数/反射赋值|代码显式调用 getter|**getter 中过滤**（构造函数也建议加）|
|构造函数/反射赋值|MyBatis `${obj.field}` 隐式访问|**构造函数中过滤**|

**原理说明**：静态分析器存在两个追踪限制：

1. **隐式调用不可见**：无法追踪 MyBatis OGNL 表达式对 getter 的隐式调用（如 `${obj.field}`），因此 getter 中的过滤对 MyBatis 隐式访问无效，必须在 setter/构造函数等赋值入口过滤。
2. **对象级污点追踪**：当整个对象被标记为污点（如 Spring Controller 的 `@RequestBody` 参数），即使 setter 中已对某个字段做了过滤，后续通过显式 getter 调用获取该字段时，分析器仍可能因对象级污点而认为返回值是污点。此时需要在 getter 中也加过滤，让分析器在追踪 getter 方法体时命中清洗规则。

**最佳实践：在 setter 和 getter 中同时过滤**，确保无论是 MyBatis 隐式访问还是代码显式调用 getter，都能被静态分析器识别到防护措施。构造函数中如有直接赋值也需过滤。

**示例1：setter 赋值 + MyBatis 隐式访问 / 显式 getter 调用（setter 和 getter 都过滤）**

```java
// 原始代码（有漏洞）
public class Page<T> {
    private String orderBy;
    
    public void setOrderBy(String orderBy) {
        this.orderBy = orderBy;  // 未过滤，MyBatis ${page.orderBy} 访问时有注入风险
    }
    
    public String getOrderBy() {
        return orderBy;  // 未过滤，显式调用时对象级污点会穿透
    }
}

// 修复后（setter 和 getter 都过滤）
public class Page<T> {
    private String orderBy;
    private static final Pattern SAFE_PATTERN = Pattern.compile("^(\\*|((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+))*))$");
    
    private static String safeFilterOrderBy(String input) {
        if (input == null || input.isEmpty()) return "";
        if (!SAFE_PATTERN.matcher(input).matches()) return "";
        return input;
    }
    
    public void setOrderBy(String orderBy) {
        this.orderBy = safeFilterOrderBy(orderBy);  // setter 过滤：覆盖 MyBatis 隐式访问场景
    }
    
    public String getOrderBy() {
        return safeFilterOrderBy(orderBy);  // getter 过滤：覆盖代码显式调用 getter 时对象级污点场景
    }
}
```
**示例2：构造函数赋值 + 显式 getter 调用（构造函数、setter、getter 都过滤）**

```java
// 原始代码（有漏洞）
public class Page<T> {
    private String orderBy;
    
    public Page(HttpServletRequest request) {
        this.orderBy = request.getParameter("orderBy");  // 构造函数直接赋值，未过滤
    }
}

// 修复后（所有入口和出口都过滤）
public class Page<T> {
    private String orderBy;
    private static final Pattern SAFE_PATTERN = Pattern.compile("^(\\*|((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+))*))$");
    
    private static String safeFilterOrderBy(String input) {
        if (input == null || input.isEmpty()) return "";
        if (!SAFE_PATTERN.matcher(input).matches()) return "";
        return input;
    }
    
    public Page(HttpServletRequest request) {
        this.orderBy = safeFilterOrderBy(request.getParameter("orderBy"));  // 构造函数中过滤
    }
    
    public void setOrderBy(String orderBy) {
        this.orderBy = safeFilterOrderBy(orderBy);  // setter 过滤：覆盖 MyBatis 隐式访问场景
    }
    
    public String getOrderBy() {
        return safeFilterOrderBy(orderBy);  // getter 过滤：覆盖显式调用时对象级污点场景
    }
}
```
**注意**：这种模式适用于所有通过 ORM/模板引擎（MyBatis、Hibernate、Freemarker 等）访问的对象属性。setter 和 getter 都加过滤虽然看似冗余，但因为静态分析器的两种限制（隐式调用不可见 + 对象级污点追踪），这是确保所有场景都能被识别到防护的最可靠方式。

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

```java
import java.util.regex.Pattern;
import java.util.Set;

// 定义过滤函数
public static String safeFilterSelect(String select, Set<String> allowedColumns) {
    // 1. 先 trim() 去除首尾空白
    select = select.trim();
    // 2. 正则验证格式（支持引用符）
    String regex = "^(\\*|((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+))*))$";
    if (!select.matches(regex)) {
        return null; // 或抛出异常
    }
    // 3. 如果是通配符 *，直接允许
    if ("*".equals(select)) {
        return select;
    }
    // 4. 提取列名并验证白名单
    String[] parts = select.split("\\s*,\\s*");
    for (String part : parts) {
        // 去除引用符
        String cleanPart = part.replaceAll("^[`\"]|[`\"]$", "");
        // 处理表名.列名格式，提取列名部分
        String column = cleanPart.contains(".") ? cleanPart.substring(cleanPart.lastIndexOf(".") + 1) : cleanPart;
        // 白名单验证（如果白名单不完整，跳过此步仅使用正则）
        if (allowedColumns != null && !allowedColumns.isEmpty()) {
            if (!allowedColumns.contains(column.toLowerCase().trim())) {
                return null; // 或抛出异常
            }
        }
    }
    return select;
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

```java
import java.util.regex.Pattern;
import java.util.Set;

// 定义过滤函数
public static String safeFilterIdentifier(String identifier, Set<String> allowedIdentifiers) {
    // 1. 先 trim() 去除首尾空白
    identifier = identifier.trim();
    // 2. 正则验证格式（支持引用符）
    String regex = "^[A-Za-z_][A-Za-z0-9_]{0,127}$|^`[^`]{1,128}`$|^\"[^\"]{1,128}\"$|^\\[[^\\]]{1,128}\\]$";
    if (!identifier.matches(regex)) {
        return null; // 或抛出异常
    }
    // 3. 去除引用符
    String cleanIdentifier = identifier.replaceAll("^[`\"\\[]|[`\"\\]]$", "");
    // 4. 白名单验证（如果白名单不完整，跳过此步仅使用正则）
    if (allowedIdentifiers != null && !allowedIdentifiers.isEmpty()) {
        if (!allowedIdentifiers.contains(cleanIdentifier.toLowerCase())) {
            return null; // 或抛出异常
        }
    }
    return identifier;
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

```java
import java.util.regex.Pattern;
import java.util.Set;

// 定义过滤函数
public static String safeFilterOrderBy(String order, Set<String> allowedColumns) {
    // 1. 正则验证格式（不区分大小写）
    String regex = "^((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(\\s+(ASC|DESC))?(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(\\s+(ASC|DESC))?)*)$";
    Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
    if (!pattern.matcher(order).matches()) {
        return null; // 或抛出异常
    }
    // 2. 提取列名并验证白名单
    String[] parts = order.split("\\s*,\\s*");
    for (String part : parts) {
        // 提取列名部分（处理表名.列名格式）
        String columnPart = part.split("\\s+")[0];
        // 去除引用符
        String cleanPart = columnPart.replaceAll("^[`\"]|[`\"]$", "");
        String column = cleanPart.contains(".") ? cleanPart.substring(cleanPart.lastIndexOf(".") + 1) : cleanPart;
        // 白名单验证（如果白名单不完整，跳过此步仅使用正则）
        if (allowedColumns != null && !allowedColumns.isEmpty()) {
            if (!allowedColumns.contains(column.toLowerCase())) {
                return null; // 或抛出异常
            }
        }
    }
    return order;
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

```java
import java.util.Set;

// 定义过滤函数
public static String safeFilterGroupBy(String group, Set<String> allowedColumns) {
    // 1. 正则验证格式
    String regex = "^((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+))*)$";
    if (!group.matches(regex)) {
        return null; // 或抛出异常
    }
    // 2. 提取列名并验证白名单
    String[] parts = group.split("\\s*,\\s*");
    for (String part : parts) {
        // 去除引用符
        String cleanPart = part.replaceAll("^[`\"]|[`\"]$", "");
        // 提取列名部分（处理表名.列名格式）
        String column = cleanPart.contains(".") ? cleanPart.substring(cleanPart.lastIndexOf(".") + 1) : cleanPart;
        // 白名单验证（如果白名单不完整，跳过此步仅使用正则）
        if (allowedColumns != null && !allowedColumns.isEmpty()) {
            if (!allowedColumns.contains(column.toLowerCase().trim())) {
                return null; // 或抛出异常
            }
        }
    }
    return group;
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

```java
// 定义过滤函数
public static String safeFilterLimit(String limit) {
    // 1. 先 trim() 去除首尾空白
    limit = limit.trim();
    // 2. 正则验证纯数字
    if (limit.matches("^\\d+\\s*,\\s*\\d+$|^\\d+$")) {
        return limit;
    }
    return null; // 或抛出异常
}
```
---

###### 6. WHERE 条件 `__WHERE_FILTER__`
**适用场景**：WHERE 子句、条件判断

**策略**：**放弃正则，使用参数化查询**

**AI 修复指引**：

```java
// ❌ 错误：字符串拼接
String sql = "SELECT * FROM users WHERE name = '" + name + "'";

// ✅ 正确：参数化查询（MySQL/SQLite 使用 ?）
String sql = "SELECT * FROM users WHERE name = ?";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setString(1, name);

// ✅ 正确：参数化查询（PostgreSQL 使用 $1, $2）
String sql = "SELECT * FROM users WHERE name = $1";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setString(1, name);

// ✅ 正确：参数化查询（SQL Server 使用 @param）
String sql = "SELECT * FROM users WHERE name = @name";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setString("@name", name);
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

```java
// ✅ 优先：参数化查询（MySQL/SQLite 使用 ?）
String sql = "SELECT * FROM users WHERE id IN (?, ?, ?)";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setInt(1, id1);
stmt.setInt(2, id2);
stmt.setInt(3, id3);

// ✅ 优先：参数化查询（PostgreSQL 使用 $1, $2）
String sql = "SELECT * FROM users WHERE id IN ($1, $2, $3)";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setInt(1, id1);
stmt.setInt(2, id2);
stmt.setInt(3, id3);

// ⚠️ 备选：严格正则验证（仅当无法参数化时）
String inClause = inClause.trim();
if (!inClause.matches("^\\(\\s*\\d+(\\s*,\\s*\\d+)*\\s*\\)$")) {
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

```java
import java.util.regex.Pattern;

// 定义过滤函数
public static String safeFilterDirection(String direction) {
    // 正则验证（不区分大小写）
    Pattern pattern = Pattern.compile("^(asc|desc)$", Pattern.CASE_INSENSITIVE);
    if (pattern.matcher(direction).matches()) {
        return direction.toUpperCase();
    }
    return null; // 或抛出异常
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

```java
// 定义过滤函数
public static String safeFilterSimpleIdentifier(String identifier) {
    if (identifier.matches("^[\\w-]+$")) {
        return identifier;
    }
    return null; // 或抛出异常
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

```java
// 定义过滤函数
public static String safeFilterPath(String path) {
    if (path.matches("^[\\w/-]+$")) {
        return path;
    }
    return null; // 或抛出异常
}
```
---

###### 11. 运算符 `__OP_FILTER__`
**适用场景**：算术运算符（如 `score+1`）

**正则**：`[+\-*/%]`

**支持格式**：

* `+` `-` `*` `/` `%` （基本算术运算符）

**AI 修复指引**：

```java
// 定义过滤函数
public static String safeFilterOperator(String operator) {
    if (operator.matches("^[+\\-*/%]$")) {
        return operator;
    }
    return null; // 或抛出异常
}
```
---

###### 正则速查表
|过滤器|正则|说明|
|-|-|-|
|`__IDENTIFIER_FILTER__`|`^[A-Za-z_][A-Za-z0-9_]{0,127}$\|^`[^`]{1,128}`$\|^"[^"]{1,128}"$`|SQL 标识符，支持反引号/双引号，1-128字符|
|`__SELECT_FILTER__`|`^(\*\|((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+))*))$`|允许通配符 `*` 和逗号分隔的列名|
|`__ORDER_FILTER__`|`^((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(\s+(ASC\|DESC))?(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(\s+(ASC\|DESC))?)*)$`|列名 + 方向关键字（不区分大小写）|
|`__GROUP_FILTER__`|`^((`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+)(,\s*(`[^`]+`\|"[^"]+"\|\w+\.\w+\|\w+))*)$`|多列，逗号分隔|
|`__LIMIT_FILTER__`|`^\d+\s*,\s*\d+$\|^\d+$`|纯数字，允许逗号|
|`__WHERE_FILTER__`|**参数化查询**|不要用正则|
|`__IN_FILTER__`|`^\(\s*\d+(\s*,\s*\d+)*\s*\)$`|数字列表|
|`__DIRECTION_FILTER__`|`^(asc\|desc)$`|ASC 或 DESC（不区分大小写）|
|`__W_FILTER__`|`^[\w-]+$`|字母数字+下划线+连字符|
|`__PATH_FILTER__`|`^[\w/-]+$`|路径字符|
|`__OP_FILTER__`|`^[+\-*/%]$`|算术运算符|

**Java 正则使用注意事项**：
```java
// 1. Java 字符串中反斜杠需要双重转义
String regex = "^\\w+$";  // 匹配 \w+

// 2. String.matches() 不支持传入 Pattern 标志，需使用 Pattern.compile()
// 错误写法：
// str.matches(regex, Pattern.CASE_INSENSITIVE);  // 编译错误！
// 正确写法：
Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
boolean matched = pattern.matcher(str).matches();

// 3. 反引号 ` 在 Java 正则中不需要转义
String regex = "^`[^`]+`$";  // 匹配反引号包裹的标识符
```

---

###### 重要提示
1. **所有正则验证前，务必先 **`trim()`** 去除首尾空白字符**
2. **白名单优先**：列名/表名等固定值优先用白名单
3. **白名单不完整时降级**：当白名单获取困难或不完整时，使用严格正则作为安全底线
4. **参数化优先**：WHERE 条件、IN 子句优先用参数化查询
5. **数据库适配**：根据使用的数据库类型选择对应的引用符和参数占位符
6. **最小化改动**：只修复漏洞点，不重构其他代码

### 修复后的检查点
1. 检查补丁代码其中参数是否在当前函数范围。
2. 检查补丁代码是否存在语法异常问题，例如正则中引号转义失败，导致非预期字符串闭合问题。
3. 检查补丁代码是否影响其他调用场景使用。

## 修复示例
以下是针对 SQL 注入漏洞在不同场景下的详细整理，包括常见 Java 框架（如 MyBatis、JDBC、Hibernate 等）中的注入风险及其示例：

---

### 1. **JDBC 拼接 SQL 语句**
* **场景**：动态拼接条件时未使用参数化查询，且原始 sql 为全局定义。
* **示例**：

```java
public class TestServiceImp implements TestService {

    /**
     * 周期营销数据,总和表
     */
    private static final String QUERY_SQL =
            "select id,uid,name from user_table where uid = '%s' and tid in (%s)";
    private static final String QUERY_SQL_ALL =
            "select * from user_table where uid = '%s' and tid in (%s)";
            
    private List<ScheduleReportDTO> getData(String uId, List<String> tId) {
        String queryReady;
        if (isAll) {
            queryReady = QUERY_SQL_ALL;
        else{
            queryReady = QUERY_SQL;
        }
        String queryReadySQL = String.format(queryReady, uId, StringUtils.join(tId, ","));
        resultSet = statement.executeQuery(queryReadySQL);
        List<ScheduleReportDTO> remindReportDataList = new ArrayList<>();
        //获取返回结果
        return remindReportDataList;
    }
}
```
* **风险**：用户输入的 uId 参数会导致 SQL 注入，tId 也是用户输入的，是List<String> 类型，可能也会导致 SQL 注入，如果这里 tId 为List<long>等情况，则tId不存在注入风险，不用修复。另外， sql 语句在全局变量定义，修复时需要考虑修改全局变量定义的 sql 语句。
* **修复**：条件直使用 PreparedStatement 动态绑定参数，同时需要对 sql 语句的源头QUERY_SQL_ALL 和 QUERY_SQL 两个全局变量进行修改，使其支持预编译：

```java
public class TestServiceImp implements TestService {

    /**
     * 周期营销数据,总和表
     */
    private static final String QUERY_SQL =
            "select id,uid,name from user_table where uid = ? and tid in (%s)";
    private static final String QUERY_SQL_ALL =
            "select * from user_table where uid = ? and tid in (%s)";
            
    private List<ScheduleReportDTO> getData(String uid, List<String> tId) {
        String queryReady;
        if (isAll) {
            queryReady = QUERY_SQL_ALL;
        } else {
            queryReady = QUERY_SQL;
        }
        String queryReadySQL = String.format(queryReady, String.join(",", Collections.nCopies(tId.size(), "?")));
        PreparedStatement pstmt = connection.prepareStatement(queryReadySQL);
        pstmt.setString(1, uid);
        for (int i = 0; i < tId.size(); i++) {
            pstmt.setString(i + 2, tId.get(i));
        }
        resultSet = pstmt.executeQuery();
        List<ScheduleReportDTO> remindReportDataList = new ArrayList<>();
        //获取返回结果
        return remindReportDataList;
    }
}
```
---

### 2. **MyBatis 使用 **`$`** 传递动态表名、列名、orderby 等**
* **场景**：MyBatis 中使用 `$` 符号直接拼接用户输入到 SQL 语句中。
* **示例**：

```xml
<select id="getUserByName" resultType="User">
    SELECT * FROM ${tableName} WHERE username = ${username} order by ${order}
</select>
```
* 若用户传入 `tableName = users; DROP TABLE users;`、`username = zhangsan; DROP TABLE users;`或者 `order = order; DROP TABLE users;`，会导致 SQL 注入。
* **风险**：`$` 符号直接拼接字符串，不进行参数化处理。
* **修复**：
    * 避免使用 `$` 传递动态表名、列名或者排序条件等。
    * 在 java 代码层面进行参数过滤，例如：


```java
if (!tableName.matches("^(\\*|((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+))*))$")) {
    throw new IllegalArgumentException("Invalid tableName");
}
if (!order.matches("^((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(\\s+(ASC|DESC))?(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(\\s+(ASC|DESC))?)*)$")) {
    throw new IllegalArgumentException("Invalid order");
}
```
```
* 使用 `#` 绑定参数传递普通值, 例如，这里的${username} 改为 #{username} 。
```
```java
<select id="getUserByName" resultType="User">
    SELECT * FROM ${tableName} WHERE username = #{username} order by ${order}
</select>
```
---

### 3. **Hibernate 拼接 HQL 查询**
* **场景**：在 Hibernate 中直接拼接用户输入到 HQL 查询中。
* **示例**：

```java
String username = request.getParameter("username");
String hql = "FROM User WHERE username = '" + username + "'";
Query query = session.createQuery(hql);
List<User> users = query.list();
```
* **风险**：用户输入 `' OR '1'='1` 会导致 SQL 注入（HQL 注入）。
* **修复**：使用命名参数绑定：

```java
String hql = "FROM User WHERE username = :username";
Query query = session.createQuery(hql);
query.setParameter("username", username);
List<User> users = query.list();
```
---

### 4. **Spring Data JPA 动态查询**
* **场景**：使用 `@Query` 注解或原生 SQL 查询时，直接拼接用户输入。
* **示例**：

```java
@Query(value = "SELECT * FROM users WHERE username = '" + username + "'", nativeQuery = true)
List<User> findByUsernameNative(String username);

```
* **风险**：使用原生 SQL 拼接则存在SQL 注入。
* **修复**：使用命名参数绑定：

```java
@Query("SELECT u FROM User u WHERE u.username = :username")
List<User> findByUsername(@Param("username") String username);
```
---

### 5. **存储过程调用传递动态参数**
* **场景**：在调用存储过程时，直接拼接用户输入到参数中。
* **示例**：

```java
String username = request.getParameter("username");
CallableStatement cstmt = connection.prepareCall("{CALL getUser(?)}");
cstmt.setString(1, "'" + username + "'"); // 直接拼接用户输入
ResultSet rs = cstmt.executeQuery();
```
* **风险**：用户输入 `'; DROP TABLE users; --` 会导致 SQL 注入。
* **修复**：使用参数化调用：

```java
CallableStatement cstmt = connection.prepareCall("{CALL getUser(?)}");
cstmt.setString(1, username); // 参数化传递
ResultSet rs = cstmt.executeQuery();
```
---

### 6. **ORM 框架的动态查询（如 JPA Criteria API）**
* **场景**：在 ORM 框架中使用动态查询时，未正确验证用户输入。
* **示例**：

```java
CriteriaBuilder cb = entityManager.getCriteriaBuilder();
CriteriaQuery<User> cq = cb.createQuery(User.class);
Root<User> user = cq.from(User.class);
cq.where(cb.equal(user.get("username"), username)); // 假设 username 未验证
List<User> users = entityManager.createQuery(cq).getResultList();
```
* **风险**：若 `username` 未验证，可能被恶意构造。
* **修复**：确保用户输入经过验证，避免直接使用未经验证的输入。

```java
CriteriaBuilder cb = entityManager.getCriteriaBuilder();
CriteriaQuery<User> cq = cb.createQuery(User.class);
Root<User> user = cq.from(User.class);
if (!username.matches("^[A-Za-z_][A-Za-z0-9_]{0,127}$")) {
    throw new IllegalArgumentException("Invalid username");
}
cq.where(cb.equal(user.get("username"), username));
List<User> users = entityManager.createQuery(cq).getResultList();
```
---

### 7. **组合条件查询中的动态拼接1**
* **场景**：在复杂查询中，动态拼接多个条件时未使用参数化查询。
* **示例**：

```java
String baseQuery = "SELECT * FROM users WHERE 1=1";
if (username != null) {
    baseQuery += " AND username = '" + username + "'";
}
if (email != null) {
    baseQuery += " AND email = '" + email + "'";
}
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(baseQuery);
```
* **风险**：用户输入 `'; DROP TABLE users; --` 会导致 SQL 注入。
* **修复**：使用 `PreparedStatement` 动态绑定参数：

```java
StringBuilder sb = new StringBuilder("SELECT * FROM users WHERE 1=1");
List<Object> params = new ArrayList<>();
if (username != null) {
    sb.append(" AND username = ?");
    params.add(username);
}
if (email != null) {
    sb.append(" AND email = ?");
    params.add(email);
}
PreparedStatement pstmt = connection.prepareStatement(sb.toString());
for (int i = 0; i < params.size(); i++) {
    pstmt.setObject(i + 1, params.get(i));
}
ResultSet rs = pstmt.executeQuery();
```
---

### 8. **组合条件查询中的动态拼接2**
* **场景**：在复杂查询中，动态拼接多个条件时未使用参数化查询，动态拼接表名列名未进行过滤。
* **示例**：

```java
String baseQuery = "SELECT id,username,email," + addr + " FROM " + userTable + " WHERE 1=1";
if (username != null) {
    baseQuery += " AND username = '" + username + "'";
}
if (email != null) {
    baseQuery += " AND email = '" + email + "'";
}
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(baseQuery);
```
* **风险**：用户输入 `'; DROP TABLE users; --` 会导致 SQL 注入。
* **修复**：对表名、列名进行正则过滤，对条件直使用 `PreparedStatement` 动态绑定参数：

```java
if (!addr.matches("^(\\*|((`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+)(,\\s*(`[^`]+`|\"[^\"]+\"|\\w+\\.\\w+|\\w+))*))$")) {
    throw new IllegalArgumentException("Invalid column addr");
}
if (!userTable.matches("^[A-Za-z_][A-Za-z0-9_]{0,127}$")) {
    throw new IllegalArgumentException("Invalid userTable");
}
StringBuilder sb = new StringBuilder("SELECT id,username,email," + addr + " FROM " + userTable + " WHERE 1=1");
List<Object> params = new ArrayList<>();
if (username != null) {
    sb.append(" AND username = ?");
    params.add(username);
}
if (email != null) {
    sb.append(" AND email = ?");
    params.add(email);
}
PreparedStatement pstmt = connection.prepareStatement(sb.toString());
for (int i = 0; i < params.size(); i++) {
    pstmt.setObject(i + 1, params.get(i));
}
ResultSet rs = pstmt.executeQuery();
```
### 9. **组合条件查询中的动态拼接3**
* **场景**：在复杂查询中，动态拼接条件时未使用参数化查询，且被其他函数使用。
* **示例**：

```java
    @Override
    public Page<Object> queryPageFieldData(String schema, String tableName, String fieldName, String keyword,
                                           OrderType orderType, int currentPage, int pageSize) {
        StringBuilder sqlSb = new StringBuilder();
        sqlSb.append("select distinct ").append(fieldName)
                .append(" from ")
                .append(quoteName(schema)).append(".").append(quoteName(tableName));
        if (StringUtils.isNotEmpty(keyword)) {
            sqlSb.append(" where ").append(quoteName(fieldName)).append(" like '%").append(keyword).append("%'");
        }
        sqlSb.append(" order by ").append(quoteName(fieldName)).append(" ").append(orderType != null ?
                orderType.toString() : "asc");
        String sql = sqlSb.toString();
        log.info("[{}]. queryPageFieldData. sql=[{}]", ThreadLocalUtil.getTraceId(), sql);

        List<Object> result = new ArrayList<>();
        String pageSql = genPageSql(sql, currentPage, pageSize);
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(pageSql)) {
            ResultSetMetaData rsmd = rs.getMetaData();
            while (rs.next()) {
                result.add(rs.getObject(fieldName));
            }
        } catch (SQLException e) {
            throw new ShowException(e);
        }
        int count = queryCount(sql);
        Page page = new Page(count, pageSize, currentPage);
        page.setData(result);
        return page;
    }

    @Override
    public int queryCount(String sql) {
        StringBuilder countSql = new StringBuilder();
        countSql.append("select count(*) as count from (").append(sql).append(") count");
        List<Integer> result = new ArrayList<>();
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(countSql.toString())) {
            while (rs.next()) {
                result.add(rs.getInt("count"));
            }
            return result.get(0);
        } catch (SQLException e) {
            throw new ShowException(e.getMessage());
        }
    }
```
* **风险**：用户输入的 like 参数会导致 SQL 注入，同时sqlSb 在当前函数使用，且被引入到sql变量中，导致风险传递到 queryCount 函数，此时需要考虑queryPageFieldData和queryCount两个函数的风险修复。
* **修复**：条件直使用 `PreparedStatement` 动态绑定参数，同时对queryCount情况也修复，因为使用预编译，所以参数也需要通过函数参数传递，此时通过重载queryCount函数，加入需要传递的参数，并对queryCount中的查询进行预编译改造：

```java
    @Override
    public Page<Object> queryPageFieldData(String schema, String tableName, String fieldName, String keyword,
                                           OrderType orderType, int currentPage, int pageSize) {
        StringBuilder sqlSb = new StringBuilder();
        sqlSb.append("select distinct ").append(fieldName)
                .append(" from ")
                .append(quoteName(schema)).append(".").append(quoteName(tableName));
        String sql;
        List<Object> params = new ArrayList<>();
        if (StringUtils.isNotEmpty(keyword)) {
            sqlSb.append(" where ").append(quoteName(fieldName)).append(" like ?");
            params.add("%" + keyword + "%");
        }
        sqlSb.append(" order by ").append(quoteName(fieldName)).append(" ").append(orderType != null ?
                orderType.toString() : "asc");
        sql = sqlSb.toString();
        log.info("[{}]. queryPageFieldData. sql=[{}]", ThreadLocalUtil.getTraceId(), sql);

        List<Object> result = new ArrayList<>();
        String pageSql = genPageSql(sql, currentPage, pageSize);
        try (PreparedStatement stmt = connection.prepareStatement(pageSql)) {
            for (int i = 0; i < params.size(); i++) {
                stmt.setObject(i + 1, params.get(i));
            }
            try (ResultSet rs = stmt.executeQuery()) {
                ResultSetMetaData rsmd = rs.getMetaData();
                while (rs.next()) {
                    result.add(rs.getObject(fieldName));
                }
            }
        } catch (SQLException e) {
            throw new ShowException(e);
        }
        int count = queryCount(sql, params);
        Page page = new Page(count, pageSize, currentPage);
        page.setData(result);
        return page;
    }

    @Override
    public int queryCount(String sql, List<Object> params) {
        StringBuilder countSql = new StringBuilder();
        countSql.append("select count(*) as count from (").append(sql).append(") count");
        List<Integer> result = new ArrayList<>();
        try (PreparedStatement stmt = connection.prepareStatement(countSql.toString())) {
            for (int i = 0; i < params.size(); i++) {
                stmt.setObject(i + 1, params.get(i));
            }
            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    result.add(rs.getInt("count"));
                }
                return result.get(0);
            }
        } catch (SQLException e) {
            throw new ShowException(e.getMessage());
        }
    }
    
    @Override
    public int queryCount(String sql) {
        return queryCount(sql, Collections.emptyList());
    }
```
---