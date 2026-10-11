---
title: "camsnap"
description: "Capture frames or clips from RTSP/ONVIF cameras."
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\skills\\camsnap\\SKILL.md"
name: "camsnap"
homepage: "https://camsnap.ai"
---

# camsnap

Use `camsnap` to grab snapshots, clips, or motion events from configured cameras.

Setup

- Config file: `~/.config/camsnap/config.yaml`
- Add camera: `camsnap add --name kitchen --host 192.168.0.10 --user user --pass pass`

Common commands

- Discover: `camsnap discover --info`
- Snapshot: `camsnap snap kitchen --out shot.jpg`
- Clip: `camsnap clip kitchen --dur 5s --out clip.mp4`
- Motion watch: `camsnap watch kitchen --threshold 0.2 --action '...'`
- Doctor: `camsnap doctor --probe`

Notes

- Requires `ffmpeg` on PATH.
- Prefer a short test capture before longer clips.
