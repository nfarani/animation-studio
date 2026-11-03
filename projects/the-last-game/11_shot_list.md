# 11 — SHOT LIST · MASTER SHOT SPECIFICATION

Tool-independent and authoritative. Prompts written by `/prompts` are adapters of this file.

22 shots · 0:34.0 · 16:9 (assumed) · 24 fps
Camera angles A–E are defined in `06_environment_bible.md`. Screen direction: from all south-side cameras, **west (the goal, the sun) is frame left; east (the gateway, home) is frame right.**

Tiers: ECONOMY 4 · STANDARD 13 · PREMIUM 3 · edit-only 2
Risk: LOW 4 · MEDIUM 12 · HIGH 4 · (edit-only 2)

| Shot | In | Out | Dur | One line | Risk | Tier |
|---|---|---|---|---|---|---|
| S01_SH01 | 0:00.0 | 0:02.0 | 2.0 | Leo runs in, ball under arm | MED | STANDARD |
| S01_SH02 | 0:02.0 | 0:03.3 | 1.3 | Red backpack drops: goalposts | LOW | ECONOMY |
| S01_SH03 | 0:03.3 | 0:04.8 | 1.5 | Ball poked away. "Oi!" | MED | STANDARD |
| S02_SH01 | 0:04.8 | 0:05.9 | 1.1 | Feet chasing the ball | MED | STANDARD |
| S02_SH02 | 0:05.9 | 0:06.9 | 1.0 | Barged; nearly falls | HIGH | STANDARD |
| S02_SH03 | 0:06.9 | 0:08.1 | 1.2 | Ball rolls between the bags | LOW | ECONOMY |
| S02_SH04 | 0:08.1 | 0:09.6 | 1.5 | Danny grabs ball, Leo chases | MED | STANDARD |
| S03_SH01 | 0:09.6 | 0:11.1 | 1.5 | "Dinner!" — Leo turns. "Coming!" | MED | STANDARD |
| S03_SH02 | 0:11.1 | 0:11.9 | 0.8 | Hand takes red bag; navy left alone | MED | STANDARD |
| S03_SH03 | 0:11.9 | 0:13.7 | 1.8 | Sam: "You coming tomorrow?" | HIGH | PREMIUM |
| S03_SH04 | 0:13.7 | 0:15.1 | 1.4 | "Yeah, obviously." Turns, runs | MED | STANDARD |
| S04_SH01 | 0:15.1 | 0:16.5 | 1.4 | Leo passes camera; body fills frame | HIGH | STANDARD |
| S04_SH02 | 0:16.5 | 0:18.5 | 2.0 | Same angle, years later, empty | LOW | ECONOMY |
| S05_SH01 | 0:18.5 | 0:21.0 | 2.5 | Man walks in, slows, stops | MED | STANDARD |
| S05_SH02 | 0:21.0 | 0:22.8 | 1.8 | His face through the wire: recognition | MED | PREMIUM |
| S05_SH03 | 0:22.8 | 0:24.0 | 1.2 | FLASH — Sam's line (reuse) | — | edit-only |
| S05_SH04 | 0:24.0 | 0:25.3 | 1.3 | The same frame, empty | LOW | ECONOMY |
| S06_SH01 | 0:25.3 | 0:26.5 | 1.2 | Memory: boys run past, laughing | MED | STANDARD |
| S06_SH02 | 0:26.5 | 0:27.2 | 0.7 | Memory: ball between the bags (reuse) | — | edit-only |
| S06_SH03 | 0:27.2 | 0:28.4 | 1.2 | A small smile | MED | PREMIUM |
| S06_SH04 | 0:28.4 | 0:29.7 | 1.3 | Hand on the wire, then off | HIGH | STANDARD |
| S07_SH01 | 0:29.7 | 0:34.0 | 4.3 | Walks on; pauses; pitch stays empty | MED | STANDARD |

---

# SCENE 1 — ARRIVAL

## S01_SH01 · 2.0 s
- **Scene:** 1 · **Narrative purpose:** place, friends, protagonist, in one image
- **Characters:** Leo, Sam, Danny, Kit
- **Starting frame:** ANGLE E. Wide of the whole pitch in low sun. Sam, Danny and Kit loosely grouped mid-pitch, left of centre. Navy backpack on the grass at frame left. Leo is just inside the gateway at frame right, mid-stride.
- **Character action:** Leo runs from the gateway toward the others (right to left), ball under his **left** arm, red backpack bouncing on his **right** shoulder.
- **Background action:** Danny raises an arm. Kit turns to look.
- **Ending frame:** Leo two-thirds of the way to the group, still running.
- **Framing:** wide establishing · **Lens feeling:** wide, ~24 mm, deep focus
- **Camera position:** south-west corner, standing height · **Camera movement:** static
- **Lighting:** golden hour from behind camera-left; long shadows stretching away to the right; warm rim on the saplings
- **Emotion:** eagerness
- **Dialogue:** none · **SFX:** running feet on grass, backpack contents thumping, boys' voices calling across distance · **Music:** none
- **Continuity:** ball left arm; backpack right shoulder; navy bag already in place; six staked saplings; left sock down
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, CHAR_SAM_MASTER, CHAR_FRIENDS_SHEET, ENV_PITCH_THEN_E, PROP_SHEET_MASTER
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–3
  - PRIMARY FAILURE RISK: four identities in one frame; an extra child appearing
  - FALLBACK: friends kept small and static in the keyframe; only Leo animates
  - REUSE: ENV_PITCH_THEN_E plate is the keyframe background

## S01_SH02 · 1.3 s
- **Scene:** 1 · **Narrative purpose:** two bags are a goal
- **Characters:** none (Leo's hand may clip the top of frame)
- **Starting frame:** ANGLE C reverse (ground level, looking west into the sun). Navy backpack sitting upright at frame right, mid-distance, backlit. Foreground left: empty grass.
- **Character action:** the red backpack drops into the foreground at frame left, lands, slumps.
- **Background action:** out-of-focus legs cross far behind
- **Ending frame:** two backpacks, red near-left, navy far-right, the gap between them glowing
- **Framing:** low insert · **Lens feeling:** ~35 mm, shallow; focus on the red bag
- **Camera position:** on the grass · **Camera movement:** static
- **Lighting:** backlit, sun flare between the bags, grass blades lit translucent
- **Emotion:** ritual; this has been done a hundred times
- **Dialogue:** none · **SFX:** soft heavy thump, zip rattle · **Music:** none
- **Continuity:** red = south post; navy = north post; red slumps, navy stands
- **RISK:** LOW
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe
  - REFERENCE ASSETS: ENV_GOAL_THEN_C (reverse view), PROP_SHEET_MASTER
  - MODEL TIER: ECONOMY
  - EXPECTED DIFFICULTY: LOW · EXPECTED ATTEMPTS: 1–2
  - PRIMARY FAILURE RISK: bag changes shape on landing
  - FALLBACK: start with the bag already landed and settling; the thump carries the drop
  - REUSE: ENV_GOAL_THEN_C reverse plate

## S01_SH03 · 1.5 s
- **Scene:** 1 · **Narrative purpose:** the game starts by itself
- **Characters:** Leo (shins and feet), Kit (one leg)
- **Starting frame:** low angle at ankle height. The ball on the grass between Leo's trainers; he has just let it drop.
- **Character action:** Kit's red trainer comes in from frame right and pokes the ball away to frame left. Leo's feet pivot and go after it.
- **Background action:** two more pairs of legs run left across the back of frame
- **Ending frame:** empty grass; dust in the light
- **Framing:** low insert, feet only · **Lens feeling:** ~35 mm
- **Camera position:** ankle height, side-on · **Camera movement:** static
- **Lighting:** golden side light from frame left; dust catching it
- **Emotion:** mock outrage, delight
- **Dialogue:** LEO (O.S.) "Oi!" · then laughter (O.S.) · **SFX:** toe on leather, scuffing turf · **Music:** none
- **Continuity:** Leo's left sock down; Kit's red trainers; ball is blue-and-off-white
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, CHAR_FRIENDS_SHEET, PROP_SHEET_MASTER, ENV_PITCH_THEN_E
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–4
  - PRIMARY FAILURE RISK: foot-to-ball contact; ball warps or teleports
  - FALLBACK: keyframe starts with the ball already moving away and the red trainer finishing its swing
  - REUSE: ground texture from ENV_PITCH_THEN_E

---

# SCENE 2 — THE GAME

## S02_SH01 · 1.1 s
- **Scene:** 2 · **Narrative purpose:** speed
- **Characters:** Leo (waist down)
- **Starting frame:** low, side-on. Leo's legs mid-sprint, the ball half a metre ahead of him, both moving right to left.
- **Character action:** he runs after the ball and touches it on with his right foot
- **Background action:** blurred fence and saplings streak past
- **Ending frame:** legs and ball leaving frame left
- **Framing:** low tracking medium of legs · **Lens feeling:** ~50 mm, motion blur
- **Camera position:** knee height, parallel to the run · **Camera movement:** lateral track right to left, matching his speed (movement justified: momentum)
- **Lighting:** golden, sun ahead of him at frame left; long shadow trailing right
- **Emotion:** flat-out effort
- **Dialogue:** none · **SFX:** fast footfalls, breath, ball skidding · **Music:** none
- **Continuity:** teal shorts; left sock down; moving toward the goal (left)
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, PROP_SHEET_MASTER, ENV_PITCH_THEN_E
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–4
  - PRIMARY FAILURE RISK: leg tangling at speed; ball drifting
  - FALLBACK: static camera, legs cross the frame right to left in 0.8 s
  - REUSE: none

## S02_SH02 · 1.0 s
- **Scene:** 2 · **Narrative purpose:** it is rough and nobody minds
- **Characters:** Leo; Danny's shoulder and arm only
- **Starting frame:** medium on Leo running right to left, eyes down on the (unseen) ball. Frame right is open.
- **Character action:** a forest-green shoulder comes in from frame right and bumps him. Leo lurches left, one arm out, catches his balance, grins.
- **Background action:** none
- **Ending frame:** Leo upright again, still moving, grinning
- **Framing:** medium, waist up · **Lens feeling:** ~50 mm, handheld feeling
- **Camera position:** chest height, three-quarter front · **Camera movement:** slight handheld drift with him
- **Lighting:** golden, sun on his face from frame left
- **Emotion:** a jolt, then laughter
- **Dialogue:** none · **SFX:** dull thud of bodies, grunt, a laugh · **Music:** none
- **Continuity:** no backpack on him (it is a goalpost); mustard shirt; tuft
- **RISK:** HIGH — see `17_high_risk_fallbacks.md`
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, CHAR_FRIENDS_SHEET, ENV_PITCH_THEN_E
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: HIGH · EXPECTED ATTEMPTS: 3–5, hard cap 4 before fallback
  - PRIMARY FAILURE RISK: character-to-character contact; limbs merging; face distortion mid-stumble
  - FALLBACK: Leo alone stumbles as if shoved; contact happens off-frame, carried by the thud
  - REUSE: none

## S02_SH03 · 1.2 s (generate ~4 s; also supplies S06_SH02)
- **Scene:** 2 · **Narrative purpose:** the goal, and the argument about it
- **Characters:** none
- **Starting frame:** ANGLE C. Ground level behind the goal, looking east. Navy backpack frame left, red backpack frame right. The ball is in the distance, coming.
- **Character action:** the ball rolls and bounces low toward camera, passes between the bags close to the red one, and runs out past the lens.
- **Background action:** out-of-focus boys behind, arms going up
- **Ending frame:** the two bags; empty goalmouth
- **Framing:** low wide insert · **Lens feeling:** ~24 mm, close to the grass
- **Camera position:** on the ground · **Camera movement:** static
- **Lighting:** front-lit gold from behind camera; bags throw shadows away from lens
- **Emotion:** triumph, disputed
- **Dialogue:** SAM (O.S.) "That wasn't in!" · LEO (O.S.) "Course it was!" · **SFX:** kick (pre-lapped from previous shot), ball hissing over grass · **Music:** none
- **Continuity:** navy left / red right from this side; ball passes inside the red bag, close enough to argue about
- **RISK:** LOW
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe
  - REFERENCE ASSETS: ENV_GOAL_THEN_C, PROP_SHEET_MASTER
  - MODEL TIER: ECONOMY
  - EXPECTED DIFFICULTY: LOW–MEDIUM · EXPECTED ATTEMPTS: 2–3
  - PRIMARY FAILURE RISK: ball panel pattern mutating as it rolls
  - FALLBACK: still plate + ball animated as a 2D element in the edit
  - REUSE: ENV_GOAL_THEN_C plate. **One generation serves two shots.**

## S02_SH04 · 1.5 s
- **Scene:** 2 · **Narrative purpose:** the game never stops; ends the fragment run on a wide
- **Characters:** Danny, Leo, Sam, Kit
- **Starting frame:** ANGLE E, slightly tighter than S01_SH01. Danny beside the goal with the ball already in both hands. Leo three metres from him. Sam and Kit mid-pitch.
- **Character action:** Danny runs off left to right with the ball held high against his chest, looking back. Leo runs after him.
- **Background action:** Sam throws his arms wide in complaint; Kit follows a beat late
- **Ending frame:** Danny and Leo deep in frame right, heading east
- **Framing:** wide · **Lens feeling:** ~28 mm
- **Camera position:** south-west corner · **Camera movement:** static
- **Lighting:** as S01_SH01, sun fractionally lower
- **Emotion:** uproar
- **Dialogue:** laughter, wordless protest (O.S. quality; nobody is close enough to need sync) · **SFX:** feet, laughing · **Music:** none
- **Continuity:** both bags in place; chase direction is now left to right (east), which positions Leo for the mother's call from the east
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, CHAR_SAM_MASTER, CHAR_FRIENDS_SHEET, ENV_PITCH_THEN_E, PROP_SHEET_MASTER
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–3
  - PRIMARY FAILURE RISK: picking the ball up (hand interaction) — avoided by starting with it already in his hands
  - FALLBACK: two-figure version, Danny and Leo only
  - REUSE: ENV_PITCH_THEN_E plate; same setup as S01_SH01

---

# SCENE 3 — CALLED HOME

## S03_SH01 · 1.5 s
- **Scene:** 3 · **Narrative purpose:** the interruption
- **Characters:** Leo
- **Starting frame:** medium on Leo, running left to right, slowing. The light is lower and redder than Scene 2.
- **Character action:** on the mother's voice he stops and turns his head to frame right, chin up. He shouts back once, already leaning toward the goal to get his bag.
- **Background action:** saplings and north fence soft behind him
- **Ending frame:** Leo in profile facing right, starting to move out of frame left
- **Framing:** medium · **Lens feeling:** ~50 mm
- **Camera position:** his eye height, from the south side · **Camera movement:** static
- **Lighting:** low sun from frame left on the back of his head and shoulder; face in warm bounce
- **Emotion:** mild annoyance; total normality
- **Dialogue:** MOTHER (O.S., from frame right, distant) "Come on! Dinner!" · LEO (no lip-sync, profile shout) "Coming!" · **SFX:** game noise thins · **Music:** none
- **Continuity:** no backpack on him yet; sweaty hair, tuft up; sun lower from this shot onward
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, ENV_PITCH_THEN_E (low-sun grade)
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–3
  - PRIMARY FAILURE RISK: face instability during the head turn
  - FALLBACK: start with the head already turned; he shouts and goes
  - REUSE: background crop from ENV_PITCH_THEN_E

## S03_SH02 · 0.8 s
- **Scene:** 3 · **Narrative purpose:** the goal loses a post
- **Characters:** Leo (hand and forearm)
- **Starting frame:** ANGLE C reverse, as S01_SH02 but in the lower sun. Red backpack foreground left, navy backpack background right.
- **Character action:** Leo's right hand takes the red bag by its top strap and lifts it up out of frame.
- **Background action:** none
- **Ending frame:** flattened grass where the red bag was; the navy bag alone in the background
- **Framing:** low insert · **Lens feeling:** ~35 mm; focus pulls from red bag to navy bag as the red one leaves
- **Camera position:** on the grass · **Camera movement:** static
- **Lighting:** deep orange backlight, longer shadows than S01_SH02
- **Emotion:** nothing; that is the point
- **Dialogue:** none · **SFX:** strap creak, canvas dragging off grass · **Music:** none
- **Continuity:** mirrors S01_SH02 exactly; right hand; navy bag does not move
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe
  - REFERENCE ASSETS: ENV_GOAL_THEN_C (reverse view), PROP_SHEET_MASTER, CHAR_LEO_BOY_MASTER
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–3
  - PRIMARY FAILURE RISK: hand grip on the strap
  - FALLBACK: reverse the S01_SH02 clip (bag rising out of frame), no hand needed
  - REUSE: same setup as S01_SH02; fallback reuses its footage outright

## S03_SH03 · 1.8 s — HERO, reused as S05_SH03
- **Scene:** 3 · **Narrative purpose:** the question the film is about
- **Characters:** Sam
- **Starting frame:** ANGLE B. Full shot. Sam stands at the centre of the pitch, slightly left of frame centre, **right foot resting on the ball**, hands loose at his sides, looking just right of the lens (at Leo). Behind him: the staked saplings, north fence, terrace, sky going orange.
- **Character action:** eyebrows lift; he asks. A small tilt of the head on the last word. He does not step, wave or lean.
- **Background action:** none. Danny and Kit are not in this frame.
- **Ending frame:** Sam in the same position, waiting for the answer, half-grin starting
- **Framing:** full shot, Sam about 60% of frame height, ball at the bottom third · **Lens feeling:** ~40 mm, moderate depth; background readable, not sharp
- **Camera position:** Leo's eye height (~1.2 m), from the south · **Camera movement:** static. Locked.
- **Lighting:** low sun from frame left; warm key on the left side of his face, long shadow to the right
- **Emotion:** easy; a question with only one possible answer
- **Dialogue:** SAM (ON-SCREEN) "You coming tomorrow?" · **SFX:** evening quiet; a dog far off · **Music:** none
- **Continuity:** sleeves pushed up; right foot on ball; navy bag is out of frame to the left; this exact frame is matched by ENV_PITCH_NOW_B
- **RISK:** HIGH — see `17_high_risk_fallbacks.md`
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video, then lip-sync pass
  - REFERENCE ASSETS: CHAR_SAM_MASTER, ENV_PITCH_THEN_B, PROP_SHEET_MASTER
  - MODEL TIER: PREMIUM
  - EXPECTED DIFFICULTY: HIGH · EXPECTED ATTEMPTS: 3–5
  - PRIMARY FAILURE RISK: mouth not matching the line; identity drift; camera creeping when it must be locked
  - FALLBACK: see file 17 (line delivered over the back of Leo's shoulder; or line pre-lapped over S03_SH02)
  - REUSE: ENV_PITCH_THEN_B plate. **This clip is used twice.** Full-shot scale keeps the mouth small, which lowers lip-sync risk.

## S03_SH04 · 1.4 s
- **Scene:** 3 · **Narrative purpose:** the promise, thrown away
- **Characters:** Leo
- **Starting frame:** reverse of S03_SH03, from Sam's position looking south-east. Medium-wide. Leo already four steps away, walking backwards toward the gateway (frame right, behind him), red backpack going onto his right shoulder.
- **Character action:** he **hitches the strap up with his right thumb**, answers without breaking step, then spins on one foot and runs for the gateway.
- **Background action:** south fence, gateway, footpath beyond
- **Ending frame:** Leo's back, running away toward the gateway
- **Framing:** medium-wide, receding figure · **Lens feeling:** ~35 mm
- **Camera position:** Sam's eye height · **Camera movement:** static
- **Lighting:** low sun from frame right now (camera has reversed); his face warm, front-lit
- **Emotion:** certainty so complete it is careless
- **Dialogue:** LEO (no lip-sync pass; small in frame, moving) "Yeah, obviously." · **SFX:** backpack shrug, feet turning on grass · **Music:** none
- **Continuity:** backpack right shoulder; **the thumb hitch is echoed in S05_SH01**; he heads for frame-right/gateway; ball stays with Sam
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, ENV_PITCH_THEN_E (for south-fence geography), PROP_SHEET_MASTER
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–4
  - PRIMARY FAILURE RISK: walking backwards then turning; backpack strap behaviour
  - FALLBACK: he is already half-turned; says the line over his shoulder and runs
  - REUSE: none

---

# SCENE 4 — THE CUT

## S04_SH01 · 1.4 s
- **Scene:** 4 · **Narrative purpose:** the wipe
- **Characters:** Leo; Sam tiny in the background
- **Starting frame:** **ANGLE A, locked.** Through the gateway: Leo mid-pitch, running straight at camera. Behind him, small, Sam beside the ball at centre. Navy backpack alone at mid-left. Saplings, terrace, orange sky.
- **Character action:** Leo runs through the gateway, across the footpath and past the lens on its right side, close enough that his mustard shirt fills the entire frame.
- **Background action:** Sam stays where he is
- **Ending frame:** the whole frame is soft, dark-mustard fabric in motion blur
- **Framing:** wide, becoming total occlusion · **Lens feeling:** ~28 mm, deep focus until he is too close to hold
- **Camera position:** ANGLE A, 1.3 m high · **Camera movement:** **none. The frame must not move by a pixel.**
- **Lighting:** low sun from frame left, strong rim on Leo; his front in shadow as he nears
- **Emotion:** nothing special; he is hungry
- **Dialogue:** none · **SFX:** feet on grass then tarmac, breath, backpack; **all sound cuts on the last frame** · **Music:** none
- **Continuity:** backpack on right shoulder; passes camera-right (toward home); red bag gone from the goal; ball at Sam's foot
- **RISK:** HIGH — see `17_high_risk_fallbacks.md`
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe built on the plate
  - REFERENCE ASSETS: CHAR_LEO_BOY_MASTER, CHAR_SAM_MASTER, ENV_PITCH_THEN_A, PROP_SHEET_MASTER
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: HIGH · EXPECTED ATTEMPTS: 3–5
  - PRIMARY FAILURE RISK: unwanted camera movement; face distorting at close range; frame never fully occluded
  - FALLBACK: generate only the run to mid-distance; finish the occlusion with a blurred mustard wipe in the edit
  - REUSE: ENV_PITCH_THEN_A is the keyframe background, unaltered

## S04_SH02 · 2.0 s
- **Scene:** 4 · **Narrative purpose:** years later
- **Characters:** none
- **Starting frame:** **ANGLE A, identical framing, NOW.** Rusted sagging fence, leaning post left of the gateway, worn surface, weeds, six mature trees, grey sky. No backpack. No ball. No one.
- **Character action:** none
- **Background action:** tree crowns move in the wind; long grass shivers at the fence foot
- **Ending frame:** the same
- **Framing:** as S04_SH01 · **Lens feeling:** identical
- **Camera position:** ANGLE A · **Camera movement:** none
- **Lighting:** flat overcast, cool, no shadows
- **Emotion:** absence
- **Dialogue:** none · **SFX:** after one beat of dead silence: wind in leaves, distant traffic, wire ticking against a post · **Music:** none
- **Continuity:** fence posts, gateway, path edge and horizon align with S04_SH01; six trees in the same positions
- **RISK:** LOW (the risk lives in the plate, not the shot)
- **GENERATION STRATEGY**
  - METHOD: still image + subtle ambient motion (image-to-video, or edit-only movement on foliage)
  - REFERENCE ASSETS: ENV_PITCH_NOW_A
  - MODEL TIER: ECONOMY
  - EXPECTED DIFFICULTY: LOW · EXPECTED ATTEMPTS: 1–2
  - PRIMARY FAILURE RISK: model adds camera drift or changes the fence
  - FALLBACK: pure still with a wind-sway warp on the tree line in the edit
  - REUSE: ENV_PITCH_NOW_A plate, unaltered. Same plate as S05_SH01 and S07_SH01.

---

# SCENE 5 — RECOGNITION

## S05_SH01 · 2.5 s
- **Scene:** 5 · **Narrative purpose:** he almost walks past
- **Characters:** Leo (adult)
- **Starting frame:** ANGLE A, NOW, continuous with S04_SH02 (should cut invisibly or be one take). Empty.
- **Character action:** Leo enters at frame left on the footpath, walking left to right at a working pace, **hitching his bag strap with his right thumb**. His head turns toward the pitch. He slows over three steps and stops just left of the gateway, turning his shoulders to the fence.
- **Background action:** trees moving
- **Ending frame:** Leo standing at the fence, centre-right, back three-quarter to camera, looking in
- **Framing:** wide; full figure, about half frame height · **Lens feeling:** as S04
- **Camera position:** ANGLE A · **Camera movement:** none
- **Lighting:** flat overcast; the ochre jumper is the only warm note
- **Emotion:** preoccupied, then caught
- **Dialogue:** none · **SFX:** leather soles on tarmac, slowing; wind; traffic · **Music:** none
- **Continuity:** bag on right shoulder; thumb hitch matches S03_SH04; coat open; enters left, will exit right; his stop position is the start position of S07_SH01
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: image-to-video with start frame (empty plate) and end frame (keyframe of Leo at the fence)
  - REFERENCE ASSETS: CHAR_LEO_ADULT_MASTER, ENV_PITCH_NOW_A, PROP_SHEET_MASTER
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–4
  - PRIMARY FAILURE RISK: identity drift for a character entering from off-frame; start/end-frame control is UNVERIFIED on the adapter
  - FALLBACK: keyframe with Leo already two steps into frame; he walks, slows, stops (cut from S04_SH02 rather than continuous)
  - REUSE: ENV_PITCH_NOW_A plate

## S05_SH02 · 1.8 s
- **Scene:** 5 · **Narrative purpose:** he recognises it
- **Characters:** Leo (adult)
- **Starting frame:** ANGLE D. Close-up of Leo's face through the chain-link; the wire is a soft diamond pattern in the foreground. He looks just left of the lens, into the pitch. Neutral, slightly puzzled.
- **Character action:** his eyes stop searching and fix. The brow lifts a millimetre. His lips part. A breath in.
- **Background action:** out-of-focus hedge and houses to the south; coat collar moves in the wind
- **Ending frame:** the same face, changed
- **Framing:** close-up, forehead to collar · **Lens feeling:** ~85 mm, shallow; focus on the eyes, wire soft
- **Camera position:** inside the pitch, his eye height · **Camera movement:** static
- **Lighting:** soft overcast, even; a small cool catchlight in each eye
- **Emotion:** recognition. Not grief.
- **Dialogue:** none · **SFX:** wind drops slightly; wire ticking; the first faint pre-echo of children, almost inaudible, in the last 6 frames · **Music:** see `02_creative_notes.md` k
- **Continuity:** ears, tuft, brows match the boy; ochre jumper visible at the collar; his eyeline goes to Sam's spot
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video
  - REFERENCE ASSETS: CHAR_LEO_ADULT_MASTER, ENV_FENCE_NOW_D
  - MODEL TIER: PREMIUM
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 3–4
  - PRIMARY FAILURE RISK: over-acting (tears, big eyes, trembling); wire pattern crawling across the face
  - FALLBACK: shoot without the foreground wire; add a soft wire overlay in the edit
  - REUSE: same setup as S06_SH03; ideally both come from one longer generation

## S05_SH03 · 1.2 s — EDIT-ONLY
- **Scene:** 5 · **Narrative purpose:** what he is remembering
- **Characters:** Sam
- **Content:** S03_SH03, trimmed to the line. Identical frame, identical performance.
- **Framing / camera / lighting:** as S03_SH03
- **Emotion:** the same easy question, now unbearable in its ease
- **Dialogue:** SAM (ON-SCREEN, memory) "You coming tomorrow?" — same recording, with a short room-less tail added in the mix · **SFX:** hard in, hard out · **Music:** see notes
- **Continuity:** must be the approved S03_SH03 take, not an alternate
- **RISK:** none (inherits S03_SH03)
- **GENERATION STRATEGY**
  - METHOD: edit-only solution
  - REFERENCE ASSETS: S03_SH03 (approved render)
  - MODEL TIER: none
  - EXPECTED DIFFICULTY: LOW · EXPECTED ATTEMPTS: 0
  - PRIMARY FAILURE RISK: none
  - FALLBACK: n/a
  - REUSE: 100% reuse of S03_SH03

## S05_SH04 · 1.3 s
- **Scene:** 5 · **Narrative purpose:** he is not there
- **Characters:** none
- **Starting frame:** **ANGLE B, identical framing to S03_SH03, NOW.** Where Sam stood: bare earth and a few weeds. No ball. Mature trees behind; the terrace mostly hidden.
- **Character action:** none
- **Background action:** grass and leaves move
- **Ending frame:** the same
- **Framing:** as S03_SH03 · **Lens feeling:** identical
- **Camera position:** ANGLE B · **Camera movement:** none
- **Lighting:** flat overcast
- **Emotion:** the answer to "Did he come back?"
- **Dialogue:** none · **SFX:** wind; the question's tail dying · **Music:** none
- **Continuity:** horizon, fence line and tree positions align with S03_SH03
- **RISK:** LOW
- **GENERATION STRATEGY**
  - METHOD: still image + subtle ambient motion
  - REFERENCE ASSETS: ENV_PITCH_NOW_B
  - MODEL TIER: ECONOMY
  - EXPECTED DIFFICULTY: LOW · EXPECTED ATTEMPTS: 1–2
  - PRIMARY FAILURE RISK: framing mismatch with S03_SH03
  - FALLBACK: pure still, aligned to S03_SH03's first frame in the edit
  - REUSE: ENV_PITCH_NOW_B plate, unaltered

---

# SCENE 6 — THE SECOND MEMORY

## S06_SH01 · 1.2 s
- **Scene:** 6 · **Narrative purpose:** what it felt like, not what was said
- **Characters:** Sam, Danny, Kit (Leo is not in frame; this is what he saw)
- **Starting frame:** low angle from near the south fence looking north-west, THEN, golden. Empty grass, sun in the top-left of frame.
- **Character action:** the three run through frame right to left, close to the lens: Danny first, Sam laughing with his head back, Kit a beat behind.
- **Background action:** the two backpacks small in the distance at frame left
- **Ending frame:** Kit's back leaving frame left; dust in the sun
- **Framing:** low medium-wide, figures crossing close · **Lens feeling:** ~28 mm, slight overexposure and halation (memory)
- **Camera position:** ~1 m high · **Camera movement:** static
- **Lighting:** strong backlight; rim on hair, faces in warm shadow
- **Emotion:** uncomplicated happiness
- **Dialogue:** none; one clear laugh (Sam) · **SFX:** feet, laughter, slightly reverberant · **Music:** see notes
- **Continuity:** both backpacks in place (this is earlier in the evening than S03); running toward the goal (left)
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video
  - REFERENCE ASSETS: CHAR_SAM_MASTER, CHAR_FRIENDS_SHEET, ENV_PITCH_THEN_E
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–4
  - PRIMARY FAILURE RISK: three running bodies close to the lens; extra limbs
  - FALLBACK: silhouettes only, fully backlit, faces unreadable
  - REUSE: backlight and halation hide identity detail, so this tolerates a cheaper take

## S06_SH02 · 0.7 s — EDIT-ONLY
- **Scene:** 6 · **Narrative purpose:** the intact goal, one last time
- **Characters:** none
- **Content:** 0.7 s from the S02_SH03 generation: the ball bouncing as it passes between the two backpacks. Punched in ~110% and graded to match S06_SH01's halation.
- **Framing / camera / lighting:** as S02_SH03
- **Emotion:** fondness
- **Dialogue:** none · **SFX:** one bounce, soft · **Music:** see notes
- **Continuity:** both bags present
- **RISK:** none (inherits S02_SH03)
- **GENERATION STRATEGY**
  - METHOD: edit-only solution
  - REFERENCE ASSETS: S02_SH03 (approved render)
  - MODEL TIER: none
  - EXPECTED DIFFICULTY: LOW · EXPECTED ATTEMPTS: 0
  - PRIMARY FAILURE RISK: none
  - FALLBACK: n/a
  - REUSE: 100% reuse of S02_SH03

## S06_SH03 · 1.2 s
- **Scene:** 6 · **Narrative purpose:** not sad
- **Characters:** Leo (adult)
- **Starting frame:** ANGLE D, same setup as S05_SH02, fractionally wider (chin to hairline plus shoulders). His face as S05_SH02 ended.
- **Character action:** the corners of his eyes crease first. Then a small closed-mouth smile, one side slightly higher. He breathes out through his nose.
- **Background action:** as S05_SH02
- **Ending frame:** the small smile, held
- **Framing:** close-up · **Lens feeling:** ~85 mm
- **Camera position:** ANGLE D · **Camera movement:** static
- **Lighting:** as S05_SH02
- **Emotion:** fondness. No wet eyes, no swallowing, no looking down.
- **Dialogue:** none · **SFX:** wind; the laughter's tail from S06_SH01 dying under it · **Music:** see notes
- **Continuity:** matches S05_SH02 in framing, wire pattern, collar
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: reference-image keyframe → image-to-video (or continuation of the S05_SH02 generation)
  - REFERENCE ASSETS: CHAR_LEO_ADULT_MASTER, ENV_FENCE_NOW_D
  - MODEL TIER: PREMIUM
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–4
  - PRIMARY FAILURE RISK: the smile comes out too big or too sad
  - FALLBACK: use the last 1.2 s of a longer S05_SH02 take if it contains a usable softening of the face
  - REUSE: S05_SH02 setup and keyframe

## S06_SH04 · 1.3 s
- **Scene:** 6 · **Narrative purpose:** he touches it, and lets go
- **Characters:** Leo (adult), right hand and coat cuff
- **Starting frame:** ANGLE D, hand height. Macro on rusted chain-link. His hand is already resting flat against the far side of the wire, fingertips through two of the diamonds.
- **Character action:** the fingers press very slightly. A beat. The hand lifts away and leaves frame downward. The wire springs back a few millimetres.
- **Background action:** charcoal coat out of focus behind the wire
- **Ending frame:** wire only, still trembling
- **Framing:** insert · **Lens feeling:** ~100 mm macro, very shallow
- **Camera position:** inside the pitch · **Camera movement:** static
- **Lighting:** soft overcast; rust texture readable
- **Emotion:** goodbye, without the word
- **Dialogue:** none · **SFX:** faint metallic give, then the wire settling · **Music:** out by the end of this shot
- **Continuity:** right hand; charcoal cuff with ochre knit showing at the wrist; no ring emphasised; no watch
- **RISK:** HIGH — see `17_high_risk_fallbacks.md`
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe (hand already in contact)
  - REFERENCE ASSETS: CHAR_LEO_ADULT_MASTER, ENV_FENCE_NOW_D (macro view)
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: HIGH · EXPECTED ATTEMPTS: 3–5, hard cap 4 before fallback
  - PRIMARY FAILURE RISK: fingers merging with the wire; finger count
  - FALLBACK: see file 17 (wide from behind at ANGLE A; or wire-only insert with shadow)
  - REUSE: starting in contact removes the approach, which is the hardest half

---

# SCENE 7 — WALKING ON

## S07_SH01 · 4.3 s — FINAL IMAGE
- **Scene:** 7 · **Narrative purpose:** he leaves; the place stays
- **Characters:** Leo (adult)
- **Starting frame:** **ANGLE A, NOW.** Leo at the fence exactly where S05_SH01 left him, back three-quarter to camera, right hand just returning to his coat pocket.
- **Character action:**
  - 0.0–0.8 s: he turns from the fence to face along the path (frame right)
  - 0.8–2.5 s: walks left to right at an easy pace, slower than he arrived
  - 2.5–3.0 s: **stops. Half a second. Head lifts a little. He does not turn round.**
  - 3.0–3.7 s: walks on and out of frame right
  - 3.7–4.3 s: empty frame
- **Background action:** tree crowns moving
- **Ending frame:** the empty pitch through the gateway. Identical to S04_SH02.
- **Framing:** wide · **Lens feeling:** as S04
- **Camera position:** ANGLE A · **Camera movement:** **none. The camera stays behind.**
- **Lighting:** flat overcast. No change, no sunbreak.
- **Emotion:** acceptance
- **Dialogue:** CHILD'S VOICE (O.S., memory, very faint, at 2.3 s) "Come on!" · **SFX:** at 2.5 s a ball is kicked, far away; children laugh, far away; then only wind and traffic. Footsteps resume at 3.0 s and fade. · **Music:** none
- **Continuity:** exits frame right, the same side the boy left by in S04_SH01; bag on right shoulder; nothing has been left at the fence
- **RISK:** MEDIUM
- **GENERATION STRATEGY**
  - METHOD: image-to-video from keyframe (Leo at fence on the NOW_A plate)
  - REFERENCE ASSETS: CHAR_LEO_ADULT_MASTER, ENV_PITCH_NOW_A, PROP_SHEET_MASTER
  - MODEL TIER: STANDARD
  - EXPECTED DIFFICULTY: MEDIUM · EXPECTED ATTEMPTS: 2–4
  - PRIMARY FAILURE RISK: the pause not landing on time; background changing once he exits
  - FALLBACK: generate a continuous walk-off with no pause, create the half-second pause with a freeze/slow in the edit (he is small and seen from behind, so it will not show); replace the empty tail with the ENV_PITCH_NOW_A still
  - REUSE: ENV_PITCH_NOW_A plate; the last 0.6 s can be S04_SH02 footage

**CUT TO BLACK. Silence. No text.**
