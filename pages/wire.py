# Wire real YouTube links into the Lesson 1-3 pages.
# usage: python3 wire.py START_URL L1_URL L2_URL L3_URL
import sys, re
SH, V1, V2, V3 = sys.argv[1:5]
CAT = "https://claude.ai/artifact/1S27dYy5tfBcnoW8L9NmsE"
PAGES = {
 1: dict(next=("Lesson 2: The workbench, one setup for every course and every job", V2, "Next video in the playlist"),
         basic=("Rewatch Lesson 1", V1, "Then try the quiz again"), recap_old="A one-minute recap of the three nested circles"),
 2: dict(next=("Lesson 3: Colab with Google Drive that remembers your work", V3, "Next video in the playlist · bring a Google account"),
         basic=("Rewatch Lesson 2", V2, "Then try the quiz again"), recap_old="A one-minute recap of the five workbench steps"),
 3: dict(next=("Course 0: Linux basics", CAT, "Coming next · see the course catalogue"),
         basic=("Rewatch Lesson 3", V3, "Then try the quiz again"), recap_old="A one-minute recap of the golden rule"),
}
for n, c in PAGES.items():
    p = f"/home/claude/quiz/lesson{n}.html"
    t = open(p).read()
    nt, nu, nf = c["next"]; bt, bu, bf = c["basic"]
    t = re.sub(r'const NEXT = \{[^}]*\};', f'const NEXT = {{title:{nt!r}, url:{nu!r}, foot:{nf!r}}};', t)
    t = re.sub(r'const BASIC = \{[^}]*\};', f'const BASIC = {{title:{bt!r}, url:{bu!r}, foot:{bf!r}}};', t)
    t = re.sub(r'<span class="foot">Lesson \$\{NEXT\.id\}[^<]*</span>', '<span class="foot">${NEXT.foot}</span>', t)
    t = t.replace(f'<span class="foot">{c["recap_old"]}</span>', '<span class="foot">${BASIC.foot}</span>')
    t = re.sub(r'<a class="btn" href="#next"( id="goNext")?>Start the next lesson</a>',
               lambda m: f'<a class="btn" href="${{NEXT.url}}" target="_blank" rel="noopener"{m.group(1) or ""}>{"Open the catalogue" if n==3 else "Watch the next lesson"}</a>', t)
    t = re.sub(r'<a class="btn" href="#short"( id="goShort")?>Watch the 60-second recap</a>',
               lambda m: f'<a class="btn" href="${{BASIC.url}}" target="_blank" rel="noopener"{m.group(1) or ""}>Rewatch the lesson</a>', t)
    t = re.sub(r'<p class="foot">Pass mark: 80% \(4 out of 5\)\.[^<]*</p>',
               f'<p class="foot">Pass mark: 80% (4 out of 5). New here? <a href="{SH}" target="_blank" rel="noopener" style="color:var(--accent);font-weight:600">Start here</a> · <a href="{CAT}" target="_blank" rel="noopener" style="color:var(--accent);font-weight:600">Course catalogue</a></p>', t)
    t = t.replace('or watch the 60-second recap first and then retry', 'or rewatch the lesson first and then retry')
    for bad in ('href="#next"', 'href="#short"', 'placeholder', 'Prototype', 'NEXT.id', '60-second'):
        assert bad not in t, (n, bad)
    open(p, "w").write(t)
    print("wired lesson", n)
