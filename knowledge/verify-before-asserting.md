---
name: verify-before-asserting
description: "Tag guesses as guesses, set the test bar before running it, read the code behind a number before contradicting it"
metadata:
  type: feedback
---

Don't present unverified inference as fact.

- A guess stated as analysis is the failure — say "unvalidated, checkable via X" and prefer checking cheaply over asserting. A subagent's digest locates claims but never verifies them; verify every number and quote against the primary source before anything ships.
- Decide what counts as a real difference (threshold, minimum group size) *before* running a comparison — a loose bar manufactures findings that evaporate under a defensible one. Report the test, not just the verdict.
- A recomputed number that disagrees with a committed one is a disagreement, not an error. Read the code that produced the original and reproduce it under its own rule before calling it wrong.
- Numbers crossing between sessions gain false independence — recompute before recording a peer's figure, and label your own as computed or eyeballed.
