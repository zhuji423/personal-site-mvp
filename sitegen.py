from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import re
import shutil


SITE_TITLE = "个人网站"
TAGLINE = "作品、笔记和长期积累。"


@dataclass(frozen=True)
class Page:
    slug: str
    title: str
    body_html: str
    source_path: Path


STYLE_CSS = """
:root {
  color-scheme: light;
  --bg: #f7f7f4;
  --text: #202124;
  --muted: #61646b;
  --line: #d9d8d1;
  --panel: #ffffff;
  --accent: #0b6bcb;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
  line-height: 1.7;
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.wrap {
  width: min(960px, calc(100% - 32px));
  margin: 0 auto;
}

header {
  border-bottom: 1px solid var(--line);
  background: rgba(247, 247, 244, 0.92);
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  min-height: 68px;
}

.brand {
  font-weight: 700;
  color: var(--text);
}

nav {
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
}

nav a {
  color: var(--muted);
  font-size: 14px;
}

main {
  padding: 44px 0 72px;
}

.hero {
  padding: 28px 0 36px;
}

.hero h1 {
  font-size: clamp(36px, 7vw, 72px);
  line-height: 1.05;
  margin: 0 0 16px;
  letter-spacing: 0;
}

.hero p {
  max-width: 680px;
  color: var(--muted);
  font-size: 18px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

.card {
  display: block;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px;
  color: var(--text);
}

.card h2,
.card h3 {
  margin-top: 0;
  line-height: 1.3;
}

.card p {
  color: var(--muted);
  margin-bottom: 0;
}

.section-title {
  margin-top: 44px;
  border-top: 1px solid var(--line);
  padding-top: 28px;
}

article {
  max-width: 760px;
}

article h1,
article h2,
article h3 {
  line-height: 1.3;
}

pre {
  overflow-x: auto;
  padding: 14px;
  background: #1f2328;
  color: #f6f8fa;
  border-radius: 8px;
}

code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
}

footer {
  border-top: 1px solid var(--line);
  padding: 24px 0;
  color: var(--muted);
  font-size: 14px;
}
""".strip()


def slugify(path: Path) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", path.stem).strip("-").lower() or "page"


def extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def render_inline(text: str) -> str:
    escaped = escape(text)
    return re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>',
        escaped,
    )


def flush_paragraph(parts: list[str], output: list[str]) -> None:
    if parts:
        output.append(f"<p>{render_inline(' '.join(parts))}</p>")
        parts.clear()


def render_markdown(markdown: str) -> str:
    output: list[str] = []
    paragraph: list[str] = []
    list_open = False
    code_open = False
    code_lines: list[str] = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            flush_paragraph(paragraph, output)
            if list_open:
                output.append("</ul>")
                list_open = False
            if code_open:
                output.append("<pre><code>" + escape("\n".join(code_lines)) + "</code></pre>")
                code_lines.clear()
                code_open = False
            else:
                code_open = True
            continue

        if code_open:
            code_lines.append(line)
            continue

        if not line.strip():
            flush_paragraph(paragraph, output)
            if list_open:
                output.append("</ul>")
                list_open = False
            continue

        if line.startswith("# "):
            flush_paragraph(paragraph, output)
            output.append(f"<h1>{render_inline(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            flush_paragraph(paragraph, output)
            output.append(f"<h2>{render_inline(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            flush_paragraph(paragraph, output)
            output.append(f"<h3>{render_inline(line[4:].strip())}</h3>")
        elif line.startswith("- "):
            flush_paragraph(paragraph, output)
            if not list_open:
                output.append("<ul>")
                list_open = True
            output.append(f"<li>{render_inline(line[2:].strip())}</li>")
        else:
            paragraph.append(line.strip())

    flush_paragraph(paragraph, output)
    if list_open:
        output.append("</ul>")
    if code_open:
        output.append("<pre><code>" + escape("\n".join(code_lines)) + "</code></pre>")

    return "\n".join(output)


def read_pages(root: Path, section: str) -> list[Page]:
    source_dir = root / "content" / section
    if not source_dir.exists():
        return []

    pages: list[Page] = []
    for source_path in sorted(source_dir.glob("*.md")):
        markdown = source_path.read_text(encoding="utf-8")
        slug = slugify(source_path)
        pages.append(
            Page(
                slug=slug,
                title=extract_title(markdown, source_path.stem),
                body_html=render_markdown(markdown),
                source_path=source_path,
            )
        )
    return pages


def layout(title: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} - {SITE_TITLE}</title>
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
  <header>
    <div class="wrap topbar">
      <a class="brand" href="{prefix}index.html">{SITE_TITLE}</a>
      <nav>
        <a href="{prefix}projects.html">Projects</a>
        <a href="{prefix}notes.html">Notes</a>
        <a href="{prefix}about.html">About</a>
      </nav>
    </div>
  </header>
  <main class="wrap">
{body}
  </main>
  <footer>
    <div class="wrap">Generated by a tiny Python static site generator.</div>
  </footer>
</body>
</html>
"""


def card_grid(pages: list[Page], section: str) -> str:
    cards = []
    for page in pages:
        cards.append(
            f'<a class="card" href="{section}/{page.slug}.html">'
            f"<h3>{escape(page.title)}</h3>"
            f"<p>{escape(page.source_path.name)}</p>"
            "</a>"
        )
    return '<div class="grid">' + "\n".join(cards) + "</div>" if cards else "<p>还没有内容。</p>"


def write_page(path: Path, title: str, body: str, depth: int = 0) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(layout(title, body, depth), encoding="utf-8")


def build_site(root: Path | str = ".") -> None:
    root = Path(root)
    site_dir = root / "site"
    if site_dir.exists():
        shutil.rmtree(site_dir)

    notes = read_pages(root, "notes")
    projects = read_pages(root, "projects")

    (site_dir / "assets").mkdir(parents=True, exist_ok=True)
    (site_dir / "assets" / "style.css").write_text(STYLE_CSS, encoding="utf-8")

    home_body = f"""
    <section class="hero">
      <h1>{SITE_TITLE}</h1>
      <p>{TAGLINE}</p>
    </section>
    <h2 class="section-title">Projects</h2>
    {card_grid(projects[:3], "projects")}
    <h2 class="section-title">Notes</h2>
    {card_grid(notes[:6], "notes")}
"""
    write_page(site_dir / "index.html", "Home", home_body)
    write_page(site_dir / "notes.html", "Notes", f"<h1>Notes</h1>\n{card_grid(notes, 'notes')}")
    write_page(site_dir / "projects.html", "Projects", f"<h1>Projects</h1>\n{card_grid(projects, 'projects')}")
    write_page(
        site_dir / "about.html",
        "About",
        "<article><h1>About</h1><p>这里放你的个人介绍、技术方向和联系方式。</p></article>",
    )

    for page in notes:
        write_page(site_dir / "notes" / f"{page.slug}.html", page.title, f"<article>{page.body_html}</article>", depth=1)
    for page in projects:
        write_page(site_dir / "projects" / f"{page.slug}.html", page.title, f"<article>{page.body_html}</article>", depth=1)


if __name__ == "__main__":
    build_site(Path(__file__).parent)
