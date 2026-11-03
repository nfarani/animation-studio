# 14 — GENERATION STRATEGY OVERVIEW

No prompts here; those come from `/prompts` after assets are approved.

## Core method: plates first, keyframes second, motion last
1. **Master assets** (12): characters, props, environment plates.
2. **Keyframes:** for each generated shot, one still composed from the approved plate + approved character references. The keyframe is where composition, identity and continuity are checked, cheaply, before any video is made.
3. **Video:** image-to-video from the approved keyframe. Text-to-video is not used anywhere in this film.
4. **Lip-sync:** one shot only (S03_SH03).
5. **Edit-only:** two shots are pure reuse; two empty holds can be stills.

## Why this order
The film has one location and five named camera positions. Almost every shot sits on one of six plates. Getting the plates right once removes most of the continuity risk from 20 generations.

## Plate usage
| Plate | Shots built on it |
|---|---|
| ENV_PITCH_THEN_E | S01_SH01, S02_SH04 (+ ground/background for S01_SH03, S02_SH01, S02_SH02, S03_SH01, S03_SH04, S06_SH01) |
| ENV_GOAL_THEN_C | S01_SH02, S02_SH03, S03_SH02 (+ S06_SH02 by reuse) |
| ENV_PITCH_THEN_B | S03_SH03 (+ S05_SH03 by reuse) |
| ENV_PITCH_THEN_A | S04_SH01 |
| ENV_PITCH_NOW_A | S04_SH02, S05_SH01, S07_SH01 |
| ENV_PITCH_NOW_B | S05_SH04 |
| ENV_FENCE_NOW_D | S05_SH02, S06_SH03, S06_SH04 |

## Method by shot
| Method | Count | Shots |
|---|---|---|
| Keyframe → image-to-video | 15 | S01_SH01–03, S02_SH01–04, S03_SH01, S03_SH02, S03_SH04, S04_SH01, S05_SH02, S06_SH01, S06_SH03, S06_SH04 |
| Start frame + end frame → video | 1 | S05_SH01 |
| Keyframe → image-to-video (long take with timed action) | 1 | S07_SH01 |
| Keyframe → image-to-video → lip-sync | 1 | S03_SH03 |
| Still + ambient motion | 2 | S04_SH02, S05_SH04 |
| Edit-only reuse | 2 | S05_SH03, S06_SH02 |

## Shared setups (generate together)
- **Goal setup:** S01_SH02 and S03_SH02 are the same framing in two light states; S03_SH02's fallback is S01_SH02 reversed.
- **Goal from behind:** one ~4 s generation of S02_SH03 supplies S06_SH02.
- **Adult close-up:** S05_SH02 and S06_SH03 share a keyframe; one longer take may yield both.
- **ANGLE A NOW:** S04_SH02's footage also supplies the empty tail of S07_SH01.

## Recommended generation order (after assets)
1. **S03_SH03** first. It is the hero, it is reused, and S05_SH04's framing is matched to it. If it cannot be made to work, the fallback changes Scene 3's coverage, so find out early.
2. **S04_SH01 + S04_SH02.** Prove the match cut.
3. **S05_SH02 + S06_SH03.** Prove the adult performance.
4. Scene 7, then the rest of Scene 5 and 6.
5. Scenes 1 and 2 last. They are the most forgiving and the most droppable.

This order puts the shots the film cannot live without at the front, so a failure is discovered before credits are spent on shots that depend on them.

## Attempt caps
- LOW: 2 · MEDIUM: 4 · HIGH: 4, then move to the written fallback rather than a fifth try.

## Adapter prerequisites (verify during `/assets`, at no cost)
- Which image models accept multiple reference images, and how many
- Which image model does faithful image **editing** (needed for the THEN → NOW plates)
- Which video models accept a start frame, and which accept start + end frames
- Maximum clip duration per video model (S07_SH01 needs ≥ 5 s)
- Whether a lip-sync or speech-driven model is available, and its input format
- Credits per image and per second of video for each candidate model (`higgsfield generate cost`)
- Mapping of specific models to ECONOMY / STANDARD / PREMIUM
