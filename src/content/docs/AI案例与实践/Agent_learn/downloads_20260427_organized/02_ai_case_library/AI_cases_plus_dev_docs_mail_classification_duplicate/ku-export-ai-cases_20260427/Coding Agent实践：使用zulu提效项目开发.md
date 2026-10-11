---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "Coding Agent实践：使用zulu提效项目开发"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Coding Agent实践：使用zulu提效项目开发.md"
---
Coding Agent实践：使用zulu提效项目开发

#### 🧑‍🏫 案例作者：[@闫英杰](https://ku.baidu-int.com?t=mention&mt=contact&id=fad9b4c0-fce4-11f0-94d1-53bade43ad41)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了使用Zulu提效项目开发的实践经验。面对流量预估与实时监控指标的弹性伸缩项目，Zulu通过优化代码结构、提供模块化设计、并行处理、日志优化等建议，显著提升了开发效率和代码质量。在CodeReview和单元测试方面，Zulu也展现了高效辅助能力，成为团队中的靠谱“同事”。项目整体效率提升30%以上，CodeReview和单元测试效率提升显著。
[文档目录]
## 1、介绍
#### 1.1 项目背景
我们团队接到一项重要任务：通过对流量预估与实时监控指标，对 Deepseek 大模型集群进行弹性伸缩，旨在提升显卡利用率并降低推理成本。

由于项目排期比较紧张且对稳定性要求极高，我们在编码上面临两大挑战：

一是如何保证项目代码质量

二是繁多的单元测试是否会延误项目进度。

#### 1.2 初识 zulu
在以往的项目中，我用过 iCoding 的代码自动补全功能，效果尚可，然而，面对此项目，需要从整体上去考虑代码质量，iCoding 的代码补全功能显然无法满足需求； 在偶然的一次机会，我向组内的 Golang 专家请教代码结构问题，他推荐了 zulu。抱着尝试的心态， 我向 zulu 发出了第一条指令: "请帮我优化 run 函数"

zulu 不仅指出了原代码存在的问题，还直接生成了代码风格与 K8s controller 常见的编程风格一致的新代码！zulu 给出的优化总结：

```
优化总结
模块化：将长函数拆分为多个小函数，每个函数只做一件事
错误处理：使用错误包装提供更多上下文信息
并行处理：使用 goroutine 并行处理无依赖的规则
日志优化：使用结构化日志提高可读性
性能优化：减少重复计算，考虑缓存
代码可读性：提取魔法数字为常量，提取复杂条件为函数
状态封装：使用结构体封装相关状态数据
这些优化将使代码更易于维护、调试和扩展，同时提高性能和可靠性。
```
被 zulu 给出的回答惊呆了，从此对 zulu 产生了浓厚兴趣，并将 zulu 推荐给其他同学；

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2、项目实践
#### 2.1 模块设计（上下文以外的需求）
鉴于项目需要跨机房容灾和多副本选主功能，而跨机房部署无法使用 K8s 原生的选主功能，只能使用 Mysql、Redis 等外围组件进行选主；

于是，我对 zulu 发出指令:  "帮我写一个多副本使用 mysql 选主的函数"

zulu 不但写出来了，并且给出了对应的测试代码：

```
package mysql

import (
    "context"
    "database/sql"
    "fmt"
    "sync"
    "time"

    _ "github.com/go-sql-driver/mysql"
)

// Node 表示一个MySQL节点
type Node struct {
    ID         string
    Addr       string // 格式: "host:port"
    User       string
    Password   string
    Database   string
    Priority   int    // 优先级，数字越大优先级越高
    IsReadOnly bool   // 是否只读
    IsHealthy  bool   // 是否健康
    LastCheck  time.Time // 最后检查时间
}

// ElectMaster 从多个MySQL副本中选举主节点
func ElectMaster(ctx context.Context, nodes []*Node, checkTimeout time.Duration) (*Node, error) {
    var wg sync.WaitGroup
    var mu sync.Mutex

    // 1. 并发检查所有节点的健康状态和只读状态
    for _, node := range nodes {
        wg.Add(1)
        go func(n *Node) {
            defer wg.Done()
            
            isHealthy, isReadOnly, err := checkMySQLNode(ctx, n, checkTimeout)
            
            mu.Lock()
            defer mu.Unlock()
            
            n.IsHealthy = isHealthy
            n.IsReadOnly = isReadOnly
            n.LastCheck = time.Now()
            
            if err != nil {
                fmt.Printf("Check node %s error: %v\n", n.Addr, err)
            }
        }(node)
    }
    wg.Wait()

    // 2. 过滤出健康的、非只读的节点
    var candidates []*Node
    for _, node := range nodes {
        if node.IsHealthy && !node.IsReadOnly {
            candidates = append(candidates, node)
        }
    }

    if len(candidates) == 0 {
        return nil, fmt.Errorf("no healthy master candidate available")
    }

    // 3. 按优先级选择主节点
    var master *Node
    for _, node := range candidates {
        if master == nil || node.Priority > master.Priority {
            master = node
        }
    }

    return master, nil
}

// checkMySQLNode 检查MySQL节点的健康状态和只读状态
func checkMySQLNode(ctx context.Context, node *Node, timeout time.Duration) (bool, bool, error) {
    // 创建带超时的context
    ctx, cancel := context.WithTimeout(ctx, timeout)
    defer cancel()

    // 构建DSN
    dsn := fmt.Sprintf("%s:%s@tcp(%s)/%s?timeout=%s&readTimeout=%s&writeTimeout=%s",
        node.User, node.Password, node.Addr, node.Database, 
        timeout, timeout, timeout)

    // 连接MySQL
    db, err := sql.Open("mysql", dsn)
    if err != nil {
        return false, false, fmt.Errorf("open connection failed: %w", err)
    }
    defer db.Close()

    // 检查连接是否可用
    if err := db.PingContext(ctx); err != nil {
        return false, false, fmt.Errorf("ping failed: %w", err)
    }

    // 检查是否只读
    var readOnly int
    err = db.QueryRowContext(ctx, "SELECT @@global.read_only").Scan(&readOnly)
    if err != nil {
        return true, false, fmt.Errorf("check read_only failed: %w", err)
    }

    return true, readOnly == 1, nil
}

// PromoteToMaster 将一个节点提升为主节点
func PromoteToMaster(ctx context.Context, node *Node) error {
    db, err := sql.Open("mysql", fmt.Sprintf("%s:%s@tcp(%s)/%s", 
        node.User, node.Password, node.Addr, node.Database))
    if err != nil {
        return fmt.Errorf("open connection failed: %w", err)
    }
    defer db.Close()

    // 设置为可写
    _, err = db.ExecContext(ctx, "SET GLOBAL read_only = OFF")
    if err != nil {
        return fmt.Errorf("set read_only=OFF failed: %w", err)
    }

    // 如果是GTID模式，可以添加更多设置
    // _, err = db.ExecContext(ctx, "STOP SLAVE")
    // _, err = db.ExecContext(ctx, "RESET MASTER")

    return nil
}
```
```
func main() {
    // 定义MySQL节点
    nodes := []*mysql.Node{
        {
            ID:       "node1",
            Addr:     "192.168.1.101:3306",
            User:     "admin",
            Password: "password",
            Database: "test",
            Priority: 100,
        },
        {
            ID:       "node2",
            Addr:     "192.168.1.102:3306",
            User:     "admin",
            Password: "password",
            Database: "test",
            Priority: 90,
        },
        {
            ID:       "node3",
            Addr:     "192.168.1.103:3306",
            User:     "admin",
            Password: "password",
            Database: "test",
            Priority: 80,
        },
    }

    ctx := context.Background()
    timeout := 5 * time.Second

    // 选举主节点
    master, err := mysql.ElectMaster(ctx, nodes, timeout)
    if err != nil {
        fmt.Printf("Elect master failed: %v\n", err)
        return
    }

    fmt.Printf("Elected master: %s (%s)\n", master.ID, master.Addr)

    // 如果需要手动提升某个节点为主节点
    // err = mysql.PromoteToMaster(ctx, nodes[1])
    // if err != nil {
    //     fmt.Printf("Promote to master failed: %v\n", err)
    // }
}
```


#### 2.2 代码优化（结合上下文的需求）
在项目初期，我们遇到了代码过于复杂，不符合 icode 编码规范的问题。

![](/personal-site-mvp/img/doc-placeholder.svg "")
通过向 zulu 提交代码优化请求，zulu 给出了几个切实可行的优化建议，（涉及到业务逻辑， 代码就不贴了）， 优化效果很高，感觉 zulu 比较重视代码可读性和性能。

```
优化总结
模块化：将长函数拆分为多个小函数，每个函数只做一件事
错误处理：使用错误包装提供更多上下文信息
并行处理：使用 goroutine 并行处理无依赖的规则
日志优化：使用结构化日志提高可读性
性能优化：减少重复计算，考虑缓存
代码可读性：提取魔法数字为常量，提取复杂条件为函数
状态封装：使用结构体封装相关状态数据
这些优化将使代码更易于维护、调试和扩展，同时提高性能和可靠性。
```
#### 2.3 CodeReview（项目提效最多的场景）
在多人合作的项目中，CodeReview 至关重要。不过 zulu 没法直接读取别人的代码，我用了比较 low 的方式：将其他同学提交的代码复制到 zulu 进行的 CodeReview， 如下，直接在输入框粘贴需要 review 的代码，让 zulu 给出优化建议：

zulu 给的优化建议基本都是比较靠谱的，极大的提升了项目 CodeReview 效率。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2.4 写单元测试
生成单侧是 iCoding 之前就已经有的功能，我没有对比 zulu 生成单侧的效果和之前效果的区别，这里不多做介绍；

#### 2.5 其他实用小工具
除了上述功能外，zulu 还提供了 base64 编解码等实用小工具，让我们无需再再打开浏览器去找 base64 网站了。

![](/personal-site-mvp/img/doc-placeholder.svg "")
此外 json 格式化工具也十分便利。

![](/personal-site-mvp/img/doc-placeholder.svg "")
通过输入/能看到 zulu 支持的很多工具，我目前用到了这 2 个，比较实用。

## 3、总结
#### 3.1 项目提效
在本次项目中，Zulu为我们带来了显著的提效效果

  - 开发效率：尽管项目规模较小(大约耗时 3 人月的时间)，zulu 帮忙总体提升了 30% 以上的效率；

  - 项目质量：zulu 通过优化代码整体结构并大幅降低 code review 时间，效率能提升 100% 以上；

  - 单元测试：写单侧的时间大幅降低，与 iCoding 之前相比不太好量化，但是比人工写单侧要提效 100% 以上；

#### 3.2 使用体验
在使用 zulu 之前，我认为 AI coding 仅仅是代码补齐工具。然而，经过本次项目实践，感觉 zulu 更像是身边多了一位靠谱的同事，它不仅能帮忙进行 CodeReview、写单元测试， 甚至还能帮忙优化代码结构，设计模块功能，非常方便。

最后提个小建议：大家的开发习惯不同，会使用不同的 IDE，有些 IDC 不支持 zulu，希望 zulu 能对指定 commit 给出优化建议，将多人协助的场景效率进一步提升 🚀

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
