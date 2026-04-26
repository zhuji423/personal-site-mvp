import { defineConfig } from "astro/config";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

export default defineConfig({
  site: "https://zhuji423.github.io",
  base: "/personal-site-mvp",
  markdown: {
    remarkPlugins: [remarkGfm, remarkMath],
    rehypePlugins: [[rehypeKatex, { strict: false }]],
  },
});
