# STYLE_BIBLE — Dan & the Dandruffs (project level)

**Canon level 3.** Must not contradict `WORLD_BIBLE.md` or `CHARACTER_BIBLE.md`. See `CANON_PRIORITY.md`.

This project has its own look. The creator confirmed on 2026-10-06 that it is separate from the channel-wide `STYLE_BIBLE.md` at the repository root, which does **not** apply here.

Rules marked *creator* are taken from the creator's briefs in `00_source/`. The working rules below began as the director's and were confirmed by the creator's blanket approval on 2026-10-07.

## OVERALL (*creator*)
- Premium original animation. Sophisticated children's animation. An original visual language.
- Tactile materials; macro photography / macro-cinematic feeling; shallow depth of field; subtle imperfections; soft directional light; natural material response.
- Warm but slightly strange. Beautiful but not overly polished. Fantastical but internally believable. Believable as a species and as a civilisation.
- Warm, restrained, muted natural palette. No bright toy or primary colours.

## MATERIALS (*creator*)
- Fibres, layered sheet-like material, thread-like structural elements, pale organic surfaces, translucent membranes, natural rigid fragments, handmade mechanical systems.
- Matte. Nothing glossy, plastic, ceramic or polished.
- Nothing disgusting, greasy, medical, dermatological, infected, dirty or grotesque. No pores, no literal skin.

## SCALE (*creator*)
- The great fibre structures dwarf the buildings and citizens. This constant difference in scale is part of the visual identity of the series.

## LIGHT (*creator*)
- Warm diffuse light from far above; soft atmosphere; floating particles; gentle haze; occasional shafts of light. Pleasant and inhabited, not dark or sinister.

## NEVER (*creator*)
- The look of existing studios or films the creator named as off-limits (see the briefs in `00_source/`), generic 3D mascots, giant eyes, cute-for-its-own-sake design, human child proportions for the dandruff species.
- Generic medieval fantasy, mushroom houses, steampunk cliché, neon cyberpunk, modern office buildings, fairy-tale towns.
- Stop-motion craft-toy styling.
- Fire, lava or literal flames for the Burning Tsunami.
- Text, labels or logos in images.

## CREATOR FEEDBACK
- On this species, brows that are lowered and drawn together read as anger. For thoughtful or worried, raise the inner ends of the brows instead. · creator on Pale round 2, 2026-10-06: "she looks angry"

- Open in the dandruff world. "The beauty of the show is in the dandruffs"; Dan's world and his friends "look very generic", and 15 seconds before reaching the dandruff world "is quite long". Keep the human world brief. · creator on EP01 Part 1, 2026-10-07

- Creatures must match the characters and the world: the first Long Foot looked "a bit disgusting" and did not "match the characters/world style". Realistic insect flesh is wrong for this show. · creator on the Long Foots, 2026-10-07

- ~~The human world is made of wool and cloth~~ — rejected 2026-10-20: "the forest trees don't match this style of hair. it matched previous Dan way more." Dan's hair must be smooth dark strands that match the Forest Trees. · creator, 2026-10-20
- The real world must be as original as the head world. The first Dan and his friends looked like "pure AI slop": a generic 3D-animated look is not acceptable for the human side either. · creator, 2026-10-07

## WORKING RULES (CONFIRMED by the creator's blanket approval, 2026-10-07; originally the director's)
- CONFIRMED · The species and its architecture share one material: pale handmade-paper-like fibre sheet with torn deckled edges. · from the approved Flake hero and Head Centre rounds, 2026-10-06
- CONFIRMED · Forest Trees are smooth, dark, untapered fibre pillars rising from pale collars; no bark, roots or branches. · Head Centre v2–v4; approved with the Head Centre images. **Exception:** at Grandpa Snow's home the Forest Tree has a flared base and branching roots that drape over the house (approved exterior)
- CONFIRMED · Buildings are low, rounded, wrapped-sheet forms with oval amber membrane windows; no pitched roofs. Some hang from the Forest Trees as pod clusters. · Head Centre v3–v4
- CONFIRMED · Environment masters are kept as empty plates; citizens are added per shot from character masters. · Head Centre plate_empty_v1
- CONFIRMED · The image model adds text labels to character sheets even when told not to; check and remove before use. · Flake sheets, 2026-10-06
- CONFIRMED · Any shot in which a character turns toward the camera needs an end keyframe built from the approved master; otherwise the video model redesigns the unseen side. Long actions are built as chained clips between keyframes. · TEST_HC_TREMOR, 2026-10-06
- CONFIRMED · Flake is a flat disc: seen from directly beside, his face is hidden. Stage dialogue and reactions in three-quarter view. · TEST_HC_TREMOR, 2026-10-06
- CONFIRMED · To change a character's build, leave the character's earlier image out of the references; the image model keeps the body structure of any image of that character it is given. · Pale rounds 2–3, 2026-10-06
- CONFIRMED · When approved character images are used as species references for background figures, the model copies those exact characters into the scene. Ask for an empty plate, or describe background figures in words only. · Scalpence Centre round 1, 2026-10-06
- CONFIRMED · Dialogue is shot as one long take per speech with cutaways laid over it, so the speaker's voice is never cut and stays consistent within the speech. · EP01 Part 1, 2026-10-06
- CONFIRMED · Recurring sounds (music motif, sting, warning bell, ambience) are single recordings reused across parts, never regenerated. · EP01 Part 1, 2026-10-06
- CONFIRMED · Tension to watch: the creator asks to avoid stop-motion toy styling, and the approved Flake has a handmade, puppet-like material quality. Keep lighting, depth and movement cinematic so it reads as a living species, not a craft object.

## MASTER ENVIRONMENT REFERENCES (canon level 4)
| Image | File | Status |
|---|---|---|
| Head Centre, empty plate | `assets/ENV_HEAD_CENTRE_MASTER/plate_empty_v1.png` | **CREATOR-APPROVED** 2026-10-07 |
| Head Centre, scale view | `assets/ENV_HEAD_CENTRE_MASTER/wide_scale_v1.png` | **CREATOR-APPROVED** 2026-10-07 |
| Scalpence Centre, hero | `assets/ENV_SCALPENCE_CENTRE_MASTER/hero_v3.png` | **CREATOR-APPROVED** 2026-10-06 |
| School street with Dan's friends (wool and cloth) | `assets/ENV_SCHOOL_STREET_MASTER/street_with_friends_v1.png` | generated, awaiting verdict |
| Grandpa Snow's home, interior | `assets/ENV_SNOW_HOME_MASTER/hero_v1.png` | **CREATOR-APPROVED** 2026-10-07 |
| Grandpa Snow's home, exterior | `assets/ENV_SNOW_HOME_MASTER/exterior_v1.png` | **CREATOR-APPROVED** 2026-10-07 |
