# Product workflow

Step-by-step workflow for building products. Each phase ends with a concrete artifact and a named judge — a phase is not done until its gate passes. Every project's current phase is tracked in `PROJECTS.md`.

## (1) Brainstorm
- What is the "True Name", the "Big Idea" of the product?
- Who is it for? What problem does it solve?
- What would make it exceptional? What would make it average?
- Work from first principles, on a conceptual level; ignore technicalities completely.
- Mostly done as an extraction session: the agent asks the human an exhaustive amount of product-level questions. The vision lives in the human's head — the agent's job is to get it out, not to invent it.

**Ends with:** a one-page concept document.{~~ Judge:~>

**Judge:**~~} human (redline pass).

## (2) Documentation
- Set up the standard doc structure{-- (as proven in game-of-youtube)--}: `ROADMAP.md` (settled decisions), `DESIGN.md` (why they are settled), `TODO.md` (short- and long-term tasks), journal + `FINDINGS.md` added once there is evidence to record.
- The spec covers core functionalities and user scenarios only. It grows over time; it does not try to be complete on day one. Agents treat every sentence in it as settled truth, so nothing speculative goes in.

**Ends with:** spec + roadmap.{~~ Judge:~>

**Judge:**~~} human (redline pass).

## (3) Data
- Crucial step, foundation of everything. Dig deep, put a lot of effort into getting this right.
- Work from the settled principles and the written spec.
- Define what the data actually is: entities, fields, where it comes from, what can go wrong with it.

**Ends with:** a mock-up dataset realistic enough to build and design against.{~~ Judge:~>

**Judge:**~~} human inspects a sample.

## (4.A) Core backend logic
- Data layer + API schema.
- The API schema is derived from the mock dataset and the spec's user scenarios — the API serves the product, not the other way around.

**Ends with:** working data layer + API against mock data, with tests.{~~ Judge:~>

**Judge:**~~} agent (tests + cross-model review); product-level decisions promoted to human.

## (4.B) Collecting / creating real data
- Runs in parallel with 4.A and 4.C.

**Ends with:** real dataset passing the same shape and sanity checks as the mock.{~~ Judge:~>

**Judge:**~~} human inspects a sample.

## (4.C) Design exploration
- Work from first principles based on steps (1) and (2).
- Diverge first: several cheap, throwaway visual directions (static mockups, mock data — hours each, not days). Human kills and picks. Only then converge on the surviving direction. Iterating on the first direction an agent happens to produce means the rest were never seen.
- Either Claude Design, or straight into Claude Code with mock data.

**Ends with:** a style guide for the project.{~~ Judge:~>

**Judge:**~~} human{++ (redline pass)++}.

## (5.A) Full frontend implementation
- Component layout, full UI/UX design.
- Work from product spec and style guide.
- Done in Claude Code, iteratively, human in the loop — small increments the human can judge in minutes, no overnight leaps in this phase.

**Ends with:** full UI running on real data, every screen approved.{~~ Judge:~>

**Judge:**~~} human.

## (5.B) Full backend implementation
- Work from product spec and existing real data.
- Autonomous Claude Code session; agent asks only product-level questions.
- Plan the session, break into small checkpointed chunks, write tests for each.
- At the end, full code review by a cross-family model (Claude reviewing ChatGPT or the other way around) → feedback to the original coding agent → accept or reject each finding.
- Product-level decisions promoted for human review.

**Ends with:** tests green + cross-model review closed out.{~~ Judge:~>

**Judge:**~~} agent; decision log to human.

## (6) Testing and iteration
- Human provides product-level decisions and visual/UI/UX taste; agents handle coding, test suite, data management, everything technical they're great at.
- Runs in rounds: each round starts from the human using the product and reporting what's wrong, and ends with a fixed build the human checks again.

**Ends with:** human uses the product for its real purpose without hitting anything broken or embarrassing.{~~ Judge:~>

**Judge:**~~} human.

## (7) Infrastructure & deployment

**Ends with:** product running in its real environment; one command (or none) to keep it running.{~~ Judge:~>

**Judge:**~~} agent verifies, human confirms.

## (8) Retro
- Short pass after the project (or after any big phase on a training-ground project): what did the workflow itself get wrong?
- Amend this file, or make no change. The workflow only stays trustworthy if it gets corrected after real use.

**Ends with:** this file updated or explicitly left as is.{~~ Judge:~>

**Judge:**~~} human.
