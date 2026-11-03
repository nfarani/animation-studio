---
description: ONE-COMMAND production — runs everything after /make (assets, prompts, generation, QA, fixes, edit package) on autopilot
argument-hint: <film-slug> [economy|balanced|quality] [budget=<credits>|low|medium|high]
---
Run /produce as defined in CLAUDE.md (section "/PRODUCE — ONE-COMMAND PRODUCTION MODE") for: $ARGUMENTS

Invoking this command is my approval to spend credits on this film's planned pipeline, up to the spend ceiling. Do not ask again per batch.

1. Parse arguments: slug (if omitted and only one project is past /make, use it; otherwise ask once), mode (default BALANCED), budget (optional).
2. Read STATUS.md, production_ledger.md, generation_log.md, 08_master_assets.md, 11_shot_list.md, qa_report.md and the adapter. Work out which stages and items are already done. Never redo finished work.
3. Validate pre-production. Apply the defaults recorded in STATUS.md for open minor decisions and note them. Stop only on a HARD STOP condition.
4. Verify the adapter (free calls only: model get, generate cost, account status), fill the tier map, then print ONE PRODUCTION PLAN with the spend ceiling. Do not wait for a reply. Proceed.
5. Run the remaining stages in order: asset specs → generate assets → validate assets → shot prompts → batch and generate shots → QA → retry / redesign failures → edit_timeline.md + audio_music.md.
6. Update production_ledger.md and generation_log.md after every batch, so the run can be resumed at any point.
7. Keep chat output minimal: one line per stage or batch. Never paste bibles, prompts, shot lists, specs or dependency maps; point to the file.
8. End with the PRODUCTION STATUS SUMMARY (credits spent vs ceiling, unresolved shots, what I still need to supply), then stop.
