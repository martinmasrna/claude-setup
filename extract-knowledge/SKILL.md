---
name: extract-knowledge
description: Guided elicitation process that turns the user's tacit, hard-to-articulate understanding of a fuzzy concept (e.g. "clean code", "premium design", "deep explanation") into a cold-readable markdown file for future LLM agents. Use when the user wants to capture, externalize, document, or "extract" their intuitive definition/taste/standard for some concept, or to build/update an entry in their personal knowledge base at ~/.claude/knowledge/. Trigger phrases: "extract my understanding of X", "let's define what I mean by X", "capture my taste for X", "add X to my knowledge base".
---

# Extract Knowledge

A guided process for converting the user's **tacit** knowledge — things they understand intuitively but can't easily state — into a precise markdown artifact that a *future, cold-start LLM agent* can act on. The user is the source of truth; you are the interviewer, then the scribe, then the student who must teach it back correctly.

## The core idea

The user knows what they mean by a fuzzy concept; they just can't write it down. Direct questions ("define clean code") yield generic answers. Tacit knowledge comes out **sideways** — through judgment, contrast, and correction. So you run a funnel that progressively *inverts who is talking*: it starts with them explaining and ends with **you** explaining while they correct you. By the time you can teach it back without correction, you have already written the artifact.

The output is **not for a human and not for this conversation** — it is for an agent two weeks from now with zero memory of this session. Optimize every word for that reader.

## The funnel

You drive the progression. When a phase feels exhausted, **announce the transition and propose moving on** — the user can approve, hold you in the current phase, or jump you ahead at any time. Never advance silently.

**Phase 1 — Open.** Broad, open-ended, Socratic questions. The user writes a lot; you mostly listen and probe. Ask "why does that matter?" and ladder down toward bedrock — this is where you surface the **motivation**: why the concept exists, what problem it solves, where it came from. No file exists yet.

**Phase 2 — Narrow.** Your questions sharpen; their answers shorten. You are triangulating specific criteria, not gathering prose. Still chat-only, no file.

**Phase 3 — Probe.** Introduce **contrast pairs** (two snippets / designs / explanations — ask which is better and *why*) and **artifacts to critique**. The "why" reveals the real criteria. Actively hunt **near-misses**: things that *look* like they satisfy the concept but the user rejects. Near-misses are the highest-value content for the file because they expose the discriminator. Still no file.

**Phase 4 — Teach-back.** Switch roles: you now explain the concept *as if teaching someone who doesn't get it yet*. **This is where the file is created.** Your teach-back *is* the draft — write it straight into `~/.claude/knowledge/<concept>.md` and iterate on the file directly. The user nudges the actual file, not a verbal proxy, so the thing they approve is exactly the thing that ships.

**Phase 5 — Converge.** Repeat teach-back, refining the file, until the **user** declares 100% alignment. The exit is always the user's call — never declare done yourself.

**Phase 6 — Retrospective (self-improvement).** After the knowledge file is done, reflect on the *session itself* and improve this skill. See the section below.

## Why the file is created only at Phase 4

Editing a file in place causes anchoring — you patch existing structure instead of rethinking. That is poison early, when ideas are still divergent. So Phases 1–3 stay in fluid chat with no file. The instant you switch from *asking* to *teaching* (Phase 4), the artifact appears and becomes the workbench. The hand-off point is the mode switch.

## Output file principles

Write the file for a cold agent on a context budget. **As long as necessary, no longer** — be mindful of bloat; this will be loaded into a future context window.

- **Motivation before mechanics.** Lead with the *why*: what problem the concept solves, the context it lives in, when an agent should reach for it, and how it came to be. This first-principles layer lets a future agent *generalize* to unseen cases instead of mechanically pattern-matching rules. It is not optional throat-clearing — it is the part that makes the rules transferable.
- **Principle-first.** State each abstract criterion in your own words, as the primary content. Examples illustrate principles; they never define them.
- **Cage the examples.** A known failure mode: LLMs latch onto an example's *surface features* (language, domain, variable names) and miss the principle. Prevent it: subordinate every example to a stated principle, and annotate it — *"What this shows: …  What's incidental: …"* — so the future agent knows where to look and what to ignore.
- **Include near-misses.** For key principles, add a counter-example that **shares surface features but violates the principle**. This forces the discriminator into the principle, where it belongs, because the surface can't tell the two apart.
- **Anchor everything.** Every abstract criterion gets ≥1 concrete example that the user explicitly endorsed during the session. No free-floating maxims.
- **Dissent log.** End the file with a short section capturing anything left unresolved and any point where the user overrode your instinct. Future agents benefit from knowing the soft spots, not just the settled doctrine.

## Self-improvement (Phase 6 retrospective)

After each session, improve this skill — but in a way that makes it *sharper*, never *bloated or drifted*. The skills folder (`~/.claude/skills/`) is a git repo; that is the audit trail and the rollback mechanism, so the skill file itself stays lean.

**What qualifies as a lesson.** Only **generalizable process** insights — something that would help across *future, different* concepts. "The contrast pairs in Phase 3 worked better when I built them from the user's own examples" qualifies. Anything specific to today's topic does **not** — that belongs in the knowledge file, not here. When in doubt, it does not qualify.

**Guard against the failure modes.** Do not encode noise from a single awkward session (overfitting). Do not append a growing changelog or pile on caveats (bloat) — the active `SKILL.md` is loaded into context every run, so edits must *refine existing instructions in place*, leaving the file the same length or shorter. Do not silently rewrite your own process (drift): every change is proposed first and committed with its reasoning.

**The loop:**
1. Reflect honestly: what worked, what fought you, what you'd do differently.
2. If (and only if) there is a generalizable lesson, draft the specific `SKILL.md` edit as a **diff** and present it to the user with a one-line rationale.
3. **The user approves before anything is written.** No approval, no change. (Same principle as the knowledge file: verify the exact thing that ships.)
4. On approval, apply the edit and `git commit` from `~/.claude/skills/` with the lesson as the commit message (e.g. `extract-knowledge: build Phase 3 contrast pairs from the user's own examples`). The reflection lives in the message; `git log` is the history.
5. If there is no worthwhile lesson, say so and commit nothing. A no-op retrospective is the common, correct outcome.

## Lifecycle

- **One session = one concept = one file**, unless the user explicitly says otherwise.
- Files live in `~/.claude/knowledge/<concept>.md` (kebab-case filename).
- **On revisit:** if a file for the concept already exists, read it first, assess how complete and correct the current understanding is, and **jump into the funnel at the matching phase** rather than restarting from Phase 1. Tell the user where you're starting and why.

## Suggested file structure

Adapt per concept; don't force a rigid template. A reasonable default:

```markdown
# <Concept>

> One-sentence operational definition — what this concept means to the user, in their sense of it.

## Motivation
Why this concept matters and the problem it solves. The context it lives in —
when an agent needs it, how it gets used, and why. Where it came from / how it
came to life, if that illuminates the big picture. This is the first-principles
"why" that everything below should trace back to.

## Principles
### <Principle 1>
<statement in plain terms>

**Example (endorsed):**
<concrete artifact>
- What this shows: <the load-bearing point>
- What's incidental: <surface features to ignore>

**Near-miss (rejected):**
<look-alike that violates the principle>
- Why it fails: <the discriminator>

### <Principle 2>
...

## Dissent log
- <unresolved point or user override>
```

## Starting a session

1. Confirm the concept and check `~/.claude/knowledge/` for an existing file.
2. If none, begin Phase 1. If one exists, read it, assess, and jump to the right phase.
3. Drive the funnel, announcing each transition. Let the user steer.
