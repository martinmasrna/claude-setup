# Self-improvement protocol (shared)

Single source of truth for how the elicitation/procedure skills capture lessons and evolve. A skill's own `## Self-improvement` section names the domain, gives concrete examples of a good staged learning, and says how to locate its folder if the session isn't running from it. Everything about **mechanism and guardrails** lives here. **Read this file before writing to any `LEARNINGS.md` or `SKILL.md`.**

## The retrospective

At the **end** of the run, reflect on the *session itself*: did anything teach a **reusable** lesson — one that would help on a *different* instance of this skill's work next time? Insights specific to *this* run's artifact don't count here — those belong in the artifact itself, not in the skill's memory.

A no-op retrospective — "nothing reusable today" — is the common, correct outcome. Don't manufacture a lesson to justify the section.

## Route the lesson by kind

- **A domain heuristic, or a read on how this user surfaces things** (what drew them out, where they stalled, what framing landed — the skill's section gives domain-specific examples) → propose it in one line and, on the user's confirmation, **append to `LEARNINGS.md`**. This is the cheap staging area — low stakes, so real lessons actually get captured.
- **A structural fix to the procedure itself** (a missing step, a better ordering, a calibration miss) → propose the concrete `SKILL.md` edit and apply it **only on the user's explicit approval**.

## Graduation

When a staged learning has proven stable across sessions, propose promoting it *into* `SKILL.md` (on approval) and delete it from the log. Keep `LEARNINGS.md` pruned so it stays a staging area, not a changelog that bloats — the active `SKILL.md` is loaded in full on every run, so it must stay lean. Edits that refine the procedure should land *in place*, leaving the file the same length or shorter.

## Hard rules

- Never edit `SKILL.md` without the user's explicit approval — no silent auto-edits, ever.
- Never write any lesson, to either file, silently; every change is proposed first.
- Guard against overfitting to one awkward session.
- The skills folder is a git repo — that's the audit trail. On approval, offer to commit the change from `~/.claude/skills/` with the reasoning as the message; never commit silently.
