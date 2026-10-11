---
title: "CNAP 操作技能"
description: "Deploy, inspect and operate K8s-based applications on CNAP (Cloud-Native Application Platform)."
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\cnap-comate\\SKILL.md"
name: "cnap"
license: "Apache-2.0"
---
# CNAP 操作技能

CNAP（Cloud-Native Application Platform）是百度内部的云原生应用平台，用于 K8s 应用的 CI/CD。本技能帮助用户通过 CNAP CLI 进行应用部署排查、日志查看、容器操作等值班相关工作。

**核心概念**：

- **账号 (Account)**：用户或团队的业务归属单元，与百度云内部资源账号绑定
- **环境 (Environment)**：按照环境功能进行的隔离，如 prod、sandbox、test、dev 等环境，又分为生产和测试两个级别
- **应用 (App)**：具体的业务应用名称，有些用户也把它称作“服务”、“模块”等
- **集群 (Cluster)**：对应实际的K8s集群在CNAP的名称，通常对应地域+AZ，有些用户也把它称作“机房”等

上述4个基本概念通过组合，实现K8s资源和应用的多维度管理。

- **K8s资源三元组**：namespace为CNAP管理集群资源的单元，每个 <账号, 环境, 集群> 三元组对应一个K8s集群的namespace；一个namespace可部署多个应用。
- **应用环境三元组**：在应用维度，所有应用以 <账号, 环境, 应用> 三元组定义；一个应用可以部署在若干K8s集群。

CNAP CLI 会自动管理系统kubeconfig，每个用户使用过的环境，会自动建立名为 'cnap:<账号名>-<环境名>:<集群名>' 的context。

## 触发场景

当用户有以下场景时，使用此技能：

- 应用部署失败、启动失败的排查
- 查看应用/Pod状态、容器日志
- 登录容器执行命令
- 批量在多个Pod上执行操作
- 文件传输（上传/下载）
- 环境切换、kubeconfig上下文管理
- 部署管理（查看、发起、控制部署）

**触发关键词**：CNAP, appspace, 一站式, 部署, 部署单, 上线, deploy, Pod, 容器日志, K8s, EKS, WebSSH

## 前置检查：安装与登录

### 检查 CNAP CLI 是否已安装

```bash
which cnap || echo "NOT_INSTALLED" && cnap version --no-logo
```

**当前版本要求**：0.7.1及以上。

### 自动安装或升级

```bash
url="http://bj.bcebos.com/appspace/cnap-cli/install_cnap_cli.sh" && cnap update --latest --quiet || ((curl -s $url || wget $url -q -O -) | sh)
```

更多安装方式参考 `references/install.md` 。

### 登录

使用以下命令获取登录状态：

```bash
cnap login status
```

登录状态无需每次检查。若需要的操作未登录，命令会提示'login required'的错误信息，需要提示用户访问 [https://uuap.baidu.com/agent/token] 获取 UGate Token，并让用户粘贴给Agent，然后Agent执行以下命令：

```bash
cnap login ugate --token <ugate-token>
```

## 核心命令速查

**通用要求**：
1. 大部分命令都支持交互式（无参数）、非交互式（有参数）两种执行方式。请在命令中将参数列全，使用有参数方式one-shot提高效率，避免进入交互式执行等待输入造成阻塞。
2. 以下速查中，没列举出来的参数，不要自己随便编造参数，以免失败或遇到其他非预期结果，除非你用 `cnap help` 事先确认过。

### 资源查询

- `cnap query url <URL>` - 根据CNAP平台页面URL，查询页面类型和账号、应用、部署ID等参数
- `cnap query pod <pod_name|pod_ip>` - 根据名称或IP查询用户有权限的 Pod
- `cnap query app <name|id|repo>` - 根据应用名称（可模糊查询）、应用ID或代码库（iCode）地址，查询应用信息

提示：
- 当用户输入了一个外部资源（如URL、代码库名、应用名）等，可以用 `query` 系列命令检索内部信息（如账号、环境、应用等），然后再调用相关命令进行处理。
- CNAP平台URL通常以 `console.cloud.baidu-int.com/devops/appspace` 开头，也可能在 `appspace.baidu-int.com` 域名下

### 环境管理

- `cnap env show` - 查看当前环境上下文（账号/环境/集群）
- `cnap env switch -A <account> -E <env> -C <cluster>` - 切换环境 **（-A、-E、-C 参数应同时存在）**
- `cnap env sync [--all]` - 同步当前（或所有）环境上下文的 kubeconfig（通常无需手动执行，仅在远端kubeconfig发生变化时需要重新同步）

注意：以下的命令一般都要求在对应的环境上下文上执行，所以需要先 `env switch` 切换到对应环境，记得-A/-E/-C参数不要缺失

### 资源获取

- `cnap get account` - 获取可访问账号列表
- `cnap get env [-A <account>]` - 获取当前账号（或指定账号<account>的）环境列表
- `cnap get app [-C <cluster>]` - 获取当前账号、环境（及指定集群<cluster>）的应用列表
- `cnap get cluster [-a <app>]` - 获取当前账号、环境（及指定应用<app>）的集群列表
- `cnap get pod [-a <app>] [-C <cluster>] [--all]` - 获取当前账号、环境、集群（或指定集群<cluster>/所有集群--all、指定应用<app>）的Pod列表

提示：`get` 和 `query` 系列命令支持 `[-o json|yaml]` 参数，必要时使用 `-o json` 格式输出，能够获得更结构化、更全面的信息（但输出也会更长），也可以配合 `jq` 等工具进一步处理。

### 容器操作

- `cnap ssh [pod] [-c <container>] [-r]` - 登录容器（`-r`只读模式）
- `cnap exec [pod] -- <cmd> [-c <container>] [-r]` - 执行命令
- `cnap exec [pod] -- sh -c '<cmd>'` - 执行带 Shell 语法的命令
- `cnap batch --app <app> [-c <container>] [-C <cluster> | --all-cluster] [-p <num>] -y -- <cmd>` - 在指定应用<app>的Pod上批量执行命令（`-p`指定并发度）

### 文件传输

- `cnap cp <pod>:<remote> <local> [-c <container>]` - 下载文件
- `cnap cp <local> <pod>:<remote> [-c <container>]` - 上传文件

### 部署管理

- `cnap deploy list [--app <app> | --repo-path <repo>] [-o json|yaml]` - 根据应用名或代码库地址获取部署列表
- `cnap deploy create --repo-path <repo> --commit-id <id> [-a <app>] [-E <env>] [--branch <branch>] [--change-type NEW_COMMIT|GERRIT_CHANGE]` - 使用指定代码库和commit发起部署
- `cnap deploy get <deployment-id> [-o json|yaml]` - 获取部署详情
- `cnap deploy abort <deployment-id>` - 终止部署
- `cnap deploy pause <deployment-id>` - 暂停部署
- `cnap deploy resume <deployment-id>` - 恢复部署
- `cnap deploy confirm <deployment-id> <step-id>` - 确认人工步骤
- `cnap deploy skip-task <deployment-id> <task-id>` - 跳过任务
- `cnap deploy redo-stage <deployment-id> <stage-id>` - 重做阶段
- `cnap deploy redo-task <deployment-id> <task-id>` - 重做任务

### 帮助

- `cnap help <command> [<subcommand>]` - 获取命令详细帮助

## 生产环境注意事项

1. **读写分离**：某些生产环境有权限限制，此时普通用户 `cnap ssh` 只能以只读模式登录容器或者无法登录
2. **谨慎操作**：批量操作 `batch` 会影响多个 Pod，务必先用 `--dry` 参数确认执行计划
3. **风险命令**：除非用户强要求，原则上不允许 Agent 执行 `rm`、`kill` 等破坏性命令

## 其他信息

### 与 kubectl 配合使用

通过 `cnap env switch` 系列命令切换context，它会管理 ~/.kube/config ，之后可以与 `kubectl` 正常交互，详见 `references/kubectl.md` 。

### 值班表

包括CNAP平台及相关的EKS、iPipe、iRegistry、iCode等平台，详见 `references/oncall.md` 。

### 典型案例

- 部署单排障的流程，详见 `references/deploy-troubleshoot.md` 。
- 查看日志、排查问题、文件传输等，详见 `references/cases.md` 。
