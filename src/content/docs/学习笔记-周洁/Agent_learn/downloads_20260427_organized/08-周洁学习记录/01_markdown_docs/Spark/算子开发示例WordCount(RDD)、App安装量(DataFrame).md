---
title: "一、WordCount算子开发示例(RDD)"
description: "算子开发示例WordCountRDD、App安装量DataFrame"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Spark\\算子开发示例WordCount(RDD)、App安装量(DataFrame).md"
---
算子开发示例WordCount(RDD)、App安装量(DataFrame)



环境配置：[Maven开始第一个项目](../Maven/Maven开始第一个项目.md)

# 一、WordCount算子开发示例(RDD)
## 1.1 引入Spark依赖包
pom.xml文件引入Spark依赖

```
<!-- https://mvnrepository.com/artifact/org.apache.spark/spark-sql -->
<dependency>
  <groupId>org.apache.spark</groupId>
  <artifactId>spark-sql_2.12</artifactId>
  <version>3.0.1</version>
</dependency>
```
## 1.2 创建本地测试文件
创建data/wordFile文件，文件中每行的单词用逗号隔开

![](../../../_remote_images/08-周洁学习记录/local_assets/IunjADfIEVOuh3/image_001.bin "")
## 1.3 编写WordCount.java代码
```
package org.zj.test;

import org.apache.spark.SparkConf;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;
import java.util.Arrays;


/**
 * 使用RDD的方式进行word出现次数的统计
 */

public class WordCount {
    public static void main(String[] args){
        // 1、新建SparkConf对象，配置集群参数，如程序名、执行集群名、需要的内存和cpu核数
        SparkConf sparkConf = new SparkConf().setAppName("WordCount demo").setMaster("local");

        // 2、基于SparkConf对象初始化SparkSession对象
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();

        // 3、基于SparkSession对象创建JavaSparkContext对象，用于与集群资源管理器做交互
        JavaSparkContext sc = JavaSparkContext.fromSparkContext(sparkSession.sparkContext());

        // 4、读取输入文件夹，创建rdd
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
    }
}
```
![](../../../_remote_images/08-周洁学习记录/local_assets/IunjADfIEVOuh3/image_002.bin "")
## 1.4 运行
本地Run程序快捷键shift+control+r，生成运行结果放在data/wordFileResult目录下

![](../../../_remote_images/08-周洁学习记录/local_assets/IunjADfIEVOuh3/image_003.bin "")
## 1.5 提交到集群运行
[https://blog.csdn.net/lovechendongxing/article/details/81748004](https://blog.csdn.net/lovechendongxing/article/details/81748004)

Spark 分布式集群部署 [https://www.cnblogs.com/zengxiaoliang/p/6478859.html](https://www.cnblogs.com/zengxiaoliang/p/6478859.html)

# 二、App安装量算子开发示例(DataFrame)
## 2.1 创建项目引入依赖包
pom.xml文件：

![](../../../_remote_images/08-周洁学习记录/local_assets/IunjADfIEVOuh3/image_004.bin "")
## 2.2 创建本地测试文件
创建data/appinstall文件，文件中每行是一个json串

![](../../../_remote_images/08-周洁学习记录/local_assets/IunjADfIEVOuh3/image_005.bin "")
## 2.3 编写AppInstall.java代码
```
package org.zj.test;

import org.apache.spark.SparkConf;
import org.apache.spark.sql.AnalysisException;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import jdk.internal.org.objectweb.asm.tree.analysis.AnalyzerException;

public class AppInstall {
    public static void main(String[] args) throws AnalyzerException, AnalysisException {
        // 1、新建SparkConf对象，配置集群参数，如程序名、执行集群名、需要的内存和cpu核数
        SparkConf sparkConf = new SparkConf().setAppName("AppInstall demo").setMaster("local");

        // 2、基于SparkConf对象初始化SparkSession对象
        SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();

        // 3、读入输入文件，创建dataFrame
        Dataset<Row> dataFrame = sparkSession.read().json("data/appinstall");

        // 4、创建临时表，发现写sql操作
        dataFrame.createTempView("appInfo");

        // 5、统计app安装量，按userId去重
        Dataset<Row> resultFrame = sparkSession.sql("select appName, count(distinct(userId)) as installNum " +
                "from appInfo group by appName");
        // 6、将统计结果以json输出到文件中
        resultFrame.repartition(1).write().json("data/resultAppInstall");
    }
}
```
## 2.4 运行
本地Run程序快捷键shift+control+r，生成运行结果放在data/resultAppInstall目录下

![](../../../_remote_images/08-周洁学习记录/local_assets/IunjADfIEVOuh3/image_006.bin "")
## 2.5 提交到集群运行
[https://blog.csdn.net/lovechendongxing/article/details/81748004](https://blog.csdn.net/lovechendongxing/article/details/81748004)

Spark 分布式集群部署 [https://www.cnblogs.com/zengxiaoliang/p/6478859.html](https://www.cnblogs.com/zengxiaoliang/p/6478859.html)




