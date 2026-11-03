#!/usr/bin/env python3
"""Assemble a cut of The Last Game from an EDL file, with picture and sound edited separately.

usage: python3 build_cut.py <ffmpeg> <edl.py> <output.mp4>

The EDL file defines:
  FPS, VIDEO = [(shot, kind, source, in_seconds, frames, opts)]      kind: clip | still | black
  AUDIO = [(label, source, in_seconds, duration, timeline_start, gain, fade_in, fade_out)]
          timeline_start may be a number or ("sync", shot)  -> audio stays in sync with that shot's picture
          (i.e. it is placed so that source time `in_seconds` lines up with wherever that time falls
           relative to the shot's own in-point, even if that is before or after the shot is on screen)
  SPEECH = {source: (start, end, text)}   spoken lines that must never be cut

Checks before building (the build stops if any fails):
  1. every AUDIO event taken from a source with a SPEECH span either contains the whole span
     (with a safety margin) or does not touch it at all;
  2. no audio event runs past the end of its source file;
  3. picture segments are whole numbers of frames.
"""
import subprocess, sys, os, json, runpy

FF, EDL_PATH, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = runpy.run_path(EDL_PATH, {"P": P})
FPS, VIDEO, AUDIO, SPEECH = E["FPS"], E["VIDEO"], E["AUDIO"], E["SPEECH"]
MARGIN_IN, MARGIN_OUT = 0.08, 0.10
W, H = E.get("SIZE", (1920, 1080))
TMP = os.path.join(P, "edit", "_tmp"); os.makedirs(TMP, exist_ok=True)

def run(a, capture=False):
    r = subprocess.run([FF, "-y", "-hide_banner"] + a, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg failed:\n" + r.stderr[-1500:])
    return r.stderr

def dur_of(src):
    r = subprocess.run([FF, "-hide_banner", "-i", src], capture_output=True, text=True).stderr
    h, m, s = r.split("Duration: ")[1].split(",")[0].split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)

# ---------- timeline ----------
t = 0.0; starts = {}; rows = []
for shot, kind, src, ss, frames, opts in VIDEO:
    starts[shot] = (t, ss, frames / FPS)
    rows.append((t, shot, kind, frames / FPS)); t += frames / FPS
TOTAL = t

def tl_start(ev):
    label, src, ss, d, where, gain, fi, fo = ev[:8]
    if isinstance(where, tuple) and where[0] == "sync":
        shot_t, shot_in, _ = starts[where[1]]
        return shot_t + (ss - shot_in)
    if isinstance(where, tuple) and where[0] == "at":      # ("at", shot, offset): offset seconds after that shot starts
        return starts[where[1]][0] + where[2]
    return float(where)

# ---------- checks ----------
problems = []; report = []
for ev in AUDIO:
    label, src, ss, d, where, gain, fi, fo = ev[:8]
    ts = tl_start(ev)
    if ts < -1e-6: problems.append(f"{label}: starts before the film ({ts:.2f}s)")
    if os.path.exists(src) and ss + d > dur_of(src) + 0.05:
        problems.append(f"{label}: runs past the end of its source ({ss + d:.2f} > {dur_of(src):.2f})")
    if src in SPEECH:
        a, b, text = SPEECH[src]
        inside = ss <= a - MARGIN_IN + 1e-6 and ss + d >= b + MARGIN_OUT - 1e-6
        clear = ss + d <= a - 0.02 or ss >= b + 0.02
        state = "whole line" if inside else ("no speech" if clear else "CUTS THE LINE")
        report.append((ts, label, text, f"{a:.2f}-{b:.2f}", f"{ss:.2f}-{ss + d:.2f}", state))
        if not (inside or clear):
            problems.append(f"{label}: audio {ss:.2f}-{ss + d:.2f} cuts into \"{text}\" ({a:.2f}-{b:.2f})")
print("PICTURE")
for ts, shot, kind, d in rows: print(f"  {ts:6.2f}  {shot:10s} {kind:5s} {d:5.2f}s")
print(f"  total {TOTAL:.2f}s\nSPEECH CHECK")
for ts, label, text, sp, used, state in sorted(report):
    print(f"  {ts:6.2f}  {label:22s} line {sp:11s} used {used:11s} {state:14s} \"{text}\"")
if problems:
    sys.exit("BUILD STOPPED:\n  " + "\n  ".join(problems))
print("  all spoken lines are complete")

# ---------- picture ----------
VF = f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1,fps={FPS},format=yuv420p"
VENC = ["-an", "-c:v", "libx264", "-preset", "slow", "-crf", "15", "-pix_fmt", "yuv420p",
        "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-r", str(FPS)]
segs = []
for n, (shot, kind, src, ss, frames, opts) in enumerate(VIDEO):
    out = f"{TMP}/{n:02d}_{shot}.mp4"; vf = VF
    if "grade" in opts: vf += "," + opts["grade"]
    if kind == "clip":
        if "zoom" in opts:
            z = opts["zoom"]; vf = f"scale={int(W * z) // 2 * 2}:{int(H * z) // 2 * 2}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1,fps={FPS},format=yuv420p"
        run(["-ss", f"{ss:.3f}", "-i", src, "-vf", vf, "-frames:v", str(frames)] + VENC + [out])
    elif kind == "still":
        run(["-loop", "1", "-framerate", str(FPS), "-i", src, "-vf", vf, "-frames:v", str(frames)] + VENC + [out])
    elif kind == "black":
        run(["-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}", "-frames:v", str(frames)] + VENC + [out])
    segs.append(out)
lst = f"{TMP}/list.txt"; open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
run(["-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", f"{TMP}/picture.mp4"])

# ---------- sound ----------
inputs = []; filt = []; labels = []
for i, ev in enumerate(AUDIO):
    label, src, ss, d, where, gain, fi, fo = ev[:8]
    ts = tl_start(ev)
    inputs += ["-ss", f"{ss:.3f}", "-t", f"{d:.3f}", "-i", src]
    ms = int(round(ts * 1000))
    filt.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,volume={gain},"
                f"afade=t=in:st=0:d={fi},afade=t=out:st={max(0, d - fo):.3f}:d={fo},adelay={ms}|{ms}[a{i}]")
    labels.append(f"[a{i}]")
filt.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=longest,apad,atrim=0:{TOTAL:.3f}[mix]")
run(inputs + ["-filter_complex", ";".join(filt), "-map", "[mix]", "-c:a", "pcm_s24le", f"{TMP}/mix.wav"])

STEMS = E.get("STEMS_DIR")
if STEMS:
    os.makedirs(STEMS, exist_ok=True)
    names = sorted({ev[8] for ev in AUDIO if len(ev) > 8})
    for name in names:
        ins = []; fl = []; lab = []; k = 0
        for ev in AUDIO:
            if len(ev) > 8 and ev[8] == name:
                label, src, ss, d, where, gain, fi, fo = ev[:8]; ms = int(round(tl_start(ev) * 1000))
                ins += ["-ss", f"{ss:.3f}", "-t", f"{d:.3f}", "-i", src]
                fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={gain},afade=t=in:st=0:d={fi},afade=t=out:st={max(0, d - fo):.3f}:d={fo},adelay={ms}|{ms}[a{k}]"); lab.append(f"[a{k}]"); k += 1
        fl.append("".join(lab) + f"amix=inputs={len(lab)}:normalize=0:duration=longest,apad,atrim=0:{TOTAL:.3f}[m]")
        run(ins + ["-filter_complex", ";".join(fl), "-map", "[m]", "-c:a", "pcm_s24le", os.path.join(STEMS, E.get("STEM_PREFIX", "") + name + ".wav")])
    print("stems:", ", ".join(names))

# two-pass loudness normalisation to the YouTube reference level (-14 LUFS, -1.5 dBTP)
m = run(["-i", f"{TMP}/mix.wav", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"])
j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
      f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
run(["-i", f"{TMP}/mix.wav", "-af", ln + ",aresample=48000", "-c:a", "pcm_s24le", f"{TMP}/mix_norm.wav"])

# ---------- mux ----------
run(["-i", f"{TMP}/picture.mp4", "-i", f"{TMP}/mix_norm.wav", "-c:v", "copy",
     "-bsf:v", "h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1", "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
     "-shortest", "-movflags", "+faststart", OUT])
print(f"measured before normalisation: {j['input_i']} LUFS, true peak {j['input_tp']} dBTP")
import shutil; shutil.rmtree(TMP, ignore_errors=True)
print(f"written: {OUT}")
