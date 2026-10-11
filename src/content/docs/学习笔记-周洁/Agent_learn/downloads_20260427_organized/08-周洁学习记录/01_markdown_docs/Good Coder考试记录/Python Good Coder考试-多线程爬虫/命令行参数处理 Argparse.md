---
title: "parser.add_argument(\"-i\", \"--info\", action = \"store\", type = \"string\", dest = \"sample_info\", help = \"the sample informat"
description: "命令行参数处理 Argparse"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\命令行参数处理 Argparse.md"
---
命令行参数处理 Argparse

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
```
import argparse
parser = argparse.ArgumentParser()
# parser.add_argument("-i", "--info", action = "store", type = "string", dest = "sample_info", help = "the sample information")
args = parser.parse_args()
# print(args.sample_info)
```
运行以上代码，如下：

**不输入参数**，也没有输出结果： $ python3 test.py **输入默认参数** --help （也可缩写为 -h ），会输出自动生成的帮助信息： $ python3 test.py --help # 输出：

```
usage: test.py [-h]
optional arguments:
-h, --help show this help message and exit
```
**输入错误参数**，会输出报错信息： $ python3 test.py -verbose # 输出：

```
usage: test.py [-h]
test.py: error: unrecognized arguments: --verbose
```
**1、创建一个新的 ArgumentParser 对象。**

```
import argparseparser = argparse.ArgumentParser(prog=None, usage=None,description=None, 
epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, 
argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)
```
所有的参数都应当作为关键字参数传入。部分参数在下面都有它更详细的描述，但简而言之，它们是：

* prog - 程序的名称（默认：sys.argv[0]）
* usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
* description - 在参数帮助文档之前显示的文本（默认值：无）
* epilog - 在参数帮助文档之后显示的文本（默认值：无）
* parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
* formatter_class - 用于自定义帮助文档输出格式的类
* prefix_chars - 可选参数的前缀字符集合（默认值：'-'）
* fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
* argument_default - 参数的全局默认值（默认值： None）
* conflict_handler - 解决冲突选项的策略（通常是不必要的）
* add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
* allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print args.echo
```
```
$ python prog.py -h
usage: prog.py [-h] echo

positional arguments:
  echo        echo the string you use here

optional arguments:
  -h, --help  show this help message and exit
```
**2、添加参数**

使用 add_argument() 方法添加参数。其中，部分参数在下面都有它更详细的描述，但简而言之，它们是：

* name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
* action - 当参数在命令行中出现时使用的动作基本类型。
* nargs - 命令行参数应当消耗的数目。
* const - 被一些 action 和 nargs 选择所需求的常数。
* default - 当参数未在命令行中出现时使用的值。
* type - 命令行参数应当被转换成的类型。
* choices - 可用的参数的容器。
* required - 此命令行选项是否可省略 （仅选项可用）。
* help - 一个此选项作用的简单描述。
* metavar - 在使用方法消息中使用的参数值示例。
* dest - 被添加到 parse_args() 所返回对象上的属性名。

**3、具体应用**

```
if __name__ == '__main__':
    # 命令行参数处理
    desc = """迷你定向网页抓取器"""
    argparse = argparse.ArgumentParser(prog="mini_spider", description=desc)
    argparse.add_argument("-v",
                          "--version",
                          action="version",
                          version="%(prog)s 1.0",
                          help="显示版本信息")
    argparse.add_argument("-c",
                          "--config",
                          required=True,
                          help="必填选项，输入爬虫配置文件路径")
    args = argparse.parse_args()
    main(args.config)
```

