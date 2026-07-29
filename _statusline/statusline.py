#!/usr/bin/env python3
"""Claude Code status line.

Reads the session JSON on stdin and prints two lines:

    [Opus 5] 📁 app  | main
    ██████████░░░░ 45% (900k/1.0M)  | 45% (resets in 2h23m)

Cross-platform (macOS/Linux/Windows) — needs python3 on PATH.
Configured via the `statusLine` key in ~/.claude/settings.json.
"""

import json
import os
import subprocess
import sys
import time

# Windows terminals (PS 5.1) default to an OEM codepage that mangles block
# chars/emoji; force UTF-8 on stdout. No-op on platforms where this isn't needed.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RESET = "\033[0m"
DIM = "\033[2m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"

BAR_WIDTH = 14
FOLDER = "\U0001F4C1"


def threshold_color(pct):
    """Green under 70%, yellow approaching the limit, red once it's tight."""
    if pct >= 90:
        return RED
    if pct >= 70:
        return YELLOW
    return GREEN


def tokens(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k".replace(".0k", "k")
    return str(n)


def bar(pct, color):
    filled = int(round(pct / 100 * BAR_WIDTH))
    filled = max(0, min(BAR_WIDTH, filled))
    return f"{color}{'█' * filled}{DIM}{'░' * (BAR_WIDTH - filled)}{RESET}"


def duration(seconds):
    """Seconds -> '2h23m' or '23m'."""
    seconds = max(0, int(seconds))
    h, m = seconds // 3600, (seconds % 3600) // 60
    return f"{h}h{m}m" if h else f"{m}m"


def git_branch(cwd):
    """Current branch, or None outside a repo. Detached HEAD -> short sha."""
    try:
        out = subprocess.run(
            ["git", "-C", cwd, "branch", "--show-current"],
            capture_output=True, text=True, timeout=1,
        )
        if out.returncode != 0:
            return None
        branch = out.stdout.strip()
        if branch:
            return branch
        sha = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=1,
        )
        return sha.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def build(data):
    model = data.get("model", {}).get("display_name")
    cwd = data.get("workspace", {}).get("current_dir") or os.getcwd()
    folder = os.path.basename(cwd.rstrip("/\\")) or cwd

    line1 = f"{CYAN}{BOLD}[{model}]{RESET} " if model else ""
    line1 += f"{FOLDER} {folder}"

    branch = git_branch(cwd)
    if branch:
        line1 += f"  {DIM}|{RESET} {GREEN}{branch}{RESET}"

    lines = [line1]

    segments = []

    ctx = data.get("context_window") or {}
    pct = ctx.get("used_percentage")
    size = ctx.get("context_window_size") or 0
    usage = ctx.get("current_usage") or {}
    used = usage.get("total_input_tokens", 0) or 0
    # Fall back to deriving one from the other if either side is missing.
    if pct is None and size:
        pct = used / size * 100
    if not used and size and pct is not None:
        used = int(size * pct / 100)
    if pct is not None:
        color = threshold_color(pct)
        segments.append(
            f"{bar(pct, color)} {BOLD}{pct:.0f}%{RESET} {DIM}({tokens(used)}/{tokens(size)}){RESET}"
        )

    five_hour = (data.get("rate_limits") or {}).get("five_hour") or {}
    fh_pct = five_hour.get("used_percentage")
    if fh_pct is not None:
        fh_color = threshold_color(fh_pct)
        seg = f"{fh_color}{fh_pct:.0f}%{RESET}"
        resets_at = five_hour.get("resets_at")
        if resets_at:
            seg += f" {DIM}(resets in {duration(resets_at - time.time())}){RESET}"
        segments.append(seg)

    if segments:
        lines.append(f"  {DIM}|{RESET} ".join(segments))

    return lines


def main():
    try:
        # A leading BOM shows up when stdin is piped through PowerShell on
        # Windows; strip it before parsing so that path doesn't degrade silently.
        data = json.loads(sys.stdin.read().lstrip(chr(0xFEFF)))
    except (json.JSONDecodeError, ValueError):
        data = {}
    try:
        lines = build(data)
    except Exception:
        # A status line must never fail loudly — degrade to the essentials.
        lines = [os.path.basename(os.getcwd().rstrip("/\\")) or os.getcwd()]
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
