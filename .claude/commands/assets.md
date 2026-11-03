---
description: Production-ready master asset specs, grouped into approval batches
argument-hint: <film-slug>
---
Run /assets as defined in CLAUDE.md for: $ARGUMENTS

For every master asset in 08_master_assets.md write: ASSET ID, ASSET TYPE, PRIORITY, DESCRIPTION, VISUAL DESIGN, STYLE, POSE / VIEW REQUIREMENTS, LIGHTING, BACKGROUND, CONTINUITY RULES, DEPENDENT SHOTS, RECOMMENDED GENERATION METHOD, RECOMMENDED MODEL TIER (+ MODEL / WHY / REQUIRED BECAUSE / CHEAPER OPTION / QUALITY TRADEOFF), GENERATION PROMPT, NEGATIVE CONSTRAINTS.

Group into batches (e.g. BATCH 1 Main Characters, BATCH 2 Recurring Environments, BATCH 3 Hero Props, BATCH 4 Variants). Update 09_asset_dependencies.md. Set stage to ASSET DESIGN.

Do NOT generate. End with the READY TO GENERATE summary for BATCH 1 and the PRODUCTION STATUS SUMMARY (next action: /generate <slug> batch 1).
