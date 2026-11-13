import json,random,re,glob,datetime,sys,os,zlib
import os
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,'kit.py')).read())
APP=os.path.join(HERE,'legacy')+'/'
ALL=[]
def grid(words,seed):
    random.seed(seed); N=10
    for attempt in range(200):
        g=[[None]*N for _ in range(N)]; cells=[]; ok=True
        for w in sorted(words,key=len,reverse=True):
            for _ in range(400):
                d=random.choice([(0,1),(1,0)]); r=random.randrange(N-(len(w)-1)*d[0]); c=random.randrange(N-(len(w)-1)*d[1])
                if all(g[r+i*d[0]][c+i*d[1]] in (None,ch) for i,ch in enumerate(w)):
                    for i,ch in enumerate(w): g[r+i*d[0]][c+i*d[1]]=ch; cells.append((r+i*d[0])*N+c+i*d[1])
                    break
            else: ok=False; break
        if ok: break
    assert ok, words
    return sorted(set(cells)),["".join(ch or random.choice("ABCDEFGHIKLMNOPRSTUW") for ch in row) for row in g]
G=("K–2nd","3rd–5th","Older kids")
def D(date,series,title,reader,ref,verses,story_title,story,teach_title,teach,q,prayer,ask,lede,blanks,words,quiz,draw,mv,pic):
    ans=[re.search(r'\[(.+?)\]',b).group(1) for b in blanks]
    bl=[re.sub(r'\[.+?\]','___',b) for b in blanks]
    bank=sorted(ans,key=lambda w:zlib.crc32((w+date).encode()))
    words=[w.upper().replace(' ','') for w in words]
    cells,gr=grid(words,date)
    ALL.append(dict(date=date,series=series,title=title,reader=reader,ref=ref,verses=[[str(a),b] for a,b in verses],story_title=story_title,story=story,
      teach_title=teach_title,teach=teach,q=[[G[i],t] for i,t in enumerate(q)],prayer=prayer,ask=ask,pic=pic,
      kids=dict(lede=lede,blanks=bl,ans=ans,bank=bank,words=words,grid=gr,cells=cells,quiz=[[a,b] for a,b,c in quiz],qa=[c for a,b,c in quiz],draw=draw,mv=list(mv))))
# --- import the two finished weeks ---
READ={"8th grader":"an older kid","3rd grader":"a 3rd–5th grader","5th grader":"a 3rd–5th grader","Mom or Dad, with everyone saying verse 7":"Mom or Dad, with everyone saying verse 7 together",
      "Theo":"a 3rd–5th grader","Junie":"a 3rd–5th grader","Max":"an older kid"}
def old(datafile,picfile,dates,series_fn):
    g={'HERE':APP.rstrip('/')}; exec(open(APP+picfile).read(),g); exec(open(APP+datafile).read(),g)
    ANS=[["storm","monk","Bible","gift","Jesus"],["indulgences","95","door","1517","Jesus"],["emperor","books","pray","stand","fortress"],["castle","George","beard","language","lamp"],["fish","six","Catechism","mean","family"]]
    for i,d in enumerate(g['DAYS']):
        k=d['kids']; a=k.get('ans',ANS[i]); cells,gr=grid(k['words'],dates[i])
        ALL.append(dict(date=dates[i],series=series_fn,title=d['title'],reader=READ.get(d['reader'],d['reader']),ref=d['ref'],verses=[[str(x),y] for x,y in d['verses']],
          story_title=d['story_title'],story=d['story'],teach_title=d['teach_title'],teach=d['teach'],q=[[G[j],t] for j,(_,t) in enumerate(d['q'])],
          prayer=d['prayer'],ask=d['ask'],pic=g['PICS'][i],
          kids=dict(lede=k['lede'],blanks=[b.replace('___','___') for b in k['blanks']],ans=a,bank=k['bank'],words=k['words'],grid=gr,cells=cells,
            quiz=[[q,o] for q,o in k['quiz']],qa=k.get('qa',[1,0]),draw=k['draw'],mv=list(k['mv']))))
try:
    old('data.py','pics.py',["2026-10-19","2026-10-20","2026-10-21","2026-10-22","2026-10-23"],"Reformation Week")
    old('data2.py','pics2.py',["2026-10-26","2026-10-27","2026-10-28","2026-10-29","2026-10-30"],"Alone")
except FileNotFoundError:
    # The legacy sources need files from the original build machine; reuse those finished days from days.json.
    prev=json.load(open(os.path.join(HERE,'..','days.json')))
    ALL.extend(d for d in prev if "2026-10-19"<=d['date']<="2026-10-30")
for f in sorted(glob.glob(os.path.join(HERE,'content','*.py'))): exec(open(f).read())
ALL.sort(key=lambda d:d['date'])
dates=[d['date'] for d in ALL]; assert len(dates)==len(set(dates)), [x for x in dates if dates.count(x)>1]
out=sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,'..')
json.dump(ALL,open(out+'/days.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(ALL),'days',dates[0],'→',dates[-1])
