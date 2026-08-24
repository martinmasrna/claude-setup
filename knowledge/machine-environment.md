---
name: machine-environment
description: "Martin's Mac quirks — python3 not python, Homebrew broken (use ~/.local/bin), codex CLI available, small browser viewport (~1280x630)"
metadata:
  type: reference
---

Martin's home Mac (macOS 13, Intel), the primary working environment:

- `python` is not on PATH — always `python3` (system Python 3.9).

- `brew install` fails on /usr/local ownership (confirmed 2026-07-29); don't reach for Homebrew. Prefer a standalone binary or user-level install into `~/.local/bin` (on PATH). The `sudo chown` fix is his call, in his own terminal, not something to run for him.

- The Codex CLI (`codex`) is installed and logged in via his ChatGPT subscription. Default model `gpt-5.6-sol` ("Sol"); `gpt-5.6-luna` ("Luna") via `-m`. Bare aliases like `sol` are rejected. Headless `claude -p` and `codex exec` were probe-verified unable to reach web or shell (permission auto-deny).

- His browser viewport is small — about 1280x630 CSS px. Layout judgements are made at that size: vertical room is genuinely scarce and lines that fit on a big screen wrap for him. Check designs at roughly that height. Related: [[visual-taste]].
