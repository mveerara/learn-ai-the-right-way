# Course 0 · Lesson 3: Wildcards, pipes and redirection
from content_common import *
from deckkit import icon, tiles, bullets
META = dict(n=3, slug='c00l3', label='Course 0 · Lesson 3', module='Linux and the terminal',
  title='Wildcards, Pipes and Redirection', h1='Wildcards, pipes and redirection',
  yt_title='Wildcards, Pipes and Redirection in Linux | Course 0, Lesson 3',
  next_title='Owners and permissions')
SL, slide = mk()
N = []
def s(title, body, narr, **kw): slide(title, body, **kw); N.append(narr)

s('Wildcards, pipes and redirection', '''
<div class="kicker">Course 0 · Linux and the terminal · Lesson 3</div>
<h1 class="big">Wildcards,<br>Pipes and<br><span class="hl">Redirection</span></h1>
<div class="sub">Where the terminal becomes a power tool.</div>''',
"So far: one command, one job. Today, commands start working together. Wildcards let one command handle many files. Redirection saves output to a file. And pipes chain commands into a little assembly line. This is where the terminal becomes a power tool.", kind='title', ria='hero')

s('Wildcards: patterns for names', table([
 ['<b>*</b>','any run of characters','<b>*.csv</b>: every CSV file'],
 ['<b>?</b>','exactly one character','<b>data?.csv</b>: data1.csv, dataA.csv'],
 ['<b>[1-3]</b>','one character from a set','<b>day[1-3].csv</b>: day1, day2, day3']], head=['Pattern','Matches','Example'], fs=34),
"A wildcard is a pattern that matches file names. The star matches any run of characters, so star dot csv means every file ending in dot csv. The question mark matches exactly one character. And square brackets match one character from a set, like day one, two or three.")

s('Wildcards in action', code(['$ ls *.csv','$ cp *.csv data/','# copies every CSV at once','$ ls temp_*','$ rm temp_*','# ls first: see exactly what will go']),
"The shell expands the pattern before the command even runs, so any command can use it. ls star dot csv lists them; cp star dot csv data slash copies them all at once. And rm with a wildcard deletes them all at once, so always run ls with the same pattern first, to see exactly what will go.")

s('Every command has three streams', '''
<svg viewBox="0 0 1300 420" width="1300" height="420" font-family="Inter">
 <rect x="470" y="130" width="360" height="160" rx="28" fill="#0B4F4C"/><text x="650" y="225" text-anchor="middle" font-size="46" font-weight="800" fill="#fff">command</text>
 <rect x="20" y="160" width="300" height="100" rx="20" fill="#DDF0EE"/><text x="170" y="222" text-anchor="middle" font-size="36" font-weight="700" fill="#0B4F4C">stdin</text>
 <rect x="980" y="60" width="300" height="100" rx="20" fill="#DFF3E6"/><text x="1130" y="122" text-anchor="middle" font-size="36" font-weight="700" fill="#1E6B3A">stdout</text>
 <rect x="980" y="260" width="300" height="100" rx="20" fill="#FBE6E0"/><text x="1130" y="322" text-anchor="middle" font-size="36" font-weight="700" fill="#9A3A28">stderr</text>
 <g stroke="#0F7C77" stroke-width="6" fill="none"><path d="M320 210h140M830 180h140M830 250l140 60"/></g>
 <g font-size="28" fill="#3C5552" text-anchor="middle"><text x="170" y="300">input</text><text x="1130" y="200">results</text><text x="1130" y="400">errors</text></g>
</svg>''',
"Every command has three streams. Standard input, where it reads from. Standard output, where its normal results go. And standard error, where error messages go. Normally, both outputs land on your screen. Redirection and pipes let you send them somewhere else.")

s('Redirection: output into files', table([
 ['<b>&gt;</b>','write to a file (replaces what was there)'],
 ['<b>&gt;&gt;</b>','append to the end of a file'],
 ['<b>2&gt;</b>','send only the errors to a file'],
 ['<b>&lt;</b>','read input from a file']], head=['Symbol','Does']),
"The greater-than sign sends output into a file instead of the screen. Careful: a single greater-than replaces whatever was in the file. Two of them, greater-than greater-than, add to the end instead. The number two followed by greater-than sends just the error messages. And less-than feeds a file in as input.")

s('Redirection in practice', code(['$ ls -l > listing.txt','$ echo "run 2 done" >> log.txt','$ python train.py 2> errors.txt','# errors kept for later']),
"For example: ls dash l, greater-than, listing dot txt saves the listing. echo, run two done, double greater-than log dot txt adds a line to a log. And python train dot py, two greater-than errors dot txt keeps the errors in their own file, so you can read them later.")

s('Pipes: chain commands', '''
<svg viewBox="0 0 1300 300" width="1300" height="300" font-family="Inter">
 <rect x="20" y="70" width="460" height="130" rx="26" fill="#0B2E2C"/><text x="250" y="152" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-size="44" fill="#DDF0EE">cat data.csv</text>
 <rect x="580" y="90" width="120" height="90" rx="20" fill="#E8A33A"/><text x="640" y="152" text-anchor="middle" font-size="60" font-weight="800" fill="#1D2A2C">|</text>
 <rect x="800" y="70" width="480" height="130" rx="26" fill="#0B2E2C"/><text x="1040" y="152" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-size="44" fill="#DDF0EE">head -n 3</text>
 <g stroke="#0F7C77" stroke-width="6"><path d="M480 135h100M700 135h100"/></g>
 <text x="650" y="270" text-anchor="middle" font-size="32" fill="#3C5552">output of the left becomes input of the right</text>
</svg>''',
"The vertical bar is a pipe. It takes the output of the command on the left and feeds it straight in as the input of the command on the right, with no temporary files. cat data dot csv, pipe, head dash n three shows just the first three lines.")

s('Four friends for pipes', table([
 ['<b>grep word</b>','keep only lines containing the word'],
 ['<b>sort</b>','put lines in order'],
 ['<b>uniq -c</b>','count repeated lines (sort first)'],
 ['<b>wc -l</b>','count the lines']], head=['Tool','Does']),
"Pipes shine with small tools. grep keeps only the lines that contain a word. sort puts lines in order. uniq dash c counts repeated lines, but only when they sit next to each other, so sort first. And wc dash l counts what's left.")

s('One line, one answer', code(['# How many CSV files are in Colab\'s sample data?','$ ls /content/sample_data | grep csv | wc -l','> 4']) +
 '<div class="note">Read it left to right: <b>list</b>, <b>keep the CSV lines</b>, <b>count</b>.</div>',
"Put them together, and one line answers a real question. ls slash content slash sample data, pipe, grep csv, pipe, wc dash l: how many CSV files are in Colab's sample data? Read it left to right: list, keep the CSV lines, count them.")

s('Finding files: find', code(['$ find /content -name "*.csv"','# every CSV, however deep','$ find . -size +10M','# files bigger than 10 MB']),
"One more tool. find searches a whole tree of folders. find slash content dash name, then star dot csv in quotes, lists every CSV file under content, however deep. The quotes stop the shell expanding the star too early. And find dot dash size plus ten M finds files bigger than ten megabytes, which is handy when a disk fills up.")

s('Your guided lab', '''
<div class="quote" style="font-size:80px">Prompts and hints,<br><span class="hl">never the full answer.</span></div>
<div class="note">Count files, save a listing, and answer a question about the MNIST digits with one pipeline. Link in the description.</div>''',
"In the lab, you'll count files with wildcards, save a listing to a file, and answer a question about the MNIST digits dataset with a single pipeline. Prompts and hints, never the full answer.")

s('Recap and your quiz', recap([
 'Wildcards: * any characters, ? one, [ ] one from a set',
 '&gt; saves, &gt;&gt; appends, 2&gt; catches errors',
 'Pipes chain commands: grep, sort, uniq -c, wc -l'], META['next_title']),
"Let's recap. Wildcards match many files with star, question mark and square brackets. Greater-than saves output, double greater-than appends, and two greater-than catches errors. The pipe chains commands, and grep, sort, uniq and wc turn them into answers. Next, a new module: who owns a file, and who's allowed to touch it.", kind='recap')

LAB = [
 dict(t="List only the CSV files",
  goal="Goal: in /content/sample_data, list only the files ending in .csv.",
  hints=["Move there with <code>%cd</code>, then use <code>ls</code> with a pattern.",
         "The star matches any characters, so a pattern of star, dot, csv matches every CSV file."]),
 dict(t="Count them with a pipe",
  goal="Goal: one line prints just the number of CSV files.",
  hints=["Send the output of your listing into a command that counts lines, using the vertical bar.",
         "The counting command is <code>wc</code> with the option for lines."]),
 dict(t="Save a listing to a file",
  goal="Goal: a file called listing.txt in /content holds the detailed listing of sample_data.",
  hints=["Run the long-format listing, then redirect its output with a single greater-than sign.",
         "Check it worked by printing the file with <code>cat</code>."]),
 dict(t="Add a line to a log",
  goal="Goal: log.txt contains two lines, written by two separate commands, and the first line survived.",
  hints=["<code>echo</code> prints text. Redirect it into log.txt.",
         "For the second line, use the redirection that appends instead of replacing. If the first line vanished, you used the wrong one."]),
 dict(t="Count the digits in MNIST",
  goal="Goal: one pipeline shows how many times each digit (0 to 9) appears as a label in mnist_test.csv.",
  hints=["The label is the first column. <code>cut -d, -f1</code> keeps just the first column of a comma-separated file.",
         "Pipe that into <code>sort</code>, then into <code>uniq</code> with the counting option.",
         "If the file has a header line, it shows up as one extra count. Use <code>head -n 2</code> on the file to check."]),
 dict(t="Find every CSV, however deep",
  goal="Goal: list every .csv file anywhere under /content.",
  hints=["The command that searches folders is <code>find</code>, followed by where to start.",
         "Use the option that matches by name, and put the pattern in quotes so the shell doesn't expand the star first."]),
]
QUIZ = [
 dict(q="Which pattern matches <code>day1.csv</code>, <code>day2.csv</code> and <code>day3.csv</code>, but not <code>day4.csv</code>?", o=["day*.csv","day?.csv","day[1-3].csv","*.csv"], a=2,
  why="Square brackets match one character from the set, here 1 to 3. The others would also match day4.csv."),
 dict(q="What does <code>&gt;&gt;</code> do?", o=["Replaces the file's contents","Adds to the end of the file","Sends only errors to the file","Reads the file as input"], a=1,
  why="Double greater-than appends. A single greater-than replaces what was there."),
 dict(q="What does the pipe in <code>ls | wc -l</code> do?", o=["Saves the listing to a file called wc","Feeds the output of ls into wc as its input","Runs both commands at the same time on different files","Deletes the listing"], a=1,
  why="A pipe passes the output of the left command straight into the command on the right."),
 dict(q="Why do you often <code>sort</code> before <code>uniq -c</code>?", o=["uniq only counts repeats that are next to each other","sort makes uniq faster","uniq can't read unsorted files","It isn't needed"], a=0,
  why="uniq compares neighbouring lines, so identical lines must sit together. Sorting puts them together."),
 dict(q="Before running <code>rm temp_*</code>, what's the safe habit?", o=["Add sudo","Run ls temp_* first to see what matches","Restart the terminal","Use rm -r instead"], a=1,
  why="The same pattern with ls shows exactly which files rm would delete. There's no recycle bin."),
]
FAQ = [
 ("Why put the pattern in quotes with find?","Without quotes, the shell may expand the star in your current folder before find ever sees it. Quotes pass the pattern to find unchanged."),
 ("What's the difference between > and >>?","A single > replaces the file's contents. A double >> adds to the end. Use >> for logs."),
 ("Why did my file become empty?","You probably redirected into the same file you were reading, like sort data.txt > data.txt. The shell empties the target before the command runs. Write to a new file instead."),
 ("Where do error messages go?","To standard error, which also shows on your screen. Redirect them with 2> errors.txt to keep them separately."),
 ("Is grep case-sensitive?","Yes. Add -i to ignore case, so grep -i error matches Error and ERROR too."),
 ("How do I see the columns of a CSV quickly?","head -n 1 file.csv shows the header line. cut -d, -f2 keeps just the second column."),
 ("Can a pipe have more than two commands?","Yes, as many as you like. Each command's output feeds the next, read from left to right."),
 ("Do wildcards work in Colab?","Yes, in lines that start with !, because they run in a real Linux shell."),
 ("What does uniq do without sort?","It only merges repeated lines that are next to each other, so the counts come out wrong. Sort first."),
]
