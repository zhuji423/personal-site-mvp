---
title: "AI播客生成系统"
description: "这是一个基于FastAPI和LangChain构建的多角色AI播客生成系统，可以模拟三个不同角色进行动态对话，生成关于AI对就业影响的播客内容。"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\01_code\\code\\hackthom\\README.md"
---
# AI播客生成系统

这是一个基于FastAPI和LangChain构建的多角色AI播客生成系统，可以模拟三个不同角色进行动态对话，生成关于AI对就业影响的播客内容。

## 项目特性

- 🎙️ 三个不同的AI角色：主持人、经济学家、打工人
- 🔄 动态工作流：每个角色基于上下文进行回应
- 📊 数据驱动：使用模拟的研究数据和新闻事件
- 🌐 REST API：FastAPI提供完整的后端服务
- 🎯 结构化输出：生成完整的播客稿件

## 角色设定

### 林知远（主持人）
- 中立引导者，保持理性温和
- 负责话题引导和结构控制
- 善于提出追问和总结观点

### 陈博士（经济学家）
- 数据与趋势专家
- 基于研究报告和历史数据分析
- 理性客观的分析视角

### 小李（打工人）
- 代表普通职场人的声音
- 表达真实的焦虑和担忧
- 情绪化但不失理性的讨论

## 技术架构

- **后端框架**: FastAPI
- **AI框架**: DeepSeek API + 自定义Agent系统
- **工作流**: Multi-Agent对话系统
- **数据模拟**: 基于真实场景的虚拟数据

## 快速开始

1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，添加 DEEPSEEK_API_KEY
# 获取API密钥: https://platform.deepseek.com/api_keys
```

3. 启动服务
```bash
uvicorn main:app --reload
```

4. 测试DeepSeek集成
```
python test_deepseek.py
```

5. 访问API文档
```
http://localhost:8000/docs
```

## API使用
```bash
POST /generate-podcast
{
  "topic": "AI自动化对客服行业的影响",
  "duration_minutes": 15
}
```

### 获取角色信息
```bash
GET /characters
```

## 项目结构

```
hackthom/
├── main.py                 # FastAPI应用入口
├── requirements.txt        # 依赖包
├── .env.example           # 环境变量模板
├── agents/                # AI角色定义
│   ├── __init__.py
│   ├── host.py           # 主持人
│   ├── economist.py      # 经济学家
│   └── worker.py         # 打工人
├── data/                 # 模拟数据
│   ├── __init__.py
│   ├── research_data.py  # 研究报告数据
│   ├── news_events.py    # 新闻事件
│   └── topics.py         # 话题库
├── workflow/             # 工作流引擎
│   ├── __init__.py
│   ├── podcast_generator.py
│   └── conversation_manager.py
└── README.md
```

## 设计思路

1. **多角色系统**: 每个角色都有独特的知识库、性格特点和表达风格
2. **动态对话**: 基于上下文和角色特点生成自然的对话流程
3. **结构化内容**: 确保播客有清晰的开头、讨论和总结
4. **数据支撑**: 使用模拟的真实数据增强对话的可信度
5. **可扩展性**: 易于添加新角色或修改对话逻辑

## 示例输出

系统会生成包含以下结构的播客稿件：
- 开场白（主持人介绍话题）
- 多轮讨论（三个角色的观点交流）
- 冲突与解决（不同观点的碰撞）
- 总结陈词（主持人收尾）
