---
title: "Bilibili Notes Workspace"
description: "这个目录按用途重新整理为以下几类。"
date: "2026-04-21"
category: "工具与环境"
source: "D:\\mac_m4\\Agent_learn\\bilibili_notes\\README.md"
---
# Bilibili Notes Workspace

这个目录按用途重新整理为以下几类。

## final_outputs

最终交付成果。

- `bert_t5_gpt_whisper/`: 30 个 BV 视频的 Whisper 字幕、关键帧、LaTeX 和 PDF 成果。
- `bert_t5_gpt_whisper/pdf_index.txt`: 30 个 PDF 的索引清单。
- `bert_t5_gpt_whisper/final_validation.json`: 最终验收结果。

## workflows

可复用脚本和批处理提示词。

- `bilibili_6_batch_prompts.md`: 6 批 Codex prompt，每批 5 个 BV。
- `prepare_whisper_assets.py`: 下载音视频、Whisper 转录、抽关键帧。
- `repair_failed_assets.py`: 对无 DASH 流的视频做 durl 回退修复。
- `generate_notes_from_whisper_assets.py`: 基于 Whisper 资产生成 LaTeX/PDF 的脚本。
- `batch_generate_bilibili_pdfs.py`: 早期批量生成脚本，保留作参考。

## experiments

历史实验和早期输出，保留用于对比或复查。

- `bert_t5_gpt_batch/`: 早期基于元数据的低质量批量 PDF。
- `BV15HXCBkEKY/`: 单视频测试目录。
- `BV1t4WGzdEJo/`: 单视频测试目录。

## cache

临时探测、benchmark、下载缓存。

- `_bench_whisper/`: Whisper 性能基准测试文件。
- `_probe/`: Bilibili/yt-dlp 探测目录。
- `_probe_a.m4s`, `_probe_v.m4s`: 探测用音视频片段。

## logs

编译器或环境测试日志。

- `_tectonic_test.*`: Tectonic/LaTeX 环境测试产物。

