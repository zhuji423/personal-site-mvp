---
title: "kami-253 【KAMI】Agent配置默认头像"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\baidu\\qamate-server\\core\\.kami\\knowledge\\requirements\\kami-253_【KAMI】Agent配置默认头像_20260415.md"
---
# kami-253 【KAMI】Agent配置默认头像

## 卡片信息
- **卡片 ID**: kami-253
- **卡片类型**: Story
- **卡片状态**: 开发中
- **负责人**: 罗力闻 (luoliwen)
- **创建时间**: 2026-04-15 16:22:32

## 需求描述
KAMI 调用 `/register` 注册 Agent 时，若 `icon` 字段为空，则用 `globalConfig` 中的 `AGENT_DEFAULT_ICON` 填充，默认值为 `https://bj.bcebos.com/newmvp/server/b754fd8a3c0f427b8d44aba6915281cc-AI%20Agent%E7%AE%80%E7%BA%A6%E5%A4%B4%E5%83%8F%E8%AE%BE%E8%AE%A1%20(2).png`

## 涉及文件
1. `src/main/java/com/baidu/qamate/core/v2/kamixmgt/common/enums/GlobalConfigKeyEnum.java` - 添加配置项枚举
2. `src/main/java/com/baidu/qamate/core/v2/kamixmgt/service/impl/AgentServiceImpl.java` - 实现默认头像填充逻辑

## 实现方案

### 1. 添加全局配置项
在 `GlobalConfigKeyEnum` 中添加 `AGENT_DEFAULT_ICON` 配置项：
```java
AGENT_DEFAULT_ICON(
    "AGENT_DEFAULT_ICON",
    String.class,
    "https://bj.bcebos.com/newmvp/server/b754fd8a3c0f427b8d44aba6915281cc-AI%20Agent%E7%AE%80%E7%BA%A6%E5%A4%B4%E5%83%8F%E8%AE%BE%E8%AE%A1%20(2).png"
)
```

### 2. 实现填充逻辑
在 `AgentServiceImpl.registerAgent()` 方法中：
1. 注入 `GlobalConfigService`
2. 在转换请求为 PO 对象后，检查 `icon` 字段
3. 如果 `icon` 为空（null 或空字符串），从全局配置获取默认值并设置

### 实现位置
在 `registerAgent()` 方法的第 48-64 行逻辑中，`toAgentPo` 转换后添加检查：
```java
agentPo = KAMIX_CONVERTOR.toAgentPo(req);
// 检查并填充默认头像
if (StringUtils.isBlank(agentPo.getIcon())) {
    String defaultIcon = globalConfigService.getByEnum(GlobalConfigKeyEnum.AGENT_DEFAULT_ICON);
    agentPo.setIcon(defaultIcon);
}
```

## 实现细节
- 使用 `StringUtils.isBlank()` 判断 icon 是否为空（null、空字符串、纯空格）
- 只在创建或更新时填充一次，不影响已有的 icon 值
- 利用现有的 GlobalConfig 机制，支持后续通过配置灵活调整默认头像
