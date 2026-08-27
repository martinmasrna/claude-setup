# Product workflow

Step-by-step workflow for building products. Each phase ends with a concrete artifact and a named judge — a phase is not done until its gate passes. Every project's current phase is tracked in `PROJECTS.md`, and only there.

The core of every phase is the same five steps:{++

1)++} {~~f~>F~~}rame the question {++
1. ++}{--→ --}{~~b~>B~~}uild the smallest artifact that answers it{-- → --}{++
1. ++}{--c--}{++C++}heck it mechanically{-- → --}{++
1. ++}{--j--}{++J++}udge it by using it{-- → --}{++
1. W++}{--w--}rite the verdict into the settled docs. {++
1. 
++}The numbered phases below are the standard version of th{~~at~>e workflow~~} for software products; other project types (content, client work) assemble their own phase list from the same pieces.

## Two kinds of work

Every piece of work is one of two kinds, and each kind runs differently:

- *{~~*~>a) ~~}Delivery work** — the right answer is already settled (a schema is defined, a spec exists); analysis and skill get there. Runs as: settled brief → agent builds → artifact judged at the gate.
- *{~~*~>b) ~~}Discovery work** — nobody knows the answer yet (a new interaction loop, what a product should feel like, taste in general); only cheap tries and reactions reveal it. Runs as: write a decision card first (the question, what evidence would answer it, the stop-rule, what happens to the artifact — default: delete it, keep the verdict) → build a small cheap try → write down the verdict → next try.

Pushing discovery work through delivery machinery is how {==nine rounds of design exploration produced nothing: one big artifact per round, one scalar verdict at the end, no question ever written down.

## ==}{>>we should generalize this, while keeping the example specific if that makes sense<<}Standing rules

1. **Whoever approves work tries it themselves.** An agent approver runs the tests itself; when Martin approves, he opens the sample, clicks through the prototype, uses the build. "The session said it works" never counts as checking — a summary is not a check.
2. **Martin's gates sit only where his judgment is the point** — one-way doors (decisions that are expensive to reverse: data schemas once real data lands, the core loop, published URLs and interfaces) and taste calls. Everything else is agent-gated, with cross-family model review standing at every code gate. Low-value confirmation gates get removed on sight: {==a judge trained to rubber-stamp small things will rubber-stamp the big one.==}{>>???<<}
3. **Discovery work gets a budget and a breaker.** Default budget: three judgment passes (set another unit if it fits better). Two consecutive passes with no movement → stop. The same question may not be re-asked; new budget comes only with a changed question or a changed precondition.
4. **At most three unjudged variants exist at any time.** Killed options: the files are deleted, and each leaves one line — what it was, why it died — in DESIGN.md or the decision card, so no future session regenerates a dead direction.
5. **Each phase names its safety check at entry** — the mechanical thing that makes its mistakes cheap (code: tests; documents: Martin's redline pass; discovery tries: the pre-written stop-rule). Work with no nameable check gets smaller steps and earlier human eyes.
6. **Every session proves it read the right documents before building.** Dispatched sessions: the work order lists the documents; the session's first reply says what it read and which phase it believes the project is in. Sessions Martin opens directly: the project's CLAUDE.md (kept static) points at the settled docs and at PROJECTS.md for the phase, and the session starts by telling Martin what it read and where the project stands.
7. **{--While a product with a game soul is alive, Martin's hands touch the real build on a fixed cadence** (weekly minimum), and he holds kill authority over loops. "Keep decorating it" is never the answer to "it feels dead."--}{>>this feels too specific and overfitted to the company HQ example, we can safely drop it without losing much I think<<}

## (1) Brainstorm — discovery
- What is the "True Name", the "Big Idea" of the product?
- Who is it for? What problem does it solve?
- What would make it exceptional? What would make it average?
- Work from first principles, on a conceptual level; ignore technicalities completely.
- Mostly done as an extraction session: the agent asks the human an exhaustive amount of product-level questions. The vision lives in the human's head — the agent's job is to get it out, not to invent it.

**Ends with:** a one-page concept document.

**Judge:** human (redline pass).

## (2) Documentation — delivery
- Set up the standard doc structure: spec (settled truth about the product), `DESIGN.md` (why settled decisions are what they are), `TODO.md` (short- and long-term tasks), journal + `FINDINGS.md` added once there is evidence to record. `ROADMAP.md` only when the project has real sequencing decisions the workflow's phases don't capture — a doc that restates the workflow or the spec is ceremony.
- The spec covers core functionalities and user scenarios only. It grows over time; it does not try to be complete on day one. Agents treat every sentence in it as settled truth, so nothing speculative goes in.
- The phase ends by writing two short lists, kept current for the rest of the project: (i) this project's one-way doors — the decisions that get careful, early, human-gated treatment; (ii) which upcoming work is delivery and which is discovery.

**Ends with:** spec + the two sorting lists.

**Judge:** human (redline pass).

## (3) Data — delivery
- Crucial step, foundation of everything. Dig deep, put a lot of effort into getting this right.
- Work from the settled principles and the written spec.
- Define what the data actually is: entities, fields, where it comes from, what can go wrong with it.

**Ends with:** a mock-up dataset realistic enough to build and design against.

**Judge:** human inspects a sample.

## (4) Core loop — discovery
- Only for products a human operates — an app, a game, a tool with a surface. Pure data and infrastructure projects skip this phase.
- Design how it feels to use, before any visual work: what the user does in one sitting, what each action costs and gives back, what accumulates over days, what changes between visits, what finishing feels like.
- The proof is a paper prototype at minimum — a written walkthrough, sketches, fake screens. Paper is the floor, not the finish: a loop on paper can still be wrong on screen, so when the product can be used in a plain unthemed form, real daily use of that plain build is the strongest proof there is.
- No art in this phase. Design exploration themes a designed loop; a look chosen before the loop exists is a skin on nothing.

**Ends with:** a core-loop prototype (paper or plain build).

**Judge:** human walks through it — or lives with the plain build.

## (5.A) Core backend logic — delivery
- Data layer + API schema.
- The API schema is derived from the mock dataset and the spec's user scenarios — the API serves the product, not the other way around.

**Ends with:** working data layer + API against mock data, with tests.

**Judge:** agent (tests + cross-family review); product-level decisions promoted to human.

## (5.B) Collecting / creating real data — delivery
- Runs in parallel with 5.A and 5.C.

**Ends with:** real dataset passing the same shape and sanity checks as the mock.

**Judge:** human inspects a sample.

## (5.C) Design exploration — discovery
Entry condition for either variant: the core loop (4) is settled.

- **Internal / living tools** (only Martin uses it, it never ships): no up-front style guide. Build plain, live in it, and run a scheduled fresh-eyes pass (monthly to start): look at the whole thing deliberately — against the taste files, against screenshots from previous months (the screenshot timeline defeats a habituated eye), optionally with a cross-family model critique as the stand-in stranger. Verdicts accumulate; a style guide is distilled when patterns stabilize, not before.
- **Audience-facing products** (strangers will see it): diverge first — several cheap, throwaway visual directions (static mockups, mock data — hours each, not days). Martin kills and picks; only then converge on the survivor. Iterating on the first direction an agent happens to produce means the rest were never seen. Ends in a style guide before anything goes public, because strangers read visual quality as trust.

**Ends with:** internal tools — a growing record of fresh-eyes verdicts, then a style guide when it's earned; audience-facing — a style guide.

**Judge:** human (redline pass).

## (6.A) Full frontend implementation — delivery
- Component layout, full UI/UX design.
- Work from product spec and style guide (internal tools before their style guide exists: plain, from the spec alone).
- Done in Claude Code, iteratively, human in the loop — small increments the human can judge in minutes, no overnight leaps in this phase.

**Ends with:** full UI running on real data, every screen approved.

**Judge:** human.

## (6.B) Full backend implementation — delivery
- Work from product spec and existing real data.
- Autonomous Claude Code session; agent asks only product-level questions.
- Plan the session, break into small checkpointed chunks, write tests for each.
- At the end, full code review by a cross-family model (Claude reviewing ChatGPT or the other way around) → feedback to the original coding agent → accept or reject each finding.
- Product-level decisions promoted for human review.

**Ends with:** tests green + cross-family review closed out.

**Judge:** agent; decision log to human.

## (7) Testing and iteration — discovery
- Human provides product-level decisions and visual/UI/UX taste; agents handle coding, test suite, data management, everything technical they're great at.
- Runs in rounds: each round starts from the human using the product and reporting what's wrong, and ends with a fixed build the human checks again.

**Ends with:** human uses the product for its real purpose without hitting anything broken or embarrassing.

**Judge:** human.

## (8) Infrastructure & deployment — delivery

**Ends with:** product running in its real environment; one command (or none) to keep it running.

**Judge:** agent verifies, human confirms.

## (9) Retro — discovery
- Short pass after the project (or after any big phase on a training-ground project): what did the workflow itself get wrong?
- Amend this file, or make no change. The workflow only stays trustworthy if it gets corrected after real use.

**Ends with:** this file updated or explicitly left as is.

**Judge:** human.
