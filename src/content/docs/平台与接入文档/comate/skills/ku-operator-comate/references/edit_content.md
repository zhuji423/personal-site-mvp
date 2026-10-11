---
title: "edit-content — 编辑文档正文"
description: "通过 JSON 操作列表编辑文档正文内容。支持追加、插入、替换、删除等操作。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\edit_content.md"
---
# edit-content — 编辑文档正文

通过 JSON 操作列表编辑文档正文内容。支持追加、插入、替换、删除等操作。

## CLI 用法

```bash
python3 scripts/ku_operator.py edit-content --doc-id <文档ID> --operations-file <JSON文件> [--publish]
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--operations-file` | 是 | JSON 文件路径，包含编辑操作列表（数组格式） |
| `--publish` | 否 | 编辑后同步发布。不传则仅在编辑态产生变更，预览态不可见 |

## 核心概念

### operations 数组

operations 是一个操作列表，每个操作依次执行：

```json
[
  { "mode": "...", "blockId": "...", "json": [...], "position": 1 },
  { "mode": "...", "blockId": "...", "json": [...] }
]
```

### mode — 操作模式

| mode | 功能 | blockId 是否必填 | 说明 |
|------|------|-----------------|------|
| `sibling` | 插入节点 | 否 | 不传 blockId 时追加到文档末尾；传 blockId 时在目标节点前后插入（由 position 决定） |
| `delete` | 删除节点 | **是** | 删除 blockId 指定的节点。json 字段传空数组 `[]` |

### position — 插入位置（仅 sibling 模式）

| 值 | 含义 |
|----|------|
| `-1` | 在目标节点**上方**插入 |
| `1` | 在目标节点**下方**插入（默认） |
| 不传 | 如果也不传 blockId，则追加到文档末尾 |

### blockId — 如何获取

通过 `query-content` 命令获取文档的原始 JSON 结构（非 Markdown），每个内容块都有 `blockId` 字段，格式为 `docyg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`。

**重要**：要获取 blockId，需要直接查看 queryContent API 返回的原始 JSON 中的 content 数组，而不是 jsonToMd 转换后的 Markdown。

### json — 编辑器节点格式

json 字段是一个节点数组，每个节点代表一个文档内容块。所有节点都需要 `type` 和 `children` 字段。

## Agent 常用节点类型速查

### 段落（paragraph）

```json
{
  "type": "paragraph",
  "children": [{"text": "普通文本内容"}]
}
```

带样式的文本：

```json
{
  "type": "paragraph",
  "children": [
    {"text": "普通文本"},
    {"text": "加粗", "bold": true},
    {"text": "斜体", "italic": true},
    {"text": "删除线", "del": true},
    {"text": "下划线", "underline": true},
    {"text": "红色文字", "font-color": "#E61300"},
    {"text": "高亮背景", "bg-color": "#51C56F"}
  ]
}
```

### 标题（heading）

```json
{
  "type": "heading",
  "level": 2,
  "children": [{"text": "二级标题"}]
}
```

level 取值 1-6，对应 H1-H6。

### 无序列表（unordered-list-item）

```json
{
  "type": "unordered-list-item",
  "depth": 0,
  "children": [{"text": "列表项"}]
}
```

depth 控制缩进层级：0=一级, 1=二级, 2=三级。

### 有序列表（ordered-list-item）

```json
{
  "type": "ordered-list-item",
  "depth": 0,
  "index": 1,
  "initialNumber": 1,
  "children": [{"text": "第一项"}]
}
```

注意：`initialNumber` 只需在同层级列表的第一个元素中指定。

### 待办列表（todo-list-item）

```json
{
  "type": "todo-list-item",
  "depth": 0,
  "checked": false,
  "children": [{"text": "待办事项"}]
}
```

### 代码块（block-code）

```json
{
  "type": "block-code",
  "language": "python",
  "autowrap": true,
  "children": [
    {"type": "block-code-line", "children": [{"text": "def hello():"}]},
    {"type": "block-code-line", "children": [{"text": "    print('hello')"}]}
  ]
}
```

每一行代码是一个 `block-code-line` 子节点。

### 表格（table）

```json
{
  "type": "table",
  "data": {"headless": true, "width": [150, 150, 150]},
  "children": [
    {
      "type": "table-row",
      "children": [
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "单元格1"}]}
          ]
        },
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "单元格2"}]}
          ]
        },
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "单元格3"}]}
          ]
        }
      ]
    }
  ]
}
```

`data.width` 数组长度 = 列数。`headless: true` 表示无表头样式。

### 引用块（blockquote）

```json
{
  "type": "blockquote",
  "children": [
    {"type": "paragraph", "children": [{"text": "引用内容"}]}
  ]
}
```

### 高亮信息块（callout）

```json
{
  "type": "callout",
  "theme": "info",
  "children": [
    {"type": "paragraph", "children": [{"text": "提示信息"}]}
  ]
}
```

theme 可选值：`info` / `warning` / `success` / `error`

### 分割线（hr）

```json
{
  "type": "hr",
  "children": [{"text": ""}]
}
```

### 超链接（内嵌在段落 children 中）

```json
{
  "type": "paragraph",
  "children": [
    {"text": "请访问 "},
    {
      "type": "link",
      "href": "https://baidu.com",
      "title": "百度",
      "children": [{"text": "百度"}]
    },
    {"text": " 了解更多"}
  ]
}
```

## 使用示例

### 1. 追加内容到文档末尾（最常用）

```bash
cat > /tmp/ops.json << 'EOF'
[
  {
    "mode": "sibling",
    "json": [
      {"type": "heading", "level": 2, "children": [{"text": "新章节"}]},
      {"type": "paragraph", "children": [{"text": "这是新增的内容。"}]},
      {
        "type": "unordered-list-item", "depth": 0,
        "children": [{"text": "要点一"}]
      },
      {
        "type": "unordered-list-item", "depth": 0,
        "children": [{"text": "要点二"}]
      }
    ]
  }
]
EOF

python3 scripts/ku_operator.py edit-content \
  --doc-id D5JiZRULjdEJHR \
  --operations-file /tmp/ops.json \
  --publish
```

### 2. 在指定位置插入内容

先通过 queryContent 获取目标节点的 blockId，然后在其下方插入：

```bash
cat > /tmp/ops.json << 'EOF'
[
  {
    "mode": "sibling",
    "blockId": "docyg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "position": 1,
    "json": [
      {"type": "paragraph", "children": [{"text": "插入到目标节点下方的内容"}]}
    ]
  }
]
EOF

python3 scripts/ku_operator.py edit-content \
  --doc-id D5JiZRULjdEJHR \
  --operations-file /tmp/ops.json \
  --publish
```

### 3. 删除指定节点

```bash
cat > /tmp/ops.json << 'EOF'
[
  {
    "mode": "delete",
    "blockId": "docyg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "json": []
  }
]
EOF

python3 scripts/ku_operator.py edit-content \
  --doc-id D5JiZRULjdEJHR \
  --operations-file /tmp/ops.json \
  --publish
```

### 4. 替换内容（先删后插）

编辑器没有原生的「替换」模式，需通过组合操作实现：先在目标节点上方插入新内容，再删除旧节点。

```bash
cat > /tmp/ops.json << 'EOF'
[
  {
    "mode": "sibling",
    "blockId": "docyg-旧节点ID",
    "position": -1,
    "json": [
      {"type": "paragraph", "children": [{"text": "替换后的新内容"}]}
    ]
  },
  {
    "mode": "delete",
    "blockId": "docyg-旧节点ID",
    "json": []
  }
]
EOF

python3 scripts/ku_operator.py edit-content \
  --doc-id D5JiZRULjdEJHR \
  --operations-file /tmp/ops.json \
  --publish
```

### 5. 批量操作（一次请求多个操作）

```bash
cat > /tmp/ops.json << 'EOF'
[
  {
    "mode": "sibling",
    "json": [
      {"type": "heading", "level": 2, "children": [{"text": "测试结果"}]},
      {
        "type": "table",
        "data": {"headless": true, "width": [100, 200, 100]},
        "children": [
          {
            "type": "table-row",
            "children": [
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "用例"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "描述"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "状态"}]}]}
            ]
          },
          {
            "type": "table-row",
            "children": [
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "TC-001"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "登录功能"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "通过", "font-color": "#00B341"}]}]}
            ]
          }
        ]
      }
    ]
  }
]
EOF

python3 scripts/ku_operator.py edit-content \
  --doc-id D5JiZRULjdEJHR \
  --operations-file /tmp/ops.json \
  --publish
```

## 输出说明

返回 JSON，成功时包含每个操作的结果：

```json
{
  "returnCode": 200,
  "result": {
    "docGuid": "D5JiZRULjdEJHR",
    "success": true,
    "operations": [
      {"success": true},
      {"success": true}
    ]
  }
}
```

## 注意事项

- **必须传 `--publish`**：不传 `--publish` 时编辑仅在编辑态可见，预览态/只读态看不到变更
- **operations 中的操作按顺序执行**：前面操作可能影响后续操作（如删除节点后其 blockId 失效）
- **替换操作**：没有原生 replace mode，用「sibling 插入 + delete 删除」组合实现
- **大内容拆分**：如果内容非常多，建议拆分为多次调用，避免网关超时（504）
- **json 中的 blockId 可省略**：新插入的节点不需要提供 blockId，编辑器会自动生成

## 表格编辑指南

### 表格是原子性 block

表格在编辑器中是一个完整的 block，**不支持**单独增删行/列。要修改表格内容，必须**替换整个表格 block**。

### 替换表格的正确做法（重要）

替换表格时，**必须拆成两次独立的 API 调用**。将 delete 和 sibling 放在同一个 operations 数组中会导致 API 返回 success 但表格无实际变化（静默失败）。

**正确步骤：**

**第 1 步：删除旧表格**

```bash
cat > /tmp/delete_table.json << 'EOF'
[
  {
    "mode": "delete",
    "blockId": "docyg-旧表格的blockId",
    "json": []
  }
]
EOF

python3 scripts/ku_operator.py edit-content \
  --doc-id <文档ID> \
  --operations-file /tmp/delete_table.json \
  --publish
```

**第 2 步：插入新表格**

在旧表格的**相邻 block** 下方插入新表格（使用 position: 1）：

```bash
cat > /tmp/insert_table.json << 'EOF'
[
  {
    "mode": "sibling",
    "blockId": "docyg-旧表格前一个block的blockId",
    "position": 1,
    "json": [
      {
        "type": "table",
        "data": {"headless": true, "width": [150, 150, 150]},
        "children": [
          {
            "type": "table-row",
            "children": [
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "列1"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "列2"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "列3"}]}]}
            ]
          },
          {
            "type": "table-row",
            "children": [
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "数据1"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "数据2"}]}]},
              {"type": "table-cell", "data": {"rowspan": 1, "colspan": 1}, "children": [{"type": "paragraph", "children": [{"text": "数据3"}]}]}
            ]
          }
        ]
      }
    ]
  }
]
EOF

python3 scripts/ku_operator.py edit-content \
  --doc-id <文档ID> \
  --operations-file /tmp/insert_table.json \
  --publish
```

### 获取 blockId 的方法

使用 `query-content --raw-json` 获取文档原始 JSON 结构，其中每个 block 都包含 `blockId` 字段：

```bash
python3 scripts/ku_operator.py query-content --doc-id <文档ID> --raw-json
```

输出中找到目标表格的 `blockId`（格式如 `docyg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`），以及其前一个 block 的 `blockId`（用于第 2 步定位插入位置）。

### 表格 JSON 结构模板

```json
{
  "type": "table",
  "data": {
    "headless": true,
    "width": [150, 200, 150]
  },
  "children": [
    {
      "type": "table-row",
      "children": [
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "表头1"}]}
          ]
        },
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "表头2"}]}
          ]
        },
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "表头3"}]}
          ]
        }
      ]
    },
    {
      "type": "table-row",
      "children": [
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "值1"}]}
          ]
        },
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "值2"}]}
          ]
        },
        {
          "type": "table-cell",
          "data": {"rowspan": 1, "colspan": 1},
          "children": [
            {"type": "paragraph", "children": [{"text": "值3"}]}
          ]
        }
      ]
    }
  ]
}
```

**关键字段说明：**
- `data.width`：数组长度 = 列数，每个值为列宽（像素）
- `data.headless`：`true` 表示无表头样式区分
- 每个 `table-cell` 内的 `children` 必须包含至少一个 `paragraph` 节点
- `rowspan` / `colspan` 用于合并单元格
