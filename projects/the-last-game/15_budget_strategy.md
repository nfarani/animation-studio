# 15 — ESTIMATED MODEL / COST STRATEGY

**No credit figures are given.** Per-model pricing has not been verified. Balance at the time of planning: **576.22 credits** (plus plan), read with `higgsfield account status` on 2026-10-06. Whether that covers the film is unknown until `/assets` runs cost estimates.

```
PROJECT GENERATION PROFILE
Total planned shots: 22 — Economy 4 · Standard 13 · Premium 3 · Edit-only 2
Generated video clips: 20
Master assets: 12 (4 character, 7 environment, 1 prop sheet)
Shot keyframes (stills): ~17
High-risk shots: 4 · Expected regeneration-heavy shots: 4
Total video seconds in the cut: 34.0, of which 1.9 are free reuse
```

## Tier allocation
| Tier | Shots | Why |
|---|---|---|
| **ECONOMY (4)** | S01_SH02, S02_SH03, S04_SH02, S05_SH04 | Props and empty plates; little or no character motion |
| **STANDARD (13)** | S01_SH01, S01_SH03, S02_SH01, S02_SH02, S02_SH04, S03_SH01, S03_SH02, S03_SH04, S04_SH01, S05_SH01, S06_SH01, S06_SH04, S07_SH01 | Normal running, walking, simple acting; most are short and partly hidden by framing or blur |
| **PREMIUM (3)** | S03_SH03, S05_SH02, S06_SH03 | The three shots where a face carries the film |
| **Edit-only (2)** | S05_SH03, S06_SH02 | Reuse |

## Expected attempts
| Risk | Shots | Attempts each | Total attempts (range) |
|---|---|---|---|
| LOW | 4 | 1–2 | 4–8 |
| MEDIUM | 12 | 2–4 | 24–48 |
| HIGH | 4 | 3–4 (capped) | 12–16 |
| **All video** | **20** | | **40–72** |

## Major cost drivers
1. **S03_SH03** — premium + lip-sync + likely retries. Worth it: it is used twice and is the centre of the film.
2. **S05_SH02 / S06_SH03** — premium close-ups, expected rejections for over-acting.
3. **S07_SH01** — longest clip (4.3 s, needs a ≥ 5 s generation).
4. **Scene 2** — four short shots with a high retry rate between them.
5. **Master assets** — 12 assets plus iterations; the two character masters for Leo will take the most rounds.

## Savings already built into the plan
- Flash (S05_SH03) is a reuse, not a new premium generation.
- Second-memory goal shot (S06_SH02) is a reuse.
- The two empty holds are stills with ambient motion, not full video generations.
- Only one shot in the film is lip-synced; seven other lines are off-screen or unsynced.
- Shoulder-barge reframed from a two-character contact shot (premium) to a single (standard).
- S02_SH04 starts with the ball already in Danny's hands, removing a pickup.
- S06_SH04 starts with the hand already on the wire, removing the approach.
- Three NOW plates are edits of THEN plates rather than new generations with their own iteration cycles.

## Further reductions available
| Change | Saves | Costs |
|---|---|---|
| Drop S02_SH02 (barge) | 1 high-risk standard shot, 3–4 attempts | One fragment of the game; also gets 1.0 s back |
| Use S03_SH02 fallback (reverse S01_SH02) | 1 standard shot | The hand; the bag "un-drops" instead |
| Take S06_SH03 from a longer S05_SH02 generation | 1 premium shot | Less control over the smile |
| Make S04_SH02 and S05_SH04 pure stills with edit-side foliage motion | 2 economy generations | Slightly less life in the frame |
| S06_SH01 as backlit silhouettes on an economy model | Tier drop on 1 shot | Faces unreadable (acceptable for a memory) |
| Apply the 0:30 trim | Removes S02_SH02 and S03_SH02; merges S06_SH03/04 | See `02_creative_notes.md` note 1 |

With all reductions applied: 16 generated clips, 2 premium.

## Where not to save
- The three ANGLE A / ANGLE B plate pairs. They are the film.
- S03_SH03.
- The Leo boy → adult likeness.

## Spending rule
Every batch is proposed separately with a verified credit estimate and waits for approval. Nothing in this file is an approval.
