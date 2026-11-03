# 18 — PRE-PRODUCTION QA

Audit of the plan in files 01–17, dated 2026-10-06. Nothing has been generated, so this checks the plan, not footage.

| Check | Result | Notes |
|---|---|---|
| STORY | PASS | Every scene carries a beat. Scene 2 is the only one that could lose a shot (S02_SH02) without loss. |
| CONTINUITY | PASS on paper | Ledger complete. Six match checks listed for `/qa` once footage exists. |
| EMOTION | PASS | Arc is visible in picture alone: fast/warm → locked/cool → small smile → walks on. |
| CAMERA | PASS | See variety table below. No two adjacent shots share scale and angle, except the deliberate ANGLE A repeats. |
| GENERATION | PASS with 4 flagged | All shots are single-action. Four HIGH-RISK shots have two fallbacks and a cheaper alternative each. |
| PACING | PASS, over length | 34.0 s against ~30 s. Trim defined. Adult half has room; childhood half is fast. |
| AUDIO | OPEN | Sound layer is specified per shot. **Voice casting is unresolved** (risk 4). |
| VISUAL REPETITION | PASS | Repetition is used on purpose three times (ANGLE A ×4 shots, ANGLE B ×3, goal setup ×3) and nowhere by accident. |
| CHARACTER | PASS | Each recurring character has identifiers, a posture and a behaviour. Performances are specified physically. |
| RETENTION | PASS | No gap over ~2.5 s without a change. Main risk is a generic-looking first half. |
| AI FAILURE RISKS | Listed | Most likely to fail: S06_SH04, S02_SH02, S03_SH03, S04_SH01, in that order. |
| MODEL OVERSPEND | PASS | 3 premium shots of 22, all face-led. No premium on action. |
| REUSE | PASS | 2 edit-only shots; 2 holds as stills; 6 plates support 20 shots; 3 NOW plates are edits. |
| MISSING MASTER REFERENCES | PASS | Every shot's assets exist in file 08. None is generated or approved yet. |
| SCREEN DIRECTION | PASS | West = left, east = right from all south-side cameras. Two reverses (S03_SH04, ANGLE D) are motivated and noted. |
| ENVIRONMENT CONSISTENCY | PASS on paper | One geography, five named camera positions, era change by edit. |
| PROP CONSISTENCY | PASS | Goal position ledger in file 07. Ball stays with Sam. Nothing left in NOW. |

## Shot variety
| Shot | Scale | Angle / height | Camera |
|---|---|---|---|
| S01_SH01 | wide | standing, ANGLE E | static |
| S01_SH02 | insert | ground, into sun | static |
| S01_SH03 | insert (feet) | ankle, side-on | static |
| S02_SH01 | medium (legs) | knee, side-on | lateral track |
| S02_SH02 | medium | chest, ¾ front | handheld drift |
| S02_SH03 | low wide insert | ground, behind goal | static |
| S02_SH04 | wide | standing, ANGLE E | static |
| S03_SH01 | medium | eye level, profile | static |
| S03_SH02 | insert | ground, into sun | static |
| S03_SH03 | full | child eye level, frontal | static |
| S03_SH04 | medium-wide | child eye level, reverse | static |
| S04_SH01 | wide → occluded | ANGLE A | locked |
| S04_SH02 | wide | ANGLE A | locked |
| S05_SH01 | wide | ANGLE A | locked |
| S05_SH02 | close-up | adult eye level, through wire | static |
| S05_SH03 | full | (S03_SH03) | static |
| S05_SH04 | full, empty | ANGLE B | locked |
| S06_SH01 | low medium-wide | 1 m, into sun | static |
| S06_SH02 | low insert | (S02_SH03) | static |
| S06_SH03 | close-up | ANGLE D | static |
| S06_SH04 | macro insert | hand height | static |
| S07_SH01 | wide | ANGLE A | locked |

Moving camera: 2 of 22 shots, both in Scene 2, both motivated by momentum. The second half has no camera movement at all. This is deliberate: the past moves, the present is still.

## Issues found and resolved during planning
1. Three-line argument in a 1.2 s shot → "You're joking!" cut.
2. Six potential lip-sync lines → one.
3. Two-character contact shot → reframed as a single.
4. S06_SH01 originally included Leo → changed to his point of view (three friends only), which removes one identity from a three-body shot.
5. ANGLE A camera originally placed on the footpath → moved to the verge so the adult can walk between camera and fence.

## Open issues
| # | Issue | Owner | Needed by |
|---|---|---|---|
| 1 | Runtime: 34 s plan or 30 s trim | Creator | before `/prompts` |
| 2 | Aspect ratio: 16:9 assumed | Creator | **before `/assets`** (plates are composed to it) |
| 3 | Voices: recorded, synthetic or library | Creator | before S03_SH03 if lip-sync is audio-driven; otherwise `/edit` |
| 4 | Music: sparse motif under the memories, or none | Creator | `/edit` |
| 5 | STYLE_BIBLE rules are PROVISIONAL | Creator | confirm or correct as assets come back |
| 6 | Adapter capabilities and pricing UNVERIFIED | Production | during `/assets`, free |

Only issue 2 blocks the next command.

## Verdict
The plan is ready for `/assets`. No major story change is proposed.
