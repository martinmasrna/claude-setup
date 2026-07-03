# LEARNINGS

Accumulated, user-ratified heuristics about this user's cleanliness taste and the
cleansing workflow. Read this at the start of every run; apply what's here. Append new
lessons only after the user confirms them (one line each). Prune or correct freely — a
bad lesson is one line to delete. Stable lessons graduate into `SKILL.md` and leave here.

<!-- Format: - [YYYY-MM-DD] <the heuristic>. -->

- [2026-06-21] Prefer guarding an invariant inline at the single point it can actually break over wrapping a normalizer helper around every call site; flag vague names (clean*/normalize*) and field-by-field object rebuilds — pass the validated value straight through, or spread+override only the field the invariant touches.
- [2026-06-21] After the user applies changes by hand, re-verify the actual tree (grep/Read/compiler) before building the next change on it — "done" is often partial, and the missed piece is the one that won't trip typecheck (a new export column, a doc line, a UI-only edit).
- [2026-07-03] In a mature codebase, residual dirt concentrates in tiny copied util/CLI helpers across sibling files (e.g. `_parse_*` arg validators). Eyeball them, then `grep` the duplicate `def _helper` bodies to confirm byte-identity before proposing — and hoist each into the module that owns the vocabulary it depends on (the shared constant/registry), not a new util module.
