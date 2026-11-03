---
description: Shot-specific, tool-adapted production prompts (approved assets only)
argument-hint: <film-slug> [scene or shot IDs]
---
Run /prompts as defined in CLAUDE.md for: $ARGUMENTS

First check that every required master asset for the requested shots is approved in 08_master_assets.md. If not, list what is missing and stop, recommending /assets or /generate.

Write prompts into prompts/<SCENE>_<tool>.md. Each shot includes: SHOT ID, DURATION, GENERATION METHOD, MODEL TIER + specific model with rationale, REFERENCE ASSETS, INITIAL STATE, ACTION, FINAL STATE, SUBJECT, ENVIRONMENT, CAMERA, COMPOSITION, LIGHTING, PERFORMANCE, MOOD, CONTINUITY, STYLE, NEGATIVE CONSTRAINTS, AUDIO CONTEXT, FALLBACK PROMPT. Adapt from the master shot spec using adapters/<tool>.md. Set stage to SHOT PROMPTING. No generation.
