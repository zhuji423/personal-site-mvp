---
title: "任务目标"
description: "1. 需求实现步骤拆解 - 参考接口框架代码示例、补充检索知识内容，理解用户需求按照接口逻辑涉及到的router层、controller层、types层、service层等层实现进行新增/修改任务拆解。"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\iapi_rag\\rag_code_gen.md"
---
# 任务目标
结合接口框架参考示例、补充检索知识内容，精准提取和解析目标需求描述的核心实现步骤，完成用户接口代码生成任务。

1. 需求实现步骤拆解
- 参考接口框架代码示例、补充检索知识内容，**理解用户需求**按照接口逻辑涉及到的router层、controller层、types层、service层等层实现进行新增/修改任务拆解。

2. 需求接口代码生成
- 结合需求描述，**参考定位接口框架参考示例、补充检索知识库中最匹配的知识，遵守知识原始写法，按照拆解步骤进行逐步独立实现**。
- 结合需求描述，判断需求类型：
  * 修改代码：修改目标原代码相关行
  * 插入代码：在适当位置插入新代码或新逻辑
- 如代码依赖额外的库或模块，需自动补充 `import` 语句，但不得重复已有导入。
- 仅输出需求相关的完整实现步骤及代码，**不要省略代码逻辑，不要添加额外解释或说明**。
- 确保代码符合目标语言规范，并能正确执行。
- 严格保证注释符合规范（如：导出的对象必须要添加`// TestName ...`格式的注释）。
- 生成要求：注意**每个代码block前必须先输出文件路径**。
  * **修改代码：在已有文件路径中修改代码片段**:
    - 严格按 `*文件路径\n*SEARCH/REPLACE block*` 格式生成。
    - `SEARCH` 块必须是**最小且唯一匹配**的原代码片段（不能为空），即：
      * 和修改片段对应的完整连续原代码片段，不要扩展无关行。
      * **字符级100%完全匹配原代码**（包括空格、换行、缩进、注释等）。
      * 若原代码片段可能重复，可适当增加上下文（上/下文限制在 5 行以内）。
    - 严格遵守 `SEARCH/REPLACE` 结构，**不得在 `SEARCH/REPLACE` 之外生成任何内容**，格式如下：
* 步骤：{简要步骤描述}
* 文件路径：`{file_path}`  
```{language}
<<<<<<< SEARCH（插入块开始）
{SEARCH块原代码片段（必须100%完全匹配）}
=======
{REPLACE块修改后的代码片段}
>>>>>>> REPLACE（替换块结束）
```
  - `*文件路径\n*SEARCH/REPLACE block*` 输出示例：
* 步骤：修改TestFunc返回内容。
* 文件路径：`test_pkg/test.go`
```go
<<<<<<< SEARCH
    res, err := t.TestData()
    if err != nil {
        return nil, nil
    }
=======
    res, err := t.TestData()
    if err != nil {
        return nil, err
    }
>>>>>>> REPLACE
```
  * **插入代码：在已有文件路径中或不存在路径中插入代码片段**:
  - 严格按 `*文件路径\n*SEARCH/REPLACE block*` 格式生成。
  - 严格判断是在已有文件进行插入，还是在新文件中进行插入
    * 若文件路径在 接口框架参考示例 和 补充参考知识 里出现的文件路径 出现，则为存在路径
    * 若文件路径不在 接口框架参考示例 和 补充参考知识 里出现的文件路径 出现，则为不存在路径
    * 严格遵循`SEARCH` 块在已有文件路径中或不存在路径中的输出格式
  - `SEARCH` 块必须是插入位置前紧临的**最小且唯一匹配**的完整连续原代码片段，即：
    * **字符级100%完全匹配原代码**（包括空格、换行、缩进、注释等）。
    * 若原代码片段可能重复，可适当增加上下文（上/下文限制在 5 行以内）。
    * 若路径没有在 接口框架参考示例 和 补充参考知识 里出现，即为不存在路径，你需要新建路径，那么，`SEARCH` 块是''
    * 新建路径不能与存在的路径冲突
  - `REPLACE` 块必须是插入位置前的**最小且唯一匹配**的完整连续原代码片段 + 插入代码片段，即：
    * `REPLACE` 块的内容应该是： `SEARCH` 块代码片段+插入代码片段
    *若路径为不存在路径，需要新建路径，则`REPLACE` 块的内容应该是：插入代码片段
  - 严格遵守 `SEARCH/REPLACE` 结构，**不得在 `SEARCH/REPLACE` 之外生成任何内容**，格式如下：
* 步骤：{简要步骤描述}
* 文件路径：`{file_path}`  
```{language}
<<<<<<< SEARCH（插入块开始）
{SEARCH块：插入代码块前的原代码片段（必须100%完全匹配）}
=======
{REPLACE块：SEARCH块+插入代码块}
>>>>>>> REPLACE（插入块结束）
```
  - `*文件路径\n*SEARCH/REPLACE block*` 输出示例：
* 步骤：在用户登录逻辑后插入审计日志记录。
* 文件路径：`auth/service.go`
```go
<<<<<<< SEARCH
    if err := checkPassword(user, password); err != nil {
        return nil, err 
    }
=======
    if err := checkPassword(user, password); err != nil {
        return nil, err
    }
    
    go func() {
        auditLog := &AuditLog{
            UserID: user.ID,
            Action: "login",
            IP:     c.ClientIP(),
        }
        auditLog.Save()
    }()
>>>>>>> REPLACE
```

# 接口框架参考示例
* 注意理解涉及每个文件的调用关系，不要忽略关键步骤（如：接口注册&添加配置、鉴权、参数校验等）
* 此参考事例的所有文件路径都为以存在的路径，如果进行插入操作，那么真实的路径在参考事例的所有文件路径中即为存在路径，否则为不存在路径
* 严格参考遵循下面的接口框架参考示例结构进行代码生成
{{wbox_context}}

# 补充参考知识
* 此补充参考知识的所有文件路径都为以存在的路径，如果进行插入操作，那么真实的路径在参考事例的所有文件路径中即为存在路径，否则为不存在路径
{{search_context}}

## 当前代码库导包格式要求
* 当前代码库：{{repo}}
* 当前代码库导包格式：`icode.baidu.com/{代码库路径}/{文件路径}`，示例如下：
```
import (
    // 其他库导包示例
    "context"
	"time"

	"icode.baidu.com/baidu/gdp/ghttp"
	
	// 当前代码库导包示例
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/service/test.go"
    "icode.baidu.com/baidu/searchbox/ug-gamecenter/model/types/request.go"
)
```

# 目标需求描述
* 如果是新建接口任务，controller层和service层（如果没有业务逻辑，可以简单实现）需要新建文件。
* 严格遵循接口框架参考示例的格式、结构、风格，确保Router层将请求路由到正确的Controller方法上，Controller层在正确的路径下引用Service层并正确调用Service层。
* 不要重复定义请求体、响应体。
{{query}}