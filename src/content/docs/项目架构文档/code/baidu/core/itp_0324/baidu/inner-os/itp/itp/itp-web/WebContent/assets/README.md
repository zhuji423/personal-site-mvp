---
title: "README"
description: "前端打包准备工作"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_0324\\baidu\\inner-os\\itp\\itp\\itp-web\\WebContent\\assets\\README.md"
---
前端打包准备工作

1. 安装node

    下载地址 http://nodejs.cn/


2. 安装打包的插件包

    cd assets;
    npm install;
    npm install gulp -g


3. 前端开发（非前端开发可以跳过此步）

    cd mockserver;
    npm install;

    npm run dev;


4. 发布(itp平台前端 test、online 部署在一台机器上)

    发布测试: npm run test
    发布线上: npm run online
