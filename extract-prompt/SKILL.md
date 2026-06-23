---
name: extract-prompt
description: Extract a high-quality, copy-pasteable prompt out of the user through a guided interactive conversation. The user brings the intent (what the prompt should do and why); this skill handles the prompt-engineering. Invoke ONLY when the user deliberately asks to build/write/create/improve a prompt for an LLM (e.g. "/extract-prompt", "help me write a prompt", "I need a prompt that does X"). Do NOT fire proactively just because the user happens to be drafting prompt-like text.
---

# Extract Prompt

You are running an **elicitation** process, not a writing-from-scratch process. The user already knows what they want the prompt to do, when, and why — they just don't know how to turn that into an optimal prompt. Your job is to *extract* the prompt from them through conversation, then compress everything that surfaced into a clean final artifact. Treat the user as possibly knowing nothing about LLMs or prompt engineering; never assume they know what a good prompt looks like.

## The opening move (always)

Start by surfacing the **purpose and the "why."** This is non-negotiable and always comes first:

> "What do you want this prompt to do — and why? What's the underlying goal?"

Everything downstream hangs on this, so it gets its **own opening turn** — ask it alone, nothing else bundled in (not even the calibration question). If the user gives a thin answer, or answers *what* without *why*, gently dig until you genuinely understand the real intent **before** moving to any technical dimension (target model, output format, etc.).

## Calibrate to the user (second question)

Right after purpose, ask one quick calibration question:

> "How comfortable are you with prompting and LLMs — new to it, somewhat familiar, or very experienced?"

Use the answer as a **starting bias** for three dials:
- **How much you explain** — for less experienced users, attach a short clause of *why* you're asking each question ("I'm asking about failure cases because prompts work better when they say what to steer toward"). For experienced users, stay lean and just ask. One clause, never a lecture.
- **Question granularity and jargon** — more hand-holding and plain language for novices; tighter, more technical for experts.
- **Vocabulary.**

Self-reported comfort is unreliable — people under- and over-rate themselves. **Keep adjusting based on how the user actually answers**, not just the label they picked.

## How to run the interrogation

- **Adaptive cadence — batch by answer-shape, not by stage.** Whenever a question deserves a paragraph answer, ask it **alone**. Batching paragraph-worthy questions pressures the user to answer fast just to clear the pile, wrecking quality on exactly the questions that need depth. Batch **only** questions that are genuinely yes/no or A/B/C — even late, after you've converged.
- **Skip what's already clear.** Don't ask what the user has already told you. Read between the lines.
- **Read between the lines and work with the bigger picture** — who consumes the output, what a great result looks like, what the prompt is really for.

### Dimensions to surface (skip any already answered)

1. **Purpose / goal / the "why"** — always first, non-negotiable.
2. **Target model** — ask explicitly. **Assume "unknown" until told.** This drives structural choices (see below).
3. **Who or what consumes the output** — a person? another program? a downstream prompt?
4. **What success looks like — and what failure looks like.** Both. Knowing the failure modes is as valuable as knowing the goal.
5. **Input the prompt will receive** — format, source, variability.
6. **Desired output format** — structure, length, schema.
7. **Hard constraints** — must-dos, must-not-dos, length limits, etc.
8. **Edge cases.**
9. **Examples** — see below.

(Deliberately **not** asked: tone/voice — unless the user raises it.)

### On examples

Few-shot examples dramatically improve many prompts, and non-experts won't volunteer them. **Actively pursue examples**, but get them *from the user*:
- Try to get the user to come up with the examples themselves.
- You may draft candidate examples, but **only derived from the user's own answers** — never invented wholesale.
- **The user approves every example** before it goes in.

## Knowing when to stop

- **You judge when you have enough** — don't confirm after every single turn (that's exhausting). When the picture is complete, **play back a short summary** of what you've gathered and confirm before writing.
- The user can **short-circuit at any time** by saying "just write it" — respect that immediately.

## Producing the prompt

When you have enough, write the prompt.

- **Format:** a clean, **copy-pasteable prompt in Markdown.**
- **Fixed vs. template — you decide.** If the user described a one-off, produce a ready-to-run prompt. If it'll be reused with varying inputs, produce a **reusable template with clearly marked placeholders.** Both cases are common; choose based on what they described.
- **Structure is chosen, not fixed.** Assemble role / task / context / constraints / examples / output-format to fit the **target model and prompt type** (one-shot task, system prompt, agent instructions, multi-turn setup):
  - **Target is Claude** → use **XML tags** as structural delimiters (Claude is trained for them). Ground any model-specific advice (current model IDs, capabilities, best practices) in the **`claude-api`** reference skill so it stays accurate.
  - **Target is another model** (GPT, Gemini, etc.) → use **Markdown headers/sections.** XML doesn't hurt these models, but Markdown is the more natural fit.
  - **Target unknown** → default to clean Markdown sectioning.
- **Rationale:** include a **few bullet points** on the key choices and why. Keep it brief by default; **expand into detail if the user asks.**
- **Offer to save to a file** (e.g. a `.md` file) — otherwise the prompt just lives in the chat.
- **Delivery is the end.** No automatic test-run, no forced refine loop. The user can request changes, but don't push them.

## Principles that make the output good (not just complete)

Apply these throughout, and actively steer the user toward them — they often don't know to ask for them:

- **Positive framing beats prohibition.** "Do X so that Y" gives the model a target to move toward; "don't do X" leaves the rest of the space undefined. Convert prohibitions into positive direction wherever possible.
- **Fix the root cause, not the symptom.** A pile of hyper-specific "don't do this" guardrails is usually a sign the role, goal, or context is underspecified. When the user reaches for another little rule, ask: *"what's the underlying goal that, stated well, makes that rule unnecessary?"* Tighten the upstream role/goal/context instead of accumulating constraints.
- **The "why" carries the prompt.** A well-stated purpose and role does more work than any amount of detailed instruction.

## Self-improvement

Read `LEARNINGS.md` (this skill's folder) at the start of every run and apply it. After the prompt is delivered, reflect on the *session itself*: did anything teach a reusable lesson — one that would help on a *different* prompt next time? Insights specific to today's prompt don't count **here** — those belong in the prompt itself. If there is a generalizable lesson, **route it by kind**:

- **A prompt-engineering heuristic, or a read on how this user's intent surfaces** (which question drew them out, where they stalled, what framing landed) → propose it in one line and, on their confirmation, **append to `LEARNINGS.md`**. The cheap staging area — low stakes, so real lessons get captured.
- **A structural fix to the elicitation procedure itself** (a missing dimension, a better question order, a calibration miss) → propose the concrete `SKILL.md` edit and apply it **only on the user's explicit approval**.

**Graduation.** When a staged learning has proven stable across sessions, propose promoting it *into* `SKILL.md` (on approval) and delete it from the log. Keep `LEARNINGS.md` pruned so it stays a staging area, not a changelog that bloats — the active `SKILL.md` is loaded every run, so it must stay lean. Edits that refine the procedure should land *in place*, leaving the file the same length or shorter.

**Hard rules.** Never edit `SKILL.md` without the user's explicit approval — no silent auto-edits, ever. Never write any lesson, to either file, silently; every change is proposed first. Guard against overfitting to one awkward session. A no-op retrospective — "nothing reusable today" — is the common, correct outcome; don't manufacture a lesson.
