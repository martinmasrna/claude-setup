# Project knowledge

- `knowledge/` holds current truth: curated facts an agent needs to work correctly (chosen approaches with rationale, constraints, learnings). One fact per file (frontmatter with `name` + `description`, then the body), one-line entry in `knowledge/INDEX.md`. Update entries in place; prune stale ones. Read a body only when its index line is relevant.
- `DECISIONS.md` is the audit trail: append one dated line per non-trivial decision (what + why). Never load it wholesale; it exists so Martin can audit how the project got here.
- Escalate to Martin BEFORE acting on: data schemas or collection methodology, product-visible behavior, external services/dependencies, anything costing money, anything expensive to redo. Everything else: decide autonomously and append it to `DECISIONS.md`; add or update a `knowledge/` entry only when the decision changes current truth that future work depends on.
- Whenever you create or edit a knowledge file, quote its content verbatim in your reply.

@knowledge/INDEX.md
