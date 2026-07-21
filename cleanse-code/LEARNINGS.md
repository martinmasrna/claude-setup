# LEARNINGS

Accumulated, user-ratified heuristics about this user's cleanliness taste and the
cleansing workflow. Read this at the start of every run; apply what's here. Append new
lessons only after the user confirms them (one line each). Prune or correct freely — a
bad lesson is one line to delete. Stable lessons graduate into `SKILL.md` and leave here.

<!-- Format: - [YYYY-MM-DD] <the heuristic>. -->

- [2026-06-21] Prefer guarding an invariant inline at the single point it can actually break over wrapping a normalizer helper around every call site; flag vague names (clean*/normalize*) and field-by-field object rebuilds — pass the validated value straight through, or spread+override only the field the invariant touches.
- [2026-06-21] After the user applies changes by hand, re-verify the actual tree (grep/Read/compiler) before building the next change on it — "done" is often partial, and the missed piece is the one that won't trip typecheck (a new export column, a doc line, a UI-only edit).
- [2026-06-26] Before unifying duplicated validators/error-mappers, check whether the tests assert on error-message *text* or only on status codes — if only status codes, message unification across the merged copies is free (no test edits), which de-risks the consolidation.
- [2026-07-03] In a mature codebase, residual dirt concentrates in tiny copied util/CLI helpers across sibling files (e.g. `_parse_*` arg validators). Eyeball them, then `grep` the duplicate `def _helper` bodies to confirm byte-identity before proposing — and hoist each into the module that owns the vocabulary it depends on (the shared constant/registry), not a new util module. Corollary: when the duplicated computation is a value's own semantics (e.g. per-record win/draw credit) and one copy is already a named helper others ignore, prefer a method on the value type over a free helper in an arbitrary module.
- [2026-07-11] In experiment/research codebases, config flags that appear only ever set to their default (never flipped) are usually abandoned A/B scaffolding — grep the whole tree (src + tests + tooling) for any non-default assignment to confirm they're dead, and confirm with the user before removing, since they may be hand-toggled levers. Mirror-image guard: before calling apparent dead code dead (an unused-looking bot `depth`/`staged` path), grep for real callers first — "validated negative result" knobs and comparison-control paths are often deliberately retained.
