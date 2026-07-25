#!/usr/bin/env python3
"""Claude Code status line.

Reads the session JSON on stdin and prints one line:

    Opus · ~/Projects/app · ⎇ main · [████░░░░░░] 45.2k/200k (23%) · 5h 45% (reset in 2h 24m)

Configured via the `statusLine` key in ~/.claude/settings.json.
"""

import json
import os
import subprocess
import sys
import time

RESET = "\033[0m"
DIM = "\033[2m"
BOLD = "\033[1m"
CYAN = "\033[36m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"

SEP = f"{DIM} · {RESET}"
BAR_WIDTH = 10


def threshold_color(pct):
    """Green under half, yellow approaching the limit, red once it's tight."""
    if pct >= 80:
        return RED
    if pct >= 50:
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
    return f"{DIM}[{RESET}{color}{'█' * filled}{RESET}{DIM}{'░' * (BAR_WIDTH - filled)}]{RESET}"


def duration(seconds):
    """Seconds -> '2h 24m', '24m', or '<1m'."""
    seconds = max(0, int(seconds))
    h, m = seconds // 3600, (seconds % 3600) // 60
    if h:
        return f"{h}h {m}m"
    return f"{m}m" if m else "<1m"


def home_relative(path):
    home = os.path.expanduser("~")
    if path == home:
        return "~"
    if path.startswith(home + os.sep):
        return "~" + path[len(home):]
    return path


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
    parts = []

    model = data.get("model", {}).get("display_name")
    if model:
        parts.append(f"{BOLD}{CYAN}{model}{RESET}")

    cwd = data.get("workspace", {}).get("current_dir") or os.getcwd()
    parts.append(f"{BLUE}{home_relative(cwd)}{RESET}")

    branch = git_branch(cwd)
    if branch:
        parts.append(f"{MAGENTA}⎇ {branch}{RESET}")

    ctx = data.get("context_window") or {}
    if ctx:
        pct = ctx.get("used_percentage")
        size = ctx.get("context_window_size") or 0
        usage = ctx.get("current_usage") or {}
        used = sum(
            usage.get(k, 0) or 0
            for k in (
                "input_tokens",
                "cache_creation_input_tokens",
                "cache_read_input_tokens",
            )
        )
        # Fall back to deriving one from the other if either side is missing.
        if pct is None and size:
            pct = used / size * 100
        if not used and size and pct is not None:
            used = int(size * pct / 100)
        if pct is not None:
            color = threshold_color(pct)
            segment = bar(pct, color)
            if size:
                segment += f" {tokens(used)}{DIM}/{RESET}{tokens(size)}"
            parts.append(segment)

    five_hour = (data.get("rate_limits") or {}).get("five_hour") or {}
    pct = five_hour.get("used_percentage")
    if pct is not None:
        color = threshold_color(pct)
        segment = f"{color}{pct:.0f}%{RESET}"
        resets_at = five_hour.get("resets_at")
        if resets_at:
            segment += f" {DIM}(reset in {duration(resets_at - time.time())}){RESET}"
        parts.append(segment)

    return SEP.join(parts)


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        data = {}
    try:
        line = build(data)
    except Exception:
        # A status line must never fail loudly — degrade to the essentials.
        line = home_relative(os.getcwd())
    print(line)


if __name__ == "__main__":
    main()
