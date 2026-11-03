---
description: Solve a failed or problematic shot, preferring editorial solutions
argument-hint: <film-slug> <SHOT ID> [what went wrong]
---
Run /fix as defined in CLAUDE.md for: $ARGUMENTS

Diagnose the failure mode. Check generation_log.md for previous attempts. If the shot has already failed reasonably (e.g. 2+ attempts), do not just rewrite the prompt: reconsider the filmmaking (change angle, simplify, split, move action off-screen, use reaction / insert / sound, shorten, use a still, composite, change method or tier).

Preserve the STORY BEAT, not the original execution. Present the redesign with its tier and expected attempts, update the shot list, prompts and continuity ledger, log in CHANGELOG.md. Any regeneration goes through /generate approval.
