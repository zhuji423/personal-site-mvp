---
title: "ITP 新增函数：__GETLASTITEM - 获取数组最后一个元素"
description: "GETLASTITEM 函数用于获取 JSON 数组的最后一个元素，解决了 ITP 原生语法 ${/arrayindex} 不支持动态索引的问题。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\function_getlastitem_usage.md"
---
# ITP 新增函数：__GETLASTITEM - 获取数组最后一个元素

## 功能说明

`__GETLASTITEM` 函数用于获取 JSON 数组的最后一个元素，解决了 ITP 原生语法 `${/array[index]}` 不支持动态索引的问题。

## 使用方式

### 方式1：获取数组的最后一个元素（完整对象）

```bash
${__GETLASTITEM(${/genresume})}
```

**示例输出：**
```json
{
  "data": {
    "object_key": "resume/51603fe9de36a32d7375a417866fb84ae55cc3f9/create/resume.svg",
    "query_id": "187384909510314",
    "user_id": "1552471340"
  },
  "error": 0
}
```

### 方式2：获取最后一个元素的指定字段

```bash
${__GETLASTITEM(${/genresume},data)}
```

**示例输出：**
```json
{
  "object_key": "resume/51603fe9de36a32d7375a417866fb84ae55cc3f9/create/resume.svg",
  "query_id": "187384909510314",
  "user_id": "1552471340"
}
```

## Shell 脚本中的使用示例

### 示例1：获取最后一个简历的完整数据

```bash
cd /home/work/twj
echo "数组大小: ${/genresume.size}"
last_item="${__GETLASTITEM(${/genresume})}"
echo "ITP_CRAWL_STRING:key:lastResume,value:$last_item"
```

### 示例2：获取最后一个简历的 data 字段

```bash
cd /home/work/twj
last_data="${__GETLASTITEM(${/genresume},data)}"
echo "最后一个简历的数据: $last_data"
echo "ITP_CRAWL_STRING:key:lastResumeData,value:$last_data"
```

### 示例3：提取嵌套字段（需要二次处理）

```bash
cd /home/work/twj
# 第一步：获取最后一个元素的 data 字段
last_data="${__GETLASTITEM(${/genresume},data)}"
echo "ITP_CRAWL_STRING:key:lastData,value:$last_data"
```

然后在下一个步骤中：
```bash
# 第二步：从 lastData 中提取 cv_url
cv_url="${/lastData/cv_url}"
echo "简历 URL: $cv_url"
```

## 函数参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| 第1个参数 | JSON Array | 是 | 要处理的 JSON 数组（通常使用 `${/arrayName}` 格式） |
| 第2个参数 | String | 否 | 要提取的字段名，如果不提供则返回完整对象 |

## 与原有方案的对比

### 原有方案（不支持动态索引）

❌ **不可行：**
```bash
size=${/genresume.size}
index=$((size - 1))
echo "${/genresume[$index]}"  # 失败！$index 无法被正确解析
```

✅ **可行但需要硬编码：**
```bash
echo "${/genresume[7]}"  # 成功，但索引是固定的
```

### 新方案（支持动态获取最后一个元素）

✅ **完美解决：**
```bash
echo "${__GETLASTITEM(${/genresume})}"  # 始终获取最后一个元素
```

## 实现原理

1. **Java 端解析**：ITP 在 Java 端执行时，先解析 `${/genresume}` 得到完整的 JSON 数组字符串
2. **函数执行**：将数组字符串传递给 `__GETLASTITEM` 函数
3. **动态计算**：函数内部使用 `jsonArray.size() - 1` 动态计算最后一个元素的索引
4. **返回结果**：返回最后一个元素或指定字段的值

## 部署说明

### 编译部署

```bash
cd /Users/zhuji_m4pro/code/baidu/core/itp_code/itp/itp/itp-tasktracker
mvn clean package -DskipTests
```

### 重启服务

编译完成后，需要重启 ITP TaskTracker 服务以加载新函数：

```bash
# 根据你的部署方式选择对应的重启命令
./build-tt.sh  # 或者你的具体重启脚本
```

## 错误处理

- 如果数组为空或 null，函数返回空字符串 `""`
- 如果指定的字段不存在，返回空字符串 `""`
- 如果输入不是有效的 JSON 数组，返回原始输入

## 相关文件

- 函数实现：`/itp/itp-tasktracker/src/main/java/com/baidu/itp/tasktracker/function/impl/FunctionGetLastItem.java`
- 参数解析：`/itp/itp-tasktracker/src/main/java/com/baidu/itp/tasktracker/function/FunctionFactory.java`
- SPI 注册：`/itp/itp-tasktracker/src/main/resources/META-INF/services/com.baidu.itp.tasktracker.function.Function`

## 作者

- ITP Team
- 创建日期：2026-03-06

