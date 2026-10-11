---
title: "tests/test_bag_extractor.py"
description: "AI 时代高效开发习惯-数据流编程"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI 时代高效开发习惯-数据流编程.md"
---
AI 时代高效开发习惯-数据流编程

#### 🧑‍🏫 案例作者：[@李伟康](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、测试、研发全流程
#### 🔧 使用工具：Comate、OpenClaw
#### 📒 案例概要：从0-1开发项目按照这三步稳定性可以增加  1. protobuf锚定点数据约定;  2. 约定数据流变化文档;  3. 锚定点测试。可以极大程度提高项目开发的稳定性
> 数据结构 · 方法沟通 · 及时文档
> 当技术不再是门槛，AI时代编程核心：数据结构约定 - 数据流如何变化（文档规范约定）- benchmark关键点校验。
>                                                           -- code is cheap, show me your doc !
---

## 核心理念
在 AI 协同开发的时代，**代码本身变得廉价，但数据的契约变得昂贵**。

与 AI 协作的关键不在于你写代码的速度，而在于遵循一个约定可追溯的三步流程：

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   1. 定义结构    │ ──→ │   2. 校验转换     │ ──→ │   3. 测试验证    │
│   (Protobuf)    │     │   (文档评审)      │    │   (Benchmark)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```
**在正式编码前，完成前两步。在提交代码前，完成第三步。**

---

## 通用方法：三步法
### 第一步：定义数据结构
**核心原则：用 Protobuf 明确定义输入、输出、Benchmark**

为什么用 Protobuf？

* **明确** — 字段类型、必填/可选一目了然
* **可验证** — 编译时检查，运行时校验
* **跨语言** — Python/C++/Go 共用同一份定义
* **可扩展** — 向后兼容有明确规则

```
// 1. 输入数据结构
message Input {
  // 明确定义每个字段
}

// 2. 输出数据结构
message Output {
  // 明确定义每个字段
}

// 3. Benchmark 数据结构（测试用例）
message BenchmarkCase {
  Input input = 1;
  Output expected_output = 2;
  string description = 3;
}
```
**与 AI 沟通的正确方式：**

❌ 错误："帮我写个数据转换脚本"
✅ 正确："这是 Input/Output 的 Protobuf 定义，请实现转换逻辑"

---

### 第二步：文档级转换校验
**核心原则：编码前，先写清楚转换逻辑**

这个文档是人与 AI 之间的"合同"，也是后续 Code Review 的依据。

#### 转换校验文档模板
```
## 数据转换校验清单

### 转换：Input → Output

| 步骤 | 输入字段 | 转换逻辑 | 输出字段 | 边界条件 | 验证方式 |
|------|----------|----------|----------|----------|----------|
| 1    | field_a  | 逻辑描述 | field_x  | 空值？   | 单元测试 |
| 2    | field_b  | 逻辑描述 | field_y  | 越界？   | 单元测试 |

### 异常路径
- 输入为空 → 输出是什么？
- 字段缺失 → 报错还是默认值？
- 数据异常 → 如何记录日志？

### Benchmark 覆盖
- [ ] 正常路径
- [ ] 边界条件
- [ ] 异常路径
```
**评审流程：**

1. 编写转换文档
2. 与 AI Review（让 AI 指出遗漏的边界条件）
3. 人工确认
4. 签字（PR approval）
5. 开始编码

**文档没有评审通过之前，不允许写任何业务代码。**

---

### 第三步：关键 Benchmark 处的充分测试
**核心原则：测试用例本身就是文档**

#### 测试覆盖标准
|测试类型|覆盖要求|执行频率|
|-|-|-|
|单元测试|每个转换步骤至少 1 个|每次 commit|
|边界测试|空值、最大值、特殊值|每次 commit|
|异常测试|所有错误路径|每次 commit|
|回归测试|历史 Bug 变 Benchmark|每次 PR|

#### 测试签字清单
```
- [ ] 所有单元测试通过
- [ ] 所有边界条件测试通过
- [ ] 所有异常路径测试通过
- [ ] Benchmark 测试通过（输入→输出断言）

签字：___________ 日期：___________
```
**测试没有全部通过之前，不允许 merge 代码。**

---

## 完整工作流
```
Step 1: 定义数据结构
├─ 编写 proto 文件（输入/输出/Benchmark）
├─ 与 AI Review proto
└─ 提交 proto PR，获得批准

Step 2: 文档级转换校验
├─ 编写转换文档（转换逻辑/边界条件/异常路径）
├─ 与 AI Review 文档
├─ 人工评审，签字确认
└─ 批准后才能编码

Step 3: 编码 + 测试
├─ 让 AI 根据 proto + 转换文档生成代码骨架
├─ 补充业务逻辑
├─ 编写/运行 Benchmark 测试
└─ 所有测试通过后提交 PR
```
**关键原则：前两步不完，不动手写代码。**

---

## 示例：从 Bag 文件抽取训练数据转换为标注格式
下面用一个具体的例子演示三步法的应用。

### 场景描述
写一个脚本，从 ROS bag 文件中抽取传感器数据，转换为训练标注格式（JSON）。

---

### Step 1: 定义数据结构
在所有开始之前，和AI提前约定好输入和输出，以及中间锚定的中间数据的数据结构。一旦约定，不要轻易改动！

```
// proto/bag_extractor.proto
syntax = "proto3";

package data_extractor;

// 输入：Bag 文件信息
message BagInput {
  string bag_path = 1;
  
  // 需要抽取的话题
  repeated string topics = 2;
  
  // 时间范围（纳秒）
  optional int64 start_time_ns = 3;
  optional int64 end_time_ns = 4;
  
  // 抽取频率（Hz），0 表示全量
  float sample_rate_hz = 5;
}

// 输出：标注数据
message AnnotationOutput {
  string frame_id = 1;
  int64 timestamp_ns = 2;
  
  // 传感器数据
  SensorData sensor = 3;
  
  // 标注结果（预留人工标注字段）
  optional Labels labels = 4;
}

message SensorData {
  // 相机数据
  optional Image image = 1;
  
  // 激光雷达数据
  optional PointCloud point_cloud = 2;
  
  // 自车位姿
  optional Pose ego_pose = 3;
}

message Image {
  string camera_name = 1;
  bytes data = 2;  // JPEG 编码
  int32 width = 3;
  int32 height = 4;
  
  // 内参
  CameraIntrinsics intrinsics = 5;
  
  // 外参（相对于自车坐标系）
  Pose extrinsics = 6;
}

message CameraIntrinsics {
  double fx = 1;
  double fy = 2;
  double cx = 3;
  double cy = 4;
  repeated double distortion = 5;
}

message PointCloud {
  string lidar_name = 1;
  repeated Point points = 2;
}

message Point {
  float x = 1;
  float y = 2;
  float z = 3;
  float intensity = 4;
}

message Pose {
  double x = 1;
  double y = 2;
  double z = 3;
  double qx = 4;  // 四元数
  double qy = 5;
  double qz = 6;
  double qw = 7;
}

message Labels {
  repeated Label objects = 1;
}

message Label {
  string id = 1;
  string category = 2;  // car, pedestrian, cyclist...
  
  // 3D 边界框（自车坐标系）
  BoundingBox3D bbox_3d = 3;
  
  // 2D 边界框（图像坐标系，可选）
  optional BoundingBox2D bbox_2d = 4;
  
  float confidence = 5;
}

message BoundingBox3D {
  double x_center = 1;
  double y_center = 2;
  double z_center = 3;
  double length = 4;
  double width = 5;
  double height = 6;
  double yaw = 7;
}

message BoundingBox2D {
  int32 x_min = 1;
  int32 y_min = 2;
  int32 x_max = 3;
  int32 y_max = 4;
}

// Benchmark 测试用例
message ExtractorBenchmarkCase {
  string name = 1;
  string description = 2;
  
  BagInput input = 3;
  
  // 期望的输出帧数
  int32 expected_frame_count = 4;
  
  // 期望的输出文件结构校验
  OutputSchema expected_schema = 5;
}

message OutputSchema {
  repeated string required_fields = 1;
  map<string, FieldType> field_types = 2;
}

enum FieldType {
  FIELD_TYPE_UNSPECIFIED = 0;
  STRING = 1;
  INT64 = 2;
  FLOAT = 3;
  OBJECT = 4;
  ARRAY = 5;
}
```
---

### Step 2: 文档级转换校验
防止事后扯皮事件发生，防止陷入自我怀疑，到底是描述错了还是AI理解错了。

```
## 数据转换校验清单

### 模块：BagExtractor

### 转换：BagInput → AnnotationOutput (JSON)

| 步骤 | 输入字段 | 转换逻辑 | 输出字段 | 边界条件 | 验证方式 |
|------|----------|----------|----------|----------|----------|
| 1    | bag_path | 检查文件存在性 | - | 文件不存在？→ 报错 | 单元测试 |
| 2    | topics   | 订阅指定话题 | - | 话题不存在？→ 警告并跳过 | 单元测试 |
| 3    | start/end_time | 时间范围过滤 | timestamp_ns | 时间戳越界？→ 丢弃 | 单元测试 |
| 4    | sample_rate_hz | 降采样 | - | 0=全量，<0=报错 | 单元测试 |
| 5    | image_msg | 提取图像 + 内参 + 外参 | sensor.image | 消息缺失？→ 字段为空 | 集成测试 |
| 6    | pointcloud_msg | 提取点云 | sensor.point_cloud | 点云为空？→ 空数组 | 集成测试 |
| 7    | pose_msg | 提取位姿 | sensor.ego_pose | 位姿缺失？→ 用上一帧 | 集成测试 |
| 8    | 所有数据 | 序列化为 JSON | 输出文件 | JSON 格式校验 | 端到端测试 |

### 异常路径处理

| 异常场景 | 检测条件 | 响应动作 |
|----------|----------|----------|
| Bag 文件不存在 | path 检查失败 | 抛出 FileNotFoundError |
| 话题不存在 | rosbag 中无此 topic | 记录警告，继续处理其他话题 |
| 消息时间戳乱序 | 当前帧 timestamp < 上一帧 | 记录警告，丢弃该帧 |
| 传感器数据缺失 | 某话题无消息 | 对应字段为 null |
| 外参未标定 | extrinsics 为空 | 使用默认单位矩阵 |

### Benchmark 覆盖清单

#### 正常场景
- [ ] 单话题抽取（仅图像）
- [ ] 多话题同步抽取（图像 + 点云 + 位姿）
- [ ] 时间范围过滤
- [ ] 降采样抽取（10Hz → 5Hz）

#### 边界场景
- [ ] Bag 文件为空
- [ ] 时间范围超出 Bag 范围
- [ ] 消息时间戳不连续
- [ ] 传感器数据部分缺失

#### 异常场景
- [ ] Bag 文件路径不存在
- [ ] 话题名称拼写错误
- [ ] 消息格式损坏
```
---

### Step 3: 编写测试
锚定点测试，人工设置锚定点，让AI对锚定点数据写测试文件。在无法保证代码正确的情况下，保证数据流动结果正确是最大程度保证代码质量的唯一手段，也是定位问题的唯一手段。

```
# tests/test_bag_extractor.py
import pytest
import json
from pathlib import Path
from proto import bag_extractor_pb2
from extractor.bag_extractor import BagExtractor

class TestBagExtractorBenchmark:
    """Bag 抽取器 Benchmark 测试套件"""
    
    @pytest.fixture
    def extractor(self):
        return BagExtractor()
    
    def test_single_topic_image(self, extractor, tmp_path):
        """场景：单话题抽取（仅图像）"""
        # Given
        bag_file = create_test_bag(
            topics=["/camera/front/image_raw"],
            frame_count=100
        )
        
        input = bag_extractor_pb2.BagInput(
            bag_path=str(bag_file),
            topics=["/camera/front/image_raw"],
            sample_rate_hz=0  # 全量
        )
        
        # When
        output_path = tmp_path / "output.jsonl"
        extractor.extract(input, str(output_path))
        
        # Then
        lines = output_path.read_text().strip().split("\n")
        assert len(lines) == 100
        
        # 验证 JSON 格式和字段
        for line in lines:
            frame = json.loads(line)
            assert "frame_id" in frame
            assert "timestamp_ns" in frame
            assert "sensor" in frame
            assert "image" in frame["sensor"]
    
    def test_multi_topic_sync(self, extractor, tmp_path):
        """场景：多话题同步抽取"""
        bag_file = create_test_bag(
            topics=[
                "/camera/front/image_raw",
                "/lidar/points",
                "/vehicle/pose"
            ],
            frame_count=50
        )
        
        input = bag_extractor_pb2.BagInput(
            bag_path=str(bag_file),
            topics=["/camera/front/image_raw", "/lidar/points", "/vehicle/pose"],
            sample_rate_hz=0
        )
        
        output_path = tmp_path / "output.jsonl"
        extractor.extract(input, str(output_path))
        
        lines = output_path.read_text().strip().split("\n")
        assert len(lines) == 50
        
        # 验证所有传感器数据都存在
        frame = json.loads(lines[0])
        assert "image" in frame["sensor"]
        assert "point_cloud" in frame["sensor"]
        assert "ego_pose" in frame["sensor"]
    
    def test_time_range_filter(self, extractor, tmp_path):
        """场景：时间范围过滤"""
        bag_file = create_test_bag(
            topics=["/camera/front/image_raw"],
            frame_count=100,
            duration_sec=10  # 10 秒
        )
        
        input = bag_extractor_pb2.BagInput(
            bag_path=str(bag_file),
            topics=["/camera/front/image_raw"],
            start_time_ns=2_000_000_000,  # 从 2 秒开始
            end_time_ns=5_000_000_000,    # 到 5 秒结束
            sample_rate_hz=0
        )
        
        output_path = tmp_path / "output.jsonl"
        extractor.extract(input, str(output_path))
        
        lines = output_path.read_text().strip().split("\n")
        # 3 秒的数据，假设 10Hz，应该约 30 帧
        assert 25 <= len(lines) <= 35
    
    def test_downsample(self, extractor, tmp_path):
        """场景：降采样抽取"""
        bag_file = create_test_bag(
            topics=["/camera/front/image_raw"],
            frame_count=100,
            original_rate_hz=10
        )
        
        input = bag_extractor_pb2.BagInput(
            bag_path=str(bag_file),
            topics=["/camera/front/image_raw"],
            sample_rate_hz=5  # 降采样到 5Hz
        )
        
        output_path = tmp_path / "output.jsonl"
        extractor.extract(input, str(output_path))
        
        lines = output_path.read_text().strip().split("\n")
        assert len(lines) == 50  # 100 帧降采样到 50 帧
    
    def test_bag_not_found(self, extractor, tmp_path):
        """异常场景：Bag 文件不存在"""
        input = bag_extractor_pb2.BagInput(
            bag_path="/nonexistent/path.bag",
            topics=["/camera/front/image_raw"]
        )
        
        output_path = tmp_path / "output.jsonl"
        
        with pytest.raises(FileNotFoundError):
            extractor.extract(input, str(output_path))
    
    def test_empty_bag(self, extractor, tmp_path):
        """边界场景：空 Bag 文件"""
        bag_file = create_test_bag(
            topics=["/camera/front/image_raw"],
            frame_count=0
        )
        
        input = bag_extractor_pb2.BagInput(
            bag_path=str(bag_file),
            topics=["/camera/front/image_raw"]
        )
        
        output_path = tmp_path / "output.jsonl"
        extractor.extract(input, str(output_path))
        
        lines = output_path.read_text().strip()
        assert lines == ""  # 空输出
    
    def test_schema_validation(self, extractor, tmp_path):
        """验证输出 Schema 符合 Benchmark 定义"""
        bag_file = create_test_bag(
            topics=["/camera/front/image_raw"],
            frame_count=10
        )
        
        input = bag_extractor_pb2.BagInput(
            bag_path=str(bag_file),
            topics=["/camera/front/image_raw"]
        )
        
        output_path = tmp_path / "output.jsonl"
        extractor.extract(input, str(output_path))
        
        # 验证 Schema
        required_fields = ["frame_id", "timestamp_ns", "sensor"]
        for line in output_path.read_text().strip().split("\n"):
            frame = json.loads(line)
            for field in required_fields:
                assert field in frame, f"Missing required field: {field}"
```
---

## AI 协同开发最佳实践
### ✅ 这样做
|场景|做法|
|-|-|
|新脚本开发|Step1 proto → Step2 转换文档 → Step3 AI 生成骨架 → 补充逻辑 → 测试|
|Bug 修复|先写复现的 Benchmark → 定位问题 → 修复 → 回归测试|
|重构|保证 proto 不变 → AI 安全重构 → Benchmark 验证行为一致|
|Code Review|Review proto + 转换文档 + Benchmark，而不是逐行看代码|

### ❌ 避免这样
|反模式|问题|
|-|-|
|"你先写个大概，我再改"|AI 生成大量需要手动修正的代码|
|口头描述需求|AI 误解，反复纠正，沟通成本高|
|事后补文档|文档永远追不上代码|
|隐式数据结构|AI 无法推断，人类也难以维护|
|跳过 Benchmark|行为与预期不符，难以定位|

---

## 工具推荐
### Protobuf 生态
* `protoc` + 语言插件
* `buf` (现代 proto 管理)
* `protolint` (lint)

### 测试框架
* **Python**: pytest, pytest-benchmark
* **C++**: gtest, gbench

---

## 总结
> **AI 时代的开发 = Step1 定义结构 + Step2 校验转换 + Step3 测试验证**
### 三步法核心
|步骤|产出物|评审标准|签字后才能|
|-|-|-|-|
|**Step1**|Protobuf 定义|字段完整、类型正确|开始写转换文档|
|**Step2**|转换文档|逻辑清晰、边界明确|开始写业务代码|
|**Step3**|Benchmark 测试|用例充分、断言准确|提交/merge 代码|

### 记住这句话
> 代码是廉价的，数据契约是昂贵的。
> 在编码前多花 1 小时定义结构和校验转换，能节省后续 10 小时的返工和调试。
---

*最后更新：2026-03-09*

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
