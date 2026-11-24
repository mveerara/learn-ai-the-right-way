# Course 0 · Lesson 5: sudo, root and staying safe
from content_common import *
from deckkit import icon, tiles, bullets
META = dict(n=5, slug='c00l5', label='Course 0 · Lesson 5', module='Users, permissions and sudo',
  title='sudo, root and staying safe', h1='sudo, root and staying safe',
  yt_title='sudo and root in Linux: Use the Power Safely | Course 0, Lesson 5',
  next_title='Git: commit, push and pull')
SL, slide = mk()
N = []
def s(title, body, narr, **kw): slide(title, body, **kw); N.append(narr)

s('sudo, root and staying safe', '''
<div class="kicker">Course 0 · Users, permissions and sudo · Lesson 5</div>
<h1 class="big">sudo, root<br>and Staying<br><span class="hl">Safe</span></h1>
<div class="sub">Borrow the administrator's power, without the accidents.</div>''',
"Root is the user who can do anything on a Linux machine, and sudo is how you borrow that power for one command. You'll type it often when you install GPU drivers and tools. Today: what it does, and how not to hurt yourself with it.", kind='title', ria='hero')

s('root: the administrator', '''
<div class="two">
 <div class="cardx good"><div class="ch">Normal user</div>Works with own files<br>Can't change the system<br><b>Mistakes stay small</b></div>
 <div class="cardx bad"><div class="ch">root</div>Can change anything<br>Can delete the system<br><b>No safety net</b></div>
</div>''',
"A normal user can work with their own files, but can't change the system. That's a safety net: mistakes stay small. Root has no safety net. Root can install anything, change any file, and delete the whole system with one wrong command.")

s('sudo: root for one command', code(['$ apt install htop','> E: ... Permission denied','> ... are you root?','$ sudo apt install htop','> [sudo] password for ria:','# runs as root, then you\'re back to normal']),
"sudo stands for superuser do. Put it in front of a command, and that one command runs as root. Linux asks for your own password, not root's, and only users on an approved list are allowed to use it. Then you're back to normal. That's much safer than logging in as root and staying there.")

s('When to use sudo', '''
<div class="two">
 <div class="cardx good"><div class="ch">Use sudo</div>Installing with <b>apt</b><br>GPU drivers<br>System settings<br>Files owned by root</div>
 <div class="cardx bad"><div class="ch">Don't</div><b>pip</b> in your venv<br>Your own files<br>Python scripts<br><b>git</b></div>
</div>''',
"Use sudo when you change the system: installing packages with apt, installing GPU drivers, changing system settings, or touching files that root owns. Don't use it for your own work: pip installs inside your virtual environment, editing your own files, running your Python scripts, or git. If a command works without sudo, run it without sudo.")

s('Never sudo pip', '''
<div class="two">
 <div class="cardx bad"><div class="ch">Risky</div><span style="font-family:DejaVu Sans Mono,monospace;font-size:34px">sudo pip install pandas</span><br>Changes the system's own Python, which the OS depends on</div>
 <div class="cardx good"><div class="ch">Right</div><span style="font-family:DejaVu Sans Mono,monospace;font-size:34px">source .venv/bin/activate<br>pip install pandas</span><br>Your project, your packages</div>
</div>''',
"One mistake is so common it gets its own slide: sudo pip install. It installs packages into the system's own Python, which the operating system itself depends on, and it can break it. Instead, activate your project's virtual environment and run pip without sudo.")

s('Read before you sudo', bullets([
 'Read the <b>whole</b> command before Enter',
 'Paste only from sources you trust',
 'Be wary of: download a script, pipe it into <b>sudo bash</b>',
 'Check every path twice, especially with <b>rm -r</b>']),
"Because sudo removes the safety net, read the whole command before you press Enter. Only paste commands from sources you trust. Be very wary of anything that downloads a script from the internet and pipes it straight into sudo bash. And check every path twice, especially with rm dash r.")

s('One space, big difference', code(['# deletes one folder','$ rm -r ~/old_project','# deletes your whole home folder, then old_project','$ rm -r ~/ old_project']) +
 '<div class="note c">Linux does exactly what you type, <span class="hl">not what you meant.</span></div>',
"Here's why checking matters. rm dash r, tilde slash old project, deletes one folder. Add a single space after the slash, and the same command deletes your entire home folder, and then anything called old project. Linux does exactly what you type, not what you meant.")

s('Root in Colab', bullets([
 'Colab runs you as <b>root</b>: <b>whoami</b> says so',
 'No sudo needed there',
 'A throwaway machine: a safe place to practise',
 'On servers and laptops, you\'ll be a normal user']),
"Remember that whoami in Colab answered root? Colab gives you a throwaway machine, so it runs you as root, and you don't need sudo there. That makes it a safe place to practise. On real servers and on your own laptop, you'll be a normal user, and sudo is how you ask for more.")

s('Four habits that keep you safe', tiles([
 ('least','Least power','Only sudo when you must'),
 ('read','Read first','Every command, every path'),
 ('script','Virtual environments','For all Python packages'),
 ('backup','Backups','Drive and Git, so mistakes are small')], cols=2, size=84),
"Four habits keep you safe. Use the least power that works. Read before you run. Keep Python packages in virtual environments. And keep your work backed up in Drive and Git, so a mistake is an inconvenience, not a disaster.")

s('Your guided lab', '''
<div class="quote" style="font-size:80px">Prompts and hints,<br><span class="hl">never the full answer.</span></div>
<div class="note">Check who you are, install a small tool with apt, and practise reading commands before running them. Link in the description.</div>''',
"In the lab, you'll check who you are, install a small tool with apt, and practise reading commands before you run them. Prompts and hints, never the full answer.")

s('Recap and your quiz', recap([
 'root can do anything; sudo borrows it for one command',
 'sudo for the system (apt, drivers), never for pip or your own files',
 'Read every command and path before you press Enter'], META['next_title']),
"Let's recap. Root can do anything, and sudo borrows that power for one command. Use it to change the system, not for pip or your own files. Read every command before you run it, and check your paths. Colab runs you as root, so it's your safe practice ground. That completes Linux basics. Next, a new module: Git.", kind='recap')

LAB = [
 dict(t="Check who you are",
  goal="Goal: confirm your user name and your user number in Colab.",
  hints=["One command answers 'who am I'. Another short command, <code>id</code>, shows your user number and groups.",
         "Root always has the user number 0. Compare what you see."]),
 dict(t="Look at a file only root may change",
  goal="Goal: see who owns /etc/hosts and what its permissions are.",
  hints=["Use the long listing on that single file.",
         "Read the owner and the permission string: who may write to it? On a normal account, changing it would need sudo."]),
 dict(t="Install a tool with apt",
  goal="Goal: the tool <code>tree</code> is installed and draws the folders under /content as a tree.",
  hints=["apt first needs an up-to-date list of packages: <code>apt-get update</code>. In Colab you're root, so no sudo is needed.",
         "Then install with <code>apt-get install -y</code> followed by the package name. The -y answers yes for you.",
         "Run the new tool with a folder name after it. On your own laptop, both apt lines would start with sudo."]),
 dict(t="Read before you run",
  goal="Goal: for each command below, say in words what it does, without running it: <code>rm -r ~/ old_project</code> and <code>chmod -R 777 /</code>.",
  hints=["Split each command into command, options and arguments, as in Lesson 1. Count the arguments carefully.",
         "The first has two arguments, so it deletes two things. The second gives everyone full access to every file on the system. Neither is something you'd ever want to run."]),
 dict(t="See where the tool lives",
  goal="Goal: find the full path of the tree program you just installed, and who owns it.",
  hints=["The command <code>which</code>, followed by a program's name, prints where that program lives.",
         "Run the long listing on that path. The owner is root: that's why installing system tools needs sudo on a normal account."]),
]
QUIZ = [
 dict(q="What does <code>sudo</code> do?", o=["Logs you in as root permanently","Runs one command with administrator rights","Speeds up a command","Deletes a user"], a=1,
  why="sudo runs just that one command as root, then you're back to your normal user."),
 dict(q="Which of these normally needs sudo?", o=["pip install inside your virtual environment","Editing your own notebook","apt install on Ubuntu","git commit"], a=2,
  why="apt changes the system, so it needs administrator rights. The others are your own work."),
 dict(q="Why avoid <code>sudo pip install</code>?", o=["pip doesn't work with sudo","It can change the system's own Python and break tools the OS relies on","It's slower","It installs an old version"], a=1,
  why="Use a virtual environment and run pip without sudo."),
 dict(q="What does <code>rm -r ~/ old_project</code> delete?", o=["Only the old_project folder","Your whole home folder, and then old_project","Nothing, it's an error","Only empty folders"], a=1,
  why="The space makes two separate arguments: ~/ (your home folder) and old_project."),
 dict(q="Why don't you need sudo in Colab?", o=["Colab doesn't run Linux","Colab runs you as root","sudo is broken in Colab","Colab asks for your password instead"], a=1,
  why="Colab gives you a throwaway machine and runs you as root, which makes it a safe place to practise."),
]
FAQ = [
 ("What password does sudo ask for?","Your own account password, not root's. Nothing appears on screen while you type it; that's normal."),
 ("Why does sudo say I'm not in the sudoers file?","Your account isn't on the list of users allowed to use sudo. On your own machine, the first user usually is. On shared servers, ask the administrator."),
 ("Should I just log in as root to save time?","No. Working as root all the time removes the safety net for every command. Use sudo for the few commands that need it."),
 ("Is it safe to run sudo commands from tutorials?","Only from sources you trust, and only after reading what each part does. Be especially careful with commands that download and run scripts."),
 ("What is apt?","Ubuntu's package manager: it installs, updates and removes system software. It needs sudo on a normal account."),
 ("What's the difference between apt and pip?","apt installs system software for the whole machine. pip installs Python packages, and belongs inside a virtual environment, without sudo."),
 ("Why is a virtual environment important?","It keeps each project's Python packages separate, so they can't clash with each other or with the system."),
 ("I ran a command with sudo and now my files are owned by root. How do I fix it?","Give them back to yourself with sudo chown, followed by your user name and the file names. Then avoid sudo for that kind of task."),
 ("Is Colab's root dangerous?","Not really. Colab's machine is temporary and is thrown away anyway, so it's a safe place to practise. Your Drive files are the exception: be careful with rm on paths under /content/drive."),
]
