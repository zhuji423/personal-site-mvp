---
title: "SSH remote access was configured for the user’s IDE workflow, then upgraded from password login to passwordless SSH key "
description: "Rollout context: The user was on local macOS in /Users/zhujim4pro/Agentlearn and wanted help connecting to a remote Auto"
date: "2026-05-05"
category: "工具与环境"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-21T08-28-42-PDTC-ssh_ide_remote_connection_passwordless_key_setup.md"
---
thread_id: 019daf27-eda3-73e3-95d4-9131893f802c
updated_at: 2026-04-21T12:03:19+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/21/rollout-2026-04-21T16-28-42-019daf27-eda3-73e3-95d4-9131893f802c.jsonl
cwd: /Users/zhuji_m4pro/Agent_learn

# SSH remote access was configured for the user’s IDE workflow, then upgraded from password login to passwordless SSH key login.

Rollout context: The user was on local macOS in `/Users/zhuji_m4pro/Agent_learn` and wanted help connecting to a remote AutoDL Ubuntu host via SSH from the current IDE, then asked for the password to be persistent so they would not have to enter it every time.

## Task 1: Connect to the remote server and make it usable from the IDE

Outcome: success

Preference signals:
- The user asked: "我希望我自己能链接这个远程服务器，帮我用当前ide去链接" -> they want the connection set up in a way that is convenient inside the IDE, not just a one-off terminal login.
- The user was using an existing `~/.ssh/config` and had an older `seetacloud` alias for another host/port, so future work should avoid overwriting that and instead add a separate alias for the new host.

Key steps:
- The agent checked `~/.ssh/config`, saw an existing `seetacloud` entry for `connect.bjb1.seetacloud.com:25873`, and created a separate alias `seetacloud-westd` for `connect.westd.seetacloud.com:18627`.
- The new alias was tested with `ssh seetacloud-westd`, which reached the remote Ubuntu 22.04 / AutoDL container successfully.
- The resulting config block was appended to `~/.ssh/config`.

Failures and how to do differently:
- The first non-escalated SSH attempt failed with DNS resolution error: `ssh: Could not resolve hostname connect.westd.seetacloud.com: -65563`.
- The successful path required escalated network access for SSH connection setup.
- The host key prompt had to be acknowledged with `yes` before the password prompt appeared.

Reusable knowledge:
- The remote host that worked was `connect.westd.seetacloud.com` on port `18627`, logging in as `root`.
- A dedicated alias `seetacloud-westd` was added in `~/.ssh/config` to keep the older `seetacloud` alias untouched.
- The alias initially used password auth; later it was converted to key auth.

References:
- `ssh -p 18627 root@connect.westd.seetacloud.com`
- `Host seetacloud-westd`
- `HostName connect.westd.seetacloud.com`
- `Port 18627`
- Verification: `ssh seetacloud-westd` opened a shell that showed `root@autodl-container-ajgk0b7384-05d929fd:~#`

## Task 2: Make the SSH login persistent / passwordless for IDE use

Outcome: success

Preference signals:
- The user asked: "我希望密码能持久化，不用我每次输入" -> they want a persistent login experience, i.e. passwordless IDE access by default.
- The agent interpreted this as SSH key authentication for the existing `seetacloud-westd` alias, which matches the user’s desire to stop repeated password prompts.

Key steps:
- A dedicated ED25519 keypair was generated locally: `~/.ssh/id_ed25519_seetacloud_westd`.
- `ssh-copy-id` installed the public key on the remote `root` account.
- The `seetacloud-westd` entry in `~/.ssh/config` was updated to use the new key with `IdentityFile`, `IdentitiesOnly yes`, and `PreferredAuthentications publickey`.
- A non-interactive test succeeded: `ssh -o BatchMode=yes seetacloud-westd 'echo SSH_KEY_LOGIN_OK'` returned `SSH_KEY_LOGIN_OK`.

Failures and how to do differently:
- Password authentication was used once more to install the key via `ssh-copy-id`; after that, the connection became passwordless.
- For future similar tasks, key-based login is the durable fix when the user asks for password persistence; merely saving an interactive password would not satisfy the request.

Reusable knowledge:
- The local keypair path is `~/.ssh/id_ed25519_seetacloud_westd`.
- The remote authorized-key installation was done with `ssh-copy-id -i ~/.ssh/id_ed25519_seetacloud_westd.pub -p 18627 root@connect.westd.seetacloud.com`.
- The final config block for the alias was:
  - `Host seetacloud-westd`
  - `HostName connect.westd.seetacloud.com`
  - `User root`
  - `Port 18627`
  - `IdentityFile ~/.ssh/id_ed25519_seetacloud_westd`
  - `IdentitiesOnly yes`
  - `PreferredAuthentications publickey`
  - `AddKeysToAgent yes`
  - `UseKeychain yes`
- After this setup, the user can connect from the IDE by selecting `seetacloud-westd` without being prompted for the server password.

References:
- `ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_seetacloud_westd -N "" -C "seetacloud-westd-2026-04-21"`
- `ssh-copy-id -i ~/.ssh/id_ed25519_seetacloud_westd.pub -p 18627 root@connect.westd.seetacloud.com`
- `ssh -o BatchMode=yes seetacloud-westd 'echo SSH_KEY_LOGIN_OK'`
- `~/.ssh/config:29-37`
- Exact success output: `SSH_KEY_LOGIN_OK`
