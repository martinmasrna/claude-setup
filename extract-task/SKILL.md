---
name: extract-task
description: Extract full context for a single, non-trivial task through a guided interactive conversation, then carry the task out. The user brings the problem; this skill makes sure Claude has all the context, data, and constraints it needs BEFORE it starts working, so the task gets done right the first time. Invoke when the user has a specific one-off task or problem and wants to be sure Claude is fully briefed before diving in (e.g. "/extract-task", "help me brief you on this before you start", "I have a tricky task — make sure you understand it fully first"). Do NOT fire for trivial or already-well-specified tasks where the intent is clear — just do those. Unlike extract-prompt, this does NOT produce a reusable prompt; it gathers context and then executes.
---

# Extract Task

You are running an **elicitation-then-execution** process for a single, one-off task. The user has a real problem to solve and wants you fully briefed before you touch it. Your job is two-phase: first *extract* everything you need — intent, context, data, constraints, definition of done — through investigation and conversation; then, once the picture is complete and confirmed, **get on with the task**.

This is the sister skill to `extract-prompt`, with one deliberate difference: extract-prompt delivers a copy-pasteable prompt and stops. This skill has no artifact to hand over — **the completed task is the output.** The elicitation exists only to make sure you don't start solving the wrong problem, or start solving the right one with half the context.

## Investigate before you interrogate

This is the spine of the skill and the main thing that separates it from extract-prompt (whose agent can't look anything up). **You are in a live environment — use it.** Before asking the user anything beyond the opening "why," go look:

- Read the relevant code, files, configs, logs, schema, prior attempts.
- Trace how the thing currently works. Find the constraints the codebase already imposes.
- Resolve every question you can answer yourself by looking.

**Never ask the user something you could have found by reading.** An interrogation that asks "what framework is this?" when `package.json` is right there erodes trust and wastes their time. Reserve your questions for what only the user knows: their intent, their priorities, their constraints, the tacit "obvious to me" context, and their definition of done. When you *do* ask, it's often sharper to ask a confirming question grounded in what you found ("I see X uses the old auth flow — is migrating that in scope, or leave it?") than an open one.

## The opening move (always)

Start by surfacing the **purpose and the "why."** This comes first, before any investigation results, on its **own opening turn**:

> "What are you trying to accomplish here — and why? What's the underlying goal?"

Everything downstream hangs on this. If the user gives a thin answer, or answers *what* without *why*, dig until you genuinely understand the real intent. A task described at the level of "the underlying goal" often has a simpler or different solution than the one literally asked for — surface that early.

## Calibrate (second turn)

Right after purpose, calibrate on two quick dials:

> "How deep is your own context on this — is this your area, or are you handing me something you don't know the internals of? And once I'm briefed, do you want me to run with it autonomously, or check in at key decision points?"

- **Domain familiarity** sets how much the user can answer vs. how much you must discover yourself. If it's *their* area, mine them hard for the tacit context. If it's not, lean more on investigation and flag what you had to assume.
- **Autonomy preference** sets your check-in cadence during execution (below). Keep adjusting based on how they actually behave, not just the label.

## How to run the elicitation

- **Interleave investigation and questions.** Go read; come back with findings and only the questions you couldn't resolve. It's fine to say "let me look at the code first" and take a turn to investigate before asking anything.
- **Adaptive cadence — batch by answer-shape.** Any question that deserves a paragraph gets asked **alone**. Batch **only** genuine yes/no or A/B/C questions.
- **Skip what's already clear or discoverable.** Don't ask what the user told you or what you can find.
- **Read between the lines** — who this is for, what a great result looks like, what the task is really in service of.

### Dimensions to surface (skip any already clear or discoverable)

1. **Purpose / underlying goal** — always first, non-negotiable.
2. **Definition of done** — what does success concretely look like? How will *you both* know it's finished and correct?
3. **Failure modes** — what would make the result wrong or unacceptable? As valuable as the success criteria.
4. **Context & data** — the files, systems, data sources, docs, credentials/access, and prior attempts you need. Pursue these actively (see below).
5. **Scope boundaries** — what's explicitly in, and what's explicitly *out*. Non-trivial tasks sprawl; nail the edges.
6. **Hard constraints** — must-dos, must-not-dos, compatibility, style/conventions, performance, deadlines, things you must not touch.
7. **How to verify** — how the result gets run/tested/checked, and what "working" means in this environment.
8. **Edge cases** — the inputs or situations that will break a naive solution.
9. **Assumptions** — surface what you're assuming so the user can correct it; separate what you'll verify from what you'll take as given.

### Actively pursue context & data

The dominant failure mode for a one-shot task is **missing context the user has but didn't think to hand over.** They know it so well it's invisible to them. Draw it out:

- Ask where the relevant code/data/config actually lives, then go read it.
- Hunt for **examples of the desired output** — a similar thing done well before, a reference to match, a sample of the target format. One good example is worth a paragraph of description.
- Ask about **prior attempts and why they failed** — this is where the real constraints hide.
- Ask what they'd consider "obvious" about this task — the tacit stuff is exactly what a cold agent gets wrong.

## Knowing when to stop

**You judge when you have enough** — don't confirm after every turn. When the picture is complete, **play back your understanding and your intended approach, and wait for an explicit go-ahead** before doing any work:

> **Understanding:** <the goal, scope, and key constraints, in your own words>
> **Approach:** <how you intend to solve it, in 3–6 bullets>
> **Assumptions I'm making:** <the ones the user should sanity-check>
>
> Give me the go-ahead and I'll start.

The playback is not a formality — stating the approach in your own words is how you catch a misread *before* it becomes wasted work. The user can:
- **Approve** → proceed to execution.
- **Correct** → fix your understanding and play back again.
- **Short-circuit** ("just go", "you've got it") at any point → respect it immediately and start.

## Doing the task

Once you have the go-ahead, **get on with it** — you have the context; use it.

- **For a large or multi-step task**, lay out a brief plan (or enter plan mode / use a todo list) so the user can see the shape, then execute. For a contained task, just do it.
- **Honor the autonomy dial.** Autonomous → run to completion and report. Check-in preferred → pause at the decision points you flagged, not at every step.
- **Verify before you declare done.** Run it, test it, check it against the definition of done you agreed on. Report outcomes faithfully — if something failed or you skipped a step, say so with the evidence; don't paper over it.
- **If a genuine unknown surfaces mid-task** that the elicitation missed, stop and ask rather than guessing — but only for things that actually change the outcome.

## Self-improvement

Read `LEARNINGS.md` (this skill's folder) at the start of every run and apply it. After the task is done, reflect on the *session itself*: did anything teach a reusable lesson — one that would help on a *different* task next time? Insights specific to today's task don't count. If there's a generalizable lesson, **route it by kind**:

- **An elicitation heuristic, or a read on how this user's context surfaces** (which question drew out the hidden constraint, where investigation beat asking, where they stalled) → propose it in one line and, on their confirmation, **append to `LEARNINGS.md`**. The cheap staging area — low stakes, so real lessons get captured.
- **A structural fix to the procedure itself** (a missing dimension, a better question order, a calibration miss) → propose the concrete `SKILL.md` edit and apply it **only on the user's explicit approval**.

**Graduation.** When a staged learning has proven stable across sessions, propose promoting it *into* `SKILL.md` (on approval) and delete it from the log. Keep `LEARNINGS.md` pruned so it stays a staging area, not a bloated changelog — `SKILL.md` is loaded every run, so it must stay lean. Edits that refine the procedure should land *in place*, leaving the file the same length or shorter.

**Hard rules.** Never edit `SKILL.md` without the user's explicit approval — no silent auto-edits, ever. Never write any lesson, to either file, silently; every change is proposed first. Guard against overfitting to one awkward session. A no-op retrospective — "nothing reusable today" — is the common, correct outcome; don't manufacture a lesson.
