---
title: "AI播客生成器"
description: "一个基于多Agent协作的AI播客内容生成系统，通过三个不同角色的AI智能体（主持人、经济学家、打工人）的深入讨论，生成有深度、有观点碰撞的播客稿件。"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\hackthon_cc\\baidu\\personal-code\\round-cast\\round_cast_new\\README.md"
---
# AI播客生成器

一个基于多Agent协作的AI播客内容生成系统，通过三个不同角色的AI智能体（主持人、经济学家、打工人）的深入讨论，生成有深度、有观点碰撞的播客稿件。

## 🎯 项目特色

- **多角色协作**：三个AI角色从不同角度讨论话题
- **动态角色生成**：基于Mita搜索动态生成4-6个专业角色
- **真实感强**：使用假数据生成器创造逼真的讨论背景
- **结构化输出**：生成完整的播客脚本，包含开场、讨论、总结
- **交互式界面**：提供简洁美观的Web界面
- **轮数控制**：支持1-5轮讨论深度调节
- **进度显示**：实时进度条显示生成过程
- **多格式保存**：JSON、TXT、Markdown三种格式输出

## 🏗️ 项目架构

```
hackthon_cc/
├── src/
│   ├── agents/          # AI智能体实现
│   │   ├── base_agent.py    # 基础Agent类
│   │   ├── host_agent.py    # 主持人Agent
│   │   ├── economist_agent.py  # 经济学家Agent
│   │   ├── worker_agent.py   # 打工人Agent
│   │   └── custom_agent.py   # 自定义角色Agent
│   ├── models/          # 数据模型
│   │   └── schemas.py       # Pydantic模型定义
│   ├── services/        # 业务逻辑
│   │   ├── workflow_engine.py  # 播客工作流引擎
│   │   └── role_generator.py # 角色生成服务
│   ├── data/            # 数据层
│   │   ├── prompts.py       # 角色prompt模板
│   │   └── role_templates.py # 专业角色模板库
│   └── main.py          # FastAPI主应用
├── static/              # 静态文件
├── templates/           # HTML模板
├── results/             # 播客结果存储
├── requirements.txt     # 依赖列表
├── run.py              # 启动脚本
├── test_demo.py        # 增强版命令行工具
├── api_server.py       # 角色生成API服务
└── README.md           # 项目说明
```

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆项目
cd hackthon_cc

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置API密钥

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，填入DeepSeek API密钥
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 3. 启动服务

#### 方式1：启动主应用（包含默认播客生成）

```bash
# 使用启动脚本
python run.py
# 或直接运行
python -m src.main
```

访问 `http://localhost:8000`

#### 方式2：启动动态角色生成服务

```bash
# 独立运行角色生成API服务
python api_server.py
```

该服务将在 `http://localhost:8021` 上运行。

### 4. API使用说明

#### 生成动态角色

- **Endpoint**: `POST /api/generate-roles`
- **说明**: 根据主题动态生成4-6个专业角色。
- **请求体 (JSON)**:
  ```json
  {
    "topic": "人工智能对未来教育的影响",
    "num_roles": 5
  }
  ```
- **响应**: 返回包含角色详细信息和Mita搜索验证事实的JSON数据。


### 5. 增强版命令行工具

除了Web界面，我们还提供了功能更强大的命令行工具：

```bash
# 使用增强版命令行工具
python test_demo.py

# 指定话题和讨论轮数
python test_demo.py --topic "AI对教育行业的影响" --rounds 3

# 简写形式
python test_demo.py -t "AI会取代程序员吗" -r 2

# 查看已生成的播客列表
python test_demo.py --list
```

#### 命令行参数说明

| 参数 | 简写 | 说明 | 示例 |
|------|------|------|------|
| `--topic` | `-t` | 讨论话题 | `--topic "AI对教育的影响"` |
| `--rounds` | `-r` | 讨论轮数(1-5) | `--rounds 3` |
| `--list` | `-l` | 列出已生成播客 | `--list` |

#### 讨论轮数控制

- **1轮**：6段发言，适合快速了解
- **2轮**：9段发言，观点碰撞与回应  
- **3轮**：12段发言，多角度深度讨论
- **4轮**：15段发言，复杂话题全面剖析
- **5轮**：18段发言，研究级深度讨论

## 🎭 角色设计

### 默认角色

项目包含三个固定的默认角色，用于快速生成通用主题的播客。

#### 主持人 - 林知远
- **性格**：理性温和，善于引导
- **风格**：亲切自然，像电台主持人
- **职责**：引导话题，总结观点，保持讨论结构

#### 经济学家 - 陈博士
- **背景**：劳动经济学家，研究未来工作趋势
- **风格**：数据驱动，严谨冷静
- **知识源**：世界经济论坛报告、麦肯锡研究等

#### 打工人 - 小李
- **背景**：互联网公司内容运营
- **风格**：真实焦虑，情感丰富
- **视角**：普通职场人的真实担忧和体验

### 动态专业角色

系统能够基于用户主题，动态生成4-6个高度专业化的角色，确保讨论的深度和广度。

- **12+种专业类型**：包括技术专家、行业领袖、学术研究员、伦理学家等。
- **Mita搜索验证**：每个角色的知识背景都基于Mita搜索的真实学术资料和新闻进行构建。
- **定制化Prompt**：为每个角色生成包含精准事实和讨论角度的定制化Prompt。

## 🔄 工作流程

1. **话题输入**：用户通过Web界面或API输入讨论主题
2. **角色生成（可选）**：如使用动态模式，系统通过`api_server.py`分析主题，生成4-6个专业角色。
3. **背景生成**：系统利用Mita搜索生成基于真实新闻和学术资料的讨论背景。
4. **多轮讨论**：
   - **默认模式**：主持人、经济学家、打工人进行讨论。
   - **动态模式**：主持人引导多个专业角色进行深度对话。
   - 观点碰撞和深入讨论
   - 主持人总结收尾
5. **结果输出**：生成完整的播客脚本

## 📝 示例输出

当输入话题"AI对内容运营工作的影响"时，系统会生成包含以下内容的播客：

- **开场**：主持人介绍话题背景
- **经济学视角**：引用世界经济论坛数据，分析结构性转变
- **打工人担忧**：真实表达被AI替代的焦虑
- **观点碰撞**：对乐观预测的质疑和深入讨论
- **总结建议**：给打工人的实用建议

## 🔧 技术栈

- **后端**：Flask / FastAPI + Python
- **AI模型**：DeepSeek Chat / Kimi (Mita Search)
- **前端**：HTML5 + CSS3 + JavaScript
- **异步处理**：asyncio + uvicorn

## 🎯 使用场景

- **内容创作**：快速生成播客脚本
- **教育培训**：展示不同观点的碰撞
- **产品演示**：展示AI Agent协作能力
- **创意启发**：为真实播客提供灵感

## 📈 未来扩展

- [x] ✅ **批量生成和导出功能** - 已完成！支持JSON/TXT/Markdown多格式导出
- [x] ✅ **话题模板库** - 已完成！支持自定义话题和轮数控制
- [x] ✅ **动态角色生成** - 已完成！支持基于主题和Mita搜索的专业角色生成。
- [ ] 支持更多角色类型
- [ ] 添加语音合成功能
- [ ] 用户自定义角色prompt

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

MIT License - 详见LICENSE文件