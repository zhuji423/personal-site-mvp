---
title: "CNAP CLI 使用案例"
description: "本文件包含 CNAP CLI 的典型使用场景和示例命令。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\cnap-comate\\references\\cases.md"
---
# CNAP CLI 使用案例

本文件包含 CNAP CLI 的典型使用场景和示例命令。

## 场景零：快速了解资源和环境

```bash
# 查看可访问的账号列表
cnap get account

# 查看当前账号下的环境列表
cnap get env

# 查看指定账号下的环境列表
cnap get env -A inf

# 查看当前环境下的集群列表
cnap get cluster

# 以 JSON 格式输出（便于脚本处理）
cnap get app -o json
cnap get pod -a my-app -o yaml
```

## 场景一：应用部署失败排查

**排查步骤：**

```bash
# 1. 确认当前上下文所在环境
cnap env show

# 2. 切换到目标环境（如需要）
cnap switch --env <env> --cluster <cluster>

# 3. 查看应用状态
cnap get app -w <app> -o wide

# 4. 查看 Pod 状态
cnap get pod -a <app> -o wide

# 5. （配合kubectl）查看 Pod 详情（定位 Pending/ImagePullBackOff 等问题）
kubectl describe pod <pod>

# 6. （配合kubectl）查看事件
kubectl get events --sort-by='.lastTimestamp' | head -20
```

## 场景二：查看容器日志

```bash
# 方式一：exec 查看单Pod日志文件
cnap exec <pod> -- tail -100 /app/logs/error.log
cnap exec <pod> -- sh -c 'cat /app/logs/*.log | grep ERROR'

# 方式二：批量查看多Pod日志
cnap batch --app <app> -- sh -c 'tail -50 /app/logs/error.log'
```

## 场景三：检查配置和进程

```bash
# 查看容器内配置
cnap exec <pod> -- cat /etc/config/app.yaml
cnap exec <pod> -- env | grep -i db

# 查看进程状态
cnap exec <pod> -- ps aux

# 检查网络连通性
cnap exec <pod> -- curl -v http://backend-service:8080/health
cnap exec <pod> -- nc -zv mysql-service 3306
```

## 场景四：批量排查问题

```bash
# 检查所有 Pod 的配置文件
cnap batch --app <app> --all-cluster -- cat /app/config/app.yaml

# 批量查找错误日志
cnap batch --app <app> -- sh -c 'grep ERROR /app/logs/*.log | tail -20'

# 批量检查进程
cnap batch --app <app> -- ps aux | grep java

# 实时监控多 Pod 日志
cnap batch --app <app> -p 100 -o realtime --output-options colorful --confirm -- tail -f /app/logs/service.log
```

## 场景五：文件传输

```bash
# 下载日志到本地分析
cnap cp <pod>:/app/logs/service.log ./service.log

# 下载整个日志目录
cnap cp <pod>:/app/logs ./logs/

# 上传诊断工具
cnap cp ./debug-tool.sh <pod>:/tmp/
```

## 场景六：通过 URL 快速定位资源

当从他人分享的 CNAP 控制台 URL 或告警链接中定位问题时：

```bash
# 解析 CNAP 控制台 URL，获取账号、环境、应用信息
cnap query url "https://console.cloud.baidu-int.com/devops/appspace/account/860/application/list"

# 解析具体应用页面
cnap query url "https://console.cloud.baidu-int.com/devops/appspace/account/860/application/123456/runtime/workload"

# 根据 query url 的输出结果切换到对应环境
cnap switch --account <account> --env <env> --cluster <cluster>

# 继续排查
cnap get pod -a <app>
cnap ssh <pod>
```

## 场景七：跨环境/集群定位 Pod

当只知道 Pod 名称或 IP，但不确定其在哪个环境/集群时：

```bash
# 根据 Pod 名称查询（跨所有账号环境）
cnap query pod my-app-5cf65f675f-w5bck

# 根据 Pod IP 查询
cnap query pod 10.0.0.1

# 输出包含账号、环境、集群、应用、Namespace 等完整信息
# 然后根据查询结果切换到对应环境继续操作
cnap switch --account <account> --env <env> --cluster <cluster>
cnap ssh <pod>
```

## 场景八：部署管理

### 查看部署列表

```bash
# 获取当前环境下的部署列表
cnap deploy list --app myapp

# 根据仓库路径查询
cnap deploy list --repo-path=baidu/repo/path

# JSON 格式输出
cnap deploy list --app myapp -o json
```

### 发起新部署

```bash
# 使用 commit ID 部署
cnap deploy create --app myapp --repo-path=baidu/repo/path --commit-id=0123456789abcdefedcba9876543210

# 使用 Gerrit Change 部署
cnap deploy create --app myapp --repo-path=baidu/repo/path --change-type=GERRIT_CHANGE --commit-id=xxx
```

### 查看部署详情

```bash
# 查看部署详情（包括阶段和任务）
cnap deploy get <deployment-id>

# JSON 格式输出
cnap deploy get <deployment-id> -o json
```

### 控制部署

```bash
# 终止正在进行的部署
cnap deploy abort <deployment-id>

# 暂停部署
cnap deploy pause <deployment-id>

# 恢复暂停的部署
cnap deploy resume <deployment-id>

# 确认人工确认步骤
cnap deploy confirm <deployment-id> <step-id>

# 跳过失败的任务
cnap deploy skip-task <deployment-id> <task-id>

# 重做阶段
cnap deploy redo-stage <deployment-id> <stage-id>

# 重做任务
cnap deploy redo-task <deployment-id> <task-id>
```