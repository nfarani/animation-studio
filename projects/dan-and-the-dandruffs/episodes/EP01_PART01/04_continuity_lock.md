# EP01 — LOCKED CONTINUITY NOTES (for Parts 2–5)

Set by the approved Part 1: **the hook cut, approved by the creator on 2026-10-07** (it replaces the earlier approved cut, kept in `deliverables/v1_previous/`). Parts 2–5 reuse these files and settings as they are. Change one only on the creator's instruction, and then in every part.

Status key: **LOCKED** = fixed by an approved asset or by reuse of the same file. **PROVISIONAL** = used in Part 1, not yet confirmed by the creator's ear or eye.

## Designs (LOCKED — creator-approved masters)
| What | Reference |
|---|---|
| Dan | `../../assets/CHAR_DAN_MASTER/hero_v1.png` |
| General Arrow | `../../assets/CHAR_GENERAL_ARROW_MASTER/hero_v1.png` |
| Senior Scalpetist | `../../assets/CHAR_SENIOR_SCALPETIST_MASTER/hero_v1.png` |
| Scalpence Centre | `../../assets/ENV_SCALPENCE_CENTRE_MASTER/hero_v3.png` |
| Flake, Grandpa Snow, Pale (not in Part 1) | their masters in `../../assets/` |
| Tiny Tales logo | `../../references/tiny-tales-logo.jpeg` |

## Designs introduced in Part 1 (LOCKED — approved with the cut, 2026-10-07)
| What | As seen in | Notes |
|---|---|---|
| Scalpetist staff | `keyframes/S3_SH07.png`, `S3_SH01.png` | Flakes of varied shapes in plain bone smocks with slate-blue trim; no loupes. Reuse these keyframes as references. |
| Dan's three friends | `keyframes/S1_SH01_wool.png` (wool and cloth, from 2026-10-20; the old look in `S1_SH01.png` is superseded) | A taller girl with two dark braids in a moss-green jacket; a short sandy-haired boy in a blue anorak; a girl with curly ginger hair in a plum jumper. Working names Maya, Ollie and Ruby are the director's and are never spoken. |
| School street | `keyframes/S1_SH01_wool.png` | Felted bricks with stitched mortar, yarn-wrapped gate and tree, crocheted leaves, felt pavement; warm, softened afternoon light. |
| Head Centre bell tower | `keyframes/S4_SH01.png` | Slender wrapped-sheet tower beside the canopied hall. Its bell looks grey and metallic; ideally it would be pale layered sheet like the Centre's. |
| Head Centre townspeople | `keyframes/S4_SH01.png` | Flakes in muted wraps, aprons and shawls. |
| The townsperson on the bridge | `keyframes/CO_SH02.png` | A round flake in a moss-green shawl and clay apron with a basket. Opens the episode. |
| Dan's hair, close | `keyframes/HAIR_MACRO_wool.png` | Thick dark twisted yarn with a golden glow between the strands; the dive starts here and the strands become the Forest Trees. |
| The world from above | `keyframes/S2_MID.png`, `S2_END.png` | The Scalpence Centre seen from above among the Forest Trees. |

## Scalpence Centre layout (LOCKED by the approved image)
Open-air terraced bowl, no roof. Centre pit: armillary. Left of it: the row of seismic drums. Right of it: the roped enclosure with two netted vessels (one pale blue), and the resonance harp. Foreground right: a large amber lens on a stand. Rim, upper left: the warning bell in its frame and the rack of signal horns. Rim: the signal mast with the dusty-blue flag (raised from the end of Part 1 onward). Walls: charts of orbits, grids and wave traces. Work tables all round the upper terrace.

**State at the end of Part 1:** flag raised; warning bell tolling; lenses manned and pointing up; staff at their posts; General Arrow on the upper terrace; the Senior Scalpetist at the seismic drums.

## Voices (LOCKED — approved with the cut, 2026-10-07)
| Role | Source | Status |
|---|---|---|
| Narrator | Text-to-speech, engine `text2speech_v2` / `elevenlabs`, preset voice **Arthur**, id `30fc8796-ceb6-4a66-b3a7-4a145ef7f346`. Lines in `audio/narr_Arthur_*.mp3` | LOCKED |
| General Arrow | The version 1 voice, generated with the picture (takes `renders/S3_SH04_take1`, `S3_SH06A_take1`, `S3_SH06B_take1`). Reference recording for all later parts: `audio/arrow_voice_ref.mp3`. Pass it as an audio reference whenever he speaks. | LOCKED |
| Senior Scalpetist | The brisk, matter-of-fact take (`renders/S3_SH05_take3`), in the same voice as his first take. Reference for later parts: `audio/scalpetist_voice_ref.mp3`. The earlier, slower reference is `scalpetist_voice_ref_v1_previous.mp3`. | LOCKED |
| Scalpetist group | `renders/S3_SH13_take1.mp4` | LOCKED |

**History:** the creator asked for an angrier General Arrow, a dreamier Senior Scalpetist and a sombre threat cue; version 2 was made with those changes; the creator then said "I actually prefer the first version" and approved version 1. The version 2 voices and cue are **not** canon. Their files are kept, marked `_v2_not_approved` / in `deliverables/v2_not_approved/`, and must not be used as references.

## Sound (LOCKED by reusing the same files)
| Element | File | Use |
|---|---|---|
| Series music motif | `audio/music_motif.m4a` (45 s: sparse opening, groove from about 15 s) | Reuse this recording; do not regenerate. Enters on the descent; sits about 11 dB under dialogue. |
| Tiny Tales sting | `audio/sting_ident.m4a` | Under the outro card of every part. |
| Warning bell | `audio/warning_bell.mp3` | The series' warning sound. Close at the Centre, quieter across Head Centre. |
| Scalpence Centre ambience | `audio/bed_scalpence.mp3` | Under every Centre scene. Drops out for a Long Foot line. |
| Scale boom | `audio/scale_boom.mp3` | When the human world is heard from inside. |
| Long Foot sonic identity | none | As approved in version 1: the ambience and music withdraw when the words are spoken. The sombre cue made for version 2 (`audio/music_threat.m4a`) was not approved and is not used. |

These are the sounds of the approved version 1.

## Picture language
- 16:9, 24 fps, delivered at 1080p (sources 720p). Key action near centre.
- Human world: relaxed tracking at child height, observational. Hidden world: mostly locked or slow, at the characters' eye height.
- Entering the world: one continuous descent, built as chained clips between shared keyframes.
- Dialogue: a long take per speech with cutaways laid over it; the speaker's sound never cut.
- Hard cuts. One dissolve only, into the outro card.
- Hidden-world palette: bone, cream, oat and honey-amber against dark Forest Trees, pale-gold sky; the only blue is the sealed vessel and the signal flag.

## Opening and closing format (LOCKED — approved with the cut, 2026-10-07)
- **Cold open first.** Each part opens inside the dandruff world, before any title. Part 1: the town at peace, one enormous distant boom, a townsperson on a thread bridge looks up and sighs.
- **No separate intro card and no intro sting.** The Tiny Tales wordmark and the title (`cards/title_overlay_part1.png`) ride over a moving shot for about 4.5 s, where the music begins. Avenir Next, letter-spaced capitals, charcoal with a soft cream halo. For Parts 2–5 only the part number changes.
- **Human world kept brief.** Dan's section is under 7 s.
- **Outro, about 2.2 s:** the last shot dissolves to the logo card with "CONTINUES IN PART 2" (`cards/outro_part1.png`), with the Tiny Tales sting (`audio/sting_ident.m4a`). For Part 5, no "continues" line.
- CLEAN versions have the cold open and no title overlay or outro.
- Edit: `edit/edl_part01.py`, `edit/build_cut.py`.

## Editing rule from Part 1
If a clip's background jumps mid-shot, split the shot there and cover the join with a cutaway (as done on General Arrow's entrance).

## Where Part 2 picks up
Head Centre, moments later: the bell tolling, citizens looking up. Flake has not been seen. Nothing has been explained about Long Foots, contaminated Heads or wet soil.
