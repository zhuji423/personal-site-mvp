---
title: "图数据库查询 Gremlin"
description: "图数据库查询 Gremlin"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\数据库\\图数据库\\图数据库查询 Gremlin.md"
---
图数据库查询 Gremlin

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
joern是一个C/C++代码分析工具，主要功能是从源码生成抽象语法树，控制流图和程序依赖，合成代码属性图(Code Property Graph)，存入图形数据库neo4j。参考：[joern安装与使用 Mac](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1620980581)

## 一、数据库概述
### 1.1 代码属性图
对于代码库的每个功能，数据库存储一个由以下节点组成的代码属性图。

**函数节点（type: Function）**

为每个函数创建一个节点。函数节点本身只保存函数名称和签名，但是，它可以用来获取函数各自的抽象语法树和控制流图。

**抽象语法树节点（type:various）**

抽象语法树表示代码的句法结构。当需要定位诸如函数调用、赋值或强制转换表达式之类的语言结构时，它们是首选表示。此外，这种分层表示揭示了语言结构如何组合以形成更大的结构。例如，一个语句可能由一个赋值表达式组成，它本身由一个左右值组成，其中右值可能包含一个乘法表达式（有关更多信息，请参阅[维基百科：抽象语法树](http://en.wikipedia.org/wiki/Abstract_syntax_tree)）。抽象语法树节点通过`IS_AST_PARENT_OF`边连接到它们的子节点。此外，相应的功能节点通过`IS_FUNCTION_OF_AST`边连接到 AST 根节点 。

**语句节点（type:various）**

这是抽象语法树节点的子集。语句节点使用`isCFGNode`value属性进行标记 `true`。语句节点通过`FLOWS_TO`和`REACHES`边连接到其他语句节点，分别表示控制流和数据流。

**符号节点（ype:Symbol）**

数据流分析总是针对一个变量进行的。由于即使头文件中包含的声明丢失，我们的模糊解析器也需要工作，因此我们经常会遇到使用*符号*的情况，而该*符号*以前没有被声明过。我们通过为遇到的每个标识符创建*符号*节点来解决这个问题，而不管这个符号的声明是否已知。我们还为后缀表达式引入了符号，例如`a->b`允许我们跟踪结构字段的使用。符号节点使用符号 by `USE`-edges连接到所有语句节点，以及分配给符号（即*定义*符号}）的所有语句节点通过`DEF`-边缘。

各个函数的代码属性图以各种方式链接，以允许从一个函数转换到另一个函数。

### 1.2 全局代码结构
此外，对于为函数创建的节点，源文件层次结构以及全局类型和变量声明如下所示。

**文件和目录节点（type:File/Directory）**

通过为每个文件和目录创建一个节点并使用`IS_PARENT_DIR_OF`和 `IS_FILE_OF`边连接这些节点来公开目录层次结构。此*源代码树*允许通过其在文件系统目录层次结构中的位置来定位代码，例如，这允许您将分析限制为包含在指定子目录中的函数。

**结构/类声明节点（type: Class）**

为通过`IS_FILE_OF`边识别并连接到文件节点的每个结构/类创建一个类节点。类的成员，即属性和方法声明，通过`IS_CLASS_OF`边连接到类节点。

**变量声明节点（type: DeclStmt）**

最后，全局变量的声明保存在声明语句节点中，并使用`IS_FILE_OF`边连接到它们所包含的源文件 。

## 二、图数据库查询
### 2.1 基础知识
图遍历分两步进行，以发现在数据库中搜索感兴趣的子图：

1.**开始节点选择。**所有遍历都从数据库中选择一组节点开始，这些节点作为图中遍历的起点。

2.**走图。**从上一步选择的节点开始，根据节点和边的属性和类型，沿着图边走，到达相邻的节点。遍历的最终目标是确定遍历可以到达的所有节点。可以将图遍历视为必须满足的子图描述才能返回节点。

选择起始节点的最简单方法是根据唯一节点 id 执行查找，如以下查询所示：

```
// 查找具有给定 nodeId 的节点
g.v(nodeId)
```
现在可以通过将所谓的 emph{Gremlin steps} 附加到起始节点来实现遍历图。这些步骤中的每一步都会处理上一步返回的所有节点，类似于 Unix 管道连接 shell 程序的方式。在学习 Gremlin 时，将点运算符视为 unix 管道运算符的别名可能是一个好主意`|`。以下是示例列表。

```
// 遍历到通过出边连接到起始节点的节点
g.v(nodeId).out()

// 遍历两跳以外的节点。
g.v(nodeId).out().out()

// 遍历到通过传入边连接到起始节点的节点
g.v(nodeId).in()

// 由输出 AST 边连接的所有节点（过滤基于边缘类型）
g.v(nodeId).out(AST_EDGE)

// 根据属性过滤：
g.v(nodeId).out().filter{ it.type == typeOfInterest}

// 根据边缘属性过滤
g.v.outE(AST_EDGE).filter{ it.propKey == propValue }.inV()
```
filter函数应用于每个传入节点，并期望返回true或false指示该节点是否应通过过滤操作。给闭包的第一个参数是it按照约定命名的，因此在两个示例中的第一个中it.type表示type传入节点的属性。在第二个示例中，边缘被传递给过滤器例程，因此it.propKey指propKey的是传入边缘的属性 。

### 2.2 开始节点选择
实际上，有趣的起始节点的 id 很少为人所知。相反，起始节点是根据节点属性选择的，例如，人们可能希望选择所有调用memcpy作为起始节点。为了允许基于节点属性进行有效的启动节点选择，我们保留了一个 (Apache Lucene) 节点索引（请参阅[Neo4J 遗留索引](http://docs.neo4j.org/chunked/stable/indexing.html)）。可以使用 Apache Lucene 查询来查询该索引（有关语法的详细信息，请参阅[Lucene 查询语言](http://lucene.apache.org/core/2_9_4/queryparsersyntax.html)）。例如，要检索代表名称包含子字符串 code{cpy} 的被调用者的所有 AST 节点，可以发出以下查询：

```
queryNodeIndex("type:Callee AND name:*cpy*") \end{verbatim}
```
Gremlin 步骤queryNodeIndex在joernsteps/lookup.groovy of 中定义 python-joern。此外 queryNodeIndex，还lookup.groovy定义了用于常见查找的各种函数。刚才给出的例子也可以表述为：

```
getCallsTo("*cpy*")
```
常见的查找操作提供速记，包含在`joernsteps/lookup.groovy`

### 2.3 遍历语法树
在上一节中，我们概述了如何根据节点的属性选择节点。作为[Gremlin 基础](https://joern.readthedocs.io/en/latest/querying.html#gremlin-basics)部分中的大纲，这些选定的节点现在可以用作属性图中游走的起点。

例如，考虑在调用函数的第一个参数中查找所有乘法的任务`malloc`。为了解决这个问题，我们可以先确定所有调用表达式`malloc` ，然后从调用开始遍历语法树中的第一个参数。然后我们确定作为第一个参数的子节点的所有乘法表达式。

原则上，所有这些任务都可以使用[Gremlin 基础](https://joern.readthedocs.io/en/latest/querying.html#gremlin-basics)部分中介绍的基本 Gremlin 遍历来解决。但是，通过引入以下用户定义的 gremlin 步骤（请参阅 参考资料`joernsteps/ast.py`），可以大大简化遍历。

```
// 遍历AST中的父节点
parents()

// 遍历AST中的子节点
children()

// 遍历 AST 中的第 i 个孩子
ithChildren()

// 遍历到封闭语句节点
statements()

// 遍历AST的所有节点
// 以输入节点为根
astNodes()
```
此外，`joernsteps/calls.groovy`介绍了用于遍历调用的用户定义步骤，特别`ithArguments`是遍历给定调用节点的第 i 个参数的步骤 。使用这些步骤，第一个参数内的乘法表达式的示例遍历`malloc`简单地变为：

```
getCallsTo('malloc').ithArguments('0')
.astNodes().filter{ it.type == 'MultiplicativeExpression'}
```
语法说明： 该文件joernsteps/composition.groovy提供了许多基本函数来组合其他遍历和查找函数。这些组合函数允许构建任意的纯语法描述（请参阅[使用代码属性图建模和发现漏洞](http://user.informatik.uni-goettingen.de/~fyamagu/pdfs/2014-oakland.pdf) ）。例如，要选择包含对foo、 bar 的调用的所有函数，可以简单地链接查找函数，例如，

```
getCallsTo('foo').getCallsTo('bar')
```
返回同时调用foo和 bar的函数。同样，调用 code{foo} OR code{bar} 的函数可以选择如下：

```
OR( getCallsTo('foo'), getCallsTo('bar') )
```
最后，not 遍历允许选择所有不匹配遍历的节点。例如，要选择所有调用foo但不调用bar 的函数，请使用以下遍历：

```
getCallsTo('foo').not{ getCallsTo('bar')
```
### 2.4 遍历符号图
如数据库概述部分中所述，通过向函数添加符号节点，语句使用和定义的符号在图形数据库中显式化（参见[使用代码属性图形建模和发现漏洞](http://user.informatik.uni-goettingen.de/~fyamagu/pdfs/2014-oakland.pdf) 附录 D ）。提供实用程序遍历来利用它来确定定义变量的符号，从而简单地访问语句和表达式使用的类型。具体来说，该文件 joernsteps/symbolGraph.groovy包含以下步骤：

```
// 从语句遍历到它使用的符号
uses()
// 从语句遍历到它定义的符号
defines()
// 从语句遍历到定义 它受（赋值和 声明）
definitions()
```
例如，考虑查找memcpy定义为函数参数的所有第三个参数的任务 。这可以使用遍历来实现

```
getArguments('memcpy', '2').definitions()
.filter{it.type == TYPE_PARAMETER}
```
中getArguments定义的查找函数在哪里joernsteps/lookup.py。

作为第二个示例，我们可以遍历所有使用len在第三个参数中命名的符号的函数，该符号memcpy未被函数中的任何条件使用，因此可能不会被检查。

```
getArguments('memcpy', '2').uses()
.filter{it.code == 'len'}
.filter{
        it.in('USES')
        .filter{it.type == 'Condition'}.toList() == []
}
```
这个例子还表明可以在过滤器表达式中执行遍历，并且在任何时候，都可以使用toList 在所有 Gremlin 步骤上定义的函数获得遍历到达的节点列表。

污点风格描述 最后一个示例已经体验了当可以实际跟踪标识符的使用和定义位置时所获得的功能。但是，仅使用增广函数符号图，无法确定一个语句所做的定义实际上会到达另一个语句。为了确保这一点， 需要解决经典的到达定义问题。此外，无法跟踪从定义到语句的过程中是否对变量进行了清理。

joern 允许使用遍历unsanitized来解决这两个问题。例如，考虑这样一种情况：您要查找所有函数，其中第三个参数memcpy 被命名len并作为参数传递给函数，并且存在满足以下两个条件的控制流路径：

begin{itemize} item 变量code{len} 中途没有重新定义。item 变量没有在关系或等式表达式中使用，也就是说，它的数值没有 针对其他变量进行“检查”。结束{itemize}

可以使用以下遍历来实现此目的：

```
getArguments('memcpy', '2')
.sideEffect{ paramName = '.*len.*' }
.filter{ it.code.matches(paramName) }
.unsanitized{ it.isCheck( paramName ) }
.params( paramName )
```
isCheck是在 joerntools/misc.groovy 中定义的遍历，以检查符号是否出现在等式或关系表达式中，并且 code{params} 遍历到与其第一个参数匹配的参数。

请注意，在上面的示例中，我们使用正则表达式来确定包含子字符串的参数，len这里可能需要更精确一些。此外，我们使用 Gremlin 步骤 sideEffect将正则表达式保存在一个变量中，这样我们就不必一遍又一遍地重新键入正则表达式。

---



有关Gremlin语言功能的详细文档，参阅[http://gremlindocs.com](http://gremlindocs.com/)和 [Gremlin 网站](https://github.com/tinkerpop/gremlin/wiki)。
