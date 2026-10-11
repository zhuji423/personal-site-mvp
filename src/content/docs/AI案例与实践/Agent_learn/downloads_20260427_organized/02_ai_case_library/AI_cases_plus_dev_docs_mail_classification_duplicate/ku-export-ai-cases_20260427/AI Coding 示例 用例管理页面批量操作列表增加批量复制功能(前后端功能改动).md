---
title: "实践简介"
description: "AI Coding 示例: 用例管理页面批量操作列表增加批量复制功能前后端功能改动"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI Coding 示例 用例管理页面批量操作列表增加批量复制功能(前后端功能改动).md"
---
AI Coding 示例: 用例管理页面批量操作列表增加批量复制功能(前后端功能改动)

#### 🧑‍🏫 案例作者：[@王哲](https://ku.baidu-int.com?t=mention&mt=contact&id=cd1b9560-fce6-11f0-bdd2-37f723af877d)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Cursor
#### 📒 案例概要：本文介绍了通过AI Coding实现用例管理页面批量操作列表增加批量复制功能的案例。通过与Coding Agent协同，不写一行代码完成了前后端需求，包括前端Modal设计、后端API实现及批量复制逻辑。展示了AI在提升开发效率、处理复杂需求方面的能力。
# 实践简介
该案例是前端测试智能化项目中一个真实的、来源于用户反馈的一个中小型的涉及到前后端同步改动的需求。

我们通过与 Coding Agent 协同，在不写一行代码的情况下，仅负责提出需求、评审方案、测试问题反馈就完成了一个 400+ 行的前后端需求。

从这个案例可以看出，对于一些中小型的需求，通过与 Coding Agent 协同，可以极大的提升开发的效率。

# 关键词
前后端功能改动、Python、JS

# 具体实施
## 需求来源
[[baidu-testmate-web-ui-aitester-345] 【用例管理】批量操作列表加上批量复制到某个分组功能](https://console.cloud.baidu-int.com/devops/icafe/issue/baidu-testmate-web-ui-aitester-345/show?t=mention&mt=doc&dt=sdk)

## 需求分析
典型的前后端需求改动，前端需要增加一个操作入口和对应的表单。

后端需要提供相应的批量复制的 API 接口。

## 基于 AI Coding 的规划 & 实现
这个需求相对来说相当明确，我们只需要找到对应的前端、后端的入口相关的就近代码，直接用 AI Coding 的 Plan 能力进行规划即可。

* 前端代码位置检索

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 后端代码 API 入口

![](/personal-site-mvp/img/doc-placeholder.svg "")


Plan Query

> 我希望在 @case-list.tsx 前端用例管理的批量操作按钮中，增加一个批量复制的按钮。
> 点击批量复制后，可以展开一个 Modal，支持批量设置:
> 1. 分组
> 2. 优先级
> 3. 标签
> 4. 状态
> 5. 登录用户
> 
> 其中，几个字段的组件选择复用用例编辑的组件模式即可。
> 另外，默认这几个字段都是保持原样，用户需要复制时批量修改哪个可以主动修改哪个，至少修复1项才允许用户确认。
> 另外， 后端 @case_api.py 也需要提供配套的 API 来支持相应的功能，相当于批量添加一组用例的逻辑。


模型在 Plan 过程提出了如下一系列问题:

![](/personal-site-mvp/img/doc-placeholder.svg "")
我们可以进行相关的需求澄清:

> 1. 批量复制后的用例名称支持用户在 Modal 中输入统一的后缀，不能为空
> 2. 复制时是否复制所有字段，即复制所有字段（包括 code、browser、env_id、runtime_config 等），用户只修改 Modal 中选择的字段
> 3. 是否保留原用例的关联信息: 保留关联信息
> 


在所有问题澄清完成后，可以看到它已经梳理好了一个规划文档了:

# 批量复制用例功能实现
## 实现内容
### 一、后端实现（tester/routers/case_api.py 和 utils/ui_cases_utils.py）
#### 1. 定义批量复制请求模型
在 `case_api.py` 的 `BatchDeleteRequest` 模型后添加：

```
class BatchCopyRequest(BaseModel):
    """批量复制请求模型"""
    case_ids: List[str]
    name_suffix: str  # 用例名称后缀，必填
    group_id: Optional[str] = None  # 新分组ID，可选
    priority: Optional[str] = None  # 新优先级，可选
    tags: Optional[List[str]] = None  # 新标签列表，可选
    status: Optional[str] = None  # 新状态，可选
    login_user: Optional[str] = None  # 新登录用户，可选
```
#### 2. 实现批量复制工具函数
在 `utils/ui_cases_utils.py` 的 `batch_update_case_field` 函数后添加：

```
def batch_copy_case(case_id: str, project_name: str, username: str, copy_data: dict):
    """
    复制单个用例
    
    Args:
        case_id: 源用例ID
        project_name: 项目名称
        username: 用户名
        copy_data: 复制配置，包含 name_suffix 和可选的字段覆盖值
        
    Returns:
        tuple: (success, message, new_case_id)
    """
    # 1. 查询原用例信息
    # 2. 复制所有字段
    # 3. 修改用例名称（添加后缀）
    # 4. 覆盖用户指定的字段
    # 5. 重置 _id、creator、updator、create_time、update_time
    # 6. 创建新用例
```
#### 3. 实现批量复制 API 路由
在 `case_api.py` 的 `batch_delete_cases` 函数后添加：

```
@router.post(
    "/ui/api/v1/cases-batch-copy",
    name="batch-copy-cases",
    summary="批量复制用例",
    response_model=BaseResponse,
    response_description="批量复制结果"
)
def batch_copy_cases(
    request: BatchCopyRequest,
    x_testmate_username: Optional[str] = Header(None, alias="X-Testmate-Username"),
    x_project_name: str = Header(..., alias="X-Project-Name"),
):
    """
    批量复制用例，支持批量修改指定字段
    
    核心逻辑：
    1. 验证 name_suffix 不能为空
    2. 验证至少有一个字段被修改（group_id/priority/tags/status/login_user）
    3. 遍历用例列表，调用 batch_copy_case 复制每个用例
    4. 返回成功和失败的统计信息
    """
```
### 二、前端实现（ai-assistant-web/components/case-management/case-list.tsx）
#### 1. 添加批量复制状态
在现有状态定义区域（约第145行）添加：

```
const [showBatchCopyModal, setShowBatchCopyModal] = useState(false)
const [batchCopyForm] = Form.useForm()
```
#### 2. 在批量操作菜单中添加复制选项
在 `batchOperationMenuItems` 数组（约第652-719行）的 `divider` 之前添加：

```
{
  key: 'copy',
  label: '批量复制',
  icon: <CopyOutlined />,
  onClick: () => {
    if (selectedRowKeys.length === 0) {
      message.warning('请先选择要复制的用例')
      return
    }
    setShowBatchCopyModal(true)
    batchCopyForm.resetFields()
  }
}
```
#### 3. 实现批量复制表单验证器
在 `handleBatchDelete` 函数后添加：

```
// 批量复制处理函数
const handleBatchCopy = async () => {
  try {
    const values = await batchCopyForm.validateFields()
    
    // 验证至少修改了一项
    const hasChanges = values.groupId || values.priority || 
                      (values.tags && values.tags.length > 0) || 
                      values.status || values.login_user
    
    if (!hasChanges) {
      message.error('请至少修改一项字段')
      return
    }
    
    const response = await fetch('/ui/api/v1/cases-batch-copy', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Project-Name': projectName || '',
        'X-Testmate-Username': username || ''
      },
      body: JSON.stringify({
        case_ids: selectedRowKeys,
        name_suffix: values.nameSuffix,
        group_id: values.groupId,
        priority: values.priority,
        tags: values.tags,
        status: values.status,
        login_user: values.login_user
      })
    })
    
    const data = await response.json()
    if (data.code === 0) {
      message.success(`批量复制完成: 成功${data.data.success_count}个，失败${data.data.failed_count}个`)
      setShowBatchCopyModal(false)
      batchCopyForm.resetFields()
      setSelectedRowKeys([])
      fetchCases()
    } else {
      message.error(data.message || '批量复制失败')
    }
  } catch (error) {
    message.error('批量复制失败')
  }
}
```
#### 4. 添加批量复制 Modal
在批量更新 Modal（约第1836行）之后添加：

```
{/* 批量复制弹框 */}
<Modal
  title="批量复制用例"
  open={showBatchCopyModal}
  onOk={handleBatchCopy}
  onCancel={() => {
    setShowBatchCopyModal(false)
    batchCopyForm.resetFields()
  }}
  width={600}
>
  <div className="mb-4 text-gray-600">
    已选择 {selectedRowKeys.length} 个用例进行批量复制
  </div>
  
  <Form
    form={batchCopyForm}
    layout="vertical"
  >
    <Form.Item
      name="nameSuffix"
      label="用例名称后缀"
      rules={[{ required: true, message: '请输入用例名称后缀' }]}
    >
      <Input placeholder="请输入用例名称后缀（例如：_副本）" allowClear />
    </Form.Item>
    
    <div className="mb-2 text-gray-500 text-sm">
      以下字段可选，至少需要修改一项：
    </div>
    
    <Form.Item
      name="groupId"
      label="所属分组"
    >
      <TreeSelect
        treeData={groups}
        placeholder="请选择所属分组（不选则保持原样）"
        treeDefaultExpandAll
        allowClear
      />
    </Form.Item>
    
    <Form.Item
      name="priority"
      label="优先级"
    >
      <Select placeholder="请选择优先级（不选则保持原样）" allowClear>
        <Select.Option value="P0">P0</Select.Option>
        <Select.Option value="P1">P1</Select.Option>
        <Select.Option value="P2">P2</Select.Option>
        <Select.Option value="P3">P3</Select.Option>
      </Select>
    </Form.Item>
    
    <Form.Item
      name="tags"
      label="标签"
    >
      <Select
        mode="multiple"
        placeholder="请选择标签（不选则保持原样）"
        allowClear
        options={allTags.map(tag => ({ label: tag.tag_name, value: tag._id }))}
      />
    </Form.Item>
    
    <Form.Item
      name="status"
      label="状态"
    >
      <Select placeholder="请选择状态（不选则保持原样）" allowClear>
        <Select.Option value="enabled">启用</Select.Option>
        <Select.Option value="disabled">禁用</Select.Option>
      </Select>
    </Form.Item>
    
    <Form.Item
      name="login_user"
      label="登录用户"
    >
      <Input placeholder="请输入登录用户（不填则保持原样）" allowClear />
    </Form.Item>
  </Form>
</Modal>
```
#### 5. 获取分组树数据
需要添加分组数据的获取逻辑（如果尚未实现），在 `useEffect` 中添加：

```
const [groups, setGroups] = useState([])

useEffect(() => {
  fetchGroups()
}, [projectName])

const fetchGroups = async () => {
  try {
    const response = await fetch('/ui/api/v1/groups', {
      headers: {
        'X-Project-Name': projectName || '',
        'X-Testmate-Username': username || ''
      }
    })
    const data = await response.json()
    if (data.code === 0) {
      // 转换为TreeSelect所需格式
      setGroups(convertGroupsToTree(data.data))
    }
  } catch (error) {
    console.error('获取分组列表失败:', error)
  }
}
```
## 关键实现细节
1. **后端复制逻辑**：保留所有字段（code、browser、env_id、runtime_config、icafe_cards、source_task_id、source_task_type），只重置 _id、creator、updator、create_time、update_time
2. **名称处理**：新用例名称 = 原用例名称 + 用户输入的后缀
3. **字段覆盖**：用户在 Modal 中选择的字段值会覆盖原用例的对应字段值
4. **验证逻辑**：至少修改一项（group_id/priority/tags/status/login_user）才允许提交
5. **iCode 模式**：如果项目使用 iCode 存储，需要在 batch_copy_case 函数中调用 iCode API 创建代码文件
6. **分支处理**：复制时使用当前选中的分支（currentBranch）

诶，我发现提到了一个问题，就是分支的问题，分支这块我之前没有考虑到。

直接复制非 master 的分支会有问题的，提交 iCode 时会出现 master 没有代码的问题，因此，我们需要补充一下需求，要求仅支持在 master 分支的状态下，支持批量复制的能力。

更新 Plan 计划后，可以确认开始启动开发了。

---

这个功能改动不少，也快到中午了，让它自己慢慢实现吧，我先去吃饭了。

---

一次性改动了前端的一个文件、后端的一个 API 文件和一个依赖的 utils 文件。

![](/personal-site-mvp/img/doc-placeholder.svg "")
测试一下，看看，前端的交互没啥问题，也考虑到了非 master 分支的拦截策略等机制。

但是后端好像有点儿问题，针对 iCode 模式的场景，复制后用例代码丢失了，让我们来分析一下，看看原因。

![](/personal-site-mvp/img/doc-placeholder.svg "")
找到问题了，获取原始用例代码的方式是读取了 code 属性，但实际上，针对 iCode 存储时，原始代码不是存在在 code 属性的，需要基于原始用例进行 iCode 对应目录查询才能得到代码。

我们来引导一下:

> 整体测试过程中，发现了一个问题
> 针对 iCode 的存储模式下，当前获取原始用例代码的方式是读取了 code 属性，但实际上，针对 iCode 存储时，原始代码不是存在在 code 属性的，需要基于原始用例进行 iCode 对应目录查询才能得到代码。
> 需要做一些适配改造。
![](/personal-site-mvp/img/doc-placeholder.svg "")
看起来好像正常了，再来验证一下试试。

棒！可以啦~功能验证没问题啦~

可以上线啦~

## 附录:
前端 CR: [评审：baidu-testmate-web-ui-aitester-345 [任务] 【用例管理】批量操作列表加上批量复制到某个分组功能](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/testmate/ai-assistant-web/reviews/118316204/files/base...latest/components/case-management/case-list.tsx?t=mention&mt=doc&dt=sdk)

后端 CR: [评审：baidu-testmate-web-ui-aitester-345 [任务] 【用例管理】批量操作列表加上批量复制到某个分组功能](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/testmate/web-ui-aitester/reviews/118314081/files/base...latest/tester/utils/ui_cases_utils.py?t=mention&mt=doc&dt=sdk)

共计一个 400+ 行代码的变更就这样在几轮对话中完成开发啦~。

# 复盘
## 模式：（好的经验）
1. 先让 Agent 去 Plan，然后再修改代码，往往可以得到更好的结果，同时，也可以帮助我们好全的思考需求；
2. 认真评审 Agent Plan 给出的方案，在方案层面提前发现问题并引导 Agent 修改比代码修改完测试发现成本要低的多；

## 反模式（不要这么做）
1. 不能盲目信任 Coding Agent 修改后的代码，还是需要进行完备的测试验证，否则质量无法得到保证；

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
