# 13 — PRODUCTION RISK ANALYSIS

Ranked by how much damage a failure does to the film, not by how likely it is.

## 1. ANGLE A alignment between eras — FILM-CRITICAL
- **What:** S04_SH01 → S04_SH02 only works if the fence, gateway, path edge and horizon sit in the same place in both plates.
- **Why it is a risk:** two independently generated images of "the same place" never line up.
- **Mitigation:** ENV_PITCH_NOW_A is produced by **editing** ENV_PITCH_THEN_A, not by generating a new image. Approval test is a 50% overlay. Both shots are locked-off, so the plates carry the match. Small residual misalignment is corrected with a transform in the edit.
- **Residual risk:** LOW once the plates pass the overlay test.

## 2. Leo boy ↔ Leo adult likeness — FILM-CRITICAL
- **What:** with no text and no voiceover, the audience must see that the man is the boy.
- **Mitigation:** adult master derived from the boy master; three redundant identifiers (ears + crown tuft, mustard → ochre, right-thumb strap hitch); he enters the same locked frame the boy just left; he exits the same side.
- **Residual risk:** LOW–MEDIUM. Even if the face likeness is only approximate, the cut and the staging make the reading unavoidable.

## 3. S03_SH03 — the one lip-synced line, used twice — HIGH
- **What:** Sam's "You coming tomorrow?" is the hinge of the film and plays twice.
- **Risks:** mouth mismatch, identity drift, camera creep.
- **Mitigation:** full-shot scale (small mouth), locked camera, 1.8 s, one line, no other action. Lip-sync capability on the adapter is UNVERIFIED and must be verified before this shot is attempted.
- **Fallbacks:** `17_high_risk_fallbacks.md`.

## 4. Child voices — NOT YET SOLVED
- **What:** the film needs four children's voices and one adult woman, eight short lines plus laughter and shouting.
- **Why it is a risk:** synthetic child voices often sound adult or uncanny, and playground walla is hard to fake convincingly.
- **Options:** (a) record real voices (best result; needs children and consent from their parents); (b) synthetic voices via the tool's voice features (UNVERIFIED on the adapter); (c) licensed library recordings for laughter and walla, with only the five distinct lines synthesised or recorded.
- **Recommendation:** (c), with (a) for the two lines that matter: "You coming tomorrow?" and "Yeah, obviously."
- **Decision needed:** by `/edit` at the latest; before S03_SH03 if lip-sync is driven by the audio file.

## 5. Scene 2 fragments — MEDIUM, contained
- **What:** fast motion, ball contact, body contact.
- **Mitigation:** every fragment is ≤ 1.5 s, framed on a part (feet, a shoulder, the goal), with motion blur expected. S02_SH02 can be dropped entirely without harming the story.

## 6. Over-acting in the adult close-ups — MEDIUM
- **What:** generation models default to big emotion: wet eyes, trembling lips, a slow sad smile.
- **Mitigation:** performance is specified physically and in millimetres; explicit negative constraints at `/prompts` (no tears, no looking down, no swallowing). Expect to reject takes for being too much.

## 7. Hand on chain-link (S06_SH04) — HIGH likelihood, LOW damage
- Hands plus a fine repeating mesh is a known failure combination. Starts in contact to remove the approach. Capped at 4 attempts, then fallback. The beat survives as a wide from behind.

## 8. Unwanted camera movement on locked shots — MEDIUM
- **What:** S04_SH01, S04_SH02, S05_SH01, S05_SH04, S07_SH01 must not drift.
- **Mitigation:** static-camera instruction; stabilise in the edit; the two empty holds can be pure stills.

## 9. Runtime — LOW
- 34.0 s against a ~30 s brief. A 30.1 s trim is defined (`02_creative_notes.md`, note 1).

## 10. Adapter knowledge — MEDIUM, cheap to fix
- Only CLI access, balance and the model list are verified. Reference-image support, start/end-frame control, lip-sync, duration limits and per-model cost are all UNVERIFIED. These must be verified (free: `higgsfield model get <model>`, `higgsfield generate cost ...`) during `/assets`, before any batch is proposed.

## Risk by shot
| Risk | Shots |
|---|---|
| **HIGH (4)** | S02_SH02, S03_SH03, S04_SH01, S06_SH04 |
| **MEDIUM (12)** | S01_SH01, S01_SH03, S02_SH01, S02_SH04, S03_SH01, S03_SH02, S03_SH04, S05_SH01, S05_SH02, S06_SH01, S06_SH03, S07_SH01 |
| **LOW (4)** | S01_SH02, S02_SH03, S04_SH02, S05_SH04 |
| **None, edit-only (2)** | S05_SH03, S06_SH02 |
