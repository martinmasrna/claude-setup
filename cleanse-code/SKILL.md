---
name: cleanse-code
description: Bring a codebase toward "clean" as defined entirely by the user's personal taste file at ~/.claude/knowledge/clean-code.md — not any generic notion of clean code. A highly interactive, propose-don't-apply audit: it reads the taste file fresh, gathers the code's intent, surfaces only genuine cleanliness issues ranked by how much they move the purity gestalt, and reaches a clean end state *with* the user. Use when the user wants to clean up / tidy / "cleanse" code, judge how clean something is, or improve cleanliness. If the code is already clean, it says so and stops.
---

# cleanse-code

Get a codebase to **clean**, where *clean* means exactly what the user's taste file says it means — nothing more, nothing less. This skill is the interactive process around that judgment; the judgment itself lives in one file.

## Source of truth — read it first, every run

`~/.claude/knowledge/clean-code.md` **is** the definition of clean for this skill. **Read it in full at the start of every run** and treat it as authoritative. Do not lean on a generic "clean code" notion from training data — the user's sense is specific and in places contrary to convention (e.g. what-comments are *dirt*, not care). That file is the spec; this file is only the procedure. If the two ever seem to disagree, the taste file wins.

The orientation below is a map, not a substitute — it exists so you know *which* part of the taste file a moment calls for. Always judge against the file itself.

**Thin orientation (judge against the real file, not this):** clean = the *fittest, least arbitrary* expression of what the code is for, **always relative to context** — nothing is clean in the absolute. Two mental models: **grid vs. maze** (navigability) and **the messy room** (a 0–100% purity gestalt, never pass/fail). Two levels: **tidy** (no arbitrary form or means) → **elegant** (parts fuse into a whole greater than their sum). Optimize for the **human** reader; LLM-clean comes free. The named levers are: (1) one place to change, (2) no useless parts, (3) fewest lines that stay clear, (4) zero-question onboarding, (5) clean module boundaries, (6) room to breathe, (7) self-evident names sized to context, (8) consistency/symmetry, (9) make bad states unrepresentable, (10) one altitude per unit, (11) no hidden side effects. Protect **#1 (one place to change)** and **#3/clarity** hardest when levers conflict. Keystone near-misses to watch for: **what-comments** (narrating what the code does = compensation for code that failed to explain itself) and the **Rube Goldberg / over-engineering** trap (works and looks neat ≠ clean; speculative abstraction and over-defensive guards against impossible states are arbitrary lumps).

## Non-negotiables (these override any instinct to be helpful)

- **Propose, never auto-apply.** No edit happens without the user's explicit approval of that specific change.
- **The user edits, by default.** The user makes the changes *by hand* so they stay in touch with the code. Your job is to describe each change precisely enough that they can apply it themselves. **Only touch files when the user explicitly tells you to do the edits** — and even then, per-change diffs and approval still apply.
- **Highly interactive, not AFK.** Assume an engaged human at the keyboard the whole time who *wants* to be involved in even small calls. Lean on clarifying/specifying questions throughout; do not make context judgments silently.
- **No sycophancy, no busywork.** Never manufacture improvements to look productive. Surface only genuine cleanliness issues grounded in the taste file. Trivial nits that don't move the gestalt are dropped, not listed.
- **"Already clean" is a valid, expected outcome.** If the code is clean, say so plainly and stop. Do not invent work to justify the session.
- **End state:** a clean codebase — *either* because analysis showed it already was, *or* because it got cleaned during the session with the user's sign-off on every change.

## The flow

A loop with hard gates. Announce transitions; never charge past a gate.

### 1. Scope — infer from how you were invoked
- A path named (file or directory) → that path.
- No path, but you're in a repo with a diff (uncommitted changes, or the branch's diff vs. its base) → offer the diff as the scope.
- Otherwise → **ask** what to look at. Don't guess at a whole-repo sweep unasked.

Confirm the scope in one line before reading deeply, so the user can redirect.

### 2. Understand intent (because clean is context-relative)
You **cannot** judge fitness without knowing what the code is *for* — "nothing is clean in the absolute." Read the code, then ask the questions whose answers change the verdict. Especially: *is this edge case actually reachable here?* *does this abstraction have a real second caller, or is it speculative?* *is this name obvious given surrounding context the reader already has?* These are exactly the judgments the Rube Goldberg / over-engineering and context-relative-naming parts of the taste file hinge on — and they're the user's to make, not yours to assume. Don't flag over-defensive code or "redundant" structure as dirt until the user confirms the context that makes it arbitrary.

### 3. Analyze against the taste file
Judge the scope as a **graded gestalt** using the levers and near-misses, with the protected levers weighted hardest. Hunt *genuine* arbitrariness — form, means, or mis-fit to context. Resist two failure modes: manufacturing findings (busywork) and importing generic clean-code dogma the user's file doesn't endorse.

### 4. The clean-already exit
If the scope is already clean (or only has nits not worth a human's time), **say so plainly, name briefly why it reads as clean, and stop.** This is a common correct ending, not a failure.

### 5. Present — one full, ranked list
Show the **complete** list up front, **ranked by purity impact** (biggest needle-movers first); the protected-lever violations naturally surface near the top. Then **stop and wait** — do not start fixing. For each finding:
- **Where**: file:line / the construct.
- **Lever or near-miss**: which part of the taste file it offends.
- **Why it's arbitrary *here***: tied to this code's context, not a generic rule.
- **Proposed change**: concrete and precise enough that the user can apply it by hand. Show the shape of the result, not just a complaint.

### 6. Decide together
Walk the list interactively. The user approves, rejects, or reshapes each item. Discuss; don't rush to consensus. A rejection is data about their taste — absorb it.

### 7. Ripple reasoning (do this for every proposed fix)
Think about the bigger picture before and after each fix:
- **Does this fix unlock a new issue?** If the new issue is fixable and *smaller than* the one that exposed it, add it to the list and handle it too. Cleaning one thing often reveals the next (and can open the higher **emergence** level, where parts start to fuse).
- **Does this fix tip toward a maze?** Guard the other direction: a change that adds indirection before there's a real second caller, or speculative machinery, is the over-engineering near-miss — back it out. Don't chase one-place-to-change into a maze of tiny hops.

### 8. Apply — the user's hands by default
Default: hand the user precise changes and let them edit. Only when the user explicitly says *you* should do it, apply approved changes yourself — one at a time, showing the concrete diff for a final yes before it stays.

### 9. Verify
After edits land (whoever made them), if the project has tests / typecheck / build, run them and report results. Cleanliness must not cost correctness. Skip gracefully if there's nothing to run; never invent a test harness.

### 10. Close
End when the codebase is clean and the user has signed off on every change — or when analysis showed it already was. State the end state plainly.

## Self-improvement

Read `LEARNINGS.md` (this skill's folder) at the start of every run and apply it. At the **end** of a session, reflect: did anything teach a reusable lesson — one that would help on a *different* codebase next time? Observations specific to today's code don't count. If there is one, **route it by kind**:

- **The user's cleanliness taste, or a workflow heuristic** (how they judge, what they reject, what made the session go better) → propose it in one line and, on their confirmation, **append to `LEARNINGS.md`**. This is the cheap staging area — low stakes, so real lessons actually get captured.
- **A structural fix to the procedure itself** (a missing gate, a better step ordering) → propose the concrete `SKILL.md` edit and apply it **only on the user's explicit approval**.

**Graduation.** When a staged learning has proven stable across sessions, propose promoting it *into* `SKILL.md` (on approval) and delete it from the log. Keep `LEARNINGS.md` pruned so it stays a staging area, not a parallel ruleset that rots into a maze.

**Hard rules.** Never edit `SKILL.md` without the user's explicit approval — no silent auto-edits, ever. Never write any lesson, to either file, silently; every change is proposed first. A no-op retrospective ("nothing reusable today") is the common, correct outcome — don't manufacture a lesson. The skills folder is a git repo; that's the audit trail.
