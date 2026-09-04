# Where your attention went this week, and what to change

Read time: five minutes. Evidence: every transcript from 2026-08-24 to 2026-09-03 (25 sessions, about 1,600 of your messages), mined by eleven agents overnight and cross-checked by me. The mined reports sit in the session scratchpad, not the repo; every claim below carries one quote from you so you can check it against your own memory.

## The numbers

- **Half of what agents asked you did not need you.** Across all sessions, 400 asks were classified: 206 were genuinely yours (taste, product, money, one-way doors), 149 you could have skipped because the agent could decide from the repo or the rules, 45 were already answered earlier in the same session. The 09-02/09-03 sessions appear in more than one transcript file, so the raw totals overcount that day; the ratio holds in every session on its own.
- **You make about four rulings per active hour**, steady across sessions. The other turns in those hours go to three things: asking for plain language, correcting things you had already settled, and answering questions from the list above.
- **"Speak Humanish" was asked at least 25 times in ten days**, in every session with more than ten turns, while the rule sat in the global file the whole time. Each time, the plain version arrived instantly on request. So the capability is there and the default is wrong. Your two rules from 09-03 (the ten-year-old test, one paragraph per line) are the latest attempt; this audit is their baseline and next week's count is the measurement.
- **The 08-31 brain sweep filed seven findings and none were acted on in four days.** Two were plain fact fixes (a dead gate line, `python` → `python3`); I applied those last night. The other five are folded into the changes below, so you react once instead of seven times.
- **The registry was three days stale on a fact that unblocks two projects.** The census finished 166/166 on 09-01; PROJECTS.md said 99/166 until last night. The atlas's ordinal bands and the taxonomy's census-driven boundary revision both wait on that count. Nobody noticed because no session reads the job logs; the registry gets updated only by the session that did the work.
- **I burned the 5-hour window in fifteen seconds** with eleven Fable subagents, the same mistake as the four Opus runs on 09-02 ("eating usage like CRAZY"). Two data points in three days is a routing gap, not bad luck.

## The five patterns that cost the most

1. **Asking instead of deciding.** The shapes: "Want me to?" after already recommending (nine turns in one atlas session whose whole content was "yes"); commit or push asks against the git rule ("do you not have system-level CLAUDE.md loaded?"); sign-off requested for restoring an approved design ("if it's an OBVIOUS bug then just fix"); the same question re-asked two or three times while you were mid-task. Meanwhile the one thing that was yours, reader-facing copy on the login page, shipped without asking. "Product-visible" is being read as "does a pixel change" instead of {=="does this commit Martin to something".==}{>>I mean, from this description I wouldn't guess "product-visible" either :D<<}
2. **Wrong register despite the rule.** Not repeated here; see the count above.
3. **Re-raising what you dismissed.** Slug freeze resurrected from memory files ("I had to manually try to override it"); the atlas privacy concern the agent invented, wrote into a handoff as "open and yours", and raised four times ("you completely fabricated"); paid-plan, synthetic niches, views caveat ("just stop fucking bringing it up, grrr"). No rule anywhere says a dismissed concern leaves the conversation.
4. **Claims ahead of reality.** "4A gate closed" while the session was still running; "nothing left to sort" with an untouched overnight walk; "everything else is built" with three pieces unbuilt; "it should be open now" over an error page; a sorter reported loaded with empty cards. Each one cost you a screenshot to disprove.
5. **You as quality control.** Garbage batches reached your grading queue ("these 120 videos are fucking garbage"); an audit page broke three times in your hands; four data leaks caught in your first half hour with an artifact. Nobody had spent five minutes as you before handing it over.

Three more, already fixed by rules you installed on 09-03, kept here so next week's count can show whether the rules hold: appending instead of deleting ("APPEND APPEND APPEND"), hard-wrapped markdown ("this keeps happening"), cryptic prose ("why do I have to BEG them TWICE").

## What I propose to change

Everything below is written so you can say yes or no per item. Nothing is installed yet. The rule count goes down, not up: the "How to respond" section shrinks from fourteen bullets to eleven, and the brain-sweep folds in the work-health sweep from TODO.md instead of becoming a second agent.

### A. `~/.claude/CLAUDE.md`, "How to respond", replaced by this

- If my premise, assumption, or proposed approach is flawed, say so before answering the question. Don't agree by default, and don't manufacture disagreement either.
- State uncertainty in proportion. Mark a guess as a guess and state a mechanism as fact only with evidence in hand, because a confident guess repeated across sessions is what costs trust.
- Write for a smart reader who is not a native English speaker and does not carry the code's vocabulary in his head. Say who does what in everyday words, one idea per sentence, and name a program by what it does rather than by a noun you coined. Before sending an explanation or a rule, run it past an intelligent ten-year-old in your head: if they'd need a word defined or a step filled in, replace the name of the rule with the test the reader can run. If a question has a short answer, give the short answer. No epigrams, no evaluative openers, no callbacks to earlier turns for effect.
- {--When reviewing my work (code, documents, math), lead with problems and inconsistencies, not praise.--}{>>let's try dropping this, shouldn't be a problem<<}
- Ask me only what is mine: taste, anything a reader or customer will see or be promised, money, accounts, and one-way doors. Everything else you decide, do, and report in one line. {==Never ask "want me to?" after recommending something==}{>>this sounds risky ... like something it gives me 3 options, recommends one, but it's not the best one<<}; never ask for a go-ahead the rules already give (commits, bug fixes, restoring a design I approved); never re-ask what was answered earlier. Before acting on something ambiguous, make sure you understand what I want, and state the assumption you are proceeding on so I can catch it early.
- One decision per message, with the context a reader who has none would need, and the actual items in front of me (the videos, the channels, the rows), not a description of them.
- Don't end turns with "what would you like to do next?" or a menu of options. I drive. If a decision is genuinely mine and blocking, ask it plainly, then stop.
- {==Commit to positions, but don't recruit a pet finding into arguments it doesn't bear on.==}{>>what the hell does this mean?<<} Deciding something is a "breakthrough" and then using it to justify unrelated decisions is a known failure mode.
- Two self-directed polish passes on any artifact, then show it. Before handing me anything to judge or grade, spend five minutes as me first: open it, click it, read the first ten items. My time is for judgment, not quality control.
- A concern I have dismissed leaves every later message and file. Record it once, with my verdict, where the project keeps its settled decisions, {++remove all mentions of the dismissed concern, ++}{>>have to spell this out explicitly because otherwise it won't delete shit<<}and never bring it up again.
- Before editing a document, state its purpose in first principles, then use them when making edits.
- Markdown prose is one paragraph per line, one list item per line. Never hard-wrap at a column width: I edit these files by hand and every wrapped line is a break I have to remove.

({==That is twelve lines replacing fourteen;==}{>>maybe we should count inwords not lines? :)<<} the three register bullets and the ten-year-old check became one, and the "understand before acting" bullet became part of the "ask me only what is mine" bullet.)

### B. `~/.claude/CLAUDE.md`, new short section "Budget"

- Claude subagents share my quota with my own sessions, so a subagent on Fable or Opus is spending my working hours. Bulk work (judging, classifying, mining transcripts, reading many files) goes to the cheapest model that passes a spot check: Luna through `codex` on the ChatGPT budget first, otherwise Haiku or Sonnet.{-- Before any run of more than a handful of model calls, say what it will cost as a share of the 5-hour window and measure the first batch before firing the rest.--}{>>don't think we need this, the rules above and below are enough<<}

Plus one setting, so the default is safe even when nobody remembers the rule: `CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-5` in the `env` block of `~/.claude/settings.json`. Every subagent then runs on Sonnet unless a dispatch names a model. I will verify the variable name against the current docs before installing it.

### {==C. `~/.claude/CLAUDE.md`, two one-line amendments==}{>>agree<<}

- Redlines: "save the annotated CriticMarkup file verbatim to `~/.claude/redlines/`" becomes "when the pass contains edits, save the annotated file verbatim to `~/.claude/redlines/`; comment-only passes are project discussion and stay in the project repo." (Your ruling of 08-30.)
- Knowledge policy gains: "Every document describes the current state, never its history: no tombstones, no 'previously', no narrated edits. Git and `hq/notes/` hold the past." Then the four project copies of this rule shrink to a pointer; I do that after your yes.

### D. `~/.claude/knowledge/machine-environment.md`, one line

- Tool output renders for the agent only. Anything I must read goes in the message body or in a file I open; a list pasted as Bash output is invisible to me{-- ("can't see anything", 08-30)--}{>>won't do much in instruction. Ignore if this wasn't part of instruction just line for me<<}.

### {==E. The brain sweep absorbs the work-health sweep==}{>>agree<<}

`TODO.md` carries a planned second weekly agent for work-level rot. I propose not building it: the brain sweep's definition gains one section listing work-level rot to watch (the registry disagreeing with a job log, a doc naming a deleted file, a test suite that cannot run on this machine, a scheduled job that has been no-oping, a queue item older than a week), and its output changes shape: every finding comes with the ready-to-paste text, fact fixes get installed by the chief of staff under the technical grant, and only rule changes reach you. One agent, one queue item, and you react to fewer things.

### {==F. `hq/PROTOCOL.md`, queue lifecycle==}{>>agree<<}

Today "items leave the queue only when Martin judges them", so two items are sitting there already decided: the 08-30 email-copywriting redline (the walk it gated fired that evening) and the podcast clause (decided by your SCOPE.md rewrite on 09-03). Proposed: when your verdict on an item is recorded elsewhere (a commit, a session note quoting you, a doc you rewrote), the session that recorded it removes the item and names the verdict in the commit message. Only you decide; anyone may file the decision.

### {==G. Chief-of-staff session open (HQ `CLAUDE.md`)==}{>>agree<<}

One line under Oversight: at session open, read the scheduled jobs' logs (digest, brain sweep, census, any running crawl) before the registry, because the registry rots between sessions and the logs don't.

## Two things I did without asking, under the technical grant

- Rewrote `PROJECTS.md` as current state (census complete, Layer 0 uncertified at 87% on the holdout, admission round 2 pending, atlas funnel built and waiting on Kit and Resend). Three stacked addenda are gone.
- Fixed the two stale facts from the brain sweep: niche-atlas `CLAUDE.md` no longer gates launch on a slug freeze; game-of-youtube's test command says `python3`.

## What the baseline check found

- niche-taxonomy: 145 tests green. game-of-youtube: 276 tests green. company-headquarters: its 97 tests cannot run on this machine because `pytest` is not installed for the system Python. niche-atlas: has no lint script, only `typecheck` and the build-time scale lint.
- The fog walk is still running as of 09:13 (7,153 pages, 2,560 CORE channels), on the 10-hour cap you set.
- Mission control's "since you were away" marker is dated 08-29. You judged five queue items in it on 09-02, so you use it, but End Turn is not part of your loop. Logged as a finding in the headquarters repo.
