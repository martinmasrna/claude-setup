---
name: visual-taste
description: "UI and figures — cut labels, one goal per surface, scannable first; figures show mechanism, judged at reading size by eye"
metadata:
  type: feedback
---

- **Cut labels by default.** The AI failure mode is over-labeling: headings restating their content, sub-captions under numbers, a percentage and a bar encoding the same value as two separate elements (a value label on the bar itself is fine — there, the number is evidence, not decoration), decorative rank numbers, stats not decision-relevant on that screen, captions explaining what a figure already shows. Leave dense sections slightly under-labelled — Martin sweeps manually and would rather add back than remove.

- **One goal per surface, one primary action.** Anything not serving the surface's goal is useless, including neutral-looking chrome (wordmark, nav, explainer pages). Justify each element out loud; push back on a cut only when it has a concrete cost.

- **Scannable before readable.** The eye takes a graphic pass (shape of the data, outlier magnitudes) before a text pass, and reads text only if the graphic pass earned it. Keep graphic and text zones separate and internally uniform; give the scan target real visual weight. A density win that yields nothing in the first half-second of looking isn't worth it. Vertical space is scarce ([[machine-environment]]) but never outranks scannability.

- **Figures show mechanism, not data.** A figure that reads as a table gets rejected — the reader wants the mechanism they can't see, not a second rendering of numbers they just read. Prefer flow/area/position forms over grids.

- **Judge at reading size, by eye.** Render in a box the width of the real column (~650px X article, ~390px phone) on the first draft, not at the end. Size arithmetic misjudges legibility in both directions — short bold labels on high-contrast fills survive far below the nominal floor, thin dark text on white doesn't.

- **On rejection, ask if it should exist before improving it.** State in one sentence what the element or figure argues and check that against the piece's goal; if they fight, cut rather than redraw. Build the alternative and show it — Martin judges visually and reacts fast.
