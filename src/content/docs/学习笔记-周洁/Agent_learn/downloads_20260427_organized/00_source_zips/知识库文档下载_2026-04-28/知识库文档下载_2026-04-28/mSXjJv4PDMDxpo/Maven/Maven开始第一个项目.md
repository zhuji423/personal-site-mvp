---
title: "Maven开始第一个项目"
description: "Maven开始第一个项目"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Maven\\Maven开始第一个项目.md"
---
Maven开始第一个项目

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间

## 一、背景
### 1.1 简介
Spark是加州大学伯克利分校AMP实验室开发的通用大数据处理框架。其生态系统也称为BDAS，力图在算法（Algorithms）、机器（Machines）和人（People）三者之间通过大规模集成来展现大数据应用的一个开源平台。

Spark使用Scala语言进行实现，它是一种面向对象、函数式编程语言，能够像操作本地集合对象一样轻松地操作分布式数据集。Spark具有运行速度快、易用性好、通用性强和随处运行等特点。

* 运行速度快：Spark基于内存计算，相对于Hadoop性能提高了几十倍，而其主要原因正是因为Spark基于内存计算和引入DAG执行引擎。
* 易用性好：Spark不仅支持Scala编写应用程序，而且支持Java和Python等语言进行编写。（Scala是一种高效、可扩展的语言，能够用简介的代码处理较为复杂的工作。）
* 通用性强：Spark生态圈中的组件：Spark Core提供内存计算框架，Spark SQL的即席查询，Spark Streaming的实时处理，MLlib的机器学习和GraphX的图处理。它们都是有AMP实验室提供，能够无缝地集成，并提供一站式解决平台。
* 随处运行：Spark具有很强的适应性，能够读取HDFS，HBase，S3和Tachyon为持久层读写原生数据；能够以Mesos，YARN和自身携带的Standalone作为资源管理器调度作业来完成Spark应用程序的计算。

### 1.2 Spark生态圈
    Spark生态圈包含了Spark Core、Spark SQL、MLLib、GraphX、Spark Streaming和Spark Structured Streaming等组件，提供离线计算、实时计算、图形化处理和机器学习等能力，能够无缝的集成并提供一站式解决方案。

* Spark Core：包含Spark的基本功能；尤其是定义RDD的API、操作以及这两者上的动作。其他Spark的库都是构建在RDD和Spark Core之上的
* Spark SQL：提供Hive查询语言（HiveQL）以及SQL查询语言(如Mysql)与Spark进行交互的API。每个数据库表被当做一个RDD，Spark SQL查询被转换为Spark Core操作。
* GraphX：控制图、并行图操作和计算的一组算法和工具的集合。GraphX扩展了RDD API，包含控制图、创建子图、访问路径上所有顶点的操作
* MLlib：一个常用机器学习算法库，算法被实现为对RDD的Spark操作。这个库包含可扩展的学习算法，比如分类、回归等需要对大量数据集进行迭代的操作
* Spark Streaming：对实时数据流进行处理和控制。Spark Streaming允许程序能够像普通RDD一样处理实时数据。
* Structured Streaming：以结构化的方式操作流式数据，能够像使用Spark SQL处理批处理一样，处理流数据。基于Event-Time，相比于SparkStreaming的Receive-Time更精确。

### 1.3 Spark与hadoop的区别
* Hadoop有两个核心模块，分布式存储模块HDFS和分布式计算模块Mapreduce
* Spark本身并没有提供分布式存储能力，因此Spark的分析大多依赖于Hadoop的分布式文件系统HDFS
* Hadoop的Mapreduce与Spark都可以进行数据计算，而相比于Mapreduce，Spark拥有DAG执行引擎，支持在内存中对数据进行迭代计算。官方提供的数据表明，如果数据由磁盘读取，速度是Hadoop MapReduce的10倍以上，如果数据从内存中读取，速度可以高达100多倍。

## 二、环境
### 2.1 JDK
下载安装JDK-1.8，地址 [http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

双击安装，安装完成后：

![](../../assets/nm4a1bszxur45p/image_001.bin "")
### 2.2 IDEA
IDEA是主流的Java集成开发工具，它提供了一系列最实用的的工具组合：智能编码辅助和编码检查等，IDEA把Java开发人员从一些耗时的常规工作中解放出来，显著地提高了开发效率。

地址 [https://www.jetbrains.com/idea/download/#section=mac](https://www.jetbrains.com/idea/download/#section=mac)

检查IDEA是否集成JDK环境，单击File 》 Project Structure菜单项，检查是否显示名字和路径，

![](../../assets/nm4a1bszxur45p/image_002.bin "")
若没有，需要手动关联，点击“+”号新增JDK，在弹出的文件选择框中选择JDK的安装目录。

### 2.3 Maven
Maven是一个项目管理工具，采用项目对象模型（POM）来管理项目。所有的项目信息都被定义在一个 pom.xml 文件中，通过该文件进行项目依赖包的管理和项目构建等。

地址 [http://maven.apache.org/download.cgi](http://maven.apache.org/download.cgi) 

![](../../assets/nm4a1bszxur45p/image_003.bin "")
解压缩文件到目录，比如/Users/zhoujie19/Tool/maven/apache-maven-3.6.3

**配置环境变量**：

① 打开.bash_profile文件：vim ~/.bash_profile

② 在此文件中添加设置环境变量的命令

export M2_HOME=/Users/zhoujie19/Tool/maven/apache-maven-3.6.3

export PATH=$PATH:$M2_HOME/bin

③ 添加之后保存并推出，执行以下命令使配置生效：source ~/.bash_profile

④ 检查：mvn -v

![](../../assets/nm4a1bszxur45p/image_004.bin "")
**修改Maven仓库的默认地址**：

打开文件/Users/zhoujie19/Tool/maven/apache-maven-3.6.3/conf/settings.xml， 搜索localRepository，找到配置本地仓库的代码，默认时，maven仓库地址是${user.home}/.m2/repository，解开<localRepository></localRepository>标签的注释，改成/Users/zhoujie19/maven/repository

![](../../assets/nm4a1bszxur45p/image_005.bin "")
## 三、开始项目
### 3.1 创建Maven工程
创建工程，关联工程对应的JDK

![](../../assets/nm4a1bszxur45p/image_006.bin "")
填写相关信息

![](../../assets/nm4a1bszxur45p/image_007.bin "")
* groupId：指明创建项目的组织或者小组的唯一标识。GroupId是项目的关键标识，典型的，此标识以组织的完全限定名来定义。比如，org.apache.maven.plugins是所有Maven插件项目指定的groupId。
* artifactId：指明此项目产生的主要产品的基本名称。项目的主要产品通常为一个JAR文件。第二，象源代码包通常使用artifactId作为最后名称的一部分。典型的产品名称使用这个格式： <artifactId>- <version>. <extension>(比如：myapp-1.0.jar)。
* version：项目产品的版本号。Maven帮助你管理版本，可以经常看到SNAPSHOT这个版本，表明项目处于开发阶段。
* name：项目的显示名称，通常用于maven产生的文档中。

完成后得到

![](../../assets/nm4a1bszxur45p/image_008.bin "")
各个文件夹说明：

|文件夹结构|描述|
|-|-|
|zj-maven-test|包含 src 文件夹和 pom.xml|
|src/main/java|java 代码文件。|
|src/main/resources|包含了 图片 / 属性 文件。|
|src/test/java|测试代码文件。|

### 3.2 pom.xml配置项详解
#### 3.2.1 项目信息
![](../../assets/nm4a1bszxur45p/image_009.bin "")
#### 3.2.2 配置依赖
![](../../assets/nm4a1bszxur45p/image_010.bin "")
Maven中心储存库查询依赖包信息： [http://](http://search.maven.org/)[mvnrepository.com](http://mvnrepository.com/)

如添加MySql JDBC的依赖jar包，

![](../../assets/nm4a1bszxur45p/image_011.bin "")
搜索第一个点击进去，可以看到所有版本，获取到MAVEN配置信息

![](../../assets/nm4a1bszxur45p/image_012.bin "")
剔除想要排除的JAR包，使用<exclusions> </exclusions> ，在<dependencies></dependencies>中添加。

#### 3.2.3 构建项目
项目构建，进行打包，使用<build></build>标签进行配置。

<plugins>给出构建过程中所用到的插件。

![](../../assets/nm4a1bszxur45p/image_013.bin "")
#### 3.2.3 资源库
Maven资源库共包含3种，分别是本地仓库、第三方仓库(私服)、中央仓库。

本地仓库：默认的仓库是在${user.home}/.m2/repository下，本文2.3 中改成/Users/zhoujie19/maven/repository；

第三方仓库(私服)：一般是由公司自己设立的，只为本公司内部共享使用。它既可以作为公司内部构件协作和存档，也可作为公用类库镜像缓存，减少在外部访问和下载的频率。连接私服，需要单独配置。如果没有配置私服，默认不使用；

中央仓库：Maven内置了远程公用仓库：[http://](http://search.maven.org/)[mvnrepository.com](http://mvnrepository.com/)。

依赖库搜索顺序：本地仓库-》第三方仓库(私服)-》中央仓库，中央仓库搜索到会下载到本地仓库备用。

**解决依赖包IDEA飘红**：

当添加依赖包，IDEA飘红提示"Dependency 'xxxx‘ not found"，

![](../../assets/nm4a1bszxur45p/image_014.bin "")
![](../../assets/nm4a1bszxur45p/image_015.bin "")
![](../../assets/nm4a1bszxur45p/image_016.bin "")
## 四、项目示例
[算子开发示例WordCount(RDD)、App安装量(DataFrame)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/IunjADfIEVOuh3?source=137?t=mention&mt=doc&dt=doc)
