# Course 0 · Lesson 2: Moving around: files and folders
from content_common import *
from deckkit import icon, tiles, bullets
META = dict(n=2, slug='c00l2', label='Course 0 · Lesson 2', module='Linux and the terminal',
  title='Moving Around: Files and Folders', h1='Moving around: files and folders',
  yt_title='Moving Around in Linux: Files and Folders | Course 0, Lesson 2',
  next_title='Wildcards, pipes and redirection')
SL, slide = mk()
N = []
def s(title, body, narr, **kw): slide(title, body, **kw); N.append(narr)

s('Moving around', '''
<div class="kicker">Course 0 · Linux and the terminal · Lesson 2</div>
<h1 class="big">Moving Around:<br>Files and<br><span class="hl">Folders</span></h1>
<div class="sub">Find, make, copy, move and delete, without a mouse.</div>''',
"Last time you met the terminal. Today you learn to move around in it: where files live, how to get from one folder to another, and how to make, copy, move and delete things, all without a mouse.", kind='title', ria='hero')

s('One big tree', '''
<svg viewBox="0 0 1300 500" width="1300" height="480" font-family="Inter">
 <rect x="560" y="10" width="180" height="90" rx="20" fill="#0B4F4C"/><text x="650" y="72" text-anchor="middle" font-size="52" font-weight="800" fill="#fff">/</text>
 <g stroke="#0B4F4C" stroke-width="5" fill="none"><path d="M650 100v50M170 150h960M170 150v40M490 150v40M810 150v40M1130 150v40M810 270v50M640 320h340M640 320v30M980 320v30"/></g>
 <g font-size="38" font-weight="700" fill="#0B4F4C" text-anchor="middle">
  <rect x="60" y="190" width="220" height="80" rx="18" fill="#DDF0EE"/><text x="170" y="243">home</text>
  <rect x="380" y="190" width="220" height="80" rx="18" fill="#DDF0EE"/><text x="490" y="243">etc</text>
  <rect x="700" y="190" width="220" height="80" rx="18" fill="#FCEFD9"/><text x="810" y="243">content</text>
  <rect x="1020" y="190" width="220" height="80" rx="18" fill="#DDF0EE"/><text x="1130" y="243">usr</text>
  <rect x="520" y="350" width="240" height="80" rx="18" fill="#FCEFD9"/><text x="640" y="403">drive</text>
  <rect x="840" y="350" width="280" height="80" rx="18" fill="#FCEFD9"/><text x="980" y="403">sample_data</text></g>
 <g font-size="28" fill="#3C5552" text-anchor="middle"><text x="170" y="305">users</text><text x="490" y="305">settings</text><text x="1130" y="305">programs</text></g>
</svg>''',
"Linux keeps everything in one big tree. At the very top is the root folder, written as a single forward slash. Everything else hangs below it: home folders for users, settings in a folder called etc, programs in usr. In Colab, your work sits in slash content.")

s('Paths: the address of a file', '''
<div class="two">
 <div class="cardx good"><div class="ch">Absolute</div>Starts at the root, <b>/</b><br><span style="font-family:DejaVu Sans Mono,monospace;font-size:32px">/content/sample_data/<br>README.md</span><br>Works from anywhere</div>
 <div class="cardx" style="border-color:#E8A33A"><div class="ch">Relative</div>Starts where you are<br><span style="font-family:DejaVu Sans Mono,monospace;font-size:32px">sample_data/<br>README.md</span><br>Shorter to type</div>
</div>''',
"A path is the address of a file. An absolute path starts from the root, with a slash, and works from anywhere. A relative path starts from where you are now. If you're already in slash content, then sample data, slash, README dot md points to the same file.")

s('Three shortcuts', '''
<div class="terms">
 <div class="term"><div class="tk">.</div><div><b>Here:</b> the folder you're in</div></div>
 <div class="term"><div class="tk">..</div><div><b>Up:</b> the folder one level above</div></div>
 <div class="term"><div class="tk dl">~</div><div><b>Home:</b> your own home folder</div></div>
</div>''',
"Three shortcuts save a lot of typing. A single dot means the folder you're in. Two dots mean the folder one level up. And the tilde means your home folder. So cd dot dot moves you up one level, and cd tilde takes you home.")

s('Moving: cd', code(['$ cd /content/sample_data','$ pwd','> /content/sample_data','$ cd ..','$ pwd','> /content']) +
 '<div class="note">In Colab, use <b>%cd</b>: a <b>!cd</b> is forgotten on the next line.</div>',
"cd means change directory. Give it a path, and you're there; check with pwd. One catch in Colab: every line that starts with an exclamation mark runs in a fresh shell, so a cd there is forgotten on the very next line. Use percent cd instead, and Colab remembers where you are.")

s('Looking: ls options', table([
 ['<b>ls -l</b>','details: permissions, owner, size, date'],
 ['<b>ls -a</b>','hidden files too (names starting with a dot)'],
 ['<b>ls -lh</b>','sizes in K, M and G'],
 ['<b>ls -lt</b>','newest first']], head=['Command','Shows']),
"ls has options worth knowing. Dash l gives details: permissions, owner, size and date. Dash a shows hidden files, whose names start with a dot. Dash h, together with l, shows sizes in kilobytes and megabytes. And dash t sorts by time, newest first. You can combine them, like ls dash l h.")

s('Making things', code(['$ mkdir results','$ mkdir -p project/data/raw','# -p: the whole chain at once','$ touch notes.txt','# an empty file']),
"mkdir makes a directory. Add dash p, and it makes a whole chain of folders at once, without complaining if some of them already exist. touch creates an empty file, or updates the time stamp on a file that's already there.")

s('Copy, move, rename', table([
 ['<b>cp a.csv b.csv</b>','copy a file'],
 ['<b>cp -r data backup</b>','copy a whole folder'],
 ['<b>mv a.csv data/</b>','move a file into a folder'],
 ['<b>mv old.csv new.csv</b>','rename a file']], head=['Command','Does']),
"cp copies a file. To copy a whole folder, add dash r, for recursive. mv moves a file. And since renaming is just moving to a new name, mv renames too.")

s('Deleting: there is no bin', '''
<div class="two">
 <div class="cardx bad"><div class="ch">rm</div><b>rm file.csv</b><br>gone for good<br><b>rm -r folder</b><br>gone, with everything inside</div>
 <div class="cardx good"><div class="ch">Stay safe</div><b>ls</b> the same path first<br><b>rm -i</b> asks each time<br>Keep precious work<br>in your Drive workbench</div>
</div>''',
"Now, careful. rm removes a file, and rm dash r removes a folder and everything in it. There is no recycle bin: it's gone. So look before you delete. Run ls on the same path first, use dash i to be asked each time, and keep anything precious in your Drive workbench.")

s('Looking inside files', table([
 ['<b>cat file</b>','print the whole file'],
 ['<b>head -n 5 file</b>','the first 5 lines'],
 ['<b>tail -n 5 file</b>','the last 5 lines'],
 ['<b>wc -l file</b>','count the lines']], head=['Command','Shows']),
"To look inside a file, cat prints the whole thing. For big files, head shows the first lines and tail the last ones; dash n sets how many. And wc dash l counts the lines, which is a quick way to see how many rows a data file has.")

s('Three keys that make you fast', '''
<div class="terms">
 <div class="term"><div class="tk" style="font-size:34px">Tab</div><div><b>Completes</b> file and folder names</div></div>
 <div class="term"><div class="tk">↑</div><div><b>Brings back</b> your last command</div></div>
 <div class="term"><div class="tk dl" style="font-size:30px">Ctrl+C</div><div><b>Stops</b> a command that's running</div></div>
</div>''',
"Three keys make you fast in any terminal. Tab completes file and folder names, so you rarely type them in full. The up arrow brings back your last command. And Control C stops a command that's running, or one that's taking too long.")

s('Your guided lab', '''
<div class="quote" style="font-size:80px">Prompts and hints,<br><span class="hl">never the full answer.</span></div>
<div class="note">Explore Colab's sample data, build a project folder, copy a dataset in and count its rows. Link in the description.</div>''',
"In the lab, you'll explore Colab's sample data, build a project folder, copy a dataset into it and count its rows, all from the terminal. Prompts and hints, never the full answer.")

s('Recap and your quiz', recap([
 'One tree from /; paths are absolute or relative; . .. ~',
 'cd, ls, mkdir, touch, cp, mv; read with cat, head, tail, wc',
 'rm has no bin: look first, keep backups'], META['next_title']),
"Let's recap. Linux is one tree starting at slash, and paths are absolute or relative, with dot, dot dot and tilde as shortcuts. You move with cd, look with ls, make with mkdir and touch, copy and move with cp and mv, and read with cat, head, tail and wc. And rm has no recycle bin, so look first. Next time: wildcards, pipes and redirection, where the terminal gets powerful.", kind='recap')

LAB = [
 dict(t="Go to the sample data",
  goal="Goal: your notebook's current folder is /content/sample_data, and Colab remembers it on the next line.",
  hints=["Remember: in Colab, a <code>!cd</code> is forgotten straight away. Use the version with a percent sign.",
         "Run <code>%cd</code> followed by the absolute path. Then check with <code>!pwd</code> in a new line."]),
 dict(t="List the files with sizes",
  goal="Goal: see every file in sample_data with its size in K or M.",
  hints=["You want the long format, plus human-friendly sizes. Both are single letters after one dash.",
         "Combine <code>l</code> and <code>h</code>. Which file is the biggest?"]),
 dict(t="Build a project folder",
  goal="Goal: /content/project/data/raw exists, made with one command.",
  hints=["The command that makes directories has an option that creates every missing folder in the chain.",
         "That option is <code>-p</code>. Give it the full path to <code>raw</code>."]),
 dict(t="Copy a dataset in",
  goal="Goal: a copy of california_housing_train.csv sits in /content/project/data/raw.",
  hints=["Copying uses a two-letter command: first the source, then the destination.",
         "The source is in <code>/content/sample_data</code>. The destination can be just the folder; the file keeps its name."]),
 dict(t="Peek inside and count rows",
  goal="Goal: you see the first 3 lines of your copy, and you know how many lines it has.",
  hints=["One command shows the start of a file, with an option for how many lines.",
         "Then use the word-count command with the option that counts lines. The first line is the header, so the data rows are one fewer."]),
 dict(t="Rename and tidy up",
  goal="Goal: your copy is renamed to housing.csv, then the whole project folder is removed.",
  hints=["Renaming is moving to a new name in the same folder.",
         "To delete a folder and everything in it, <code>rm</code> needs the recursive option. List the folder first, so you know exactly what goes."]),
]
QUIZ = [
 dict(q="What does the path <code>/content/sample_data</code> start from?", o=["Your current folder","The root of the file tree","Your home folder","Google Drive"], a=1,
  why="A path that starts with / is absolute: it begins at the root of the tree and works from anywhere."),
 dict(q="You're in <code>/content/sample_data</code>. Where does <code>cd ..</code> take you?", o=["/","/content","/content/sample_data/..","Your home folder"], a=1,
  why="Two dots mean one level up, so you move from sample_data to its parent, /content."),
 dict(q="Which command makes <code>project/data/raw</code> in one go, even if <code>project</code> doesn't exist yet?", o=["mkdir project/data/raw","mkdir -p project/data/raw","touch project/data/raw","cd -p project/data/raw"], a=1,
  why="mkdir -p creates every missing folder in the path."),
 dict(q="How do you rename <code>old.csv</code> to <code>new.csv</code>?", o=["rename old.csv new.csv","cp old.csv new.csv","mv old.csv new.csv","rm old.csv new.csv"], a=2,
  why="Renaming is moving to a new name, so mv does it. cp would leave both files."),
 dict(q="True or false: files deleted with <code>rm</code> go to a recycle bin.", o=["True","False"], a=1,
  why="There is no bin in the terminal. rm deletes for good, so look before you delete and keep backups."),
]
FAQ = [
 ("Why doesn't !cd work in Colab?","Each line starting with ! runs in its own short-lived shell, so the change of folder is lost when that line ends. Use %cd, which Colab remembers for the rest of the notebook."),
 ("What's the difference between a folder and a directory?","Nothing: they're two words for the same thing. Linux tradition says directory, which is why the command is cd, change directory."),
 ("Are file names case-sensitive?","Yes. Data.csv and data.csv are two different files on Linux. Stick to lowercase names to avoid surprises."),
 ("Can I use spaces in file names?","You can, but you then have to put the name in quotes every time. Use underscores or dashes instead, like my_data.csv."),
 ("What are hidden files?","Files whose names start with a dot, such as .bashrc. They usually hold settings. ls -a shows them."),
 ("I deleted a file with rm. Can I get it back?","Usually not. That's why your important work lives in your Drive workbench, and later in Git, where earlier versions are kept."),
 ("What's the difference between cp and cp -r?","cp copies files. To copy a folder and everything inside it, you need -r, for recursive."),
 ("Where is my home folder in Colab?","Colab runs you as root, so your home is /root. Your notebook starts in /content, which is where you should work."),
 ("Why count lines with wc -l?","For a CSV file, it tells you the number of rows almost instantly, before you even open Python. Remember the header line."),
]
