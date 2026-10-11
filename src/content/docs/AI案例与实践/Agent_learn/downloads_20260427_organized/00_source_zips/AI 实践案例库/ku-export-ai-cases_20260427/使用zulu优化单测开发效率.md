---
title: "单元测试规范"
description: "使用zulu优化单测开发效率"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\使用zulu优化单测开发效率.md"
---
使用zulu优化单测开发效率

#### 🧑‍🏫 案例作者：[@徐志明](https://ku.baidu-int.com?t=mention&mt=contact&id=337a30e0-fced-11f0-bb14-c9da0b828592)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了使用zulu优化单测开发效率的经验。针对mock代码分析迭代次数多、修复效果不理想的问题，通过为代码库生成单测规则，显著提升了修复效率和准确性。规则包括文件组织、测试执行规范、mock逻辑说明等，使单测修复从多次交互优化为1-2次交互完成，极大提高了开发效率和代码质量。
## 总结
1. 使用规则之后，zulu效果有可感知的提升
2. 建议代码库owner将规则生成好，可以优化后续同学的上手体验

## 背景
有1个使用mock机制的单测任务写的有问题，准备用zulu进行修复。但是，zulu修复的效果不太理想：

1. 运行单测的时候误修改单测内容（增加依赖），导致测试执行失败，需要返工
2. 本次变更只修改了1个单测任务，但是却回归测试了整个package，等待耗时高
3. 针对mock代码的分析迭代次数较多

因为上面几点，导致耗时增加，甚至需要增加交互次数，降低了自动修复单测的性价比。如果是新同学上手时就遇到这些问题，容易打消积极性。



根据官方文档的介绍，发现规则（rules）是比较合适的解决方案，经过尝试，效果非常理想。

## 一、为代码库生成（单测）规则
规则（rules）的介绍：[Coding Agent学习之旅](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/uki8i2YOsd/EJUDf4xgPwrTWd#anchor-13aeccb0-c6ad-11f0-b4d6-dbf43a7b9b30?t=mention&mt=doc&dt=doc)

|问题|操作|执行结果|
|-|-|-|
|代码库没有规则文件，zulu的操作少了很多关键约束，容易出错|让zulu生成默认的规则![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9a03eba404f644a5b38cbe3796f6008f&docGuid=Gyfb3XaJ47W1hF "")|自动生成了多个规则文件规则文件介绍了项目整体的框架，目录组织等，有比较大的参考价值![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4dc9e9976fed47819c6d87e029199bae&docGuid=Gyfb3XaJ47W1hF "")|
|默认生成的规则没有覆盖单测|让zulu针对单测生成规则![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d4a5365a99924c719405b438dc2896af&docGuid=Gyfb3XaJ47W1hF "")|单测的规则说明了单测的通用要求，格式也非常规范![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=37030701ad37476da4c4180872f3f1e1&docGuid=Gyfb3XaJ47W1hF "")|
|默认生成的单测规则，没有包含“文件组织”要求，导致zulu修复单测时会添加一些多余代码zulu修改单测时，修改完成后会测试package或xx_test.go整个文件，测试效率低或者执行失败|让zulu修改单测规则，添加特殊要求![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=665a28f1f5964036a1e895caeba1adc5&docGuid=Gyfb3XaJ47W1hF "")|根据要求，添加了“包级测试文件组织”、“测试执行规范”，符合预期![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e598b7f57b0f49a4b3e368bccbb5d287&docGuid=Gyfb3XaJ47W1hF "")|
|http的mock，是单测中最复杂的逻辑，新同学也容易犯错，对此逻辑增加特别说明|让zulu介绍mock逻辑的原理并举例说明用法![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=baeba389adcf43e0a4622d2d90e8b839&docGuid=Gyfb3XaJ47W1hF "")|根据要求，介绍了mock的工作原理，并给出了示例![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a84da339f6f74eadb93519defe8c9dd0&docGuid=Gyfb3XaJ47W1hF "")|
|经过多次修改，单测的规则文件结构不那么清晰，需要优化|让zulu帮优化规则表述![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f6719c644c8e4a96ac74a14d592b0589&docGuid=Gyfb3XaJ47W1hF "")|只需要1分钟，就从结构、段落、表述等多个方面修改了规则人工来写，半个小时也难以这个效果将来有新同学了，这个规则文档也是非常好的上手说明![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=461bf9de75664ea1b32f2ed4839181f8&docGuid=Gyfb3XaJ47W1hF "")|



最终生成的单测规则：[评审：system-management-733 add rules](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/simian/brain-data-api-server/reviews/118964988/files/base...latest/.comate/rules/unit-testing.mdr?t=mention&mt=doc&dt=sdk)

```
---
globs: **/*_test.go,library/testutil/**
description: 单元测试编写规范和最佳实践
---
# 单元测试规范
## 概述
本规范定义了项目的单元测试编写标准，确保测试代码的质量、一致性和可维护性。
## 1. 测试文件组织规范
### 1.1 包级测试组织模式
参考 model/data/pandora 包的最佳实践：
**文件组织结构**：
- `*_suite_test.go` - 测试套件入口，定义全局的 BeforeSuite/AfterSuite
- `*_test.go` - 按功能模块拆分的具体测试文件
**pandora包示例**：
- `pandora_suite_test.go` - 测试套件配置
- `federa_info_test.go` - Federation信息相关测试
- `host_test.go` - 主机信息相关测试
- `instance_test.go` - 实例信息相关测试
- `naming_service_test.go` - 命名服务相关测试
### 1.2 修改单测代码规则
**必须遵守的执行流程**：
1. **优先检查suite_test.go**：修改测试代码前，必须先检查package下是否存在`suite_test.go`文件
2. **创建缺失的套件文件**：如果没有`suite_test.go`文件，必须先创建对应的测试套件文件
3. **限制修改范围**：如果已有`suite_test.go`文件，只能修改`_test.go`文件，不能修改其他内容
**套件文件创建模板**：
```go
package packagename
import (
    "github.com/onsi/ginkgo/v2"
    "github.com/onsi/gomega"
)
var _ = ginkgo.Describe("Package Test Suite", func() {
    ginkgo.BeforeSuite(func() {
        // 包级初始化逻辑
    })
    
    ginkgo.AfterSuite(func() {
        // 包级清理逻辑
    })
})
```
### 1.3 测试执行原则
- **禁止直接运行文件级测试**：不使用 `go test *_test.go` 命令
- **优先使用ginkgo focus语法**：进行精准的测试用例执行
- **避免无谓的完整包测试**：修改单个用例时不执行整个包
## 2. 测试框架与工具
### 2.1 推荐框架
- **Ginkgo** - BDD测试框架
- **Gomega** - 断言库
- **library/testutil** - 项目自定义测试工具集
## 3. 测试用例执行规范
### 3.1 Ginkgo Focus语法使用
使用focus语法可以精准执行特定测试用例：
```bash
# 执行FederaInfo相关测试
ginkgo -focus="FederaInfo" ./model/data/pandora/
# 执行特定标签的测试（如label selector）
ginkgo -focus="label selector parsing" ./model/data/pandora/
# 执行所有标记为FIt的测试用例
ginkgo -focus=".*" ./model/data/pandora/
# 查看可用focus模式（预览）
ginkgo -focus=".*" ./model/data/pandora/ --dry-run
```
### 3.2 改动用例的测试策略
修改测试代码时，按以下优先级选择执行方式：
1. **FIt** - 单个测试用例（最高优先级）
2. **FContext** - 特定场景组
3. **FDescribe** - 特定组件组
4. **完整包测试** - 尽量避免使用
## 4. 测试用例结构规范
### 4.1 Ginkgo测试结构模板
```go
var _ = ginkgo.Describe("组件名称", func() {
    Context("具体场景", func() {
        BeforeEach(func() {
            // 测试前置设置
        })
        AfterEach(func() {
            // 测试后置清理
        })
        
        It("测试用例描述", func() {
            // 测试逻辑实现
        })
    })
})
```
### 4.2 结构要素说明
- **Describe** - 描述被测试的组件
- **Context** - 描述具体的测试场景
- **It** - 定义单个测试用例
- **BeforeEach/AfterEach** - 测试前后置操作
## 5. 测试环境与依赖管理
### 5.1 测试环境初始化
使用统一的环境初始化函数：
```go
// 在测试套件的BeforeSuite中调用
InitTestCommon()
```
**初始化内容包括**：
- 设置测试运行模式：`util.SetRunMode(env.RunModeTest)`
- 配置加载：`boot.MustLoadAppConfig()`
- 日志重定向到stdout
- GDP框架初始化
- Mock服务器设置
### 5.2 外部依赖Mock
对于有外部依赖的测试，使用Mock机制：
**HTTP服务Mock示例**：
```go
handler := testutil.MockHTTPServerHandler{
    UrlPath: "/api/getData",
    MockResponseBody: `{"data":[],"message":"OK","success":true}`,
}
```
## 6. 断言与验证规范
### 6.1 Gomega断言使用
```go
// 基础断言
Expect(err).To(BeNil())
Expect(result).To(Equal(expected))
Expect(slice).To(HaveLen(expectLen))
// 错误处理断言
if testCase.ErrMessage != "" {
    Expect(err).To(MatchError(ContainSubstring(testCase.ErrMessage)))
}
```
### 6.2 表格驱动测试模式
使用结构体定义测试用例：
```go
testCases := []struct {
    name         string
    input        string
    expected     interface{}
    errMessage   string
}{
    {"正常用例", "valid_input", expectedResult, ""},
    {"异常用例", "invalid_input", nil, "错误信息"},
}
```
## 7. 测试数据管理
### 7.1 数据验证要点
- 验证时间戳唯一性
- 检查批量请求的数据合并正确性
- 充分测试异常场景和边界条件
## 8. 关键规则总结
### 8.1 必须遵守的原则
1. **优先检查suite_test.go**：修改测试代码前必须检查并创建缺失的套件文件
2. **限制修改范围**：存在suite_test.go时只能修改_test.go文件
3. **严禁文件级测试**：禁止使用文件路径直接执行测试
4. **精准测试优先**：改动用例时使用Focus语法进行精准测试
5. **Mock外部依赖**：确保测试的稳定性和可重复性
6. **手工测试标记**：需要手动执行的测试必须使用Skip标记
### 8.2 合规执行流程示例
```bash
# ✅ 合规流程：
# 1. 检查package下是否有suite_test.go文件
ls $PACKAGE_PATH/*suite_test.go
# 2. 如果没有则创建套件文件
# 3. 然后修改具体的_test.go文件
# 4. 使用focus语法精准测试
ginkgo -focus="特定用例" ./$PACKAGE_PATH/
```
### 8.3 测试代码修改约束
**允许的操作**：
- 修改、新增、删除`_test.go`文件的内容
- 当缺少`suite_test.go`时创建该文件
**禁止的操作**：
- 当存在`suite_test.go`时修改该文件
- 修改非测试文件（`.go`但不以`_test.go`结尾）
- 删除已存在的`suite_test.go`文件
### 8.4 合规与违规示例
```bash
# ❌ 违规：执行文件级测试
ginkgo ./model/data/pandora/host_test.go
# ❌ 违规：修改单个用例时执行完整包测试
ginkgo ./model/data/pandora/
# ✅ 合规：使用focus语法精准测试
ginkgo -focus="FederaInfo" ./model/data/pandora/
ginkgo -focus=".*" ./model/data/pandora/
```
## 9. 最佳实践建议
### 9.1 测试用例设计
- 每个测试用例只验证一个功能点
- 测试用例描述要清晰明确
- 覆盖正常流程、异常流程和边界条件
### 9.2 可维护性
- 保持测试代码的简洁性
- 使用有意义的变量名和函数名
- 定期清理过时的测试用例
通过遵循这些规范，可以确保项目的单元测试质量，提高代码的可维护性和可靠性。
## 10. Mock逻辑工作示例
### 10.1 RAL RPC框架Service Name替换机制
项目中通过`library/testutil`包提供RAL RPC框架的service name替换功能，核心原理是将外部服务的service name替换为本地Mock服务器的service name。
**Service Name替换示例**：
```go
package aladdin
import (
    "context"
    
    "icode.baidu.com/baidu/simian/brain-data-api-server/library/testutil"
    "icode.baidu.com/baidu/simian/brain-data-api-server/library/util"
)
var _ = Describe("Aladdin数据获取", func() {
    BeforeEach(func() {
        // 初始化测试环境
        InitTestCommon()  
        // 在BeforeSuite中已经自动调用了mockRalServicer(constant.LOCAL_UNIT_TEST_SERVER_NAME)
        // 所有RAL请求会被重定向到Mock服务器
    })
    
    It("应该能从Aladdin获取数据", func() {
        // 真实代码中，RAL请求会使用ServiceName常量
        result, err := GetAladdinData(context.Background())
        Expect(err).To(BeNil())
        Expect(result).ToNot(BeNil())
    })
})
```
**替换机制说明**：
- 在测试模式下，`util.GetRalRequestServerName()`函数会将任意service name替换为`constant.LOCAL_UNIT_TEST_SERVER_NAME`
- Mock服务器会自动注册这个service name到RAL框架，指向本地Mock服务器进程
- 所有外部RPC请求都会被拦截并转发到Mock服务器处理
### 10.2 HTTP结果Mock示例
使用`testutil.MockHTTPServerHandler`可以灵活地Mock HTTP API的响应结果。
**HTTP Mock配置示例**：
```go
package noah
import (
    "context"
    
    "icode.baidu.com/baidu/simian/brain-data-api-server/library/testutil"
)
var _ = Describe("Noah数据查询", func() {
    BeforeEach(func() {
        // 配置Mock Noah API响应
        handler := testutil.MockHTTPServerHandler{
            UrlPath: "/monquery/getHistoryitemdata",
            UrlParameters: map[string]testutil.MockRalHandlerParameterValueMatcher{
                "namespaces": testutil.MockEqualMatcher("ps-arc.www.hba"),
                "items":      testutil.MockEqualMatcher("cpu_usage"),
                "start":      testutil.MockPrefixMatcher("20250404080000"),
                "end":        testutil.MockPrefixMatcher("20250404090000"),
            },
            MockResponseBody: `{
                "data": [{
                    "NameSpace": "ps-arc.www.hba",
                    "Items": {
                        "cpu_usage": [{
                            "Timestamp": 1743724800,
                            "Value": 85.5
                        }]
                    }
                }],
                "message": "OK",
                "success": true
            }`,
        }
        
        Expect(testutil.GlobalMockHTTPServer.RegisterHandler(handler)).To(Succeed())
    })
    
    It("应该能获取Noah监控数据", func() {
        request := Request{
            NameSpaces: []string{"ps-arc.www.hba"},
            Items:      []string{"cpu_usage"},
            Start:      "20250404080000",
            End:        "20250404090000",
        }
        
        result, err := GetNoahDataByParams(context.Background(), request)
        Expect(err).To(BeNil())
        Expect(result.Data).To(HaveLen(1))
        Expect(result.Data[0].NameSpace).To(Equal("ps-arc.www.hba"))
    })
})
```
**Mock参数匹配器说明**：
- `MockEqualMatcher`: 精确匹配参数值
- `MockPrefixMatcher`: 匹配参数值前缀
- `MockSuffixMatcher`: 匹配参数值后缀
- `MockContainsMatcher`: 包含特定字符串
### 10.3 Mock逻辑工作流程总结
1. **初始化阶段**：测试套件启动时，Mock服务器创建并注册到RAL框架
2. **Service Name重定向**：所有外部RPC请求自动重定向到Mock服务器
3. **HTTP Handler注册**：为具体API路径注册Mock处理器和响应数据
4. **请求拦截**：RAL框架将请求转发到对应的Mock处理器
5. **响应返回**：Mock处理器返回预设的响应数据
6. **测试完成**：测试结束后Mock服务器自动清理
通过这种机制，单元测试可以完全隔离外部依赖，确保测试的稳定性和可重复性。
```
## 二、修复单测
### 问题说明
有个单测任务，没有mock http请求的结果，导致单测执行过程中抛出异常，虽然单测执行不会失败，但是打印出来的信息会干扰问题排查。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ad38e621e3164ee7be172f83162ccfcb&docGuid=Gyfb3XaJ47W1hF "")
### 修复效果
使用单测规则后，zulu可以在1次交互（耗时2分钟）左右自动完成问题确认、分析、修复、验证。

注：单测规则针对比较复杂的Mock逻辑进行了重点说明，如果没有此说明，zulu会使用单测自带的README文件信息，仍然可以通过2次交互，完成问题修复。

|操作|执行结果|
|-|-|
|告诉zulu，单测有问题，需要修复![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1937f0c49ce141f78df50951e3f19e7e&docGuid=Gyfb3XaJ47W1hF "")|复现问题：![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7cce137ede484a0fa9c945af4bf79e26&docGuid=Gyfb3XaJ47W1hF "")分析问题：![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b3095a833837488eb521874c8e6c26ae&docGuid=Gyfb3XaJ47W1hF "")修复问题&验证结果：![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f8c58c791b6547d38638414218fa6c93&docGuid=Gyfb3XaJ47W1hF "")|



修复效果：[评审：system-management-733 add rules](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/simian/brain-data-api-server/reviews/118964988/files/base...latest/model/service/crontab/dump_model_detail_test.go?t=mention&mt=doc&dt=sdk)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
