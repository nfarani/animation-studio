# MASTER ASSET SPECS — as built by /produce (ECONOMY), 2026-10-06

Designs follow `05_character_bible.md`, `06_environment_bible.md`, `07_prop_bible.md`. The exact prompt sent for every asset is recorded in `prompts/used_prompts.md` under the same output path. All assets: model `nano_banana_pro`, 16:9, 2k, 2 credits per attempt.

Status **VALIDATED** means checked by the agent against the bibles. None is CREATOR-APPROVED yet.

| Asset ID | File | Method | Reference inputs | Attempts | Status | Notes |
|---|---|---|---|---|---|---|
| CHAR_LEO_BOY_MASTER | `CHAR_LEO_BOY_MASTER/turnaround_v1.png` | text-to-image, 4-view turnaround | — | 1 | VALIDATED | Ears, crown tuft, mustard/teal correct. One sock is down, but which leg varies between views. |
| CHAR_SAM_MASTER | `CHAR_SAM_MASTER/turnaround_v1.png` | reference-image, 4-view turnaround | Leo boy (style) | 1 | VALIDATED | Tooth gap, curls, pushed-up sleeves correct. |
| CHAR_FRIENDS_SHEET | `CHAR_FRIENDS_SHEET/sheet_v1.png` | reference-image, 2 characters front/back | Leo boy (style) | 1 | VALIDATED | Danny and Kit; relative heights correct. |
| PROP_SHEET_MASTER | `PROP_SHEET_MASTER/sheet_v1.png` | reference-image | Leo boy (style) | 1 | VALIDATED | Ball, red and navy backpacks, grey messenger bag. |
| CHAR_LEO_ADULT_MASTER | `CHAR_LEO_ADULT_MASTER/turnaround_v1.png` | reference-image, derived from the boy | Leo boy | 1 | VALIDATED | Reads clearly as the same person: ears, tuft, brows, ochre jumper. |
| ENV_PITCH_THEN_E | `ENV_PITCH_THEN_E/plate_v2.png` | reference-image | plate_v1 | 3 | LAYOUT REFERENCE ONLY | v1 had the trees on the wrong side. v2 and v3 have the right layout but a low fence and a raised camera. Not used as a shot background. |
| ENV_PITCH_THEN_A | `ENV_PITCH_THEN_A/plate_v1.png` | reference-image | E v2, E v1, prop sheet | 1 | VALIDATED | The locked match-cut frame. Became the look reference for every other pitch view. |
| ENV_PITCH_NOW_A | `ENV_PITCH_NOW_A/plate_v1.png` | image edit of THEN_A | THEN_A | 1 | VALIDATED | Posts, gateway, path and horizon line up with THEN_A. The original saplings are still faintly visible in front of the grown trees. |
| ENV_PITCH_THEN_B | `../keyframes/S03_SH03_v1.png` | built directly as the S03_SH03 keyframe | Sam, THEN_A, prop sheet | 1 | VALIDATED | No separate empty plate was made (economy). |
| ENV_PITCH_NOW_B | `ENV_PITCH_NOW_B/plate_v1.png` | image edit of the S03_SH03 keyframe | S03_SH03 keyframe | 1 | VALIDATED | Same framing, Sam and ball removed, bare earth where he stood. |
| ENV_GOAL_THEN_C | `../keyframes/S02_SH03_v1.png`, `../keyframes/S01_SH02_v1.png` | built directly as shot keyframes | prop sheet, S03_SH03 keyframe | 1 each | VALIDATED | No separate plate (economy). |
| ENV_FENCE_NOW_D | `../keyframes/S05_SH02_v1.png`, `../keyframes/S06_SH04_v1.png` | built directly as shot keyframes | Leo adult, NOW_A | 1 each | VALIDATED | No separate plate (economy). |

## Deviations from the pre-production design
1. **Geography.** The generated ANGLE A view is flatter and shallower than the plan in `06_environment_bible.md`: the gateway is in the centre of the frame, it has a gate leaf (open), and the far fence is close behind the pitch. Sam's shot (ANGLE B) uses the same fence-and-terrace background. This was accepted because the views are consistent with each other.
2. **Navy backpack position.** In ANGLE A it sits near the fence, left of the gateway, rather than out on the pitch.
3. **Tree count.** Five saplings are visible in ANGLE A, not six.
4. **Four plates folded into keyframes** (THEN_B, GOAL_C, FENCE_D), saving separate generations.
