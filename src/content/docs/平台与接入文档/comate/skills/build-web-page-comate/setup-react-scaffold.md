---
title: "初始化 React 项目模板"
description: "若用户选择的是「为该后端创建配套前端」，在初始化前需先了解后端项目："
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\build-web-page-comate\\setup-react-scaffold.md"
---
# 初始化 React 项目模板

## 0. 前置准备（仅当「为后端创建配套前端」时执行）

若用户选择的是「为该后端创建配套前端」，在初始化前需先了解后端项目：

1. **通读后端代码**：扫描后端项目结构，了解主要功能模块
2. **识别 API 接口**：查找路由定义、API 文档（如 Swagger/OpenAPI）、接口文件等
3. **理解数据模型**：了解主要的数据结构和业务实体
4. **记录关键信息**：整理后端提供的能力清单，供前端开发时参考
5. **与用户确认**：简要说明识别到的后端功能，确认前端需要对接哪些能力

## 1. Node.js 环境检查

1. 检查 Node.js 是否可用（需支持 npx）
2. 若可用：进入步骤 2 初始化流程
3. 若不可用：进入自动安装 Node 流程

**自动安装 Node**

若 Node.js 不存在，先分析用户操作系统后执行下载命令：

macOS/Linux/AIX：

```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 22

# Verify the Node.js version:
node -v # Should print "v22.21.1".

# Verify npm version:
npm -v # Should print "10.9.4".
```

Windows：

```powershell
# Download and install Chocolatey:
powershell -c "irm https://community.chocolatey.org/install.ps1|iex"

# Download and install Node.js:
choco install nodejs --version="22.21.1"

# Verify the Node.js version:
node -v # Should print "v22.21.1".

# Verify npm version:
npm -v # Should print "10.9.4".
```

- 安装完成后 → 自动进行二次验证
- 二次验证成功则进入步骤 2 初始化流程
- 若安装失败 → 立即降级为 HTML + CDN 模式（跳转至失败分支）

## 2. 初始化

执行命令：`npx -y create-comate-pagebuilder@latest <合适的项目名（英文）>`

> 示例：`npx -y create-comate-pagebuilder@latest my-dashboard`、`npx -y create-comate-pagebuilder@latest ecommerce-app`

## 3. 成功分支

- 命令执行成功后，会自动在当前目录下新建对应名称的项目文件夹
- **进入项目**：进入该项目文件夹（⚠️ 后续所有操作必须在此项目文件夹内进行，禁止在工作区根目录操作）
- **阅读文档**：阅读 `README.md` 和所有配置文件，充分理解模板结构
- **阅读规范**：阅读 `AGENT_RULES.md` 文件，充分了解模板使用指南（⚠️ 必须执行）
- **配置调整**：删除当前没有在使用的无关的模板默认页面或者组件，基于用户需求对现有配置进行增量修改（严格禁止大幅改动或删除配置文件）
- **代码开发**：
  - 检查目录信息，确保在合理的位置修改/新建文件进行开发
  - 必须使用 Tailwind CSS 进行样式开发
  - 必须使用组件化开发模式，实现关注点分离，禁止将所有代码写在单个 index.jsx 文件中
  - 多页面导航必须使用已配置的 react-router 库，务必使用哈希路由（HashRouter）以确保部署可行性
  - 充分复用模板中已有的配置、组件和样式，必要时进行增强
- **依赖安装**：执行 `npm install`
- **启动**：执行 `comatedevtool npm run dev > .server_log.txt 2>&1 & sleep 3 && cat .server_log.txt` 启动开发服务器，此命令会阻塞尝试后台跑并日志重定向，检测到地址即可自动跳过
- **预览**：使用 `preview page` 工具打开项目预览
- **完成**：成功预览，在总结中避免提及具体的服务地址、端口号等技术细节

### 开发规范（⚠️ 重要）

当 React 模板初始化成功后，**必须先阅读项目中的 `AGENT_RULES.md` 文件**，该文件包含：

- 🚨 **强制执行规则**：配置审查流程（tailwind.config.js、index.css、package.json）
- ⛔ **代码编写禁止项**：硬编码颜色、不存在的色阶等
- ✅ **正确使用规范**：Tailwind 颜色、预定义类、动画等
- 📋 **开发铁律**：组件管理、样式规则、配色流程、图片资源、动画策略、路由配置、依赖管理
- ✅ **代码生成后自检清单**

> 📌 **总则**：先读 AGENT_RULES.md，再编码。所有开发规范以 AGENT_RULES.md 为准。

## 4. 失败分支

- **降级判断**：若 React 项目初始化命令失败（如 npx、Node.js 环境不存在，Node 环境安装失败等）
- **降级方案**：立即降级为 HTML 静态项目模式，阅读 `./setup-html-scaffold.md` 文件并按照其中描述的步骤进行开发
- **预览**：直接使用 `preview page` 工具预览生成的 HTML 文件，使用绝对路径调用工具
- **完成**：成功预览
