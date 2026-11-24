import re, numpy as np, subprocess
NUM={'1956':'nineteen fifty six','1980s':'nineteen eighties','2010s':'twenty tens'}
SPEC={'ai':2,'x':1,'y':1,'gps':3,'ml':2,'tensorflow':4,'ria':2,"i'm":1,'sql':3,'gpu':3,'vs':2,'duckdb':4,'bigquery':4,'colab':2,'github':2}
def syl_word(w):
    w=w.lower().strip(".,:;!?\"'()")
    if not w: return 0
    if w in SPEC: return SPEC[w]
    if w in NUM: return sum(syl_word(x) for x in NUM[w].split())
    w2=re.sub(r"'s$|'re$|'ll$|'ve$","",w)
    n=len(re.findall(r'[aeiouy]+',w2))
    if w2.endswith('e') and not w2.endswith(('le','ee','ie')) and n>1: n-=1
    if w2.endswith('ed') and not w2.endswith(('ted','ded')) and n>1: n-=1
    return max(1,n)
def syl(text): return sum(syl_word(w) for w in re.split(r'[\s-]+',text))
def envelope_peaks(mp3):
    raw=subprocess.run(['ffmpeg','-v','error','-i',mp3,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
    x=np.frombuffer(raw,np.int16).astype(float)
    fr=np.sqrt(np.convolve(x**2,np.ones(400)/400,'same')[::160])
    e=np.convolve(fr,np.ones(5)/5,'same')
    thr=0.15*np.percentile(e[e>0],90)
    pk=[i for i in range(8,len(e)-8) if e[i]==e[i-8:i+9].max() and e[i]>thr and e[i]-min(e[i-8:i+9])>0.25*e[i]]
    return np.array(pk)*0.01
