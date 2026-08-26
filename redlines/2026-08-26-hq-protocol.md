# End-of-session protocol

{--Headquarters shows Martin only what is filed in this folder — unfiled work is invisible, and "nothing needs you" becomes a lie. --}{>>this is completely out of context, someone who start reading this feels like they got dropped in the middle of something random<<}{--So--} {~~e~>E~~}very working session in a company project closes with the two steps below. `company-headquarters/DATA.md` is the authority on formats; the templates here are copies for convenience.

## 1. Leave a session note — always

One file: `hq/notes/YYYY-MM-DD-<project>-<slug>.md`.

```markdown
---
project: <registry name from PROJECTS.md>
ended: <ISO 8601 timestamp with offset>
by: <what session this was, e.g. "overnight census session">
commits: <range or list; empty only if the body says why>
---
What got done, plain, a few lines. Name uncommitted leftovers explicitly.
```

Completeness over prose — {~~this is material for the digest agent, not text Martin reads.~>**this is material for the digest agent, not text Martin reads.**~~} A session with nothing to commit (research, a decision) leaves `commits:` empty and says why in the body.

## 2. File a queue item — only when Martin's judgment is the blocker

When the work cannot move forward without Martin — typically a workflow gate: a document ready for his redline pass, a decision only he can make — file `hq/queue/YYYY-MM-DD-<project>-<slug>.md`:

```markdown
---
project: <registry name>
type: <document | decision>
created: <ISO 8601 timestamp with offset>
by: <what session this was>
gate: "<workflow gate>"                  # optional
open: <path from Personal Brand root>    # optional; opens in the redline editor
---
First line: the ask, one sentence. Then the minimum context needed to judge.
For a decision: the options and your recommendation.
```

Never file what an agent can decide — the queue spends Martin's attention, the scarcest resource in the company. And never delete or edit queue items; judging them is Martin's act, through headquarters{==.==}{>>is this for review agent, or for me?<<}
