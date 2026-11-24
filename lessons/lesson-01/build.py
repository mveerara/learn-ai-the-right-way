import sys; sys.path.insert(0,'/home/claude')
import deckkit as K
SL=[dict(title='What AI, ML and DL are', body='''
<div class="kicker">Course 1 · Build Your Workbench · Lesson 1</div>
<h1 class="big">What AI, ML and<br>Deep Learning<br><span class="hl">Actually Are</span></h1>
<div class="sub">Three circles, one big picture. For complete beginners.</div>''', kind='title', ria='hero')]
print(K.render(SL, 1, '/home/claude/l01t'))
