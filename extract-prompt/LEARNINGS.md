# Learnings — extract-prompt

Accumulated, user-ratified heuristics about this user's prompting patterns and the
prompt-extraction workflow. Read this at the start of every run; apply what's here. Append
new lessons only after the user confirms them (one line each). Prune or correct freely — a
bad lesson is one line to delete. Stable lessons graduate into `SKILL.md` and leave here.

<!-- Format: - [YYYY-MM-DD] <the heuristic>. -->

- [2026-06-30] When the target model isn't Claude, find that out early — and especially ask early about the run mechanics (agentic file reading vs. inline content). With sensitive data this also decides whether structure is transferred to the model by having it read a pattern/example file rather than embedding examples in the prompt.
- [2026-07-21] For open-ended/exploratory agent prompts, specify the job and constraints, not the method. Prescribing *how to think* (e.g. "brainstorm wide," "include wildcards," "cast a broad net then narrow") biases the exact capability the user is outsourcing to the agent. Watch for method-verbs sneaking into a prompt that's meant to describe an outcome.
