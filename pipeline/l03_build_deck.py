# Lesson 3 deck: Colab + Google Drive (workbench step 1). Original content; facts checked against the Colab FAQ.
import sys
sys.path.insert(0, '/home/claude')
import deckkit as K
from deckkit import icon, tiles, bullets
S = K.S
K.IC.update({
 'browser': f'<rect x="12" y="20" width="96" height="80" rx="10" {S}/><path d="M12 40h96" {S}/><circle cx="26" cy="30" r="3" fill="currentColor"/><circle cx="38" cy="30" r="3" fill="currentColor"/><path d="M40 64h40M40 80h26" {S}/>',
 'code':    f'<path d="M42 34 18 60l24 26M78 34l24 26-24 26M66 26 54 94" {S}/>',
 'folder':  f'<path d="M14 34h34l10 12h48v54H14z" {S}/>',
 'cloud':   f'<path d="M34 92h56a22 22 0 0 0 0-44 30 30 0 0 0-58-6 20 20 0 0 0 2 50z" {S}/>',
 'link':    f'<path d="M50 70l20-20M44 52l-10 10a16 16 0 0 0 22 22l10-10M76 68l10-10a16 16 0 0 0-22-22l-10 10" {S}/>',
 'text':    f'<path d="M24 28h72M24 50h72M24 72h48M24 94h60" {S}/>',
})
SL = []
def slide(title, body, kind='std', ria='corner'):
    SL.append(dict(title=title, body=body, kind=kind, ria=ria))

slide('Colab with Google Drive', '''
<div class="kicker">Course 1 · Build Your Workbench · Lesson 3</div>
<h1 class="big">Step One:<br>Colab with a<br><span class="hl">Memory</span></h1>
<div class="sub">Run Python in your browser. Keep your work for good.</div>''', kind='title', ria='hero')

slide('What is Google Colab?', tiles([
 ('browser', 'In your browser', 'Nothing to install'),
 ('code', 'Runs Python', 'On Google\'s computers'),
 ('cloud', 'Free', 'Just a Google account')], cols=3, size=110))

slide('A notebook is made of cells', '''
<div class="code"><span class="c"># Code cell: press run</span>
print("Hello, workbench!")</div>
<div style="font:500 34px 'DejaVu Sans Mono',monospace;color:#0B4F4C;margin:14px 0 30px 34px">Hello, workbench!</div>
<div class="note" style="margin-top:0">Text cells hold notes. Code, results and the story <span class="hl">sit together</span>.</div>''')

slide('The catch: Colab forgets', '''
<div class="two">
 <div class="cardx bad"><div class="ch">Colab's computer</div>Temporary<br>Taken back when idle,<br>or after long sessions<br><b>Files there vanish</b></div>
 <div class="cardx good"><div class="ch">Google Drive</div>Permanent<br>Yours, backed up<br>Opens anywhere<br><b>Keep work here</b></div>
</div>''')

slide('What we\'ll set up', '''
<ol class="steps">
 <li>A <b>workbench</b> folder in Google Drive</li>
 <li>A <b>notebook</b> saved inside it</li>
 <li>A <b>connection</b> from notebook to Drive</li>
</ol>
<div class="note">Do it once. Every lab starts here.</div>''')

slide('Step 1: the workbench folder', '''
<svg viewBox="0 0 1300 520" width="1300" height="500" font-family="Inter">
 <rect x="390" y="20" width="520" height="110" rx="22" fill="#0B4F4C"/>
 <text x="650" y="90" text-anchor="middle" class="svt w">My Drive / workbench</text>
 <g stroke="#0B4F4C" stroke-width="5" fill="none"><path d="M650 130v70M200 200h900M200 200v60M650 200v60M1100 200v60"/></g>
 <rect x="40" y="260" width="320" height="200" rx="22" fill="#DDF0EE" stroke="#0F7C77" stroke-width="5"/>
 <text x="200" y="345" text-anchor="middle" class="svt">data</text><text x="200" y="395" text-anchor="middle" class="svs">datasets</text>
 <rect x="490" y="260" width="320" height="200" rx="22" fill="#DDF0EE" stroke="#0F7C77" stroke-width="5"/>
 <text x="650" y="345" text-anchor="middle" class="svt">notebooks</text><text x="650" y="395" text-anchor="middle" class="svs">your work</text>
 <rect x="940" y="260" width="320" height="200" rx="22" fill="#FCEFD9" stroke="#C98722" stroke-width="5"/>
 <text x="1100" y="345" text-anchor="middle" class="svt">outputs</text><text x="1100" y="395" text-anchor="middle" class="svs">charts, results</text>
</svg>''')

slide('Step 2: a notebook', '''
<ol class="steps">
 <li>Go to <b>colab.research.google.com</b></li>
 <li><b>New notebook</b>, then rename it: <i>lesson3_setup</i></li>
 <li><b>File → Move</b> into <i>workbench/notebooks</i></li>
</ol>
<div class="note">Colab saves to your Drive as you work.</div>''')

slide('Step 3: connect to Drive', '''
<div class="two" style="align-items:center">
 <div style="flex:1">''' + icon('link', 170) + '''</div>
 <div style="flex:3">''' + bullets(['Colab has a built-in command: <b>drive.mount</b>', 'Google asks your permission: <b>allow</b>', 'Your Drive appears as a folder', 'The lab shows you where to find it']) + '''</div>
</div>''')

slide('Test: does it remember?', '''
<ol class="steps">
 <li>Write a line of text to <i>outputs/hello.txt</i></li>
 <li><b>Runtime → Disconnect and delete runtime</b></li>
 <li>Reconnect, mount Drive, <b>read it back</b></li>
</ol>
<div class="note c">Still there? <span class="hl">Your workbench remembers.</span></div>''')

slide('About the free GPU', bullets([
 '<b>Runtime → Change runtime type</b> can offer a GPU',
 'Not needed yet: early labs run fine without it',
 'Free GPU time is <b>limited and changes</b>',
 'We switch it on when deep learning arrives']))

slide('Good habits from day one', tiles([
 ('text', 'Clear names', 'lesson3_setup, not Untitled7'),
 ('folder', 'Right folder', 'data in, outputs out'),
 ('code', 'Setup cell on top', 'Rerun everything after a restart'),
 ('cloud', 'Disconnected?', 'Reconnect, rerun, carry on')], cols=2, size=84))

slide('Your guided lab', '''
<div class="quote" style="font-size:80px">Prompts and hints,<br><span class="hl">never the full code.</span></div>
<div class="note">Try each step, peek at a hint only when stuck, tick it off when it works. Link in the description.</div>''')

slide('Recap and your quiz', '''
<div class="terms">
 <div class="term"><div class="tk">1</div><div>Colab runs Python free in your browser; its computer is temporary</div></div>
 <div class="term"><div class="tk">2</div><div>Keep work in Drive: workbench / data, notebooks, outputs</div></div>
 <div class="term"><div class="tk dl">3</div><div>Connect with drive.mount; test by save, restart, read back</div></div>
</div>
<div class="quiz">5 quick questions · pass mark 80% · link in the description</div>
<div class="next" style="margin-top:14px">Next: <b>Python on your own laptop</b></div>''', kind='recap')

print(K.render(SL, 3, '/home/claude/l03'), 'slides')
