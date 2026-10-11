---
title: "CNAP CLI 与 kubectl 配合使用"
description: "CNAP CLI 与 kubectl 完全兼容，kubeconfig 存储在 ~/.kube/config。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\cnap-comate\\references\\kubectl.md"
---
# CNAP CLI 与 kubectl 配合使用

## kubeconfig 位置

CNAP CLI 与 kubectl 完全兼容，kubeconfig 存储在 `~/.kube/config`。

## 使用流程

1. 使用 `cnap switch` 切换环境（更新 kubeconfig context）
2. 使用 `kubectl` 执行更多操作

## 概念对照

### 集群与 Namespace

每个环境可对应若干个 K8s 集群。在每个集群上，应用部署在名称为 `<account>-<environment>` 的 namespace 中。

### kubeconfig 上下文

集群+namespace 是对 K8s 集群操作的基本单元。在 kubeconfig 中对应 `cnap:<account>-<environment>:<cluster>` 的 context。

## 环境切换

在对每个应用的 K8s 资源进行操作前，需要使用 `cnap env` 系列命令切换环境。具体命令请参考 SKILL.md 中的核心命令速查部分。

## 常用组合

```bash
# 1. 使用 cnap 切换环境
cnap switch --account appspace-test --env sandbox --cluster nb-bjdd

# 2. 然后用 kubectl 执行更多操作
kubectl get pods -o wide
kubectl logs <pod> --tail=100
kubectl describe pod <pod>
kubectl get events --sort-by='.lastTimestamp'

# 3. 查看特定 Pod 的详细状态
kubectl get pod <pod> -o yaml

# 4. 查看资源限制和配置
kubectl get pod <pod> -o jsonpath='{.spec.containers[*].resources}'

# 5. 查看节点信息
kubectl get nodes

# 6. 查看 namespace 下的所有资源
kubectl api-resources --namespaced=true
```

## 注意事项

- CNAP CLI 自动管理 kubeconfig 中的 context，无需手动配置
- 切换环境后，kubectl 会自动使用新的 context
- 使用 `cnap env show` 查看当前使用的 context