---
title: "临时关闭，重启恢复"
description: "查看ip命令： ifconfig"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\k8s_引用文档\\k8s搭建.md"
---
k8s搭建

### 一、安装准备
#### 1、验证2台机子网络互通（本文用的ubuntu）
##### **1）**机子信息
2个机子信息：

|主机|角色|IP|hostname|
|-|-|-|-|
|node1|Master|172.22.0.1|Super-Server|
|node2|Node|172.19.0.1 |kongdefu.bcc-szth.baidu.com|

查看ip命令： ifconfig

查看hostname命令： hostname

##### **2）验证网络互通**
机子1执行：ping {Node ip}

![](/personal-site-mvp/img/doc-placeholder.svg "")
机子2执行：ping {Master ip}

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2、安装Docker
集群2台机子均要安装

安装参考：[Docker安装与配置](../docker_引用文档/Docker安装与配置.md)

验证2台机子已安装docker成功：

```
docker version
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 3、安装Kubernetes
集群2台机子均要安装

##### 1）环境配置
###### 关闭Swap分区
kubelet要求必须禁用交换分区，所以kubeadm初始化时回检测swap是否关闭，如果没有关闭会报错，如果不想关闭安装时命令行可以指定-ignore-preflight-errors=Swap

使用 free -m 检查Swap分区是否关闭：

![](/personal-site-mvp/img/doc-placeholder.svg "")
不为0则说明Swap分区没有关闭

```
# 临时关闭，重启恢复
sudo swapoff -a  

# 永久关闭
sudo sed -ri 's/.*swap.*/#&/' /etc/fstab 
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
###### 禁用SELinux
使用 sestatus 查询是否已禁用：

![](/personal-site-mvp/img/doc-placeholder.svg "")
disabled表示已禁用，否则使用 sudo setenforce 0 进行禁用

```
# 临时禁用
sudo setenforce 0 

# 永久禁用 SELinux配置文件修改状态(需要重启系统才能生效)
vim /etc/selinux/config
SELINUX=disabled --设置为禁用状态
```
###### 关闭防火墙
```
ufw status verbose
ufw disable
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
###### 允许 iptables 检查桥接流量 
```
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sudo sysctl --system
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
查看网桥过滤模块是否加载成功：

```
lsmod | grep br_netfilter
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 2）安装kubelet、kubeadm、kubectl
###### 添加源，更新缓存索引
su切换到root，否则添加访问公钥会失败

支持https传送

```
apt update && apt install -y apt-transport-https
```
添加访问公钥

```
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - 
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
添加源

```
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
```
更新缓存索引

```
apt update
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
###### 安装kubectl kubelet kubeadm
查看kubectl可用版本

```
apt-cache madison kubectl
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
可以选择安装指定版本或者安装最新版本：

```
# 安装最新版本（不建议）
apt install  kubectl kubelet kubeadm -y

# 指定版本
apt install -y kubectl=1.25.9-00 kubelet=1.25.9-00 kubeadm=1.25.9-00
```
###### 开机自启kubelet
```
systemctl enable kubelet
```
查看状态

```
systemctl status kubelet
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
查看k8s版本

```
kubectl version --short=true
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 二、测试集群
#### 1、初始化master主节点
##### kubeadm init
把Super-Server（172.22.0.1)作为master，只在主节点执行：

```
# 只在主节点执行
kubeadm init \
--kubernetes-version=v1.25.9  \
--service-cidr=10.96.0.0/12 \
--pod-network-cidr=172.20.0.0/16 \
--image-repository registry.aliyuncs.com/google_containers
```
* kubernetes-version：k8s版本
* service-cidr：为Service分配的IP地址段
* pod-network-cidr：为pod分配的IP地址段
* image-repository：镜像仓库，此处为国内阿里云镜像仓库加速下载

更多初始化参数详情点击[这里](https://kubernetes.io/zh-cn/docs/reference/setup-tools/kubeadm/kubeadm-init/?login=from_csdn)。若出现报错：this version of kubeadm only supports deploying clusters with the control plane version >= 1.27.0. Current version: v1.25.0，降一下版本就好：

```
# 删除高版本的
apt purge  kubectl kubelet kubeadm -y
# 安装低版本的
apt install -y kubectl=1.25.9-00 kubelet=1.25.9-00 kubeadm=1.25.9-00
```
若执行初始化过程中出错，根据错误信息调整后，执行 kubeadm reset ; rm -rf $HOME/.kube，然后重新执行初始化命令

等上几分钟，初始化成功会出现：

```
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 172.18.12.141:6443 --token xgc7ez.0uit6bee22zpfikc \
	--discovery-token-ca-cert-hash sha256:6eb64c35a30986b11e8d3f97c54f3dffadc9b0c975004e414e4f4ecdcdeaaeff
```
注：记住这里输出的kubeadm join命令，该命令可将节点加入集群

##### 配置
初始化后还需要2步配置

###### **a. 配置kube**
按照上面kubeadm init输出进行配置

非root用户： 

```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
 root用户：

```
export KUBECONFIG=/etc/kubernetes/admin.conf
```
以上命令二选一，若未执行，会报错：The connection to the server localhost:8080 was refused - did you specify the right host or port? root 用户需要注意的是，如果选择了设置KUBECONFIG，这个环境变量只是暂时的，机器重启后kubectl会因为找不到KUBECONFIG而仍然报该错误，可以通过把export写进/etc/profile里解决

###### **b. 添加网络配置**
这里我使用flannel，其他[参考](https://kubernetes.io/docs/concepts/cluster-administration/addons/)

```
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
```
![非root](/personal-site-mvp/img/doc-placeholder.svg "非root")
![root](/personal-site-mvp/img/doc-placeholder.svg "root")
##### 查看集群信息
```
kubectl get nodes
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2、node工作节点加入master节点
Node节点执行如下命令，这里对应kubeadm init输出，需要换成自己的： 

```
kubeadm join 172.18.12.141:6443 --token xgc7ez.0uit6bee22zpfikc \
	--discovery-token-ca-cert-hash sha256:6eb64c35a30986b11e8d3f97c54f3dffadc9b0c975004e414e4f4ecdcdeaaeff
```
默认token有效期为24小时，如果忘记添加命令或过期之后token失效，可在Master节点重新生成token：

```
kubeadm token create --print-join-command
```
Node节点执行成功后：



常见报错1：kubernetes默认设置cgroup驱动(cgroupdriver)为"systemd"，而docker服务的cgroup驱动默认为"cgroupfs"，建议将其修改为"systemd"，与kubernetes保持一致

![](/personal-site-mvp/img/doc-placeholder.svg "")
在 /etc/docker/daemon.json 里添加 {"exec-opts":["native.cgroupdriver=systemd"]}，重启docker

![](/personal-site-mvp/img/doc-placeholder.svg "")
常见报错2：validate service connection: CRI v1 runtime API is not implemented for endpoint

```
vi /etc/containerd/config.toml
# 注释 disabled_plugins = ["cri"]

# 重启containerd
systemctl restart containerd
```
#### 3、简单使用
### 

