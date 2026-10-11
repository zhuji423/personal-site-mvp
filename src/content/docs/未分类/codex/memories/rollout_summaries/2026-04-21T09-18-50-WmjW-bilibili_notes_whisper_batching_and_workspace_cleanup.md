---
title: "User pushed from low-quality metadata-only PDF generation to a Whisper-first, subagent-parallel workflow, then asked to "
description: "Rollout context: working in /Users/zhujim4pro/Agentlearn, mostly under bilibilinotes. The target Bilibili content was th"
date: "2026-05-05"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-21T09-18-50-WmjW-bilibili_notes_whisper_batching_and_workspace_cleanup.md"
---
thread_id: 019daf55-d3e2-7e02-91b9-4bff85d20ccc
updated_at: 2026-04-21T14:12:27+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/21/rollout-2026-04-21T17-18-50-019daf55-d3e2-7e02-91b9-4bff85d20ccc.jsonl
cwd: /Users/zhuji_m4pro/Agent_learn

# User pushed from low-quality metadata-only PDF generation to a Whisper-first, subagent-parallel workflow, then asked to cleanly reorganize the workspace.

Rollout context: working in `/Users/zhuji_m4pro/Agent_learn`, mostly under `bilibili_notes`. The target Bilibili content was the series behind `BV1W34y157tA`, which turned out to be a 30-video collection (`BERT、T5、GPT`). The user later rejected a metadata-only PDF batch and explicitly asked for Whisper-based transcription, deeper understanding, and subagent-driven extraction.

## Task 1: Identify the Bilibili series and list videos
Outcome: success

Preference signals:
- The user asked for “这个哔哩哔哩下面所有的分p视频” and then accepted a full 30-item list, indicating they wanted the complete collection, not just the single BV page.
- After the first answer clarified the single BV was one page but the collection had 30 videos, the user did not push back on the “series vs single video” distinction, implying that future agents should check both the video page and any attached season/collection metadata.

Key steps:
- Used Bilibili public APIs (`x/web-interface/view`) to confirm `BV1W34y157tA` had 1 page but also an attached `ugc_season` with 30 episodes.
- Listed all 30 BV IDs and URLs from the season metadata.

Reusable knowledge:
- For Bilibili pages that look like single-part uploads, check `ugc_season` / collection metadata; the “underneath this video” set may be the collection rather than the page’s `pages[]` list.
- Public API endpoint `https://api.bilibili.com/x/web-interface/view?bvid=...` reliably exposed the season and episodes in this rollout.

References:
- [1] `curl -s 'https://api.bilibili.com/x/web-interface/view?bvid=BV1W34y157tA' | jq '.code, .message, .data.title, (.data.pages | length)'` returned `0`, `"OK"`, title, and `1` page.
- [2] `ugc_season_title: "BERT、T5、GPT"`, `ugc_sections: [{"title":"正片","episodes":30}]`.
- [3] Final 30-BV list was produced and later reused in batch prompts.

## Task 2: First PDF batch was rejected; user required Whisper + deeper extraction
Outcome: fail

Preference signals:
- The user explicitly rejected the first batch: “你太敷衍了，这三十个视频的pdf 都没有图片没有音轨文字，你必须用wisper 去生成，然后理解之后分配给subagent 进行提取，重新做”. This is strong evidence that future work should not rely on metadata-only summaries when the user expects real content extraction.
- The user’s wording implies a preferred workflow: Whisper transcription first, then semantic understanding, then distribute to subagents for extraction.
- The user later asked “继续” multiple times while waiting, so progress updates during long runs were useful.

Key steps:
- First batch attempted to generate one PDF per video using only metadata/collection info and a template-driven structure; it produced 30 PDFs, but the user rejected it as too shallow.
- The redo switched to a Whisper-first pipeline: download audio/video, transcribe with `faster_whisper`, extract keyframes, then generate LaTeX and PDFs.
- The workflow used a repair pass for videos where Bilibili’s DASH stream was unavailable; fallback to `durl` succeeded.
- A second generation pass built better PDFs from Whisper assets, then the work was split among six subagents for deeper rewriting.

Failures and how to do differently:
- The initial approach produced structurally complete but content-poor PDFs; the user explicitly said they lacked images and transcript text and were “敷衍”.
- The corrected default should be: if the user asks for Bilibili note PDFs, prioritize actual Whisper transcription and keyframe extraction before any polishing or summarization.
- For long batch tasks, be explicit about quality gates and whether the result is metadata-only vs audio-derived.

Reusable knowledge:
- `yt-dlp` direct webpage access to Bilibili hit HTTP 412 in this environment; API-based `playurl` requests with browser headers worked better.
- `x/player/playurl?bvid=...&cid=...&fnval=4048` returned DASH streams for most videos; some videos needed `durl` fallback.
- `faster_whisper` was available (`base`, CPU/int8) and produced usable Chinese transcriptions.
- The repaired pipeline generated, per video, `cover.jpg`, `video.m4s`, `audio.m4s` or `source.mp4`, `audio.wav`, `transcript.srt`, `transcript.json`, `frames/frames_manifest.json`, `note.tex`, `note.pdf`.

References:
- [1] First batch script: `bilibili_notes/batch_generate_bilibili_pdfs.py`.
- [2] Whisper prep script: `bilibili_notes/workflows/prepare_whisper_assets.py`.
- [3] Repair script for missing DASH: `bilibili_notes/workflows/repair_failed_assets.py`.
- [4] Generation script from Whisper assets: `bilibili_notes/workflows/generate_notes_from_whisper_assets.py`.
- [5] Final validation showed `30/30` PDFs, `30/30` transcripts, and `0` missing items.

## Task 3: Produce 6 batch prompts for manual/parallel Codex execution
Outcome: success

Preference signals:
- The user asked, “有什么办法能一下子开30个codex 然后一个一个的处理,” then specifically requested, “使用这个promtp生成6批prompt.” This indicates a preference for batched parallel execution with bounded concurrency rather than a single monolithic run.
- The user’s later complaint about quality suggests that the prompt should force substantive extraction, not just asset download.

Key steps:
- Generated a markdown file with 6 prompts, 5 BV IDs per batch, each batch assigned its own output root (`quality_batch_1` … `quality_batch_6`) to avoid collisions.
- Each prompt explicitly required Whisper transcripts, keyframes, detailed Chinese notes, cover images, and successful compilation.

Reusable knowledge:
- Six batches of five videos each is a practical concurrency shape for this workload.
- Output isolation by batch directory is important to prevent cross-agent file overwrites.

References:
- [1] File created: `bilibili_notes/workflows/bilibili_6_batch_prompts.md`.
- [2] Batches were organized as:
  - Batch 1: `BV1W34y157tA` … `BV1X94y1R7La`
  - Batch 2: `BV1sv4y1M7aw` … `BV1VW4y1b79x`
  - Batch 3: `BV1AG4y1H7wq` … `BV14V4y1f7L2`
  - Batch 4: `BV1XX4y1B71n` … `BV1Ho4y1x76q`
  - Batch 5: `BV1Lh4y1b74i` … `BV1ec411971a`
  - Batch 6: `BV1sK421C7oG` … `BV1Vt3QzLEQ1`

## Task 4: Reorganize the `bilibili_notes` workspace into clear categories
Outcome: success

Preference signals:
- The user said, “你整理一下当前biliblinotes文件夹，分门别类的摆放，现在这样太乱了,” showing a strong preference for a cleaner, categorized workspace.
- The user asked for organization without losing work, so a non-destructive move/rename approach is appropriate by default.

Key steps:
- Created a cleaner top-level structure under `bilibili_notes`:
  - `final_outputs/` for final deliverables
  - `workflows/` for scripts and prompts
  - `experiments/` for earlier experiments and reference outputs
  - `cache/` for probes and benchmarks
  - `logs/` for compiler test artifacts
- Moved the final 30-video Whisper/PDF corpus into `final_outputs/bert_t5_gpt_whisper`.
- Moved the earlier low-quality batch and single-video experiments into `experiments/`.
- Moved scripts and the 6-batch prompt file into `workflows/`.
- Added a root `README.md` explaining the layout.

Failures and how to do differently:
- The workspace had accumulated large temporary directories and probes; future long-running Bilibili note work should default to keeping final deliverables separate from scratch assets and benchmarks.
- The final archive is large (`final_outputs` about 2.5G), so if space becomes a concern, the next agent should expect to manage cache/experiment retention explicitly.

Reusable knowledge:
- The organized layout now makes the primary artifact paths easy to find:
  - final PDFs and validation: `final_outputs/bert_t5_gpt_whisper/`
  - batch prompts/scripts: `workflows/`
  - older or lower-quality runs: `experiments/`
  - temp benchmarks/probes: `cache/`
  - compile tests: `logs/`
- Root README now points to `pdf_index.txt`, `final_validation.json`, and the batch prompt file for quick retrieval.

References:
- [1] `bilibili_notes/README.md` describes the new folder taxonomy.
- [2] `bilibili_notes/final_outputs/bert_t5_gpt_whisper/pdf_index.txt` lists all 30 final PDFs.
- [3] `bilibili_notes/final_outputs/bert_t5_gpt_whisper/final_validation.json` reports `ok: true`, `items: 30`, `missing: 0`.
- [4] Root directory check confirmed only categorized folders and README remained at top level.
