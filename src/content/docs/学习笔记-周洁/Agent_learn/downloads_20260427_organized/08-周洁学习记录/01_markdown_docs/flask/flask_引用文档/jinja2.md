---
title: "jinja2"
description: "本页面由v姚宇辰于2022/03/02迁移自wiki 周洁空间 jinja2 jinja2是Flask作者开发的一个模板系统，起初是仿django模板的一个模板引擎，为Flask提供模板支持，由于其灵活，快速和安全等优点被广泛使用。"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\flask\\flask_引用文档\\jinja2.md"
---
jinja2

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
# 
# jinja2 
jinja2是Flask作者开发的一个模板系统，起初是仿django模板的一个模板引擎，为Flask提供模板支持，由于其灵活，快速和安全等优点被广泛使用。

# 引入jinja2进行渲染
jinja2模块中有一个名为Enviroment的类，这个类的实例用于存储配置和全局对象，然后从文件系统或其他位置中加载模板。 ```py from jinja2 import Environment, FileSystemLoader env = Environment(loader=FileSystemLoader('./data/html')) #创建一个文件系统加载器 template = env.get_template('template.html') # 获取一个模板文件 template.render(name='daxin',age=18) # 渲染 ``` Environment支持两种加载方式： PackageLoader：包加载器 from jinja2 import PackageLoader,Environment FileSystemLoader：文件系统加载器 from jinja2 import Environment, FileSystemLoader 

# 使用
## 语法
{{ ... }}：装载一个变量，模板渲染的时候，会使用传进来的同名参数这个变量代表的值替换掉。 {% ... %}：装载一个控制语句。 {# ... #}：装载一个注释，模板渲染的时候会忽视这中间的值。

## 变量 {{}}
### **显示**
jinja2支持python中所有的Python数据类型比如列表、字段、对象等。 ``` py <p>this is a dicectory:{{ mydict['key'] }} </p> <p>this is a list:{{ mylist[3] }} </p> <p>this is a object:{{ myobject.something() }} </p> ```

### **在模板中添加变量，可以使用（set）语句。**
```py

{% set name='xx' %} ```

### **局部变量**
使用with创建一个内部作用域，将set语句放在其中，创建的变量只在with代码块中才有效。

```py {% with foo = 42 %} {{ foo }} {% endwith %} ```

## if结构
```py

{% if daxin.safe %} daxin is safe. {% elif daxin.dead %} daxin is dead {% else %} daxin is okay {% endif %} ```

## for循环
jinja2中的for循环用于迭代Python的数据类型，包括列表，元组和字典。在jinja2中不存在while循环。

### **迭代列表**
```py <ul> {% for user in users %} <li>{{ user.username|title }}</li> {% endfor %} </ul> ```

### **迭代字典**
```py <dl> {% for key, value in my_dict.iteritems() %} <dt>{{ key }}</dt> <dd>{{ value}}</dd> {% endfor %} </dl> ```

### **在循环中加入else**
```py

<ul> {% for user in users %} <li>{{ user.username|e }}</li> {% else %} <li><em>no users found</em></li> {% endfor %} </ul> ``` 注：不可以使用continue和break表达式来控制循环的执行 Jinja2中for循环内置常量：

|loop.index|当前迭代的索引（从1开始）|
|-|-|
|loop.index0|当前迭代的索引（从0开始）|
|loop.first|是否是第一次迭代，返回True/False|
|loop.last|是否是最后一次迭代，返回True/False|
|loop.length|序列的长度|

## 特殊运算符
\*\*号运算符：次幂运算符，比如2**3=8。 in操作符：跟python中的in一样使用，比如{{1 in [1,2,3]}}返回true。 ~号运算符：拼接多个字符串，比如{{"Hello" ~ "World"}}将返回HelloWorld。

## 过滤器
|过滤器名称|说明|
|-|-|
|safe|渲染时值不转义|
|capitialize|把值的首字母转换成大写|
|lower|把值转换成小写形式|
|upper|把值转换成大写形式|
|title|把值中每个单词的首字母都转换成大写|
|trim|把值的首尾空格去掉|
|striptags|渲染之前把值中所有的HTML标签都删掉|
|join|拼接多个值为字符串|
|replace|替换字符串的值|
|round|默认对数字进行四舍五入，也可以用参数进行控制|
|int|把值转换成整型|

多个过滤器可以链式调用，前一个过滤器的输出会作为后一个过滤器的输入。 ```py {{ 'abc' | captialize }} # Abc {{ 'abc' | upper }} # ABC {{ 'hello world' | title }} # Hello World {{ "hello world" | replace('world','daxin') | upper }} # HELLO DAXIN {{ 18.18 | round | int }} # 18 ```

## 宏
宏类似于Python中的函数 在宏中定义一个宏的关键字是macro，后面跟宏的名称和参数等 ```py {% macro input(name,age=18) %} # 参数age的默认值为18 <input type='text' name="{{ name }}" value="{{ age }}" > {% endmacro %} ``` 调用方法 ```py <p>{{ input('daxin') }} </p> <p>{{ input('daxin',age=20) }} </p> ```
