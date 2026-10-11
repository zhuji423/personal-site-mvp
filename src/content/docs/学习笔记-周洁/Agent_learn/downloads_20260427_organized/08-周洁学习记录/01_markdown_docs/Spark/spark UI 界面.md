---
title: "spark UI 界面"
description: "spark UI 界面"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Spark\\spark UI 界面.md"
---
spark UI 界面

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 一、spark UI 界面
![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_001.bin "")
![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_002.bin "")
任务运行过程中是UI详情界面，运行结束后：

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_003.bin "")
## 二、UI界面构成
### job页面
在里面可以看到当前应用分析出来的所有任务，以及所有的excutors中action的执行时间。页面分为两部分，一部分是event timeline，另一部分是进行中和完成的job任务。

第一部分event timeline展开后，可以看到executor创建的时间点，以及某个action触发的算子任务，执行的时间。通过这个时间图，可以快速的发现应用的执行瓶颈，触发了多少个action。

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_004.bin "")
第二部分的图表，显示了触发action的job名字，它通常是某个count,collect等操作。

count at QueryCovSelect.java:79描述了action的名字和所在的行号，通过它可以直接定位到任务所属的代码，帮助调试分析。Duration显示了该action的耗时，通过它也可以对代码进行专门的优化。最后的进度条，显示了该任务失败和成功的次数，如果有失败的就需要引起注意，因为这种情况在生产环境可能会更普遍更严重。点击能进入该action具体的分析页面，可以看到DAG图等详细信息。

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_005.bin "")
### stage页面
在里面可以看到应用的所有stage，stage是按照宽依赖来区分的，因此粒度上要比job更细一些。标记了每个rdd从创建到应用的一个流程图，也是进行分析和调优很重要的内容。

窄依赖是指前一个rdd计算能出一个唯一的rdd，比如map或者filter等；宽依赖则是指多个rdd生成一个或者多个rdd的操作，比如groupbykey reducebykey等，这种宽依赖通常会进行shuffle。

因此Spark会根据宽窄依赖区分stage，某个stage作为专门的计算，计算完成后，会等待其他的executor，然后再统一进行计算。

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_006.bin "")
### storage页面
所做的cache persist等操作，都会在这里看到，可以看出来应用目前使用了多少缓存，点击进去可以看到具体在每个机器上，使用的block的情况。

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_007.bin "")
查看ShuffledRDD详情

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_008.bin "")
### environment页面
里面展示了当前spark所依赖的环境，比如jdk,lib等等

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_009.bin "")
### executors页面
这里可以看到执行者申请使用的内存以及shuffle中input和output等数据 这个页面比较常用了，一方面通过它可以看出来每个excutor是否发生了数据倾斜，另一方面可以具体分析目前的应用是否产生了大量的shuffle，是否可以通过数据的本地性或者减小数据的传输来减少shuffle的数据量。

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_010.bin "")
查看工作目录

![](../../../_remote_images/08-周洁学习记录/local_assets/8sBRqYG588pd7C/image_011.bin "")
## 三、调试总结
1 输出信息

在数据量很大的时候，做一些show()（默认显示20），count() 或者 take(10)进行分析。

2 内存不够

当任务失败，收到sparkContext shutdown的信息时，基本都是执行者的内存不够。这个时候，一方面可以调大--excutor-memory参数，另一方面还是得回去看看程序。如果受限于系统的硬件条件，无法加大内存，可以采用局部调试法，检查是在哪里出现的内存问题。程序分成几个步骤，一步一步的打包运行，最后检查出现问题的点。

3 ThreadPool

线程池不够，这个是因为--excutor-core给的太少了，出现线程池不够用的情况。需要调整参数的配置。

4 physical memory不够

这种问题一般是driver memory不够导致的，driver memory通常存储了以一些调度方面的信息，这种情况很有可能是调度过于复杂，或者是内部死循环导致。

5 合理利用缓存

在Spark的计算中，不太建议直接使用cache，万一cache的量很大，可能导致内存溢出。可以采用persist的方式，指定缓存的级别为MEMORY_AND_DISK,这样在内存不够的时候，可以把数据缓存到磁盘上。另外，要合理的设计代码，恰当地使用广播和缓存，广播的数据量太大会对传输带来压力，缓存过多未及时释放，也会导致内存占用。一般来说，代码在需要重复使用某一个rdd的时候，才需要考虑进行缓存，并且在不使用的时候，要及时unpersist释放。

6 尽量避免shuffle

这个点，在优化的过程中是很重要的。比如需要把两个rdd按照某个key进行groupby，然后在进行leftouterjoin，这个时候一定要考虑大小表的问题。如果把大表关联到小表，那么性能很可能会很惨。而只需要简单的调换一下位置，性能就可能提升好几倍。

原理：[https://www.cnblogs.com/yy3b2007com/p/10847253.html](https://www.cnblogs.com/yy3b2007com/p/10847253.html)
