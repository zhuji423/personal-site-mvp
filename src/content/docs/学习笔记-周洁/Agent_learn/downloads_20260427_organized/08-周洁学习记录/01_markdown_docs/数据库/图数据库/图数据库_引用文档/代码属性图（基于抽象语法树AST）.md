---
title: "代码属性图（基于抽象语法树AST）"
description: "代码属性图（基于抽象语法树AST）"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\数据库\\图数据库\\图数据库_引用文档\\代码属性图（基于抽象语法树AST）.md"
---
代码属性图（基于抽象语法树AST）

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 一、背景
代码属性图(Code Property Graph)的论文： [Modeling and Discovering Vulnerabilities with Code Property Graphs](https://link.zhihu.com/?target=https%3A//fabs.codeminers.org/papers/2014-ieeesp.pdf)

提出了一种有效挖掘大量源代码漏洞的方法。

引入了一种新的源代码表示，称为代码属性图，它将经典程序分析的概念，即抽象语法树、控制流图和程序依赖图，合并成一个联合数据结构。【可以重点参考的部分】

这种全面的表示使能够用图形遍历为常见漏洞优雅地建模模板，例如，可以识别缓冲区溢出、整数溢出、格式字符串漏洞或内存泄露。使用一个流行的图形数据库来实现具体的方法，并通过识别Linux内核源代码中18个以前未知的漏洞来证明它的有效性。

## 二、代码的表示
三种经典表示：抽象语法树、控制流图和程序依赖图

以如下原始代码为例：

```
void foo() 
{
  int x = source();
  if (x < MAX)
  {
    int y = 2 * x;
    sink(y); 
  }
}
```
### AST(抽象语法树)
**构建**：通常是由编译器的代码分析器产生的第一批中间表示，因此构成了许多其他代码表示生成的基础。这些树忠实地编码了如何嵌套语句和表达式来生成程序。

**结构**：抽象语法树是有序树，其中内部节点表示运算符(例如，加法或赋值)，叶节点对应于操作数(例如，常数或标识符)。

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_001.bin "")
**优缺点**：虽然抽象语法树非常适合简单的代码转换，并已被用来识别语义相似的代码，但它们不适用于更进化的代码分析，例如检测未初始化的变量。这种缺陷的原因是，代码的这种表示既没有明确控制流，也没有明确数据依赖关系。

### CFG(控制流程图)
**结构**：控制流图明确描述了代码语句的执行顺序，以及特定执行路径需要满足的条件。语句和谓词由节点表示，节点通过有向边连接，以指示控制权的转移。为每个边分配一个真、假或ϵ的标签：语句节点有一个标记为ϵ的输出边，而谓词节点有两个输出边，分别对应于谓词的真或假评估。

**构建**：通过两个步骤从抽象语法树构建: 首先，考虑结构化控制语句(例如，if、while、for)来构建初步的控制流图。其次，通过额外考虑非结构化控制语句(如goto、break 和continue)来修正初步控制流图。

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_002.bin "")
**优缺点**：控制流图已被用于各种应用安全上下文中的操作，成为逆向工程中的标准代码表示，有助于程序理解。然而，尽管控制流图展示了应用程序的控制流，但它们无法提供数据流信息。特别是对于漏洞分析，这意味着控制流图不能很容易地用于识别处理受攻击者影响的数据的语句。

### PDG(程序依赖图)
**结构**：程序依赖图明确表示语句和谓词之间的依赖关系。特别地，该图使用两种类型的边来构造:反映一个变量对另一个变量的影响的**数据依赖边**和对应于谓词对变量值的影响的**控制依赖边**。

**构建**：通过首先确定定义的变量集和每个语句使用的变量集，并计算每个语句和谓词的到达定义，可以从控制流图计算程序依赖图的边。

**优缺点**：语句的执行顺序不再能从图中确定，而语句和谓词之间的依赖关系是清晰可见的。

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_003.bin "")
## 三、属性图与图遍历
属性图（property graph）是一种结构化数据的基本表示，可以在图形数据库中存储使用（例如ArangoDB, Neo4J, OrientDB）。

### 属性图定义
G = (V, E, λ, μ)是一个有向的、边标记的、属性多重图，其中V是一组节点，E是一组有向边，而 λ:  E→Σ是一个边标记函数，定义每条边的一个标签。

属性可以通过函数

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_004.bin "")
分配给节点，其中K是一组属性键，S是一组属性值。

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_005.bin "")
属性图的示例，分配给节点的属性由虚线表示。具有关键字k ∈ K的属性被分配给每个节点，其中只有节点A和B存储来自集合S{ x，w}的属性值。

在属性图中挖掘信息的主要工具是所谓的图遍历或短遍历，它们可以用来根据标签和属性沿着图的边缘移动。

### 图遍历
遍历是函数

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_006.bin "")
，它根据属性图G将一组节点映射到另一组节点，其中P是V的幂集。这个通用定义允许链接多个遍历一起，使用

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_007.bin "")
表示。基于这种链接，可以定义一些基本遍历，这些基本遍历是本文讨论的所有其他遍历的基础。

#### 过滤器遍历
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_008.bin "")
返回集合X中匹配布尔谓词

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_009.bin "")
的所有节点，例如，通过检查某个属性。

#### 正向遍历
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_010.bin "")
为了沿着属性图的边缘移动，定义了正向遍历：

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_011.bin "")
* 返回从X可到达的所有节点

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_012.bin "")
* 返回在标签为l的边上可到达的所有节点

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_013.bin "")
* 返回在标签为l 的边上可到达的所有属性为k:s节点

#### 后向遍历
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_014.bin "")
类似于正向遍历，定义了后向遍历。

#### 或遍历
或遍历与与遍历用来聚合其他遍历的输出

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_015.bin "")
#### 与遍历
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_016.bin "")
总结：尽管有些技术上的定义，几个图形数据库为这些元素遍历提供了有效的实现。具体来说，FILTER、OUT和In遍历是受流行数据库(如Neo4J和InfiniteGraph)支持的图形语言Gremlin的基本功能。

## 四、代码属性图
抽象语法树、控制流图和程序依赖图都提供了关于源代码的独特视图，强调了底层程序的不同方面。代码属性图CPG将这些视图合并为一个图，提供各个表示的所有优点。

#### 转换抽象语法树
将一个AST表示为属性图

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_017.bin "")
，节点

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_018.bin "")
由树节点给出，而边

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_019.bin "")
是由标记函数

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_020.bin "")
标记为AST边的相应的树边。此外，为每个边通过

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_021.bin "")
分配一个属性code，使得属性值对应于该节点表示的运算符或操作数。最后，为每个节点分配一个属性order，以反映树的有序结构。因此，该图的属性键集合为

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_022.bin "")
，而属性值集合

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_023.bin "")
由所有运算符和操作数以及自然数给出。

#### 转换控制流图
下一步，将CFG 合并到联合表示中。将CFG 表示为属性图

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_024.bin "")
，其中节点

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_025.bin "")
对应于AST中的语句和谓词（也就是所有属性值为STMT 和PRED的

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_018.bin "")
节点）。此外，定义了一个边标记函数

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_027.bin "")
，它将集合

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_028.bin "")
的一个标记分配给属性图中的所有边。

#### 转换程序依赖图
程序依赖图表示语句和谓词之间的数据和控制依赖关系。因此，该图的节点是与CFG的相同，只是两个图的边不同。因此，PDG可以被视为一种通过一组新的边

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_029.bin "")
和相应的边标记函数

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_030.bin "")
:

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_031.bin "")
定义的属性图

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_032.bin "")
， 其中

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_033.bin "")
对应于控制依赖和数据依赖。此外，分配了一个属性符号以指示对应的符号，并向每个控件依赖项提供属性条件，以指示原始谓词的状态为真或假。

#### 组合表示
最后一步，将三个属性图组合成一个联合数据构，称为代码属性图。构建这个图所必需的关键见解是，对于源代码中的每个语句和谓词，在三个图中的每一个图中都存在一个节点。事实上，AST是三种表示中唯一一种引入了额外的节点。语句和谓词节点连接表示并充当从一个表示到另一个表示的转换点。

#### 代码属性图图表示
代码属性图是从源代码的AST、CFG和PDG构造的一种属性图，定义为：

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_034.bin "")
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_035.bin "")
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_036.bin "")
代码属性图示意图

这篇论文主要参考的就是代码属性图的生成与存储查询，后面一个章节举了具体几个代码漏洞的例子，使用代码属性图和人工规则进行漏洞判定，参考意义不大。

## 实验：进行代码分析
#### 静态代码分析工具
用静态代码分析工具：Joern、Codeql

Joern 是ShiftLeft公司开发的用于C/C++代码健壮性分析的平台。其核心思想: 将代码分析问题转化为用Gremlin去遍历存储在Neo4j中的AST，CFG，DFG等属性图。其商业产品 [Ocular](https://link.zhihu.com/?target=https%3A//go.shiftleft.io/ocular-free-trial) 支持多种语言。

补充定义：

AST：abstract syntax tree 抽象语法树 CFG：control flow graph 控制流图（由AST生成） CDG：Control Dependence Graphs 控制依赖图 DDG：Data Dependence Graphs 数据依赖图 PDG：Program Dependence graphs 程序依赖图（由CDG、DDG构成） CPG：Code Property Graphs 代码属性图（由CFG+PDG构成）

#### 示例1：对demo代码进行分析
**demo.cpp**

```
void foo() 
{
  int x = source();
  if (x < MAX)
  {
    int y = 2 * x;
    sink(y); 
  }
}
```
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_037.bin "")
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_038.bin "")
抽象语法树：

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_039.bin "")
程序依赖图：

黄色线条为控制依赖CDG，红色线条为数据依赖DDG，由控制流图CFG+CDG、DDG构成程序依赖图PDG

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_040.bin "")
#### 示例2：使用joern对开源VLC库进行分析
1、下载并导入代码

```
cd $JOERN //joern目录
mkdir tutorial; cd tutorial //创建并转入tutorial
wget http://download.videolan.org/pub/videolan/vlc/2.1.4/vlc-2.1.4.tar.xz //下载vlc源码
tar xfJ vlc-2.1.4.tar.xz //解压
cd .. //返回上一级
./joern tutorial/vlc-2.1.4/  //导入代码
```
2、启动图数据库

```
cd $neo4j/bin
sudo ./neo4j console
```
3、图查询

使用joern-tools来实现节点的查询，-g 参数是指使用Germlin语言查询。首先使用Germlin查询检索所有直接连接到根节点的所有节点：

```
echo 'g.v(0).out()' | joern-lookup -g
```
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_041.bin "")
首先是目录，或者说文件夹。n0是第一个文件夹，总目录，也就是vlc-2.1.4，其余的14个分别对应vlc-2.1.4中的14的文件夹。

4、尝试使用joern来获取某个函数的AST,CFG,DFG

**1 查看GetAoutBuffer函数的位置**

```
echo 'getFunctionsByName("GetAoutBuffer").id' | joern-lookup -g | joern-location
```
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_042.bin "")
**2 使用john -plot- ast生成AST 抽象语法树**

如下：

```
echo 'getFunctionsByName("GetAoutBuffer").id' | joern-lookup -g | tail -n 1 | joern-plot-ast > foo.dot
```
显示这个ast图像：

```
dot -Tpng -o foo.png foo.dot
```
GetAoutBuffer函数的抽象语法树：

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_043.bin "")
放大左上角，对于语句

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_044.bin "")
的AST为：

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_045.bin "")
**3 获取该函数的CFG 程序控制流图**

利用 joern-plot-proggraph -cfg 生成CFG的dot文件

```
echo 'getFunctionsByName("GetAoutBuffer").id' | joern-lookup -g | tail -n 1 | joern-plot-proggraph -cfg > cfg.dot
dot -Tpng -o cfg.png cfg.dot
```
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_046.bin "")
上面部分放大后：

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_047.bin "")
**4 获取该函数的PDG 程序依赖图**

利用 joern-plot-proggraph -ddg -cdg -cfg 生成相应的dot文件

```
echo 'getFunctionsByName("GetAoutBuffer").id' | joern-lookup -g | tail -n 1 | joern-plot-proggraph -ddg -cdg -cfg > pdg.dot
dot -Tpng -o pdg.png pdg.dot
```
![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_048.bin "")
放大上方，黄色线条为控制依赖CDG，红色线条为数据依赖DDG，由控制流图CFG+CDG、DDG构成程序依赖图PDG

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_049.bin "")
**5 通过joern获取相应的切片**

观察代码属性图，对于语句

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_050.bin "")
（id为476502），获取p_buf变量的切片：

```
echo 'getFunctionsByName("GetAoutBuffer").id' | joern-lookup -g | tail -n 1 | joern-plot-proggraph -ddg -cdg -cfg | joern-plot-slice 476502 'p_buf' > slice.dot
dot -Tpng -o slice.png slice.dot
```
阴影部分为获取的相关切片

![](../../../../../_remote_images/08-周洁学习记录/local_assets/d4iEAMmMwKp9Qw/image_051.bin "")

