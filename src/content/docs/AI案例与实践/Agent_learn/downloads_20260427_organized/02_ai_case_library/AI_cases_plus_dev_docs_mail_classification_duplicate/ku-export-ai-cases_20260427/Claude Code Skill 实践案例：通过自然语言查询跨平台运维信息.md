---
title: "Claude Code Skill 实践案例：通过自然语言查询数据库信息"
description: "Claude Code Skill 实践案例：通过自然语言查询跨平台运维信息"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Claude Code Skill 实践案例：通过自然语言查询跨平台运维信息.md"
---
Claude Code Skill 实践案例：通过自然语言查询跨平台运维信息

#### 🧑‍🏫 案例作者：[@杨轶男](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、运维
#### 🔧 使用工具：Ducc
#### 📒 案例概要：通过Claude Code Skill（Ducc）实现自然语言查询数据库。传统方式需编写SQL或使用平台，门槛高。Ducc自动分析代码库，提取数据表结构、关联关系和查询逻辑，生成配置。用户仅需提供代码路径和少量业务规则，即可零配置实现高效查询，降低使用门槛，提升运维效率，促进团队知识共享。
# Claude Code Skill 实践案例：通过自然语言查询数据库信息
## 背景介绍
在日常 DevOps 运维工作中，经常需要查询 BGW 和 BigNAT 集群的底层服务器规模信息。

![](/personal-site-mvp/img/doc-placeholder.svg "")
传统的查询方式有两种：

1. **直接查询数据库**：需要登录数据库，编写 SQL 语句查询相关表
2. **使用 DevOps 平台**：需要在平台中分集群查找、汇总数据

这两种方式都需要对数据库表结构和业务关联关系有深入了解，对于不熟悉的~~老板~~同事来说门槛较高。

![OS： 啊！这个我在平台上要一个一个集群查啊，数据库直接查的话我还要写 sql，我的 sql 水平 ...](/personal-site-mvp/img/doc-placeholder.svg "OS： 啊！这个我在平台上要一个一个集群查啊，数据库直接查的话我还要写 sql，我的 sql 水平 ...")






## 解决方案
通过配置 Claude Code Skill，现在可以直接用自然语言进行查询。生成完整的 Skill 配置。

* 但是但是，这个数据表之间的关系、每个字段的含义如果让我手动写 md 的话，我宁愿临时写 sql 啊，唉，长痛与短痛 ...
* 唉？不如让 Claude Code 为我打黑工！（之前代码里有很多查表的逻辑）



### 2.1. Skill 配置过程（Ducc 自动完成）
#### 1. 自动分析代码仓库
用户只需提供代码路径，Ducc 自动分析：

* `/Users/yangyinan02/go/src/icode.baidu.com/baidu/bs-platform/cmdb/internal/pkg/models/cmdb` - 提取数据表定义
* `/Users/yangyinan02/go/src/icode.baidu.com/baidu/bs-platform/cmdb/internal/apps` - 分析表之间的查询关联关系

Ducc 自动识别并整理了 BGW、BigNAT、DNS、拨测、BNS 等模块的 20+ 张核心业务表。

#### 2. 自动提取表结构
Ducc 从 Go 结构体定义中自动提取每张表的字段信息：

|字段名|类型|说明|
|-|-|-|
|id|int|主键ID|
|name|string|集群名称|
|...|...|...|

#### 3. 自动梳理关联关系
Ducc 分析代码中的查询逻辑，自动梳理表之间的关联关系：

|主表|从表|关联字段|关联类型|业务说明|
|-|-|-|-|-|
|bgw_cluster|bgw_machine|cluster(name)|业务关联|集群包含多台主机|
|bgw_machine|general_machine|Hostname(name)|Has One|BGW主机对应一台通用主机|

#### 4. 自动生成常用查询场景
Ducc 根据代码中的查询模式，自动生成常用查询场景的 SQL 模板，便于快速复用。

#### 5. 用户补充业务规则
在 Ducc 自动生成的框架基础上，用户只需补充少量业务规则，如：

* 机器名称格式为 `{机房名}-{其他信息}`
* 线上状态值为 `running`

整个过程中，用户无需手动编写任何表结构或关联关系，只需提供代码路径和少量业务规则即可。





## 使用效果
### 查询需求
> BGW 和 BigNAT 在 bddwd 机房底层服务器规模大概是多少？
### 交互过程
```
用户: BGW 和 BigNAT 在 bddwd 机房当前有多少线上机器？

Ducc:
理解用户意图: 查询 bddwd 机房中 BGW 和 BigNAT 的线上机器数量

生成的SQL:
SELECT
    'BGW' as type,
    COUNT(*) as online_count
FROM bgw_machine bm
WHERE bm.status = 'running' AND SUBSTRING_INDEX(bm.name, '-', 1) = 'bddwd'
UNION ALL
SELECT
    'BigNAT' as type,
    COUNT(*) as online_count
FROM bignat_machine bnm
WHERE bnm.status = 'running' AND SUBSTRING_INDEX(bnm.name, '-', 1) = 'bddwd';

说明: 机器名称格式为 {机房名}-{其他信息}，使用 SUBSTRING_INDEX 提取机房名称

[自动执行查询]
执行结果:
BGW: 42
BigNAT: 16
```
### 效果对比
|对比项|传统方式|Skill 方式|
|-|-|-|
|查询复杂度|需要编写 SQL 或登录平台|自然语言提问|
|配置成本|需要手动梳理表结构和关联关系|Ducc 自动分析代码库生成|
|时间成本|5-10 分钟|30 秒内获得答案|
|学习成本|需要熟悉 表结构、sql|无需了解技术细节|
|可复用性|每次都需要重新查询|可持续积累知识|





## Ducc 的核心能力
### 1. 代码库自动分析
Ducc 能够自动分析 Go 代码库中的 Model 定义，识别数据表结构，无需用户手动梳理。

### 2. 关联关系智能推导
Ducc 通过分析代码中的查询逻辑，自动推导表之间的关联关系和业务含义。

### 3. 语义理解
Ducc 能够理解"机房名称包含在机器名称 `-` 分割的第一个字段中"这样的业务规则，自动生成正确的 SQL 语句。

### 4. 动态 SQL 生成
根据用户的自然语言描述，自动生成包含多表关联、条件过滤的 SQL 语句。

### 5. 自动执行查询
Ducc 能够直接连接数据库执行查询，返回结果，无需用户手动操作。

## 总结
通过 Ducc 的自动分析能力，将 DevOps 领域的数据库知识转化为可被 AI 理解的知识库，实现了：

1. **零配置成本**：用户只需提供代码路径，Ducc 自动生成 Skill 配置
2. **降低使用门槛**：无需 SQL 知识即可查询数据库
3. **提升查询效率**：自然语言交互，快速获取结果
4. **知识沉淀复用**：一次配置，持续服务
5. **团队知识共享**：将代码库中的隐性知识转化为团队资产

## 扩展思路
基于 Ducc 的自动分析能力，可以将更多 DevOps 场景知识转化为 Skill：

* 告警规则查询：分析告警代码库，实现自然语言查询告警规则
* 资源配额查询：分析配管系统代码，实现资源配额查询
* 配置变更历史查询：分析配置管理系统，实现变更历史查询
* 服务依赖关系查询：分析服务注册中心代码，实现依赖关系查询

用户只需提供相关代码库路径，Ducc 就能自动分析并生成对应的 Skill，逐步实现 DevOps 运维工作的智能化辅助。

* 其实知识库 90% 也是 ducc 生成的

附上 skill.md 本组同学有相关查询需求可以拿走使用。

```
# DevOps平台数据库查询

## Description

通过自然语言查询 DevOps 平台数据库的连接信息、表结构及业务关联关系。

## Instructions

你是一个 DevOps 平台的数据库查询助手。你的任务是帮助用户通过自然语言查询数据库相关信息。

### 数据库连接配置

#### MySQL 连接信息
```bash
mysql -u ****** -h ****** -P****** -p****** devops_platform_db
```
- Host: ******
- Port: ******
- Database: devops_platform_db
- Username: ******
- 认证方式: 密码认证
- Password: ****** (注意：明文展示仅供测试，实际使用请存入密钥管理安全组)

### 数据库表结构

#### 核心业务表

| 表名 | 用途说明 | 主键 |
|------|---------|------|
| bgw_cluster | BGW集群信息 | id |
| bgw_machine | BGW主机信息 | id |
| bgw_conf_content | BGW配置内容 | id |
| bignat_cluster | BigNAT集群信息 | id |
| bignat_machine | BigNAT主机信息 | id |
| bignat_conf_content | BigNAT配置内容 | id |
| dns_slave_cluster | DNS从集群信息 | id |
| dns_cluster_source | DNS集群来源配置 | id |
| dns_node / dns_slave_host | DNS节点信息 | id |
| dns_detection | DNS探测配置 | id |
| dns_service_address | DNS服务地址 | id |
| dns_flow_in | DNS流量流入 | id |
| bns_group_cell | BNS组单元映射 | id |
| bns_hostname | BNS主机名映射 | id |
| general_machine | 通用主机信息 | id |
| common_machine | 通用主机基本信息 | id |
| probe_host | 拨测机信息 | probe_host_id |
| probe_host_egress | 拨测机出网配置 | probe_host_egress_id |
| probe_isp | 拨测运营商 | probe_isp_id |
| probe_host_isp | 拨测机对应运营商 | probe_host_isp_id |
| port_conf | 端口配置 | id |
| network_segment_out_info | 网段外网出口信息 | id |
| assets_model | 资产模型 | id |
| domain_ip | 域名IP | id |
| vs_rs | 虚拟服务器真实服务器 | id |
| source_info | 来源信息 | id |

### 表关联关系

#### 1. BGW 集群关联关系

| 主表 | 从表 | 关联字段 | 关联类型 | 业务说明 |
|------|------|----------|----------|----------|
| bgw_cluster | network_segment_out_info | cluster(name) | Has Many | 集群拥有多个网段外网出口信息 |
| bgw_machine | general_machine | Hostname(name) | Has One | BGW主机对应一台通用主机 |
| bgw_machine | bgw_conf_content | Host(name) | Has Many | BGW主机有多个配置内容 |
| bgw_machine | port_conf | Host(name) | Has Many | BGW主机有多个端口配置 |
| bgw_cluster | bgw_machine | cluster(name) | 业务关联 | 集群包含多台主机 |

#### 2. BigNAT 集群关联关系

| 主表 | 从表 | 关联字段 | 关联类型 | 业务说明 |
|------|------|----------|----------|----------|
| bignat_cluster | network_segment_out_info | cluster(name) | Has Many | 集群拥有多个网段外网出口信息 |
| bignat_machine | general_machine | Hostname(name) | Has One | BigNAT主机对应一台通用主机 |
| bignat_machine | bignat_conf_content | Host(name) | Has Many | BigNAT主机有多个配置内容 |
| bignat_machine | port_conf | Host(name) | Has Many | BigNAT主机有多个端口配置 |
| bignat_cluster | bignat_machine | cluster(name) | 业务关联 | 集群包含多台主机 |

#### 3. DNS 集群关联关系

| 主表 | 从表 | 关联字段 | 关联类型 | 业务说明 |
|------|------|----------|----------|----------|
| dns_slave_cluster | dns_cluster_source | name | Has Many | DNS集群有多个来源配置 |
| dns_slave_cluster | dns_detection | dns_cluster_id(ID) | Has Many | DNS集群有多个探测配置 |
| dns_slave_cluster | dns_service_address | dns_cluster(name) | Has Many | DNS集群有多个服务地址 |
| dns_cluster_source | dns_slave_cluster | name(name) | Belongs To | 来源属于某个DNS集群 |
| dns_node | dns_cluster_source | bns_cell(source_value) | Has Many | DNS节点关联到多个来源 |

#### 4. 拨测系统关联关系

| 主表 | 从表 | 关联字段 | 关联类型 | 业务说明 |
|------|------|----------|----------|----------|
| probe_host | probe_host_egress | probe_host_id | Has Many | 拨测机有多个出网配置 |
| probe_host | probe_host_isp | probe_host_id | Has Many | 拨测机关联多个运营商 |
| probe_isp | probe_host_isp | probe_isp_id | Has Many | 运营商被多个拨测机关联 |
| probe_host_isp | probe_host | probe_host_id | Belongs To | 拨测机运营商关联属于某台拨测机 |
| probe_host_isp | probe_isp | probe_isp_id | Belongs To | 拨测机运营商关联属于某个运营商 |

#### 5. BNS 关联关系

| 主表 | 从表 | 关联字段 | 关联类型 | 业务说明 |
|------|------|----------|----------|----------|
| bns_group_cell | bns_hostname | bns_cell, bns_group | 业务关联 | BNS组单元与主机名映射 |

#### 6. DNS 流量关联关系

| 主表 | 从表 | 关联字段 | 关联类型 | 业务说明 |
|------|------|----------|----------|----------|
| dns_flow_in | bgw_cluster | bgw_cluster | 业务关联 | DNS流量流入通过BGW集群 |
| dns_flow_in | bgw_machine | bgw_cluster | 业务关联 | DNS流量流入BGW主机 |

### 表结构详情

#### 表1: bgw_cluster (BGW集群表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int | 主键ID |
| name | string | 集群名称 |
| scope | string | 范围 |
| net_type | string | 网络类型 |
| single_bw | string | 单机带宽 |
| area | string | 区域 |
| idc | string | IDC |
| router_proto | string | 路由协议 |
| ip_segment | JSON | 网段列表 |
| out_bw | string | 出口带宽 |
| design_bw | string | 设计带宽 |
| structure | string | 架构 |
| description | string | 描述 |
| controller | string | 控制器 |
| cheetah_name | string | Cheetah名称 |
| cheetah_id | string | Cheetah ID |
| is_cloud_related | int | 是否云相关 |
| related_key_customer | string | 关键客户 |
| remark | string | 备注 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表2: bgw_machine (BGW主机表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int | 主键ID |
| name | string | 主机名 |
| cluster | string | 所属集群 |
| status | string | 状态 |
| version | string | 版本 |
| second_version | string | 二级版本 |
| time_version | string | 时间版本 |
| capacity | string | 容量 |
| network_card | string | 网卡 |
| switchboard | string | 交换机 |
| config | string | 配置 |
| remark | string | 备注 |
| status_change_time | string | 状态变更时间 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表3: bgw_conf_content (BGW配置内容表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int | 主键ID |
| host | string | 主机名 |
| conf_type | string | 配置类型(service/router) |
| md5 | string | MD5 |
| path | string | 路径 |
| content | string | 内容 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表4: bignat_cluster (BigNAT集群表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| name | string | 集群名称 |
| uuid | string | UUID |
| backup_name | string | 备份名称 |
| backup_uuid | string | 备份UUID |
| net_type | string | 网络类型 |
| single_bw | string | 单机带宽 |
| area | string | 区域 |
| idc | string | IDC |
| pass_idc | string | 透传IDC |
| router_proto | string | 路由协议 |
| vtep | string | VTEP |
| backup_vtep | string | 备份VTEP |
| out_bw | string | 出口带宽 |
| design_bw | string | 设计带宽 |
| structure | string | 架构 |
| description | string | 描述 |
| controller | string | 控制器 |
| backup_ipv4 | string | 备份IPv4 |
| backup_ipv6 | string | 备份IPv6 |
| support_ipv6 | string | 支持IPv6 |
| status | string | 状态 |
| is_cloud_related | int | 是否云相关 |
| related_key_customer | string | 关键客户 |
| remark | string | 备注 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表5: bignat_machine (BigNAT主机表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| name | string | 机器名 |
| uuid | string | UUID |
| bgp_as | string | BGP AS |
| cluster | string | 集群 |
| status | string | 状态 |
| version | string | 版本 |
| capacity | string | 容量 |
| network_card | string | 网卡信息 |
| switchboard | string | 交换机信息 |
| remote_as | string | 交换机BGP-AS |
| ipv4_1 | string | 互联IP1 |
| ipv4_gateway_1 | string | 互联网关1 |
| ipv4_2 | string | 互联IP2 |
| ipv4_gateway_2 | string | 互联网关2 |
| ipv6 | string | 互联IPv6 |
| ipv6_gateway | string | 互联IPv6网关 |
| ipv4_eip | string | EIP网段 |
| ipv6_eip | string | IPv6 EIP网段 |
| numa_id | int8 | numa_id |
| worker_cpu | string | worker_cpu |
| pci0 | string | pci0 |
| pci1 | string | pci1 |
| pci2 | string | pci2 |
| tcp_idle_timeout | int32 | TCP空闲超时 |
| icmp_timeout | int32 | ICMP超时 |
| bnat_version | string | bnat_version |
| time_version | string | 时间版本 |
| bignat_node_agent_version | string | agent版本 |
| udp_timeout | int32 | UDP超时 |
| tor_as | string | tor_as |
| bal_version | string | bal版本 |
| remark | string | 备注 |
| status_change_time | time.Time | 状态变更时间 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表6: bignat_conf_content (BigNAT配置内容表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int | 主键ID |
| host | string | 主机名 |
| conf_type | string | 配置类型(bnat/bgpd/ospfd/bal/agent) |
| md5 | string | MD5 |
| path | string | 路径 |
| content | string | 内容 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表7: dns_slave_cluster (DNS从集群表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| name | string | 集群名称 |
| code | string | 编码 |
| service_type | string | 服务类型 |
| server_type | string | 服务器类型 |
| can_detect | int | 可探测 |
| is_sink | int | 是否下沉 |
| is_delete | int | 是否删除 |
| route | string | 路由 |
| is_route | int | 是否路由 |
| ns | string | NS |
| sdns | string | SDNS |
| local | string | 本地 |
| is_bce | int | 是否BCE |
| bce_service_type | string | BCE服务类型 |
| idc | string | IDC |
| structure | string | 架构 |
| network_type | string | 网络类型 |
| scope | string | 范围 |
| detect_domain | string | 探测域名 |
| detect_agent | string | 探测代理 |
| process | string | 进程 |
| function_type | string | 功能类型 |
| customer | string | 客户 |
| backup_cluster | string | 备份集群 |
| description | string | 描述 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表8: dns_cluster_source (DNS集群来源表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| service_type | string | 服务类型 |
| code | string | 编码 |
| name | string | 名称 |
| source_type | string | 来源类型 |
| source_value | string | 来源值 |
| description | string | 描述 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表9: dns_node / dns_slave_host (DNS节点表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| bns_cell | string | BNS单元 |
| status | string | 状态 |
| is_delete | int | 是否删除 |
| hostname | string | 主机名 |
| ip | string | IP |
| vnic0_ipv4 | string | vnic0 IPv4 |
| vnic0_ipv6 | string | vnic0 IPv6 |
| vnic1_ipv4 | string | vnic1 IPv4 |
| vnic1_ipv6 | string | vnic1 IPv6 |
| server_port | string | 服务器端口 |
| bignat_cluster | string | BigNAT集群 |
| bignat_pool | int | BigNAT池号 |
| bignat_isp | string | BigNAT运营商 |
| ttm_version | string | TTM版本 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表10: dns_detection (DNS探测表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| detection_type | string | 探测类型 |
| dst_type | string | 目标类型 |
| dst_value | string | 目标值 |
| dns_cluster_id | int64 | DNS集群ID |
| server_type | string | 服务器类型 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表11: dns_service_address (DNS服务地址表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| dns_cluster | string | DNS集群 |
| ns | string | NS |
| vip | string | VIP |
| bgw_cluster | string | BGW集群 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表12: dns_flow_in (DNS流量流入表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| bind_type | string | 绑定类型 |
| bind_name | string | 绑定名称 |
| ip_type | string | IP类型 |
| bgw_cluster | string | BGW集群 |
| vip | string | VIP |
| vip_isp | string | VIP运营商 |
| vport | string | 虚拟端口 |
| protocol | string | 协议 |
| type | string | 类型 |
| conf | string | 配置 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表13: general_machine (通用主机表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int | 主键ID |
| hostname | string | 主机名 |
| ipv4 | string | IPv4地址 |
| ipv6 | string | IPv6地址 |
| sn | string | 序列号 |
| rack_place | string | 机架位置 |
| os | string | 操作系统 |
| kernel | string | 内核 |
| torname | string | TOR名称 |
| networkcard | JSON | 网卡列表 |
| cpu | JSON | CPU列表 |
| memory | JSON | 内存列表 |
| maintenance_time | time.Time | 维护时间 |
| status | string | 状态 |
| idc | string | IDC |
| net_cluster | string | 网络集群 |
| net_pod | string | 网络Pod |
| description | string | 描述 |
| created_at | string | 创建时间 |
| updated_at | string | 更新时间 |
| hardware_fault_list | JSON | 硬件故障列表 |
| hardware_fault_count | int | 硬件故障数量 |
| machine_status | int | 机器状态 |

#### 表14: probe_host (拨测机表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| probe_host_id | int | 主键ID |
| hostname | string | 主机名 |
| ip_type | int8 | IP类型 |
| network_area | string | 网络区域 |
| idc | string | IDC |
| ldns | string | LDNS |
| comment | string | 备注 |
| is_delete | int8 | 是否删除 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表15: probe_host_egress (拨测机出网表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| probe_host_egress_id | int | 主键ID |
| probe_host_id | int | 拨测机ID |
| ip_type | int8 | IP类型 |
| cluster | string | 集群 |
| pool_number | int | 池号 |
| isp | string | 运营商 |
| idc | string | IDC |
| is_delete | int8 | 是否删除 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表16: probe_isp (拨测运营商表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| probe_isp_id | int | 主键ID |
| code | string | 编码 |
| region | string | 区域 |
| province | string | 省份 |
| isp | string | 运营商 |
| ldns | string | LDNS |
| is_delete | int8 | 是否删除 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表17: probe_host_isp (拨测机对应运营商表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| probe_host_isp_id | int | 主键ID |
| probe_host_id | int | 拨测机ID |
| probe_isp_id | int | 拨测运营商ID |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表18: port_conf (端口配置表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int64 | 主键ID |
| host | string | 主机名 |
| uio_port | string | UIO端口 |
| if_ip | string | 接口IP |
| if_ip6 | string | 接口IPv6 |
| gw_ip | string | 网关IP |
| gw_ip6 | string | 网关IPv6 |
| netmask | string | 子网掩码 |
| prefix_len | string | 前缀长度 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

#### 表19: network_segment_out_info (网段外网出口信息表)

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | int | 主键ID |
| name | string | 名称 |
| cluster | string | 集群 |
| nsc_id | string | NSC ID |
| status | string | 状态 |
| uses | string | 用途 |
| remark | string | 备注 |
| net_prefix_len | string | 网段前缀长度 |
| out_id | string | 出口ID |
| out_name | string | 出口名称 |
| iaz | string | IAZ |
| pop | string | POP |
| vendor | string | 供应商 |
| continent | string | 大洲 |
| country | string | 国家 |
| province | string | 省份 |
| charging_group | string | 计费组 |
| operators | string | 运营商 |
| group_notes | string | 组备注 |
| as_number | string | AS号 |
| portnum | string | 端口数 |
| network | string | 网络 |
| attribute | string | 属性 |
| out_bandwidth | string | 出口带宽 |
| in_bandwidth | string | 入口带宽 |
| port_bandwidth | string | 端口带宽 |
| billing_mode | string | 计费模式 |
| min_bandwidth | string | 最小带宽 |
| created_at | time.Time | 创建时间 |
| updated_at | time.Time | 更新时间 |

### 常用查询场景

#### 查询 BGW 集群及其所有主机信息

**场景**: 查询某个BGW集群的详细信息，包括所有主机及配置

```sql
-- 查询指定BGW集群的所有主机
SELECT
    bc.name AS cluster_name,
    bc.area,
    bc.idc,
    bc.status,
    bm.name AS machine_name,
    bm.status AS machine_status,
    bm.version,
    gm.hostname,
    gm.ipv4,
    gm.ipv6
FROM bgw_cluster bc
LEFT JOIN bgw_machine bm ON bc.name = bm.cluster
LEFT JOIN general_machine gm ON bm.name = gm.hostname
WHERE bc.name = 'YOUR_CLUSTER_NAME';
```

#### 查询 BigNAT 集群网段出口信息

**场景**: 查询BigNAT集群的所有网段及外网出口详情

```sql
-- 查询指定BigNAT集群的网段出口信息
SELECT
    nsoi.cluster,
    nsoi.name AS segment_name,
    nsoi.net_prefix_len,
    nsoi.out_id,
    nsoi.out_name,
    nsoi.operators,
    nsoi.out_bandwidth,
    nsoi.continent,
    nsoi.country,
    nsoi.province
FROM network_segment_out_info nsoi
WHERE nsoi.cluster = 'YOUR_CLUSTER_NAME';
```

#### 查询 DNS 集群的所有来源和节点

**场景**: 查询DNS集群的所有来源配置及关联的DNS节点

```sql
-- 查询指定DNS集群的来源配置
SELECT
    dsc.name AS cluster_name,
    dsc.service_type,
    dcs.source_type,
    dcs.source_value,
    dcs.description
FROM dns_slave_cluster dsc
LEFT JOIN dns_cluster_source dcs ON dsc.name = dcs.name
WHERE dsc.name = 'YOUR_CLUSTER_NAME';
```

#### 查询主机的硬件故障信息

**场景**: 查询通用主机的硬件故障列表和故障数量

```sql
-- 查询有硬件故障的主机
SELECT
    hostname,
    ipv4,
    idc,
    machine_status,
    hardware_fault_count,
    hardware_fault_list
FROM general_machine
WHERE hardware_fault_count > 0;
```

#### 查询拨测机的运营商和出网配置

**场景**: 查询拨测机关联的运营商及出网信息

```sql
-- 查询拨测机及其关联的运营商和出网配置
SELECT
    ph.hostname AS probe_hostname,
    ph.network_area,
    pi.isp AS isp_name,
    pi.region,
    phe.cluster AS egress_cluster,
    phe.isp AS egress_isp,
    phe.pool_number
FROM probe_host ph
LEFT JOIN probe_host_isp phi ON ph.probe_host_id = phi.probe_host_id
LEFT JOIN probe_isp pi ON phi.probe_isp_id = pi.probe_isp_id
LEFT JOIN probe_host_egress phe ON ph.probe_host_id = phe.probe_host_id
WHERE ph.hostname = 'YOUR_PROBE_HOST';
```

#### 查询 DNS 节点的 BigNAT 关联信息

**场景**: 查询DNS节点关联的BigNAT集群、池号和运营商信息

```sql
-- 查询指定BNS单元的DNS节点BigNAT信息
SELECT
    bns_cell,
    hostname,
    ip,
    bignat_cluster,
    bignat_pool,
    bignat_isp,
    status
FROM dns_node
WHERE bns_cell = 'YOUR_BNS_CELL';
```

#### 查询配置文件的 MD5 变更

**场景**: 查询BGW/BigNAT主机的配置文件内容及其MD5

```sql
-- 查询BGW主机的配置内容
SELECT
    bcc.host,
    bcc.conf_type,
    bcc.md5,
    bcc.path
FROM bgw_conf_content bcc
WHERE bcc.host = 'YOUR_HOST_NAME';

-- 查询BigNAT主机的配置内容
SELECT
    bncc.host,
    bncc.conf_type,
    bncc.md5,
    bncc.path
FROM bignat_conf_content bncc
WHERE bncc.host = 'YOUR_HOST_NAME';
```

### 常见字段映射

| 业务术语 | 对应表.字段 |
|----------|-------------|
| 集群名称 | bgw_cluster.name, bignat_cluster.name, dns_slave_cluster.name |
| 主机名 | bgw_machine.name, bignat_machine.name, general_machine.hostname, probe_host.hostname, dns_node.hostname |
| 所属集群 | bgw_machine.cluster, bignat_machine.cluster |
| 状态 | bgw_cluster.status, bgw_machine.status, bignat_cluster.status, bignat_machine.status, dns_node.status |
| 版本 | bgw_machine.version, bignat_machine.version |
| IDC | bgw_cluster.idc, bignat_cluster.idc, general_machine.idc |
| 区域 | bgw_cluster.area, bignat_cluster.area |
| 网络类型 | bgw_cluster.net_type, bignat_cluster.net_type |
| BNS单元 | dns_node.bns_cell, bns_group_cell.bns_cell |
| VIP | dns_service_address.vip, dns_flow_in.vip |
| BGW集群 | dns_service_address.bgw_cluster, dns_flow_in.bgw_cluster |
| 运营商 | probe_isp.isp, bignat_machine.remote_as, dns_node.bignat_isp |
| 硬件故障数量 | general_machine.hardware_fault_count |
| 硬件故障列表 | general_machine.hardware_fault_list |

### 注意事项

- 数据库连接密码仅为测试用途，实际使用时应存入密钥管理安全组
- `ip_segment`、`networkcard`、`cpu`、`memory`、`hardware_fault_list` 等字段为 JSON 类型，查询时可能需要使用 JSON 函数解析
- 某些表有 `is_delete` 字段，查询时需注意过滤已删除记录
- `general_machine` 表通过 `hostname` 字段关联 `bgw_machine` 和 `bignat_machine` 的 `name` 字段
- `dns_node` 表别名 `dns_slave_host`，两者指向同一张表
- `conf_type` 字段在 `bgw_conf_content` 中值为 `service` 或 `router`
- `conf_type` 字段在 `bignat_conf_content` 中值为 `bnat`、`bgpd`、`ospfd`、`bal` 或 `agent`
- `created_at` 和 `updated_at` 为时间戳字段，可按时间范围筛选
- `machine_status` 字段表示机器状态，可能与 `status` 字段含义不同
- `bgw_machine.status` 和 `bignat_machine.status` 字段：线上运行状态值为 `running`
- `bgw_machine.name` 和 `bignat_machine.name` 字段：机器名称格式为 `{机房名}-{其他信息}`，使用 `SUBSTRING_INDEX(name, '-', 1)` 提取机房名称

### 回复格式

当用户提出查询需求时，请按照以下格式回复：

1. **理解用户意图**: 简要说明对用户查询的理解
2. **生成的SQL**: 提供完整的SQL查询语句
3. **说明**: 解释SQL的逻辑和涉及表的关联关系
4. **注意事项**: 提醒相关的注意事项（如有）

```
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
