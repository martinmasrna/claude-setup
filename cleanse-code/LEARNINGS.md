# LEARNINGS

Accumulated, user-ratified heuristics about this user's cleanliness taste and the
cleansing workflow. Read this at the start of every run; apply what's here. Append new
lessons only after the user confirms them (one line each). Prune or correct freely — a
bad lesson is one line to delete. Stable lessons graduate into `SKILL.md` and leave here.

<!-- Format: - [YYYY-MM-DD] <the heuristic>. -->

- [2026-06-21] Prefer guarding an invariant inline at the single point it can actually break over wrapping a normalizer helper around every call site; flag vague names (clean*/normalize*) and field-by-field object rebuilds — pass the validated value straight through, or spread+override only the field the invariant touches.
- [2026-06-21] After the user applies changes by hand, re-verify the actual tree (grep/Read/compiler) before building the next change on it — "done" is often partial, and the missed piece is the one that won't trip typecheck (a new export column, a doc line, a UI-only edit).
