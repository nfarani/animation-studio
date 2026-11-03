# CHANGELOG — The Last Game

## 2026-10-06 — /produce economy
- **S02_SH02 dropped.** Economy mode applied the written cheaper alternative (`17_high_risk_fallbacks.md`) without an attempt. Scene 2 is now three shots.
- **S03_SH02 became edit-only:** S01_SH02 played in reverse (the red bag lifts away). No hand in the shot.
- **S04_SH02 and S05_SH04 became stills** (no ambient motion generated).
- **S06_SH03 became edit-only:** the later part of the S05_SH02 take.
- **S03_SH03: no lip-sync pass.** The video model animated the mouth from the quoted line in the prompt. Take 1 rejected for a camera push-in; take 2 locked by using the keyframe as both first and last frame.
- **S04_SH01: the wipe was generated**, using a locally made blurred mustard image as the end frame.
- **S05_SH01 and S07_SH01 use first/last frame pairs** (empty plate ↔ man at the fence) to control entry and exit.
- **Environment plan changed.** ENV_PITCH_THEN_E is a layout reference only; ENV_PITCH_THEN_A became the look reference for all pitch views. ENV_PITCH_THEN_B, ENV_GOAL_THEN_C and ENV_FENCE_NOW_D were not made as separate plates; they exist as shot keyframes. Geography is simpler than `06_environment_bible.md` describes (see `assets/asset_specs.md`).
- **Every shot planned as STANDARD or PREMIUM was made on the economy video model.**
- **Runtime:** rough cut is 35.75 s of picture against a 34.0 s plan.
- New files: `assets/asset_specs.md`, `keyframes/`, `prompts/used_prompts.md`, `renders/`, `rough_cut/`, `generation_log.md`, `production_ledger.md`, `edit_timeline.md`, `audio_music.md`, `qa_report.md`.
- `11_shot_list.md` (the master spec) was not rewritten; the changes above are deviations from it, recorded here and in `production_ledger.md`.

## 2026-10-06 — Version 2 (balanced), after creator feedback on the rough cut
Creator feedback: "some of the editing is weird, some scenes are a bit repetitive and slow like the backpack one"; asked for a balanced model stack, no voices cut off, a clean edit for YouTube, and less repetition.

Found in version 1: five lines were cut mid-word by the edit ("Yeah, obviously.", the mother's call, "Coming!", both halves of the goal argument); one shot was a reversed clip with reversed sound; two shots were frozen stills; the backpacks appeared four times; every wide shot used the same flat fence-on view.

Changed:
- **Removed** S03_SH02 (reversed backpack shot) and S06_SH02 (second ball-between-bags shot). S01_SH02 shortened from 1.30 to 0.92 s.
- **Restored** S02_SH02 (shoulder bump) on the standard model: a face in the middle of the game fragments.
- **New camera angles** for S01_SH01 and S02_SH04 (diagonal view down the fence) and S03_SH04 (over Sam's shoulder), so the wides no longer all look alike.
- **Regenerated on better models:** S03_SH03 and S05_SH02 on premium; S01_SH01, S02_SH02, S02_SH04, S03_SH01, S03_SH04, S07_SH01 on standard.
- **S05_SH02 / S06_SH03:** new calmer keyframe; recognition and smile are now separate takes, the smile from its own keyframe.
- **S07_SH01:** the half-second pause is now in the shot.
- **S04_SH02 and S05_SH04** are moving shots instead of frozen stills. **S01_SH03** background fence corrected.
- **Sound rebuilt:** picture and sound are cut separately; lines run across cuts; continuous background under each half; silence at the wipe and at the end; distant memory sound at the final pause; loudness set to −14 LUFS.
- **Export:** 1080p, constant 24 fps, BT.709.
- New tooling: `rough_cut/build_cut.py` (stops the build if a cut lands in a spoken line) and `rough_cut/edl_v2.py`.
- Runtime 34.54 s including black (version 1: 37.25 s).
