---
title: "交互时序"
description: "当前是百度 APP 极速版存钱罐业务，需求围绕当前场景展开，该业务场景 Server 开发主要包含以下两个代码库："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\570\\repo_role.md"
---
当前是百度 APP 极速版存钱罐业务，需求围绕当前场景展开，该业务场景 Server 开发主要包含以下两个代码库：

1. 代码库 `baidu/jady/ug-duoduo-video` 是存钱罐业务的核心实现代码库，负责处理存钱罐的内部业务逻辑，并对外提供内部服务接口，供 sbox-basic 等上层服务调用。

2. 代码库 `baidu/searchbox/sbox-basic` 是面向前端请求的接入层服务，负责接收客户端请求并调用 ug-duoduo-video 的内部接口以获取业务数据，实现逻辑处理与数据中转。

# 交互时序

用户操作存钱罐客户端
→ 客户端发送请求至 sbox-basic
→ sbox-basic 调用 ug-duoduo-video 内部接口
→ ug-duoduo-video 执行存钱罐业务逻辑
→ ug-duoduo-video 返回处理结果给 sbox-basic
→ sbox-basic 将最终响应返回客户端
