---
title: "一些python代码规范的应用"
description: "一些python代码规范的应用"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\语言学习\\python\\Python代码规范\\一些python代码规范的应用.md"
---
一些python代码规范的应用

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 默认迭代器和操作符
·[强制] 对容器或文件的只读遍历，应该使用内置的迭代方法，不要使用返回list的方式遍历。

·[强制] [PY013] 对容器类型，使用in或not in判断元素是否存在。而不是has_key。

**解释**

* 可读性和性能更好。例如：file.readlines()会一次性读入文件中所有行，存储到一个list中返回。当文件很大时，性能开销较大
* 当文件或容器较小时，调用返回list的函数也可以接受。请reviewer视具体情况决定是否通过。
* 如果遍历过程中需要对容器进行增删，请使用返回list的方式遍历

**示例**

**YES**

|1 2 3 4 5 6 7 8 9|`for` `key ``in` `adict: ...` `if` `key ``not` `in` `adict: ...` `if` `obj ``in` `alist: ...` `for` `line ``in` `afile: ...` `for` `k, v ``in` `dict``.iteritems(): ...` `# 删除毕业学生` `for` `id` `in` `students.keys():` `    ``if` `students[``id``].graduated:` `        ``del` `students[``id``]`|
|-|-|

## **NO**
|1 2 3 4 5 6 7|`for` `key ``in` `adict.keys(): ...` `if` `not` `adict.has_key(key): ...` `for` `line ``in` `afile.readlines(): ...` `#删除毕业学生` `for` `id` `in` `students:` `    ``if` `students[``id``].graduated:` `        ``del` `students[``id``]      ``# 抛出RuntimeError异常`|
|-|-|

## yield和generator函数
·[建议] 当返回较长列表数据时建议使用yield和generator函数。

**解释**

* 生成器函数可以避免返回大列表，占用过多内存、影响性能。同时还可以保持代码的优雅易读。

**示例** **YES**

|1 2 3 4 5 6 7 8|`#返回n以内的奇数` `def` `odds(n):` `    ``for` `i ``in` `xrange``(``1``, n ``+` `1``):` `        ``if` `i ``%` `2` `=``=` `1``:` `            ``yield` `i`   `for` `i ``in` `odds(``1000``):` `    ``print` `i`|
|-|-|

**NO**

|1 2 3 4 5 6 7 8 9 10|`#返回n以内的奇数` `def` `odds(n):` `    ``ret ``=` `[]` `    ``for` `i ``in` `xrange``(``1``, n ``+` `1``):` `        ``if` `i ``%` `2` `=``=` `1``:` `            ``ret.append(i)` `    ``return` `ret`   `for` `i ``in` `odds(``1000``):` `    ``print` `i`|
|-|-|

```
def cube(n):
    for i in range(n):
        yield i ** 3

for i in cube(5):
    print i

#output
0
1
8
27
64
```



