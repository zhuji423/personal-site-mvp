---
title: "敏感信息硬编码漏洞修复流程"
description: "修复漏洞分为以下三个步骤： 1. 读取漏洞报告 2. 修复硬编码漏洞 3. 引入SDK（如果需要）"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\code-security-comate\\references\\vul_repair_sensitive.md"
---
# 敏感信息硬编码漏洞修复流程

修复漏洞分为以下三个步骤：
1. 读取漏洞报告
2. 修复硬编码漏洞
3. 引入SDK（如果需要）

## 读取漏洞报告

基于凭证配置网页回传的数据获取漏洞报告，示例如下：
```json
{
  "scanChatID": "从 credential_poll 返回的 chatUUID",
  "repo": {
    "language": "java",
    "framework": "springboot"
  },
  "deployment": {
    "platform": 2,
    "platformName": "ipipe"
  },
  "files": [
    {
      "name": "src/main/resources/application.properties",
      "hash": "文件SHA256",
      "vulList": [
        {
          "ruleID": "codescan_generic_password-config_sensitive",
          "line": 35,
          "hash": "漏洞hash",
          "extra": {
            "secret": {
              "credentialName": "KL_SPRING_DATASOURCE_PASSWORD",
              "start": {"col": 28, "line": 35},
              "end": {"col": 43, "line": 35}
            }
          }
        }
      ]
    }
  ],
  "trigger": 1,
  "type": 4
}
```
各字段说明如下：
* repo：代码库信息
    * language：代码语言
    * framework：代码框架
* deployment：部署信息
    * platform：部署平台，1 表示 cnap，2 表示 ipipe，3 表示 opera，4 表示 datamanage
    * platformName：部署平台名称（如 ipipe、cnap、opera、datamanage）
    * credential_id：凭证 ID（platform 为 4 时使用，用于引入 keyless-sdk）
* files：文件信息
    * name：漏洞文件的相对路径
    * vulList：漏洞列表
        * extra.secret.start：敏感信息的开始位置（行、列）
        * extra.secret.end：敏感信息的结束位置（行、列）
        * extra.secret.credentialName：建议使用的环境变量名称

## 修复漏洞
硬编码漏洞修复的本质就是改变原来在代码中的硬编码敏感信息写法，改为从环境变量中读取敏感信息。修复时遍历漏洞报告中的所有文件和漏洞，逐个修复，按以下流程进行处理。

### 代码文件
如果漏洞文件是代码文件，比如 java、go、php、py 等，则根据各语言的写法生成读取环境变量的代码，并替换掉原来的硬编码敏感信息，注意有以下几点要求：
1. 与环境变量读取无关的其他代码和字符不要做任何改动
2. 如果漏洞行是被引号包裹的纯字符串，输出时保留其结构不变，仍然可以直接执行字符串操作，但要避免空字符串的拼接
3. 不要给出环境变量默认值
4. 如果代码开头存在空格、tab等缩进，保留原始代码的缩进，不要清除两端的空白字符
5. 如果是 python 语言，使用 os.environ 的方式获取环境变量，而不是 os.getenv
6. 如果是 go 语言，不能在 const 中读取环境变量，在 const 下方重新定义读取代码，并删除 const 的硬编码的值
7. 如果是 java 语言，且 platform 为 4 时，则采用 System.getProperty 的语法读取变量
8. 如果原文件中缺失读取环境变量所需的第三方库，则自动引入，比如 python 的 os 库，go 的 os 库等

### 配置文件
如果漏洞文件是配置文件，比如 yml、properties、ini 等，则结合语言和框架共同决定如何修改代码，修改原则如下：
1. 如果语言为 go，框架为 gdp，toml 后缀的文件直接使用特定的占位符替换敏感信息，占位符的环境变量名称根据 credential_name 命名，示例如下：
```toml
// 修复前
password=123123123
// 修复后
password=${env.KL_PASSWORD}
```
2. 除第一种情况之外，其他语言、框架、配置文件类型，使用常规的环境变量占位符替换敏感信息，占位符的环境变量名称根据 credential_name 命名。
```toml
// 修复前
password=123123123
// 修复后
password=${KL_PASSWORD}
```

漏洞报告可能涉及多个文件，修复时按文件进行聚合，优先将一个文件中的漏洞全部修复完成再修复其他漏洞。

## 引入SDK
从第一个漏洞报告读取数据，如果 platform 为 4 时需要引入 keyless-sdk 并添加初始化代码。通过该 sdk 将凭证注入到环境变量中，然后其他位置的代码才能读取到环境变量。注意，只有平台为 4 时才需要引入 sdk，其他平台不需要。不同语言 sdk 及初始化代码添加方式如下。

#### java 语言
pom.xml 文件中添加 keyless-sdk 依赖，其中的注释需要保留。
```xml
<!-- keyless-sdk dependency -->
<dependency>
    <groupId>com.baidu.xbu-data</groupId>
    <artifactId>keyless-sdk</artifactId>
    <version>1.0.2</version>
</dependency>
```
项目启动的函数中添加以下初始化代码，注意其中的 credentialID 需要与漏洞报告中的 credential_id 保持一致。
```java
import com.baidu.keyless.KeylessClient;

public class KeylessAppCredentialDemo {
    public static void main(String[] args) {
        // 初始化 keyless-sdk 开始
        // step1: 设置 credentialID 构建 client，详情可参考 https://ku.baidu-int.com/d/BRnvQROwD8akQY
        String credentialID = "appDemo_prod";
        KeylessClient keylessClient = KeylessClient.builder()
            .credentialId(credentialID)
            .build();
        // step2: 获取凭证信息并注入到系统环境变量中
        try {
            keylessClient.load();
        } catch (Exception e) {
            System.out.println("load keyless client error: " + e.getMessage());
        }
        // 初始化 keyless-sdk 结束
        // 以下为其他原始代码
        ... ...
    }
}
```

#### go 语言
go.mod 文件中添加 keyless-sdk 依赖，其中的注释需要保留。
```mod
require (
    icode.baidu.com/baidu/xbu-data/things-go keyless-sdk-2.2.0 // keyless-sdk dependency
)
```
项目启动的函数中添加以下初始化代码，注意其中的 CredentialID 需要与漏洞报告中的 credential_id 保持一致。
```go
package main

import (
    "icode.baidu.com/baidu/xbu-data/things-go/pkg/keyless"
)

func main() {
    // 初始化 keyless-sdk 开始
    // step1: 设置 CredentialID 构建 client，详情可参考 https://ku.baidu-int.com/d/G_QqzMQrQR9_K_
    req := &keyless.GetCredentialReq{
        CredentialID: "appDemo_prod", // 凭证标识
    }
    // step2: 获取凭证信息并注入到系统环境变量中
    client := keyless.NewClient(req)
    err := client.Load()
    if err != nil {
        fmt.Println(err.Error())
        return
    }
    // 初始化 keyless-sdk 结束
    // 以下为其他原始代码
        ... ...
}
```

#### python 语言
requirements.txt 文件中添加 keyless-sdk 依赖，其中的注释需要保留。
```txt
// keyless-sdk dependency
credential-vault-sdk>=0.1.12（Python3 版本添加此依赖）
credential-vault-sdk-py2>=0.1.9（Python2 版本添加此依赖）
```
初始化代码如下，注意
* 其中的 credential_id 需要与漏洞报告中的 credential_id 保持一致；
* 如果是完整的服务或项目，初始化代码要添加在项目启动的函数中；
* 如果是独立的 Python 脚本文件，每个独立的文件都要添加 keyless-sdk 依赖和初始化代码。
```python
from credential_vault_sdk.keyless_client import KeylessClient

def main():
    # 初始化 keyless-sdk 开始
    # step1: 设置 credential_id 构建 client，详情可参考 https://ku.baidu-int.com/d/HWaSIaQSThk88b
    client = KeylessClient(credential_id="appDemo_prod")
    # step2: 获取凭证信息并注入到系统环境变量中
    client.load()
    # 初始化 keyless-sdk 结束
    # 以下为其他原始代码
    ... ...
```

#### C++ 语言
在文件开始引入头文件和命名空间，其中的注释需要保留：
```C++
// keyless-sdk dependency
#include "keyless/keyless_client.h"

using namespace baidu::credentialvault::cppsdk;
```

项目启动的函数中添加以下初始化代码，注意其中的 credentialID 需要与漏洞报告中的 credential_id 保持一致。
```C++
#include "keyless/keyless_client.h"

using namespace baidu::credentialvault::cppsdk;

int main(int argc, char *argv[]) {
    // 初始化 keyless-sdk 开始
    // step1: 设置 credential_id 构建 client，详情可参考 https://ku.baidu-int.com/d/x5s_A3YHll0PvR
    KeylessClient client = KeylessClient("appDemo_prod");
    // step2: 获取凭证信息并注入到系统环境变量中
    KeylessStatus load_result = client.load();
    if (!load_result.ok()) {
        return 0;
    }
    // 初始化 keyless-sdk 结束
    // 以下为其他原始代码
    ... ...
}
```