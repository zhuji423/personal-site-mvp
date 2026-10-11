---
title: "ITP 批量创建脚本"
description: "用于把“代码库 / 产品 / itpGroupId / itpParentId / moduleId / itpProductId”批量 POST 到 ITP 接口。"
date: "2026-04-28"
category: "项目架构文档"
source: "D:\\mac_m4\\Agent_learn\\tools\\itp_batch\\README.md"
---
# ITP 批量创建脚本

用于把“代码库 / 产品 / itpGroupId / itpParentId / moduleId / itpProductId”批量 POST 到 ITP 接口。

不要把 Cookie 写入文件。执行时用环境变量传：

```bash
export ITP_COOKIE='你的 Cookie 字符串'
```

## 1. 准备原始数据

把从表格复制出来的文本放到：

```bash
tools/itp_batch/health_itp_nodes.raw.txt
```

原始文本可以是这种按行粘贴的格式：

```text
代码库
产品
itp的groupId
itp的parentId
qamate的moduleid
itp的productid
baidu/health/consult-ui
问诊
193826
104965132
270
1254
...
```

## 2. 解析并校验

```bash
python3 tools/itp_batch/batch_itp_nodes.py parse \
  --raw tools/itp_batch/health_itp_nodes.raw.txt \
  --csv tools/itp_batch/health_itp_nodes.csv
```

## 3. 先 dry-run

```bash
python3 tools/itp_batch/batch_itp_nodes.py run \
  --csv tools/itp_batch/health_itp_nodes.csv \
  --endpoint 'http://10.12.184.175:8555/core/tree/node/itpMigrate'
```

## 4. 真正执行

```bash
python3 tools/itp_batch/batch_itp_nodes.py run \
  --csv tools/itp_batch/health_itp_nodes.csv \
  --endpoint 'http://10.12.184.175:8555/core/tree/node/itpMigrate' \
  --execute
```

结果会写到：

```bash
tools/itp_batch/results/
```
