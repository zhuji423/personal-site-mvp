$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$Repo = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Date = Get-Date -Format "yyyy-MM-dd"
$Report = Join-Path $Repo "weixincli-report\reports\dive-into-genai-daily-analysis-$Date.md"

Write-Host "==> Exporting WeChat archive for $Date"
$env:PYTHONIOENCODING = "utf-8"
$Python = "C:\apps\miniconda\python.exe"
$Exporter = Join-Path $Repo "weixincli-report\reporter\run_export.py"
& $Python -u $Exporter
if ($LASTEXITCODE -ne 0) { throw "WeChat export failed with exit code $LASTEXITCODE" }

Write-Host "==> Generating daily analysis with Codex"
$CodexCandidates = Get-ChildItem -LiteralPath (Join-Path $env:LOCALAPPDATA "OpenAI\Codex\bin") -Recurse -Filter codex.exe -File -ErrorAction SilentlyContinue |
  Sort-Object LastWriteTime -Descending
$Codex = $CodexCandidates | Select-Object -First 1
if (-not $Codex) { throw "codex.exe was not found under $env:LOCALAPPDATA\OpenAI\Codex\bin" }

$PromptTemplate = Get-Content -LiteralPath (Join-Path $Repo "tools\prompts\wechat-daily.md") -Raw
$Prompt = $PromptTemplate.Replace("YYYY-MM-DD", $Date)
$LastMessage = Join-Path $env:TEMP "wechat-daily-$Date-codex.txt"
$Prompt | & $Codex.FullName exec --cd $Repo --sandbox workspace-write --approve-for-me --output-last-message $LastMessage -
if ($LASTEXITCODE -ne 0) { throw "Codex daily summary failed with exit code $LASTEXITCODE" }
if (-not (Test-Path -LiteralPath $Report)) { throw "Codex did not create $Report" }

Write-Host "==> Syncing reports into Astro"
$Node = (Get-Command node.exe -ErrorAction Stop).Source
$Sync = Join-Path $Repo "tools\sync-wechat-reports.mjs"
& $Node $Sync
if ($LASTEXITCODE -ne 0) { throw "Report sync failed with exit code $LASTEXITCODE" }

Write-Host "==> Building Astro site"
Push-Location $Repo
try {
  npm run build
  if ($LASTEXITCODE -ne 0) { throw "Astro build failed with exit code $LASTEXITCODE" }

  git pull --rebase --autostash
  git add -- src/content/wechat-daily
  if ($LASTEXITCODE -ne 0) { throw "git add failed with exit code $LASTEXITCODE" }

  $Changed = git diff --cached --name-only
  if (-not $Changed) {
    Write-Host "No WeChat daily content changed."
  } else {
    git commit -m "chore: publish WeChat daily $Date"
    if ($LASTEXITCODE -ne 0) { throw "git commit failed with exit code $LASTEXITCODE" }
    git push
    if ($LASTEXITCODE -ne 0) { throw "git push failed with exit code $LASTEXITCODE" }
  }
} finally {
  Pop-Location
}
