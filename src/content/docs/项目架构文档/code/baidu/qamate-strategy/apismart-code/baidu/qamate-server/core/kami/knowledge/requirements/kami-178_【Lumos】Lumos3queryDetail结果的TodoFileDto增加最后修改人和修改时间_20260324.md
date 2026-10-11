---
title: "kami-178 【Lumos】Lumos 3 queryDetail 结果的 TodoFileDto 增加最后修改人和修改时间"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\baidu\\qamate-server\\core\\.kami\\knowledge\\requirements\\kami-178_【Lumos】Lumos3queryDetail结果的TodoFileDto增加最后修改人和修改时间_20260324.md"
---
# kami-178 【Lumos】Lumos 3 queryDetail 结果的 TodoFileDto 增加最后修改人和修改时间

## 卡片信息
- 卡片ID: kami-178
- 类型: Story
- 状态: 开发中
- 负责人: maxiaolong01

## 需求描述
Lumos 3 queryDetail 结果的 TodoFileDto 增加最后修改人和修改时间

## 涉及文件
1. `src/main/java/com/baidu/qamate/core/v2/lumosgmt/domain/dto/TodoFileDto.java`
2. `src/main/java/com/baidu/qamate/core/v2/lumosgmt/domain/po/TodoFilePo.java`
3. `src/main/resources/mapper/TodoFeatureDocMapper.xml`
4. `src/main/java/com/baidu/qamate/core/v2/lumosgmt/domain/dto/SpecCodeFileDto.java`
5. `src/main/resources/mapper/SpecCodeRepoMapper.xml`
6. `src/main/java/com/baidu/qamate/core/v2/lumosgmt/service/impl/LumosServiceImpl.java`

## 实现方案

### 1. TodoFileDto 增加字段
- 在 `TodoFileDto` 中添加 `updateUser` (String) 和 `updateTime` (Long) 字段
- 修改 `TodoFilePo.convert()` 方法，将这两个字段赋值给 DTO

### 2. TodoFeatureDocMapper.xml 增加映射
- 在 `TodoFileDtoMap` 中添加 `file_update_user` 和 `file_update_time` 映射
- 在 SQL 查询中添加 `file.update_user` 和 `file.update_time` 字段

### 3. SpecCodeFileDto 增加字段
- 在 `SpecCodeFileDto` 中添加 `updateUser` (String) 和 `updateTime` (Long) 字段

### 4. SpecCodeRepoMapper.xml 增加映射
- 在 `SpecCodeFileDtoMap` 中添加 `file_update_user` 和 `file_update_time` 映射
- 在 SQL 查询中添加 `file.update_user` 和 `file.update_time` 字段

### 5. docCr 文件版本按 updateTime 排序
- 修改 `LumosServiceImpl.docCr()` 方法
- 使用 `Pair<Long, String>` 存储 (updateTime, content)
- 收集完所有文件版本后，按 updateTime 递增排序再转换为 `List<String>`
