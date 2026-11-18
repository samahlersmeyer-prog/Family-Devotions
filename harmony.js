// Doxology in four parts: OLD HUNDREDTH in G, the setting from The Lutheran Hymnal (1941)
// as printed at LSB 805 (text and music public domain). The Amen is held as two whole notes.
// One system per line of text; the Amen rides on the last line.
// Note names use "s" for sharp (Fs4 = F-sharp above middle C).
// "A4/G4" means that voice moves A4 then G4 within one syllable (two equal halves, slurred).
const DOX={
 lyrics:[
  ['Praise','God,','from','whom','all','bless-','ings','flow;'],
  ['Praise','Him,','all','crea-','tures','here','be-','low;'],
  ['Praise','Him','a-','bove,','ye','heav’n-','ly','host;'],
  ['Praise','Fa-','ther,','Son,','and','Ho-','ly','Ghost.','A-','men.']],
 beats:[[2,1,1,1,1,2,2,2],[2,1,1,1,1,2,2,2],[2,1,1,1,1,2,2,2],[2,2,2,1,1,2,2,2,4,4]],
 parts:{
 S:['G4 G4 Fs4 E4 D4 G4 A4 B4','B4 B4 B4 A4 G4 C5 B4 A4','G4 A4 B4 A4 G4 E4 Fs4 G4','D5 B4 G4 A4 C5 B4 A4 G4 G4 G4'],
 A:['D4 D4 D4 B3 B3 B3 D4 D4','G4 G4 G4 Fs4 E4 G4 G4 Fs4','E4 D4 D4 D4 D4 C4 D4 D4','Fs4 D4 E4 Fs4 A4 A4/G4 G4/Fs4 D4 E4 D4'],
 T:['B3 B3 A3 G3 Fs3 G3 Fs3 G3','D4 D4 D4 D4 B3 E4 D4 D4','B3 A3 G3 Fs3 G3 G3/A3 A3 B3','A3 G3 B3 D4 E4 D4 D4 B3 C4 B3'],
 B:['G3 G3 D3 E3 B2 E3 D3 G2','G3 G2 B2 D3 E3 C3 G3 D3','E3 Fs3 G3 D3 B2 C3/A2 D3 G3','D3 G3 E3 D3 A2 B2 D3 G2 C3 G2']},
 names:{S:'Soprano',A:'Alto',T:'Tenor',B:'Bass'},
 hint:{S:'the melody',A:'a lower harmony for women and kids',T:'a higher part for men',B:'the lowest part for men'}
};

const DOX_STEP={C:0,D:1,E:2,F:3,G:4,A:5,B:6},DOX_SEMI={C:0,D:2,E:4,F:5,G:7,A:9,B:11};
const doxStep=n=>(+n.slice(-1))*7+DOX_STEP[n[0]];               // diatonic position (C4 = 28)
const doxHz=n=>{const m=12*(+n.slice(-1)+1)+DOX_SEMI[n[0]]+(n[1]==='s'?1:0);return 440*Math.pow(2,(m-69)/12)};
const doxSlots=(v,li)=>DOX.parts[v][li].split(' ').map(x=>x.split('/'));

// ---------- notation ----------
function doxSystem(li){
 const W=360,X0=58,hs=4,T0=30,B0=T0+135,H=B0+72,bt=DOX.beats[li],n=bt.length;
 const P={};for(const v of 'SATB')P[v]=doxSlots(v,li);
 const split=i=>'SATB'.split('').some(v=>P[v][i].length>1);
 const wOf=(b,i)=>split(i)?2:b>=4?1.6:b>=2?1.5:1,tot=bt.reduce((a,b,i)=>a+wOf(b,i),0),unit=(W-14-X0)/tot;
 const yT=d=>T0+(38-d)*hs, yB=d=>B0+(26-d)*hs;                  // treble top line F5, bass top line A3
 let s=`<svg viewBox="0 0 ${W} ${H}" class="dox-sys" role="img" aria-label="Line ${li+1}: ${DOX.lyrics[li].join(' ').replace(/- /g,'')}">`;
 for(const top of [T0,B0])for(let k=0;k<5;k++)s+=`<line class="sl" x1="6" x2="${W-6}" y1="${top+k*8}" y2="${top+k*8}"/>`;
 s+=`<line class="sl" x1="6" x2="6" y1="${T0}" y2="${B0+32}"/><line class="sl" x1="${W-6}" x2="${W-6}" y1="${T0}" y2="${B0+32}"/>`;
 s+=`<text class="clef" x="9" y="${T0+27}">𝄞</text><text class="clef bass" x="10" y="${B0+20}">𝄢</text>`;
 s+=`<text class="acc" x="40" y="${yT(38)+4}">♯</text><text class="acc" x="40" y="${yB(24)+4}">♯</text>`;
 const led=(y,treble,d)=>{const L=[];if(treble){for(let k=28;k>=d;k-=2)L.push(y(k));for(let k=40;k<=d;k+=2)L.push(y(k))}else{for(let k=28;k<=d;k+=2)L.push(y(k));for(let k=16;k>=d;k-=2)L.push(y(k))}return L};
 const note=(x,y,d,treble,b,up,cls)=>{let o='';
   for(const L of led(y,treble,d))o+=`<line class="sl" x1="${x-8}" x2="${x+8}" y1="${L}" y2="${L}"/>`;
   o+=`<ellipse class="nh ${cls}${b>=2?' half':''}" cx="${x}" cy="${y(d)}" rx="4.7" ry="3.4" transform="rotate(-20 ${x} ${y(d)})"/>`;
   if(b<4){const sx=up?x+4.3:x-4.3;o+=`<line class="stem ${cls}" x1="${sx}" x2="${sx}" y1="${y(d)}" y2="${up?y(d)-27:y(d)+27}"/>`}
   return o};
 let cx=X0;
 for(let i=0;i<n;i++){const w=wOf(bt[i],i)*unit,x=cx+Math.min(w*.5,unit*.55),b=bt[i];cx+=w;
   if(li===3&&i===8){const xb=x-unit*.8;s+=`<line class="sl" x1="${xb}" x2="${xb}" y1="${T0}" y2="${B0+32}"/>`}
   for(const [hi,lo,y,treble] of [['S','A',yT,true],['T','B',yB,false]]){
     const H_=P[hi][i],L_=P[lo][i];
     if(H_.length===1&&L_.length===1&&H_[0]===L_[0]){const d=doxStep(H_[0]);   // unison: one head, two stems
       s+=note(x,y,d,treble,b,true,`v-${hi} v-${lo}`)+(b<4?`<line class="stem v-${lo}" x1="${x-4.3}" x2="${x-4.3}" y1="${y(d)}" y2="${y(d)+27}"/>`:'');continue}
     for(const [v,parts,up,other] of [[hi,H_,true,L_],[lo,L_,false,H_]]){
       const nudge=!up&&Math.abs(doxStep(other[0])-doxStep(parts[0]))===1?9:0;   // a second apart: nudge the lower head
       const xs=parts.map((p,k)=>x+nudge+(k?unit*.9:0));
       parts.forEach((p,k)=>{s+=note(xs[k],y,doxStep(p),treble,parts.length>1?b/2:b,up,`v-${v}`)});
       if(parts.length>1){const lowY=Math.max(...parts.map(p=>y(doxStep(p))))+6;
         s+=`<path class="slur v-${v}" d="M${xs[0]-1} ${lowY} Q${(xs[0]+xs[1])/2} ${lowY+6} ${xs[1]+1} ${lowY}"/>`}}}
   const wd=DOX.lyrics[li][i]||'';s+=`<text class="lyr" x="${x}" y="${T0+87}">${wd}</text>`}
 if(li===3)s+=`<line class="sl thick" x1="${W-8.5}" x2="${W-8.5}" y1="${T0}" y2="${B0+32}"/>`;
 return s+'</svg>'}

function doxParts(open,part,soft){
 const btn=v=>`<button type="button" class="btn small vbtn ${part===v?'on':''}" data-a="dox" data-v="${v}" aria-pressed="${part===v}">▶ ${DOX.names[v]}</button>`;
 return `<details class="dox-parts" ${open?'open':''} data-part="${part||''}"><summary>Sing it in four parts</summary>
 <p class="note">Pick your part to hear it loud, with the other three softly underneath. Soprano is ${DOX.hint.S}, alto is ${DOX.hint.A}, tenor is ${DOX.hint.T}, and bass is ${DOX.hint.B}.</p>
 <div class="tune">${['S','A','T','B'].map(btn).join('')}<button type="button" class="btn small vbtn ${part==='all'?'on':''}" data-a="dox" data-v="all" aria-pressed="${part==='all'}">▶ All four</button><button type="button" class="btn small ghost" data-a="doxStop">■ Stop</button></div>
 <label class="dox-soft"><input type="checkbox" id="doxSoft" ${soft?'checked':''}> Play the other parts softly</label>
 <div class="dox-score">${[0,1,2,3].map(doxSystem).join('')}</div>
 <p class="note">The setting from <i>The Lutheran Hymnal</i> (1941), as in LSB 805, with the Amen held longer. Top staff: soprano (stems up) and alto (stems down). Bottom staff: tenor (stems up) and bass (stems down). Kids can sing any part an octave higher.</p></details>`}

// ---------- audio ----------
function doxClip(part,soft,synth){const b=.71,notes=[];let t=.1;
 for(let li=0;li<4;li++){if(li)t+=b*2.5;   // rest between lines
  const bt=DOX.beats[li],P={};for(const v of 'SATB')P[v]=doxSlots(v,li);
  for(let i=0;i<bt.length;i++){if(li===3&&i===8)t+=b*.5;      // a breath before the Amen
   for(const v of 'SATB'){const vol=part==='all'?.24:(v===part?.5:(soft?.08:0));if(!vol)continue;
     const ps=P[v][i],d=b*bt[i]/ps.length;ps.forEach((p,k)=>notes.push([doxHz(p),t+k*d,d-.04,vol]))}
   t+=b*bt[i]}}
 return synth(notes,t+.4)}
