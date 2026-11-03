# CANON_PRIORITY — Dan & the Dandruffs

Creator's rule of 2026-10-06 (verbatim copy in `00_source/canon_priority.md`).

When generating assets, scenes, prompts or scripts, follow this hierarchy:

| # | Level | Where it lives in this project |
|---|---|---|
| 1 | WORLD_BIBLE.md | `WORLD_BIBLE.md` |
| 2 | CHARACTER_BIBLE.md | `CHARACTER_BIBLE.md` |
| 3 | STYLE_BIBLE.md | `STYLE_BIBLE.md` in this folder (not the channel-wide one at the repository root) |
| 4 | Approved master reference images | `assets/*_MASTER/`, only those marked CREATOR-APPROVED |
| 5 | Episode script | per episode, once written |
| 6 | Individual shot prompt | `prompts/` |

Lower-level material may add detail but must not contradict higher-level canon.

If an established term appears in a script: consult the World Bible before interpreting it.

Never reinterpret an established world term.

Example: Burning Tsunami = anti-dandruff shampoo. Do not generate fire, lava or literal flames unless explicitly required by canon.

## How this is applied
- Before any asset, scene, prompt or script: read levels 1–3, then the relevant approved masters.
- When two levels disagree, the higher one wins and the lower one is corrected; the conflict is reported to the creator.
- Images that are generated but not yet approved are not canon.
