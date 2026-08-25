# Headquarters — Spec

Core functionality and user scenarios for v0.001. This file grows as decisions settle; nothing speculative goes in. The product-level why lives in `CONCEPT.md`.

## User scenarios

1. **The morning turn.** Martin sits down and opens headquarters. In one glance he sees: every active project with its workflow phase, a one-line state, and what it's waiting on; the queue of judgments ready for him; and a plain-language digest of what got built since his last visit. He plays through the queue and is done — no patrolling files or apps.
2. **Playing a queue item.** Each queue item names the judgment being asked (a document ready for a redline pass, a decision to approve or reject, a sample to inspect, a milestone to grade) and deep-links into the right file or tool — documents open in the redline editor. A judged item leaves the queue.
3. **The between-sessions glance.** During the day, headquarters answers "did anything change, does anything need me?" in seconds — what needs attention stands out, everything healthy stays quiet.

## Core functionality

- **Project registry** — every active project, its phase in the product workflow, current state, and gate markers (blocked by / waiting on).
- **Judgment queue** — the list of items waiting for Martin's judgment, each with the ask and a deep link. {==Agents file items; the workflow's gates are the main source.==}{>>can't even re-wrtie this because I have no clues what it means :D<<}
- **Change digest** — what got built since Martin's last visit, per project, written for a human, not a commit log.
- **Deep links** — any document opens directly in the redline editor; other custom tools are reachable the same way as they come to exist.
- **Live state** — headquarters reads the actual current state of the company; it is never a stale copy{++, and it's not  a progress log full of diary entries++}.

## Out of scope for v0.001

Socials, clients, newsletter, calendar, metric integrations, talking to agents from inside headquarters (unless it turns out trivially cheap).
