# EDL for EP01 PART 1 — HOOK VERSION (cold open in the dandruff world, shorter Dan section).
# Based on the approved version 1 edit (edl_part01.py); everything from the descent onward is unchanged.
# EDL for EP01 PART 1. Read by build_cut.py; `P` (episode folder) is injected.
# VERSION=MASTER (intro + story + outro) or VERSION=CLEAN (story only), from the environment.
import os
VERSION = os.environ.get("VERSION", "MASTER")
FPS = 24
SIZE = (1920, 1080)
R = lambda n: f"{P}/renders/{n}_take1.mp4"
A = lambda n: f"{P}/audio/{n}"
NARR = "Arthur"                      # locked narrator voice (see 04_continuity_lock.md)
S1A, S1B, S1C = R("S1_SH01"), R("S1_SH02"), R("S1_SH03")
S2A, S2B = R("S2_SH01"), R("S2_SH02")
CO1, CO2 = R("CO_SH01"), R("CO_SH02")                  # cold open: the tremor, wide and close
S1C_FAST = f"{P}/edit/seg_S1_SH03_fast.mp4"            # the push-in on Dan's hair at 1.4x
ROOM, ENTER, STATUS, SCAL = R("S3_SH01"), R("S3_SH03"), R("S3_SH04"), R("S3_SH05")
ARA, ARB = R("S3_SH06A"), R("S3_SH06B")
REACT, LENS, OBS, FLAG, GROUP, BELLV, TOWN = R("S3_SH07"), R("S3_SH08"), R("S3_SH09"), R("S3_SH10"), R("S3_SH13"), R("S3_SH14"), R("S4_SH01")

COLD_OPEN = [
    ("CO_SH01", "clip", CO1, 0.20, 77, {}),        # the world at peace, then one enormous distant boom
    ("CO_SH02", "clip", CO2, 1.10, 68, {}),        # a townsperson on a thread bridge steadies herself and looks up
]
STORY = [
    ("S1_SH01", "clip", S1A, 0.85, 79, {}),        # Dan and friends; starts on a bounce of the ball
    ("S1_SH03", "clip", S1C_FAST, 0.00, 86, {}),   # the camera closes on his hair (faster); the ball-stealing shot is dropped
    ("S2_SH01", "clip", S2A, 0.08, 110, {}),   # into the hair: the Forest Trees
    ("S2_SH02", "clip", S2B, 0.10, 115, {}),   # descent to the Scalpence Centre
    ("S3_SH01", "clip", ROOM, 0.20, 82, {}),   # the Centre at work
    ("S3_SH03", "clip", ENTER, 0.50, 100, {}), # General Arrow enters
    ("S3_SH04", "clip", STATUS, 1.20, 55, {}), # "What's the Boy's status?"
    ("S3_SH05", "clip", SCAL, 0.10, 118, {}),  # the Senior Scalpetist answers
    ("A_PIC",   "clip", ARA, 0.10, 124, {}),   # "Alright, everyone. Listen up! The Boy is heading to the Green Field."
    ("A_CUT1",  "clip", REACT, 1.00, 26, {}),  # workers react            (Arrow's take A continues underneath)
    ("A_CUT2",  "clip", LENS, 0.80, 46, {}),   # lens swings round        ("...on every telescope.")
    ("A_CUT3",  "clip", OBS, 0.60, 43, {}),    # observer scans the sky   ("Watch for contaminated Heads.")
    ("B_CUT1",  "clip", FLAG, 0.60, 43, {}),   # signal flag hauled up    ("Issue a wet-soil warning.")
    ("B_PIC1",  "clip", ARB, 1.89, 71, {}),    # "And recommend all elders remain indoors tonight."
    ("B_CUT2",  "clip", ROOM, 2.60, 18, {}),   # activity increases       (pause in take B)
    ("B_PIC2",  "clip", ARB, 5.60, 146, {}),   # "The Head will be shaking ... Understood?"
    ("S3_SH13", "clip", GROUP, 0.15, 79, {}),  # "Sir, yes, sir!"
    ("S3_SH14", "clip", BELLV, 0.30, 62, {}),  # the warning bell
]
if VERSION == "MASTER":
    # no separate intro card: the title rides over the descent, where the music begins
    TITLED = f"{P}/edit/seg_descent_titled.mp4"
    STORY = [(n, k, TITLED, 0.0, fr, o) if n == "S2_SH01" else (n, k, TITLED, 110 / 24, fr, o) if n == "S2_SH02" else (n, k, src, ss, fr, o)
             for (n, k, src, ss, fr, o) in STORY]
    VIDEO = COLD_OPEN + STORY + \
            [("S4_SH01", "clip", f"{P}/edit/seg_ending_with_outro.mp4", 0.0, 163, {})]   # Head Centre bell, dissolving to the outro card
else:
    VIDEO = COLD_OPEN + STORY + [("S4_SH01", "clip", TOWN, 0.20, 110, {})]

# spoken lines that must be heard whole or not at all: source -> (start, end, text)
# (the narrator files begin on the first word and are always used from 0.00, so their spans start at 0.09)
SPEECH = {
    A(f"narr_{NARR}_1.mp3"): (0.09, 2.72, "This is Dan. He's a pretty normal kid."),
    A(f"narr_{NARR}_2.mp3"): (0.20, 3.02, "Except there's a little more going on in his hair than he knows."),
    A(f"narr_{NARR}_3.mp3"): (0.09, 0.80, "A lot more."),
    STATUS: (1.60, 3.02, "What's the Boy's status?"),
    SCAL:   (0.40, 4.64, "He's finished school. He's heading to the Green Field with his friends."),
    ARA:    (0.30, 9.52, "Alright, everyone. Listen up! The Boy is heading to the Green Field. Get someone on every telescope. Watch for contaminated Heads."),
    ARB:    (0.09, 11.42, "Issue a wet-soil warning. And recommend all elders remain indoors tonight. The Head will be shaking, and I want every possible Long Foot threat contained. Understood?"),
    GROUP:  (0.38, 1.78, "Sir, yes, sir!"),
}
sync = lambda shot: ("sync", shot)
at = lambda shot, off=0.0: ("at", shot, off)
D, M, X = "dialogue", "music", "effects"
# (label, source, in, duration, timeline start, gain, fade in, fade out, stem)
AUDIO = [
    # ---- narration ----
    ("VO 1", A(f"narr_{NARR}_1.mp3"), 0.00, 3.10, at("S1_SH01", 0.20), 1.00, 0.02, 0.10, D),
    ("VO 2", A(f"narr_{NARR}_2.mp3"), 0.00, 3.34, at("S1_SH03", 0.15), 1.00, 0.02, 0.10, D),
    ("VO 3", A(f"narr_{NARR}_3.mp3"), 0.00, 1.50, at("S2_SH01", 0.30), 1.00, 0.02, 0.15, D),
    # ---- cold open: the hidden world, then the boom ----
    ("cold open air (borrowed from the descent)", S2B, 0.60, 3.40, at("CO_SH01", 0.00), 0.45, 0.50, 0.50, X),
    ("cold open tremor, wide", CO1, 0.20, 3.21, sync("CO_SH01"), 0.90, 0.05, 0.25, X),
    ("cold open boom", A("scale_boom.mp3"), 0.00, 4.20, at("CO_SH01", 1.25), 0.75, 0.03, 1.40, X),
    ("cold open bridge", CO2, 1.10, 2.83, sync("CO_SH02"), 0.90, 0.15, 0.20, X),
    # ---- the human world (kept under the narrator) ----
    ("street 1", S1A, 0.85, 3.29, sync("S1_SH01"), 0.50, 0.03, 0.20, X),
    ("street 3, sinking away", S1C_FAST, 0.00, 3.58, sync("S1_SH03"), 0.45, 0.15, 0.60, X),
    # ---- the change of scale ----
    ("giant boom", A("scale_boom.mp3"), 0.00, 4.20, at("S2_SH01", 1.70), 0.55, 0.05, 1.50, X),
    ("descent 1", S2A, 0.08, 4.58, at("S2_SH01", 0.00), 0.60, 0.40, 0.30, X),
    ("descent 2", S2B, 0.10, 4.79, at("S2_SH02", 0.00), 0.60, 0.30, 0.40, X),
    # ---- music: enters on the descent, drops under the dialogue, out before the Long Foot line ----
    ("music, descent", A("music_motif.m4a"), 0.00, 10.60, at("S2_SH01", 0.30), 0.34, 1.80, 1.00, M),
    ("music, under dialogue", A("music_motif.m4a"), 9.60, 27.00, at("S2_SH01", 9.90), 0.13, 1.00, 3.00, M),
    # ---- Scalpence Centre ambience (dips out for the Long Foot line, returns with the room) ----
    ("centre bed 1", A("bed_scalpence.mp3"), 0.00, 29.50, at("S3_SH01", 0.00), 0.26, 0.60, 1.20, X),
    ("centre bed 2", A("bed_scalpence.mp3"), 2.00, 6.00, at("S3_SH13", 1.60), 0.30, 0.40, 0.80, X),
    ("room", ROOM, 0.20, 3.42, sync("S3_SH01"), 0.55, 0.30, 0.25, X),
    ("Arrow enters", ENTER, 0.50, 4.17, sync("S3_SH03"), 0.70, 0.15, 0.20, X),
    # ---- dialogue ----
    ("Arrow: status", STATUS, 1.20, 2.29, sync("S3_SH04"), 1.00, 0.10, 0.10, D),
    ("Scalpetist", SCAL, 0.10, 4.92, sync("S3_SH05"), 1.00, 0.10, 0.10, D),
    ("Arrow: take A (runs under three cutaways)", ARA, 0.10, 9.96, sync("A_PIC"), 1.00, 0.08, 0.10, D),
    ("Arrow: take B (starts a breath before the flag cutaway)", ARB, 0.00, 11.70, at("B_CUT1", -0.10), 1.00, 0.02, 0.12, D),
    ("Scalpetists: Sir, yes, sir!", GROUP, 0.15, 3.29, sync("S3_SH13"), 0.90, 0.08, 0.25, D),
    # ---- cutaway effects, low, under his voice ----
    ("lens", LENS, 0.80, 1.92, sync("A_CUT2"), 0.30, 0.15, 0.25, X),
    ("flag", FLAG, 0.60, 1.79, sync("B_CUT1"), 0.30, 0.15, 0.25, X),
    # ---- the warning bell: one recording, carried across the cut to Head Centre ----
    ("warning bell, close", A("warning_bell.mp3"), 0.00, 2.70, at("S3_SH14", 0.25), 0.85, 0.02, 0.35, X),
    ("warning bell, across the town", A("warning_bell.mp3"), 2.45, 5.40, at("S3_SH14", 2.60), 0.42, 0.20, 1.60, X),
    ("town hush", TOWN, 0.20, 4.50, sync("S4_SH01") if VERSION == "CLEAN" else at("S4_SH01", 0.00), 0.10, 0.40, 1.20, X),
]
if VERSION == "MASTER":
    AUDIO += [
        ("Tiny Tales sting, outro", A("sting_ident.m4a"), 0.00, 3.20, at("S4_SH01", 4.20), 0.60, 0.02, 0.80, M),
    ]
    STEMS_DIR = f"{P}/deliverables/hook/stems"; STEM_PREFIX = "EP01_PART01_HOOK_MASTER_"
