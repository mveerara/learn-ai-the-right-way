# Start Here deck: orientation before Course 0. Ria explains the catalogue, entrance quiz and help.
import sys
sys.path.insert(0, '/home/claude')
import deckkit as K
from deckkit import icon, tiles, bullets
S = K.S
K.IC.update({
 'layers': f'<path d="M60 18 106 42 60 66 14 42z" {S}/><path d="M14 62l46 24 46-24M14 82l46 24 46-24" {S}/>',
 'hand':   f'<path d="M40 104V56a8 8 0 0 1 16 0v-24a8 8 0 0 1 16 0v26a8 8 0 0 1 16 0v8a8 8 0 0 1 16 0v18c0 14-10 26-26 26H58c-10 0-18-8-18-18z" {S}/>',
 'check':  f'<circle cx="60" cy="60" r="44" {S}/><path d="M38 62l16 16 30-34" {S}/>',
})
LABEL = 'Start here'
import re
ARJ = re.sub(r'<svg [^>]*>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="70 140 460 540" width="360" height="420" preserveAspectRatio="xMidYMax slice">', open('/home/claude/arjun/arjun_v2.svg').read(), 1).replace('id="aj','id="aj')
SL = []
def slide(title, body, kind='std', ria='corner'):
    SL.append(dict(title=title, body=body, kind=kind, ria=ria))

slide('Start here', '''
<div class="kicker">Learn AI the Right Way · Before Course 0</div>
<h1 class="big">Start Here:<br>How This<br><span class="hl">Course Works</span></h1>
<div class="sub">The map, the lessons, and your entrance quiz.</div>''', kind='title', ria='hero')

slide('The right way: foundations first', tiles([
 ('layers', 'Foundations first', 'Basics before the exciting part'),
 ('hand', 'Hands on', 'You type every line'),
 ('check', 'Check as you go', 'A quiz after every lesson')], cols=3, size=110))

TR = [('Getting Started', 'Prep course, then your workbench'),
      ('Python for Data', 'Python, charts, statistics'),
      ('Classical Machine Learning', 'Machine learning from zero'),
      ('Neural Networks & Deep Learning', 'Networks, CNNs, sequences'),
      ('Running Real ML Projects', 'Strategy, big data, case studies'),
      ('NLP, LLMs & Generative AI', 'Large language models from zero')]
slide('What you\'ll learn: 13 courses, 6 tracks', '<table class="tb wide" style="font-size:32px">' + ''.join(
 f'<tr><td style="width:60px;color:#0F7C77;font-weight:800">{i}</td><td><b>{a}</b></td><td style="color:#4C6461">{b}</td></tr>'
 for i, (a, b) in enumerate(TR, 1)) + '</table>')

slide('Course 0: the prep course', '''
<div class="two">
 <div class="cardx good"><div class="ch">Video</div>Linux command line<br>File permissions<br>Git<br>The GPU stack<br>Python basics</div>
 <div class="cardx" style="border-color:#E8A33A"><div class="ch">Cheatsheet + quiz</div>Installing software<br>Environments<br>Networks and SSH<br>Containers, cloud</div>
</div>''')

slide('How every lesson works', '''
<ol class="steps">
 <li><b>Watch</b> a short video</li>
 <li><b>Guided lab</b>: prompts and hints, never the full code</li>
 <li><b>Quiz</b>: pass mark 80%</li>
 <li><b>FAQ</b>: answers to the common questions</li>
</ol>''')

slide('Why an entrance quiz?', '''
<div class="code"><span class="c"># A real step from a later lesson</span>
sudo apt install nvidia-driver</div>
<div class="note">If <b>sudo</b> is a mystery, you are stuck before the lesson starts.</div>
<div class="note c" style="margin-top:30px"><span class="hl">Placement, not a filter.</span> It tells you where to start.</div>''')

slide('Where you take it', '''
<ol class="steps">
 <li>Open the <b>course catalogue</b> (link in the description)</li>
 <li>Under <b>Where to start</b>, press <b>Take the entrance quiz</b></li>
 <li>About <b>20 easy questions</b>, 15 minutes, free</li>
</ol>
<div class="note">Learned it elsewhere? Passing is all the proof you need.</div>''')

slide('Two outcomes', '''
<div class="two">
 <div class="cardx good"><div class="ch">Passed</div>80% overall,<br>no weak area<br><b>Register, start Course 1</b></div>
 <div class="cardx" style="border-color:#E8A33A"><div class="ch">Not yet</div>See the modules you missed<br>Take only those in Course 0<br><b>Retake the quiz</b></div>
</div>
<div class="note c">Nobody is turned away.</div>''')

slide('What it costs', bullets([
 'Videos, quizzes, cheatsheets, certificate: <b>free</b>',
 'Optional lab packs for extra practice',
 '<b>Lower prices for students</b>',
 'Every price in the catalogue · 7-day refund']))

slide('Stuck? Ask Arjun', '''
<div class="two" style="align-items:center">
 <div id="arjun" style="flex:0 0 360px;height:420px;background:#fff;border-radius:30px;overflow:hidden;box-shadow:0 14px 40px rgba(11,79,76,.10)">''' + ARJ + '''</div>
 <div style="flex:1">''' + bullets(['Arjun is our <b>FAQ guide</b>', 'Describe the problem in your words', 'He points you to matching FAQ answers', 'Not answered? Ask in the comments']) + '''</div>
</div>''')

slide('Your first step', '''
<style>#p11 .body{top:260px;bottom:auto;justify-content:flex-start}</style>
<div class="terms">
 <div class="term"><div class="tk">1</div><div>Open the course catalogue in the description</div></div>
 <div class="term"><div class="tk">2</div><div>Take the entrance quiz</div></div>
 <div class="term"><div class="tk dl">3</div><div>Passed: register, start Course 1 · Not yet: begin Course 0</div></div>
</div>''', kind='recap')

print(K.render(SL, LABEL, '/home/claude/l00'), 'slides')
