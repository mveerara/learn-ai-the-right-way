# Course 0 · Lesson 1: Why Linux runs AI
from content_common import *
from deckkit import icon, tiles, bullets
META = dict(n=1, slug='c00l1', label='Course 0 · Lesson 1', module='Linux and the terminal',
  title='Why Linux Runs AI', h1='Why Linux runs AI',
  yt_title='Why Linux Runs AI | Course 0, Lesson 1 for Complete Beginners',
  next_title='Moving around: files and folders', thumb_l1='Why Linux', thumb_l2='Runs <span class="hl">AI</span>')
SL, slide = mk()
N = []
def s(title, body, narr, **kw): slide(title, body, **kw); N.append(narr)

s('Why Linux runs AI', '''
<div class="kicker">Course 0 · Linux and the terminal · Lesson 1</div>
<h1 class="big">Why Linux<br>Runs <span class="hl">AI</span></h1>
<div class="sub">The ground every AI tool stands on.</div>''',
"Welcome to Course zero, the prep course. Before we train a single model, we learn the ground every AI tool stands on, and it starts with Linux. In this lesson: what Linux is, why almost all AI runs on it, and how to open a Linux terminal in two minutes, for free.", kind='title', ria='hero')

s('What is Linux?', tiles([
 ('terminal','An operating system','Like Windows or macOS'),
 ('free','Free and open','Anyone can use and change it'),
 ('server','Everywhere','Web servers, Android, the cloud')], cols=3, size=110),
"Linux is an operating system, like Windows or macOS: the layer that runs a computer's hardware and its programs. It's free and open source, which means anyone can use it, read its code and change it. You may never have seen it, but you use it every day: it runs most of the web's servers, and Android is built on it.")

s('Where AI actually runs', bullets([
 'Cloud servers that train models',
 'Rented GPU machines',
 'Colab and Kaggle notebooks',
 'Every one of the world\'s <b>500 fastest supercomputers</b>']) + '<div class="note">Underneath, they all run <span class="hl">Linux</span>.</div>',
"Now here's why it matters for AI. When you train a model in the cloud, rent a GPU machine, or run a notebook in Colab, the computer underneath is almost always Linux. For years now, every one of the world's five hundred fastest supercomputers has run Linux. So the instructions you'll meet in tutorials, papers and real jobs are written for Linux.")

s('Why AI chose Linux', tiles([
 ('free','Costs nothing','Run it on a thousand machines'),
 ('server','Built for servers','Works with no screen at all'),
 ('chip','AI tools target it','GPU and AI tools are built for it'),
 ('script','Everything is a command','So it can be scripted and repeated')], cols=2, size=84),
"Why Linux? It costs nothing, so it can run on thousands of machines at once. It was built for servers, so it works well with no screen at all. GPU and AI tools are built and tested for it. And everything in Linux can be done by typing commands, which means it can be written into scripts and repeated exactly.")

s('The terminal: talking in words', code(['# you type a command, press Enter...','$ pwd','> /content','# ...and the computer answers in text']) +
 '<div class="note">Fast, exact, and the same on your laptop, in Colab, or on a GPU server.</div>',
"On a server, there's no mouse and no desktop. You talk to the computer through the terminal: you type a command, press Enter, and it answers in text. It looks old-fashioned, but it's fast and exact, and it works the same on your laptop, in Colab, or on a GPU server on the other side of the world.")

s('Anatomy of a command', '''
<svg viewBox="0 0 1300 430" width="1300" height="430" font-family="Inter">
 <rect x="40" y="40" width="1220" height="150" rx="26" fill="#0B2E2C"/>
 <text x="130" y="140" font-family="DejaVu Sans Mono,monospace" font-size="80" fill="#DDF0EE">ls</text>
 <text x="380" y="140" font-family="DejaVu Sans Mono,monospace" font-size="80" fill="#F0B95A">-l</text>
 <text x="640" y="140" font-family="DejaVu Sans Mono,monospace" font-size="80" fill="#8FD3CC">/content</text>
 <g font-size="40" font-weight="700" fill="#0B4F4C" text-anchor="middle">
  <text x="175" y="290">command</text><text x="430" y="290">option</text><text x="830" y="290">argument</text></g>
 <g font-size="32" fill="#3C5552" text-anchor="middle">
  <text x="175" y="345">the action</text><text x="430" y="345">changes how</text><text x="830" y="345">what to act on</text></g>
 <path d="M175 200v40M430 200v40M830 200v40" stroke="#0F7C77" stroke-width="5"/>
</svg>''',
"Every command has the same shape. First the command itself: the action. Then options, which start with a dash and change how it behaves. Then arguments: what to act on, like a folder or a file. So ls, dash l, slash content means: list, in long form, the folder called content.")

s('Your free Linux machine: Colab', '''
<ol class="steps">
 <li>Open a notebook in <b>Colab</b></li>
 <li>Start a line with <b>!</b> to send it to Linux</li>
 <li>Run <b>!pwd</b> and <b>!whoami</b></li>
</ol>''' + code(['!pwd','> /content']),
"You don't need to install anything. The Colab notebook from Lesson three already runs on a Linux computer. In a code cell, start a line with an exclamation mark, and Colab sends it to Linux instead of Python. Try exclamation pwd, and exclamation whoami.")

s('Your first three commands', '''
<div class="terms">
 <div class="term"><div class="tk">pwd</div><div><b>Where am I?</b> Prints the folder you're in</div></div>
 <div class="term"><div class="tk">ls</div><div><b>What's here?</b> Lists the folder's contents</div></div>
 <div class="term"><div class="tk dl" style="font-size:30px">whoami</div><div><b>Who am I?</b> Shows your user name</div></div>
</div>''',
"Here are your first three. pwd prints the working directory: where you are. ls lists what's in it. And whoami tells you which user you are. In Colab, whoami answers root: the all-powerful administrator. We'll see why that matters in the lesson on sudo.")

s('Linux on your own laptop', bullets([
 '<b>Windows:</b> WSL gives you a real Ubuntu terminal: <b style="white-space:nowrap">wsl --install</b>',
 '<b>Mac:</b> the Terminal app works almost the same',
 '<b>For now:</b> Colab is all you need']),
"Later, you'll want Linux on your own laptop. On Windows, the Windows Subsystem for Linux gives you a real Ubuntu terminal, installed with a single command. A Mac's Terminal is a close cousin of Linux and works almost the same way. But for now, Colab is all you need.")

s('Help is built in', code(['$ ls --help','# a short guide to every option','$ man ls','# the full manual (press q to leave)']) +
 '<div class="note">Nobody memorises everything. <span class="hl">Reading help is the skill.</span></div>',
"You never have to memorise everything. Most commands explain themselves: add dash dash help after a command to see its options. On a full Linux system, man, short for manual, opens the complete guide; press q to leave it. Reading help is a real skill, and every engineer uses it every day.")

s('Your guided lab', '''
<div class="quote" style="font-size:80px">Prompts and hints,<br><span class="hl">never the full answer.</span></div>
<div class="note">Run your first Linux commands in Colab, and find out what kind of machine Google lends you. Link in the description.</div>''',
"Your lab is in the description. You'll open Colab, run your first Linux commands, and find out exactly what kind of machine Google is lending you. Prompts and hints, never the full answer.")

s('Recap and your quiz', recap([
 'Linux runs almost all AI: cloud, GPUs, supercomputers, Colab',
 'Commands: action, options, arguments',
 'pwd, ls, whoami, and --help when stuck'], META['next_title']),
"Let's recap. Linux runs almost all AI computing, from Colab to supercomputers. You talk to it through the terminal, with commands made of an action, options and arguments. And you've met pwd, ls, whoami and dash dash help. Take the quiz in the description, then next time, we learn to move around the file system. See you there.", kind='recap')

LAB = [
 dict(t="Open a notebook and run your first command",
  goal="Goal: a Colab code cell prints the folder you're in.",
  hints=["Open colab.research.google.com and create a new notebook, saved in your workbench/notebooks folder.",
         "In a code cell, a line that starts with <code>!</code> goes to Linux. The command that prints your working directory is three letters: <code>p</code>, <code>w</code>, <code>d</code>."]),
 dict(t="Look around",
  goal="Goal: you see what's inside the folder you're in, first as a plain list, then with details.",
  hints=["The command that lists a folder is two letters, both in the word 'list'.",
         "Add the option for 'long' format after it, with a dash. You should see a folder called <code>sample_data</code>."]),
 dict(t="Find out who you are",
  goal="Goal: Linux tells you which user you're running as.",
  hints=["The command reads like a question: who am I, written as one word.",
         "Colab should answer <code>root</code>. Keep that in mind for the lesson on sudo."]),
 dict(t="Discover your machine",
  goal="Goal: find which Linux distribution Colab runs, and how many processors it has.",
  hints=["Linux keeps a small text file describing itself at <code>/etc/os-release</code>. The command <code>cat</code> prints a file.",
         "For the processor count, the command is short for 'number of processing units': <code>nproc</code>.",
         "Bonus: <code>free -h</code> shows memory and <code>df -h</code> shows disk space, in human-friendly units."]),
 dict(t="Use the built-in help",
  goal="Goal: from the help text alone, find the <code>ls</code> option that shows hidden files, and use it.",
  hints=["Run <code>ls</code> followed by two dashes and the word for asking for assistance.",
         "Look for an option described as not ignoring entries that start with a dot. Run <code>ls</code> with it in <code>/content</code>."]),
]
QUIZ = [
 dict(q="Which operating system runs almost all AI training in the cloud?", o=["Windows","Linux","macOS","Android"], a=1,
  why="Cloud servers, GPU machines, Colab and the world's top supercomputers run Linux."),
 dict(q="In <code>ls -l /content</code>, what is <code>-l</code>?", o=["The command","An option","An argument","A file name"], a=1,
  why="Options start with a dash and change how the command behaves. Here it asks for the long, detailed format."),
 dict(q="In a Colab code cell, how do you send a line to Linux instead of Python?", o=["Start it with #","Start it with !","End it with ;","Write it in capitals"], a=1,
  why="A leading exclamation mark tells Colab to run the line as a shell command."),
 dict(q="Which command tells you the folder you are in?", o=["ls","whoami","pwd","cd"], a=2,
  why="pwd prints the working directory. ls lists its contents, whoami shows your user, cd moves you."),
 dict(q="You don't remember a command's options. What's the quickest built-in help?", o=["Restart the computer","Add --help after the command","Reinstall Linux","Press Ctrl+C"], a=1,
  why="Most commands print a short guide to their options with --help. On a full Linux system, man opens the full manual."),
]
FAQ = [
 ("Do I need to install Linux for this course?","No. Colab already runs on Linux, so you can do every Course 0 lab in your browser. Later, Windows users can add WSL and Mac users can use the Terminal app."),
 ("Is Linux hard to learn?","The basics take a few hours, and you only need a dozen commands to get going. This module teaches exactly those, one lesson at a time."),
 ("What is the difference between Linux and Ubuntu?","Linux is the core of the system. Ubuntu is a distribution: Linux packaged with tools and an installer. Colab runs Ubuntu, and so does WSL by default."),
 ("Why does Colab say I'm root?","Colab gives you a temporary machine all to yourself, so it runs you as the administrator. On real servers you'll be a normal user. The sudo lesson explains why that matters."),
 ("Is the Mac Terminal the same as Linux?","Very close. macOS is a Unix system, so most commands in this course work the same. A few options differ slightly; --help will tell you."),
 ("What is WSL?","Windows Subsystem for Linux: a Microsoft feature that runs a real Linux system inside Windows. You install it by running wsl --install in PowerShell as administrator."),
 ("Why use commands when there's a mouse?","Servers usually have no screen, commands can be saved and repeated exactly, and they're much faster for repetitive work."),
 ("My command says 'command not found'. What now?","Check the spelling and capitals: Linux is case-sensitive, so LS is not ls. If it's spelled right, the program may simply not be installed."),
 ("Does man work in Colab?","Colab's Linux is a trimmed-down version, so the full manuals may be missing. Use --help instead, which works for almost every command."),
]
