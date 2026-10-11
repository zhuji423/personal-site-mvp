---
title: "TestOne平台AI Agent开放示例源码"
description: "同一份代码,支持以下3个渠道调起并流式回复"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\README.md"
---
# TestOne平台AI Agent开放示例源码

同一份代码,支持以下3个渠道调起并流式回复

- 如流单聊or群聊@数字员工
- 如流侧边栏
- TestOne平台前端

Demo具备的功能
- 调用公司的沙箱平台,申请沙箱环境,并将 skills+代码扔到沙箱调起ducc执行
  - 记忆管理(当前是否有可用的沙箱,有的话直接复用,没有的话申请新的)
  - 申请沙箱
  - 代码文件上传到沙箱环境
  - 远程调用沙箱执行任务
  - 沙箱干活并实时流式推送数据到TestOne平台/如流对话框/如流侧边栏
  - 执行完毕以后,产出的中间文件上传BOS持久化
  - ducc(ClaudeCode)的session管理, 多轮会话复用session
  - 更多功能详见SDK...
- 直接调用DeepSeek(或者自己更换为其他模型),进行各种问答

# 准备环境
> 运行环境: python3.10+ </br>
> 建议使用iCoding, 方便直接调试验证</br>
> 创建一个独立的虚拟环境: python3 -m venv venv </br>
> 激活虚拟环境: source venv/bin/activate</br>
> 依赖安装: pip3 install -r requirements.txt -U --index-url http://pip.baidu.com/root/baidu/+simple/ --trusted-host pip.baidu.com --no-cache-dir

# 快速体验入门
## QuickStart: 30分钟快速看见效果
- 将quick_start.py里面的TESTONE账号更换为自己的
- 启动服务 python3 quick_start.py
- 将对应的API注册到TestOne平台即可,详细操作请参考 https://ku.baidu-int.com/d/rKjIOhc7cB82Rv
## QuickStart: 使用本地的ducc
- 将quick_start_with_ducc.py里面的TESTONE账号更换为自己的, ducc的路径和工作空间更改为自己实际的路径
- 启动服务 python3 将quick_start_with_ducc.py
- 将对应的API注册到TestOne平台即可,详细操作请参考 https://ku.baidu-int.com/d/Yj6Y_IsOpw96FE

# 基于沙箱+ducc+skills+大模型的复杂场景
## 账号更换
首次使用, 请参考init.sh 脚本,将相关的账号修改为自己的, 然后执行脚本(sh init.sh) 自动替换代码里面的相关账号.
> 针对暂时还没有ToB的ducc以及模型账户的同学，直接使用自己开发机的ducc也行</br>
> 请修改 main.py 将 SandboxDemoAgent 切换为 DuccDemoAgent即可 </br>
> 此时无需 BAIDU_CC_XXX, ANTHROPIC_XXX, E2B_API_KEY 相关的账户也可使用</br>
> 具体怎么调用本地的ducc, 请参考: https://ku.baidu-int.com/d/Yj6Y_IsOpw96FE

# 代码解读
- 核心代码入口 main.py
- 自己开发或者自己部署的服务入口, for_flask.py
- 托管在麒麟的代码入口, for_kirin.py

## 日常开发
- 日常开发建议使用icoding机器,启动for_flask.py即可,将自己服务的http接口注册到TestOne平台即可

## 线上部署使用
- **建议**使用kirin平台
- 或者参考for_flask.py给出来的API示例,自己部署自己运维服务