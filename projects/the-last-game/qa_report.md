# QA REPORT — The Last Game

/produce (ECONOMY), 2026-10-06. Reviewed by the agent from extracted frames of every clip and a one-frame-per-second sheet of the rough cut.

**Limits of this review:** frames only. Motion between sampled frames was not watched at speed, and **no audio was listened to**. Anything about timing of speech, voice quality or sound is unverified.

## Result
15 clips generated, 15 accepted. 1 take rejected and redone. 0 unresolved shots. Rough cut assembled.

## Findings, by severity

### 1. HIGH — Audio is unverified and incomplete
Every spoken line comes from the video model, generated separately per clip. Voices almost certainly do not match between shots, and Sam's line may not sync to his mouth. The ending's memory sounds are absent.
**Fix:** listen; then record or replace voices and build a proper mix (`audio_music.md`).

### 2. MEDIUM — S07_SH01: the pause is not confirmed
He turns from the fence, walks right, exits, and the frame ends empty, as specified. Sampled frames show steady progress across the frame, so the half-second pause is probably missing.
**Fix:** check at speed. If missing, one regeneration (5 credits) with the pause as the only instruction, or cut without it.

### 3. MEDIUM — S05_SH02 / S06_SH03: performance is bigger than written
Recognition plays with widened eyes and an open mouth; the smile is a clear smile rather than a barely-there one. The film asks for restraint ("a small smile, not sad"). It is not sad, but it is not small.
**Fix:** in the edit, use the earliest frames of the smile (done: in-point 3.30). For a subtler read, regenerate the 6 s take with a keyframe as both first and last frame, which limits how far the face can travel (6 credits).

### 4. MEDIUM — Location geography is simplified
The pitch reads as shallow, with the gateway in the middle of the fence and the terrace close behind. Sam's shot, the match-cut frame and the "running home" shot all show a similar fence-and-terrace background, so the audience cannot tell inside from outside views apart. It is consistent, but less spatially clear than the plan.
**Fix:** none recommended at this budget. Noted in `assets/asset_specs.md`.

### 5. LOW — S01_SH03: wooden fence in the background
The feet insert shows a wooden paling fence, soft-focus, instead of chain-link. 1.5 s, out of focus.
**Fix:** regenerate the keyframe with the pitch plate as reference (2 + 4 credits), or leave.

### 6. LOW — Present-day plates differ slightly from each other
The trees in the present-day view behind Sam's empty spot are larger and fewer than in the present-day wide. Small young trees remain visible at the fence in the present-day wide.
**Fix:** leave; the shots are not adjacent.

### 7. LOW — Stills are frozen
S04_SH02 and S05_SH04 have no movement at all. A few pixels of foliage sway would help the reveal.
**Fix:** add in the edit, or generate 4 s of ambient motion each with locked first/last frame (8 credits).

### 8. LOW — Sock continuity
Which of Leo's socks is down varies between shots. Not noticeable at speed.

### 9. INFO — S02_SH02 dropped
The shoulder-barge was never attempted (economy rule: go straight to the cheaper alternative). Scene 2 runs feet → goal → chase.

## Checks
| Check | Result |
|---|---|
| Story: every beat of the script present | PASS, except the barge (dropped) and the final-shot sounds (audio, pending) |
| Character identity across shots | PASS — Leo, Sam, Danny, Kit hold; adult reads as the same person |
| Match cut alignment (S04_SH01 → S04_SH02) | PASS — body wipe covers the frame; fence and gateway align |
| Sam's frame vs the empty frame (S05_SH03 → S05_SH04) | PASS — same framing, bare earth where he stood |
| Screen direction | PASS — boy and man both leave toward frame right / the path |
| Prop continuity | PASS — two bags, then one; ball stays with Sam; nothing in the present |
| Locked camera where required | PASS after one retake (S03_SH03) |
| Hands | PASS — S06_SH04 holds five fingers through the move |
| Extra characters, text, logos | none found |
| Model overspend | none — no standard or premium video model used |
| Spend | 130 of 210 credits |
