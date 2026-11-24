# Course 0 · Lesson 4: Owners and permissions
from content_common import *
from deckkit import icon, tiles, bullets
META = dict(n=4, slug='c00l4', label='Course 0 · Lesson 4', module='Users, permissions and sudo',
  title='Owners and Permissions', h1='Owners and permissions',
  yt_title='Linux File Permissions Explained: chmod and chown | Course 0, Lesson 4',
  next_title='sudo, root and staying safe')
SL, slide = mk()
N = []
def s(title, body, narr, **kw): slide(title, body, **kw); N.append(narr)

s('Owners and permissions', '''
<div class="kicker">Course 0 · Users, permissions and sudo · Lesson 4</div>
<h1 class="big">Owners and<br><span class="hl">Permissions</span></h1>
<div class="sub">Read them, change them, and fix "Permission denied".</div>''',
"Every file on Linux belongs to someone, and comes with rules about who can read it, change it or run it. Most permission denied errors you'll ever see come from these rules. Today you learn to read them and change them.", kind='title', ria='hero')

s('Users, groups and root', tiles([
 ('user','User','One account per person'),
 ('group','Group','A team of users'),
 ('crown','root','The administrator: can do anything')], cols=3, size=110),
"Linux is built for many people sharing one machine. Each person has a user account. Users can belong to groups, like a team. And one special user, root, is the administrator, who can do anything. Every file has one owner user and one owner group.")

s('Reading ls -l', '''
<svg viewBox="0 0 1340 470" width="1340" height="470" font-family="Inter">
 <rect x="10" y="40" width="1320" height="120" rx="24" fill="#0B2E2C"/>
 <g font-family="DejaVu Sans Mono,monospace" font-size="50">
  <text x="40" y="118" fill="#F0B95A">-</text><text x="70" y="118" fill="#8FD3CC">rwx</text><text x="180" y="118" fill="#B8E3A0">r-x</text><text x="290" y="118" fill="#F4A58F">r--</text>
  <text x="440" y="118" fill="#DDF0EE">ria</text><text x="570" y="118" fill="#DDF0EE">data</text><text x="730" y="118" fill="#DDF0EE">2048</text><text x="900" y="118" fill="#DDF0EE">train.sh</text></g>
 <g stroke="#0F7C77" stroke-width="4"><path d="M48 160v50M125 160v120M235 160v190M345 160v120M480 160v50M625 160v120M790 160v50M1010 160v120"/></g>
 <g font-size="30" font-weight="700" fill="#0B4F4C" text-anchor="middle">
  <text x="60" y="240">type</text><text x="125" y="315">owner</text><text x="235" y="385">group</text><text x="345" y="315">others</text>
  <text x="480" y="240">owner</text><text x="625" y="315">group</text><text x="790" y="240">size</text><text x="1010" y="315">file name</text></g>
 <text x="670" y="445" text-anchor="middle" font-size="30" fill="#3C5552">first character: - is a file, d is a directory</text>
</svg>''',
"Run ls dash l, and the first column is the permission string. The first character is the type: a dash for a file, d for a directory. Then come three groups of three letters: for the owner, for the group, and for everyone else. After that you see the owner's name, the group's name, the size, and the file name.")

s('r, w and x', table([
 ['<b>r</b> read','see what\'s inside','list its contents'],
 ['<b>w</b> write','change it','add or delete files in it'],
 ['<b>x</b> execute','run it as a program','enter it with cd']], head=['Letter','On a file','On a folder']),
"Each group has three letters. r is read: see what's inside. w is write: change it. x is execute: for a file, run it as a program; for a folder, enter it with cd. A dash means that permission is missing. So r w x, r dash x, r dash dash means: the owner can do everything, the group can read and run, and everyone else can only read.")

s('Changing permissions: chmod', code(['$ chmod u+x train.sh','# owner may now run it','$ chmod g-w notes.txt','# group can no longer change it','$ chmod o-r secrets.txt','# others can no longer read it']),
"chmod changes permissions. Say who: u for the user who owns it, g for group, o for others, a for all. Then plus to add, or minus to remove. Then the letters. chmod u plus x train dot sh lets you run your script. chmod o minus r secrets dot txt stops everyone else from reading it.")

s('The number form', table([
 ['<b>7</b>','rwx','4 + 2 + 1'],
 ['<b>6</b>','rw-','4 + 2'],
 ['<b>5</b>','r-x','4 + 1'],
 ['<b>4</b>','r--','4']], head=['Digit','Means','Read 4 · write 2 · run 1']) +
 '<div class="note"><b>755</b> programs and folders · <b>644</b> normal files · <b>600</b> private keys</div>',
"You'll often see permissions as numbers. Read is four, write is two, execute is one, and you add them up. Seven is read, write and execute; six is read and write; five is read and execute; four is read only. Three digits mean owner, group and others. So seven five five is the usual setting for programs and folders, six four four for normal files, and six hundred for private files, like keys.")

s('The classic error', code(['$ ./train.sh','> Permission denied','$ chmod u+x train.sh','$ ./train.sh','> Training started']) +
 '<div class="note"><b>./</b> means: the file in this folder.</div>',
"Here's the classic case. You write a script, try to run it with dot slash train dot sh, and get permission denied: the file isn't marked as executable yet. chmod u plus x, run it again, and it works. The dot slash just means: the file in this folder.")

s('Changing owners: chown', code(['$ sudo chown ria:data results.csv','# owner ria, group data']) +
 '<div class="note">Giving files away needs the administrator, so chown usually needs <b>sudo</b>: next lesson.</div>',
"chown changes the owner and the group: user, colon, group. Only the administrator can give files away, so chown usually needs sudo, which is next lesson's topic. You'll meet chown when files created by one program have to be used by another.")

s('Why it matters for AI work', bullets([
 'SSH refuses a private key others can read: use <b>600</b>',
 'Shared GPU servers: your data stays yours',
 'Scripts need <b>x</b> before they run',
 'Containers and mounted disks: <b>Permission denied</b> is common']),
"Why does this matter for AI work? SSH refuses to use a private key that others can read, so keys must be six hundred. On a shared GPU server, permissions keep your data and other people's apart. Scripts need the execute bit before they run. And with containers and mounted disks, permission denied is one of the first errors you'll meet. Now you can read it.")

s('Your guided lab', '''
<div class="quote" style="font-size:80px">Prompts and hints,<br><span class="hl">never the full answer.</span></div>
<div class="note">Write a script, watch it fail, fix it with chmod, and practise both forms. Link in the description.</div>''',
"In the lab, you'll create a tiny script, watch it fail with permission denied, fix it with chmod, and practise both the letter form and the number form. Prompts and hints, never the full answer.")

s('Recap and your quiz', recap([
 'Every file: an owner, a group, and r w x for owner, group, others',
 'chmod with letters (u+x) or numbers (755, 644, 600)',
 'chown changes the owner; it usually needs sudo'], META['next_title']),
"Let's recap. Every file has an owner, a group, and three sets of permissions: read, write and execute, for the owner, the group and everyone else. ls dash l shows them; chmod changes them, with letters or with numbers like seven five five and six four four; and chown changes the owner. Next: sudo and root, and how to use that power safely.", kind='recap')

LAB = [
 dict(t="Read a permission string",
  goal="Goal: from ls -l, say what the owner, the group and others may do with the files in /content/sample_data.",
  hints=["Run the long listing on that folder and look at the first column.",
         "Split the string after its first character into three groups of three: owner, group, others."]),
 dict(t="Write a tiny script",
  goal="Goal: a file /content/hello.sh exists, containing one line that prints a greeting.",
  hints=["You can create a file with one line of text using <code>echo</code> and a single greater-than sign.",
         "The line inside the file should itself be an <code>echo</code> command. Put the whole line you want inside single quotes so the shell writes it as it is."]),
 dict(t="Watch it fail",
  goal="Goal: running ./hello.sh from /content gives Permission denied.",
  hints=["Move to <code>/content</code> with <code>%cd</code>, then run the file with dot slash in front of its name.",
         "Check its permissions with the long listing: there's no x anywhere yet."]),
 dict(t="Fix it with letters",
  goal="Goal: the owner may now run hello.sh, and it prints your greeting.",
  hints=["Use <code>chmod</code> with who (the owner), plus, and the letter for execute.",
         "Run the long listing again: an x has appeared in the owner's group. Now run the script."]),
 dict(t="Set it with numbers",
  goal="Goal: hello.sh ends up as rwxr-xr-x, set with three digits.",
  hints=["Work out each group: read 4, write 2, execute 1, then add them up.",
         "Owner can do everything, group and others can read and run. Give chmod the three digits, then check with the long listing."]),
 dict(t="Make a file private",
  goal="Goal: a file secret.txt that only its owner can read and write: rw-------.",
  hints=["Create it with <code>touch</code>, then think in numbers: the owner gets read plus write, the others get nothing.",
         "That's a six for the owner and zeros for the rest. Note: Colab runs you as root, and root can read any file anyway, so you won't see a refusal here. On a real server, you would."]),
]
QUIZ = [
 dict(q="In <code>-rwxr-x---</code>, what can members of the group do?", o=["Everything","Read and run","Read only","Nothing"], a=1,
  why="After the type character, the groups are owner rwx, group r-x, others ---. So the group can read and run."),
 dict(q="What does <code>x</code> mean on a folder?", o=["You can delete it","You can enter it with cd","You can rename it","You can run it as a program"], a=1,
  why="On a directory, execute means you're allowed to go into it."),
 dict(q="Which number means <code>rw-r--r--</code>?", o=["755","644","600","777"], a=1,
  why="rw- is 4+2=6, r-- is 4, r-- is 4: 644, the usual setting for normal files."),
 dict(q="Your script gives Permission denied when you run it. What's the usual fix?", o=["chmod u+x script.sh","rm script.sh","chown root script.sh","mv script.sh /"], a=0,
  why="The file needs the execute permission for you, its owner."),
 dict(q="Why must an SSH private key be set to 600?", o=["To make it faster","SSH refuses keys that other users can read","So everyone can use it","It must be executable"], a=1,
  why="600 means only the owner can read and write it. SSH rejects keys with looser permissions."),
]
FAQ = [
 ("My script says Permission denied when I run it. Why?","It isn't marked as executable yet. Run chmod u+x followed by the script's name, then run it again with ./ in front."),
 ("Why does chmod not stop me reading a file in Colab?","Colab runs you as root, and root can read any file regardless of permissions. On a normal user account, the same settings would block you."),
 ("What does chmod 777 do, and should I use it?","It lets everyone read, change and run the file. It's a common quick fix online, but it's unsafe on shared machines. Give the least permission that works."),
 ("What's the difference between chmod and chown?","chmod changes what people may do with a file. chown changes who owns it."),
 ("Why does running my script need ./ in front?","Linux only looks for commands in certain folders listed in PATH. ./ tells it to run the file in the current folder instead."),
 ("What does the d at the start of ls -l mean?","It marks a directory. A dash marks a normal file, and an l marks a link."),
 ("Can I change permissions on files in Google Drive?","Drive mounted in Colab doesn't follow Linux permissions in the usual way. Practise on files in /content instead."),
 ("What is a group used for?","To share files with a team: give the group read or write access, and everyone in it gets that access."),
 ("How do I see which groups I'm in?","Run groups, or id for more detail."),
 ("What does chmod -R do?","It applies the change to a folder and everything inside it. Use it carefully."),
]
