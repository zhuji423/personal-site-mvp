---
title: "Nano Banana Pro Image Generation & Editing"
description: "Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image). Use for image create/modify requests incl. edits. Supports text-to-image + image-to-image; 1K/2K/4K resolution."
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\imagegen-comate\\SKILL.md"
name: "imagegen"
---

# Nano Banana Pro Image Generation & Editing

Generate new images or edit existing ones using Google's Nano Banana Pro API (Gemini 3 Pro Image) via curl.

## Requirements

### macOS / Linux

- `curl` and `jq` must be installed
- `base64` built-in
- `sips` for auto-resolution detection (macOS built-in)
- `identify` for auto-resolution detection (Linux, via `imagemagick`)

### Windows

- `curl.exe` built-in (Windows 10 1803+)
- PowerShell 5.1+ built-in (Windows 10+), used for all JSON parsing

### Common

- API endpoint: `https://comate.baidu-int.com/api/aidevops/autocomate/rest/autowork/v1/generate-image`
- Username is passed via Header `login-name`, NOT in the request body
- Username: ${COMATE_USERNAME}

---

## Usage

**Important:** Always save output images to the user's current working directory.

### 1. Generate new image (text-to-image)

**macOS / Linux (bash/zsh):**

```bash
curl -s -X POST https://comate.baidu-int.com/api/aidevops/autocomate/rest/autowork/v1/generate-image \
  -H "Content-Type: application/json" \
  -H "login-name: ${COMATE_USERNAME}" \
  -d '{
    "contents": [{"parts": [{"text": "YOUR_PROMPT_HERE"}]}],
    "resolution": "1K"
  }' \
  | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' \
  | base64 --decode > output-name.png
```

**Windows (PowerShell):**

```powershell
# Write JSON to temp file to avoid PowerShell double-quote escaping bug with curl.exe -d
$tmpFile = "$env:TEMP\request.json"
@'
{"contents":[{"parts":[{"text":"YOUR_PROMPT_HERE"}]}],"resolution":"1K"}
'@ | Set-Content -Path $tmpFile -Encoding UTF8 -NoNewline

$response = curl.exe -s -X POST https://comate.baidu-int.com/api/aidevops/autocomate/rest/autowork/v1/generate-image `
  -H "Content-Type: application/json" `
  -H "login-name: $env:${COMATE_USERNAME}" `
  -d "@$tmpFile" | ConvertFrom-Json

$imgBase64 = $response.candidates[0].content.parts |
  Where-Object { $_.inlineData } |
  Select-Object -First 1 -ExpandProperty inlineData |
  Select-Object -ExpandProperty data
[System.IO.File]::WriteAllBytes(
  (Join-Path (Get-Location) "output-name.png"),
  [System.Convert]::FromBase64String($imgBase64)
)
```

### 2. Edit existing image (image-to-image)

**base64 image data is large — must write to a temp file, never inline in the command.**

**macOS / Linux (bash/zsh):**

```bash
# Step 1: encode input image
IMG_B64=$(base64 -i path/to/input.png | tr -d '\n')

# Step 2: write JSON to temp file
cat > /tmp/request.json << EOF
{
  "contents": [
    {
      "parts": [
        {"inline_data": {"mime_type": "image/png", "data": "${IMG_B64}"}},
        {"text": "YOUR_EDIT_INSTRUCTIONS_HERE"}
      ]
    }
  ],
  "resolution": "2K"
}
EOF

# Step 3: send request
curl -s -X POST https://comate.baidu-int.com/api/aidevops/autocomate/rest/autowork/v1/generate-image \
  -H "Content-Type: application/json" \
  -H "login-name: ${COMATE_USERNAME}" \
  -d @/tmp/request.json \
  | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' \
  | base64 --decode > output-name.png
```

**Windows (PowerShell):**

```powershell
# Step 1: encode input image
$imgBytes  = [System.IO.File]::ReadAllBytes((Resolve-Path "path\to\input.png"))
$imgBase64 = [System.Convert]::ToBase64String($imgBytes)

# Step 2: write JSON to temp file
$tmpFile = "$env:TEMP\request.json"
@"
{
  "contents": [
    {
      "parts": [
        {"inline_data": {"mime_type": "image/png", "data": "$imgBase64"}},
        {"text": "YOUR_EDIT_INSTRUCTIONS_HERE"}
      ]
    }
  ],
  "resolution": "2K"
}
"@ | Set-Content -Path $tmpFile -Encoding UTF8

# Step 3: send request
$response = curl.exe -s -X POST https://comate.baidu-int.com/api/aidevops/autocomate/rest/autowork/v1/generate-image `
  -H "Content-Type: application/json" `
  -H "login-name: $env:${COMATE_USERNAME}" `
  -d "@$tmpFile" | ConvertFrom-Json

$outBase64 = $response.candidates[0].content.parts |
  Where-Object { $_.inlineData } |
  Select-Object -First 1 -ExpandProperty inlineData |
Select-Object -ExpandProperty data

[System.IO.File]::WriteAllBytes(
  (Join-Path (Get-Location) "output-name.png"),
  [System.Convert]::FromBase64String($outBase64)
)
```

---

## Default Workflow (draft > iterate > final)

- Draft (1K): quick feedback loop
- Iterate: adjust prompt in small diffs; keep filename new per run
- Final (4K): only when prompt is locked

## Resolution Options

- **1K** (default) - ~1024px, use for drafts and quick feedback
- **2K** - ~2048px, use for mid-quality or medium-size input images
- **4K** - ~4096px, use only when prompt is locked and quality is required

---

## Auto-Resolution Detection (image-to-image only)

When editing an existing image and the user has not specified a resolution,
auto-detect based on the input image's longest edge.

**macOS (bash/zsh):**

```bash
MAX_DIM=$(sips -g pixelWidth -g pixelHeight "input.png" \
  | awk '/pixel/{print $2}' | sort -rn | head -1)

if   [ "${MAX_DIM}" -ge 3000 ]; then RESOLUTION="4K"
elif [ "${MAX_DIM}" -ge 1500 ]; then RESOLUTION="2K"
else                                  RESOLUTION="1K"
fi
```

**Linux (bash):**

```bash
# requires: apt install imagemagick  /  yum install imagemagick
MAX_DIM=$(identify -format "%[fx:max(w,h)]" input.png)

if   [ "${MAX_DIM}" -ge 3000 ]; then RESOLUTION="4K"
elif [ "${MAX_DIM}" -ge 1500 ]; then RESOLUTION="2K"
else                                  RESOLUTION="1K"
fi
```

**Windows (PowerShell):**

```powershell
Add-Type -AssemblyName System.Drawing
$img        = [System.Drawing.Image]::FromFile((Resolve-Path "input.png"))
$maxDim     = [Math]::Max($img.Width, $img.Height)
$img.Dispose()

$resolution = if     ($maxDim -ge 3000) { "4K" }
              elseif ($maxDim -ge 1500) { "2K" }
              else                      { "1K" }
```

---

## Prompt Handling

**For generation:** Pass the user's image description as-is to the `text` field.
**For editing:** Pass editing instructions to the `text` field alongside the `inline_data` image part.

---

## Output

- Saves PNG to current directory
- Script outputs the full path to the generated image
- **Do not read the image back** - display the image using markdown syntax: `![image](/personal-site-mvp/img/doc-placeholder.svg)`
- **Display the image path only once** using a relative path (e.g. `output-name.png` or `subdir/output-name.png`);
- do NOT display absolute paths (e.g. `/home/user/...` formats are forbidden); do NOT repeat the path multiple times in
  the conversation

---

## Notes

| Rule              | macOS/Linux                         | Windows                                                                                                                      |
|-------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| curl command      | `curl`                              | `curl.exe` (avoid PowerShell `curl` alias conflict)                                                                          |
| `-d` body         | inline `'{"key":"val"}'` is fine    | **never** inline — PowerShell escapes `"` to `\u0022`, corrupts JSON; **always** write to temp file and use `-d "@$tmpFile"` |
| base64 encode     | `base64 -i file \| tr -d '\n'`      | `[Convert]::ToBase64String([IO.File]::ReadAllBytes(...))`                                                                    |
| base64 decode     | `base64 --decode`                   | `[IO.File]::WriteAllBytes(path, [Convert]::FromBase64String(...))` (PS 5.1 compatible)                                       |
| image size detect | `sips` (macOS) / `identify` (Linux) | `System.Drawing.Image` (built-in)                                                                                            |
| line continuation | `\`                                 | `` ` `` (backtick)                                                                                                           |
| env variable      | `${COMATE_USERNAME}`                | `$env:COMATE_USERNAME`                                                                                                       |

---

## Windows Pitfall: PowerShell escapes `"` when passing to external programs

When PowerShell passes a variable containing `"` to an external program like `curl.exe`,
it silently converts `"` into `\u0022`, which corrupts JSON and causes the server to return:

```
JsonParseException: Unexpected character ('u'): was expecting double-quote to start field name
```

**Wrong (never do this on Windows):**

```powershell
$body = '{"contents":[...]}'
curl.exe ... -d $body        # PowerShell corrupts the " characters
```

**Correct — always write JSON to a temp file and pass with `-d @file`:**

```powershell
# Single-quote here-string: content is taken literally, no escaping
$tmpFile = "$env:TEMP\request.json"
@'
{"contents":[{"parts":[{"text":"YOUR_PROMPT_HERE"}]}],"resolution":"1K"}
'@ | Set-Content -Path $tmpFile -Encoding UTF8 -NoNewline

curl.exe ... -d "@$tmpFile"  # curl reads the file directly, no PowerShell escaping
```

**Here-string type selection:**

| Situation                                  | Here-string type       | Reason                          |
|--------------------------------------------|------------------------|---------------------------------|
| text-to-image (no variables in JSON)       | `@'...'@` single-quote | content taken literally, safest |
| image-to-image (need `$imgBase64` in JSON) | `@"..."@` double-quote | allows variable expansion       |
