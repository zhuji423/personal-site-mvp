import { mkdir, readdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const sourceDir = path.join(repoRoot, "weixincli-report", "reports");
const targetDir = path.join(repoRoot, "src", "content", "wechat-daily");
const dailyFile = /^dive-into-genai-daily-analysis-(\d{4}-\d{2}-\d{2})\.md$/;

function yamlString(value) {
  return JSON.stringify(value);
}

function extractOneLineSummary(markdown) {
  const match = markdown.match(/^## 一句话摘要\s*\n+([^\n]+)$/m);
  const summary = match?.[1]?.replace(/\s+/g, " ").trim();
  if (!summary) return "Dive into GenAI 群聊日级分析。";
  return summary.length > 220 ? `${summary.slice(0, 217)}...` : summary;
}

function stripGeneratedFrontMatter(markdown) {
  return markdown.replace(/^---\n[\s\S]*?\n---\n\s*/, "");
}

function stripTitle(markdown) {
  return markdown.replace(/^#\s+[^\n]+\n\s*/, "");
}

await rm(targetDir, { recursive: true, force: true });
await mkdir(targetDir, { recursive: true });

try {
  const entries = await readdir(sourceDir, { withFileTypes: true });
  const reports = entries
    .filter((entry) => entry.isFile() && dailyFile.test(entry.name))
    .map((entry) => {
      const date = dailyFile.exec(entry.name)[1];
      return { date, sourcePath: path.join(sourceDir, entry.name) };
    })
    .sort((a, b) => a.date.localeCompare(b.date));

  for (const report of reports) {
    const original = await readFile(report.sourcePath, "utf8");
    if (/(^|[^A-Za-z])sk-[A-Za-z0-9_-]{12,}/.test(original)) {
      throw new Error(`Refusing to publish a report that contains an API key: ${report.sourcePath}`);
    }

    const body = stripTitle(stripGeneratedFrontMatter(original)).trim();
    const titleMatch = original.match(/^#\s+([^\n]+)/);
    const title = titleMatch?.[1] ?? `Dive into GenAI 日级分析（${report.date}）`;
    const frontMatter = [
      "---",
      `title: ${yamlString(title)}`,
      `description: ${yamlString(extractOneLineSummary(original))}`,
      `date: ${yamlString(report.date)}`,
      'category: "WeChat Daily"',
      'source: "Dive into GenAI"',
      "---",
      "",
    ].join("\n");

    await writeFile(path.join(targetDir, `${report.date}.md`), `${frontMatter}${body}\n`, "utf8");
  }

  console.log(`Synced ${reports.length} WeChat daily reports to ${path.relative(repoRoot, targetDir)}.`);
} catch (error) {
  if (error?.code === "ENOENT") {
    console.warn(`Source report directory does not exist: ${sourceDir}`);
    process.exit(1);
  }
  throw error;
}