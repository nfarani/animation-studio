"""usage: speech.py <ffmpeg> <media...>  -> word timings (faster-whisper) and the span of confident speech"""
import sys, subprocess, os, wave
import numpy as np
from faster_whisper import WhisperModel
m=WhisperModel("small.en",device="cpu",compute_type="int8"); FF=sys.argv[1]; MINP=float(os.environ.get("MINP","0.5"))
for f in sys.argv[2:]:
    wav=os.path.join(os.path.dirname(os.path.abspath(FF)),"_sp.wav"); subprocess.run([FF,"-y","-loglevel","error","-i",f,"-ac","1","-ar","16000",wav],check=True)
    w=wave.open(wav); a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768; w.close()
    segs,_=m.transcribe(a,word_timestamps=True,vad_filter=False,condition_on_previous_text=False)
    ws=[(x.start,x.end,x.word.strip(),x.probability) for s in segs for x in s.words]
    good=[x for x in ws if x[3]>=MINP]
    print(os.path.basename(f),"| dur %.2f |"%(len(a)/16000),"words:"," ".join(f"[{x[0]:.2f}-{x[1]:.2f}]{x[2]}({x[3]:.2f})" for x in ws) or "(none)")
