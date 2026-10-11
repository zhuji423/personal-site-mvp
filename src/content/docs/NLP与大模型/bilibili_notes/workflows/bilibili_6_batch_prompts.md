---
title: "Bilibili 6-Batch Codex Prompts"
description: "下面 6 段 prompt 可分别复制到 6 个 Codex 会话中执行。每个会话只处理自己那一批 BV，输出目录互不重叠。"
date: "2026-04-21"
category: "NLP与大模型"
source: "D:\\mac_m4\\Agent_learn\\bilibili_notes\\workflows\\bilibili_6_batch_prompts.md"
---
# Bilibili 6-Batch Codex Prompts

下面 6 段 prompt 可分别复制到 6 个 Codex 会话中执行。每个会话只处理自己那一批 BV，输出目录互不重叠。

## Batch 1

```text
使用 bilibili-render-pdf 技能处理下面 5 个 B 站视频：

1. BV1W34y157tA
2. BV1dZ4y1v7U3
3. BV1xT411V7Ng
4. BV1HT41137Zw
5. BV1X94y1R7La

要求：
1. 每个 BV 单独创建输出目录，根目录使用 /Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1。
2. 下载视频封面、音频、可用视频源和关键帧。
3. 如果没有 CC 字幕，必须用 Whisper 生成 transcript.srt，并保留 transcript.srt。
4. 必须阅读 transcript.srt 和关键帧后再写，不允许只按标题或元数据泛泛总结。
5. 每个视频分别生成一份详细中文课程笔记 PDF。
6. PDF 必须包含首页封面、正文关键帧、每张关键帧的时间脚注、课程总结与延伸。
7. 课程笔记必须按教学逻辑重构内容，不要逐句转录，也不要只做摘要。
8. 每个视频至少包含：课程导读、核心概念拆解、关键公式/代码/机制解释、关键画面解析、总结与延伸。
9. 每个视频必须编译成功，输出 note.tex、note.pdf、cover.jpg、transcript.srt、figures 或 frames。
10. 最后给出 5 个视频的输出路径、PDF 编译结果和任何失败/降级说明。
```

## Batch 2

```text
使用 bilibili-render-pdf 技能处理下面 5 个 B 站视频：

1. BV1sv4y1M7aw
2. BV1Qa411D7vZ
3. BV14B4y1x79R
4. BV1pe411g7NX
5. BV1VW4y1b79x

要求：
1. 每个 BV 单独创建输出目录，根目录使用 /Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_2。
2. 下载视频封面、音频、可用视频源和关键帧。
3. 如果没有 CC 字幕，必须用 Whisper 生成 transcript.srt，并保留 transcript.srt。
4. 必须阅读 transcript.srt 和关键帧后再写，不允许只按标题或元数据泛泛总结。
5. 每个视频分别生成一份详细中文课程笔记 PDF。
6. PDF 必须包含首页封面、正文关键帧、每张关键帧的时间脚注、课程总结与延伸。
7. 课程笔记必须按教学逻辑重构内容，不要逐句转录，也不要只做摘要。
8. 每个视频至少包含：课程导读、核心概念拆解、关键公式/代码/机制解释、关键画面解析、总结与延伸。
9. 每个视频必须编译成功，输出 note.tex、note.pdf、cover.jpg、transcript.srt、figures 或 frames。
10. 最后给出 5 个视频的输出路径、PDF 编译结果和任何失败/降级说明。
```

## Batch 3

```text
使用 bilibili-render-pdf 技能处理下面 5 个 B 站视频：

1. BV1AG4y1H7wq
2. BV1Je4y1e7uF
3. BV1tM411L7HE
4. BV14s4y127kk
5. BV14V4y1f7L2

要求：
1. 每个 BV 单独创建输出目录，根目录使用 /Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_3。
2. 下载视频封面、音频、可用视频源和关键帧。
3. 如果没有 CC 字幕，必须用 Whisper 生成 transcript.srt，并保留 transcript.srt。
4. 必须阅读 transcript.srt 和关键帧后再写，不允许只按标题或元数据泛泛总结。
5. 每个视频分别生成一份详细中文课程笔记 PDF。
6. PDF 必须包含首页封面、正文关键帧、每张关键帧的时间脚注、课程总结与延伸。
7. 课程笔记必须按教学逻辑重构内容，不要逐句转录，也不要只做摘要。
8. 每个视频至少包含：课程导读、核心概念拆解、关键公式/代码/机制解释、关键画面解析、总结与延伸。
9. 每个视频必须编译成功，输出 note.tex、note.pdf、cover.jpg、transcript.srt、figures 或 frames。
10. 最后给出 5 个视频的输出路径、PDF 编译结果和任何失败/降级说明。
```

## Batch 4

```text
使用 bilibili-render-pdf 技能处理下面 5 个 B 站视频：

1. BV1XX4y1B71n
2. BV1Ch4y1n7jZ
3. BV1hL41187Pw
4. BV1aa4y1G7p9
5. BV1Ho4y1x76q

要求：
1. 每个 BV 单独创建输出目录，根目录使用 /Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_4。
2. 下载视频封面、音频、可用视频源和关键帧。
3. 如果没有 CC 字幕，必须用 Whisper 生成 transcript.srt，并保留 transcript.srt。
4. 必须阅读 transcript.srt 和关键帧后再写，不允许只按标题或元数据泛泛总结。
5. 每个视频分别生成一份详细中文课程笔记 PDF。
6. PDF 必须包含首页封面、正文关键帧、每张关键帧的时间脚注、课程总结与延伸。
7. 课程笔记必须按教学逻辑重构内容，不要逐句转录，也不要只做摘要。
8. 每个视频至少包含：课程导读、核心概念拆解、关键公式/代码/机制解释、关键画面解析、总结与延伸。
9. 每个视频必须编译成功，输出 note.tex、note.pdf、cover.jpg、transcript.srt、figures 或 frames。
10. 最后给出 5 个视频的输出路径、PDF 编译结果和任何失败/降级说明。
```

## Batch 5

```text
使用 bilibili-render-pdf 技能处理下面 5 个 B 站视频：

1. BV1Lh4y1b74i
2. BV1Do4y1A7EN
3. BV16V4y18733
4. BV1KN411p73o
5. BV1ec411971a

要求：
1. 每个 BV 单独创建输出目录，根目录使用 /Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_5。
2. 下载视频封面、音频、可用视频源和关键帧。
3. 如果没有 CC 字幕，必须用 Whisper 生成 transcript.srt，并保留 transcript.srt。
4. 必须阅读 transcript.srt 和关键帧后再写，不允许只按标题或元数据泛泛总结。
5. 每个视频分别生成一份详细中文课程笔记 PDF。
6. PDF 必须包含首页封面、正文关键帧、每张关键帧的时间脚注、课程总结与延伸。
7. 课程笔记必须按教学逻辑重构内容，不要逐句转录，也不要只做摘要。
8. 每个视频至少包含：课程导读、核心概念拆解、关键公式/代码/机制解释、关键画面解析、总结与延伸。
9. 每个视频必须编译成功，输出 note.tex、note.pdf、cover.jpg、transcript.srt、figures 或 frames。
10. 最后给出 5 个视频的输出路径、PDF 编译结果和任何失败/降级说明。
```

## Batch 6

```text
使用 bilibili-render-pdf 技能处理下面 5 个 B 站视频：

1. BV1sK421C7oG
2. BV1S6421u7jA
3. BV1ZA4m1w7D5
4. BV1ox4y147o1
5. BV1Vt3QzLEQ1

要求：
1. 每个 BV 单独创建输出目录，根目录使用 /Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_6。
2. 下载视频封面、音频、可用视频源和关键帧。
3. 如果没有 CC 字幕，必须用 Whisper 生成 transcript.srt，并保留 transcript.srt。
4. 必须阅读 transcript.srt 和关键帧后再写，不允许只按标题或元数据泛泛总结。
5. 每个视频分别生成一份详细中文课程笔记 PDF。
6. PDF 必须包含首页封面、正文关键帧、每张关键帧的时间脚注、课程总结与延伸。
7. 课程笔记必须按教学逻辑重构内容，不要逐句转录，也不要只做摘要。
8. 每个视频至少包含：课程导读、核心概念拆解、关键公式/代码/机制解释、关键画面解析、总结与延伸。
9. 每个视频必须编译成功，输出 note.tex、note.pdf、cover.jpg、transcript.srt、figures 或 frames。
10. 最后给出 5 个视频的输出路径、PDF 编译结果和任何失败/降级说明。
```
