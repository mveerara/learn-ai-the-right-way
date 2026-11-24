# Build decks, narration, voice paste, PDF and thumbnail for Course 0 lessons 1-5.
import sys, json, os, shutil, subprocess, importlib
sys.path.insert(0, '/home/claude/c00'); sys.path.insert(0, '/home/claude')
import deckkit as K
from PIL import Image
ONLY = sys.argv[1:] or ['1','2','3','4','5']
for n in ONLY:
    m = importlib.import_module(f'l{n}')
    out = f'/home/claude/c00/out/l{n}'
    os.makedirs(out + '/slides', exist_ok=True); os.makedirs(out + '/audio', exist_ok=True)
    for i, sl in enumerate(m.SL, 1):
        sl['body'] = sl['body'].replace('pREC', f'p{i}')
    K.render(m.SL, m.META['label'], out)
    for f in ('shoot.py', 'align.py', 'syl.py', 'render_lesson.py'):
        shutil.copy(f'/home/claude/l03/{f}', out)
    for f in ('align.py', 'render_lesson.py'):
        p = f'{out}/{f}'; t = open(p).read().replace('/home/claude/l03', out); open(p, 'w').write(t)
    subprocess.run(['python3', 'shoot.py', out], cwd=out, check=True, capture_output=True)
    narr = {str(i): x for i, x in enumerate(m.N, 1)}
    json.dump(narr, open(f'{out}/narr.json', 'w'), indent=1, ensure_ascii=False)
    # split into 3 parts at slide boundaries, balancing words
    w = [len(x.split()) for x in m.N]; tot = sum(w); cuts = []; acc = 0
    for i, x in enumerate(w):
        acc += x
        if len(cuts) < 2 and acc >= tot * (len(cuts) + 1) / 3: cuts.append(i + 1)
    bounds = [(1, cuts[0]), (cuts[0] + 1, cuts[1]), (cuts[1] + 1, len(w))]
    json.dump(bounds, open(f'{out}/parts.json', 'w'))
    txt = [f"COURSE 0 · LESSON {n}: {m.META['title']}  (voice: Bella, same settings)\n"]
    for k, (a, b) in enumerate(bounds, 1):
        txt.append(f"===== PART {k}: slides {a}-{b} =====\n\n" + "\n\n".join(narr[str(i)] for i in range(a, b + 1)))
    open(f'{out}/voice_paste.txt', 'w').write("\n\n\n".join(txt) + "\n")
    ims = [Image.open(f'{out}/slides/s{i:02d}.png').convert('RGB') for i in range(1, len(m.SL) + 1)]
    ims[0].save(f'{out}/C0L{n}_deck.pdf', save_all=True, append_images=ims[1:])
    ims[0].resize((1280, 720), Image.LANCZOS).save(f'{out}/C0L{n}_thumbnail.jpg', quality=90)
    print(n, len(m.SL), 'slides; parts', bounds)
