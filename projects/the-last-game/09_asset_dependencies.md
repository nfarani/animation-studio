# 09 — ASSET DEPENDENCY MAP

Rule: nothing is generated before everything above it is approved.

## Graph

```
TIER 0 (no dependencies)
  CHAR_LEO_BOY_MASTER     CHAR_SAM_MASTER     CHAR_FRIENDS_SHEET     PROP_SHEET_MASTER     ENV_PITCH_THEN_E

TIER 1
  CHAR_LEO_BOY_MASTER ──► CHAR_LEO_ADULT_MASTER
  ENV_PITCH_THEN_E ─────► ENV_PITCH_THEN_A
  ENV_PITCH_THEN_E ─────► ENV_PITCH_THEN_B
  ENV_PITCH_THEN_E + PROP_SHEET_MASTER ──► ENV_GOAL_THEN_C

TIER 2 (era edits — same pixels, aged)
  ENV_PITCH_THEN_A ─────► ENV_PITCH_NOW_A
  ENV_PITCH_THEN_B ─────► ENV_PITCH_NOW_B

TIER 3
  ENV_PITCH_NOW_A ──────► ENV_FENCE_NOW_D

TIER 4 (shots)
  see table below
```

## Shot → required assets
| Shot | Characters | Environment | Props |
|---|---|---|---|
| S01_SH01 | LEO_BOY, SAM, FRIENDS | THEN_E | PROP_SHEET |
| S01_SH02 | — | GOAL_THEN_C (reverse view) | PROP_SHEET |
| S01_SH03 | LEO_BOY (legs), FRIENDS (Kit's foot) | THEN_E (ground texture) | PROP_SHEET |
| S02_SH01 | LEO_BOY (legs) | THEN_E (ground texture) | PROP_SHEET |
| S02_SH02 | LEO_BOY, FRIENDS (Danny's shoulder) | THEN_E | — |
| S02_SH03 | — | GOAL_THEN_C | PROP_SHEET |
| S02_SH04 | LEO_BOY, SAM, FRIENDS | THEN_E | PROP_SHEET |
| S03_SH01 | LEO_BOY | THEN_E (low sun) | — |
| S03_SH02 | LEO_BOY (hand) | GOAL_THEN_C | PROP_SHEET |
| S03_SH03 | SAM | THEN_B | PROP_SHEET |
| S03_SH04 | LEO_BOY | THEN_E (low sun) | PROP_SHEET |
| S04_SH01 | LEO_BOY | **THEN_A** | PROP_SHEET |
| S04_SH02 | — | **NOW_A** | — |
| S05_SH01 | LEO_ADULT | **NOW_A** | PROP_SHEET |
| S05_SH02 | LEO_ADULT | FENCE_NOW_D | — |
| S05_SH03 | *edit-only reuse of S03_SH03* | | |
| S05_SH04 | — | NOW_B | — |
| S06_SH01 | SAM, FRIENDS | THEN_E | PROP_SHEET |
| S06_SH02 | *edit-only reuse of S02_SH03 (second half of the same generation)* | | |
| S06_SH03 | LEO_ADULT | FENCE_NOW_D | — |
| S06_SH04 | LEO_ADULT (hand) | FENCE_NOW_D (macro) | — |
| S07_SH01 | LEO_ADULT | **NOW_A** | PROP_SHEET |

## Shot → shot dependencies
```
S03_SH03 ──► S05_SH03   (same clip; must exist and be approved first)
S03_SH03 ──► S05_SH04   (framing of the NOW_B hold is matched to the approved S03_SH03 frame)
S02_SH03 ──► S06_SH02   (same generation, later portion)
S04_SH01 ──► S04_SH02   (cut point: last frame of the wipe decides the first frame of the hold)
S05_SH01 ──► S07_SH01   (Leo's standing position at the fence must match between them)
S05_SH02 ──► S06_SH03   (same setup; same wire pattern, same framing)
```

## Regeneration impact (if an approved asset changes)
| If this changes | Regenerate |
|---|---|
| CHAR_LEO_BOY_MASTER | CHAR_LEO_ADULT_MASTER + all 9 boy shots + all 5 adult shots |
| CHAR_LEO_ADULT_MASTER | S05_SH01, S05_SH02, S06_SH03, S06_SH04, S07_SH01 |
| CHAR_SAM_MASTER | S01_SH01, S02_SH04, S03_SH03 (and therefore S05_SH03), S06_SH01 |
| CHAR_FRIENDS_SHEET | S01_SH01, S01_SH03, S02_SH02, S02_SH04, S06_SH01 |
| PROP_SHEET_MASTER | ENV_GOAL_THEN_C + every THEN shot with ball or bags |
| ENV_PITCH_THEN_E | **every environment plate and every shot** |
| ENV_PITCH_THEN_A | ENV_PITCH_NOW_A, ENV_FENCE_NOW_D, S04_SH01, S04_SH02, S05_SH01, S07_SH01 |
| ENV_PITCH_NOW_A | ENV_FENCE_NOW_D, S04_SH02, S05_SH01, S07_SH01 |
| ENV_PITCH_THEN_B | ENV_PITCH_NOW_B, S03_SH03, S05_SH03, S05_SH04 |
| ENV_PITCH_NOW_B | S05_SH04 |
| ENV_GOAL_THEN_C | S01_SH02, S02_SH03, S06_SH02, S03_SH02 |
| ENV_FENCE_NOW_D | S05_SH02, S06_SH03, S06_SH04 |

## Recommended approval order
1. **Batch 1 — identity:** CHAR_LEO_BOY_MASTER, CHAR_SAM_MASTER, PROP_SHEET_MASTER, ENV_PITCH_THEN_E
2. **Batch 2 — derived:** CHAR_LEO_ADULT_MASTER, CHAR_FRIENDS_SHEET, ENV_PITCH_THEN_A, ENV_PITCH_THEN_B, ENV_GOAL_THEN_C
3. **Batch 3 — era edits:** ENV_PITCH_NOW_A, ENV_PITCH_NOW_B, ENV_FENCE_NOW_D

Each batch needs its own approval before generation.
