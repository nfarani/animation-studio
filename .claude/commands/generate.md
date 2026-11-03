---
description: Prepare ONE paid generation batch, wait for approval, then run only that batch
argument-hint: <film-slug> <batch name, asset IDs or shot IDs>
---
Run /generate as defined in CLAUDE.md for: $ARGUMENTS

1. Check prerequisites: assets/prompts exist and dependencies are approved. If not, stop and say what is missing.
2. Run `higgsfield account status` (read-only) to check login and balance.
3. Present the READY TO GENERATE summary (items, model per item with tier, estimated credits or "unverified", purpose, remaining balance) and STOP. Wait for my explicit approval.
4. Only after I approve THIS batch: generate exactly these items, save outputs to assets/<ASSET_ID>/ or renders/<SHOT_ID>/, log model, attempts and job IDs in generation_log.md.
5. Report results, mark items as GENERATED (not approved: I approve outputs separately), update STATUS.md, and stop. Approval of this batch is not approval of any other batch.
