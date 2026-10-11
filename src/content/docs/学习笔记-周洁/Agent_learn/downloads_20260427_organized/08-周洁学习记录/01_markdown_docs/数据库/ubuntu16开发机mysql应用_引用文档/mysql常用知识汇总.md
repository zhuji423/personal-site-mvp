---
title: "mysql常用知识汇总"
description: "mysql常用知识汇总"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\数据库\\ubuntu16开发机mysql应用_引用文档\\mysql常用知识汇总.md"
---
mysql常用知识汇总

### `EXPLAIN`
EXPLAIN SELECT * FROM table_name WHERE condition; 会返回一个结果集，包含了查询语句的执行计划的相关信息：

|**字段名**|**含义**|**常见取值及解释**|
|-|-|-|
|**id**|查询的执行顺序标识|1：单表查询；多表查询时，id 值越大，优先执行|
|**select_type**|查询类型|SIMPLE：简单查询（无子查询、UNION）； PRIMARY：最外层查询；SUBQUERY：子查询； UNION：UNION 语句的第二个及后续部分|
|**table**|访问的表|tuser：表示查询的表名|
|**type**|访问类型（查询效率）|**ALL**（最差，全表扫描）；**index（全索引扫描）；****range**（索引范围扫描）； **ref**（使用索引查找匹配某个值）；**eq_ref（唯一索引匹配）；** **const/system（常量匹配）；****NULL**（不需要访问表，例如 `COUNT(*)`）|
|**possible_keys**|可能使用的索引|该查询可能会用到的索引列表|
|**key**|实际使用的索引|如果为 `NULL`，说明没使用索引|
|**key_len**|使用索引的字节长度|索引字段的长度，值越短越好|
|**ref**|索引匹配的列|指示 `key` 参与匹配的列|
|**rows**|预计扫描的行数|估算 MySQL 需要读取的行数，值越小越好|
|**filtered**|过滤率|过滤后的数据比例（越高越好）|
|**Extra**|额外信息|`Using index`（覆盖索引）；`Using where`（需要额外过滤）；`Using filesort`（需要额外排序，可能影响性能）； `Using temporary`（使用临时表）|

### 聚合函数
**GROUP BY 和 SELECT 规则**：

当使用 `GROUP BY` 子句时，`SELECT` 语句中的字段必须满足以下条件之一：

    * 出现在 `GROUP BY` 子句中。
    * 使用聚合函数（如 `COUNT()`、`SUM()`、`AVG()`、`MAX()`、`MIN()` 等）。

**不在 **`GROUP BY`** 子句中也不作为聚合函数参数的字段限制**：

* 该类字段在每个分组中必须具有**唯一值**，否则无法确定哪一条记录应该被选中。这种情况在标准SQL中通常不被允许，会导致错误。

```
✅正确示例
SELECT a, MIN(b), COUNT(*) FROM userinfo GROUP BY a;
❎错误示例
SELECT a, b, COUNT(*) FROM userinfo GROUP BY a;
```
### 窗口函数
**场景1：**在学生成绩表中查询每个班级总分第一的学生成绩记录

```
WITH RankedStudents AS (
    SELECT
        student_id,
        student_name,
        class_id,
        score,
        ROW_NUMBER() OVER (PARTITION BY class_id ORDER BY score DESC) AS rn
    FROM
        students
)
SELECT
    student_id,
    student_name,
    class_id,
    score
FROM
    RankedStudents
WHERE
    rn = 1;
```
* `PARTITION BY class_id`：按班级分组排名。
* `ORDER BY score DESC`：按总分降序排序，确保总分最高的学生排名第一。
* `ROW_NUMBER()`：为每个分组生成行号。
* `rn = 1`：筛选总分排名第一的学生。

### 查询分析思路
****




