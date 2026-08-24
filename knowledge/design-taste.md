---
name: design-taste
description: "UI taste — cut ~80% of labels, one goal per surface, scannable as a graphic before readable as text"
metadata:
  type: feedback
---

**Cut the labelling by default.** The usual AI failure mode: "over-labeling and over-annotating everything, visual elements that add nothing" — Martin asked for ~80% of titles, labels and stats to go. What that meant concretely: section headings restating their content, caption text on headings, sub-captions under numbers, a percentage and a bar encoding the same value, decorative 01/02/03 rank numbers, stats that were interesting but not decision-relevant on that screen. Leave dense sections slightly under-labelled — he sweeps manually afterwards and would rather remove less than add back.

**One goal per surface.** "If something on screen doesn't help us get newsletter subscribers, it's USELESS." State the surface's single goal first, give it exactly one primary action, and justify each element out loud before adding it. Neutral-looking chrome (wordmarks, nav, explanatory pages) is cost without return unless it moves someone toward the goal. He's fine with pushback when a cut has real cost — keeping `/browse` for crawlability survived exactly that argument.

**Scannable before readable.** He judges a display by time-to-gist, not pixel count: a dense layout that reads in 5 seconds loses to a taller one that reads in 0.5. Humans take a display in two passes — pass one is graphic (the shape of the distribution, the outlier magnitudes, at a glance), pass two is text, read only if pass one earned it. Interleaving graphic and text into one line destroys pass one. Keep the graphic zone and the text zone separate and each internally uniform; give the scan target real visual weight (size, face, a shape like a wedge or staircase). Before proposing a density win, ask what the first half-second of looking yields — if "nothing yet", the saving isn't worth it. Vertical space is genuinely scarce (small viewport, see [[machine-environment]]) but never outranks this.
