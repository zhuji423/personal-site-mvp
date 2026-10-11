# -*- coding: utf-8 -*-
"""Import personal MD docs into Astro site content collection.

Idempotent: re-running rebuilds src/content/docs and the manifest.
File names and directory hierarchy are preserved verbatim (emoji included).
"""
import csv
import hashlib
import io
import os
import re
import shutil
import sys
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(REPO, "src", "content", "docs")
ASSET_SRC_ROOT = os.path.join(
    r"F:\百度工作\02_Agent_learn\Agent_learn\downloads_20260427_organized",
    "00_source_zips", "知识库文档下载_2026-04-28", "知识库文档下载_2026-04-28",
)
ASSET_PUBLIC_DIR = os.path.join(REPO, "public", "img", "docs-assets")
MANIFEST = os.path.join(REPO, "scripts", "docs_manifest.csv")

ROOTS = [
    r"F:\百度工作\01_code",
    r"F:\百度工作\02_Agent_learn",
    r"F:\百度工作\03_documents_keep",
    r"F:\百度工作\05_downloads_keep",
    r"F:\百度工作\06_comate_aiide_config",
    r"F:\百度工作\07_codex_cloud_data_sensitive",
    r"D:\mac_m4\Agent_learn",
    r"D:\mac_m4\code",
    r"D:\mac_m4\My_project",
]

EXCLUDE_DIR_TOKENS = [
    "node_modules", ".venv", "venv", "site-packages", ".conda",
    "__pycache__", ".git", ".tmp", "plugins", "extensions", "vendor_imports",
]
EXCLUDE_PATH_PREFIXES = [
    os.path.join(".codex", ".tmp"),
    os.path.join(".codex", "plugins"),
    "vendor_imports",
    os.path.join(".comate", "extensions"),
]

# Ordered rules: (category, path-regex, name-regex). First hit wins.
RULES = [
    ("BatOwl与UI检测", re.compile(r"ui_defect_detection|BatOwl|batowl|roamdetect|录屏体验师", re.I), None),
    ("项目架构文档", re.compile(r"itp|qamate|apismart|wiki_deepseek|ARCHITECTURE_OVERVIEW|core-migrate|fix_roamdetect", re.I), None),
    ("平台与接入文档", re.compile(r"testone|如流|ducc|沙箱|接入指南|knowledge_docs|comate|baidu-cc|Docker文档导出", re.I), None),
    ("AI案例与实践", re.compile(r"ku-export-ai-cases|AI.?实践案例库|AI案例库", re.I), None),
    ("学习笔记-周洁", re.compile(r"08-周洁学习记录|知识库文档下载|mSXjJv4PDMDxpo", re.I), None),
    ("个人事务与记录", None, re.compile(r"述职|简历|杨德乾|离职|晋升|绩效|OKR|孟新萍|年终|举报|起诉|身份证|email_classification|email-export|迁移|MIGRATION|投递清单")),
    ("研究与资讯", None, re.compile(r"论文|精读|研读|会议|survey|Survey|daily-research|daily-tech")),
    ("Agent与RAG", re.compile(r"wow-rag|RAG|GraphRAG|openclaw|auto-dev|hackthon|medical|qerag|sandbox_agent", re.I), re.compile(r"Agent|agent|RAG|AutoGen|Auto-GPT|ChatDev|OpenDevin|SWE-agent|ComfyUI|AppBuilder|coze|扣子")),
    ("NLP与大模型", None, re.compile(r"NLP|Bert|bert|大模型|大语言模型|LLM|llm|chatglm|ChatGLM|llama|LLaMa|GPT|transformers?|微调|lora|LoRA|prompt|文心|词向量|token|AIGC|EMO|Sora|文生")),
    ("视觉与图像", None, re.compile(r"视觉|图像|图像|torchvision|目标检测|分割|OCR|StableDiffusion|Stable.?Diffusion|Midjourney|关键点|ControlNet|Flux|作画|图片|空间智能|可视化|视频|Avatar|Genmoji|多模态")),
    ("深度学习与机器学习", None, re.compile(r"神经网络|深度学习|机器学习|损失函数|优化算法|正则化|dropout|注意力|MNIST|GAN|激活函数|数据集|显存|GPU|训练|量化|分类算法|归一化|机器学习|cs336|LLMs-from-scratch| llama")),
    ("推荐系统", None, re.compile(r"推荐|DeepFM|协同过滤|召回|贴吧")),
    ("后端与工程", None, re.compile(r"Java|Spring|Maven|Nginx|Docker|Git|数据库|Redis|Kafka|hadoop|Spark|RPC|flask|Vue|React|前端|gdp2|中间件|NLP学习|冒烟|ORC|ep-qa| consult|后端|接口")),
    ("工具与环境", None, re.compile(r"开发机|工具|环境|Chrome|扩展|python包|LaTeX|pip|bcloud|Outlook|orp|配置|README|CHANGELOG|LICENSE|setup|安装|使用指南|快捷键")),
]
FALLBACK = "未分类"
CATEGORIES = [r[0] for r in RULES] + [FALLBACK]

IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}
NTFS_BAD = dict.fromkeys(map(ord, '<>:"|?*'), "_")
NTFS_BAD[ord("%")] = "％"  # full-width percent: URI-safe


def lp(path):
    """Windows long-path prefix."""
    p = os.path.abspath(path)
    if p.startswith("\\\\?\\"):
        return p
    return "\\\\?\\" + p


def is_excluded(rel: str) -> bool:
    parts = rel.replace("/", os.sep).split(os.sep)
    if any(t in parts for t in EXCLUDE_DIR_TOKENS):
        return True
    norm = rel.replace("/", os.sep)
    return any(norm.startswith(p.replace("/", os.sep)) for p in EXCLUDE_PATH_PREFIXES)


def classify(rel: str, name: str) -> str:
    for cat, path_re, name_re in RULES:
        if path_re and path_re.search(rel):
            return cat
        if name_re and name_re.search(name):
            return cat
    return FALLBACK


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(lp(path), "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def yaml_str(v: str) -> str:
    v = str(v).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{v}"'


def parse_frontmatter(text: str):
    """Return (fm_dict, body). Only supports simple flat key: value blocks."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return fm, text[m.end():]


def extract_title(body: str, filename: str) -> str:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# ") and len(s) > 2:
            return s[2:].strip()[:120]
    return os.path.splitext(filename)[0]


def extract_desc(body: str) -> str:
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p.startswith(("#", "!", "[//", "<", "---", "```", "|", "thread_id", "updated_at", "rollout_path", "cwd")):
            continue
        p = re.sub(r"[*_`>#\[\]()!]", "", p)
        p = re.sub(r"\s+", " ", p).strip()
        if len(p) >= 8:
            return p[:120]
    return ""


def build_frontmatter(fm: dict, title: str, desc: str, date: str, cat: str, source: str) -> str:
    out = {
        "title": fm.get("title") or title,
        "description": fm.get("description") or desc,
        "date": fm.get("date") or date,
        "category": fm.get("category") or cat,
        "source": fm.get("source") or source,
    }
    keep = {k: v for k, v in fm.items() if k not in out}
    lines = ["---"]
    for k in ("title", "description", "date", "category", "source"):
        if out[k]:
            lines.append(f"{k}: {yaml_str(out[k])}")
    for k, v in keep.items():
        if v:
            lines.append(f"{k}: {yaml_str(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def sanitize_component(s: str) -> str:
    return s.translate(NTFS_BAD).rstrip(" .") or "_"


IMG_MD_REF = re.compile(r"(!\[[^\]]*\]\()([^)\s]+)(\)|\s)", re.M)
IMG_HTML_REF = re.compile(r"(<img[^>]*src=([\"']))([^\"']+)(\2)", re.I)


def rewrite_images(rel_body: str, src_md_abs: str, copied: set) -> str:
    """Rewrite relative image refs: knowledge assets -> copied public assets; others -> placeholder."""
    PLACEHOLDER = "/personal-site-mvp/img/doc-placeholder.svg"

    def new_url(target: str):
        ref_unq = target.replace("%20", " ")
        if ref_unq.startswith(("http://", "https://", "data:", "#", "/")):
            return None
        src_dir = os.path.dirname(src_md_abs)
        cand = os.path.normpath(os.path.join(src_dir, ref_unq))
        if os.path.splitext(cand)[1].lower() not in IMG_EXT:
            return None
        if os.path.abspath(cand).startswith(ASSET_SRC_ROOT) and os.path.isfile(lp(cand)):
            return resolve_asset(ref_unq, src_md_abs, copied)
        return PLACEHOLDER

    def repl_md(m):
        new = new_url(m.group(2))
        return m.group(1) + (new or m.group(2)) + m.group(3) if new else m.group(0)

    def repl_html(m):
        new = new_url(m.group(3))
        return (m.group(1) + (new or m.group(3)) + m.group(4)) if new else m.group(0)

    body = IMG_MD_REF.sub(repl_md, rel_body)
    body = IMG_HTML_REF.sub(repl_html, body)
    return body


def resolve_asset(ref: str, src_md_abs: str, copied: set):
    ref_unq = ref.replace("%20", " ")
    if ref_unq.startswith(("http://", "https://", "/", "#", "data:")):
        return None
    src_dir = os.path.dirname(src_md_abs)
    cand = os.path.normpath(os.path.join(src_dir, ref_unq))
    if not os.path.abspath(cand).startswith(ASSET_SRC_ROOT):
        return None
    if not os.path.isfile(lp(cand)) or os.path.splitext(cand)[1].lower() not in IMG_EXT:
        return None
    flat = sanitize_component(os.path.basename(cand))
    dst = os.path.join(ASSET_PUBLIC_DIR, flat)
    base, ext = os.path.splitext(flat)
    i = 1
    while os.path.exists(lp(dst)) and not filecmp_ok(cand, dst):
        flat = f"{base}_{i}{ext}"
        dst = os.path.join(ASSET_PUBLIC_DIR, flat)
        i += 1
    os.makedirs(lp(ASSET_PUBLIC_DIR), exist_ok=True)
    if not os.path.exists(lp(dst)):
        shutil.copyfile(lp(cand), lp(dst))
    copied.add(flat)
    return "/personal-site-mvp/img/docs-assets/" + urllib_quote(flat)


def filecmp_ok(a, b):
    return os.path.getsize(a) == os.path.getsize(b)


def urllib_quote(s):
    from urllib.parse import quote
    return quote(s)


def main():
    if os.path.isdir(DOCS_DIR):
        shutil.rmtree(lp(DOCS_DIR))
    os.makedirs(lp(DOCS_DIR), exist_ok=True)
    os.makedirs(lp(ASSET_PUBLIC_DIR), exist_ok=True)
    for f in os.listdir(ASSET_PUBLIC_DIR):
        os.remove(lp(os.path.join(ASSET_PUBLIC_DIR, f)))

    seen_hash = {}
    rows = []
    copied_imgs = set()
    stats = {c: 0 for c in CATEGORIES}
    scanned = kept = 0

    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for dp, dns, fns in os.walk(root):
            rel_dp = os.path.relpath(dp, root)
            if is_excluded("" if rel_dp == "." else rel_dp.replace(os.sep, "/")):
                dns[:] = []
                continue
            for fn in fns:
                if fn.startswith("._"):
                    continue
                if not fn.lower().endswith((".md", ".markdown")):
                    continue
                src = os.path.join(dp, fn)
                rel = os.path.relpath(src, root).replace(os.sep, "/")
                if is_excluded(rel):
                    continue
                scanned += 1
                try:
                    h = sha256_file(src)
                except OSError:
                    rows.append([src, "ERROR-READ", "", ""])
                    continue
                if h in seen_hash:
                    rows.append([src, stats and "DUPLICATE", seen_hash[h], ""])
                    continue
                seen_hash[h] = src

                cat = classify(rel, fn)
                rel_parts = [sanitize_component(p) for p in rel.split("/")]
                # strip leading dot from dir components: glob loader ignores dot-dirs
                rel_parts = [(x[1:] if x.startswith(".") and x != "." else x) for x in rel_parts]
                target_rel = os.path.join(cat, *rel_parts)
                target = os.path.join(DOCS_DIR, *rel_parts)
                target = os.path.join(DOCS_DIR, cat, *rel_parts)
                # collision with different content -> suffix
                n = 1
                while os.path.exists(lp(target)):
                    stem, ext = os.path.splitext(target)
                    target = f"{stem}__dup{n}{ext}"
                    n += 1

                mtime = datetime.fromtimestamp(os.path.getmtime(lp(src))).strftime("%Y-%m-%d")
                with io.open(lp(src), "r", encoding="utf-8", errors="replace") as f:
                    text = f.read()
                fm, body = parse_frontmatter(text)
                title = extract_title(body, fn)
                desc = extract_desc(body)
                body = rewrite_images(body, src, copied_imgs)
                out = build_frontmatter(fm, title, desc, mtime, cat, src) + body
                os.makedirs(lp(os.path.dirname(target)), exist_ok=True)
                with io.open(lp(target), "w", encoding="utf-8", newline="\n") as f:
                    f.write(out)
                kept += 1
                stats[cat] += 1
                rows.append([src, cat, target, os.path.basename(target)])

    with io.open(MANIFEST, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "category", "target", "note"])
        w.writerows(rows)

    print(f"scanned={scanned} kept={kept} images_copied={len(copied_imgs)}")
    for c in CATEGORIES:
        if stats[c]:
            print(f"  {c}: {stats[c]}")


if __name__ == "__main__":
    main()
