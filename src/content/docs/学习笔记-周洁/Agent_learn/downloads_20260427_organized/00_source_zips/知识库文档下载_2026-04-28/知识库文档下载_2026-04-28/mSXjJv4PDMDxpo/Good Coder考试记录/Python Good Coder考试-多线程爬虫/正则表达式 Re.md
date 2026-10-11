---
title: "encoding: UTF-8"
description: "正则表达式 Re"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\正则表达式 Re.md"
---
正则表达式 Re

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 
## 1、语法规则
![](../../../assets/xO1FmWMR5xI2uq/image_001.bin "")
## 2、在python中的使用
### 2.1 简单使用
Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。

```
# encoding: UTF-8
import re
 
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')
 
if match:
    # 使用Match获得分组信息
    print match.group()
 
### 输出 ###
# hello
```
**re.compile(strPattern[, flag]): **

这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。 第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M。

re.**I**(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同） 

**    M**(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图） 

**    S**(DOTALL): 点任意匹配模式，改变'.'的行为 

**    L**(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定 

**    U**(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性 

**    X**(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

re提供了众多模块方法用于完成正则表达式的功能。这些方法可以使用Pattern实例的相应方法替代，但无法复用编译后的Pattern对象。如上面这个例子可以简写为：

```
m = re.match(r'hello', 'hello world!')
print m.group()
```
### 2.2 Match
```
import re
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
 
print "m.string:", m.string  
# 匹配时使用的文本 hello world!
print "m.re:", m.re 
# 匹配时使用的Pattern对象 <_sre.SRE_Pattern object at 0x016E1A38>
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
 
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')
 
### output ###
# m.string: hello world!
# m.re: <_sre.SRE_Pattern object at 0x016E1A38>
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\2 \1\3'): world hello!
```
### 2.3 Pattern
Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。

Pattern不能直接实例化，必须使用re.compile()进行构造。

Pattern提供了几个可读属性用于获取表达式的相关信息：

    pattern: 编译时用的表达式字符串。 

    flags: 编译时用的匹配模式。数字形式。 

    groups: 表达式中分组的数量。 

    groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。

**search **用于查找字符串中可以匹配成功的子串

```
# encoding: UTF-8 
import re 
 
# 将正则表达式编译成Pattern对象 
pattern = re.compile(r'world') 
 
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None 
# 这个例子中使用match()无法成功匹配 
match = pattern.search('hello world!') 
 
if match: 
    # 使用Match获得分组信息 
    print match.group() 
 
### 输出 ### 
# world
```
re.match与re.search的区别：re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

**split** 按照能够匹配的子串将string分割后返回列表

```
import re
 
p = re.compile(r'\d+')
print p.split('one1two2three3four4')
 
### output ###
# ['one', 'two', 'three', 'four', '']
```
**findall** 搜索string，以列表形式返回全部能匹配的子串。

```
import re
 
p = re.compile(r'\d+')
print p.findall('one1two2three3four4')
 
### output ###
# ['1', '2', '3', '4']
```
**finditer** 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。

```
import re
 
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group(),
 
### output ###
# 1 2 3 4
```

