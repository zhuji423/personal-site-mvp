---
title: "Batch-rendered Bilibili course notes in `bilibili_notes/quality_batch_1`"
description: "Rollout context: The user wanted the bilibili-render-pdf skill applied to five Bilibili BV videos, with each BV in its o"
date: "2026-05-05"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-22T03-15-34-2q92-bilibili_quality_batch_1_render_pdf.md"
---
thread_id: 019db32f-9b4d-74c1-80ad-3a4bda751e08
updated_at: 2026-04-22T05:49:00+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/22/rollout-2026-04-22T11-15-34-019db32f-9b4d-74c1-80ad-3a4bda751e08.jsonl
cwd: /Users/zhuji_m4pro/Agent_learn

# Batch-rendered Bilibili course notes in `bilibili_notes/quality_batch_1`

Rollout context: The user wanted the `bilibili-render-pdf` skill applied to five Bilibili BV videos, with each BV in its own output directory under `/Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1`, and explicitly required re-downloading video assets, re-extracting keyframes, generating `transcript.srt` via Whisper when CC subtitles were unavailable, and writing detailed Chinese course notes after reading the transcript and frames.

## Task 1: Batch render 5 Bilibili course-note PDFs

Outcome: success

Preference signals:
- The user said “使用 bilibili-render-pdf 技能处理下面 5 个 B 站视频” and specified “每个 BV 单独创建输出目录，根目录使用 /Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1” -> future similar requests should default to per-BV isolated directories rooted in the batch folder.
- The user required “下载视频封面、音频、可用视频源和关键帧” and later emphasized “视频需要下载，关键帧需要重新抽取” -> future similar runs should not rely on existing assets; re-download and re-extract by default.
- The user required “必须阅读 transcript.srt 和关键帧后再写，不允许只按标题或元数据泛泛总结” -> future similar runs should treat transcript+frames as mandatory inputs before writing teaching notes.
- The user asked for “整体的思路，搜索相关的内容进行笔记的整理” in a later follow-up -> for similar tasks, proactively provide a synthesized teaching outline and gather supporting context rather than only transcribing or summarizing.

Key steps:
- Read `bilibili_notes/README.md`, the `bilibili-render-pdf` skill, and batch prompt docs to confirm the workspace structure and expected deliverables.
- Built a reusable batch script (`bilibili_notes/workflows/quality_batch_render.py`) to process the five BV IDs in sequence.
- The first run hit Bilibili `HTTP 412 Precondition Failed` on `yt-dlp -J`, showing that the environment needed authenticated/cookie-backed requests.
- Retried with a `BILI_COOKIE` environment variable populated from the user-provided cookie string; this restored access and allowed the whole batch to complete.
- For each BV, the pipeline downloaded metadata, cover, source video, and audio; fell back to Whisper to produce `transcript.srt`; re-extracted 12 keyframes; generated `note.tex`; and compiled `note.pdf` with Tectonic.

Failures and how to do differently:
- Unauthenticated Bilibili requests failed with `HTTP 412`; future similar work should expect cookie-backed `yt-dlp` requests when Bilibili blocks metadata/video access.
- The first script version had a string-escaping issue around a LaTeX `lstlisting` block; it was fixed before the successful run. For similar generator scripts, prefer raw triple-quoted strings or smaller concatenated segments when embedding LaTeX/verbatim blocks.

Reusable knowledge:
- The repo already has a dedicated Bilibili workspace with `cache/`, `experiments/`, `final_outputs/`, `logs/`, `quality_batch_1/`, and `workflows/`, and the skill docs explicitly treat `bilibili_notes` as the workspace for these PDF notes.
- `faster_whisper`, `ffmpeg`, `yt-dlp`, and `tectonic` were all available in the environment; the batch pipeline could be run entirely locally once Bilibili access was fixed.
- The working batch script writes each episode to `bilibili_notes/quality_batch_1/<BV>/` and records a compact `batch_summary.json` at the batch root.
- Each successful episode directory contained the expected artifacts: `note.tex`, `note.pdf`, `cover.jpg`, `audio.wav`, `transcript.srt`, `frames/frames_manifest.json`, plus logs and downloaded source media.

References:
- [1] `bilibili_notes/workflows/quality_batch_render.py` — reusable batch pipeline script for download/transcribe/frame extraction/LaTeX/PDF compilation.
- [2] First failure evidence: `ERROR: [BiliBili] ... Unable to download webpage: HTTP Error 412: Precondition Failed` from `yt-dlp -J --no-warnings https://www.bilibili.com/video/BV...`.
- [3] Successful batch summary: each of `BV1W34y157tA`, `BV1dZ4y1v7U3`, `BV1xT411V7Ng`, `BV1HT41137Zw`, and `BV1X94y1R7La` reported `downloaded: true`, `subtitle_mode: whisper`, `compiled: true`.
- [4] The batch root summary file: `/Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1/batch_summary.json`.

## Task 2: Resolve Bilibili access and rerun with cookies

Outcome: success

Preference signals:
- The user had already provided a long cookie/header blob together with the Bilibili context -> future similar runs should anticipate that access may require authenticated headers and should be prepared to use them.
- The user repeatedly reinforced the need to download and rebuild assets rather than rely on stale outputs -> future similar runs should treat credentialed re-downloads as the expected path after an access failure.

Key steps:
- Verified that `yt-dlp` could identify the BV with the provided cookie header by running a cookie-backed `yt-dlp -J ... | jq '.id,.title'` check.
- Switched the batch pipeline to read `BILI_COOKIE` from the environment and inject it into all `yt-dlp` calls.
- Re-ran the full batch successfully after the authentication fix.

Failures and how to do differently:
- Passing cookie data as a raw `Cookie:` header is workable but noisy; future similar work may be more stable if credentials are loaded from a browser cookie file or a dedicated env var rather than copy-pasted into commands.

Reusable knowledge:
- Once cookie-backed `yt-dlp` worked, all five videos processed cleanly with Whisper fallback and PDF compilation succeeded.

References:
- [1] Cookie-backed verification command: `yt-dlp -J --no-warnings --add-header "Referer:https://www.bilibili.com" --add-header "Cookie:..." https://www.bilibili.com/video/BV1W34y157tA | jq '.id,.title'` returned the BV ID and title.
- [2] The successful batch run was triggered with `BILI_COOKIE='...' python3 bilibili_notes/workflows/quality_batch_render.py`.
- [3] Final per-video outputs were under:
  - `/Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1/BV1W34y157tA`
  - `/Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1/BV1dZ4y1v7U3`
  - `/Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1/BV1xT411V7Ng`
  - `/Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1/BV1HT41137Zw`
  - `/Users/zhuji_m4pro/Agent_learn/bilibili_notes/quality_batch_1/BV1X94y1R7La`

