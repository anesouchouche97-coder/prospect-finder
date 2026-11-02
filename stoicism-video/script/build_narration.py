import json, subprocess, sys
names=["s1_hook","s2_what","s3_control","s4_traffic","s5_story","s6_obstacle","s7_seneca","s8_close"]
LEAD=0.25; GAP=0.45
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())
t=LEAD; scenes=[]; inputs=[]; filt=[]
for i,n in enumerate(names):
    d=dur(f"assets/voice/{n}.wav")
    scenes.append({"id":n,"voiceStart":round(t,3),"voiceEnd":round(t+d,3)})
    t+=d+GAP
total=round(t+0.9,2)
# scene slots: each scene starts at its voice start minus 0.2 (first at 0), ends at next start
for i,s in enumerate(scenes):
    s["start"]=0 if i==0 else round(s["voiceStart"]-0.2,3)
for i,s in enumerate(scenes):
    s["end"]=scenes[i+1]["start"] if i+1<len(scenes) else total
    s["duration"]=round(s["end"]-s["start"],3)
cmd=["ffmpeg","-y","-v","error"]
for n in names: cmd+=["-i",f"assets/voice/{n}.wav"]
parts=[]
for i,s in enumerate(scenes):
    ms=int(s["voiceStart"]*1000)
    parts.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms}[a{i}]")
parts.append("".join(f"[a{i}]" for i in range(len(names)))+f"amix=inputs={len(names)}:normalize=0,apad=whole_dur={total}[out]")
cmd+=["-filter_complex",";".join(parts),"-map","[out]","-ac","1","-t",str(total),"assets/voice/narration.wav"]
subprocess.check_call(cmd)
json.dump({"total":total,"scenes":scenes},open("script/timing.json","w"),indent=1)
print(json.dumps({"total":total,"scenes":scenes},indent=1))
