---
title: "Bilibili Notes Batch Workflow"
description: "User-specific Bilibili lecture-to-PDF batch workflow for Agent_learn/bilibili_notes; use for BV collections, Whisper-first notes, keyframes, and per-video PDF artifacts."
date: "2026-04-23"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\skills\\bilibili-notes-batch\\SKILL.md"
name: "bilibili-notes-batch"
argument-hint: "[bilibili-url-or-bv-list] [output-root]"
user-invocable: "false"
---

# Bilibili Notes Batch Workflow

## When To Use

Use this when the user asks to turn Bilibili videos or a Bilibili collection into detailed Chinese course-note PDFs under `/Users/zhuji_m4pro/Agent_learn/bilibili_notes`.

Non-goals:
- Do not use this for a metadata-only summary.
- Do not claim completion without verifying media, transcript, frames, TeX, and PDF artifacts.
- Do not reuse stale frames when the user says "视频需要下载，关键帧需要重新抽取".

## Inputs And Context

Gather first:
1. BV IDs or Bilibili URL.
2. Output root, usually under `/Users/zhuji_m4pro/Agent_learn/bilibili_notes`.
3. Whether this is a collection/season task or a fixed BV list.
4. Current tool availability: DNS/network to Bilibili, `ffmpeg`, `yt-dlp`, `faster_whisper` or Whisper, and a PDF engine such as `tectonic`, `xelatex`, or `pdflatex`.
5. Whether authenticated Bilibili access is needed. If the user supplied cookies/headers or previous runs hit HTTP 412, prepare `BILI_COOKIE` or a cookie file before the main run.
6. Whether the chosen Whisper path can actually download/load its model in the current TLS environment.

## Procedure

1. For a single BV that may have "下面所有的分p视频", query Bilibili metadata and check both `data.pages` and `data.ugc_season.sections[].episodes`.
2. Preflight blockers before the full batch: verify Bilibili access with `yt-dlp -J` on one BV and verify the chosen Whisper path can load/download its model without TLS failures.
3. If Bilibili access needs auth, run through `BILI_COOKIE` or a browser-cookie file from the start instead of waiting for an HTTP 412 failure mid-run.
4. Create one output directory per BV. Do not merge several videos into one artifact folder.
5. Download `cover.jpg`, audio, a usable video source, and keyframes for each BV.
6. If CC subtitles are absent or inadequate, generate `transcript.srt` with Whisper and keep the `.srt` artifact.
7. Read `transcript.srt` and keyframes before writing. The user explicitly rejected notes written only from title or metadata.
8. Write `note.tex` as a detailed Chinese course note organized by teaching logic, not a line-by-line transcript.
9. Include cover page, body keyframes, timestamp footnotes for every frame, course summary, and extension/discussion.
10. Compile `note.pdf` and preserve compile logs.
11. Final report must include each video's output path, PDF compile result, and any failure/degradation notes.

## Efficiency Plan

- For a 30-video collection, split into six batches of five BV IDs and isolate outputs as `quality_batch_1` through `quality_batch_6` or similar.
- Keep scripts/prompts in `bilibili_notes/workflows/`, final deliverables in `bilibili_notes/final_outputs/`, experiments in `bilibili_notes/experiments/`, probes in `bilibili_notes/cache/`, and compile tests in `bilibili_notes/logs/`.
- If a previous run was interrupted, inspect existing per-BV directories before redownloading.
- Keep per-BV processing restartable. One transcription/download failure should not stop the remaining BV IDs.
- Stop early and report blockers if DNS/network to Bilibili or the PDF engine is missing.

## Pitfalls And Fixes

- Symptom: user says "太敷衍了" or PDFs have no images/audio-derived text. Cause: metadata-only generation. Fix: redo Whisper-first with keyframes and transcript-grounded writing.
- Symptom: direct `yt-dlp` Bilibili webpage access hits HTTP 412. Fix: use Bilibili API/playurl requests with browser headers; if DASH is missing, retry with `durl`.
- Symptom: authenticated `yt-dlp` still is not configured and the user already supplied cookie/header material. Cause: the pipeline ignored available credentials. Fix: wire `BILI_COOKIE` or a cookie file into every `yt-dlp` call before the main batch.
- Symptom: Whisper fails with `ssl.SSLCertVerificationError` / `CERTIFICATE_VERIFY_FAILED` while downloading model weights. Cause: TLS chain/model-fetch problem. Fix: pre-download the model or solve TLS trust before promising the batch.
- Symptom: `Could not resolve host: www.bilibili.com` or `Failed to resolve 'www.bilibili.com'`. Cause: shell DNS/network blocked. Fix: do not keep retrying; ask for environment change or local source files.
- Symptom: no `pdflatex`, `xelatex`, `lualatex`, or `tectonic`. Cause: no usable PDF toolchain. Fix: install/enable a PDF engine before promising final PDFs.

## Verification Checklist

- One BV preflight succeeded for both `yt-dlp -J` access and Whisper model loading/download.
- Per BV: `cover.jpg`, media/audio source, `transcript.srt`, frames or figures, `note.tex`, `note.pdf`, and compile log exist.
- Notes are grounded in transcript and frames, not title/metadata alone.
- PDF includes cover, embedded keyframes, timestamp footnotes, summary, and extension/discussion.
- Final report lists output paths, compile status, and failures/degradations.
