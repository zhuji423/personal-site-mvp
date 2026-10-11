---
title: "Hadoop"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\hadoop\\README.md"
---
hadoop



一些重要概念：

# Hadoop
* Hadoop是一个开源的分布式计算框架，用于存储和处理大规模数据集。它提供了一个可扩展的**分布式文件系统（HDFS）**和一个**分布式计算框架（MapReduce）**，可以在大量廉价硬件上进行并行计算。

# HDFS
* HDFS（Hadoop Distributed File System）是Hadoop的分布式文件系统。它被设计用于在集群中存储和管理大规模数据集。HDFS将数据分割成块，并将这些块复制到不同的计算节点上，以提供容错性和高可用性。
* 一般将模型需要的数据例如csv/libsvm格式的文件都会保存成Hive表并存放在HDFS上。
* 详情：[HDFS分布式文件系统](./hadoop_引用文档/HDFS分布式文件系统.md)

# HIVE
* HIVE是基于Hadoop的数据仓库基础设施，可以理解为一种类似于SQL的引擎或工具，提供了查询语言（HiveQL），用于**查询和分析存储**在Hadoop上的数据。Hive可以将结构化数据映射到Hadoop的分布式文件系统上HDSF上，并提供高层抽象，使用户能够**使用类SQL语法进行查询和分析**。
* Hive构建在HDFS之上，本质上可看作是一个翻译器，将HiveSQL语言翻译成MapReduce程序或Spark程序。

# HBase
HBase是一个分布式、可扩展、面向列的NoSQL数据库，建立在Hadoop之上。它提供了对大规模数据集的**实时读写访问**能力，并具有高可靠性和高性能的特点。HBase适用于**需要随机、快速访问大规模数据**的应用程序。

# Spark
* Spark是一个快速、通用的大数据处理引擎，可以进行**分布式数据处理和分析**。与Hadoop的MapReduce相比，Spark具有更高的性能和更丰富的功能。Spark支持多种编程语言（如Scala、Java和Python(pyspark)），并提供了一组丰富的API，包括用于数据处理、机器学习和图计算的库。
* 详情：[Spark](./hadoop_引用文档/Spark.md)


