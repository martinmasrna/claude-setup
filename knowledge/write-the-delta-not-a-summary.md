---
name: write-the-delta-not-a-summary
description: Never summarise a source that is already in the repo — record only what changes a decision and link to the source.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cea6231c-1f2c-440d-918c-9a14b268aa5c
  modified: 2026-08-05T13:28:07.727Z
---

When a source document exists — a call transcript, a study, a scrape, a research file — **do not write a summary of it into another file.** Record only the parts that change a decision, in as few lines as possible, and point at the source.

**Why:** on 2026-08-05 Martin spent ninety minutes cutting CLAUDE.md from 1,323 words to under 800, mostly deleting summaries of things stated elsewhere. Within the hour I read a 46-minute client transcript and wrote 700 words of bullets summarising it into `clients/iterate/engagement.md` — a summary of a file sitting in the same repo. His reaction: *"we'll never get anything done because we'll get lost reading the Bible that is your documentation."* The correct version was five lines. Earlier the same day I had diagnosed this exact pattern in his repo (four files summarising the same nine studies) and then committed it myself, so recognising it in someone else's work does not stop me doing it.

**How to apply:** before adding to a doc, ask what a reader would *do differently* because of each line. Cut anything that only restates the source. A pointer plus the deltas beats a faithful précis every time — the précis is guaranteed to drift from the source, and nobody reads two accounts of the same thing. This is the same instinct as the How-to-respond rules in global CLAUDE.md, applied to files rather than to speech, and it is the one Martin has had to correct most often.
