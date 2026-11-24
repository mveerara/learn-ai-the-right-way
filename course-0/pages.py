# Generate Course 0 lesson pages (lab + quiz + FAQ) from the Lesson 3 page.
import sys, json, re, importlib
sys.path.insert(0, '/home/claude/c00')
TPL = open('/home/claude/quiz/lesson3.html').read()
CHANNEL = 'https://www.youtube.com/@LearnAItheRightway/videos'
CAT = 'https://claude.ai/artifact/1S27dYy5tfBcnoW8L9NmsE'
MENTOR = TPL[TPL.index(' ["Can I ask a question or get help from a mentor?"'):TPL.index(']\n];\ndocument.getElementById("faqList")') + 1]

def sub(t, a, b, count=1):
    assert t.count(a) >= 1, a[:70]
    return t.replace(a, b, count)

def js(v): return json.dumps(v, ensure_ascii=False)

for n in sys.argv[1:] or ['1', '2', '3', '4', '5']:
    m = importlib.import_module(f'l{n}'); M = m.META
    t = TPL
    t = re.sub(r'<title>[^<]*</title>', f'<title>Course 0 Lesson {n} Lab and Quiz</title>', t, count=1)
    t = sub(t, 'Learn AI the Right Way · Course 1 · Lesson 3', f'Learn AI the Right Way · Course 0 · Lesson {n} · {M["module"]}')
    t = sub(t, '<h1>Step one: Colab with a memory</h1>', f'<h1>{M["h1"]}</h1>')
    t = sub(t, 'Guided lab: a workbench that remembers', 'Guided lab: try it in Colab')
    t = sub(t, 'About 20 minutes. You need a Google account and a browser.', 'About 20 minutes in a Colab notebook: start Linux lines with <code>!</code>.')
    t = re.sub(r'const LAB = \[.*?\n\];', 'const LAB = ' + js(m.LAB) + ';', t, count=1, flags=re.S)
    t = sub(t, 'const KEY = "lairw-l3-lab";', f'const KEY = "lairw-c0l{n}-lab";')
    t = sub(t, "Your workbench remembers. That's the habit that matters most. Now try the quiz.", "Every step done. Now try the quiz.")
    t = re.sub(r'const QUIZ = \[.*?\n\];', 'const QUIZ = ' + js(m.QUIZ) + ';', t, count=1, flags=re.S)
    t = sub(t, '$("q").textContent = it.q;', '$("q").innerHTML = it.q;')
    t = re.sub(r"const NEXT = \{.*?\};", 'const NEXT = ' + js(dict(title=M['next_title'], url=CHANNEL, foot='Coming soon on the channel')) + ';', t, count=1)
    t = re.sub(r"const BASIC = \{.*?\};", 'const BASIC = ' + js(dict(title=f'Rewatch Course 0, Lesson {n}', url=CHANNEL, foot='Then try the quiz again')) + ';', t, count=1)
    t = sub(t, '"Brilliant, a perfect score. Your workbench has a memory." : "Well done, you passed. You\'ve got the key habit."',
               '"Brilliant, a perfect score." : "Well done, you passed."')
    t = sub(t, '>Open the catalogue</a>', '>Go to the channel</a>')
    faq = js([list(x) for x in m.FAQ])[:-1] + ',\n' + MENTOR + ']'
    t = re.sub(r'const FAQ = \[.*?\n\];', 'const FAQ = ' + faq + ';', t, count=1, flags=re.S)
    t = sub(t, '<h2 id="faqh">Lesson 3 FAQ</h2>', f'<h2 id="faqh">Course 0, Lesson {n} FAQ</h2>')
    out = f'/home/claude/c00/out/l{n}/page.html'
    open(out, 'w').write(t)
    for bad in ('Course 1 · Lesson 3', 'Rewatch Lesson 3', 'workbench that remembers', 'lairw-l3', 'kGTMBFCdetA'):
        assert bad not in t, (n, bad)
    print('page', n, len(t))
