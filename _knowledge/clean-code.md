# Clean Code

> Clean code keeps order against chaos: it is the fittest, least *arbitrary* expression of what the program is for — every part solved with the tool built for it, nothing wasted and nothing missing, cohering so well that a stranger can navigate it without getting lost or asking a question. Fitness is always judged against context, never in the absolute.

This file captures one person's cross-domain aesthetic of "cleanness" as it applies to code. Treat it as taste to internalize, not a lint config to mechanically apply.

## Motivation — why this concept exists

**The enemy is chaos.** A codebase decays toward a maze. Once it's a maze, every action — reading, understanding, changing, fixing — becomes an uphill battle, and that burns real resources: human hours, LLM tokens, company money. Clean code is the discipline of keeping the codebase a **grid instead of a maze**: predictable, navigable, hard to get lost in. That is the root payoff everything below traces back to. Clean code also makes whole classes of error *harder to make*, not just easier to spot.

**Two mental models, used together:**
- **Grid vs. maze** (primary). In a grid you always know where you are and how to get where you're going; movement is cheap and you can't get lost. A maze punishes every step with dead ends and surprises. Cleanliness = navigability.
- **The messy room** (secondary). Messiness is *holistic and graded*, not a single defect. A room isn't dirty because of one sock; the whole gestalt is off. Likewise cleanliness is a **purity scale from 0–100%**, never a binary pass/fail.

**At root, clean is the fittest, least *arbitrary* expression of a thing for its context.** Arbitrariness is the enemy. And fitness is **always judged against a purpose — nothing is clean in the absolute.** The same prime number, the same name, the same line of code can be clean in one context and not in another. (This context-relativity is load-bearing, not a footnote; it recurs everywhere below.) Cleanliness then builds in two levels.

**Basic level — nothing arbitrary.** Arbitrariness sneaks in two ways, and both must be shut out:
- *Regular, compressible form:* the thing collapses to a short, simple rule — no lumpy, patternless content you'd have to specify piece by piece. A **circle** is one number (a radius); `x² + 5x + 6` *looks* lumpy but collapses to `(x+2)(x+3)`. Counter-case: a **key** is an arbitrary list of notches — nothing about it is wasted, yet it isn't clean. **Minimal ≠ clean; the content itself must be non-arbitrary.**
- *Fit of means to end:* the job is done with the tool/abstraction *built for it*, at the right level — never a crude or wrong-level workaround. `x**3` over `x*x*x` (exponentiation is what powers are *for* — not merely one character shorter); a key **plus lock** to keep a door shut-but-openable, not planks nailed across it. The fit that counts is means→end, not object→its-own-function. *"Nothing wasted, nothing missing" is a symptom of this fit, not the whole of it.*

**Higher level — emergence:** a clean creation is *much greater than the sum of its good parts.* Having no bad parts is necessary but not sufficient; at its best the parts **synergize** into a single coherent whole with properties none of them have alone — the codebase reads as *one unified thing* rather than a pile of features. (Cross-domain: the original iPhone; the album *Hybrid Theory*; the rules of chess generating a bottomless game; the Mandelbrot set's infinite coastline from one short equation.)

So the purity climb is: **chaos → tidy (no arbitrary form or means) → elegant (the parts fuse into a whole greater than their sum).**

**Cross-domain anchors (endorsed):**
- *Fit of means to end:* one Hearthstone **Swipe** (4 damage to one target, 1 to every other) against a 4/4 and three 1/1s clears the whole board — one card, perfectly matched to the situation.
  - What this shows: the means fitting the end so exactly that nothing is left over and nothing more is needed.
  - What's incidental: the game, the numbers. *Not* "code should be one-liners."
- *Greater than the sum:* a hand of **Wild Growth → Chillwind Yeti → Azure Drake** isn't three good cards, it's a smooth curve where each turn sets up the next, so the sequence is worth more than the cards counted separately.
  - What this shows: parts that synergize into one coherent whole — the higher level.
  - What's incidental: the card names. The point is synergy, not the deck.

**Care is a diagnostic, not the definition.** Clean things are almost always made by someone who cared — with expertise, effort, even love — and cleanliness reliably lets you *infer* that care. But "care" is a fingerprint to read off, not a property an agent can act on. An agent can't care; it can only produce the structural qualities careful people tend to produce. Use the smell test ("does this feel careless?") as a check, never as the goal.

## The human ⟹ LLM asymmetry

A crucial constraint on what "clean" means: **if something is clean for a human, it is automatically clean for an LLM — but not the reverse.** Human-clean is the *stricter* standard. An LLM can hold a 2,000-line flat, repetitive, verbose file in its head at once; a human cannot. So always optimize for **human-clean**; you get LLM-clean for free. Code that is merely LLM-clean (e.g. sprawling, verbose, repetitive but consistent) can still be human-*dirty* because it isn't navigable or chunkable by a limited working memory.

## Principles (the tactical levers)

These are the concrete, nameable moves that raise the purity %. They are **additive and holistic** — each chips the score up or down; **none is a single kill-switch**, and the gestalt is what matters. Each serves one or more of the qualities above — fit, regularity, navigability, or emergence. When two conflict, see the priority notes.

### 1. One place to change (near-supreme)
A given thing lives in exactly one spot; to change a behavior you edit one place. This is the highest-priority lever — it wins **almost always**, even against immediate understandability.

**Why the usual objection fails:** "but now the newcomer has to hunt down the abstraction" — in *clean* code that hunt is cheap, because the abstraction you land on is itself self-evident. DRY and understandability only fight in *dirty* code; in clean code **every hop is a clean hop**. Self-evidence applies at every level, not just the top.

### 2. No useless parts
No dead code, no vestigial parameters, nothing that doesn't serve the program's purpose.

### 3. Fewest lines that stay clear — clarity is the master
Compress, but **clarity outranks brevity**. "As few lines as possible" is always bounded by "without losing clarity." Code golf is not clean.

### 4. Zero-question onboarding
A programmer who has never seen the code can pick it up cold and understand what's going on **without asking anyone a question**. This is the felt test of self-evidence.

### 5. Clean module boundaries
Sharp, clear separations between modules/components. Each has a crisp edge; responsibilities don't bleed.

### 6. Room to breathe
The code is readable and aesthetically pleasing — enough whitespace that it breathes. Visual calm is part of cleanliness, not decoration.

### 7. Self-evident names — sized to context
Names carry meaning so the reader doesn't have to ask. **But this is reader-relative:** supply *exactly* the information the reader needs given what context already provides — no more, no less. Verbose names where context already makes the meaning obvious are themselves waste. (This is fit-to-context applied to *information*.)

**Example (endorsed) — naming is context-relative:**
```python
# B wins with no surrounding context:
def compound_balance(principal, annual_rate, years):
    return principal * (1 + annual_rate) ** years

# A wins WHEN context already makes p, r, t obvious:
def d(p, r, t): return p * ((1 + r) ** t)
```
- What this shows: the right amount of naming depends on what context already supplies. Neither is universally cleaner.
- What's incidental: the finance domain, the specific letters. The point is information economy, not "always use long names."

### 8. Consistency / symmetry
Like things are written alike; unlike things are written differently; one concept gets exactly **one name** across the whole codebase. Arbitrary inconsistency is a *lump* — when two similar things look different, the reader must stop and check whether the difference *means* something. (This is the regularity/grid strand applied across files.)

### 9. Make bad states unrepresentable
Shape the types and data so an illegal state literally can't be written — then a whole class of bugs vanishes by construction. The *structure* does the prevention, not vigilance. (This is "errors **hard to make**, not just easy to spot" — the double-entry-bookkeeping move in code.)

### 10. One altitude per unit
A function reads at a single level of abstraction — don't mix high-level orchestration with low-level bit-twiddling in the same breath. Mixed altitude is a maze. (Generalizes `x**3`: use *and stay at* the level built for the job.)

### 11. No hidden side effects (least surprise)
A unit does what its name says and nothing sneaky — no action-at-a-distance, no secret mutation of shared state. Surprises are the maze; a grid is predictable.

## Keystone near-miss — comments that narrate *what*

```python
# C — heavily commented, looks careful and considerate
def proc(x):
    # multiply by 1.08 to add 8% sales tax
    y = x * 1.08
    # round to 2 decimals for currency
    return round(y, 2)

# D — names do the talking
def add_sales_tax(price):
    TAX_RATE = 0.08
    return round(price * (1 + TAX_RATE), 2)
```
**D is infinitely cleaner.** C *looks* clean — documented, considerate to the newcomer, evidently effortful. That is exactly why it's the highest-value near-miss: comments that narrate *what the code does* are not cleanliness, they are **compensation for code that failed to explain itself**. Clean code makes the *what* self-evident, which makes such comments redundant. The discriminator: heavy what-comments are a *symptom of dirt*, not a sign of care.

## Keystone near-miss — works ≠ clean (the Rube Goldberg machine)

A Rube Goldberg machine *works*, and every piece "fits" the next — yet it's the opposite of clean: it reaches a trivial end through a sprawl of arbitrary means. It nails the wrong kind of fit (part→part) while failing the one that matters (means→end). Same lesson as the lone **key** and `x*x*x`: working, even tidy, is not clean if the means are arbitrary or pitched below the right level of abstraction. Beware judging cleanliness by *does it work* or *does it look neat* — judge it by *is this the fitting, non-arbitrary way to do it, here*.

**In code this is over-engineering.** Speculative abstraction layers for needs that may never arrive, configuration knobs nobody turns, and *over-defensive* code that guards against states which cannot occur in this context — all bolt on arbitrary machinery that doesn't serve the real purpose. Each handler for an impossible edge case is a lump: it costs reading, hides the real path, and (per context-relativity) defends against a case *this* context already rules out. The clean instinct is to build the fitting solution to the problem you actually have, not a general machine for problems you imagine. This is also where chasing "one place to change" tips into a maze — abstraction added before there's a second real caller is just another arbitrary means.

## How to read all this

- Cleanliness is a **graded gestalt**, not a checklist score. Use the levers to move the needle, but judge the whole — does it read as a navigable grid that coheres into a whole greater than its parts, made by someone who cared?
- **Nothing is clean in the absolute.** Always judge fit against the specific context/purpose — the same name, number, or construct can be clean here and not there.
- **Working and tidy are not cleanliness.** A thing can run correctly and look neat while solving its problem with arbitrary or wrong-level means (the Rube Goldberg trap).
- Optimize for the **human** reader; the LLM is covered automatically.
- When levers conflict: **one-place-to-change** and **clarity** are the two you protect hardest.

## Dissent log
- **The limit of DRY is deliberately unresolved.** Where does chasing "one place to change" tip into a maze of tiny indirections? The user declined to set a threshold — "would need a specific example, but it's common sense." Do not invent a rule; judge case by case.
- **What-comments vs. why-comments.** The C-vs-D ruling is specifically about comments narrating *what* the code does. Comments explaining a non-obvious *why* may be a different animal and were not ruled on. Don't over-extend "comments = dirt" to why-comments.
- **Source's stance:** strong cross-domain intuition for cleanliness, junior-level hands-on coding experience. The *aesthetic* is authoritative; specific code-mechanics claims (e.g. typing variables preventing errors) were offered tentatively and should be weighted as illustrations, not doctrine.
