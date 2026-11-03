# EP01 PART 1 — QA REPORT

2026-10-06. Reviewed by the agent from extracted frames, transcripts and audio measurements.
**The agent cannot hear and did not watch the cut at speed.** Passes 3, 4, 5 and 6 are therefore incomplete and need the creator's ears.

| Pass | Result | How it was checked |
|---|---|---|
| 1 Character consistency | PASS with notes | Frames from every clip against the approved masters |
| 2 Environment continuity | PASS with notes | Frames against the approved Scalpence Centre |
| 3 Lip-sync | **NOT VERIFIED** | Speech and picture were generated together; mouths move during lines and are closed after them in sampled frames. Phoneme accuracy cannot be judged from stills |
| 4 Voice consistency | **NOT VERIFIED — likely issue** | Pitch measurement only |
| 5 Sound design | BUILT, NOT HEARD | Constructed to the brief; levels measured |
| 6 Music / mix | PASS on measurement | Loudness and stem levels |
| 7 Editing / pacing | PASS with notes | Timeline, one-frame-per-second overview |
| 8 Visual artefacts | PASS on sampled frames | One frame per second of the master; individual clips at 1.5 frames per second |

## Findings, most serious first

**1. General Arrow's voice may differ between takes (HIGH).** His first long take measures a median pitch of 213 Hz; his second long take and his opening line measure about 180 Hz. That may be the same voice projecting harder, or a different voice. The later two were generated with the first as a voice reference. Needs listening. If they differ, regenerate the first take with one of the others as reference (10 credits).

**2. One word to check by ear (MEDIUM).** In "recommend all elders remain indoors tonight", the transcription hears "elevators". It may be a mishearing by the transcriber or a wrong word in the take. If wrong, regenerate take B (12 credits).

**3. Narrator chosen blind (MEDIUM).** "Arthur" was picked on pacing and pitch (about 130 Hz, unhurried) without being heard. Three alternates exist for the same lines.

**4. Lip-sync unverified (MEDIUM).** Five shots show a speaking mouth: Arrow's status line, the Scalpetist's answer, Arrow's two long takes, and the group answer (small in frame). The edit already covers 5.5 s of take A and 1.8 s of take B with cutaways; more cutaways can cover any bad stretch.

**5. Runtime is at the top of the range (LOW).** MASTER 74.0 s (limit 75), CLEAN 69.0 s. The longest single hold is 6.1 s on Arrow's close shot for the Long Foot line.

**6. Stray words in the street ambience (LOW).** The first Dan clip's background voices include something like "more fight". It sits low under the narrator.

**7. Small design drifts (LOW).**
- Dan's hair in the extreme close-up is mid-brown and glossy, lighter than his approved hair.
- Mid-descent, for a few frames, the Forest Trees show branch-like shapes before becoming smooth pillars.
- General Arrow is darker in his entrance shot than elsewhere (he is in shadow).
- The Senior Scalpetist smiles slightly while speaking; the approved look is serious.
- Several staff have a faint vertical ridge between the eyes that suggests a nose.
- The Head Centre bell looks grey and metallic.

**8. Not seen at speed (LOW).** General Arrow's near-collision with the chart cart was prompted; whether it reads as the dry beat intended is unconfirmed.

## Checks that passed
- Every scripted line is present, complete and in order in the finished master (transcribed from the final file). No cut lands inside a line.
- Narration ends with "A lot more." Nothing after it.
- No Flake, no Grandpa Snow, no Burning Tsunami history, no Long Foot shown.
- No screens, electronics or neon in the Scalpence Centre.
- No scalp, skin or pores in the descent.
- Loudness: MASTER −13.7 LUFS, CLEAN −14.3 LUFS; true peak −1.4 dBTP.
- During Arrow's speech the music sits about 11 dB under the dialogue and the effects about 16 dB under.
- 1920×1080, constant 24 fps, BT.709, AAC 48 kHz.
- CLEAN starts on the first story frame and ends on the last, with no cards.

## Not done
- No shot was regenerated: all 18 clips were first takes.
- Sources are 720p, upscaled.
- The effects stem contains the ambience that came with the dialogue clips' pictures only where those clips are non-speaking; the dialogue stem's speaking clips carry a little room sound of their own.

---

# VERSION 2 — after the creator's notes (2026-10-06)

Creator's notes on version 1: General Arrow's voice "is too mainstream or nice guy, he needs to be a bit angrier as his character will be a funny mix between serious and clumsy"; the Senior Scalpetist "can also sound a bit more like a head in the clouds type of guy"; and where Arrow mentions the possibility of a threat "there should [be] music but more sombre, almost scary".

## What changed
- General Arrow's three speaking clips were regenerated with a gruff, gravelly, short-fused voice and a scowl (`S3_SH04_take2`, `S3_SH06A_take2`, `S3_SH06B_take2`). Take A was made first and used as the voice reference for the other two.
- The Senior Scalpetist's clip was regenerated (`S3_SH05_take2`): he gazes at the sky, notices the question late, answers in a soft dreamy voice, and drifts off again. The shot is 1.1 s longer than before.
- A new sombre cue (`audio/music_threat.m4a`) runs from the pause before "The Head will be shaking" through "Understood?" and cuts away as the staff answer.
- To hold the runtime, the room establishing shot and Arrow's entrance were each trimmed slightly.

## Re-checked
- Every scripted line is present, complete and in order in the new master. The word "elders" now transcribes correctly, which closes finding 2.
- Pitch across Arrow's three new takes: 308, 314 and 271 Hz (the lowest is the take with the low growl). They are closer to each other than in version 1, which eases finding 1 but does not replace listening.
- Threat cue level: first set too high (about 1.4 dB above the voice in that passage); lowered so it sits about 6 dB under the voice.
- Loudness: MASTER −13.6 LUFS, CLEAN −14.2 LUFS; true peak −1.4 dBTP.
- Runtime: MASTER 74.25 s (limit 75), CLEAN 69.25 s.

## Still open
- Nothing has been heard by the agent: the new voices' character, the cue's mood and the mix balance all need the creator's ears.
- Lip-sync on the four new clips is unverified, as before.
- In take A (version 2) General Arrow steps toward the camera in the second half; that part is under cutaways.
- The narrator is unchanged and still chosen blind.
- Version 1 files are kept in `deliverables/v1/`.

---

# OUTCOME (2026-10-06)
The creator compared the two versions and approved **version 1**. Version 2 is kept for reference only. The open findings in the version 1 report above (voice match between Arrow's takes, the word "elders", the narrator) are closed by that approval: the creator has heard version 1 and accepted it.

---

# OUTCOME (2026-10-07)
The creator approved the hook cut as Part 1 (blanket approval). Open findings above are closed by that approval. Fixed in this cut: the background jump in General Arrow's entrance; the Senior Scalpetist's passive delivery.
