---
title: "Comate Automation Browser"
description: "|"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\automation-browser-comate\\SKILL.md"
name: "comate-automation-browser"
hidden: "true"
---

# Comate Automation Browser

Invoke browser automation capabilities via the `run_command` tool with the `comate-automation-browser` prefix.

## Invocation

```json
{ "command": "comate-automation-browser <subcommand> [arguments]" }
```

**Important**: Must be invoked via `run_command` with the `comate-automation-browser` prefix. Do not call `browser_use` as a standalone tool directly, and do not execute `comate-automation-browser` as a shell command. The `run_command` call **MUST** contain only the `comate-automation-browser ...` command exactly as shown — do not prepend, append, or chain any other commands (e.g., no `&&`, `||`, `;`, `|`, or subshells). This is Comate's wrapper around the IDE browser, not Claude Code's native `browser-use` CLI.

## Core Workflow

Follow this sequence by default, unless the task explicitly does not require it:

```text
1. navigate/open
2. snapshot or status
3. click/type/fill_form/drag/click_at
4. snapshot/status
5. screenshot/console/evaluate for verification
```

For asynchronously updating pages, do not assume success after a single action. Repeatedly verify using `snapshot`, `status`, `evaluate`, `console`, or `screenshot`.

## Browser Modes

The current mode is determined by IDE settings; the agent does not need to choose.

- `builtin`
  - Runs in the IDE's built-in browser or webview.
  - `snapshot` returns an approximate accessibility tree, not a full Playwright snapshot.
  - Post-action waits are heuristic-based; complex frontend pages may require additional verification.
- `chrome`
  - Connects to the local Chrome/CDP, reusing a Comate-dedicated persistent profile.
- `standalone`
  - Uses a standalone Chromium downloaded by Comate.
- `off`
  - Browser capabilities are disabled; tool calls will fail.

## Available Commands

### Navigation

| Command | Arguments | Description |
|---------|-----------|-------------|
| `navigate <url>` | `url` (required) | Navigate to the specified URL |
| `open <url>` | `url` (required) | Alias for `navigate` |
| `back` | — | Go back in browser history |
| `forward` | — | Go forward in browser history |
| `reload` | — | Reload the current page |

### Page Inspection

| Command | Arguments | Description |
|---------|-----------|-------------|
| `snapshot` | — | Get an accessibility snapshot (YAML tree with element UID/`ref`) |
| `html [selector]` | `selector` (optional) | Get page HTML, optionally filtered by CSS selector |
| `screenshot` | See options below | Take a screenshot of the current page |
| `status` | — | Show current browser state and all open tabs |
| `console` | See options below | Get console messages |
| `evaluate <script>` | `script` (required) | Execute JavaScript in the page context |

`screenshot` options:
- Positional argument: `filePath`, path to save the screenshot
- `--format <png|jpeg|webp>`, image format
- `--full-page`, capture the entire scrollable page
- `--uid <uid>`, capture a specific element by UID

`console` options:
- `--types <type...>`, filter by type, available values: `log info warn error debug`
- `--limit <n>`, limit the number of returned entries
- `--offset <n>`, start reading from the specified offset
- `--include-preserved`, include previously collected messages

### Interaction

| Command | Arguments | Description |
|---------|-----------|-------------|
| `click <uid>` | `uid` (required) | Click an element |
| `dblclick <uid>` | `uid` (required) | Double-click an element |
| `rightclick <uid>` | `uid` (required) | Right-click an element |
| `click_at <x> <y>` | Coordinates (required) | Click at coordinates, suitable for canvas/special controls |
| `type <text>` | See options below | Type text |
| `scroll <direction>` | `up/down/left/right` | Scroll the page |
| `drag <startUid> <endUid>` | Start and end UIDs (required) | Drag an element |
| `fill_form <json>` | JSON (required) | Batch fill form fields |

`click` options:
- `--double`, double-click
- `--button <left|right|middle>`, specify mouse button
- `--modifiers <Alt Control Meta Shift>`, click with modifier keys

`type` options:
- `<text>` (required), the text to type; wrap multi-word text in quotes
- `--uid <uid>`, specify the target element
- `--submit`, press Enter after typing
- `--slowly`, type character by character

`scroll` options:
- `--amount <pixels>`, specify scroll distance in pixels

`fill_form` notes:
- Argument should be a JSON array, or a JSON object containing a `fields` array
- Each field object must include at least `name`, `type`, `ref`/`uid`, and `value`
- `ref`/`uid` must come from the most recent `snapshot`

Example:

```text
comate-automation-browser fill_form '[{"name":"Email","type":"textbox","uid":"e3","value":"hi@example.com"}]'
```

### Tab Management

| Command | Arguments | Description |
|---------|-----------|-------------|
| `new_page [url]` | `url` (optional) | Open a new tab, optionally navigating to a URL |
| `select_page <index>` | `index` (integer) | Switch to a tab by index |
| `close_page <index>` | `index` (integer) | Close a tab by index |

## Execution Behavior

- Manual confirmation mode (default): Commands enter a `pending` state and wait for user confirmation.
- Auto-execute mode: When `autoExecute` is enabled in settings, commands execute immediately.
- Status flow: `pending -> running -> success / failed / aborted / skipped`

## Standard Workflows

### General Interaction

```text
1. run_command: "comate-automation-browser navigate https://example.com"
2. run_command: "comate-automation-browser snapshot"
3. run_command: "comate-automation-browser click e15"
4. run_command: "comate-automation-browser snapshot"
5. run_command: "comate-automation-browser screenshot"
```

### Reading Page Content

```text
1. run_command: "comate-automation-browser navigate https://example.com"
2. run_command: "comate-automation-browser evaluate document.body.innerText"
3. For a specific section: evaluate document.querySelector('.article').innerText
```

### Form Filling

```text
1. run_command: "comate-automation-browser snapshot"
2. Identify field UIDs/refs from the snapshot
3. run_command: "comate-automation-browser fill_form '[{\"name\":\"Email\",\"type\":\"textbox\",\"uid\":\"e3\",\"value\":\"hi@example.com\"}]'"
4. run_command: "comate-automation-browser snapshot"
5. run_command: "comate-automation-browser screenshot"
```

## Key Rules

- UIDs/refs come from `snapshot`. Always run `snapshot` before using `click`, `type --uid`, `drag`, `fill_form`, or `screenshot --uid`.
- Re-run `snapshot` after interactions by default. After clicking, navigating, scrolling, reloading, submitting forms, switching tabs, or executing `evaluate` that modifies the DOM, always refresh the page state.
- Use `snapshot` for structure and interaction; prefer `evaluate ...innerText` for reading body text. Do not use `html` as a text extraction tool.
- When `type` is used without `--uid`, only use it when an element is already focused. If the input target is unclear, run `snapshot` first and pass `--uid`.
- There is no explicit `wait` command for async pages. Poll and verify results using `snapshot`, `status`, `console`, `evaluate`, or `screenshot`.
- Fall back to alternative actions for complex controls. If a regular click fails, consider `dblclick`, `rightclick`, `click_at`, or `drag`.
- Always run `status` before tab operations. Closing the last tab is generally not possible.
- Sessions are automatically managed per conversation; no need to manually create or destroy sessions.
- Do not expose cache paths or temporary paths for screenshots, HTML, or script results in responses.
- When a command indicates that content has been written to a file, read the corresponding file directly to get the full result.

## Pause for Manual User Actions

Pause automation and wait for the user to complete the following scenarios:

- CAPTCHA, slider verification, or bot detection challenges
- SMS or email verification codes
- QR code login
- User-specific sensitive credentials such as passwords, OTP, or security tokens
- Complex choices requiring the user's subjective judgment

Regular form filling, button clicking, and text input do not fall into this category and should be handled by the agent.

## Troubleshooting

### Element Not Found

```text
1. snapshot
2. scroll down --amount 600
3. snapshot
4. If still failing, use screenshot or console to assist in locating the element
```

### No Response After Action

```text
1. snapshot
2. status
3. console --types warn error --limit 20
4. evaluate document.readyState
5. screenshot
```

### IDE Built-in Browser Behaving Unexpectedly

- In `builtin` mode, waits and snapshots are approximate implementations.
- If the page relies heavily on animations, virtual lists, canvas, or complex focus management, always perform an additional verification step — do not assume the first action succeeded.
