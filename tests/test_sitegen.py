from pathlib import Path
import tempfile
import unittest

import sitegen


class SiteGeneratorTest(unittest.TestCase):
    def test_build_site_generates_home_notes_projects_and_static_assets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content" / "notes").mkdir(parents=True)
            (root / "content" / "projects").mkdir(parents=True)
            (root / "content" / "assets").mkdir(parents=True)

            (root / "content" / "notes" / "python.md").write_text(
                "# Python 工具笔记\n\n这是第一篇笔记。\n",
                encoding="utf-8",
            )
            (root / "content" / "projects" / "site.md").write_text(
                "# 个人网站\n\n一个最小静态站生成器。\n",
                encoding="utf-8",
            )
            (root / "content" / "assets" / "thesis.pdf").write_bytes(b"%PDF-1.4 test")

            sitegen.build_site(root)

            self.assertIn("Python 工具笔记", (root / "site" / "notes.html").read_text(encoding="utf-8"))
            self.assertIn("个人网站", (root / "site" / "projects.html").read_text(encoding="utf-8"))
            self.assertIn("这是第一篇笔记。", (root / "site" / "notes" / "python.html").read_text(encoding="utf-8"))
            self.assertTrue((root / "site" / "assets" / "style.css").exists())
            self.assertEqual(b"%PDF-1.4 test", (root / "site" / "assets" / "thesis.pdf").read_bytes())

    def test_generated_links_are_relative_for_project_pages_deployments(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content" / "notes").mkdir(parents=True)
            (root / "content" / "notes" / "python.md").write_text("# Python\n", encoding="utf-8")

            sitegen.build_site(root)

            home = (root / "site" / "index.html").read_text(encoding="utf-8")
            note = (root / "site" / "notes" / "python.html").read_text(encoding="utf-8")

            self.assertIn('href="assets/style.css"', home)
            self.assertIn('href="projects.html"', home)
            self.assertIn('href="../assets/style.css"', note)
            self.assertIn('href="../notes.html"', note)

    def test_markdown_renderer_handles_headings_lists_code_and_links(self):
        html = sitegen.render_markdown(
            "# 标题\n\n- item\n\n```python\nprint('hi')\n```\n\n[GitHub](https://github.com)\n\n[详情](projects/thesis.html)\n"
        )

        self.assertIn("<h1>标题</h1>", html)
        self.assertIn("<li>item</li>", html)
        self.assertIn("<code>print(&#x27;hi&#x27;)</code>", html)
        self.assertIn('<a href="https://github.com" target="_blank" rel="noopener">GitHub</a>', html)
        self.assertIn('<a href="projects/thesis.html">详情</a>', html)

    def test_about_page_can_be_written_in_markdown_and_link_to_project_detail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content").mkdir()
            (root / "content" / "about.md").write_text(
                "# About\n\n本科论文：[基于心电散点图识别的心脏类疾病诊断](projects/undergraduate-thesis.html)\n",
                encoding="utf-8",
            )

            sitegen.build_site(root)

            about = (root / "site" / "about.html").read_text(encoding="utf-8")
            self.assertIn("本科论文", about)
            self.assertIn('href="projects/undergraduate-thesis.html"', about)

    def test_pdf_links_open_in_new_tab(self):
        html = sitegen.render_markdown("[PDF](../assets/undergraduate-thesis.pdf)")

        self.assertIn(
            '<a href="../assets/undergraduate-thesis.pdf" target="_blank" rel="noopener">PDF</a>',
            html,
        )

    def test_markdown_renderer_ignores_utf8_bom(self):
        html = sitegen.render_markdown("\ufeff# 带 BOM 的标题")

        self.assertIn("<h1>带 BOM 的标题</h1>", html)


if __name__ == "__main__":
    unittest.main()
