---
title: "VSCode 搭建cc++基本开发环境 Mac"
description: "VSCode 搭建c/c++基本开发环境 Mac"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Good Coder考试记录\\C++ Good Coder考试-词表解析读取工具类\\VSCode 搭建cc++基本开发环境 Mac.md"
---
VSCode 搭建c/c++基本开发环境 Mac

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
1、vscode安装插件

![](../../../assets/2eVf8fD0b4jUG2/image_001.bin "")
2、安装cmake

![](../../../assets/2eVf8fD0b4jUG2/image_002.bin "")
3、创建一个包含.cpp文件的文件夹

![](../../../assets/2eVf8fD0b4jUG2/image_003.bin "")
4、配置c_cpp_properties.json

“command+shift+p”打开命令行工具窗口，输入或者选择“Edit Configurations(JSON)”命令。

![](../../../assets/2eVf8fD0b4jUG2/image_004.bin "")
此时会在当前工作空间目录生成.vscode配置目录，同时在配置目录会生成一个c_cpp_properties.json文件。 修改includePath：

```
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}",
                "/Library/Developer/CommandLineTools/usr/include/c++/v1",
                "/usr/local/include",
                "/Library/Developer/CommandLineTools/usr/lib/clang/10.0.1/include", // 注意版本号10.0.1需要改成自己的，去这个路径看下自己的版本号
                "/Library/Developer/CommandLineTools/usr/include",
            ],
            "defines": [],
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/System/Library/Frameworks"
            ],
            "compilerPath": "/usr/bin/clang",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "clang-x64"
        }
    ],
    "version": 4
}
```


5、配置task.json

选中main.cpp后，“command+shift+p”打开命令行工具窗口，输入或者选择“Tasks: Configure Task”，在配置目录会生成一个task.json文件。

![](../../../assets/2eVf8fD0b4jUG2/image_005.bin "")
![](../../../assets/2eVf8fD0b4jUG2/image_006.bin "")
修改args:

```
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "shell",
            "label": "C/C++: g++ build active file",
            "command": "/usr/bin/g++",
            "args": [
                "-g",
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}.o"
            ],
            "options": {
                "cwd": "${workspaceFolder}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": "build"
        }
    ]
}
```
选中main.cpp后，输入shift+command+b，选择g++ build

![](../../../assets/2eVf8fD0b4jUG2/image_007.bin "")
构建成功，生成可执行文件main.o

6、配置task.json

“command+shift+p”打开命令行工具窗口，输入或者，选择Debug: Open launch.json命令，在配置目录会生成一个launch.json文件。

![](../../../assets/2eVf8fD0b4jUG2/image_008.bin "")
![](../../../assets/2eVf8fD0b4jUG2/image_009.bin "")
修改program

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(lldb) 启动",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/main.o",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "lldb"
        }
    ]
}
```
7、调试

![](../../../assets/2eVf8fD0b4jUG2/image_010.bin "")

