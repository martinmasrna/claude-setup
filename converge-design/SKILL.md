---
name: converge-design
description: Converge on a frontend design through static mockups instead of trying to specify it up front. Use when the user wants to explore, improve, redesign, or rethink the visual design of a UI element, component, page, or whole app — especially when they say things like "I don't know what I want until I see it," "show me some options/mockups," "let's iterate on the look," or "redesign this." Generates throwaway static mockups, lets the user judge them in the browser, and narrows down via an N-ary search through a design decision tree. It CONVERGES on a winning design; it does NOT implement it in the real codebase.
---

# converge-design

A tool for *converging* on a frontend design by generating throwaway static mockups,
reacting to them in a browser, and progressively narrowing — an N-ary search down a
design decision tree. The folder tree on disk **is** the decision history.

This skill **does not implement** the design in the real codebase. It stops at a
documented winner and hands off to a fresh coding session.

## Mental model

Imagine a tree of all possible designs. Each round generates a few sibling nodes
(typically ~3, but more for cheap variations). The user reacts, you descend into the
chosen branch, and the next round generates *its* children — refinements of the pick.
The branching factor stays roughly constant; the **distance between siblings shrinks**
as you descend: wide, divergent directions near the root → tight, single-knob
refinements near the leaves. One adaptive process, converging asymptotically on the
design the user wants.

Every round holds some dimensions **locked** and varies others **free** (A/B testing:
fix what's good, iterate on what isn't). The single most important discipline:
**make the locked/free split explicit and get the user's agreement before generating.**
Never silently change something the user was happy with.

## Two phases

This skill is phase-aware based on the **working directory the skill is invoked in**
(the process cwd), checked one level only — not parents, not children:

- **cwd contains a `_context/` folder** → you are in the sandbox. Run **EXPLORE**.
- **cwd does NOT contain `_context/`** → you are (presumably) in the real repo. Before
  running BOOTSTRAP, check whether a sandbox for this work already exists (ask the user
  if you can't tell). If one does, do **not** silently re-bootstrap — ask whether to
  **resume** there (tell them to `cd` into it and re-invoke the skill) or start fresh.
  Otherwise run **BOOTSTRAP**.

---

## Phase 1 — BOOTSTRAP (run once, in the real repo)

This is the **only** phase that reads the real app code. Distill reality into a few
small files so that exploration can run later reading *only those* — keeping context
lean across many rounds and isolating the exploration from the sprawling codebase.

Steps 1, 2, and the screenshot request (step 4) all need user input — **present them
together as one batched prompt**, don't fire three serial round-trips.

1. **Confirm scope.** What element / component / page / whole-app is being designed?
   Is this *improving something that exists* or *designing from scratch*?

2. **Pick the sandbox location.** Ask the user where to create the temp folder (or
   propose a sensible path next to, but outside, the repo). Create it.

3. **Read reality once** (only if improving something that exists): read the real
   component(s) + their CSS / Tailwind classes / theme config. You are reading this
   **once**, now, to distill it — not on every round.

4. **Build `_context/`:**
   - `tokens.css` — **extract** the real design tokens (whatever subset the app
     actually defines — colors, fonts, spacing scale, radii, shadows; skip categories
     it doesn't have) as CSS custom properties. Never hand-write these; read them from
     the real source so the lock is *exact* and porting back is mechanical. Where the
     real values live varies — handle the common cases:
     - **Clean `:root` / theme stylesheet** → copy the custom properties verbatim.
     - **Tailwind** → read `tailwind.config.*`'s `theme`/`extend` and emit the
       equivalent custom properties.
     - **JS/TS theme object** (styled-components, MUI, a `theme.ts`) → read it and
       translate to custom properties.
     - **Hard-coded values scattered in CSS** → collect the recurring hexes/sizes,
       name them sensibly, and note in the file that these names are invented (so the
       port-back step knows they don't yet exist in the real app).
   - `project-summary.txt` — **draft** this yourself from the real code: what the
     element is, the real copy/labels/data it shows, what matters. Then **ask the user
     to review and correct it** — they own the intent; you only inferred it. This gives
     mockups real content instead of Lorem Ipsum.
   - `current.png` — if improving something that exists, **ask the user to drop a
     screenshot** of the current state here, with a one-line hint on what to capture.
     Code tells you structure; the screenshot is the ground truth of *appearance*.
     Strongly request it. If it's genuinely unobtainable, record its absence in
     `_context/` (a short note) and proceed code-only, flagging that *appearance* is
     unverified — do not hard-block. (Skip entirely if designing from scratch.)
   - `skill-path.txt` — write the absolute path of **this skill's own folder** (the one
     containing this `SKILL.md` and `LEARNINGS.md`) so the later EXPLORE session, which
     runs from the sandbox, can find `LEARNINGS.md`.

5. **Hand off to a fresh session.** Once `_context/` is built and ratified, tell the
   user to start exploration in a clean session, e.g.:

   ```
   cd <sandbox-path>
   claude
   ```
   then run `/converge-design` again. The fresh session, started in the sandbox, will
   detect `_context/` and enter EXPLORE mode automatically. Do not start generating
   mockups in the bootstrap session.

---

## Phase 2 — EXPLORE (run in the sandbox, fresh session)

Read `_context/` (`project-summary.txt`, `tokens.css`, `current.png` if present) and
read the existing folder tree to recover where things stand. **Do not read the real app
code** — everything you need is in `_context/`.

### The per-round loop

1. **Agree on the locked/free split.** State plainly what stays fixed and what you'll
   vary this round, and what "better" means here. Get the user's nod. The free
   dimension *is* the differentiator that names the siblings (see below). This step is
   the gate: do not generate until the next branch is unambiguous. A verdict ("#2 is
   best") tells you where the user landed, not where to go next — keep talking until
   intent is crystal clear.

2. **Choose render mode** from the locked/free split:
   - **Divergent siblings** (different layouts/directions, little shared code) →
     **separate pages**, one per named folder. Typical for wide rounds near the root.
   - **Variations on a locked structure** (color, type scale, spacing — one knob) →
     **one page with a switcher navbar**, N variants inline (can be 12–20). Typical for
     tight rounds near the leaves, and whenever separate pages would share most code.

3. **Generate.** Every mockup links `_context/tokens.css` so locked dimensions are
   *exactly* the real values. **Mind the relative path:** mockups live in nested
   folders, so the link must climb the right number of levels — a file at
   `split-hero/warm/tighter/index.html` needs `../../../_context/tokens.css`, not
   `_context/tokens.css`. Count the depth and verify it resolves when opened; if in
   doubt, copy `tokens.css` into the mockup's own folder. Use real copy from
   `project-summary.txt`. Static only — visuals, no logic.

4. **Auto-open in the browser.** Detect the OS and shell; never assume. Per-OS:
   - macOS: `open <file>`
   - Linux: `xdg-open <file>`
   - Windows: `start "" <file>` (cmd/Git-Bash — bare `start <file>` is misleading) or
     `Start-Process <file>` (PowerShell)

5. **Stop and wait.** Do not charge ahead.

6. **Converge.** Back-and-forth until 100% aligned on the *next* locked/free split,
   then loop.

### Folder structure (the tree IS the history)

```
<sandbox>/
  _context/
    project-summary.txt
    tokens.css
    current.png
    skill-path.txt
  split-hero/  centered-stack/  sidebar/      <- round 1: wide, divergent
        index.html
        notes.md
        warm/  cool/  mono/                    <- round 2: refinements OF the pick
              index.html
              notes.md
              tighter/  looser/                <- round 3: narrower still
```

- **Name folders after the differentiator** — the free dimension that round — in 1–2
  kebab words. The path reads as a sentence: `split-hero/warm/tighter`. Names describe
  *what's different*, not the whole design.
- **A node that has children is, by definition, the chosen branch.** No separate winner
  marker. **Backing up** = go up a folder and try a different sibling.
- **`notes.md`** per node records what was locked, what varied, and why — what you need
  when backing up later.
- **Switcher rounds:** the round lives as one `index.html` with the switcher. Once the
  user picks a variant, **promote that choice into its own properly named folder**
  (e.g. `.../teal-warm/`) which becomes the parent for the next round. The switcher is
  the exploration surface; the named folder is the committed decision. Keep the tree
  semantic and intact, always.

### Context hygiene

Only the current node and the siblings you're about to generate need to be in context.
The rest of the tree lives on disk — re-open files on demand if the user says "go back
to round 2." Never load the whole tree at once.

---

## Handoff (end state)

When the user is happy, the skill's job is to STOP at a clean, documented winner — not
to implement it. Produce:

- The winning `index.html` (already in its named folder).
- `port-spec.md` next to it: what the design is, which `_context/` tokens it uses (so
  the names already line up with the real app), what is **new** vs. what already exists
  in the real components, and any gotchas (responsiveness, states, accessibility the
  static mockup didn't cover).

Tell the user to hand `port-spec.md` + the winning `index.html` to a fresh coding
session for implementation. Do not implement it here, even if asked to "just do it" —
that's a different mode and belongs in a clean session with the real codebase loaded.

---

## Self-improvement

Read `LEARNINGS.md` (in this skill's folder) at the start of every run and apply what's
there. In EXPLORE, the session runs from the sandbox, not the skill folder — find the
skill folder via `_context/skill-path.txt` (written during bootstrap) to locate it. At the **end** of a converged session, reflect: did anything this time teach a
reusable heuristic about *this user's* taste or workflow? If so, **propose it** to the
user in one line and append it to `LEARNINGS.md` **only on their confirmation**. Never
write a lesson silently, and never edit this `SKILL.md` to "learn" — keep the stable
spec and the accumulated taste separate.
