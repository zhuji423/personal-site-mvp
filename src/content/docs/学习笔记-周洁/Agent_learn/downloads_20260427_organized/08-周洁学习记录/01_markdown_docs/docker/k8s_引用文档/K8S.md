---
title: "K8S"
description: "服务发现和负载均衡"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\k8s_引用文档\\K8S.md"
---
K8S

## 一、简介
Kubernetes 是一个可移植的、可扩展的开源平台，用于管理容器化的工作负载和服务，可促进声明式配置和自动化。 Kubernetes 拥有一个庞大且快速增长的生态系统。Kubernetes 的服务、支持和工具广泛可用。它将组成应用程序的容器组合成逻辑单元，以便于管理和服务发现。 Kubernetes 为你提供了一个可弹性运行分布式系统的框架。 Kubernetes 会满足你的扩展要求、故障转移、部署模式等。

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_001.bin "")
Kubernetes 为你提供：

* **服务发现和负载均衡**

Kubernetes 可以使用 DNS 名称或自己的 IP 地址公开容器，如果进入容器的流量很大， Kubernetes 可以负载均衡并分配网络流量，从而使部署稳定。

* **存储编排**

Kubernetes 允许你自动挂载你选择的存储系统，例如本地存储、公共云提供商等。

* **自动部署和回滚**

你可以使用 Kubernetes 描述已部署容器的所需状态，它可以以受控的速率将实际状态 更改为期望状态。例如，你可以自动化 Kubernetes 来为你的部署创建新容器， 删除现有容器并将它们的所有资源用于新容器。

* **自动完成装箱计算**

Kubernetes 允许你指定每个容器所需 CPU 和内存（RAM）。 当容器指定了资源请求时，Kubernetes 可以做出更好的决策来管理容器的资源。

* **自我修复**

Kubernetes 重新启动失败的容器、替换容器、杀死不响应用户定义的 运行状况检查的容器，并且在准备好服务之前不将其通告给客户端。

* **密钥与配置管理**

Kubernetes 允许你存储和管理敏感信息，例如密码、OAuth 令牌和 ssh 密钥。 你可以在不重建容器镜像的情况下部署和更新密钥和应用程序配置，也无需在堆栈配置中暴露密钥。

### 1，相关术语
**主机（Master）：** 用于控制 Kubernetes 节点的计算机。所有任务分配都来自于此。

**节点（Node）：**负责执行请求和所分配任务的计算机。由 Kubernetes 主机负责对节点进行控制。

**容器集（Pod）：**被部署在单个节点上的，且包含一个或多个容器的容器组。同一容器集中的所有容器共享同一个 IP 地址、IPC、主机名称及其它资源。容器集会将网络和存储从底层容器中抽象出来。这样，您就能更加轻松地在集群中移动容器。

**复制控制器（Replication controller）：**用于控制应在集群某处运行的完全相同的容器集副本数量。

**服务（Service）：**将工作内容与容器集分离。Kubernetes 服务代理会自动将服务请求分发到正确的容器集——无论这个容器集会移到集群中的哪个位置，甚至可以被替换掉。

**Kubelet： **集群的“节点代理”，运行在节点上的服务，可读取容器清单（container manifest），确保指定的容器启动并运行。kubelet启动后会向K8S集群注册资金，并上报节点的相关信息，此时整个集群中就增加了一台新的可用的Node节点。

**kubectl：** Kubernetes 的命令行配置工具。



### 2，POD
POD运行在节点Node环境中，这个节点可以是物理机或者私有云/公有云中的一个虚拟机，一个节点上通常运行几百个Pod。在每个pod中都有一个特殊的Pause容器，其他的容器都称作业务容器，他们共享Pause容器的网络栈和Volume挂载卷。

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_002.bin "")
### 3，基本框架
![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_003.bin "")
### 二、资源对象
### 1，汇总
k8s可以看作一个高度自动化的资源控制系统，它通过跟踪对比etcd库保存的“资源期望状态”与当前环境中的“实际资源状态”的差异来实现自动化控制和自动纠错的高级功能。

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_004.bin "")
在 Kubernetes 项目中，我们所推崇的使用方法是：

首先，通过一个“编排对象”，比如 Pod、Job、CronJob 等，来描述你试图管理的应用；

然后，再为它定义一些“服务对象”，比如 Service、Secret、Horizontal Pod Autoscaler（自动水平扩展器）等。这些对象，会负责具体的平台级功能。

这种使用方法，就是所谓的“声明式 API”。这种 API 对应的“编排对象”和“服务对象”，都是 Kubernetes 项目中的 API 对象（API Object）。

|资源对象|特点|创建|
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



### 2，将服务暴露给外部
|方式|配置清单|请求流程|
|-|-|-|
|将服务的类型设置成NodePort：通过创建NodePort服务， 可以让Kubemetes在其所有节点上保留一个端口（所有节点上都使用相同的端口号）， 并将在该端口上接收到的流量重定向到基础服务。|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=34ef34bc34588bc4ea767dd30b8e67f9 "")|服务暴露在两个集群节点的端口30123上。外部请求到达任何一个端口的传入连接将被重定向到一个随机选择的pod，该pod是否位于接收到连接的节点上是不确定的，在第一个节点的端口30123收到的连接， 可以被重定向到第一节点个上运行的pod, 也可能是第二个节点上运行的pod![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=91324c3c95d58cf588d656f60e719543 "")|
|将服务类型设置成LoadBalance：它是NodePort类型的一种扩展，是K8s集群外部的一个专用的负载均衡器，K8s对此进行了支持，需要做的就是设置服务的类型为Load Balance而不是NodePort。负载均衡器拥有自己独一无二的可公开访问的IP 地址， 并将所有连接重定向到服务。可以通过负载均衡器的IP 地址访问服务|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=cecea2ac1d8bd88f174c685473b8e72a "")|外部客户端连接到负载均衡器的80端口，并路由到其中一个节点上的隐式分配节点端口。之后该连接被转发到一个pod实例![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=a45f0edb9c0ff64d2a234e18f63496a5 "")|
|创建一个Ingress资源|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=01b2b51718596fb277fbf10530623669 "")|客户端首先对[kubia.example.com](http://kubia.example.com/) 执行DNS 查找， DNS服务器返回了Ingress 控制器的IP 。客户端然后向Ingress 控制器发送HTTP 请求，并在Host头中指定[kubia.example.com](http://kubia.example.com/)。控制器从该头部确定客户端尝试访问哪个服务，并通过服务选择一个pod，并将客户端的请求转发给其中一个pod![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=09fc3bbc2b50e5abed36eb582cfa1684 "")|



### 3，Volume
Kubernetes的卷是pod的一个组成部分，因此像容器一样在pod的规范中就定义了。它们不是独立的Kubernetes对象，也不能单独创建或删除。pod的所有容器都可以使用卷，但必须先将它挂载在每个需要访问它的容器中。 在每个容器中，都可以在其文件系统的任意位置挂载卷。

常用的卷的类型：

*hostPath——用于将目录从工作节点的文件系统挂载到pod中*

hostPath卷指向节点文件系统节点上的特定文件或目录。在同一个节点上运行并在其hostPath卷中使用相同路径的pod可以看到相同的文件。

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_005.bin "")
configMap、Secret——用于将k8s部分资源和集群信息公开给pod的特殊类型卷。

persistentVolumeClaim——使用预置或者动态配置的持久存储类型

持久卷 (PersistentVolume，简称 PV)

持久卷声明 (Persistent VolumeClaim, 简称PVC)

研发人员无须向他们的pod中添加特定技术的卷，而是由集群管理员设置底层存储，然后通过Kubernetes API服务器创建持久卷并注册。在创建持久卷时，管理员可以指定其大小和所支持的访问模式。

当集群用户需要在其pod中使用持久化存储时，他们首先创建持久卷声明 (Persistent VolumeClaim, 简称 PVC) 清单，指定所需要的最低容量要求和访问模式，然后用户将待久卷声明清单提交给 Kubernetes API 服务器， Kubernetes将找到可匹配的待久卷并将其绑定到持久卷声明。

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_006.bin "")
持久卷不属于任何命名空间，它跟节点一样是集群层面的资源

持久卷声明可以当作 pod 中的一个卷来使用，其他用户不能使用相同的持久卷，除非先通过删除持久卷声明绑定来释放。

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_007.bin "")


## 三、K8S的常用命令
```
kubectl create -f xxx.yaml                          #根据一个yaml文件创建一个对象
 
 
kubectl get namespace                               #获取所有的命名空间
kubectl get pods                                    #查看所有pod
kubectl get pods -o wide                            #查看所有pod，同时展示更多的信息
kubectl get pods -o yaml                            #查看pod的信息，通过yaml形式展示
kubectl get pods -n xxx(命名空间名)                  #查看命名空间下所有的pods
kubectl get pods -n databases grep|mysql -o yaml    #查看databases命名空间下，含有mysql字段的pods，并使用yaml形式展示详细信息
kubectl label pod xxx aaa=bbb                       #给xxxpod打便签，key为aaa，value为bbb
kubectl get pods -L aaa                               #列出所有拥有标签key为aaa的pod
ps. -o wide -o yaml -n xxx grep 这些命令可以在除了pod的其他如svc、rc等对象均可以使用
 
 
kubectl get node                                    #查看k8s集群所有的node
kubectl get pods                                      #查看所有的pods
kubectl get svc                                     #查看所有的service
kubectl get rc                                      #查看所有的replicaController
kubectl get rs                                      #查看所有的replicationSet
kubectl get deploy                                  #deployment
kubectl get cm                                      #configmap
kubectl get pv                                      #pv
kubectl get pvc                                     #pvc
...
 
 
kubectl describe pod(dp、cm等等..)                 #类似，docker inspect，解释相关对象，例如针对pod对象可以看到pod的创建过程，创建失败时看到错误原因。
 
 
kubectl logs xxx（容器名）                           #查看容器日志
 
 
kubectl exec -it xxx（容器名）bash                   #进入容器，可以对容器进行操作，比如进入mysql的pod，然后连接mysql，添加数据等等
 
 
kubectl delete pod xxx                              #删除名为xxx的pod，可以通过-l通过标签过滤。也可以通过--all删除所有的pod
```


## 四、Group、Version、Resource之间的关系整理
![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_008.bin "")
### 1，group
Group，即资源组，在kubernetes对资源进行分组时，对应的数据结构就是Group，源码路径：k8s.io/apimachinery/pkg/apis/meta/v1/types.go。Group有自己的名称和版本：

```
type APIGroup struct {
	TypeMeta `json:",inline"`
	Name string `json:"name" protobuf:"bytes,1,opt,name=name"`
	Versions []GroupVersionForDiscovery `json:"versions" protobuf:"bytes,2,rep,name=versions"`
	PreferredVersion GroupVersionForDiscovery `json:"preferredVersion,omitempty" protobuf:"bytes,3,opt,name=preferredVersion"`
	ServerAddressByClientCIDRs []ServerAddressByClientCIDR `json:"serverAddressByClientCIDRs,omitempty" protobuf:"bytes,4,rep,name=serverAddressByClientCIDRs"`
}
```
k8s中的两种资源组：

* 有组名资源组，比如：deployment

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_009.bin "")
* 无组名资源组（核心资源组Core Groups），比如：Pod

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_010.bin "")


### 2，version
```
type APIVersions struct {
	TypeMeta `json:",inline"`
	Versions []string `json:"versions" protobuf:"bytes,1,rep,name=versions"`
	ServerAddressByClientCIDRs []ServerAddressByClientCIDR `json:"serverAddressByClientCIDRs" protobuf:"bytes,2,rep,name=serverAddressByClientCIDRs"`
}
```
Version即版本，k8s的版本分类：

* Alpha：内部测试版本，如v1alpha1
* Beta：经历了官方和社区测试的相对稳定版，如v1beta1
* Stable：正式发布版，如v1、v2

比如，资源组batch之下有v1和v2alpha1两个版本，每个版本下都有多个资源：

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_011.bin "")


### 3，resource
```
type APIResource struct {
	Name string `json:"name" protobuf:"bytes,1,opt,name=name"`
	SingularName string `json:"singularName" protobuf:"bytes,6,opt,name=singularName"`
	Namespaced bool `json:"namespaced" protobuf:"varint,2,opt,name=namespaced"`
	Group string `json:"group,omitempty" protobuf:"bytes,8,opt,name=group"`
	Version string `json:"version,omitempty" protobuf:"bytes,9,opt,name=version"`
	Kind string `json:"kind" protobuf:"bytes,3,opt,name=kind"`
	Verbs Verbs `json:"verbs" protobuf:"bytes,4,opt,name=verbs"`
	ShortNames []string `json:"shortNames,omitempty" protobuf:"bytes,5,rep,name=shortNames"`
	Categories []string `json:"categories,omitempty" protobuf:"bytes,7,rep,name=categories"`
	StorageVersionHash string `json:"storageVersionHash,omitempty" protobuf:"bytes,10,opt,name=storageVersionHash"`
}
```


资源的特性总结：

* kubernetes为资源准备了8种操作：create、delete、deletecollection、get、list、patch、update、watch
* 资源支持以命名空间（namespace）进行隔离
* 资源对象描述文件在日常操作中频繁用到，一共由五部分组成：apiVersion、kind、metadata、spec、status。deployment描述文件的demo：

![](../../../../_remote_images/08-周洁学习记录/local_assets/C4rP2J0ygK0tTR/image_012.bin "")





