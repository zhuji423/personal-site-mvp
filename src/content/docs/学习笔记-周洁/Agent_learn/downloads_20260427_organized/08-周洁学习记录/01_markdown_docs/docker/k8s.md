---
title: "位于名字空间中的资源"
description: "Docker运行可方便了，为什么要用K8S，它有什么优势？ 传统的后端部署办法：把程序包（包括可执行二进制文件、配置文件等）放到服务器上，接着运行启动脚本把程序跑起来，同时启动守护脚本定期检查程序运行状态、必要的话重新拉起程序。"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\k8s.md"
---
k8s

### 一、k8s的诞生
> 什么是k8s？
**K8S是负责自动化运维管理多个Docker程序的集群**。

> Docker运行可方便了，为什么要用K8S，它有什么优势？
传统的后端部署办法：把程序包（包括可执行二进制文件、配置文件等）放到服务器上，接着运行启动脚本把程序跑起来，同时启动守护脚本定期检查程序运行状态、必要的话重新拉起程序。

存在的问题在于：**如果服务的请求量上来，已部署的服务响应不过来怎么办？**传统的做法往往是，如果请求量、内存、CPU超过阈值做了告警，运维马上再加几台服务器，部署好服务之后，接入负载均衡来分担已有服务的压力。

从监控告警到部署服务，中间需要人力介入！而**K8S可以自动完成服务的部署、更新、卸载和扩容、缩容**。

### 二、架构
K8S是属于**主从设备模型（Master-Slave架构）**，即有Master节点负责核心的调度、管理和运维，Slave节点则在执行用户的程序。**所有Master Node和Worker Node组成了K8S集群**，同一个集群可能存在多个Master Node和Worker Node。

* K8S的Master Node具备：请求入口管理（API Server），Worker Node调度（Scheduler），监控和自动调节（Controller Manager），以及存储功能（etcd）；
* 而K8S的Worker Node具备：状态和监控收集（Kubelet），网络和负载均衡（Kube-Proxy）、保障容器化运行环境（Container Runtime）、以及定制化功能（Add-Ons）。

![](/personal-site-mvp/img/doc-placeholder.svg "")
|**概念**|**节点**|**解释**|
|-|-|-|
|**主机（Master）**|-| 用于控制 Kubernetes 节点的计算机。所有任务分配都来自于此。|
|**节点（Node）**|-|负责执行请求和所分配任务的计算机。由 Kubernetes 主机负责对节点进行控制。|
|**API Server**|**Master Node**|**K8S的请求入口服务**。API Server组件主要提供认证与授权、运行一组准入控制器以及管理API版本等功能，通过REST API向外提供服务，允许各类组件创建、读取、写入、更新和监视资源（Pod, Deployment, Service等）。|
|**Scheduler**||**K8S所有Worker Node的调度器**。Scheduler组件，根据集群资源和状态选择合适的节点用于创建Pod。|
|**Controller Manager**||**K8S所有Worker Node的监控器**。Controller Manager组件，实现ReplicaSet的行为。|
|**etcd**||**K8S的存储服务**。etcd存储了K8S的关键配置和用户配置，K8S中仅API Server才具备读写权限，其他组件必须通过API Server的接口才能读写数据。|
|**Kubelet**|**Worker Node**|**Worker Node的监视器，以及与Master Node的通讯器**。Kubelet是Master Node安插在Worker Node上的“眼线”，它会定期向Master Node汇报自己Node上运行的服务的状态，并接受来自Master Node的指示采取调整措施。|
|**Kube-Proxy**||**K8S的网络代理**。私以为称呼为Network-Proxy可能更适合？Kube-Proxy负责Node在K8S的网络通讯、以及对外部网络流量的负载均衡。|
|**Container Runtime**||**Worker Node的运行环境**。即安装了容器化所需的软件环境确保容器化程序能够跑起来，比如Docker Engine。大白话就是帮忙装好了Docker运行环境。|
|**Logging Layer**||**K8S的监控状态收集器**。私以为称呼为Monitor可能更合适？Logging Layer负责采集Node上所有服务的CPU、内存、磁盘、网络等监控项信息。|
|**Add-Ons**||**K8S管理运维Worker Node的插件组件**。有些文章认为Worker Node只有三大组件，不包含Add-On，但笔者认为K8S系统提供了Add-On机制，让用户可以扩展更多定制化功能，是很不错的亮点。|
|**容器集（Pod）**||被部署在单个节点上的，且包含一个或多个容器的容器组。同一容器集中的所有容器共享同一个 IP 地址、IPC、主机名称及其它资源。容器集会将网络和存储从底层容器中抽象出来。这样就能更加轻松地在集群中移动容器。|
|**复制控制器（Replication controller）**||用于控制应在集群某处运行的完全相同的容器集副本数量。|
|**服务（Service）**||将工作内容与容器集分离。Kubernetes 服务代理会自动将服务请求分发到正确的容器集——无论这个容器集会移到集群中的哪个位置，甚至可以被替换掉。|
|**kubectl**||Kubernetes 的命令行配置工具。|

### 三、一些重要概念
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### Pod 实例
Pod是可以在 Kubernetes 中创建和管理的、最小的可部署的计算单元。

在同一个Pod里的几个Docker服务/程序，好像被部署在同一台机器上，可以通过localhost互相访问，并且可以共用Pod里的存储资源。

一个最简单的Pod的yaml：[官方网站](https://link.zhihu.com/?target=https%3A//kubernetes.io/zh/docs/tasks/configure-pod-container/assign-memory-resource/)

```
apiVersion: v1
kind: Pod
metadata:
  name: memory-demo
  namespace: mem-example
spec:
  containers:
  - name: memory-demo-ctr
    image: polinux/stress
    resources:
      limits:
        memory: "200Mi"
      requests:
        memory: "100Mi"
    command: ["stress"]
    args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
    volumeMounts:
    - name: redis-storage
      mountPath: /data/redis
  volumes:
  - name: redis-storage
    emptyDir: {}
```
* `apiVersion`记录K8S的API Server版本，现在看到的都是`v1`，用户不用管。
* `kind`记录该yaml的对象，比如这是一份Pod的yaml配置文件，那么值内容就是`Pod`。
* `metadata`记录了Pod自身的元数据，比如这个Pod的名字、这个Pod属于哪个namespace（同一个命名空间内的对象互相可见）。
* `spec`记录了Pod内部所有的资源的详细信息（重要）：
    * `containers`记录了Pod内的容器信息，`containers`包括了：`name`容器名，`image`容器的镜像地址，`resources`容器需要的CPU、内存、GPU等资源，`command`容器的入口命令，`args`容器的入口参数，`volumeMounts`容器要挂载的Pod数据卷等。可以看到，上述这些信息都是启动容器的必要和必需的信息。
    * `volumes`记录了Pod内的数据卷信息。


##### Volume 数据卷
K8S支持很多类型的volume数据卷挂载：[K8S卷](https://link.zhihu.com/?target=https%3A//kubernetes.io/zh/docs/concepts/storage/volumes/)

数据卷volume是**Pod内部的磁盘资源**。

volume与volumeMounts关系：volume是K8S的对象，对应一个实体的数据卷；而volumeMounts只是container的挂载点，对应container的其中一个参数。volumeMounts依赖于volume，只有当Pod内有volume资源的时候，该Pod内部的container才可能有volumeMounts。

##### Container 容器
一个Pod内可以有多个容器container。

在Pod中，容器也有分类：

* 标准容器 Application Container。
* 初始化容器 Init Container。
* 边车容器 Sidecar Container。
* 临时容器 Ephemeral Container。

一般来说，部署的大多是标准容器（ Application Container）。

##### Deployment 和 ReplicaSet
Deployment的作用是管理和控制Pod和ReplicaSet，管控它们运行在用户期望的状态中。

ReplicaSet的作用就是管理和控制Pod，管控他们好好干活。但是，ReplicaSet受控于Deployment。形象来说，ReplicaSet就是总包工头手下的小包工头。

![](/personal-site-mvp/img/doc-placeholder.svg "")
用户会直接操作Deployment部署服务，而当Deployment被部署的时候，K8S会自动生成要求的ReplicaSet和Pod。在[K8S官方文档](https://link.zhihu.com/?target=https%3A//www.kubernetes.org.cn/replicasets)中也指出用户只需要关心Deployment而不操心ReplicaSet。

还有一个类似的概念**ReplicationController**。ReplicationController 确保一个 Pod 或一组同类的 Pod 总是可用的。ReplicationController是ReplicaSet的前身”，官方也**推荐用Deployment取代ReplicationController来部署服务**。

##### Service和Ingress
前文介绍的Deployment、ReplicationController和ReplicaSet主要管控Pod程序服务；那么，Service和Ingress则负责管控Pod网络服务。

K8S中的服务（Service）更像是网关层，是若干个Pod的流量入口、流量均衡器。

**Service是K8S服务的核心，屏蔽了服务细节，统一对外暴露服务接口，真正做到了“微服务”**。举个例子，我们的一个服务A，部署了3个备份，也就是3个Pod；对于用户来说，只需要关注一个Service的入口就可以，而不需要操心究竟应该请求哪一个Pod。优势非常明显：**一方面外部用户不需要感知因为Pod上服务的意外崩溃、K8S重新拉起Pod而造成的IP变更，外部用户也不需要感知因升级、变更服务带来的Pod替换而造成的IP变化，另一方面，Service还可以做流量负载均衡**。

Service主要负责K8S集群内部的网络拓扑。Ingress负责集群外部怎么访问集群内部呢？这个时候就需要Ingress了。Ingress是整个K8S集群的接入层，复杂集群内外通讯。

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### namespace 命名空间
前文提到的概念都是为了服务Pod的，而namespace则是为了服务整个K8S集群的。

**namespace是为了把一个K8S集群划分为若干个资源不可共享的虚拟集群而诞生的**。

在同一个namespace下deployment不能同名；但是不同namespace之间没有影响；前文提到的所有对象，都是在namespace下的；也有一些对象是不隶属于namespace的，而是在K8S集群内全局可见的，查看命令：

```
# 位于名字空间中的资源
kubectl api-resources --namespaced=true
​
# 不在名字空间中的资源
kubectl api-resources --namespaced=false
```
### 四、API Server
#### API Object
|**资源对象**|**特点**|**创建**|
|-|-|-|
|Pod|K8s中**最为重要**的概念，其他对象仅仅是在管理、暴露pod或者被pod使用。|创建pod时指定标签：![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=7f6c823f6a9855ccea45e0cc8443d744 "")使用标签和选择器来约束pod调度：比如将pod调度到包含`gpu=true`的节点：![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=a876b129d69a4c06ccfa33f21ac1c00e "")|
|ReplicationController|旨在创建和管理一个pod的多个副本（replicas）会持续监控正在运行的pod列表， 并保证相应” 类型” 的pod的数目与期望相符|RC有三个主要部分标签选择器（label selector）， 用于确定ReplicationController作用域中有哪些pod副本个数（replica count），指定应运行的pod数量Pod 模板（pod template），用于创建新的pod 副本![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=18f8fe712b4b51f3dfa1bd3094e0d6a8 "")|
|ReplicaSet|新一代的ReplicaController，并且将其完全替换，与ReplicaController相比，ReplicaSet的pod选择器的表达能力更强。ReplicaSet可以给选择器添加额外的表达式，表达式支持以下四个有效的运算符In：Label的值必须与其中一个指定的values 匹配。NotIn：Label的值与任何指定的values 不匹配。Exists：pod 必须包含一个指定名称的标签（值不重要）。使用此运算符时，不应指定values字段。DoesNotExist：pod不得包含有指定名称的标签。values属性不得指定。|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=eff40e2b0057c3f4130da928561eb6a6 "")|
|DaemonSet|当希望pod在集群的每个节点运行时、并且每个节点都需要正好一个运行的pod实例时，比如我们希望在每个节点上运行日志收集器和资源监控器，就要用DaemonSet。|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=8611d9fd9a35e37159a7d3bfce6f8ea7 "")|
|Job|RC、RS、DS会持续运行任务，永远达不到完成态，但是有些任务只需要它运行一次，并在完成工作后就终止任务。Job创建并管理的pod，该pod在内部进程**成功结束**时，不重启容器，即一旦任务完成，pod就被认为处于完成状态。Job对于临时任务很有用，关键是任务要以正确的方式结束，可以在未托管的pod中运行任务并等待它完成|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e4aae674997db524fd9a41888af42cca "")支持顺序运行、并行运行、限制Job pod完成任务的时间等特性|
|CronJob|Job资源在创建时会立刻运行pod，CronJob则支持定期运行或将来运行一次的Job。|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=7c63f640eb24607c4e701f6769a551a2 "")|
|service|它能为一组功能相同的pod提供单一不变的接入点的资源。当服务存在时，它的IP地址和端口不会改变，客户端通过IP地址和端口号建立连接，这些连接会被**路由**到提供该服务的任意一个pod上。![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=cdbcd79517d592700a4db369958e77b4 "")|创建服务：这个名称为kubia的服务，它将在端口80接收请求并将连接路由到具有标签选择器是app=kubia的pod的8080端口上![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=f509ab233f87f66bbc5ad7b4b0ec1100 "")服务发现环境变量：![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=93e0afc2e6cafee124be94c43ad09647 "")DNS发现服务：K8s下有一个被称作kube-dns的pod，这个pod运行DNS服务，在集群中的其他pod 都被配置成**使用其作为dns** ( Kubemetes 通过修改每个容器的/etc/resolv.conf 文件实现）。运行在pod 上的进程DNS 查询都会被Kubemetes自身的DNS 服务器响应，该服务器知道系统中运行的所有服务。|
|Deployment|Deployment 是一种更高阶资源，用于部署应用程序并以声明的方式升级应用，而不是通过 ReplicationController 或 ReplicaSet 进行部署， 它们都被认为是更底层的概念![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e38c20aaba7391b19dcdcb5b75c66c6b "")|在升级应用程序时， 需要引入一个额外的ReplicationController, 并协调两个 Controller, 使它们再根据彼此不断修改， 而不会造成干扰。 所以需要另一个资源用来协调。 Deployment 资源就是用来负责处理这个问题的创建Deployment与创建ReplicationController并没有任何区别。Deployment也是由标签选择器、期望副数和pod模板组成的。此外，它还包含另一个字段，指定一个部署策略，该策略定义在修改Deployment资源时应该如何执行更新。|
|configMap|k8s允许将配置选项分离到单独的资源对象configMap中，本质上就是一个键/值对映射，值可以是一个短字面量，也可以是完整的配置文件。将配置存放在独立的资源对象中，有助于在不同环境下拥有多份同名配置清单。pod是通过名称引用configMap的，因此可以在多环境下使用相同的pod定义描述，同时保持不同的配置项以适应不同的环境|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=dfc5e1a8398ca89bcddc97a0e42b9821 "")|
|Secret|用于存储和分发敏感数据，如证书和私钥。 Secret 结构与 ConfigMap类似，均是键／值对的映射。k8s把Secret仅分发到需要访问Secret的pod所在的机器节点上来保障其安全性。另外，为了防止从硬盘窃取敏感数据，Secret只会存储在节点的内存中，永不写入物理存储。对于主节点本身（尤其是etcd），secret以非加密形式存储（k8s1.7以后开始加密存储）。|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=70f430389662ee7bc5ad24c189ba6e4f "")|

#### 将服务暴露给外部
|**方式**|**配置清单**|**请求流程**|
|-|-|-|
|将服务的类型设置成NodePort：通过创建NodePort服务， 可以让Kubemetes在其所有节点上保留一个端口（所有节点上都使用相同的端口号）， 并将在该端口上接收到的流量重定向到基础服务。|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=34ef34bc34588bc4ea767dd30b8e67f9 "")|服务暴露在两个集群节点的端口30123上。外部请求到达任何一个端口的传入连接将被重定向到一个随机选择的pod，该pod是否位于接收到连接的节点上是不确定的，在第一个节点的端口30123收到的连接， 可以被重定向到第一节点个上运行的pod, 也可能是第二个节点上运行的pod![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=91324c3c95d58cf588d656f60e719543 "")|
|将服务类型设置成LoadBalance：它是NodePort类型的一种扩展，是K8s集群外部的一个专用的负载均衡器，K8s对此进行了支持，需要做的就是设置服务的类型为Load Balance而不是NodePort。负载均衡器拥有自己独一无二的可公开访问的IP 地址， 并将所有连接重定向到服务。可以通过负载均衡器的IP 地址访问服务|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=cecea2ac1d8bd88f174c685473b8e72a "")|外部客户端连接到负载均衡器的80端口，并路由到其中一个节点上的隐式分配节点端口。之后该连接被转发到一个pod实例![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=a45f0edb9c0ff64d2a234e18f63496a5 "")|
|创建一个Ingress资源|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=01b2b51718596fb277fbf10530623669 "")|客户端首先对[kubia.example.com](http://kubia.example.com/) 执行DNS 查找， DNS服务器返回了Ingress 控制器的IP 。客户端然后向Ingress 控制器发送HTTP 请求，并在Host头中指定[kubia.example.com](http://kubia.example.com/)。控制器从该头部确定客户端尝试访问哪个服务，并通过服务选择一个pod，并将客户端的请求转发给其中一个pod![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=09fc3bbc2b50e5abed36eb582cfa1684 "")|

### 五、实际应用
#### 安装部署
[k8s搭建](./k8s_引用文档/k8s搭建.md)

#### 常用命令
### 六、扩展
调度器、device-plugin、容器运行时运行机制、容器网络、RDMA通信

Kubeflow、Volcano

### 附录
[https://kubernetes.io/zh-cn/docs/concepts/](https://kubernetes.io/zh-cn/docs/concepts/)

[K8S系列一：概念入门](https://zhuanlan.zhihu.com/p/292081941?t=mention&mt=doc&dt=sdk)

[K8S](./k8s_引用文档/K8S.md)


