# EDIT TIMELINE — The Last Game

**Current cut: version 2** — `rough_cut/the-last-game_v2.mp4`, 2026-10-06.
Defined in `rough_cut/edl_v2.py`, built by `rough_cut/build_cut.py` (needs ffmpeg). Version 1 (`the-last-game_rough_v1.mp4`, `build_rough_cut.py`) is kept for comparison.

**Runtime 33.04 s of picture + 1.5 s black = 34.54 s.** 1920×1080 (upscaled from 720p sources), 24 fps constant, H.264 high profile, BT.709, AAC 48 kHz stereo. Loudness −14.7 LUFS integrated, true peak −1.4 dBTP. All cuts are hard cuts.

## Picture
| Time | Shot | Dur | Source (in-point) | Visual |
|---|---|---|---|---|
| 0:00.00 | S01_SH01 | 1.83 | v2_take1 (0.40) | Leo runs in with the ball (diagonal angle) |
| 0:01.83 | S01_SH02 | 0.92 | take1 (0.25) | Red backpack drops: goalposts |
| 0:02.75 | S01_SH03 | 1.42 | v2_take1 (0.15) | Ball poked away |
| 0:04.17 | S02_SH01 | 1.00 | take1 (0.50) | Legs chasing the ball |
| 0:05.17 | S02_SH02 | 1.08 | v2_take1 (0.70) | Shoulder bump; Leo stumbles, laughing |
| 0:06.25 | S02_SH03 | 1.17 | take1 (0.95) | Ball through the backpack goal |
| 0:07.42 | S02_SH04 | 1.58 | v2_take1 (0.35) | Danny runs off with the ball; Leo chases |
| 0:09.00 | S03_SH01 | 1.92 | v2_take1 (1.55) | Leo turns to the voice; "Coming!" |
| 0:10.92 | S03_SH03 | 1.75 | v2_take1 (1.75) | Sam: "You coming tomorrow?" |
| 0:12.67 | S03_SH04 | 2.17 | v2_take1 (0.40) | Over Sam's shoulder: "Yeah, obviously." He turns and runs |
| 0:14.83 | S04_SH01 | 1.50 | take1 (2.05) | Leo runs at camera; his shirt fills the frame |
| 0:16.33 | S04_SH02 | 1.25 | v2_take1 (0.50) | Same angle, years later, empty |
| 0:17.58 | S05_SH01 | 2.42 | take1 (0.45) | The man walks in, slows, stops |
| 0:20.00 | S05_SH02 | 1.83 | v2_take1 (1.15) | His face through the wire: recognition |
| 0:21.83 | S05_SH03 | 1.25 | S03_SH03 v2_take1 (2.00) | Flash: Sam's line |
| 0:23.08 | S05_SH04 | 1.08 | v2_take1 (0.50) | The same frame, empty |
| 0:24.17 | S06_SH01 | 1.25 | take1 (0.00) | Memory: boys run past |
| 0:25.42 | S06_SH03 | 1.42 | v2_take1 (2.45) | A small smile |
| 0:26.83 | S06_SH04 | 1.33 | take1 (1.55) | Hand on the wire, then off |
| 0:28.17 | S07_SH01 | 4.29 | v2_take1 (0.70) | Walks on, pauses, leaves frame right |
| 0:32.46 | hold | 0.58 | last frame of S07_SH01 | The empty pitch |
| 0:33.04 | black | 1.50 | — | Black, silent, no text |

## Sound
Picture and sound are cut separately, so lines run across picture cuts instead of being chopped.

| Starts | Sound | Note |
|---|---|---|
| 0:00.00–0:16.33 | Background: evening, children playing in the distance | generated ambience, low level |
| 0:02.75 | "Oi!" | finishes over the first frames of the next shot |
| 0:05.50 | "That wasn't in!" / "Course it was!" | starts under the bump shot, ends under the chase |
| 0:08.10 | Mother: "Come on! Dinner!" | starts over the chase; picture cuts to Leo on "Dinner!" |
| 0:10.00 | Leo: "Coming!" | |
| 0:11.35 | Sam: "You coming tomorrow?" | |
| 0:12.90 | Leo: "Yeah, obviously." | |
| 0:16.33 | **Silence, 0.32 s** | everything out on the last frame of the wipe |
| 0:16.63–0:33.04 | Background: wind in trees, distant traffic | generated ambience, fades in |
| 0:21.83 | Flash: "You coming tomorrow?" | same recording |
| 0:24.17 | Laughter | rings on under the smile and fades |
| 0:30.30 | Distant kick and children laughing | at the pause in the final shot, faint |
| 0:33.04 | **Silence, 1.47 s** | cut to black |

## Checks run on this cut
- **No line is cut:** the builder refuses to build if any audio edit lands inside a spoken line. All seven passes. The finished file was then transcribed: every scripted line is heard complete, in order.
- **Silences:** exactly two, at the wipe and in the black.
- **Constant 24 fps, 1080p, BT.709 tagged, −14.7 LUFS:** matches YouTube's reference loudness; no clipping.

## Not done
- No music.
- The faint "Come on!" child's voice at the end is not confirmed to be in the generated memory sound.
- Voices still come from separate generations, so the same character may sound different between shots.
