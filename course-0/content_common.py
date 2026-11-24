# Shared icons for Course 0 decks.
import sys; sys.path.insert(0,'/home/claude')
import deckkit as K
S = K.S
K.IC.update({
 'terminal': f'<rect x="12" y="20" width="96" height="80" rx="10" {S}/><path d="M30 46l16 14-16 14M54 76h30" {S}/>',
 'server':   f'<rect x="20" y="16" width="80" height="26" rx="6" {S}/><rect x="20" y="47" width="80" height="26" rx="6" {S}/><rect x="20" y="78" width="80" height="26" rx="6" {S}/><circle cx="36" cy="29" r="3" fill="currentColor"/><circle cx="36" cy="60" r="3" fill="currentColor"/><circle cx="36" cy="91" r="3" fill="currentColor"/>',
 'chip':     f'<rect x="32" y="32" width="56" height="56" rx="6" {S}/><path d="M44 18v14M60 18v14M76 18v14M44 88v14M60 88v14M76 88v14M18 44h14M18 60h14M18 76h14M88 44h14M88 60h14M88 76h14" {S}/>',
 'free':     f'<circle cx="60" cy="60" r="44" {S}/><path d="M42 62l12 12 26-30" {S}/>',
 'script':   f'<path d="M30 14h44l18 18v74H30z" {S}/><path d="M42 50h36M42 66h36M42 82h24" {S}/>',
 'user':     f'<circle cx="60" cy="40" r="20" {S}/><path d="M22 104c4-22 20-34 38-34s34 12 38 34" {S}/>',
 'group':    f'<circle cx="42" cy="44" r="15" {S}/><circle cx="80" cy="44" r="15" {S}/><path d="M14 100c3-18 14-28 28-28s25 10 28 28M52 100c3-18 14-28 28-28s25 10 28 28" {S}/>',
 'crown':    f'<path d="M18 86l8-50 22 24 12-30 12 30 22-24 8 50z" {S}/><path d="M18 100h84" {S}/>',
 'shield':   f'<path d="M60 12l40 16v28c0 28-18 46-40 54-22-8-40-26-40-54V28z" {S}/><path d="M44 60l12 12 22-24" {S}/>',
 'read':     f'<path d="M14 60s18-30 46-30 46 30 46 30-18 30-46 30-46-30-46-30z" {S}/><circle cx="60" cy="60" r="12" {S}/>',
 'backup':   f'<path d="M34 92h56a22 22 0 0 0 0-44 30 30 0 0 0-58-6 20 20 0 0 0 2 50z" {S}/><path d="M60 82V54M48 66l12-12 12 12" {S}/>',
 'least':    f'<path d="M40 54V38a20 20 0 0 1 40 0v16" {S}/><rect x="28" y="54" width="64" height="48" rx="8" {S}/><circle cx="60" cy="78" r="6" fill="currentColor"/>',
})
def mk():
    SL=[]
    def slide(title, body, kind='std', ria='corner'):
        SL.append(dict(title=title, body=body, kind=kind, ria=ria))
    return SL, slide
def code(lines):
    """lines: list of str; '#' starts a comment line, '>' an output line"""
    out=[]
    for l in lines:
        if l.startswith('#'): out.append(f'<span class="c">{l}</span>')
        elif l.startswith('>'): out.append(f'<span class="c">{l[1:].strip()}</span>')
        else: out.append(l)
    return '<div class="code">'+'\n'.join(out)+'</div>'
def table(rows, head=None, fs=36):
    h=''.join(f'<th>{c}</th>' for c in head) if head else ''
    body=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<table class="tb wide" style="font-size:{fs}px">{"<tr>"+h+"</tr>" if h else ""}{body}</table>'
def recap(items, nxt):
    t=''.join(f'<div class="term"><div class="tk{" dl" if i==len(items)-1 else ""}">{i+1}</div><div>{x}</div></div>' for i,x in enumerate(items))
    return f'''<style>#pREC .body{{top:250px;bottom:auto;justify-content:flex-start}}#pREC .terms{{gap:16px}}#pREC .term{{padding:16px 34px}}#pREC .quiz{{margin-top:26px}}#pREC .next{{display:inline-block;margin:0 0 0 34px;vertical-align:middle}}</style>
<div class="terms">{t}</div><div><div class="quiz">5 quick questions · pass mark 80%</div><div class="next">Next: <b>{nxt}</b></div></div>'''
