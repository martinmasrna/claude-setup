---
name: grading-tool
description: "Martin grades items in one local page with git-tracked JSON state (niche-taxonomy tools/layer/); extend it per job, never build a new grading page"
metadata:
  type: feedback
---

When Martin has to judge items one at a time (sort videos into buckets, admit or reject channels, mark routing disagreements), the instrument is the layer sorter in `niche-taxonomy/tools/layer/`: a local page, one item at a time, buckets as buttons, state in a git-tracked JSON file with a revision guard so a batch loader and the open page cannot overwrite each other.

**Why:** in ten days five separate grading pages were built for five jobs, and each rebuild repeated the same bugs (filing as a side effect of another click, save conflicts, clobbered state, hint labels and shortcuts he had to ask to remove, a page that broke three times in his hands). The sorter is the version that survived his use.

**How to apply:** a new grading job is a new configuration of the sorter (what an item shows, which buttons, which batch tag, which state file), not a new page. Jobs differ, so the tool stays flexible: add what a job needs to it, and keep the parts that earned their place (one action per click, no labels or shortcuts by default, the raw item and its context on screen, state on disk). Before showing him a batch, load it and click through the first ten items yourself.
