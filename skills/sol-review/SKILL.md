---
name: sol-review
description: Cross-family code review by Sol (GPT via the codex CLI) at a code gate — package the change, run Sol read-only, triage its findings into what the session fixes and what Martin decides. Use when the user types /sol-review, says "have Sol review this", or a code gate needs the cross-family pass the product workflow requires.
---

# Sol review

Purpose: same-family models share blind spots, so every code gate gets a second look from the other family. Sol reads a brief and answers; it cannot open files or run anything, so the brief must carry the code.

## 1. Scope

Decide what is under review: the working tree against the last gate (`git diff <last-gate-commit>`), a commit range, or a named set of files. Say the scope in one line before running.

## 2. Write the brief

One markdown file in the session scratchpad. It holds, in this order:

- What the code is for, in three or four plain sentences, and what changed since Sol's last review if there was one.
- What to review for, as a numbered list in priority order: correctness and security first, then data or methodology assumptions, then bugs, dead code, and claims in comments or READMEs that the code does not keep.
- The code itself: the diff, plus the full text of any changed file the diff does not make readable on its own. Sol sees only what is in the brief. If the brief passes about 60k words, split by subsystem and run twice.
- The output format: numbered findings with file and line, severity (blocker, should-fix, nit), a concrete failure scenario, and the fix. Last paragraph: ship or not, and why.

Open with: "You are reviewing code written by a Claude model. Same-family models share blind spots; you are the other family. Lead with problems. No praise. Do not edit files."

## 3. Run

```
codex exec -m gpt-5.6-sol "$(cat <brief path>)" > <brief path>.answer.md
```

If Codex answers with an error (it has returned 404s from its backend before), keep the brief where it is, say so in the session note with the path, and do not close the gate. A gate without the review stays open.

## 4. Triage, because Martin ruled on this (2026-08-30)

Sort every finding into one of two classes before touching anything:

- **Hygiene** (tests, dead code, naming, a plain bug with an obvious fix, doc drift): fix it now, all of it, however small. Real, small, cheap fixes go in; nothing gets parked for "a later pass".
- **Martin's** (data schemas, collection methodology, anything a reader or customer will see or be promised, a security design choice with a product trade-off): do not apply. Put it in front of him with the finding, Sol's reasoning, and your recommendation.

## 5. Report

One table: finding, severity, class, what happened (fixed / yours / rejected with the reason). Then Sol's ship verdict in one line and yours if it differs. The table goes in the message body, never only in tool output.
