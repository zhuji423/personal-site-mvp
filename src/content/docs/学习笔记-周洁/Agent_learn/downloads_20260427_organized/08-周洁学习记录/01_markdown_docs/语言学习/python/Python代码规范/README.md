---
title: "代码风格规范"
description: "Python代码规范"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\语言学习\\python\\Python代码规范\\README.md"
---
Python代码规范

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
# 代码风格规范
## 程序规模
`每行不超过120字符` 解决：分两个字符串，py会自动join

`函数长度不超过120行`

## 语句
`禁止以分号结束` `一行只能写一句`

## 括号
除了表达式优先级、tuple、隐式链接 尽量避免

## 缩进
`4个空格缩进，禁用tab` `单行拆成多行，要么与首行对齐，要么第二行起缩进4空格`

foo = long_fun_name(var_one, var_two,
                    var_three, var_four)


## 空行
`类或全局函数间隔2空行，类方法隔1空行`

## 空格
`{},(),[]内侧不加空格`

`参数列表，索引，切片左括号前不加空格`

`,:;前不加空格，后面加1空格`

`二元运算符前后加1空格`

`关键字参数或参数默认值里的等号前后不加空格`

## 注释
`文件必须有文件声明`

"""
Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
XXXXXX训练模型入口


Authors: zhoujie19(zhoujie19@baidu.com)
Date:    2020/07/14 19:33:07
"""


`使用docstring描述模块、类、函数和method接口，docstring使用3个引号括起来`

`对外接口必须docstring描述，内部接口看情况`

`docstring描述包括简介、参数、返回值，如果可能抛出异常，需注明`

def get_token_by_usrname_password(usrname, password): 
    """
    get token by usrname and password
    Args:
        username: username
        password: password
    Returns: 
        result: dict()
            result["RESULT"]: success without error
            result["TOKEN"]: icode token
            result["MSG"]: error message
    Raise: 
        ArgsException while args is invaild
    """


# 包引用规范
`禁止from xxx import yyy直接导入`

import os
os.unlink(path)


每行导入一个库 导入库顺序：标准库，第三方库，应用程序自有库，每部分隔1行

# 定义变量
`局部变量全小写，_分隔` local_version = "1.1.3"

`全局变量写在文件头`

`常量全大写`

# 函数定义
## 返回值
`返回值个数<=3，多的话用类/namedtuple/dic包装`

## 默认参数
`仅可使用整数、bool、浮点、字符串、None类型常量`

# 类定义
## 命名方式
`函数使用首字母大写驼峰式命名`

## 构造函数
类构造函数应尽量简单，不包含可能失败或复杂的操作

## 成员
`protected成员使用_前缀`

`private成员使用__前缀`

## 类继承
`没有基类的类必须继承自object类`

# 异常
`禁止使用双参数或字符串抛异常`

`自定义异常：定义名为Error继承自Exception的异常基类，其他异常由该Error类派生而来`

`除非重新抛出异常，禁止使用except捕获所有异常`

# good
try:
    data = urllib2.urlopen(req_url)
except urllib2.URLError as ex:
    ···
# bad
try: 
    data = urllib2.urlopen(req_url)
except: 
    ···


`捕获异常，使用as，禁止用，`

# good
try: 
    data = urllib2.urlopen(req_url)
except urllib2.URLError as ex: 
    ···
# bad
try:
    data = urllib2.urlopen(req_url)
except urllib2.URLError, ex: 
    ···


# Python编码惯例
## 让模块可被导入又可执行
`if __name__ == '__main__':`

def main(): 
    print('Doing stuff in module', _name_)

if __name__ == '__main__': 
    print('Executed from the cmd line')
    main()


## 使用in运算符
`if x in items`

# good
if name in name_list: 
    print('True')
# bad
for item in name_list: 
    if name == item: 
    print('True')


## 不使用临时变量调换两个值
## 用序列构建字符串
`''.join(str)`

# good
chars = ['Hello', 'World']
worlds = ''.join(chars)
print worlds
# bad
chars = ['Hello', 'World']
words = ''
for char in chars:
    words += char
print words

