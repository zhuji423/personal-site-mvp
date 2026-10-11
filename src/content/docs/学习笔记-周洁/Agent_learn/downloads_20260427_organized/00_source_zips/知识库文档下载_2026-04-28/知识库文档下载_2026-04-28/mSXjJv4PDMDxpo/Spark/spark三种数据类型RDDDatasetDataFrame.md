---
title: "spark三种数据类型RDDDatasetDataFrame"
description: "spark三种数据类型RDD/Dataset/DataFrame"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Spark\\spark三种数据类型RDDDatasetDataFrame.md"
---
spark三种数据类型RDD/Dataset/DataFrame

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间

## 一、RDD/Dataset/DataFrame关系
### 1.1 简介
Spark共提供3种基本的数据类型，分别是Spark Core引擎对应的RDD，以及Spark SQL引擎对应的DataFrame 和 DataSet。

![](../../assets/lJFhF3sileZP7i/image_001.bin "")
Spark-core的核心抽象是RDD，Spark SQL等都基于RDD封装了自己的抽象，在Spark SQL中是DataFrame/DataSet。相对来说RDD是更偏底层的抽象，DataFrame/DataSet是在其上做了一层封装，做了优化，使用起来更加方便。从功能上来说，DataFrame/DataSet能做的事情RDD都能做，RDD能做的事情DataFrame/DataSet不一定能做。

### 1.2 RDD/Dataset/DataFrame区别
**1.2.1 RDD**

RDD就是一个不可变的分布式对象集合，是Spark对数据的核心抽象。每个RDD都被分为多个分区，每个分区就是一个数据集片段，这些分区运行在集群中的不同节点上。 RDD提供了一种高度受限的内存共享模型，即RDD是只读的，只能基于稳定的物理储存中的数据集来创建RDD或对已有的RDD进行转换操作来得到新的RDD。

**①分片的集合**

RDD(resilient distributed dataset)即弹性分布式数据集，它由多个partition(分区)组成的集合。每个partition运行在分布式集群的不同节点上。

默认情况下，每个HDFS的分区文件（默认分区文件块大小是64M）都会创建一个RDD分区。

注：一个文件被切成N份，那么每一份就代表一个分区， 每个分区能被并行的处理。

**②函数作用在每个分区**

RDD共包含两种计算方式，一种是transformations转换(如：map, filter, groupBy, join等)，一个种是actions操作(如：count, collect, save等)，每种计算方式对应的具体函数

函数作用在每个分区上并行执行。通过转换或者操作后，生成新的RDD，旧的RDD内容不变。

注意：Transformations转换是Lazy的，也就是说从一个RDD转换生成另一个RDD的操作不是马上执行，Spark在遇到Transformations转换时只会记录需要这样的转换，并不会去执行，需要等到有Actions操作的时候才会真正启动计算过程进行计算。需重点注意！

**③RDD之间有一系列依赖关系**

由于RDD每次转换计算都会生成新的RDD，所以RDD会形成类似流水线一样的前后依赖关系。

Spark会记录RDD前后依赖关系，所以当有分区的数据丢失时， Spark会通过依赖关系进行重新计算，从而计算出丢失的数据，而不是对RDD所有的分区进行重新计算。

依赖关系共包含两种：宽依赖和窄依赖。

a、窄依赖是指父RDD的每个分区只被子RDD的一个分区所使用

b、宽依赖是指父RDD的每个分区都可能被多个子RDD分区所使用

如下图，一个HDFS文件被切成3个分区，函数作用于每个分区上，具体计算过程如下：

a、进行一系列Transformations转换，如下的map、filter处理后，生成了3个新的RDD（窄依赖），经过reduceByKey处理后，生成2个新的RDD（宽依赖）

b、最后，经过一个actions操作，如下的saveAsTextFile操作处理，触发整条RDD依赖链执行，将结果保存到目标HDFS中

![](../../assets/lJFhF3sileZP7i/image_002.bin "")
**1.2.2 DataFrame**

DataFrame是用在Spark SQL中的一种存放Row对象的特殊RDD，是Spark SQL中的数据抽象，它是一种结构化的数据集，每一条数据都由几个命名字段组成（类似与传统数据库中的表），DataFrame能够利用结构信息更加高效的存储数据。同时， Spark SQL为DataFrame提供了非常好用的API，而且还能注册成表使用sql来操作。 DataFrame可以从外部数据源创建，也可以从查询结果或已有的RDD创建。

Dataset每一行存储的是强类型的值，例如：Dataset<String>，Dataset<Person>，因此取得每条数据某个值时，可以直接使用 类的方法获取，如person.getName() ，并且Dataset可以在编译时检查类型

而DataFrame被声明为Dataset<Row>，存储的Row是无类型的，是以列名来作处理的，因此取得每条数据某个值时，要使用row.getString(0)或col("name")这样的方式解析来取得，无法知道某个值的具体的数据类型。

**1.2.3 Dataset**

Dataset是Spark1.6开始提供的API，是Spark SQL最新的数据抽象。它把RDD的优势（强类型，可以使用lambda表达式函数）和Spark SQL的优化执行引擎结合到了一起。 Dataset可以从JVM对象创建得到，而且可以像DataFrame一样使用API或sql来操作。

**结构**

Dataset 也是弹性分布式数据集，但相比于RDD，多了shema信息（类似数据表的列名），使得RDD每一行的数据, 结构都是一样的。

Spark SQL通过schema可以清楚地知道该数据集中包含哪些列，每列的名称和类型各是什么，因此，可以通过类SQL的语法对数据进行操作（如筛选某列，列聚合等），简单易用。

如下图，直观地体现了Dataset和RDD的区别。左侧的JavaRDD<Person>虽然以Person类为类型参数，但Spark Core框架本身不了解Person类的内部结构。而右侧的Dataset<Person>却提供了详细的结构信息，使得Spark SQL可以清楚地知道该数据集中包含哪些列，每列的名称和类型各是什么，如图中红框框起来的部分。

![](../../assets/lJFhF3sileZP7i/image_003.bin "")
因此，Dataset既可以进行一些RDD操作(如map、filter等) 又可以进行一些 SQL的操作（如果group、select等）。

**1.2.4 关系**

**RDD + Schema = DataFrame = Dataset[Row]**

注：RDD是Spark的核心，DataFrame/Dataset是Spark SQL的核心，RDD不支持sql操作。

|数据类型|优点|缺点|
|-|-|-|
|RDD|JVM对象组成的分布式数据集合不可变并且有容错能力可处理结构化和非结构化的数据支持函数式转换|没有Schema用户自己优化程序从不同的数据源读取数据非常困难合并多个数据源中的数据也非常困难|
|DataFrame|Row对象组成的分布式数据集不可变并且有容错能力处理结构化数据自带优化器Catalyset,可自动优化程序DataFrame让Spark对结构化数据有了处理能力|编译时不能类型转化进行安全检查，运行时才能确定是否有问题对于对象支持不友好，RDD内部数据直接以Java对象存储，DataFrame内存存储的是Row对象而不能是自定义对象|
|Dataset|DateSet整合了RDD和DataFrame的优点，支持结构化和非结构化数据和RDD一样，支持自定义对象存储和DataFrame一样，支持结构化数据的sql查询采用堆外内存存储，gc友好类型转化安全，代码友好||

### 1.3 选用
使用的时候，如果数据源是HDFS（每行存储的不是json串）,推荐使用RDD。

如果数据源是HDFS（每行存储json串）、HIVE表（如公司的UDW）或者 外部的数据库表（如mysql、redis）等，推荐使用 DataFrame 和 Dataset。

### 1.4 入口类
Spark2.0以前，使用不同的数据类型，需要采用不同的入口类，如RDD对应的入口类是SparkContext，DataFrame对应的入口类是SQLContext或者HiveContext，入口类用于指定Spark集群的各种参数，并与资源管理器做交互。

Spark2.0开始及之后，提出了一个统一的入口类SparkSession，封装了SparkContext、SQLContext和HiveContext.

### 1.5 互相转化
**RDD—>DataFrame**

```
Dataset<Row> dataFrame = sparkSession.createDataFrame(personRDD, Person.class);
```
**DataFrame—>Dataset**

```
Encoder personEncoder = Encoders.bean(Person.class);
Dataset<Person> dataSet = dataFrame.as(personEncoder);
```
**Dataset—>RDD**

```
JavaRDD<Person> rdd = dataSet.toJavaRDD();
```
## 二、RDD操作
### 2.1 说明
a、RDD共包含两种计算方式，一种是transformations转换，一种是actions操作，每种计算方式包含一些常用的方法。

注意：Transformations转换是Lazy的，也就是说从一个RDD转换生成另一个RDD的操作不是马上执行，Spark在遇到Transformations转换时只会记录需要这样的转换，并不会去执行，需要等到有Actions操作的时候才会真正启动计算过程进行计算。写代码的时候，一定要特别注意，基本是新手必踩的坑！！！

b、如果一个RDD需要多次调用，还可以使用持久化方法，将RDD持久化到内存或者磁盘中，该RDD再次调用时，就无需重复计算。

c、如果想在Driver和Executors之间共享大容量的变量或者使用累加器，可以采用Broadcast和Accumulator。

### 2.2 RDD创建
在pom.xml文件中引入Spark的依赖包

```
<dependency>
  <groupId>org.apache.spark</groupId>
  <artifactId>spark-sql_2.12</artifactId>
  <version>3.0.1</version>
</dependency>
```
创建RDD共两种方式：1) 通过列表创建RDD；2) 通过HDFS/AFS路径创建RDD

```
package org.zj.test;

import org.apache.spark.SparkConf;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import java.util.Arrays;
import java.util.List;


/**
 * RDD学习
 */

public class learnRDD {
    public static void main(String[] args){
        // 1、新建SparkConf对象，配置集群参数，如程序名、执行集群名、需要的内存和cpu核数
        SparkConf sparkConf = new SparkConf().setAppName("learnRDD demo").setMaster("local");

        // 2、基于SparkConf对象初始化SparkSession对象
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();

        // 3、基于SparkSession对象创建JavaSparkContext对象，用于与集群资源管理器做交互
        JavaSparkContext sc = JavaSparkContext.fromSparkContext(sparkSession.sparkContext());

        // 4、通过列表创建RDD
        List<Integer> data = Arrays.asList(1, 2, 3, 4, 5);
        JavaRDD<Integer> listRDD = sc.parallelize(data);

        // 4、或 通过HDFS/AFS路径创建RDD
        JavaRDD<String> javaRDD = sc.textFile("data/wordFile");
    }
}
```
### 2.3 transformations转换方法
#### 2.3.1 函数体采用Lambda表达式
 格式：(参数1, 参数2, 参数...) -> { 处理代码块 }  

```
// 4、或 通过HDFS/AFS路径创建RDD
JavaRDD<String> javaRDD = sc.textFile("data/wordFile");

// 5、统计单词出现次数，并输出结果
javaRDD.flatMap(line -> {
    // 将多个单词一行转化为一个单词一次
    return Arrays.asList(line.split(",")).iterator();
}).mapToPair(word -> {
    // 输出单词元组，每个单词初始化个数为1
    return new Tuple2<String, Integer>(word, 1);
}).reduceByKey((x, y) -> {
    // 将相同单词进行聚合，并对出现次数进行累加
    return x + y;
}).saveAsTextFile("data/wordFileResult");
```
#### 2.3.2 常用方法
data/wordFile文件：

![](../../assets/lJFhF3sileZP7i/image_004.bin "")
|方法名|方法描述|代码示例|
|-|-|-|
|flatMap(func)|实现一行转多行。作用于RDD的每一行，产出新的RDD每行为迭代器的一个元素。|JavaRDD<String> flatMapRDD = javaRDD.flatMap(line -> {
    // 将多个单词一行转化为一个单词一次，返回值需要iterator迭代器，将String数组转List后获取iterator
    return Arrays.asList(line.split(",")).iterator();
});
System.out.println(flatMapRDD.collect());
// [a, b, c, d, a, b, e, e, f, a, c, o, d]|
|map(func)|作用于RDD的每一行，产出新RDD每一行为经过函数处理后的结果。|JavaRDD<String> mapRDD = javaRDD.map(line -> {
    return line.split(",")[0];
});
System.out.println(mapRDD.collect());
// [a, a, e]|
|mapPartitions(func)|作用于RDD的一个分区，产出新的RDD的每行为迭代器的一个元素。与map的区别是，以分区为单位进行输入和输出处理。常用场景：在map处理时，需要读取mysql数据，如果采用map方法每行处理都需进行mysql连接而采用mapPartitions，连接次数为分区数的个数，大大节省资源消耗，提升效率。|JavaRDD<String> mapPartitionsRDD = javaRDD.mapPartitions(iterator -> {
    ArrayList<String> results = new ArrayList<String>();
    while (iterator.hasNext()){
        String line = iterator.next();
        results.add(line.split(",")[0]);
    }
    return results.iterator();
});
System.out.println("mapPartitions:" + mapPartitionsRDD.collect());
// mapPartitions:[a, a, e]|
|mapToPair(func)|作用于RDD的每一行，产出新的RDD每一行为一个元组元组用 Tuple2 这个类表示常用场景：按key做聚合，需要先将一行转换成元组，元组的第一个元素是key，第二个元素是value注意：读取Tuple2元组中的值，采用 元组名._1 读取元组的第一个值，采用 元组名._2 读取元组的第二个值|JavaPairRDD<String, Integer> mapToPairRDD = javaRDD.mapToPair(line -> {
    return new Tuple2<String, Integer>(line.split(",")[0], 1);
});
System.out.println("mapToPair:" + mapToPairRDD.collect());
// mapToPair:[(a,1), (a,1), (e,1)]
System.out.println("mapToPair第一个元素的第一个值:" + mapToPairRDD.collect().get(0)._1);
// mapToPair第一个元素的第一个值:a|
|filter(func)|作用于RDD的每一行，通过函数对行进行过滤，产出新的RDD每一行满足条件的行注意：再进行进一步操作前，经常通过filter把一些不必要的行过滤掉，可以提升效率|// 原始数据:[a,b,c,d, a,b,e, e,f,a,c,o,d]
JavaRDD<String> filterRDD = javaRDD.filter(line -> {
    if (!line.contains("e")){
        return true;
    }
    else {
        return false;
    }
});
System.out.println("filter:" + filterRDD.collect());
// filter:[a,b,c,d]|
|distinct()|作用于RDD的每一行，对重复行进行过滤，产出新的RDD为没有重复的行|// map:[a, a, e]
JavaRDD<String> distinctRDD = mapRDD.distinct();
System.out.println("distinct:" + distinctRDD.collect());
// distinct:[e, a]|
|reduceByKey(func)|作用于PairRDD的每一行，按相同key进行聚合操作，产出新的RDD每一行为元组，格式为 （key, 聚合后的value）func函数的参数是（value1，value2），value1代表该key上次聚合后的值，value2代表该key当前行元组的值初始的value1为0|// mapToPair:[(a,1), (a,1), (e,1)]
JavaPairRDD<String, Integer> reduceByKeyRDD = mapToPairRDD.reduceByKey((value1, value2) -> {
    return value1 + value2;
});
System.out.println("reduceByKey:" + reduceByKeyRDD.collect());
// reduceByKey:[(e,1), (a,2)]|
|sortByKey([ascending])|作用于PairRDD的每一行，按key进行排序|// mapToPair:[(a,1), (a,1), (e,1)]
JavaPairRDD<String, Integer> sortByKeyRDD = mapToPairRDD.sortByKey();
System.out.println("sortByKey:" + sortByKeyRDD.collect());
// sortByKey:[(a,1), (a,1), (e,1)]|
|coalesce(numPartitions, shuffle)|修改RDD分区的个数为指定numPartitions，当shuffle为false时，coalesce只能用来减少分区个数.当shuffle为ture时，相当于repartition的功能，既可以减少，也可以增加分区个数。一般情况下，减少分区数时，如果减少的分区数不多，将shuffle设置为false，coalesce的效率比repartition高.如果减少的分区数很多，如原始分区数为100，numPartitions设置为1，那么用repartition效率会高一些因为shuffle设置为true能增加处理的并行度。|// 将RDD分区减少到1个，默认情况下shuffle为false
JavaRDD<String> coalesceRDD = javaRDD.coalesce(1);
System.out.println("coalesce:" + coalesceRDD.collect());
// coalesce:[a,b,c,d, a,b,e, e,f,a,c,o,d]
// 将RDD分区减少到1个，并设置shuffle为true，相当于repartition
JavaRDD<String> coalesceRDD2 = javaRDD.coalesce(1, true);
System.out.println("coalesce_with_shuffle_true:" + coalesceRDD2.collect());
// coalesce_with_shuffle_true:[a,b,c,d, a,b,e, e,f,a,c,o,d]|
|repartition(numPartitions)|修改RDD分区的个数为指定numPartitions，repartition既可以减少，也可以增加分区个数。|// 将RDD分区减少到1个，默认情况下shuffle为false
JavaRDD<String> repartitionRDD = javaRDD.repartition(1);
System.out.println("repartition:" + repartitionRDD.collect());
// repartition:[a,b,c,d, a,b,e, e,f,a,c,o,d]|
|union(otherDataset)|原始的RDD与目标RDD做并集操作，返回包含原始和目标元素的RDD|// 原始数据:[a,b,c,d, a,b,e, e,f,a,c,o,d]
// map:[a, a, e]
JavaRDD<String> unionRDD = javaRDD.union(mapRDD);
System.out.println("union:" + unionRDD.collect());
// union:[a,b,c,d, a,b,e, e,f,a,c,o,d, a, a, e]|
|intersection(otherDataset)|原始的RDD与目标RDD做交集操作，返回包含原始和目标元素的RDD|// union:[a,b,c,d, a,b,e, e,f,a,c,o,d, a, a, e]
// map:[a, a, e]
JavaRDD<String> intersectionRDD = unionRDD.intersection(mapRDD);
System.out.println("intersection:" + intersectionRDD.collect());
// intersection:[e, a]|
|join(otherDataset)|原始的PairRDD与目标PairRDD做join操作，key相同的结果才会被输出。例如：原始RDD存在行为(K, V) ，目标RDD存在行为(K, W)，则join后的结果是 (K, (V, W)) 同样支持`leftOuterJoin`, `rightOuterJoin`, 和 `fullOuterJoin这几种类型的join`注意：Optional<>类型的取值直接用 .get()方法|// mapToPair:[(a,1), (a,1), (e,1)]
// reduceByKey:[(e,1), (a,2)]
// join
JavaPairRDD<String, Tuple2<Integer, Integer>> joinRDD = mapToPairRDD.join(reduceByKeyRDD);
System.out.println("join:" + joinRDD.collect());
// join:[(e,(1,1)), (a,(1,2)), (a,(1,2))]
// leftOuterJoin
JavaPairRDD<String, Tuple2<Integer, org.apache.spark.api.java.Optional<Integer>>> leftOuterJoinRDD
        = mapToPairRDD.leftOuterJoin(reduceByKeyRDD);
System.out.println("leftOuterJoin:" + leftOuterJoinRDD.collect());
// leftOuterJoin:[(e,(1,Optional[1])), (a,(1,Optional[2])), (a,(1,Optional[2]))]
// rightOuterJoin
JavaPairRDD<String, Tuple2<org.apache.spark.api.java.Optional<Integer>, Integer>> rightOuterJoinRDD
        = mapToPairRDD.rightOuterJoin(reduceByKeyRDD);
System.out.println("rightOuterJoin:" + rightOuterJoinRDD.collect());
// rightOuterJoin:[(e,(Optional[1],1)), (a,(Optional[1],2)), (a,(Optional[1],2))]
// fullOuterJoin
JavaPairRDD<String, Tuple2<Optional<Integer>, Optional<Integer>>> fullOuterJoinRDD
        = mapToPairRDD.fullOuterJoin(reduceByKeyRDD);
System.out.println("fullOuterJoin:" + fullOuterJoinRDD.collect());
// fullOuterJoin:[(e,(Optional[1],Optional[1])), (a,(Optional[1],Optional[2])), (a,(Optional[1],Optional[2]))]|

### 2.4 actions操作方法
|方法名|方法描述|代码示例|
|-|-|-|
|collect()|将RDD所有元素收集到Drive节点，返回一个List列表，如上面的示例用的就是collect方法当数据量大时，这种操作容易造成Drive节点的内存溢出，**慎用**！！！如果只是想查看元素的格式，可以使用take(n)，查看少量元素即可如果要遍历所有元素，推荐使用foreach(func)|List<String> collectList = javaRDD.collect();
System.out.println("collect:" + collectList);
// collect:[a,b,c,d, a,b,e, e,f,a,c,o,d]|
|take(n)|返回值是 包含RDD的n个元素的List列表|List<String> takeList = javaRDD.take(2);
System.out.println("take:" + takeList);
// take:[a,b,c,d, a,b,e]|
|foreach(func)|没有返回值。RDD的每个元素会被func处理。在分区节点上运行，不会将结果收集到Drive节点|javaRDD.foreach(line -> {
    // line 存储到外部存储介质
});|
|count()|返回值是 RDD元素的个数|long count = javaRDD.count();
System.out.println("count:" + count);
// count:3|
|saveAsTextFile(path)|将RDD的元素输出到指定的外部存储介质中，如HDFS/AFS中|javaRDD.saveAsTextFile("/file/path/to/hdfs");|
|countByKey()countByValue()|统计PairRDD的key出现的次数统计RDD的value出现的次数|// mapToPair:[(a,1), (a,1), (e,1)]
// countByKey
Map<String, Long> countByKeyMap = mapToPairRDD.countByKey();
System.out.println("countByKey:" + countByKeyMap);
// countByKey:{e=1, a=2}
// countByValue
Map<String, Long> countByValueMap = javaRDD.countByValue();
System.out.println("countByValue:" + countByValueMap);
// countByValue:{e,f,a,c,o,d=1, a,b,e=1, a,b,c,d=1}|

示例代码

**learnRDD.java**

```
package org.zj.test;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.Optional;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;


/**
 * RDD学习
 */

public class learnRDD {
    public static void main(String[] args){
        // 1、新建SparkConf对象，配置集群参数，如程序名、执行集群名、需要的内存和cpu核数
        SparkConf sparkConf = new SparkConf().setAppName("learnRDD demo").setMaster("local");

        // 2、基于SparkConf对象初始化SparkSession对象
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();

        // 3、基于SparkSession对象创建JavaSparkContext对象，用于与集群资源管理器做交互
        JavaSparkContext sc = JavaSparkContext.fromSparkContext(sparkSession.sparkContext());

        // 4、通过列表创建RDD
        // List<Integer> data = Arrays.asList(1, 2, 3, 4, 5);
        // JavaRDD<Integer> listRDD = sc.parallelize(data);

        // 4、或 通过HDFS/AFS路径创建RDD
        JavaRDD<String> javaRDD = sc.textFile("data/wordFile");
        System.out.println("原始数据:" + javaRDD.collect());
        // 原始数据:[a,b,c,d, a,b,e, e,f,a,c,o,d]

        // 5、transformations转换

        // flatMap
        JavaRDD<String> flatMapRDD = javaRDD.flatMap(line -> {
            // 将多个单词一行转化为一个单词一次，返回值需要iterator迭代器，将String数组转List后获取iterator
            return Arrays.asList(line.split(",")).iterator();
        });
        System.out.println("flatMap:" + flatMapRDD.collect());
        // flatMap:[a, b, c, d, a, b, e, e, f, a, c, o, d]

        // map
        JavaRDD<String> mapRDD = javaRDD.map(line -> {
            return line.split(",")[0];
        });
        System.out.println("map:" + mapRDD.collect());
        // map:[a, a, e]

        // mapPartitions
        JavaRDD<String> mapPartitionsRDD = javaRDD.mapPartitions(iterator -> {
            ArrayList<String> results = new ArrayList<String>();
            while (iterator.hasNext()){
                String line = iterator.next();
                results.add(line.split(",")[0]);
            }
            return results.iterator();
        });
        System.out.println("mapPartitions:" + mapPartitionsRDD.collect());
        // mapPartitions:[a, a, e]

        // mapToPair
        JavaPairRDD<String, Integer> mapToPairRDD = javaRDD.mapToPair(line -> {
            return new Tuple2<String, Integer>(line.split(",")[0], 1);
        });
        System.out.println("mapToPair:" + mapToPairRDD.collect());
        // mapToPair:[(a,1), (a,1), (e,1)]
        System.out.println("mapToPair第一个元素的第一个值:" + mapToPairRDD.collect().get(0)._1);
        // mapToPair第一个元素的第一个值:a

        // filter
        JavaRDD<String> filterRDD = javaRDD.filter(line -> {
            if (!line.contains("e")){
                return true;
            }
            else {
                return false;
            }
        });
        System.out.println("filter:" + filterRDD.collect());
        // filter:[a,b,c,d]

        // distinct
        JavaRDD<String> distinctRDD = mapRDD.distinct();
        System.out.println("distinct:" + distinctRDD.collect());
        // distinct:[e, a]

        // reduceByKey
        JavaPairRDD<String, Integer> reduceByKeyRDD = mapToPairRDD.reduceByKey((value1, value2) -> {
            return value1 + value2;
        });
        System.out.println("reduceByKey:" + reduceByKeyRDD.collect());
        // reduceByKey:[(e,1), (a,2)]

        // sortByKey
        JavaPairRDD<String, Integer> sortByKeyRDD = mapToPairRDD.sortByKey();
        System.out.println("sortByKey:" + sortByKeyRDD.collect());
        // sortByKey:[(a,1), (a,1), (e,1)]

        // coalesce
        // 将RDD分区减少到1个，默认情况下shuffle为false
        JavaRDD<String> coalesceRDD = javaRDD.coalesce(1);
        System.out.println("coalesce:" + coalesceRDD.collect());
        // coalesce:[a,b,c,d, a,b,e, e,f,a,c,o,d]
        // 将RDD分区减少到1个，并设置shuffle为true，相当于repartition
        JavaRDD<String> coalesceRDD2 = javaRDD.coalesce(1, true);
        System.out.println("coalesce_with_shuffle_true:" + coalesceRDD2.collect());
        // coalesce_with_shuffle_true:[a,b,c,d, a,b,e, e,f,a,c,o,d]

        // repartition
        // 将RDD分区减少到1个，默认情况下shuffle为false
        JavaRDD<String> repartitionRDD = javaRDD.repartition(1);
        System.out.println("repartition:" + repartitionRDD.collect());
        // repartition:[a,b,c,d, a,b,e, e,f,a,c,o,d]

        // union
        JavaRDD<String> unionRDD = javaRDD.union(mapRDD);
        System.out.println("union:" + unionRDD.collect());
        // union:[a,b,c,d, a,b,e, e,f,a,c,o,d, a, a, e]

        // intersection
        JavaRDD<String> intersectionRDD = unionRDD.intersection(mapRDD);
        System.out.println("intersection:" + intersectionRDD.collect());
        // intersection:[e, a]

        // join
        JavaPairRDD<String, Tuple2<Integer, Integer>> joinRDD = mapToPairRDD.join(reduceByKeyRDD);
        System.out.println("join:" + joinRDD.collect());
        // join:[(e,(1,1)), (a,(1,2)), (a,(1,2))]
        // leftOuterJoin
        JavaPairRDD<String, Tuple2<Integer, org.apache.spark.api.java.Optional<Integer>>> leftOuterJoinRDD
                = mapToPairRDD.leftOuterJoin(reduceByKeyRDD);
        System.out.println("leftOuterJoin:" + leftOuterJoinRDD.collect());
        // leftOuterJoin:[(e,(1,Optional[1])), (a,(1,Optional[2])), (a,(1,Optional[2]))]
        // rightOuterJoin
        JavaPairRDD<String, Tuple2<org.apache.spark.api.java.Optional<Integer>, Integer>> rightOuterJoinRDD
                = mapToPairRDD.rightOuterJoin(reduceByKeyRDD);
        System.out.println("rightOuterJoin:" + rightOuterJoinRDD.collect());
        // rightOuterJoin:[(e,(Optional[1],1)), (a,(Optional[1],2)), (a,(Optional[1],2))]
        // fullOuterJoin
        JavaPairRDD<String, Tuple2<Optional<Integer>, Optional<Integer>>> fullOuterJoinRDD
                = mapToPairRDD.fullOuterJoin(reduceByKeyRDD);
        System.out.println("fullOuterJoin:" + fullOuterJoinRDD.collect());
        // fullOuterJoin:[(e,(Optional[1],Optional[1])), (a,(Optional[1],Optional[2])), (a,(Optional[1],Optional[2]))]

        // 6、actions操作

        // collect
        List<String> collectList = javaRDD.collect();
        System.out.println("collect:" + collectList);
        // collect:[a,b,c,d, a,b,e, e,f,a,c,o,d]

        // take
        List<String> takeList = javaRDD.take(2);
        System.out.println("take:" + takeList);
        // take:[a,b,c,d, a,b,e]

//        // foreach
//        javaRDD.foreach(line -> {
//            // line 存储到外部存储介质
//        });

        // count
        long count = javaRDD.count();
        System.out.println("count:" + count);
        // count:3

//        // saveAsTextFile
//        javaRDD.saveAsTextFile("/file/path/to/hdfs");

        // countByKey
        Map<String, Long> countByKeyMap = mapToPairRDD.countByKey();
        System.out.println("countByKey:" + countByKeyMap);
        // countByKey:{e=1, a=2}
        // countByValue
        Map<String, Long> countByValueMap = javaRDD.countByValue();
        System.out.println("countByValue:" + countByValueMap);
        // countByValue:{e,f,a,c,o,d=1, a,b,e=1, a,b,c,d=1}
    }
}
```
### 2.5 RDD持久化方法
Spark通过cache()方法可以将RDD持久化到内存中，一旦首次被触发，该RDD将会被保留在计算节点的内存中，之后再调用这个RDD就不会再重复计算。

```
javaRDD.cache();
```
### 2.6 共享变量Broadcast和Accumulator
多个task想要共享某个变量，Spark为此提供了两个共享变量，一种是Broadcast Variable（广播变量），另一种是Accumulator（累加变量）。

Broadcast Variable会将使用到的变量，仅仅为每个节点拷贝一份，而不会为每个task都拷贝一份。当变量很大时，其最大的用处是优化性能，减少网络传输以及内存消耗。

Accumulator则可以让多个task共同操作一份变量，主要可以进行累加操作。但是task只能对Accumulator进行累加操作，不能读取它的值。只有Driver程序可以读取Accumulator的值。

```
public class learnRDDShareVariable {
    public static void main(String[] args){
        SparkConf sparkConf = new SparkConf().setAppName("learnRDDShareVariable demo").setMaster("local");
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();
        JavaSparkContext sc = JavaSparkContext.fromSparkContext(sparkSession.sparkContext());

        // 需要共享的值
        List<String> share = Arrays.asList("my", "big", "data", "to", "share");
        List<String> first = Arrays.asList("a o", "b p");

        // 通过列表创建RDD
        JavaRDD<String> javaRDD = sc.parallelize(first);

        // 创建Broadcast
        Broadcast<String> shareBroadcast = sc.broadcast(share.toString());
        // 创建累加器
        LongAccumulator accum = sc.sc().longAccumulator();

        // RDD操作
        JavaRDD<String> mapRDD = javaRDD.map(line -> {
            // 累加器进行叠加，在分区处理节点上不能读取累加器的值
            accum.add(12);
            // RDD每个元素与共享变量做链接
            String join = line + "--" + shareBroadcast.value();

            return join;
        });

        System.out.println("mapRDD:" + mapRDD.collect());
        // mapRDD:[a o--[my, big, data, to, share], b p--[my, big, data, to, share]]
        System.out.println("accum:" + accum.value());
        // accum:24
    }
}
```
### 2.7 RDD转DataFrame
共两种方式，一种是通过反射机制，另一种是通过程序指定schema。

#### 2.7.1 通过反射机制的方式
![](../../assets/lJFhF3sileZP7i/image_005.bin "")
a、新建JavaBean类，类需要实现序列化接口Serializable且属性都要有get、set方法。如下例：

```
public class Person implements Serializable {
    String name;
    String sex;
    Long age;
    Long height;

    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }

    public String getSex(){
        return sex;
    }
    public void setSex(String sex){
        this.sex = sex;
    }

    public Long getAge(){
        return age;
    }
    public void setAge(Long age){
        this.age = age;
    }

    public Long getHeight(){
        return height;
    }
    public void setHeight(Long height){
        this.height = height;
    }
}
```
b、新建DataFrame

首先，读取文件，创建JavaRDD<类名>，每一行是类的信息

然后，调用sparkSession对象的createDataFrame(RDD, 类的Class对象) 方法创建DataFrame

```
public class learnRDDToDataFrame {
    public static void main(String[] args){
        SparkConf sparkConf = new SparkConf().setAppName("learnRDDToDataFrame demo").setMaster("local");
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();
        JavaSparkContext sc = JavaSparkContext.fromSparkContext(sparkSession.sparkContext());

        // 读取输入文件，创建RDD
        JavaRDD<Person> personRDD = sc.textFile("data/person").map(line -> {
            String [] infos = line.split(",");
            Person person = new Person();
            person.setName(infos[0]);
            person.setSex(infos[1]);
            person.setAge(Long.valueOf(infos[2]));
            person.setHeight(Long.valueOf(infos[3]));
            return person;
        });

        // 将RDD转为DataFrame
        Dataset<Row> dataFrame = sparkSession.createDataFrame(personRDD, Person.class);
        dataFrame.printSchema();
        // root
        // |-- age: long (nullable = true)
        // |-- height: long (nullable = true)
        // |-- name: string (nullable = true)
        // |-- sex: string (nullable = true)
    }
}
```
#### 2.7.2 通过程序指定schema类的方式
a、新建RDD，并将RDD的每行转成Row类型

b、创建fields类，存储到fields类列表中，基于列表，新建schema类StructType

c、通过JavaRDD<Row>和StructType对象，创建DataFrame

```
public static void main(String[] args){
    SparkConf sparkConf = new SparkConf().setAppName("learnRDDToDataFrame demo").setMaster("local");
    SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();
    JavaSparkContext sc = JavaSparkContext.fromSparkContext(sparkSession.sparkContext());

    // 读取输入文件，将每行转为Row类型
    JavaRDD<Row> rowRDD = sc.textFile("data/person").map(line -> {
        String [] attributes = line.split(",");
        return RowFactory.create(attributes[0], attributes[1], Integer.valueOf(attributes[2]));
    });

    // 创建field，名字、类型、是否可为空
    StructField nameField = DataTypes.createStructField("name", DataTypes.StringType, true);
    StructField sexField = DataTypes.createStructField("sex", DataTypes.StringType, true);
    StructField ageField = DataTypes.createStructField("age", DataTypes.IntegerType, true);

    // 存储field到list
    List<StructField> fieldList = new ArrayList<>();
    fieldList.add(nameField);
    fieldList.add(sexField);
    fieldList.add(ageField);
    
    // 通过fieldList创建schema
    StructType schema = DataTypes.createStructType(fieldList);

    Dataset<Row> dataFrame = sparkSession.createDataFrame(rowRDD, schema);
    dataFrame.printSchema();
    // root
    // |-- age: long (nullable = true)
    // |-- name: string (nullable = true)
    // |-- sex: string (nullable = true)
}
```
## 三、DataFrame操作
### 3.1 说明
a、提供类SQL的函数，如select、group、count、filter等，让用户方便对数据进行操作。Spark SQL 会将这些操作转化成RDD的操作，在Spark Core引擎上执行。

b、提供SQL方法，可以创建临时或者全局的数据表，直接写sql语句对数据进行操作。

c、提供与JDBC交互的方法，例如从mysql表读取数据，将结果写入mysql

d、提供与Hive表交互的方法，可以从Hive表读取数据，将结果写入Hive表。

### 3.2 DataFrame创建
DataFrame共三种创建方式

1）从 HDFS文件中

data/appinstall文件：

![](../../assets/lJFhF3sileZP7i/image_006.bin "")
```
public class learnDataFrame {
    public static void main(String[] args) throws AnalyzerException, AnalysisException {
        // 1、新建SparkConf对象，配置集群参数，如程序名、执行集群名、需要的内存和cpu核数
        SparkConf sparkConf = new SparkConf().setAppName("learnDataFrame demo").setMaster("local");

        // 2、基于SparkConf对象初始化SparkSession对象
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();

        // 3、读入输入文件，创建dataFrame
        Dataset<Row> dataFrame = sparkSession.read().json("data/person.json");
        dataFrame.printSchema();
        // root
        // |-- age: long (nullable = true)
        // |-- height: long (nullable = true)
        // |-- name: string (nullable = true)
        // |-- sex: string (nullable = true)
    }
}
```
2）从 外部的数据库表中

3）从 外部的Hive表中

**3.3 类SQL方法**

创建如下DataFrame

```
Dataset<Row> dataFrame = sparkSession.read().json("data/person.json");
// {"name":"周迅","sex":"女","age":18,"height":150}
// {"name":"王菲","sex":"女","age":20,"height":160}
// {"name":"俞飞鸿","sex":"女","age":24,"height":170}
Dataset<Row> dataFrame1 = sparkSession.read().json("data/person1.json");
// {"name":"周迅","sex":"女","age":18,"height":150}
// {"name":"黄龄","sex":"女","age":22,"height":160}
// {"name":"陈道明","sex":"男","age":28,"height":180}
```


|方法名|方法描述|代码示例|
|-|-|-|
|printSchema()|输出shema信息|dataFrame.printSchema();
//root
// |-- age: long (nullable = true)
// |-- height: long (nullable = true)
// |-- name: string (nullable = true)
// |-- sex: string (nullable = true)|
|show(n)|输出前n条数据|dataFrame.show(2);
//+---+------+----+---+
//|age|height|name|sex|
//+---+------+----+---+
//| 18| 150|周迅| 女|
//| 20| 160|王菲| 女|
//+---+------+----+---+
//only showing top 2 rows|
|select()|选择某些列，生成新的DataFrame注意：列的选择采用 内置的 col(“列名”)函数支持对列的值加减，重命名alias等操作如图中的col("age").plus(1).alias("age1"）表示对列age的每一个值加1，并且重命名为age1|dataFrame.select(col("name"),col("age")).show(2);
//+----+---+
//|name|age|
//+----+---+
//|周迅| 18|
//|王菲| 20|
//+----+---+
dataFrame.select(col("name"),col("age").plus(1).alias("age1")).show(2);
//+----+----+
//|name|age1|
//+----+----+
//|周迅| 19|
//|王菲| 21|
//+----+----+|
|cast ()|更改列的类型如图中，age列的类型由long类型变为string类型|dataFrame.printSchema();
//root
// |-- age: long (nullable = true)
// |-- height: long (nullable = true)
// |-- name: string (nullable = true)
// |-- sex: string (nullable = true)
dataFrame.select(col("age").cast(DataTypes.StringType)).printSchema();
//root
// |-- age: string (nullable = true)|
|filter()|按条件对列的值进行过滤，多个条件用and或者or函数关联条件包含如下几种：col("列名").$greater$eq("值") 大于等于col("列名").$greater("值") 大于col("列名").$less$eq("值") 小于等于col("列名").$less("值") 小于col("列名").$eq$eq$eq("值") 等于col("列名").$eq$bang$eq("值") 不等于col("列名").rlike("值") 是否包含值|dataFrame.filter(col("age").$greater("20").and(col("sex").$eq$eq$eq("女"))).show();
//+---+------+------+---+
//|age|height| name|sex|
//+---+------+------+---+
//| 24| 170|俞飞鸿| 女|
//+---+------+------+---+
dataFrame.filter(col("name").rlike("周")).show();
//+---+------+----+---+
//|age|height|name|sex|
//+---+------+----+---+
//| 18| 150|周迅| 女|
//+---+------+----+---+
dataFrame.filter(col("name").rlike("^迅")).show();
//+---+------+----+---+
//|age|height|name|sex|
//+---+------+----+---+
//+---+------+----+---+|
|count()|获取表的总条数|long count = dataFrame.count();
System.out.println("count:" + count);
// count:3|
|groupBy()|按列分组，进行count、sum、max、min等统计操作1、可以一次对单列或者多列进行同一种聚合2、也可以一次对单列或者多列进行多种聚合|// 按多列分组，统计每个分组出现次数
Dataset<Row> groupByCount = dataFrame.groupBy(col("sex"),col("name")).count();
groupByCount.show();
//+---+------+-----+
//|sex| name|count|
//+---+------+-----+
//| 女| 周迅| 1|
//| 女| 王菲| 1|
//| 女|俞飞鸿| 1|
//+---+------+-----+
// 按单列分组，一次对多列进行同一种聚合
Dataset<Row> groupBySum = dataFrame.groupBy(col("sex")).sum("age","height");
groupBySum.show();
//+---+--------+-----------+
//|sex|sum(age)|sum(height)|
//+---+--------+-----------+
//| 女| 62| 480|
//+---+--------+-----------+
// 按列分组，对多列进行多种聚合
Dataset<Row> groupBySum2 = dataFrame.groupBy(col("sex")).agg(sum(col("age")),
 max(col("name")).alias("maxName"));
groupBySum2.show();
//+---+--------+-------+
//|sex|sum(age)|maxName|
//+---+--------+-------+
//| 女| 62| 王菲|
//+---+--------+-------+|
|withColumnRenamed()|对列进行重命名|Dataset<Row> withColumnRenamed = dataFrame1.withColumnRenamed("name", "name1");
withColumnRenamed.show();
//+---+------+------+---+
//|age|height| name1|sex|
//+---+------+------+---+
//| 18| 150| 周迅| 女|
//| 22| 160| 黄龄| 女|
//| 28| 180|陈道明| 男|
//+---+------+------+---+|
|drop()|删除某列|Dataset<Row> drop = groupBySum2.drop(col("sex"));
drop.show();
//+--------+-------+
//|sum(age)|maxName|
//+--------+-------+
//| 62| 王菲|
//+--------+-------+|
|withColumn()| 新增一列，并给列赋新的值|dataFrame.withColumn("newCol", col("age").minus("10").cast(DataTypes.IntegerType)).show();
//+---+------+------+---+------+
//|age|height| name|sex|newCol|
//+---+------+------+---+------+
//| 18| 150| 周迅| 女| 8|
//| 20| 160| 王菲| 女| 10|
//| 24| 170|俞飞鸿| 女| 14|
//+---+------+------+---+------+|
|sort()| 按指定列进行排序|dataFrame.sort(col("name").desc()).show();
//+---+------+------+---+
//|age|height| name|sex|
//+---+------+------+---+
//| 20| 160| 王菲| 女|
//| 18| 150| 周迅| 女|
//| 24| 170|俞飞鸿| 女|
//+---+------+------+---+|
|join ()|对两个dataframe进行连接操作，共包含三个参数第一个参数是需要连接的dataFrame 第二个参数是join时的on条件，多个条件用and函数连接连接的列的列名须不同，可以在join之前对某个dataframe的列名重命名下第三个参数是连接类型，包括 left、right、inner(内连接)、outer(全连接)|Dataset<Row> leftJoin = dataFrame.join(withColumnRenamed,col("name").equalTo(col("name1")), "left");
leftJoin.show();
//+---+------+------+---+----+------+-----+----+
//|age|height| name|sex| age|height|name1| sex|
//+---+------+------+---+----+------+-----+----+
//| 18| 150| 周迅| 女| 18| 150| 周迅| 女|
//| 20| 160| 王菲| 女|null| null| null|null|
//| 24| 170|俞飞鸿| 女|null| null| null|null|
//+---+------+------+---+----+------+-----+----+|
|write()|支持以json格式输出到分布式文件系统支持以csv格式输出到分布式文件系统支持输出到外部sql中|dataFrame.write().json("data/person_json");
dataFrame.write().csv("data/person_csv");|

保存后：

![](../../assets/lJFhF3sileZP7i/image_007.bin "")
![](../../assets/lJFhF3sileZP7i/image_008.bin "")
### 3.4 SQL语句查询 
可以创建临时表或者全局表，采用SQL语句操作数据。

1）创建临时表，进行操作

```
// 创建临时表
dataFrame.createTempView("people");
// 用SQL语句操作数据
Dataset<Row> sqlFrame = sparkSession.sql("select name,age from people limit 2");
sqlFrame.show();
```
2）创建全局表，进行操作，相比于临时表，可以跨不同SparkSession共享同一张表

```
// 创建全局表
dataFrame.createGlobalTempView("people");
sparkSession.sql("select name,age from global_temp.people limit 2").show();
sparkSession.newSession().sql("select name,age from global_temp.people limit 2").show();
//+----+---+
//|name|age|
//+----+---+
//|周迅| 18|
//|王菲| 20|
//+----+---+
```
### 3.5 与JDBC交互
a、添加JDBC的依赖包，如mysql

```
<dependency>
  <groupId>mysql</groupId>
  <artifactId>mysql-connector-java</artifactId>
  <version>8.0.22</version>
</dependency>
```
b、从JDBC表读取数据，如mysql，生成DataFrame

```
Dataset<Row> jdbcDataFrame = sparkSession.read()
        .format("jdbc")
        .option("url", "jdbc:mysql://10.99.200.230:8836/app_demo")
        .option("dbtable", "people")
        .option("user", "work")
        .option("password", "dcs1234")
        .load();
jdbcDataFrame.show(3);
```
c、将DataFrame数据写到JDBC表，如mysql

包含四种写的模式：

 SaveMode.ErrorIfExists 如果数据表已存在，则报错 （默认）

 SaveMode.Ignore 如果数据表已存在，则忽略，不操作也不报错

 SaveMode.Append 如果数据表已存在，则往尾部追加内容

 SaveMode.Overwrite 如果数据表已存在，则直接覆盖

```
jdbcDataFrame.write()
        .format("jdbc")
        .option("url", "jdbc:mysql://10.99.200.230:8836/app_demo")
        .option("dbtable", "people")
        .option("user", "work")
        .option("password", "dcs1234")
        .mode(SaveMode.Ignore)
        .save();
```
### 3.6 DataFrame转Dataset
#### 3.6.1 通过toJSON方法
```
// 通过toJSON方法
Dataset<String> dataSet1 = dataFrame.toJSON();
dataSet1.show();
//+--------------------+
//|               value|
//+--------------------+
//|{"age":18,"height...|
//|{"age":20,"height...|
//|{"age":24,"height...|
//+--------------------+
```
#### 3.6.2 通过as方法
```
// 通过as方法
Encoder personEncoder = Encoders.bean(Person.class);
Dataset<Person> dataSet2 = dataFrame.as(personEncoder);
dataSet2.show();
//+---+------+------+---+
//|age|height|  name|sex|
//+---+------+------+---+
//| 18|   150|  周迅| 女|
//| 20|   160|  王菲| 女|
//| 24|   170|俞飞鸿| 女|
//+---+------+------+---+
```
Person.class(参照 [2.7.1 通过反射机制的方式](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1339414760))

### 3.7 示例代码


```
package org.zj.test;

import org.apache.spark.SparkConf;
import org.apache.spark.sql.*;
import org.apache.spark.sql.types.DataTypes;
import jdk.internal.org.objectweb.asm.tree.analysis.AnalyzerException;
import static org.apache.spark.sql.functions.*;

public class learnDataFrame {
    public static void main(String[] args) throws AnalyzerException, AnalysisException {
        // 1、新建SparkConf对象，配置集群参数，如程序名、执行集群名、需要的内存和cpu核数
        SparkConf sparkConf = new SparkConf().setAppName("learnDataFrame demo").setMaster("local");

        // 2、基于SparkConf对象初始化SparkSession对象
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();

        // 3、读入输入文件，创建dataFrame
        Dataset<Row> dataFrame = sparkSession.read().json("data/person.json");
        // {"name":"周迅","sex":"女","age":18,"height":150}
        // {"name":"王菲","sex":"女","age":20,"height":160}
        // {"name":"俞飞鸿","sex":"女","age":24,"height":170}
        Dataset<Row> dataFrame1 = sparkSession.read().json("data/person1.json");
        // {"name":"周迅","sex":"女","age":18,"height":150}
        // {"name":"黄龄","sex":"女","age":22,"height":160}
        // {"name":"陈道明","sex":"男","age":28,"height":180}

        // 4、类SQL方法
        // printSchema
        dataFrame.printSchema();
        //root
        // |-- age: long (nullable = true)
        // |-- height: long (nullable = true)
        // |-- name: string (nullable = true)
        // |-- sex: string (nullable = true)

        // show
        dataFrame.show(2);
        //+---+------+----+---+
        //|age|height|name|sex|
        //+---+------+----+---+
        //| 18|   150|周迅| 女|
        //| 20|   160|王菲| 女|
        //+---+------+----+---+
        //only showing top 2 rows

        // select
        dataFrame.select(col("name"),col("age")).show(2);
        //+----+---+
        //|name|age|
        //+----+---+
        //|周迅| 18|
        //|王菲| 20|
        //+----+---+
        dataFrame.select(col("name"),col("age").plus(1).alias("age1")).show(2);
        //+----+----+
        //|name|age1|
        //+----+----+
        //|周迅|  19|
        //|王菲|  21|
        //+----+----+

        // cast
        dataFrame.printSchema();
        //root
        // |-- age: long (nullable = true)
        // |-- height: long (nullable = true)
        // |-- name: string (nullable = true)
        // |-- sex: string (nullable = true)
        dataFrame.select(col("age").cast(DataTypes.StringType)).printSchema();
        //root
        // |-- age: string (nullable = true)


        // filter
        dataFrame.filter(col("age").$greater("20").and(col("sex").$eq$eq$eq("女"))).show();
        //+---+------+------+---+
        //|age|height|  name|sex|
        //+---+------+------+---+
        //| 24|   170|俞飞鸿| 女|
        //+---+------+------+---+
        dataFrame.filter(col("name").rlike("周")).show();
        //+---+------+----+---+
        //|age|height|name|sex|
        //+---+------+----+---+
        //| 18|   150|周迅| 女|
        //+---+------+----+---+
        dataFrame.filter(col("name").rlike("^迅")).show();
        //+---+------+----+---+
        //|age|height|name|sex|
        //+---+------+----+---+
        //+---+------+----+---+

        // count
        long count = dataFrame.count();
        System.out.println("count:" + count);
        // count:3

        // groupBy
        // 按多列分组，统计每个分组出现次数
        Dataset<Row> groupByCount = dataFrame.groupBy(col("sex"),col("name")).count();
        groupByCount.show();
        //+---+------+-----+
        //|sex|  name|count|
        //+---+------+-----+
        //| 女|  周迅|    1|
        //| 女|  王菲|    1|
        //| 女|俞飞鸿|    1|
        //+---+------+-----+
        // 按单列分组，一次对多列进行同一种聚合
        Dataset<Row> groupBySum = dataFrame.groupBy(col("sex")).sum("age","height");
        groupBySum.show();
        //+---+--------+-----------+
        //|sex|sum(age)|sum(height)|
        //+---+--------+-----------+
        //| 女|      62|        480|
        //+---+--------+-----------+
        // 按列分组，对多列进行多种聚合
        Dataset<Row> groupBySum2 = dataFrame.groupBy(col("sex")).agg(sum(col("age")),
                max(col("name")).alias("maxName"));
        groupBySum2.show();
        //+---+--------+-------+
        //|sex|sum(age)|maxName|
        //+---+--------+-------+
        //| 女|      62|   王菲|
        //+---+--------+-------+

        // withColumnRenamed
        Dataset<Row> withColumnRenamed = dataFrame1.withColumnRenamed("name", "name1");
        withColumnRenamed.show();
        //+---+------+------+---+
        //|age|height| name1|sex|
        //+---+------+------+---+
        //| 18|   150|  周迅| 女|
        //| 22|   160|  黄龄| 女|
        //| 28|   180|陈道明| 男|
        //+---+------+------+---+

        // drop
        Dataset<Row> drop = groupBySum2.drop(col("sex"));
        drop.show();
        //+--------+-------+
        //|sum(age)|maxName|
        //+--------+-------+
        //|      62|   王菲|
        //+--------+-------+

        // withColumn
        dataFrame.withColumn("newCol", col("age").minus("10").cast(DataTypes.IntegerType)).show();
        //+---+------+------+---+------+
        //|age|height|  name|sex|newCol|
        //+---+------+------+---+------+
        //| 18|   150|  周迅| 女|     8|
        //| 20|   160|  王菲| 女|    10|
        //| 24|   170|俞飞鸿| 女|    14|
        //+---+------+------+---+------+

        // sort
        dataFrame.sort(col("name").desc()).show();
        //+---+------+------+---+
        //|age|height|  name|sex|
        //+---+------+------+---+
        //| 20|   160|  王菲| 女|
        //| 18|   150|  周迅| 女|
        //| 24|   170|俞飞鸿| 女|
        //+---+------+------+---+

        // join
        Dataset<Row> leftJoin = dataFrame.join(withColumnRenamed,col("name").equalTo(col("name1")), "left");
        leftJoin.show();
        //+---+------+------+---+----+------+-----+----+
        //|age|height|  name|sex| age|height|name1| sex|
        //+---+------+------+---+----+------+-----+----+
        //| 18|   150|  周迅| 女|  18|   150| 周迅|  女|
        //| 20|   160|  王菲| 女|null|  null| null|null|
        //| 24|   170|俞飞鸿| 女|null|  null| null|null|
        //+---+------+------+---+----+------+-----+----+

        // write
        dataFrame.write().json("data/person_json");
        dataFrame.write().csv("data/person_csv");

        // 5、SQL语句查询
        // 创建临时表
        dataFrame.createTempView("people");
        // 用SQL语句操作数据
        Dataset<Row> sqlFrame = sparkSession.sql("select name,age from people limit 2");
        sqlFrame.show();

        // 创建全局表
        dataFrame.createGlobalTempView("people");
        sparkSession.sql("select name,age from global_temp.people limit 2").show();
        sparkSession.newSession().sql("select name,age from global_temp.people limit 2").show();
        //+----+---+
        //|name|age|
        //+----+---+
        //|周迅| 18|
        //|王菲| 20|
        //+----+---+

        // 6、DataFrame转Dataset
        // 通过toJSON方法
        Dataset<String> dataSet1 = dataFrame.toJSON();
        dataSet1.show();
        //+--------------------+
        //|               value|
        //+--------------------+
        //|{"age":18,"height...|
        //|{"age":20,"height...|
        //|{"age":24,"height...|
        //+--------------------+

        // 通过as方法
        Encoder personEncoder = Encoders.bean(Person.class);
        Dataset<Person> dataSet2 = dataFrame.as(personEncoder);
        dataSet2.show();
        //+---+------+------+---+
        //|age|height|  name|sex|
        //+---+------+------+---+
        //| 18|   150|  周迅| 女|
        //| 20|   160|  王菲| 女|
        //| 24|   170|俞飞鸿| 女|
        //+---+------+------+---+
    }
}
```
## 四、Dataset操作
### 4.1 说明
Dataset是从Spark 1.6开始引入的一个新的数据类型，Dataset存储的是强类型的数据（如Dataset<String>），所以，使用DataSet方法，需要Encoder类来指定数据的具体类型。

由于DataSet存储的是强类型的数据，在编译时，会做类型正确性校验。 注： DataFrame作为Dataset的一个特例，存储的是无类型的数据（格式是：Dataset<Row>），编译时不做类型校验

Dataset可以使用 DataFrame的方法（如select、group、sql语言查询等）和RDD的方法（如map、filter、reduce等），能较方便的进行数据操作。

### 4.2 Dataset创建
通常情况下，Dataset是通过DataFrame转换而来的。

### 4.3 Encoder类创建
Dataset通过Encoder类序列化处理对象并在网络上传输而不是使用Java serialization或者Kryo方式。

尽管Encoder和标准序列化方式都是将对象转换为字节，但是Encoder是动态生成代码的，并且允许Spark在不需要反序列化的情况下执行许多操作，比如：过滤，排序，哈希等。

1) 基本类型的 Encoder类创建

```
// 基本类型的  Encoder类创建
Encoder<String> stringEncoder = Encoders.STRING();
Encoder<Integer> intEncoder = Encoders.INT();
Encoder<Double> doubleEncoder = Encoders.DOUBLE();
```
2) 自定义类的 Encoder类创建

使用bean方法，Person.class(参照 [2.7.1 通过反射机制的方式](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1339414760))

```
// 自定义类的  Encoder类创建，使用bean方法
Encoder personEncoder = Encoders.bean(Person.class);
Dataset<Person> dataSet = dataFrame.as(personEncoder);
dataSet.show();
```
### 4.4 Dataset方法
Dataset可以使用 DataFrame的方法（如select、group、sql语言查询等）和RDD的方法（如map、filter、reduce等），能较方便的进行数据操作。

注：使用RDD的方法时，不能用lambda表达式，需要用匿名内部类的方法写。

### 4.5 Dataset转RDD
 调用.toJavaRDD()方法

```
JavaRDD<Person> rdd = dataSet.toJavaRDD();
```


![](/personal-site-mvp/img/docs-assets/image_009_3.png "")

