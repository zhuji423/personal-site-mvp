---
title: ".vscode配置与运行"
description: ".vscode配置与运行"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Good Coder考试记录\\C++ Good Coder考试-词表解析读取工具类\\.vscode配置与运行.md"
---
.vscode配置与运行

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
**c_cpp_properties.json**

```
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}",
                "/Library/Developer/CommandLineTools/usr/include/c++/v1",
                "/usr/local/include",
                "/Library/Developer/CommandLineTools/usr/lib/clang/10.0.1/include",
                "/Library/Developer/CommandLineTools/usr/include"
            ],
            "defines": [],
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/System/Library/Frameworks"
            ],
            "compilerPath": "/usr/bin/clang++",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "clang-x64"
        }
    ],
    "version": 4
}
```
**tasks.json**

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
                "${workspaceFolder}/demo.cpp",
                "${workspaceFolder}/src/read_file_line_by_line.cpp",
                "${workspaceFolder}/src/public_parse.cpp",
                "${workspaceFolder}/src/private_parse.cpp",
                "${workspaceFolder}/src/parse.cpp",
                "-o",
                "${workspaceFolder}/demo.o"
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
编译：shift+command+b进行编译，选择

![](../../../assets/yHp40343-225oZ/image_001.bin "")
，生成demo.o文件。

**launch.json**

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++ - 生成和调试活动文件",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/demo.o",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "lldb",
            "preLaunchTask": "C/C++: g++ build active file"
        }
    ]
}
```
调试：

![](../../../assets/yHp40343-225oZ/image_002.bin "")
直接运行：

![](../../../assets/yHp40343-225oZ/image_003.bin "")

