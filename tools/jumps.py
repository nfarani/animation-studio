"""usage: jumps.py <ffmpeg> <clip...>  -> frames where the picture changes abruptly between two frames (background jumps)"""
import sys, subprocess, numpy as np
FF=sys.argv[1]; w,h=320,180
for f in sys.argv[2:]:
    raw=subprocess.run([FF,"-loglevel","error","-i",f,"-vf",f"scale={w}:{h},format=gray","-f","rawvideo","-"],capture_output=True).stdout
    fr=np.frombuffer(raw,dtype=np.uint8).reshape(-1,h,w).astype(np.float32)
    mask=np.zeros((h,w),bool); mask[:40,:]=True; mask[:,:40]=True; mask[:,-40:]=True
    d=[float(np.abs(fr[i+1]-fr[i])[mask].mean()) for i in range(len(fr)-1)]; med=float(np.median(d))
    hits=[(i+1,x) for i,x in enumerate(d) if x>max(med*4,12)]
    print(f.split('/')[-1], f"median {med:.1f}", "JUMPS:" if hits else "no jumps", " ".join(f"f{i}({i/24:.2f}s,{x:.0f})" for i,x in hits))
