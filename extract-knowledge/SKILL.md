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

**Phase 3 — Probe.** Reach for whichever technique fits the concept's grain: **contrast pairs** (two snippets/designs — which is better, and *why*); **artifact critique** (strongest for complex things — a landing page, an essay); and **rapid classification** of a long list of concrete instances (strongest when instances are simple/atomic, where the **rejections** expose the discriminator fast). The "why" — and especially the rejections — reveal the real criteria. Whichever you use, actively hunt **near-misses**: things that *look* like they satisfy the concept but the user rejects — the file's most valuable content. Still no file.

**Phase 4 — Teach-back.** Switch roles: explain the concept *as if teaching a bright 18-year-old with general knowledge but zero domain experience* — fully self-contained, leaning on **none** of this session's shorthand or jargon. (Catching yourself reference in-session context is the tell you're faking understanding.) **This is where the file is created.** Your teach-back *is* the draft — write it straight into `~/.claude/knowledge/<concept>.md` and iterate on the file directly. The user nudges the actual file, not a verbal proxy, so what they approve is exactly what ships.

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

Read `LEARNINGS.md` (this skill's folder) at the start of every run and apply it. After the knowledge file is done, reflect on the *session itself*: did anything teach a reusable lesson — one that would help across *future, different* concepts? Insights specific to today's concept don't count **here** — those belong in the knowledge file. If there is a generalizable process lesson, **route it by kind**:

- **An elicitation heuristic, or a read on how this user's tacit knowledge surfaces** (which technique drew them out, where they stalled) → propose it in one line and, on their confirmation, **append to `LEARNINGS.md`**. The cheap staging area — low stakes, so real lessons get captured.
- **A structural fix to the funnel itself** (a missing phase cue, a better transition) → propose the concrete `SKILL.md` edit and apply it **only on the user's explicit approval**.

**Graduation.** When a staged learning has proven stable across sessions, propose promoting it *into* `SKILL.md` (on approval) and delete it from the log. Keep `LEARNINGS.md` pruned so it stays a staging area, not a changelog that bloats — the active `SKILL.md` is loaded every run, so it must stay lean. Edits that refine the procedure should land *in place*, leaving the file the same length or shorter.

**Hard rules.** Never edit `SKILL.md` without the user's explicit approval — no silent auto-edits, ever. Never write any lesson, to either file, silently; every change is proposed first, and on approval committed from `~/.claude/skills/` with its reasoning as the message (`git log` is the history). Guard against overfitting to one awkward session. A no-op retrospective — "nothing reusable today" — is the common, correct outcome; don't manufacture a lesson.

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
