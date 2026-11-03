# 08 — MASTER ASSET LIST

12 master assets. Full production specs and batches are written by `/assets`. Nothing here has been generated.

Priority: **P1** blocks everything · **P2** blocks specific scenes · **P3** supporting.

## CHARACTERS

### CHAR_LEO_BOY_MASTER — P1
- **Type:** character reference
- **Purpose:** lock Leo's identity as a boy; source for the adult
- **Description:** see `05_character_bible.md` → LEO — BOY
- **Views:** front, three-quarter, profile, back (full body, neutral pose, flat neutral light); one running pose
- **Expressions:** open grin · mock outrage ("Oi!") · head turned, listening · casual over-the-shoulder
- **Continuity:** crown tuft, ears, left sock down, mustard/teal, backpack on right shoulder
- **Dependent scenes:** S1, S2, S3, S4
- **Dependent shots:** S01_SH01, S01_SH03, S02_SH01, S02_SH02, S02_SH04, S03_SH01, S03_SH02, S03_SH04, S04_SH01
- **Downstream assets:** CHAR_LEO_ADULT_MASTER

### CHAR_LEO_ADULT_MASTER — P1
- **Type:** character reference, **derived from CHAR_LEO_BOY_MASTER**
- **Purpose:** the same person 22 years on
- **Description:** see `05_character_bible.md` → LEO — ADULT
- **Views:** front, three-quarter, profile, back three-quarter (the back view matters: S05_SH01 and S07_SH01 see him from behind)
- **Expressions:** neutral/inward · recognition (eyes sharpen, brow lifts a millimetre) · small smile (eyes first)
- **Continuity:** same ears, tuft, brows, eye shape; ochre jumper; bag on right shoulder
- **Approval test:** placed beside the boy master, they must read as one person
- **Dependent scenes:** S5, S6, S7
- **Dependent shots:** S05_SH01, S05_SH02, S06_SH03, S06_SH04, S07_SH01

### CHAR_SAM_MASTER — P1
- **Type:** character reference
- **Purpose:** lock the face the audience has to remember
- **Description:** see `05_character_bible.md` → SAM
- **Views:** front, three-quarter, profile; **one full-body pose standing with right foot on the ball, hands loose**
- **Expressions:** easy half-grin · asking (eyebrows up, mouth just open) · laughing
- **Continuity:** tooth gap, pushed-up sleeves, curls
- **Dependent scenes:** S1, S2, S3, S5 (flash), S6
- **Dependent shots:** S01_SH01, S02_SH04, S03_SH03 (→ S05_SH03), S06_SH01

### CHAR_FRIENDS_SHEET — P2
- **Type:** character reference sheet (Danny + Kit on one sheet)
- **Purpose:** keep the two background friends consistent in wides and fragments
- **Views:** front and back, full body, side by side at correct relative height (include Leo's height line)
- **Expressions:** laughing only
- **Dependent shots:** S01_SH01, S01_SH03 (Kit's red trainer), S02_SH02 (Danny's green shoulder), S02_SH04, S06_SH01

## ENVIRONMENTS

### ENV_PITCH_THEN_E — P1 (geography master)
- **Type:** environment plate, ANGLE E, THEN
- **Purpose:** establish and lock the whole layout; every other plate is checked against it
- **Description:** full pitch from the south-west corner: fence, gateway, six staked saplings, terrace, goal position, golden hour
- **Views:** one wide, empty (no characters, no props)
- **Dependent shots:** S01_SH01, S02_SH04
- **Downstream assets:** all other ENV plates

### ENV_PITCH_THEN_A — P1 (the match-cut plate)
- **Type:** environment plate, ANGLE A, THEN, low sun (S3 light)
- **Purpose:** the locked frame the boy runs out of
- **Description:** from the footpath through the gateway; fence left and right; pitch; saplings; terrace. Navy backpack alone on the grass, mid-left. Ball at centre.
- **Views:** one, empty of characters
- **Dependent shots:** S04_SH01
- **Downstream assets:** ENV_PITCH_NOW_A

### ENV_PITCH_NOW_A — P1
- **Type:** environment plate, **edited from ENV_PITCH_THEN_A** (same pixels, aged)
- **Purpose:** the reveal and the final image
- **Description:** identical framing. Rust, sag, leaning post, worn surface, weeds, mature trees, overcast. No backpack, no ball.
- **Approval test:** overlaid at 50% on ENV_PITCH_THEN_A, fence posts, gateway, path edge and horizon line up
- **Dependent shots:** S04_SH02, S05_SH01, S07_SH01

### ENV_PITCH_THEN_B — P2
- **Type:** environment plate, ANGLE B, THEN, low sun
- **Purpose:** background for Sam's line
- **Description:** looking north across the centre of the pitch to the saplings, north fence and terrace. Empty.
- **Dependent shots:** S03_SH03 (→ S05_SH03)
- **Downstream assets:** ENV_PITCH_NOW_B

### ENV_PITCH_NOW_B — P2
- **Type:** environment plate, **edited from ENV_PITCH_THEN_B**
- **Purpose:** "the empty spot"
- **Description:** identical framing, aged. Bare earth where Sam stood.
- **Dependent shots:** S05_SH04

### ENV_GOAL_THEN_C — P2
- **Type:** environment plate, ANGLE C, THEN, ground level
- **Purpose:** the backpack goal seen from behind, and its reverse
- **Description:** grass-blade-level view east through the two backpacks, navy left, red right, low sun flaring from behind camera-left; bare goalmouth patch
- **Views:** (1) from behind the goal looking east; (2) reverse, from in front looking west, with only the navy bag in place (for S01_SH02)
- **Dependent shots:** S01_SH02, S02_SH03 (→ S06_SH02)

### ENV_FENCE_NOW_D — P2
- **Type:** environment plate, ANGLE D, NOW
- **Purpose:** background and foreground wire for the adult's close shots
- **Description:** rusted chain-link filling the frame in soft focus; beyond it, the footpath and out-of-focus hedges/houses to the south. Overcast.
- **Views:** (1) face-height framing; (2) hand-height macro of the wire
- **Dependent shots:** S05_SH02, S06_SH03, S06_SH04

## PROPS

### PROP_SHEET_MASTER — P1
- **Type:** prop reference sheet
- **Purpose:** lock the ball and all three bags
- **Description:** PROP_BALL, PROP_BACKPACK_LEO, PROP_BACKPACK_SAM, PROP_BAG_ADULT per `07_prop_bible.md`
- **Views:** each object front + three-quarter on neutral ground; backpacks also shown **dropped/slumped on grass**; ball beside a backpack for scale
- **Dependent shots:** every THEN shot; S05_SH01, S07_SH01 (adult bag)

## Summary
| Asset ID | Type | Priority | Derived from | Shots depending |
|---|---|---|---|---|
| CHAR_LEO_BOY_MASTER | char | P1 | — | 9 |
| CHAR_LEO_ADULT_MASTER | char | P1 | CHAR_LEO_BOY_MASTER | 5 |
| CHAR_SAM_MASTER | char | P1 | — | 4 (+1 reuse) |
| CHAR_FRIENDS_SHEET | char | P2 | — | 5 |
| ENV_PITCH_THEN_E | env | P1 | — | 2 |
| ENV_PITCH_THEN_A | env | P1 | ENV_PITCH_THEN_E | 1 |
| ENV_PITCH_NOW_A | env | P1 | ENV_PITCH_THEN_A | 3 |
| ENV_PITCH_THEN_B | env | P2 | ENV_PITCH_THEN_E | 1 (+1 reuse) |
| ENV_PITCH_NOW_B | env | P2 | ENV_PITCH_THEN_B | 1 |
| ENV_GOAL_THEN_C | env | P2 | ENV_PITCH_THEN_E | 2 (+1 reuse) |
| ENV_FENCE_NOW_D | env | P2 | ENV_PITCH_NOW_A | 3 |
| PROP_SHEET_MASTER | prop | P1 | — | all THEN + 2 |
