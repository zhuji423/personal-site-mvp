---
title: "ITP常见问题Q&A"
description: "线上数据库注意事项： - 线上数据库不可直连，需要数据库DBA先加白名单 - 出于安全性考虑不建议测试直连线上库"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\qamate-strategy\\api-smart-ai\\sandbox_agent\\.claude_dev\\skills\\doc-helper\\resources\\常见问题Q&A.md"
---
# ITP常见问题Q&A

## 📋 文档概述
本文档整理了ITP平台使用过程中常见的技术问题及解决方案，涵盖平台访问、数据库连接、用例执行、API调用等多个方面。

## 🔗 平台访问

### 平台链接更新
- **问题**：ITP平台不能正常登录，频繁loading或打不开
- **解决方案**：使用新链接：[https://console.cloud.baidu-int.com/itp#](https://console.cloud.baidu-int.com/itp#)

## 🗄️ 数据库连接

### 数据库连接失败
**排查步骤**：
1. 检查数据库配置（用户名和密码，密码不需要加""）
2. 检查数据库访问权限配置
3. 检查数据库白名单设置

**线上数据库注意事项**：
- 线上数据库不可直连，需要数据库DBA先加白名单
- 出于安全性考虑不建议测试直连线上库

**白名单配置**：
```
IP段：10.178.216.0/23
BNS列表：group.opera-itp-itptasktracknormal-all-bj.TOOS.all 等
```

## 📊 用例管理

### Case生命周期管理
- **恢复death状态**：调用接口 `/itp/node/api/case/updatestatusbatch`
- **手动置为death**：计划执行结果页面点击"失败用例置为death"

### 数据库操作
**SQL语句写法示例**：
```sql
SELECT id,name FROM example.tb_example WHERE id=1;
UPDATE example.tb_example SET name='zhangsan' WHERE id=1;
INSERT INTO example.tb_example(id, name) VALUES (100, 'zhangsan');
DELETE FROM example.tb_example WHERE id=1;
```

## 🔧 API接口使用

### 接口认证
- **禁止调用需要cookie的接口**，只允许调用路径中包含`/api/`的接口
- 不支持获取UUAP信息

### 接口超时配置
- **HTTP默认超时**：5分钟
- **Case超时**：60秒
- **无最大限制**，但用例执行时间过长会导致计划强制终止

## 🚀 计划执行

### 并发执行
- **case级别**：不支持并发执行
- **文件夹级别**：支持并发，最高16倍并发
- **智能并发**：根据资源情况和历史稳定性动态计算并发倍数，上限20倍

### 重试机制
- **重试粒度**：case级别
- **重试逻辑**：最小粒度是case，如果op失败，重试op归属的case

### 执行稳定性
- **执行结果保存**：只保留7天历史数据
- **计划终止策略**：case超时达到10%会触发提前终止

## 🔐 安全相关

### 权限管理
- **访问限制**：线上环境仅支持cookie，线下和沙盒环境支持账号登录
- **接口认证**：API接口无需AK/SK或token认证

### 安全扫描
- **啄木鸟扫描**：默认开启，可在计划配置中关闭
- **支持类型**：不区分同步/异步接口

## 💾 数据驱动

### 动态数据更新
**支持场景**：
- setup中获取数据，通过API更新case数据驱动
- 前置op返回值长度不确定时使用

**接口示例**：
```
更新case数据驱动：/itp/node/api/case/{caseId}/dynamicData
```

## 🌐 网络配置

### 多域名配置
参考文档：[多域名配置指南](https://cloud.baidu-int.com/icloud/ITP/常见问题/如何进行多域名配置)

### 出口IP列表
**CNAP集群**：124.64.200.x系列
**OPERA集群**：39.156.65.x系列

## 📈 监控统计

### 报警机制
- **报警方式**：邮箱、Hi群（hippassport@baidu.com机器人）
- **报警条件**：连续失败次数达到设定阈值
- **不支持**：电话报警

### 稳定性评估
**评分维度**：
1. 断言个数和种类
2. 执行活跃度和成功率
3. 维护频度和复杂度
4. 性能耗时波动

**等级划分**：A(70+)、B(50-70)、C(30-50)、D(10-30)、E(10-)

## 🔄 版本管理

### 分支合并
- **合并策略**：只涉及内容和新增，不包含删除操作
- **状态同步**：分支和master状态独立，合并时相互影响

## 💡 最佳实践

### 断言编写
```json
{"type": "array", "items": {"type": "string"}, "minLength": 1}
```

### 数据驱动标识
- 用例中必须有数据驱动标识如`$[xxx]`
- 否则数据驱动功能会置灰

### Shell操作
- 获取前置返回值需要用特定格式：`echo "ITP_CRAWL_STRING:key:xxxx,value:xxxx"`

## 🤖 扩展功能

### 扩展函数
- **支持语言**：Python、JavaScript
- **使用限制**：不支持嵌套写法
- **参考文档**：[现有扩展函数列表](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/rXPeyrumXw/q1zC9MNH8iOCfb)

### AI功能
- **Prompt使用**：公共配置中支持AIGC接口测试

## 📞 技术支持

### 问题提交
```
需求空间：http://newicafe.baidu.com/v5/space/MEG-qa-ep-Customer/planbox/-1/issue
负责人：当天ITP主值班同学
```

## 🔗 相关文档链接
- [新版ITP使用文档](https://cloud.baidu-int.com/icloud/ITP/操作入门/更多功能/配置管理)
- [产品线接入文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/rXPeyrumXw/Qy8VMSLduAScB9)
- [开放API说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/rXPeyrumXw/Ce6AMNAoS1ekzt)

---
*文档生成时间：2026-01-28*
*数据来源：ITP平台知识库*