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

            (root / "content" / "notes" / "python.md").write_text(
                "# Python 工具笔记\n\n这是第一篇笔记。\n",
                encoding="utf-8",
            )
            (root / "content" / "projects" / "site.md").write_text(
                "# 个人网站\n\n一个最小静态站生成器。\n",
                encoding="utf-8",
            )

            sitegen.build_site(root)

            self.assertIn("Python 工具笔记", (root / "site" / "notes.html").read_text(encoding="utf-8"))
            self.assertIn("个人网站", (root / "site" / "projects.html").read_text(encoding="utf-8"))
            self.assertIn("这是第一篇笔记。", (root / "site" / "notes" / "python.html").read_text(encoding="utf-8"))
            self.assertTrue((root / "site" / "assets" / "style.css").exists())

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
            "# 标题\n\n- item\n\n```python\nprint('hi')\n```\n\n[GitHub](https://github.com)\n"
        )

        self.assertIn("<h1>标题</h1>", html)
        self.assertIn("<li>item</li>", html)
        self.assertIn("<code>print(&#x27;hi&#x27;)</code>", html)
        self.assertIn('<a href="https://github.com">GitHub</a>', html)


if __name__ == "__main__":
    unittest.main()
