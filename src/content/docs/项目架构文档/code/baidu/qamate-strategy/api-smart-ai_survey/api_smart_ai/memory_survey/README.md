---
title: "DeepSeek 长短期记忆助理使用指南"
description: "memory = EnhancedLongTermMemory userid=\"customuser\", persistdir=\"./custommemorydir\" 自定义存储路径"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\api-smart-ai_survey\\api_smart_ai\\memory_survey\\README.md"
---
# DeepSeek 长短期记忆助理使用指南

## 功能特性

### 🧠 短期记忆
- **会话级别**：保存当前会话的所有对话历史
- **自动维护**：无需手动管理，自动保持对话上下文
- **灵活清空**：可以随时清空短期记忆，重新开始对话

### 💾 长期记忆
- **向量检索**：使用 Chroma 向量数据库存储和检索历史对话
- **智能评估**：自动评估对话重要性，只存储重要内容
- **持久化存储**：记忆跨会话保留，重启程序后仍然可用
- **语义检索**：根据问题语义自动检索相关历史记忆

### 🎯 记忆分层策略
```
用户提问
    ↓
检索长期记忆（相关历史）
    ↓
结合短期记忆（当前会话）
    ↓
生成回答
    ↓
评估重要性 → 存入长期记忆
```

## 安装依赖

```bash
# 进入项目目录
cd /Users/zhuji_m4pro/code/baidu/qamate-strategy/api-smart-ai

# 安装依赖
pip install langchain langchain-openai langchain-community langchain-core chromadb
```

## 使用方法

### 1. 基本对话

```python
from api_smart_ai.memory_survey.langchain_mem import chat

# 普通对话（自动使用短期记忆）
response = chat("你好，我是张三")
print(response)

# 继续对话（能记住之前的内容）
response = chat("我刚才说我叫什么？")
print(response)
```

### 2. 特殊命令

#### 更新长期记忆
```python
# 更新部门信息
chat("请记住我部门是测试部")

# 更新偏好设置
chat("请记住我偏好是详细的技术解释")
```

#### 查看记忆
```python
# 查看记忆摘要
chat("查看记忆")
# 或
chat("memory")
```

#### 清空短期记忆
```python
# 清空当前会话记忆（长期记忆保留）
chat("清空记忆")
# 或
chat("clear")
```

### 3. 多会话支持

```python
# 会话1
response = chat("我喜欢Python", session_id="session_001")

# 会话2（独立的短期记忆）
response = chat("我喜欢Java", session_id="session_002")

# 回到会话1（能记住Python）
response = chat("我喜欢什么语言？", session_id="session_001")
```

### 4. 自定义用户

```python
from api_smart_ai.memory_survey.langchain_mem import EnhancedLongTermMemory

# 为不同用户创建独立的长期记忆
user1_memory = EnhancedLongTermMemory(user_id="user_001")
user2_memory = EnhancedLongTermMemory(user_id="user_002")

# 每个用户的记忆互不影响
```

## 工作原理

### 1. 短期记忆（对话历史）
使用 LangChain 的 `ChatMessageHistory` 存储当前会话的对话记录，保持对话上下文连贯性。

### 2. 长期记忆（向量数据库）
- **自动评估**：每次对话后，系统自动评估对话的重要性（0-1分）
- **智能存储**：重要性 >= 0.6 的对话会自动存入长期记忆
- **语义检索**：提问时自动检索相关历史记忆

### 3. 重要性评估规则
- **基础分**：0.3
- **关键词匹配**：包含"记住"、"我是"、"我叫"、"喜欢"等关键词，每个 +0.15
- **对话长度**：较长的对话 +0.1
- **阈值**：>= 0.6 存入长期记忆

## 配置说明

### 环境变量
在 `.env` 文件中配置：
```bash
QIANFAN_DEEPSEEK_API_KEY=your_api_key_here
```

### 自定义配置

```python
from api_smart_ai.memory_survey.langchain_mem import EnhancedLongTermMemory

memory = EnhancedLongTermMemory(
    user_id="custom_user",
    persist_dir="./custom_memory_dir"  # 自定义存储路径
)

# 调整重要性阈值
memory.importance_threshold = 0.7  # 更严格的存储条件
```

## 使用示例

### 示例1：记住用户信息
```python
# 第一次对话
chat("我叫李四，在研发部工作")
# ✨ 重要对话已存入长期记忆（重要性：0.75）

# 清空短期记忆
chat("clear")

# 新会话中仍能记住
chat("我在哪个部门工作？")
# 💬 根据我的记忆，你在研发部工作。
```

### 示例2：跨会话检索
```python
# 会话1：讨论技术问题
chat("我们项目使用的是Python 3.11", session_id="project_chat")

# 几天后，新会话
chat("我们项目用的Python版本是多少？", session_id="new_chat")
# 💬 根据之前的对话，你们项目使用的是 Python 3.11
```

### 示例3：命令行交互
```bash
# 运行程序
python -m api_smart_ai.memory_survey.langchain_mem

# 交互示例
👤 你：我叫张三，喜欢编程
💬 助理：你好张三！很高兴认识你...
✨ 重要对话已存入长期记忆（重要性：0.75）

👤 你：clear
💬 助理：🗑️  短期记忆已清空，长期记忆保留

👤 你：我叫什么名字？
💬 助理：根据我的记忆，你叫张三，而且你喜欢编程。

👤 你：查看记忆
💬 助理：📋 记忆摘要
用户特征：
- department: AI研究部
- preference: 喜欢简洁、专业的回答
历史记忆条数：5
```

## 文件结构

```
memory_store/
├── user_001/          # 用户1的长期记忆
│   ├── chroma.sqlite3
│   └── ...
├── user_002/          # 用户2的长期记忆
│   ├── chroma.sqlite3
│   └── ...
```

## 注意事项

1. **首次运行**：向量数据库初始化可能需要几秒钟
2. **API配置**：确保 `.env` 文件中配置了正确的 API Key
3. **存储空间**：长期记忆会占用磁盘空间，定期清理不需要的记忆
4. **隐私保护**：记忆文件包含对话历史，注意保护用户隐私

## 高级用法

### 自定义重要性评估
```python
# 修改 evaluate_importance 方法，使用LLM评估
def evaluate_importance_with_llm(self, user_input: str, response: str) -> float:
    prompt = f"""
    评估以下对话的重要性（0-1分）：
    用户：{user_input}
    助理：{response}
    
    只返回数字分数。
    """
    result = llm.predict(prompt)
    return float(result.strip())
```

### 导出记忆
```python
from api_smart_ai.memory_survey.langchain_mem import long_term_memory

# 获取所有记忆
summary = long_term_memory.get_memory_summary()
print(summary)

# 检索特定记忆
memories = long_term_memory.retrieve_relevant_memories("Python", k=5)
for memory in memories:
    print(memory)
```

## 疑难解答

**Q: 向量数据库初始化失败？**
A: 检查是否安装了 chromadb，运行 `pip install chromadb`

**Q: 记忆检索不准确？**
A: 可以调整检索数量 `retrieve_relevant_memories(query, k=5)`

**Q: 如何重置所有记忆？**
A: 删除 `memory_store` 目录即可

## 技术栈

- **LangChain**: 对话链管理
- **LangChain OpenAI**: LLM 接口
- **Chroma**: 向量数据库
- **DeepSeek**: 大语言模型（保持不变）

