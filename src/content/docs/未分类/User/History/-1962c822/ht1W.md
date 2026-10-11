---
title: "Bilibili 6-Batch Codex Prompts"
description: "下面 6 段 prompt 可分别复制到 6 个 Codex 会话中执行。每个会话只处理自己那一批 BV，输出目录互不重叠。"
date: "2026-04-21"
category: "未分类"
source: "F:\\百度工作\\06_comate_aiide_config\\User\\History\\-1962c822\\ht1W.md"
---
# Bilibili 6-Batch Codex Prompts
cookies buvid3=8F75EDE2-FEB7-B0D1-DD9C-1F98D817C58D98006infoc; b_nut=1754364598; _uuid=C10E1023BC-AAE10-71058-8473-AEDF2104362F798426infoc; buvid_fp=b31c8c3cb7161eaa66a5d6e53c09c144; rpdid=0zbfVCM3B3|dMchYSae|2Xo|3w1UJ8nd; enable_web_push=DISABLE; theme-tip-show=SHOWED; PVID=1; LIVE_BUVID=AUTO2117547456772093; theme-avatar-tip-show=SHOWED; DedeUserID=119092698; DedeUserID__ckMd5=049bbaa57e78cf98; theme-switch-show=SHOWED; theme_style=dark; buvid4=999D7D28-E452-4BCC-B2D2-A8EFA76749FB98869-025080511-JZNVzXE9OuPWTXqIEsjl8kZ0Ven4hjj9xwCqApQu+s6kLJbEbKigzPOBBgVdiQ4N; lang=zh-Hans; share_source_origin=COPY; bsource=search_google; CURRENT_QUALITY=120; home_feed_column=5; browser_resolution=1653-1002; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzY5NDA2OTMsImlhdCI6MTc3NjY4MTQzMywicGx0IjotMX0.LbI2nS2542ZBovgFAZJ3xHsQT9gVsrlE_Ng8M2dYMXU; bili_ticket_expires=1776940633; SESSDATA=e9820809%2C1792233494%2Cf5527%2A42CjDihzz6bAMO2J41hXIh7kT7603G9DBnVO9TfmVfq7HRnQ0B-XF0oTSWpUbCrmLhuCsSVmRWS3hEdkdJd1k1TVRLWUlWOUdZdzM2ZVBEY0VhdXlJMnVNWDdEWkI0dm9pQlVxelk5SnhrT0s3V2paTHJXSHN4c0dPbUtUN2ROSndlZkloMHZsdURRIIEC; bili_jct=568e288532f3e214cccc00981d9e1d75; sid=57a15hlx; bp_t_offset_119092698=1193327148178341888; CURRENT_FNVAL=4048; RT="z=1&dm=bilibili.com&si=b8b172c2-c7bd-4c83-b25c-0194111bad6f&ss=mo8ev6u7&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; b_lsid=FA1EF771_19DB05E1357

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
