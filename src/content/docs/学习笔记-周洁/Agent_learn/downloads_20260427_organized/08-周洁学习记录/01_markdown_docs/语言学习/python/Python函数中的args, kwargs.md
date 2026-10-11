---
title: "Python函数中的args, kwargs"
description: "Python函数中的args, kwargs"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\语言学习\\python\\Python函数中的args, kwargs.md"
---
Python函数中的*args, **kwargs

在写程序时，不确定将来要往函数中传入多少个参数，即可使用可变参数（即不定长参数），用*args,**kwargs表示：

* *args称之为Non-keyword Variable Arguments，无关键字参数；
* **kwargs称之为keyword Variable Arguments，有关键字参数；

### 1、***args**
当函数中以**列表或者元组**的形式传参时，就要使用***args**

样例代码：

```
def test_args(first, *args):
    print('Required argument: ', first)
    print(type(args))
    for v in args:
        print ('Optional argument: ', v)

test_args(1, 2, 3)
```
输出如下：

```
Required argument:  1
<class 'tuple'>
Optional argument:  2
Optional argument:  3
```
### 2、****kwargs**
当传入**字典**形式的参数时，就要使用****kwargs**

样例代码：

```
def total_fruits(**kwargs):
    print(kwargs, type(kwargs))
total_fruits(banana=5, mango=7, apple=8)
```
输出如下：

```
{'banana': 5, 'mango': 7, 'apple': 8} <class 'dict'>
```

