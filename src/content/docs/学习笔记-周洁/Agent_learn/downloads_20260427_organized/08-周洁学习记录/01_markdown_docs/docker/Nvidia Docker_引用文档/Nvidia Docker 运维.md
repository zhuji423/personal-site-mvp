---
title: "清除原驱动"
description: "Nvidia Docker 运维"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\Nvidia Docker_引用文档\\Nvidia Docker 运维.md"
---
Nvidia Docker 运维

## 一、显卡驱动cuda相关
### 1、Failed to initialize NVML: Driver/library version mismatch 原因：系统驱动自动更新，导致NVIDIA内核驱动版本与系统内核版本不一致
问题描述：容器报错Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error running hook #0: error running hook: exit status 1, stdout: , stderr: Auto-detected mode as 'legacy'

nvidia-container-cli: initialization error: nvml error: driver/library version mismatch: unknown

![](/personal-site-mvp/img/doc-placeholder.svg "")
**原因：系统驱动自动更新，导致NVIDIA内核驱动版本与系统内核版本不一致**

查询library version：

```
ldconfig -p | grep nvidia
```
定位：

```
cat /var/log/dpkg.log |grep nvidia
```
系统驱动从510.108.03更新到了525.125.06。

```
 cat /proc/driver/nvidia/version
```
显卡驱动内核版本还是原来的版本 520.61.05

![](/personal-site-mvp/img/doc-placeholder.svg "")


#### 解决方法：卸载现有驱动，重新安装。
```
# 清除原驱动
sudo apt-get --purge remove nvidia-*
# 查看可以安装的版本
ubuntu-drivers devices
# 选择安装nvidia-driver-525  需要与上面的library version一致
sudo apt install nvidia-driver-525
# 重启
sudo reboot
# 验证是否安装成功
nvidia-smi
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


### 2、NVIDIA-SMI has failed because it couldn‘t communicate with the NVIDIA driver. 原因：服务器内核自动更新导致显卡无法链接
问题描述：

![](/personal-site-mvp/img/doc-placeholder.svg "")
**原因：服务器内核自动更新导致显卡无法链接**

定位：

![](/personal-site-mvp/img/doc-placeholder.svg "")
解决：

```
 sudo apt-get install dkms
 ls -l /usr/src/
 sudo dkms install -m nvidia -v 520.61.05
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
重启后正常

还不行就参照上面的方法卸载后重装，药到病除。

### 3、docker: Error response from daemon: could not select device driver ““ with capabilities: [[gpu]]原因：未**安装**nvidia-container-toolkit
问题描述：好好的docker用不了了，之前刚重装了驱动

![](/personal-site-mvp/img/doc-placeholder.svg "")
**原因：要在宿主服务器上安装**`nvidia-container-toolkit`**才能使用 --gpus**

解决：

```
sudo apt-get install -y nvidia-container-toolkit  # 安装nvidia-container-toolkit
sudo systemctl restart docker  # 重启docker 
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 二、进程相关
### 1、显存占用过高
定位正在运行的python程序

```
ps -ef |grep python
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 2、端口占用
1）有哪些端口在监听

```
sudo netstat -tulpn | grep LISTEN
```
2）查看端口是否占用

```
sudo lsof -i:端口号
```
![](/personal-site-mvp/img/doc-placeholder.svg "")


其他：

[docker](../README.md)

[docker网卡的IP地址修改](https://zhuanlan.zhihu.com/p/627278912?t=mention&mt=doc&dt=sdk)


