"""Align narration sentences to an ElevenLabs MP3 using pause positions.
usage: python3 align.py partN.mp3 first_slide last_slide  -> writes partN_align.json
Each sentence end is mapped to a detected pause; sentence duration ~ rate * chars.
Dynamic programming keeps the order and minimises timing error, favouring longer pauses."""
import sys, re, json, subprocess
sys.path.insert(0,'/home/claude/c00/out/l1')
from syl import syl, envelope_peaks
import numpy as np
mp3, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
narr = json.load(open('/home/claude/c00/out/l1/narr.json'))
sents = []  # (slide, text)
for s in range(a, b + 1):
    t = narr[str(s)].replace('Quick, Draw!', 'Quick Draw§')
    for x in re.split(r'(?<=[.?!])\s+', t.strip()):
        if x: sents.append((s, x.replace('Quick Draw§', 'Quick, Draw!')))
out = subprocess.run(['ffmpeg', '-hide_banner', '-i', mp3, '-af', 'silencedetect=noise=-38dB:d=0.2', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp3],
                           capture_output=True, text=True).stdout)
starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]
ends = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
P = [(s, e) for s, e in zip(starts, ends) if s > 0.3 and e < dur - 0.2]  # interior pauses
lead = ends[0] if starts and starts[0] < 0.05 else 0.0
tail = starts[-1] if starts and ends[-1] >= dur - 0.25 else dur
n = len(sents); m = len(P)
L = [len(x) + 12 for _, x in sents]  # +12 chars ~ fixed per-sentence overhead
rate = (tail - lead) / sum(L)
PK = envelope_peaks(mp3)
SY = [syl(x) for _, x in sents]
ratio = ((PK >= lead) & (PK < tail)).sum() / sum(SY)
cnt = lambda t0, t1: int(((PK >= t0) & (PK < t1)).sum())
INF = 1e18
# dp[i][j]: first i sentences done, sentence i ends at pause j (j index into P); start boundary = lead
dp = [[INF] * (m + 1) for _ in range(n + 1)]; bk = [[-1] * (m + 1) for _ in range(n + 1)]
pos = lambda j: lead if j == -1 else P[j][0]       # speech end time at pause j
nxt = lambda j: lead if j == -1 else P[j][1]       # speech restart after pause j
def cost(i, jp, j):  # sentence i (0-based) spans from after pause jp to pause j
    c = cnt(nxt(jp), pos(j)); e = SY[i] * ratio
    plen = P[j][1] - P[j][0]
    return (c - e) ** 2 / (e + 2) - plen * 0.3
# use index shift: k=0 means 'lead'
best = {(-1): 0.0}; trail = []
prev = {-1: (0.0, None)}
layers = []
for i in range(n - 1):
    cur = {}
    for jp, (c0, _) in prev.items():
        for j in range(jp + 1, m):
            if pos(j) - nxt(jp) > L[i] * rate * 2.5: break
            c = c0 + cost(i, jp, j)
            if j not in cur or c < cur[j][0]: cur[j] = (c, jp)
    layers.append(cur); prev = cur
# last sentence ends at tail
fin = None
for jp, (c0, _) in prev.items():
    e = SY[n - 1] * ratio
    c = c0 + (cnt(nxt(jp), tail) - e) ** 2 / (e + 2)
    if fin is None or c < fin[0]: fin = (c, jp)
js = []; j = fin[1]
for i in range(n - 2, -1, -1):
    js.append(j); j = layers[i][j][1]
js.reverse()
res = []; t0 = lead
for i, (s, x) in enumerate(sents):
    te = pos(js[i]) if i < n - 1 else tail
    res.append(dict(slide=s, text=x, start=round(t0, 3), end=round(te, 3)))
    t0 = nxt(js[i]) if i < n - 1 else tail
json.dump(dict(mp3=__import__('os').path.abspath(mp3), duration=dur, sents=res), open(mp3.replace('.mp3', '_align.json'), 'w'), indent=1)
for r in res:
    print(f"{r['slide']:2d} {r['start']:7.2f}-{r['end']:7.2f} pk {cnt(r['start'], r['end']):3d} vs {syl(r['text'])*ratio:5.1f}  {r['text'][:50]}")
