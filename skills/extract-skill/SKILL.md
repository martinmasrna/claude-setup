---
name: extract-skill
description: Extract a well-formed Claude Code skill (a SKILL.md, plus supporting files) out of the user through a guided interactive conversation. The user brings the procedure — what they want done and when; this skill handles the skill-authoring craft: trigger design, cold-readability, progressive disclosure. Invoke ONLY when the user deliberately asks to build/write/create/improve a skill or slash command (e.g. "/extract-skill", "turn this into a skill", "I want a skill that does X", "let's improve my /foo skill"). Do NOT fire proactively just because a task looks repeatable, and do NOT fire for a one-off prompt (that's extract-prompt) or a definition of a fuzzy concept (that's extract-knowledge).
---

# Extract Skill

You are running an **elicitation** process, not a writing-from-scratch process. The user already knows the procedure they want — they've probably done it by hand several times. What they don't know is how to turn it into a skill that fires at the right moment and reads correctly to a cold agent mid-task. Your job is to *extract* the procedure from them, then compress it into a lean `SKILL.md`.

This is the sister skill to `extract-prompt`, `extract-task`, and `extract-knowledge`. The distinguishing difference: a prompt is invoked deliberately by a human who already has the intent in mind, so it can assume its own context. **A skill is invoked by an agent that has to first decide the skill applies, and then follow it while in the middle of something else.** That forces two things a prompt never needs: a trigger contract, and instructions that survive being read cold, out of order, with no session history.

## First, check it should be a skill at all

Before eliciting anything, test the premise — and say so plainly if it fails:

- **A one-off ask** → not a skill. Route to `extract-prompt` (reusable text) or `extract-task` (just do it).
- **A definition of taste or a fuzzy concept** ("what I mean by clean code") → not a skill. Route to `extract-knowledge`.
- **A rule that should apply always, unconditionally** → belongs in `CLAUDE.md`, not a skill. Skills load conditionally; if it must never be missed, don't gate it behind a trigger.
- **A deterministic automation that must run on every X** ("always run the linter after editing") → belongs in a **hook** in `settings.json`. The harness executes hooks; skills only advise the model, so a skill can be skipped.
- **A specialized long-running worker with its own context** → likely a **subagent** (`.claude/agents/*.md`) rather than a skill.
- **A procedure whose real content is a script** → the skill may be a thin wrapper around a committed script; say so, and keep `SKILL.md` to when-and-how-to-run.

A skill is the right shape when the work is a **procedure or body of guidance**, applied **sometimes**, that the model should follow **using judgment**. If it's borderline, say which way you lean and why, and let the user decide.

## Investigate before you interrogate

You're in a live environment — use it. Before asking anything beyond the opening "why":

- **Read the existing skills** (`~/.claude/skills/`, and `.claude/skills/` in the project). You need them for three reasons: **collision** (does this overlap an existing skill's trigger?), **house style** (match the user's established voice and structure), and **reuse** (does this belong as a section in an existing skill instead of a new one?).
- **Read `CLAUDE.md`.** Anything already stated there is global — don't restate it in the skill.
- **Mine the session and the repo for the worked example.** Skills are usually born from work just done by hand. If the procedure was performed in this session or is visible in recent commits/files, reconstruct the actual steps from that and bring them back as a draft to correct — far better than asking the user to recite from memory.

**Never ask what you could have found by reading.** Reserve questions for what only the user knows: why the procedure exists, the judgment calls inside it, what a bad run looks like, and when it must *not* fire.

## The opening move (always)

Surface **purpose and the "why"** first, on its **own opening turn**, nothing bundled with it:

> "What do you want this skill to do — and why? What goes wrong today without it?"

"What goes wrong today" is the load-bearing half. It surfaces the failure the skill exists to prevent, which is what lets a future agent generalize instead of pattern-matching your rules.

## Calibrate (second turn)

> "Is this a procedure you already run by hand — one you could walk me through a real instance of — or a standard you want enforced that doesn't have concrete steps yet? And should it live in your personal `~/.claude/skills/` or in this project's `.claude/skills/`?"

- **Practiced vs. aspirational.** Practiced → mine them hard for the real steps and the exceptions; a walkthrough of one real run is worth an hour of abstract questions. Aspirational → you'll be co-designing the procedure, so expect to propose structure and have them correct it.
- **Personal vs. project.** Personal skills can assume the user's habits and machine. Project skills are read by teammates and other agents, so they must be self-contained and conventions-explicit. Default to personal if unstated; confirm before writing.

## How to run the elicitation

- **Adaptive cadence — batch by answer-shape, not by stage.** Any question deserving a paragraph gets asked **alone**. Batch **only** genuine yes/no or A/B/C questions.
- **Skip what's already clear or discoverable.**
- **Draft-and-correct beats open questions** for procedure steps. Once you have the shape, write the steps as you understand them and let the user attack the draft. People correct a wrong step instantly and describe a right one badly.

### Dimensions to surface (skip any already clear)

1. **Purpose / the failure it prevents** — always first, non-negotiable.
2. **The trigger** — when should this fire? Get **concrete phrasings** the user would actually type, and the situations where it should fire *without* being named.
3. **The anti-trigger** — when must it *not* fire? Equally important, and never volunteered. Every over-eager skill in existence is missing this.
4. **The procedure** — the real steps, in order, including the ones they'd call obvious.
5. **Judgment points** — where the agent must decide rather than follow, and what to weigh. This is what separates a skill from a script.
6. **What a bad run looks like** — the specific wrong output or wrong behavior. Then decide whether to state it as an explicit anti-pattern or fix it upstream (see principles).
7. **Stopping condition** — when is the skill done? What does it hand back, and to whom?
8. **Inputs and environment** — files, tools, commands, credentials, external services the skill needs; whether it should read or write anything.
9. **Supporting material** — scripts, templates, reference docs, examples. Ask what the procedure needs *at hand* versus what can be described.
10. **Examples** — actively pursue them, *from the user*. You may draft candidates derived from their own answers; the user approves every one before it goes in.

## Knowing when to stop

**You judge when you have enough** — don't confirm after every turn. When the picture is complete, **play it back and get a go-ahead before writing**:

> **What it does:** <the procedure, in your own words>
> **When it fires / doesn't fire:** <trigger and anti-trigger>
> **Where it lives:** <path>
> **Files I'll create:** <SKILL.md, plus anything else>
>
> Give me the go-ahead and I'll write it.

The user can approve, correct, or short-circuit ("just write it") at any point — respect a short-circuit immediately.

## Writing the skill

Create `<skills-dir>/<kebab-case-name>/SKILL.md` with YAML frontmatter (`name`, `description`).

**The description is the whole trigger contract.** Until the skill fires, the description is the *only* part of it in context — the body is never seen. So it must do all the discovery work by itself, in third person:

- Say what the skill does **and** what it produces.
- Include **realistic trigger phrasings**, including the slash-command form.
- Include the **anti-trigger** explicitly (`Do NOT fire when…`). Match the phrasing to the sibling skills that could steal or leak the trigger.
- Write it for a model deciding under uncertainty, not for a human reading a catalog.

**Write the body for a cold agent mid-task.** It has no memory of this conversation and is halfway through unrelated work when the skill loads.

- **Motivation before mechanics.** Open with what the skill is for and what failure it prevents. That's what lets the agent handle a case your steps didn't anticipate.
- **Imperative procedure, not prose about the procedure.** Second person, direct instruction. Cut anything the agent can't act on.
- **Make judgment explicit.** Where the agent must decide, say what to weigh and what the default is. Where there's no judgment, say "always" or "never" and mean it.
- **Positive framing beats prohibition.** "Do X so that Y" gives a target; "don't do X" leaves the rest of the space undefined.
- **Fix the root cause, not the symptom.** A pile of narrow "don't do this" rules means the purpose or role is underspecified. When the user reaches for another little rule, ask what upstream statement would make it unnecessary.
- **Don't restate general good behavior.** No "be helpful," no "write clean code," nothing already in `CLAUDE.md`. Every line must be something the agent wouldn't already do.
- **Progressive disclosure.** `SKILL.md` is loaded in full every time it fires, so keep it lean and push bulk into sibling files the skill points to on demand — `references/<topic>.md` for lookup material, `scripts/` for executable steps, templates for output shapes. Reference them by relative path with a one-line note on *when* to read each.
- **State the stopping condition** so the skill doesn't run forever or hand back half a result.

**Self-improvement scaffolding — judge per skill, default yes.** For a procedural or taste-bearing skill whose process will keep evolving, add a `LEARNINGS.md` staging file and a short self-improvement stub pointing at the shared protocol in `../_shared/self-improvement.md` (mirror the block at the bottom of this file: start-of-run `LEARNINGS.md` read, pointer to the shared file, and a couple of domain-specific examples). For a thin mechanical skill, skip it. State the call so the user can override.

**Delivery is the end.** Report the paths you created and the key authoring choices in a few bullets — expand only if asked. No automatic test run, no forced refine loop. **Offer** to commit with the reasoning as the message; never commit silently — and mind *which* repo the commit lands in: a personal skill goes into `~/.claude/skills/`'s own git history (low stakes, just yours), while a project skill under `.claude/skills/` commits into the **project** repo, where it's a team-visible change. Say which repo you're about to touch and confirm before committing into a project.

## Revisit path (improving an existing skill)

If a skill for this already exists — the user names it, or you find a close match while investigating — **read it first**, then say where you're starting and why:

- Assess what's already sound, what's stale, and what's missing. Don't restart the elicitation from the opening "why" when the file already answers it.
- Enter at the shallowest dimension that's actually unresolved. Often the file's procedure is fine and only the trigger is wrong, or vice versa — fix that and stop.
- **Edit in place.** A refinement should leave the file the same length or shorter; `SKILL.md` is loaded on every run, so growth has a real cost. If it's genuinely outgrowing itself, propose splitting bulk into a `references/` file rather than letting the body sprawl.
- If the right fix is *deleting* the skill, or folding it into another, say so.

## Self-improvement

At the start of every run, read `LEARNINGS.md` (this skill's folder) and apply it. After the skill is delivered, run the retrospective — the mechanism and guardrails (route-by-kind, graduation, and the hard rules on never editing/writing without approval) live in `../_shared/self-improvement.md`; **read it before writing to either file.** Skill-specific:

- **Reusable means** it would help on a *different skill* next time; anything specific to today's skill belongs in that skill itself.
- **A good staged learning here:** a skill-authoring heuristic, or a read on how this user's procedures surface — which question exposed the anti-trigger, where a draft-and-correct beat asking, where they stalled.
