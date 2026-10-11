---
title: "CNAP CLI 安装与更新"
description: "此命令会尝试更新 CNAP CLI，如果未安装，则默认安装至 ${HOME}/.cnap/bin/cnap。 建议将 ${HOME}/.cnap/bin 添加到 PATH 中以方便后续使用。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\cnap-comate\\references\\install.md"
---
# CNAP CLI 安装与更新

## 安装 CNAP CLI

### 方式一：一行命令安装或更新

此命令会尝试更新 CNAP CLI，如果未安装，则默认安装至 `${HOME}/.cnap/bin/cnap`。
建议将 `${HOME}/.cnap/bin` 添加到 `PATH` 中以方便后续使用。

```bash
url="http://bj.bcebos.com/appspace/cnap-cli/install_cnap_cli.sh" && cnap update -q || ((curl -s $url || wget $url -q -O -) | sh)
```

### 方式二：使用系统包管理器

前提：系统上已经安装了百度内部软件源（地址前缀为 `bj.bcebos.com/baidu-packages`），需要有 root 或 sudo。

```bash
# Ubuntu
apt-get install -y cnap

# Alpine
apk add cnap

# CentOS
yum install cnap -y
```

### 检查安装状态

```bash
which cnap || echo "NOT_INSTALLED" && cnap version --no-logo
```

## 更新 CNAP CLI

```bash
cnap update --latest --quiet
```

## 登录认证

登录认证详细说明请参考 [auth.md](./auth.md)。