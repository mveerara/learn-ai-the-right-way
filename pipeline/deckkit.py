# Lesson 1 deck: Mukund's Edvey "AI Introduction" deck, polished into channel style with Ria in the corner.
import json, html as H
defs = open('/home/claude/ria/ria_symbol_defs.txt').read()
char = open('/home/claude/ria/ria_symbol_body.txt').read()

# ---------- tiny icon library (original line drawings) ----------
S = 'fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
IC = {
 'speaker': f'<rect x="34" y="14" width="52" height="92" rx="24" {S}/><circle cx="60" cy="44" r="8" {S}/><path d="M44 78h32" {S}/>',
 'watch':   f'<rect x="34" y="30" width="52" height="60" rx="14" {S}/><path d="M44 30V12h32v18M44 90v18h32V90" {S}/><path d="M44 62h8l5-12 7 22 5-10h7" {S}/>',
 'home':    f'<path d="M16 58 60 20l44 38" {S}/><path d="M28 50v52h64V50" {S}/><circle cx="60" cy="74" r="10" {S}/>',
 'chat':    f'<path d="M18 24h84v54H52l-20 18V78H18z" {S}/><path d="M38 50h4M58 50h4M78 50h4" {S}/>',
 'bank':    f'<path d="M14 44 60 18l46 26z" {S}/><path d="M26 52v38M48 52v38M72 52v38M94 52v38M14 100h92" {S}/>',
 'chart':   f'<path d="M16 100h88M24 84l22-26 18 14 32-40" {S}/><path d="M80 32h16v16" {S}/>',
 'leaf':    f'<path d="M24 96C24 48 52 22 100 20c0 50-28 76-76 76z" {S}/><path d="M24 96 70 50" {S}/>',
 'health':  f'<path d="M48 18h24v30h30v24H72v30H48V72H18V48h30z" {S}/>',
 'car':     f'<path d="M16 78V60l14-24h60l14 24v18z" {S}/><circle cx="36" cy="82" r="10" {S}/><circle cx="84" cy="82" r="10" {S}/>',
 'planet':  f'<circle cx="60" cy="60" r="26" {S}/><ellipse cx="60" cy="60" rx="50" ry="14" transform="rotate(-20 60 60)" {S}/>',
 'board':   f'<rect x="18" y="18" width="84" height="84" rx="6" {S}/><path d="M18 46h84M18 74h84M46 18v84M74 18v84" stroke="currentColor" stroke-width="3" fill="none"/><circle cx="46" cy="46" r="9" fill="currentColor"/><circle cx="74" cy="74" r="9" {S}/>',
 'music':   f'<path d="M46 88V26l50-10v60" {S}/><circle cx="34" cy="88" r="12" {S}/><circle cx="84" cy="78" r="12" {S}/>',
 'ball':    f'<circle cx="60" cy="60" r="40" {S}/><path d="M60 20v80M20 60h80" {S}/><path d="M32 32c14 14 14 42 0 56M88 32c-14 14-14 42 0 56" {S}/>',
 'megaphone': f'<path d="M20 50v20h16l40 24V26L36 50z" {S}/><path d="M90 46c6 8 6 20 0 28" {S}/>',
}
def icon(name, size=120, color='#0F7C77'):
    return f'<svg viewBox="0 0 120 120" width="{size}" height="{size}" style="color:{color}">{IC[name]}</svg>'

def tiles(items, cols=3, size=96):
    cells = ''.join(f'<div class="tile">{icon(i,size)}<div class="tl">{H.escape(t)}</div><div class="ts">{H.escape(s)}</div></div>' for i,t,s in items)
    return f'<div class="tiles" style="grid-template-columns:repeat({cols},1fr)">{cells}</div>'

def bullets(items):
    return '<ul class="bl">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

# ---------- page ----------
css = '''
:root{--teal:#0F7C77;--deep:#0B4F4C;--mint:#DDF0EE;--amber:#E8A33A;--ink:#1D2A2C;--paper:#F6FAF9}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#333;font-family:Inter,sans-serif;color:var(--ink)}
.slide{position:relative;width:1920px;height:1080px;overflow:hidden;background:linear-gradient(180deg,#F6FAF9,#E7F3F1);margin:0 auto 20px}
.hdr{position:absolute;left:0;right:0;top:0;height:74px;background:var(--deep);color:#DDF0EE;display:flex;align-items:center;justify-content:space-between;padding:0 56px;font:600 26px Inter}
.hdr .br b{color:var(--amber)}
.ttl{position:absolute;left:110px;top:120px;right:420px;font:700 68px 'Inter Display',Inter;color:var(--deep);letter-spacing:-.5px}
.ttl:after{content:"";display:block;width:120px;height:8px;border-radius:4px;background:var(--amber);margin-top:22px}
.body{position:absolute;left:110px;top:290px;right:420px;bottom:170px;display:flex;flex-direction:column;justify-content:center}
.capzone{position:absolute;left:0;right:0;bottom:0;height:150px}
.ria{position:absolute;right:40px;bottom:150px;width:340px;height:420px;border-radius:30px;overflow:hidden;background:linear-gradient(180deg,#E7F3F1,#CFE6E2);box-shadow:0 20px 50px rgba(0,0,0,.15);border:5px solid #fff}
.ria .nm{position:absolute;left:0;right:0;bottom:0;background:var(--teal);color:#fff;font:600 24px Inter;text-align:center;padding:8px}
.src{position:absolute;left:110px;bottom:118px;font:400 18px Inter;color:#7A9491}
.bl{list-style:none;font-size:46px;line-height:1.35}
.bl li{position:relative;padding-left:58px;margin:18px 0}
.bl li:before{content:"";position:absolute;left:6px;top:22px;width:22px;height:22px;border-radius:6px;background:var(--teal)}
.tiles{display:grid;gap:30px}
.tile{background:#fff;border-radius:26px;padding:30px 30px 34px;box-shadow:0 14px 40px rgba(11,79,76,.10);display:flex;flex-direction:column;align-items:flex-start;gap:10px}
.tl{font:700 38px Inter;color:var(--deep)}
.ts{font:400 28px Inter;color:#4C6461}
.quote{font:700 92px 'Inter Display',Inter;line-height:1.1;color:var(--deep)}
.hl{color:var(--teal);background:linear-gradient(transparent 62%,rgba(232,163,58,.45) 62%)}
.note{font:400 38px Inter;color:#3C5552;margin-top:40px;line-height:1.4}
.note.c{text-align:center}
.svt{font:700 40px Inter;fill:var(--deep)} .svt.w{fill:#fff}
.svh{font:700 40px Inter;fill:var(--deep)} .svl{font:500 38px Inter;fill:var(--ink)} .svs{font:400 30px Inter;fill:#4C6461}.svs.w{fill:#DDF0EE}
.terms{display:flex;flex-direction:column;gap:26px}
.term{display:flex;gap:34px;align-items:center;background:#fff;border-radius:24px;padding:26px 34px;font-size:36px;line-height:1.35;box-shadow:0 10px 30px rgba(11,79,76,.08)}
.tk{flex:0 0 120px;height:120px;border-radius:24px;background:var(--mint);color:var(--teal);font:800 50px Inter;display:grid;place-items:center;border:5px solid var(--teal)}
.tk.dl{background:var(--teal);color:#fff}
.two{display:flex;gap:60px;align-items:stretch}
.cardx{flex:1;background:#fff;border-radius:28px;padding:44px;font-size:42px;line-height:1.45;border-top:16px solid}
.cardx.bad{border-color:#B4462F}.cardx.good{border-color:#1E8B4C}
.ch{font:800 54px Inter;margin-bottom:18px}
.tb{border-collapse:separate;border-spacing:0;font-size:36px;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 10px 30px rgba(11,79,76,.08)}
.tb th{background:var(--deep);color:#fff;padding:18px 28px;text-align:left}
.tb td{padding:16px 28px;border-top:2px solid #E3ECEA}
.tb .y{background:#FCEFD9}.tb th.y{background:var(--amber);color:var(--ink)}
.tb.wide{width:100%}
.kicker{font:600 34px Inter;color:var(--teal);letter-spacing:.5px;margin-bottom:26px}
.big{font:800 112px 'Inter Display',Inter;line-height:1.02;color:var(--deep)}
.sub{font:400 42px Inter;color:#3C5552;margin-top:34px}
.quiz{margin-top:44px;background:var(--amber);border-radius:22px;padding:24px 34px;font:700 40px Inter;display:inline-block}
.next{margin-top:26px;font-size:36px;color:#3C5552}
.code{font:500 34px 'DejaVu Sans Mono',monospace;background:#0B2E2C;color:#DDF0EE;border-radius:20px;padding:26px 34px;line-height:1.5;white-space:pre}
.code .c{color:#8FCBC3}
.steps{counter-reset:s;list-style:none;font-size:40px;line-height:1.35}
.steps li{counter-increment:s;position:relative;padding-left:84px;margin:20px 0}
.steps li:before{content:counter(s);position:absolute;left:0;top:-2px;width:60px;height:60px;border-radius:16px;background:var(--teal);color:#fff;font:800 34px Inter;display:grid;place-items:center}
'''
def ria_box(kind):
    if kind=='hero':
        return '<svg viewBox="60 120 480 680" style="position:absolute;right:120px;top:130px;width:620px;height:878px"><use href="#ria" x="0" y="0" width="600" height="800"/></svg>'
    return '<div class="ria"><svg viewBox="70 165 460 570" style="width:100%;height:100%"><use href="#ria" x="0" y="0" width="600" height="800"/></svg><div class="nm">Ria</div></div>'

pages=[]

def render(SL, lesson, outdir):
    pages=[]
    for i,s in enumerate(SL,1):
        if s['kind']=='title':
            inner=f'<div class="body" style="top:150px;right:760px">{s["body"]}</div>'
        elif s['kind']=='recap':
            b=s["body"].replace('class="term"','class="term" style="padding:16px 30px"').replace('class="tk','style="flex-basis:96px;height:96px" class="tk')
            inner=f'<div class="ttl">{H.escape(s["title"])}</div><div class="body" style="top:250px;bottom:150px;font-size:.9em">{b}</div>'
        else:
            inner=f'<div class="ttl">{H.escape(s["title"])}</div><div class="body">{s["body"]}</div>'
        pages.append(f'''<section class="slide" id="p{i}"><div class="hdr"><div class="br">Learn AI <b>the Right Way</b></div><div>{lesson if isinstance(lesson,str) else 'Lesson '+str(lesson)} · {i}/{len(SL)}</div></div>
{inner}{ria_box(s.get("ria","corner"))}<div class="capzone"></div></section>''')
    doc=f'''<!doctype html><html><head><meta charset="utf-8"><title>Lesson {lesson} deck</title><style>{css}</style></head><body>
<svg width="0" height="0" style="position:absolute"><defs>{defs}<symbol id="ria" viewBox="0 0 600 800">{char}</symbol></defs></svg>
{''.join(pages)}</body></html>'''
    open(f'{outdir}/deck.html','w').write(doc)
    json.dump([dict(n=i+1,title=s['title']) for i,s in enumerate(SL)],open(f'{outdir}/slides.json','w'),indent=1)
    return len(SL)
