# _statusline

Custom Claude Code status line. Not a skill — the `_` prefix keeps it out of skill
discovery, same as `_knowledge/`.

```
Opus · ~/Projects/app · ⎇ main · [██░░░░░░░░] 45.5k/200k · 45% (reset in 2h 23m)
```

Left to right: model, working folder, git branch, context window (progress bar +
tokens used/total), and 5-hour usage percentage with time until reset. The bar and
the usage figure turn yellow at 50% and red at 80%.

## Activating it

Cloning this repo installs the script but does **not** switch it on — that lives in
`~/.claude/settings.json`, which is outside the repo. Add:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/skills/_statusline/statusline.py"
  }
}
```

Then restart Claude Code; the status line is read at session start.

If the bar doesn't appear, check that the script is executable
(`chmod +x ~/.claude/skills/_statusline/statusline.py`) and that `disableAllHooks`
is not set in your settings — it disables the status line too.

## How it works

Claude Code pipes session JSON to the script on stdin. Everything shown comes from
that payload: `model.display_name`, `workspace.current_dir`, `context_window`
(`used_percentage`, `current_usage`, `context_window_size`), and
`rate_limits.five_hour` (`used_percentage`, `resets_at`). The branch comes from
`git branch --show-current`, falling back to a short SHA on detached HEAD.

Needs `python3` and a Claude Code new enough to send `context_window` and
`rate_limits`. Segments whose data is missing are dropped rather than guessed, so
an older client shows a shorter line instead of wrong numbers.

Test it without restarting:

```sh
echo '{"model":{"display_name":"Opus"},"workspace":{"current_dir":"'"$HOME"'"},
"context_window":{"used_percentage":23,"context_window_size":200000,
"current_usage":{"input_tokens":45500}}}' | ./statusline.py
```
