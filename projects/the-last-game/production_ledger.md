# PRODUCTION LEDGER — The Last Game

Source of truth for resuming `/produce`. Updated 2026-10-06, run: ECONOMY, ceiling 210, spent 130.

VALIDATED = passed the agent's check. Nothing here is CREATOR-APPROVED yet.

## Master assets

| ID | Type | Tier | Model | Status | Attempts | Credits | Output path | Notes |
|---|---|---|---|---|---|---|---|---|
| CHAR_LEO_BOY_MASTER | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/CHAR_LEO_BOY_MASTER/turnaround_v1.png` |  |
| CHAR_LEO_ADULT_MASTER | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/CHAR_LEO_ADULT_MASTER/turnaround_v1.png` |  |
| CHAR_SAM_MASTER | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/CHAR_SAM_MASTER/turnaround_v1.png` |  |
| CHAR_FRIENDS_SHEET | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/CHAR_FRIENDS_SHEET/sheet_v1.png` |  |
| PROP_SHEET_MASTER | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/PROP_SHEET_MASTER/sheet_v1.png` |  |
| ENV_PITCH_THEN_E | asset | — | nano_banana_pro | LAYOUT REFERENCE ONLY | 3 | 6 | `assets/ENV_PITCH_THEN_E/plate_v2.png` | not used as a shot background |
| ENV_PITCH_THEN_A | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/ENV_PITCH_THEN_A/plate_v1.png` | match-cut frame |
| ENV_PITCH_NOW_A | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/ENV_PITCH_NOW_A/plate_v1.png` | aligned with THEN_A |
| ENV_PITCH_THEN_B | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `keyframes/S03_SH03_v1.png` | built as the S03_SH03 keyframe |
| ENV_PITCH_NOW_B | asset | — | nano_banana_pro | VALIDATED | 1 | 2 | `assets/ENV_PITCH_NOW_B/plate_v1.png` |  |
| ENV_GOAL_THEN_C | asset | — | nano_banana_pro | VALIDATED | 0 | 0 | `keyframes/S02_SH03_v1.png, S01_SH02_v1.png` | folded into shot keyframes (cost counted there) |
| ENV_FENCE_NOW_D | asset | — | nano_banana_pro | VALIDATED | 0 | 0 | `keyframes/S05_SH02_v1.png, S06_SH04_v1.png` | folded into shot keyframes (cost counted there) |

## Shots

Credits include the shot's keyframe(s) at 2 each.

| ID | Type | Tier | Model | Status | Attempts | Credits | Output path | Notes |
|---|---|---|---|---|---|---|---|---|
| S01_SH01 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S01_SH01/take1.mp4` | keyframe 2 + clip 4 |
| S01_SH02 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 8 | `renders/S01_SH02/take1.mp4` | start + end keyframes 4 + clip 4 |
| S01_SH03 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S01_SH03/take1.mp4` | background fence is wooden, not chain-link (soft focus) |
| S02_SH01 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S02_SH01/take1.mp4` |  |
| S02_SH02 | shot | — | — | DROPPED (economy) | 0 | 0 | `—` | shoulder-barge; written cheaper alternative applied without an attempt |
| S02_SH03 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S02_SH03/take1.mp4` | also supplies S06_SH02 |
| S02_SH04 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S02_SH04/take1.mp4` |  |
| S03_SH01 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S03_SH01/take1.mp4` | expression a little more worried than written |
| S03_SH02 | shot | — | — | EDIT-ONLY | 0 | 0 | `renders/S01_SH02/take1.mp4 reversed` | no hand in shot |
| S03_SH03 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 2 | 8 | `renders/S03_SH03/take2.mp4` | take1 rejected (camera push-in); no separate lip-sync pass; keyframe counted under ENV_PITCH_THEN_B |
| S03_SH04 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S03_SH04/take1.mp4` |  |
| S04_SH01 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S04_SH01/take1.mp4` | body wipe works; end frame was a locally made mustard blur (free) |
| S04_SH02 | shot | — | — | EDIT-ONLY | 0 | 0 | `first frame of renders/S05_SH01/take1.mp4, held` | still, no ambient motion |
| S05_SH01 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 7 | `renders/S05_SH01/take1.mp4` | end keyframe 2 + 5 s clip 5 |
| S05_SH02 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 8 | `renders/S05_SH02/take1.mp4` | 6 s take; also supplies S06_SH03. Reaction is bigger than specified |
| S05_SH03 | shot | — | — | EDIT-ONLY | 0 | 0 | `renders/S03_SH03/take2.mp4` | flash reuse |
| S05_SH04 | shot | — | — | EDIT-ONLY | 0 | 0 | `assets/ENV_PITCH_NOW_B/plate_v1.png` | still, no ambient motion |
| S06_SH01 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S06_SH01/take1.mp4` |  |
| S06_SH02 | shot | — | — | EDIT-ONLY | 0 | 0 | `renders/S02_SH03/take1.mp4` | reuse, 110% punch-in |
| S06_SH03 | shot | — | — | EDIT-ONLY | 0 | 0 | `renders/S05_SH02/take1.mp4 from 3.3 s` | the smile; later part of the same take |
| S06_SH04 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S06_SH04/take1.mp4` | five fingers held; palm faces camera |
| S07_SH01 | shot | ECONOMY | seedance_2_0_mini | PASSED QA* | 1 | 5 | `renders/S07_SH01/take1.mp4` | *exits right and frame ends empty; the half-second pause is NOT confirmed |

Assets 24 + shots 96 = 120 credits traced; 130 actually spent (see `generation_log.md`).

## Summary

- Master assets: 11 of 12 validated; 1 kept as layout reference only
- Shots: 22 planned → 15 generated and passed, 6 edit-only, 1 dropped, 0 unresolved
- Rough cut: `rough_cut/the-last-game_rough_v1.mp4` (37.2 s including 1.5 s of black)

---

# VERSION 2 — BALANCED (2026-10-06)

Ceiling 170, spent 120.25. Cut: `rough_cut/the-last-game_v2.mp4`, defined by `rough_cut/edl_v2.py`.

| ID | Type | Tier | Model | Status | Attempts | Credits | Output path | Notes |
|---|---|---|---|---|---|---|---|---|
| S01_SH01 | shot | STANDARD | wan3_0 | PASSED QA | 1 | 9 | `renders/S01_SH01/v2_take1.mp4` | new diagonal angle (keyframe v2) |
| S01_SH02 | shot | ECONOMY | seedance_2_0_mini | REUSED from v1 | — | 0 | `renders/S01_SH02/take1.mp4` | shortened to 0.92 s |
| S01_SH03 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S01_SH03/v2_take1.mp4` | background fence corrected |
| S02_SH01 | shot | ECONOMY | seedance_2_0_mini | REUSED from v1 | — | 0 | `renders/S02_SH01/take1.mp4` | |
| S02_SH02 | shot | STANDARD | wan3_0 | PASSED QA | 1 | 9 | `renders/S02_SH02/v2_take1.mp4` | restored; background swings during the bump |
| S02_SH03 | shot | ECONOMY | seedance_2_0_mini | REUSED from v1 | — | 0 | `renders/S02_SH03/take1.mp4` | |
| S02_SH04 | shot | STANDARD | wan3_0 | PASSED QA | 1 | 9 | `renders/S02_SH04/v2_take1.mp4` | new diagonal angle (keyframe v2) |
| S03_SH01 | shot | STANDARD | wan3_0 | PASSED QA | 1 | 7 | `renders/S03_SH01/v2_take1.mp4` | both lines present and complete |
| S03_SH02 | shot | — | — | REMOVED | — | 0 | — | reversed backpack shot cut as repetitive |
| S03_SH03 | shot | PREMIUM | seedance_2_0 | PASSED QA | 1 | 18 | `renders/S03_SH03/v2_take1.mp4` | locked frame; also the flash |
| S03_SH04 | shot | STANDARD | wan3_0 | PASSED QA | 1 | 9 | `renders/S03_SH04/v2_take1.mp4` | new over-the-shoulder angle (keyframe v2) |
| S04_SH01 | shot | ECONOMY | seedance_2_0_mini | REUSED from v1 | — | 0 | `renders/S04_SH01/take1.mp4` | |
| S04_SH02 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 4 | `renders/S04_SH02/v2_take1.mp4` | now moving (trees, grass) |
| S05_SH01 | shot | ECONOMY | seedance_2_0_mini | REUSED from v1 | — | 0 | `renders/S05_SH01/take1.mp4` | |
| S05_SH02 | shot | PREMIUM | seedance_2_0 | PASSED QA | 1 | 20 | `renders/S05_SH02/v2_take1.mp4` | calmer keyframe; restrained recognition |
| S05_SH03 | shot | — | — | EDIT-ONLY | — | 0 | `renders/S03_SH03/v2_take1.mp4` | flash |
| S05_SH04 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 4 | `renders/S05_SH04/v2_take1.mp4` | now moving |
| S06_SH01 | shot | ECONOMY | seedance_2_0_mini | REUSED from v1 | — | 0 | `renders/S06_SH01/take1.mp4` | |
| S06_SH02 | shot | — | — | REMOVED | — | 0 | — | second ball-between-bags shot cut as repetitive |
| S06_SH03 | shot | ECONOMY | seedance_2_0_mini | PASSED QA | 1 | 6 | `renders/S06_SH03/v2_take1.mp4` | own smile keyframe; first 2.3 s unusable (open-mouth exhale) |
| S06_SH04 | shot | ECONOMY | seedance_2_0_mini | REUSED from v1 | — | 0 | `renders/S06_SH04/take1.mp4` | |
| S07_SH01 | shot | STANDARD | wan3_0 | PASSED QA | 1 | 8.75 | `renders/S07_SH01/v2_take1.mp4` | the pause is in the take (about 2.5–3.1 s) |
| AUDIO | audio | — | mirelo_text_to_audio | NOT LISTENED TO | 1 each | 10.5 | `audio/` | two ambience beds, one distant memory sound |

Shots in version 2: 20 in the cut (8 new clips on standard/premium, 4 new economy clips, 7 reused v1 clips, 1 edit-only flash). 2 removed.
