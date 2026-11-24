"""Render Lesson 1 from slide PNGs + aligned Ria audio parts.
usage: python3 render_lesson.py out.mp4 audio/part1_align.json [audio/part2_align.json ...]
- audio cut per slide at the middle of the pause before the slide's first sentence
- GAP seconds of silence inserted at each slide change; HEAD lead-in on slide 1; TAIL hold on the last slide
- 0.35 s crossfade between slides; captions per sentence (long ones split), burned in."""
import sys, json, subprocess, os, re, textwrap
out = sys.argv[1]; aligns = [json.load(open(p)) for p in sys.argv[2:]]
W = '/home/claude/c00/out/l1/build'; os.makedirs(W, exist_ok=True)
GAP, HEAD, TAIL, XF = 0.7, 0.8, 2.0, 0.35
def run(*a): subprocess.run(a, check=True, capture_output=True)

# 1) slide audio clips
clips = []  # (slide, wavpath, [(text, t0, t1) relative to clip start])
for A in aligns:
    S = A['sents']; slides = sorted({s['slide'] for s in S})
    for k, sl in enumerate(slides):
        ss = [s for s in S if s['slide'] == sl]
        prev_end = max((s['end'] for s in S if s['slide'] == slides[k-1]), default=0) if k else 0
        a0 = 0.0 if k == 0 else (prev_end + ss[0]['start']) / 2
        if k + 1 < len(slides):
            nxt = [s for s in S if s['slide'] == slides[k+1]][0]['start']
            a1 = (ss[-1]['end'] + nxt) / 2
        else:
            a1 = A['duration']
        wav = f'{W}/a{sl:02d}.wav'
        run('ffmpeg', '-y', '-i', A['mp3'], '-ss', f'{a0:.3f}', '-to', f'{a1:.3f}', '-ac', '1', '-ar', '44100', wav)
        clips.append((sl, wav, a1 - a0, [(s['text'], s['start'] - a0, s['end'] - a0) for s in ss]))

# 2) per-slide durations (audio + gap; head on first, tail on last)
segs = []; t = 0.0; caps = []
for i, (sl, wav, d, ss) in enumerate(clips):
    pre = HEAD if i == 0 else GAP / 2
    post = TAIL if i == len(clips) - 1 else GAP / 2
    total = pre + d + post
    for text, c0, c1 in ss: caps.append((text, t + pre + c0, t + pre + c1))
    segs.append((sl, wav, pre, post, total)); t += total

# 3) audio track
parts = []
for sl, wav, pre, post, total in segs:
    p = f'{W}/p{sl:02d}.wav'
    run('ffmpeg', '-y', '-i', wav, '-af', f'adelay={int(pre*1000)},apad=pad_dur={post:.3f}', '-ar', '44100', '-ac', '1', p)
    parts.append(p)
open(f'{W}/alist.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run('ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', f'{W}/alist.txt', '-c:a', 'pcm_s16le', f'{W}/audio.wav')

# 4) captions (ASS); split long sentences into chunks timed by characters
def chunks(text, maxc=84):
    if len(text) <= maxc: return [text]
    words = text.split(); out = []; cur = ''
    n = max(2, -(-len(text) // maxc)); target = len(text) / n
    for w in words:
        if cur and len(cur) + 1 + len(w) > target and len(out) < n - 1 and cur[-1] in ',:;' or (cur and len(cur) + 1 + len(w) > maxc):
            out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    out.append(cur); return out
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f'{h}:{m:02d}:{s:05.2f}'
ev = []
for text, c0, c1 in caps:
    ch = chunks(text); tot = sum(len(c) for c in ch); a = c0
    for c in ch:
        b = a + (c1 - c0) * len(c) / tot
        lines = textwrap.wrap(c, 46)
        ev.append(f"Dialogue: 0,{ts(a)},{ts(b + 0.15)},Cap,,0,0,0,,{'\\N'.join(lines)}"); a = b
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter,44,&H00FFFFFF,&H00FFFFFF,&H004C4F0B,&H1A4C4F0B,1,0,0,0,100,100,0,0,3,14,0,2,200,200,36,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(ev) + '\n'
open(f'{W}/captions.ass', 'w').write(ass)

# 5) video: stills with crossfades
inp = [];
for sl, wav, pre, post, total in segs:
    inp += ['-loop', '1', '-framerate', '25', '-t', f'{total + XF:.3f}', '-i', f'/home/claude/c00/out/l1/slides/s{sl:02d}.png']
fc = []; last = '[0:v]'; off = 0.0
for i in range(1, len(segs)):
    off += segs[i-1][4]
    fc.append(f'{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={off - XF/2:.3f}[x{i}]'); last = f'[x{i}]'
fc.append(f"{last}format=yuv420p,ass={W}/captions.ass[v]")
total = sum(s[4] for s in segs)
cmd = ['ffmpeg', '-y', *inp, '-i', f'{W}/audio.wav', '-filter_complex', ';'.join(fc), '-map', '[v]', '-map', f'{len(segs)}:a',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-r', '25', '-c:a', 'aac', '-b:a', '192k', '-t', f'{total:.3f}', '-movflags', '+faststart', out]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode: print(r.stderr[-3000:]); sys.exit(1)
json.dump(dict(chapters=[(sl, round(sum(x[4] for x in segs[:i]), 2)) for i, (sl, *_ ) in enumerate(segs)], total=total), open(f'{W}/chapters.json', 'w'))
print('ok', round(total, 1), 's')
