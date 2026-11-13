(()=>{
// Family sync: set this to a Firebase web config to turn on the "family PIN" option.
// Families who never set a PIN keep everything on their own device, same as before.
const FB_CONFIG=window.FB_CONFIG||null;
const FB_VER='12.19.0';

const $=s=>document.querySelector(s);
// All the owner's GitHub Pages apps share one localStorage, so new keys get an "fd:" prefix.
// family/log/done keep their original names so existing journals carry over.
const LEGACY=['family','log','done'];const K=k=>LEGACY.includes(k)?k:'fd:'+k;
const ls={get(k){try{return JSON.parse(localStorage.getItem(K(k)))}catch(e){return null}},set(k,v){try{localStorage.setItem(K(k),JSON.stringify(v))}catch(e){}},del(k){try{localStorage.removeItem(K(k))}catch(e){}}};
const clone=o=>JSON.parse(JSON.stringify(o));
const KEYS=['family','log','done','prayers','known','noread','rd'];
const DEF={family:[],log:{},done:{},prayers:{},known:{},noread:[],rd:{}};
let S={};KEYS.forEach(k=>{const v=ls.get(k);S[k]=(v&&typeof v==='object')?v:clone(DEF[k])});
let DAYS=[],byDate={},cur=null,tab='devotion',showAns=false,editFam=false,jFilter='',ansOpen=null,quiz=false,famReturn='devotion';
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const pad=n=>String(n).padStart(2,'0');
const iso=d=>`${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
const parse=s=>{const[y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d)};
const DOW=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const todayISO=iso(new Date());
const uid=()=>Date.now().toString(36)+Math.random().toString(36).slice(2,7);
const short=s=>{const d=parse(s);return `${MON[d.getMonth()]} ${d.getDate()}`};
function fmt(s){const d=parse(s);return `${['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][d.getDay()]}, ${['January','February','March','April','May','June','July','August','September','October','November','December'][d.getMonth()]} ${d.getDate()}`}

// ---------- state + sync ----------
function setPath(o,p,v){let x=o;for(let i=0;i<p.length-1;i++){if(!x[p[i]]||typeof x[p[i]]!=='object'||Array.isArray(x[p[i]]))x[p[i]]={};x=x[p[i]]}
  if(v===null||v===undefined)delete x[p[p.length-1]];else x[p[p.length-1]]=v}
function prune(o,p){for(let n=p.length-1;n>0;n--){let x=o;for(let i=0;i<n-1;i++){x=x&&x[p[i]]}const k=p[n-1];
  if(x&&x[k]&&typeof x[k]==='object'&&!Array.isArray(x[k])&&!Object.keys(x[k]).length)delete x[k];else break}}
function cleanLog(log){for(const d in log){const day=log[d];if(!day||typeof day!=='object'){delete log[d];continue}
  for(const n in day){const e=day[n];if(!e||(!e.h&&!e.l))delete day[n]}if(!Object.keys(day).length)delete log[d]}return log}
function persist(){KEYS.forEach(k=>ls.set(k,S[k]))}
function put(p,v,opt){setPath(S,p,v);prune(S,p);ls.set(p[0],S[p[0]]);sync.write(p,v,opt)}

const sync={pin:ls.get('pinHash'),on:false,status:'off',fs:null,ref:null,timers:{},outbox:ls.get('outbox')||[],
  async load(){if(this.fs)return this.fs;
    const base=`https://www.gstatic.com/firebasejs/${FB_VER}/`;
    const [app,fs]=await Promise.all([import(base+'firebase-app.js'),import(base+'firebase-firestore.js')]);
    const a=app.getApps().length?app.getApp():app.initializeApp(FB_CONFIG);
    this.db=fs.getFirestore(a);this.fs=fs;return fs},
  setStatus(s){this.status=s;updSync()},
  async start(){if(!FB_CONFIG||!this.pin)return;this.setStatus('connecting');
    try{const fs=await this.load();this.ref=fs.doc(this.db,'families',this.pin);
      fs.onSnapshot(this.ref,{includeMetadataChanges:true},snap=>this.onSnap(snap),()=>this.setStatus('error'));
      this.on=true;this.outbox.forEach(x=>this.send(x))}
    catch(e){this.setStatus('offline')}},
  onSnap(snap){if(!snap.exists()){this.send({id:uid(),p:null});return}
    const d=snap.data();const next={};KEYS.forEach(k=>next[k]=d[k]!=null?clone(d[k]):clone(DEF[k]));
    this.outbox.forEach(x=>{if(x.p){setPath(next,x.p,x.v);prune(next,x.p)}});cleanLog(next.log);
    const changed=JSON.stringify(next)!==JSON.stringify(Object.fromEntries(KEYS.map(k=>[k,S[k]])));
    if(changed){S=next;persist();soft()}
    this.setStatus(snap.metadata.hasPendingWrites||this.outbox.length?'saving':(snap.metadata.fromCache?'offline':'synced'))},
  nest(p,v){const o={};let x=o;p.forEach((k,i)=>{if(i===p.length-1)x[k]=v;else x=x[k]={}});return o},
  queue(x){const key=JSON.stringify(x.p);this.outbox=this.outbox.filter(y=>JSON.stringify(y.p)!==key);this.outbox.push(x);ls.set('outbox',this.outbox)},
  write(p,v,opt){if(!this.pin)return;const x={id:uid(),p,v:v??null};this.queue(x);if(!this.on)return;
    const key=JSON.stringify(p);clearTimeout(this.timers[key]);
    if(opt&&opt.slow)this.timers[key]=setTimeout(()=>this.send(x),700);else this.send(x)},
  send(x){if(!this.on||!this.ref)return;const fs=this.fs;
    const data=x.p?this.nest(x.p,x.v==null?fs.deleteField():x.v):Object.fromEntries(KEYS.map(k=>[k,S[k]]));
    fs.setDoc(this.ref,data,{merge:true}).then(()=>{this.outbox=this.outbox.filter(y=>y.id!==x.id);ls.set('outbox',this.outbox);
      if(!this.outbox.length&&this.status==='saving')this.setStatus('synced')}).catch(()=>this.setStatus('error'))},
  async pair(pin){const h=await hashPin(pin);const fs=await this.load();const ref=fs.doc(this.db,'families',h);
    const snap=await fs.getDoc(ref);let merged=Object.fromEntries(KEYS.map(k=>[k,clone(S[k])]));
    if(snap.exists()){const r=snap.data();merged=Object.fromEntries(KEYS.map(k=>[k,union(r[k]!=null?r[k]:clone(DEF[k]),S[k])]))}
    cleanLog(merged.log);await fs.setDoc(ref,merged);S=merged;persist();
    this.pin=h;ls.set('pinHash',h);this.outbox=[];ls.set('outbox',[]);await this.start()},
  unpair(){this.pin=null;this.on=false;ls.del('pinHash');this.outbox=[];ls.set('outbox',[]);location.reload()}
};
function union(a,b){if(Array.isArray(a)||Array.isArray(b))return [...new Set([...(Array.isArray(a)?a:[]),...(Array.isArray(b)?b:[])])];
  if(a&&b&&typeof a==='object'&&typeof b==='object'){const o=clone(a);for(const k in b)o[k]=k in o?union(o[k],b[k]):clone(b[k]);return o}
  return b??a}
async function hashPin(p){const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode('family-devotions:v1:'+p.trim().toLowerCase()));
  return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('')}
let pendingRender=false;
function soft(){if(!DAYS.length)return;const a=document.activeElement;if(a&&a.matches&&a.matches('input,textarea,select')&&$('#main').contains(a)){pendingRender=true;return}render()}
document.addEventListener('focusout',()=>setTimeout(()=>{if(pendingRender){pendingRender=false;soft()}},60));
function updSync(){const b=$('#famBtn');if(!b)return;b.dataset.sync=sync.pin?sync.status:'off';
  const m=$('#syncMsg');if(m)m.textContent=syncLabel()}
function syncLabel(){return {connecting:'Connecting…',synced:'Synced with your family ✓',saving:'Saving…',offline:'Offline. Changes will sync when you’re back online.',error:'Couldn’t reach the sync server. Changes are saved on this phone.'}[sync.status]||''}

// ---------- calendar ----------
const family=()=>S.family;
function monday(s){const d=parse(s);const k=(d.getDay()+6)%7;d.setDate(d.getDate()-k);return d}
function pickStart(){const h=location.hash.slice(1);if(byDate[h])return h;if(byDate[todayISO])return todayISO;
  const future=DAYS.find(d=>d.date>=todayISO);return (future||DAYS[DAYS.length-1]).date}
function renderWeek(){const n=$('#days');n.innerHTML='';const m=monday(cur);
  for(let i=0;i<7;i++){const d=new Date(m);d.setDate(m.getDate()+i);const s=iso(d);const has=!!byDate[s];
    const b=document.createElement('button');b.type='button';b.disabled=!has;
    b.className=(s===todayISO?'is-today ':'')+(S.done[s]?'done':'');b.setAttribute('aria-pressed',s===cur);
    b.innerHTML=`<span class="d">${DOW[d.getDay()]}</span><span class="n">${d.getMonth()+1}/${d.getDate()}</span><span class="check" aria-hidden="true">✓</span>`;
    b.setAttribute('aria-label',`${DOW[d.getDay()]} ${MON[d.getMonth()]} ${d.getDate()}${has?': '+byDate[s].title:''}`);
    b.onclick=()=>go(s);n.appendChild(b)}
  const pm=new Date(m);pm.setDate(m.getDate()-1);const nm=new Date(m);nm.setDate(m.getDate()+7);
  $('#prevWeek').disabled=iso(pm)<DAYS[0].date;$('#nextWeek').disabled=iso(nm)>DAYS[DAYS.length-1].date}
function weekJump(dir){const m=monday(cur);m.setDate(m.getDate()+7*dir);for(let i=0;i<7;i++){const d=new Date(m);d.setDate(m.getDate()+i);if(byDate[iso(d)])return go(iso(d))}}
function go(s){cur=s;if(tab==='kids'||tab==='family')tab='devotion';showAns=false;ansOpen=null;history.replaceState(null,'','#'+s);render();scrollTo(0,0)}

// ---------- church year ----------
function season(s,series){const md=s.slice(5);
  if(/St\. (Stephen|Thomas)|Holy Innocents|Reformation/.test(series))return 'red';
  if(md>='12-24'||md<='01-06')return 'white';
  if(/^All Saints/.test(series))return 'white';
  if(md>='11-29'||/^Advent|St\. Nicholas/.test(series))return 'blue';
  if(md>='10-25'&&md<='10-31')return 'red';
  return 'green'}
const SEASON={green:'Green',blue:'Advent blue',white:'White',red:'Red'};
const weekly=s=>{const w=window.WEEKLY||[];let x=null;for(const e of w)if(e.start<=s)x=e;return x};

// ---------- readers ----------
const readers=()=>S.family.filter(n=>!S.noread.includes(n));
function readerFor(d){if(/^Mom or Dad/.test(d.reader)||!readers().length)return null;
  const r=readers();if(S.rd[d.date]&&r.includes(S.rd[d.date]))return S.rd[d.date];
  const k=Math.round((parse(d.date)-new Date(2026,0,1))/864e5);return r[((k%r.length)+r.length)%r.length]}

// ---------- prayer wording ----------
const andList=a=>a.length<2?(a[0]||''):a.length===2?`${a[0]} and ${a[1]}`:`${a.slice(0,-1).join(', ')}, and ${a[a.length-1]}`;
const items=t=>String(t||'').split(/[,;\n]+/).map(s=>s.trim().replace(/[.!?]+$/,'')).filter(Boolean);
const norm=s=>s.toLowerCase().replace(/\s+/g,' ').trim();
const ARTS=/^(the|a|an|his|her|their|your|our|all)\s/i;
const poss=o=>andList(o.map(esc))+'’s';
function groupItems(day,k){const e=S.log[day]||{};const who=S.family.filter(n=>e[n]&&items(e[n][k]).length);const m=new Map();
  who.forEach(n=>items(e[n][k]).forEach(t=>{const key=norm(t);if(!m.has(key))m.set(key,{t,owners:[]});const o=m.get(key);if(!o.owners.includes(n))o.owners.push(n)}));
  return {list:[...m.values()],who}}
function highsText(day){const {list,who}=groupItems(day,'h');if(!list.length)return '';
  const shared=x=>x.owners.length>=3||(x.owners.length>1&&x.owners.length===who.length);const out=[],groups=new Map();
  list.forEach(x=>{let t=esc(x.t);
    if(/^my\s/i.test(x.t)){out.push({s:(shared(x)?'our ':poss(x.owners)+' ')+t.replace(/^my\s/i,'')});return}
    if(shared(x)){out.push({s:ARTS.test(x.t)?t:'today’s '+t});return}
    if(ARTS.test(x.t)){out.push({s:`${t} for ${andList(x.owners.map(esc))}`});return}
    const key=x.owners.join('|');if(groups.has(key))groups.get(key).items.push(t);else{const g={owners:x.owners,items:[t]};groups.set(key,g);out.push({g})}});
  out.sort((a,b)=>(b.s&&!a.s)-(a.s&&!b.s));
  return 'Thank You for '+andList(out.map(o=>o.g?poss(o.g.owners)+' '+andList(o.g.items):o.s))+'.'}
function lowsText(day){const {list,who}=groupItems(day,'l');if(!list.length)return '';const groups=new Map(),out=[];
  list.forEach(x=>{const t=esc(x.t.replace(/^my\s/i,''));const key=x.owners.join('|');if(groups.has(key))groups.get(key).items.push(t);else{const g={owners:x.owners,items:[t]};groups.set(key,g);out.push(g)}});
  out.sort((a,b)=>b.owners.length-a.owners.length);
  return 'Please help '+andList(out.map(g=>`${g.owners.length>2&&g.owners.length===who.length?'all of us':andList(g.owners.map(esc))} with ${andList(g.items)}`))+'.'}
function activeReqs(day){return Object.entries(S.prayers).filter(([,r])=>r&&r.t&&(r.added||'')<=day&&!(r.ans&&r.ans<day)&&!(r.kind==='thru'&&r.until&&r.until<day)
  )
  .sort((a,b)=>((b[1].kind==='ongoing')-(a[1].kind==='ongoing'))||((a[1].added||'')<(b[1].added||'')?-1:1))}
const reqPhrase=r=>{if(!r.who)return esc(r.t);const its=items(r.t).map(t=>esc(t.replace(/^my\s/i,'')));return ARTS.test(r.t)?`${andList(its)} for ${esc(r.who)}`:`${esc(r.who)}’s ${andList(its)}`};
const reqLabel=r=>r.who?`${esc(r.who)}: ${esc(r.t)}`:esc(r.t);
function reqText(day){const act=activeReqs(day).filter(([,r])=>r.src!==day||r.ans===day);const thanks=act.filter(([,r])=>r.ans===day).map(([,r])=>reqPhrase(r));const asks=act.filter(([,r])=>r.ans!==day).map(([,r])=>reqPhrase(r));
  return [thanks.length?`Thank You for answering our prayer${thanks.length>1?'s':''} for ${andList(thanks)}.`:'',asks.length?`We also pray for ${andList(asks)}.`:''].filter(Boolean).join(' ')}
function hlPrayer(day,print){const h=highsText(day),l=lowsText(day),r=reqText(day);const blank=t=>print?'______':`<span class="blank">${t}</span>`;
  const parts=[h||(S.family.length?`Thank You for ${blank('(today’s highs)')}.`:''),l||(S.family.length?`Please help with ${blank('(today’s lows)')}.`:''),r].filter(Boolean);
  if(!S.family.length&&!r)return `Thank You for ${blank('(the highs)')}. Please help with ${blank('(the lows)')}.`;
  return parts.join(' ')}

// ---------- audio (Doxology: Old Hundredth in G) ----------
let AC=null;
function ac(){if(!AC){try{if(navigator.audioSession)navigator.audioSession.type='playback'}catch(e){}AC=new (window.AudioContext||window.webkitAudioContext)()}
  if(AC.state==='suspended')AC.resume();return AC}
function tone(f,t0,dur,vol){const c=ac(),g=c.createGain(),o=c.createOscillator(),o2=c.createOscillator(),g2=c.createGain();
  o.type='triangle';o2.type='sine';o.frequency.value=f;o2.frequency.value=f*2;g2.gain.value=.12;o2.connect(g2);g2.connect(g);o.connect(g);g.connect(c.destination);
  g.gain.setValueAtTime(0.0001,t0);g.gain.exponentialRampToValueAtTime(vol,t0+.02);g.gain.exponentialRampToValueAtTime(vol*.55,t0+.35);
  g.gain.setValueAtTime(vol*.55,t0+Math.max(.36,dur-.06));g.gain.exponentialRampToValueAtTime(.0001,t0+dur+.35);
  [o,o2].forEach(x=>{x.start(t0);x.stop(t0+dur+.4)})}
const HZ={G3:196,B3:246.94,D4:293.66,E4:329.63,Fs4:369.99,G4:392,A4:440,B4:493.88};
function playNote(){const c=ac(),t=c.currentTime+.05;[HZ.G3,HZ.B3,HZ.D4].forEach(f=>tone(f,t,.9,.09));tone(HZ.G4,t+1.05,1.8,.3)}
function playLine(){const c=ac();let t=c.currentTime+.05;const b=.55;
  [['G4',2],['G4',1],['Fs4',1],['E4',1],['D4',1],['G4',1],['A4',1],['B4',2.5]].forEach(([n,l])=>{tone(HZ[n],t,b*l-.04,.28);t+=b*l})}

// ---------- views ----------
function hymnStep(w){if(!w)return '';const h=w.hymn;return `<section class="step"><h3>Hymn of the week</h3><p class="ref">${esc(h.title)} · ${esc(h.by)}</p><p class="hymn">${h.lines.map(esc).join('<br>')}</p><p class="note">Same hymn all week, so by the end everyone knows it.</p></section>`}
function catStep(w){if(!w)return '';const c=w.cat;return `<section class="step"><h3>Catechism</h3><p class="ref">Small Catechism · ${esc(c.part)}</p><p class="cat-text"><b>${esc(c.text)}</b></p><p class="rub">What does this mean?</p><p>${esc(c.mean)}</p><p class="note">Say it together each night this week.</p></section>`}
function readerLine(d){const r=readerFor(d);
  if(!r)return `<p class="rub">Reader: ${esc(d.reader)}.</p>`;
  return `<p class="rub">Tonight’s reader: <b>${esc(r)}</b>${readers().length>1?` <button type="button" class="link" data-a="swapRd">Switch</button>`:''}</p>`}
function devotion(d){const v=d.verses.map(([n,t])=>`<sup>${n}</sup>${t}`).join(' ');const w=weekly(d.date);
 return `<div class="steps">
 <section class="step"><h3>Invocation</h3><p>In the name of the Father and of the ✠ Son and of the Holy Spirit. Amen.</p><p>Lord Jesus, thank You for bringing us together tonight. Open our ears to hear Your Word. Amen.</p></section>
 ${hymnStep(w)}
 <section class="step"><h3>Scripture</h3><p class="ref">${d.ref} · ESV</p><p class="scripture">${v}</p>${readerLine(d)}</section>
 <section class="step"><h3>${d.story_title}</h3>${d.story.map(p=>`<p>${p}</p>`).join('')}</section>
 <section class="step"><h3>${d.teach_title}</h3><div class="teach">${d.teach.map(p=>`<p>${p}</p>`).join('')}</div></section>
 ${catStep(w)}
 <section class="step"><h3>Questions</h3><ul class="qs">${d.q.map(([w,t])=>`<li><span class="who">${w}</span>${t}</li>`).join('')}</ul></section>
 <section class="step" id="hl"><h3>Highs, lows, and prayers</h3>${hlBlock()}</section>
 <section class="step"><h3>Doxology</h3><div class="tune"><button class="btn small" type="button" data-a="note">♪ Starting note</button><button class="btn small" type="button" data-a="line">▶ First line</button></div><p class="hymn">Praise God, from whom all blessings flow;<br>Praise Him, all creatures here below;<br>Praise Him above, ye heavenly host;<br>Praise Father, Son, and Holy Ghost. Amen.</p><p class="note">Old Hundredth, in G. Turn your volume up.</p></section>
 <section class="step"><h3>Closing prayer</h3><p>${d.prayer} <span id="hlPrayer" class="ins">${hlPrayer(cur)}</span> ${d.ask} Watch over us tonight and let Your holy angels be with us. In Jesus’ name. Amen.</p><p>Pray the Lord’s Prayer together.</p></section>
 </div>`}
function kids(d){const k=d.kids;
 return `<div class="steps">
 <div class="toolbar"><button class="btn" data-a="ans" type="button" aria-pressed="${showAns}">${showAns?'Hide answers':'Show answers'}</button><button class="btn primary" data-a="printKids" type="button">Print kids’ sheet</button></div>
 <section class="step"><h3>Coloring picture</h3><p class="note">${k.lede}</p><div class="pic">${d.pic}</div></section>
 <section class="step"><h3>Fill in the blanks</h3><ol class="blanks">${k.blanks.map((b,i)=>`<li>${b.replace('___',showAns?`<b class="ans">${k.ans[i]}</b>`:'<b>______</b>')}</li>`).join('')}</ol><div class="bank">${k.bank.map(w=>`<span class="chip">${w}</span>`).join('')}</div></section>
 <section class="step"><h3>Word search</h3><p class="note">Tap letters to mark the words you find.</p><div style="overflow-x:auto"><table class="ws" id="ws">${k.grid.map((r,ri)=>'<tr>'+[...r].map((c,ci)=>`<td class="${showAns&&k.cells.includes(ri*10+ci)?'hit':''}">${c}</td>`).join('')+'</tr>').join('')}</table></div><div class="words">${k.words.map(w=>`<span class="chip">${w}</span>`).join('')}</div></section>
 <section class="step"><h3>Circle the answer</h3>${k.quiz.map(([q,o],qi)=>`<p>${q}</p><div class="choice">${o.map((x,xi)=>`<span class="${showAns&&k.qa[qi]===xi?'right':''}">${x}${showAns&&k.qa[qi]===xi?' ✓':''}</span>`).join('')}</div>`).join('')}</section>
 <section class="step"><h3>Draw</h3><p>${k.draw}</p></section>
 <section class="step"><h3>Memory verse</h3><p class="scripture">${k.mv[1]}</p><p class="ref">${k.mv[0]} · ESV</p></section>
 </div>`}
function sheet(d){const k=d.kids;const f='<span class="f"></span>';
 return `<div class="sheet"><div class="top"><h1>${d.title}</h1><div class="name">Name: <span>&nbsp;</span></div></div><p class="lede">${k.lede}</p><div class="p">${d.pic}</div>
 <div class="g"><div class="b"><h2>1. Fill in the blanks</h2><ol>${k.blanks.map(b=>`<li>${b.replace('___',f)}</li>`).join('')}</ol><p><b>Word bank:</b> ${k.bank.join(' · ')}</p></div>
 <div class="b"><h2>2. Word search</h2><table>${k.grid.map(r=>'<tr>'+[...r].map(c=>`<td>${c}</td>`).join('')+'</tr>').join('')}</table><p style="text-align:center;margin:.04in 0 0;font-size:9pt">${k.words.join(' · ')}</p></div>
 <div class="b"><h2>3. Circle the answer</h2>${k.quiz.map(([q,o])=>`<p style="margin:.03in 0">${q}</p><div class="c">${o.map(x=>`<span>${x}</span>`).join('')}</div>`).join('')}</div>
 <div class="b draw"><h2>4. Draw</h2><p style="margin:0">${k.draw}</p></div>
 <div class="b full"><h2>Memory verse · ${k.mv[0]}</h2><p style="margin:0">${k.mv[1]}</p></div></div></div>`}
function devoPrint(d){const w=weekly(d.date);const r=readerFor(d);return `<div class="devo"><h1>${d.title}</h1><p class="r">${fmt(d.date)} · ${d.series}</p>
 <h2>Invocation</h2><p>In the name of the Father and of the ✠ Son and of the Holy Spirit. Amen.</p>
 ${w?`<h2>Hymn: ${esc(w.hymn.title)}</h2><p>${w.hymn.lines.map(esc).join('<br>')}</p>`:''}
 <h2>Scripture: ${d.ref} (ESV)</h2><p>${d.verses.map(([n,t])=>`<sup>${n}</sup>${t}`).join(' ')}</p><p class="r">Reader: ${r?esc(r):d.reader}.</p>
 <h2>${d.story_title}</h2>${d.story.map(p=>`<p>${p}</p>`).join('')}<h2>${d.teach_title}</h2>${d.teach.map(p=>`<p>${p}</p>`).join('')}
 ${w?`<h2>Catechism: ${esc(w.cat.part)}</h2><p><b>${esc(w.cat.text)}</b></p><p><i>What does this mean?</i> ${esc(w.cat.mean)}</p>`:''}
 <h2>Questions</h2>${d.q.map(([w,t])=>`<p><b>${w}:</b> ${t}</p>`).join('')}<h2>Highs and lows · Doxology</h2>
 <h2>Closing prayer</h2><p>${d.prayer} ${hlPrayer(d.date,true)} ${d.ask} Watch over us tonight and let Your holy angels be with us. In Jesus’ name. Amen.</p><p>Pray the Lord’s Prayer together.</p></div>`}
function doPrint(html){$('#printArea').innerHTML=html;window.print()}

function famEditor(){const f=S.family;return `<div class="fam"><p class="note">Who’s joining devotions? Add each person once. Tap 📖 to take someone out of the Scripture-reading rotation.</p>
 <div class="famlist">${f.map((n,i)=>`<span class="chip famchip"><button type="button" class="rdt" data-a="rdToggle" data-i="${i}" aria-pressed="${!S.noread.includes(n)}" aria-label="${esc(n)} reads Scripture">📖</button>${esc(n)} <button type="button" class="x" data-a="rmFam" data-i="${i}" aria-label="Remove ${esc(n)}">×</button></span>`).join('')}</div>
 <form id="famForm" class="famform"><label for="famName" class="sr">Name</label><input id="famName" maxlength="24" placeholder="Name" autocomplete="off"><button class="btn" type="submit">Add</button>${f.length&&tab!=='family'?'<button class="btn" type="button" data-a="famDone">Done</button>':''}</form></div>`}
function hlBlock(){const reqs=activeReqs(cur).filter(([,r])=>r.ans!==cur);
 const reqLine=`<div class="preqs"><p class="note">${reqs.length?`Praying for: ${reqs.map(([,r])=>`<span class="pill">${reqLabel(r)}</span>`).join(' ')}`:'No prayer requests yet.'} <button type="button" class="link" data-a="tab" data-t="prayer">${reqs.length?'Prayer list':'Add one'}</button></p></div>`;
 if(!S.family.length||editFam)return `<p>Everyone shares one high and one low, Mom and Dad included.</p>${famEditor()}${reqLine}`;
 const e=S.log[cur]||{};
 return `<p>Everyone shares a high and a low. Separate a few with commas. They’ll show up in the closing prayer. Tap 🙏 to keep praying for a low on the coming nights.</p><div class="hlrows">${S.family.map((n,i)=>`<div class="hlrow"><span class="who">${esc(n)}</span>
 <label class="sr" for="h${i}">${esc(n)} high</label><input id="h${i}" data-n="${esc(n)}" data-k="h" placeholder="High ☀" value="${esc((e[n]||{}).h||'')}" maxlength="140">
 <div class="lowwrap"><label class="sr" for="l${i}">${esc(n)} low</label><input id="l${i}" data-n="${esc(n)}" data-k="l" placeholder="Low ☁" value="${esc((e[n]||{}).l||'')}" maxlength="140"><button type="button" class="mini" data-a="prayLow" data-i="${i}" aria-label="Add ${esc(n)}’s low to the prayer list" title="Keep praying for this">🙏</button></div></div>`).join('')}</div>
 ${reqLine}<p class="note">${sync.pin?'Synced with your family.':'Saved on this device.'} <button type="button" class="link" data-a="editFam">Edit family</button></p>`}

function nightsPrayed(r){const end=r.ans||todayISO;return Object.keys(S.done).filter(d=>S.done[d]&&d>=(r.added||'')&&d<=end).length}
function prayerTab(){const act=activeReqs(todayISO).filter(([,r])=>!r.ans);
 const answered=Object.entries(S.prayers).filter(([,r])=>r&&r.ans).sort((a,b)=>a[1].ans<b[1].ans?1:-1);
 const past=Object.entries(S.prayers).filter(([,r])=>r&&!r.ans&&r.kind==='thru'&&r.until&&r.until<todayISO).sort((a,b)=>a[1].until<b[1].until?1:-1);
 const who=S.family;
 const meta=r=>[r.by&&r.by!==r.who?`From ${esc(r.by)}`:'',r.kind==='ongoing'?'Ongoing':r.kind==='thru'&&r.until?`Through ${short(r.until)}`:'',`Since ${short(r.added)}`,(()=>{const n=nightsPrayed(r);return n?`Prayed ${n} night${n>1?'s':''}`:''})()].filter(Boolean).join(' · ');
 return `<div class="steps">
 <section class="step"><h3>Add a prayer request</h3>
  <form id="pForm" class="pform"><label for="pText" class="sr">Prayer request</label><input id="pText" maxlength="160" placeholder="What should we pray for?" autocomplete="off" required>
  <div class="prow">${who.length?`<label class="sel"><span>From</span><select id="pBy"><option value="">Everyone</option>${who.map(n=>`<option>${esc(n)}</option>`).join('')}</select></label>`:''}
  <label class="sel"><span>Pray</span><select id="pKind"><option value="until">until it’s answered</option><option value="ongoing">every night (ongoing)</option><option value="thru">through a date</option></select></label>
  <label class="sel" id="pUntilWrap" hidden><span>Through</span><input type="date" id="pUntil" min="${todayISO}"></label></div>
  <button class="btn primary" type="submit">Add to our prayers</button></form>
  <p class="note">Requests show up in the closing prayer every night until you mark them answered.</p></section>
 <section class="step"><h3>We’re praying for</h3>${act.length?`<ul class="plist">${act.map(([id,r])=>`<li class="preq"><div class="ptxt">${reqLabel(r)}</div><div class="note">${meta(r)}</div>
   ${ansOpen===id?`<form class="ansform" data-id="${id}"><label class="sr" for="how">How did God answer?</label><input id="how" maxlength="200" placeholder="How did God answer? (optional)"><div class="prow"><button class="btn primary small" type="submit">Save 🙌</button><button class="btn small" type="button" data-a="ansCancel">Cancel</button></div></form>`
   :`<div class="prow"><button class="btn small" type="button" data-a="ansOpen" data-id="${id}">🙌 Answered</button><button class="btn small ghost" type="button" data-a="pDel" data-id="${id}">Remove</button></div>`}</li>`).join('')}</ul>`:'<p>Nothing on the list yet. Add a request above, or tap 🙏 next to someone’s low.</p>'}</section>
 <section class="step"><h3>Answered prayers</h3>${answered.length?`<ul class="plist">${answered.map(([id,r])=>`<li class="preq done"><div class="ptxt">🙌 ${reqLabel(r)}</div>${r.how?`<p class="how">${esc(r.how)}</p>`:''}<div class="note">Answered ${short(r.ans)}${r.by?` · From ${esc(r.by)}`:''}${(()=>{const n=nightsPrayed(r);return n?` · Prayed ${n} night${n>1?'s':''}`:''})()} · <button type="button" class="link" data-a="unans" data-id="${id}">Undo</button></div></li>`).join('')}</ul>`:'<p>When God answers a prayer, mark it here. Looking back on this list is a great way to remember what He’s done.</p>'}</section>
 ${past.length?`<section class="step"><h3>Finished</h3><ul class="plist">${past.map(([id,r])=>`<li class="preq"><div class="ptxt">${reqLabel(r)}</div><div class="note">Prayed through ${short(r.until)} · <button type="button" class="link" data-a="ansOpen" data-id="${id}">Mark answered</button> · <button type="button" class="link" data-a="pDel" data-id="${id}">Remove</button></div></li>`).join('')}</ul></section>`:''}
 </div>`}

function journal(){const log=S.log;const dates=Object.keys(log).sort().reverse();const names=[...new Set(dates.flatMap(d=>Object.keys(log[d]||{})))];
 const rows=dates.map(dt=>{const ents=Object.entries(log[dt]||{}).filter(([n,x])=>x&&(x.h||x.l)&&(!jFilter||n===jFilter));if(!ents.length)return '';
  return `<section class="step jday"><p class="ref"><button type="button" class="link" data-a="go" data-d="${dt}">${fmt(dt)}${byDate[dt]?' · '+esc(byDate[dt].title):''}</button></p>
  ${ents.map(([n,x])=>`<div class="jent"><span class="who">${esc(n)}</span>${x.h?`<p>☀ ${esc(x.h)}</p>`:''}${x.l?`<p class="${x.ok?'okd':''}">☁ ${esc(x.l)} <label class="ans-ck"><input type="checkbox" data-d="${dt}" data-n="${esc(n)}" ${x.ok?'checked':''}> God answered</label> <button type="button" class="link small" data-a="jPray" data-d="${dt}" data-n="${esc(n)}">🙏 Keep praying</button></p>`:''}</div>`).join('')}</section>`}).join('');
 return `<div class="steps"><div class="toolbar"><span class="note">Highs and lows from every night, newest first.</span></div>
 ${names.length>1?`<div class="bank">${['',...names].map(n=>`<button type="button" class="chip fbtn ${jFilter===n?'on':''}" data-a="jf" data-f="${esc(n)}">${n?esc(n):'Everyone'}</button>`).join('')}</div>`:''}
 ${rows||'<section class="step"><p>No entries yet. Share highs and lows on the Devotion tab, and they’ll collect here for you to look back on.</p></section>'}</div>`}

function verseList(){const max=DAYS.some(d=>d.date<=todayISO)?todayISO:DAYS[0].date;const seen=new Map();
 DAYS.forEach(d=>{if(d.date>max)return;const [r,t]=d.kids.mv;if(!seen.has(r))seen.set(r,{r,t,date:d.date,title:d.title})});return [...seen.values()].reverse()}
function versesTab(){const v=verseList();const n=v.filter(x=>S.known[x.r]).length;
 return `<div class="steps"><div class="toolbar"><span class="note"><b>${n}</b> of ${v.length} memory verses learned</span><button class="btn small ${quiz?'primary':''}" type="button" data-a="quiz" aria-pressed="${quiz}">${quiz?'Show all words':'Quiz me'}</button></div>
 ${quiz?'<p class="note" style="margin:0">Say the verse from memory, then tap the card to check.</p>':''}
 ${v.map(x=>`<section class="step verse ${S.known[x.r]?'known':''}"><p class="ref"><button type="button" class="link" data-a="go" data-d="${x.date}">${esc(x.r)}</button> · ${short(x.date)}</p>
  <p class="scripture vtext ${quiz?'hid':''}" data-a="reveal">${quiz?'<span class="tapme">Tap to check</span>':''}<span class="vt">${esc(x.t)}</span></p>
  <label class="ans-ck"><input type="checkbox" data-known="${esc(x.r)}" ${S.known[x.r]?'checked':''}> We know it</label></section>`).join('')}</div>`}

function famTab(){return `<div class="steps">
 <section class="step"><h3>Family</h3>${famEditor()}</section>
 ${FB_CONFIG?`<section class="step"><h3>Sync between phones</h3>${sync.pin?`<p id="syncMsg" class="syncmsg">${syncLabel()}</p><p class="note">Highs and lows, prayer requests, checkmarks, and memory verses stay in sync on every phone that uses your family PIN.</p><button class="btn small ghost" type="button" data-a="unpair">Stop syncing on this phone</button>`
  :`<p>Set up a family PIN and use it on each parent’s phone so you share one journal and one prayer list.</p>
  <form id="pinForm" class="famform"><label for="pin" class="sr">Family PIN</label><input id="pin" type="password" minlength="6" maxlength="40" placeholder="Family PIN (6+ characters)" autocomplete="off" required><button class="btn primary" type="submit">Connect</button></form>
  <p class="note">Use the same PIN on each phone. A word plus numbers works well (like <i>bluejay2026</i>). Anyone with the PIN can see your journal, so keep it in the family. Other families can make their own PIN, or skip this and keep everything on their phone.</p><p class="note" id="pinMsg"></p>`}</section>`:''}
 <section class="step"><h3>Back up</h3><p class="note">${sync.pin?'Your journal is synced, but you can still save a copy.':'The journal and prayer list live only on this device. Save a backup now and then, or to move them to another phone.'}</p>
 <div class="nav" style="margin:0"><button class="btn" type="button" data-a="backup">Save backup</button><label class="btn" for="rs">Restore backup</label><input type="file" id="rs" accept=".json,application/json" class="sr"></div><p class="note" id="bkMsg"></p></section>
 <p style="text-align:center"><button class="btn" type="button" data-a="tab" data-t="${famReturn}">‹ Back</button></p></div>`}

function render(){const d=byDate[cur];renderWeek();const m=$('#main');const sea=season(d.date,d.series);document.documentElement.dataset.season=sea;
 if(tab==='family'){m.innerHTML=`<div class="hero"><span class="eyebrow">SETTINGS</span><h2>Family &amp; sync</h2></div>${famTab()}`;return}
 const T=[['devotion','Devotion'],['kids','Kids'],['prayer','Prayers'],['journal','Journal'],['verses','Verses']];
 m.innerHTML=`<div class="hero"><span class="eyebrow">${cur===todayISO?'TONIGHT · ':''}${fmt(cur).toUpperCase()}</span><h2>${d.title}</h2>
 <div class="meta"><span class="chip">${d.series}</span><span class="chip">${d.ref}</span><span class="chip sea"><i class="dot ${sea}"></i>${SEASON[sea]}</span></div></div>
 <div class="tabs" role="tablist">${T.map(([k,l])=>`<button class="tab" role="tab" aria-selected="${tab===k}" data-a="tab" data-t="${k}">${l}</button>`).join('')}</div>
 ${tab==='devotion'?devotion(d):tab==='kids'?kids(d):tab==='prayer'?prayerTab():tab==='verses'?versesTab():journal()}
 <div class="nav"><button class="btn" data-a="prev" type="button" ${DAYS.findIndex(x=>x.date===cur)===0?'disabled':''}>‹ Previous</button>
 <button class="btn primary ${S.done[cur]?'is-done':''}" data-a="done" type="button">${S.done[cur]?'Done ✓':'Mark as done'}</button>
 <button class="btn" data-a="next" type="button" ${DAYS.findIndex(x=>x.date===cur)===DAYS.length-1?'disabled':''}>Next ›</button></div>
 ${tab==='devotion'?'<p style="text-align:center"><button class="btn" data-a="printDevo" type="button">Print devotion</button></p>':''}
 <footer>Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), copyright © 2001 by Crossway, a publishing ministry of Good News Publishers. Used by permission. All rights reserved.</footer>`}

let toastT;function toast(t){let el=$('#toast');if(!el){el=document.createElement('div');el.id='toast';el.setAttribute('role','status');document.body.appendChild(el)}
 el.textContent=t;el.classList.add('on');clearTimeout(toastT);toastT=setTimeout(()=>el.classList.remove('on'),2200)}
function addReq(t,by,kind,until,low){t=String(t||'').trim();if(!t)return false;
 const dup=Object.values(S.prayers).some(r=>r&&!r.ans&&norm(r.t)===norm(t)&&(r.who||'')===((low&&low.who)||''));if(dup){toast('That’s already on the prayer list.');return false}
 const r={t,added:cur&&cur<todayISO?cur:todayISO,kind:kind||'until'};if(by)r.by=by;if(kind==='thru'&&until)r.until=until;if(low){r.who=low.who;r.src=low.src}put(['prayers',uid()],r);return true}

// ---------- events ----------
const ACT={
 tab:b=>{const t=b.dataset.t;if(t!=='family')famReturn=t;tab=t;ansOpen=null;render();if(t==='prayer'||t==='family')scrollTo(0,0)},
 go:b=>{tab='devotion';go(b.dataset.d)},
 prev:()=>{const i=DAYS.findIndex(x=>x.date===cur);if(i>0)go(DAYS[i-1].date)},
 next:()=>{const i=DAYS.findIndex(x=>x.date===cur);if(i<DAYS.length-1)go(DAYS[i+1].date)},
 done:()=>{put(['done',cur],S.done[cur]?null:true);render()},
 ans:()=>{showAns=!showAns;render()},
 printKids:()=>doPrint(sheet(byDate[cur])),printDevo:()=>doPrint(devoPrint(byDate[cur])),
 note:()=>playNote(),line:()=>playLine(),
 swapRd:()=>{const r=readers(),c=readerFor(byDate[cur]);put(['rd',cur],r[(r.indexOf(c)+1)%r.length]);render()},
 editFam:()=>{editFam=true;render()},famDone:()=>{editFam=false;render()},
 rmFam:b=>{const f=S.family.slice();f.splice(+b.dataset.i,1);put(['family'],f);render()},
 rdToggle:b=>{const n=S.family[+b.dataset.i];const nr=S.noread.includes(n)?S.noread.filter(x=>x!==n):[...S.noread,n];put(['noread'],nr);render()},
 prayLow:b=>{const n=S.family[+b.dataset.i];const v=((S.log[cur]||{})[n]||{}).l;if(!v){toast(`Type ${n}’s low first.`);return}
   if(addReq(v,n,'until','',{who:n,src:cur})){toast('Added to the prayer list 🙏');const pr=$('#hlPrayer');if(pr)pr.innerHTML=hlPrayer(cur);const box=$('#hl .preqs');if(box)box.outerHTML=hlBlock().match(/<div class="preqs">[\s\S]*?<\/div>/)[0]}},
 jPray:b=>{const x=(S.log[b.dataset.d]||{})[b.dataset.n];if(x&&x.l&&addReq(x.l,b.dataset.n,'until','',{who:b.dataset.n,src:b.dataset.d}))toast('Added to the prayer list 🙏')},
 ansOpen:b=>{ansOpen=b.dataset.id;render();const h=$('#how');if(h)h.focus()},
 ansCancel:()=>{ansOpen=null;render()},
 unans:b=>{put(['prayers',b.dataset.id,'ans'],null);put(['prayers',b.dataset.id,'how'],null);render()},
 pDel:b=>{const r=S.prayers[b.dataset.id];if(r&&confirmDel(r.t)){put(['prayers',b.dataset.id],null);render()}},
 jf:b=>{jFilter=b.dataset.f;render()},
 quiz:()=>{quiz=!quiz;render()},
 reveal:b=>{b.classList.remove('hid')},
 backup:()=>{const blob=new Blob([JSON.stringify(Object.fromEntries(KEYS.map(k=>[k,S[k]])),null,1)],{type:'application/json'});const u=URL.createObjectURL(blob);const a=document.createElement('a');a.href=u;a.download=`devotions-journal-${todayISO}.json`;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),1000);$('#bkMsg').textContent='Backup saved to your downloads.'},
 unpair:()=>sync.unpair()
};
let delArm=null;function confirmDel(t){if(delArm===t){delArm=null;return true}delArm=t;toast('Tap Remove again to delete it.');setTimeout(()=>{if(delArm===t)delArm=null},3000);return false}
const main=$('#main');
main.addEventListener('click',e=>{const ws=e.target.closest('#ws td');if(ws){ws.classList.toggle('on');return}
 const b=e.target.closest('[data-a]');if(b&&ACT[b.dataset.a]){if(b.tagName==='BUTTON')e.preventDefault();ACT[b.dataset.a](b,e)}});
main.addEventListener('input',e=>{const t=e.target;
 if(t.matches('.hlrow input')){const n=t.dataset.n,k=t.dataset.k;put(['log',cur,n,k],t.value||null,{slow:true});const p=$('#hlPrayer');if(p)p.innerHTML=hlPrayer(cur)}});
main.addEventListener('change',e=>{const t=e.target;
 if(t.matches('.ans-ck input[data-d]')){put(['log',t.dataset.d,t.dataset.n,'ok'],t.checked||null);t.closest('p').classList.toggle('okd',t.checked)}
 if(t.matches('[data-known]')){put(['known',t.dataset.known],t.checked||null);t.closest('.verse').classList.toggle('known',t.checked);const v=verseList();const tb=main.querySelector('.toolbar b');if(tb)tb.textContent=v.filter(x=>S.known[x.r]).length}
 if(t.id==='pKind'){$('#pUntilWrap').hidden=t.value!=='thru'}
 if(t.id==='rs'){const f=t.files[0];if(!f)return;f.text().then(x=>{const j=JSON.parse(x);if(!j.log)throw 0;
   KEYS.forEach(k=>{if(j[k]!=null)put([k],union(S[k],j[k]))});render();const m=$('#bkMsg');if(m)m.textContent='Backup restored.'}).catch(()=>{$('#bkMsg').textContent='That file isn’t a journal backup. Pick the .json file you saved.'})}});
main.addEventListener('submit',e=>{const f=e.target;e.preventDefault();
 if(f.id==='famForm'){const v=$('#famName').value.trim();if(v&&!S.family.includes(v))put(['family'],[...S.family,v]);if(tab!=='family')editFam=true;render();const n=$('#famName');if(n)n.focus()}
 if(f.id==='pForm'){const kind=$('#pKind').value,until=$('#pUntil').value;if(kind==='thru'&&!until){toast('Pick a date to pray through.');return}
   if(addReq($('#pText').value,$('#pBy')?$('#pBy').value:'',kind,until)){render();toast('Added to our prayers 🙏')}}
 if(f.classList.contains('ansform')){const id=f.dataset.id;put(['prayers',id,'ans'],todayISO);const how=$('#how').value.trim();if(how)put(['prayers',id,'how'],how);ansOpen=null;render();toast('Praise God! 🙌')}
 if(f.id==='pinForm'){const v=$('#pin').value;const msg=$('#pinMsg');if(v.trim().length<6){msg.textContent='Use at least 6 characters.';return}
   msg.textContent='Connecting…';f.querySelector('button').disabled=true;
   sync.pair(v).then(()=>{render();toast('Synced with your family ✓')}).catch(()=>{msg.textContent='Couldn’t connect. Check your internet and try again.';f.querySelector('button').disabled=false})}});

$('#todayBtn').onclick=()=>{if(tab==='family')tab='devotion';go(byDate[todayISO]?todayISO:pickStart())};
$('#famBtn').onclick=()=>{if(tab==='family'){tab=famReturn;render();return}famReturn=tab;tab='family';render();scrollTo(0,0)};
$('#prevWeek').onclick=()=>weekJump(-1);$('#nextWeek').onclick=()=>weekJump(1);
cleanLog(S.log);updSync();
fetch('days.json').then(r=>r.json()).then(j=>{DAYS=j;DAYS.forEach(d=>byDate[d.date]=d);cur=pickStart();render();sync.start()})
 .catch(()=>{$('#main').innerHTML='<p class="note">Couldn’t load the devotions. Check your connection and refresh.</p>'});
})();
