// Doxology in four parts (Old Hundredth, key of G).
// One system per line of text; the Amen rides on the last line.
// Note names use "s" for sharp (Fs4 = F-sharp above middle C).
const DOX={
 lyrics:[
  ['Praise','God,','from','whom','all','bless-','ings','flow;'],
  ['Praise','Him,','all','crea-','tures','here','be-','low;'],
  ['Praise','Him','a-','bove,','ye','heav’n-','ly','host;'],
  ['Praise','Fa-','ther,','Son,','and','Ho-','ly','Ghost.','A-','men.']],
 parts:{
 S:['G4 G4 Fs4 E4 D4 G4 A4 B4', 'B4 B4 B4 A4 G4 C5 B4 A4', 'G4 A4 B4 A4 G4 E4 Fs4 G4', 'D4 G4 Fs4 E4 D4 G4 A4 G4 G4 G4'],
 A:['D4 E4 D4 C4 D4 B3 D4 D4', 'D4 D4 D4 D4 B3 C4 D4 D4', 'D4 D4 D4 E4 E4 E4 D4 D4', 'D4 B3 D4 B3 D4 B3 D4 B3 C4 B3'],
 T:['B3 B3 B3 G3 G3 G3 Fs3 G3', 'G3 G3 G3 Fs3 G3 G3 G3 Fs3', 'B3 A3 G3 E3 G3 A3 A3 B3', 'G3 G3 A3 G3 G3 G3 Fs3 D3 E3 D3'],
 B:['G3 E3 B2 C3 B2 E3 D3 G2', 'G2 B2 D3 D3 E3 E3 D3 D3', 'G2 Fs2 G2 C3 C3 C3 D3 G3', 'B2 E3 D3 E3 B2 E3 D3 G2 C3 G2']},
 names:{S:'Soprano',A:'Alto',T:'Tenor',B:'Bass'},
 hint:{S:'the melody',A:'a lower harmony for women and kids',T:'a higher part for men',B:'the lowest part for men'}
};

const DOX_STEP={C:0,D:1,E:2,F:3,G:4,A:5,B:6},DOX_SEMI={C:0,D:2,E:4,F:5,G:7,A:9,B:11};
const doxStep=n=>(+n.slice(-1))*7+DOX_STEP[n[0]];               // diatonic position (C4 = 28)
const doxHz=n=>{const m=12*(+n.slice(-1)+1)+DOX_SEMI[n[0]]+(n[1]==='s'?1:0);return 440*Math.pow(2,(m-69)/12)};
const doxLong=(li,i,n)=>i===0||i===n-1||(li===3&&i>=8);      // half notes: first and last of each line, and the Amen

// ---------- notation ----------
function doxSystem(li){
 const W=360,X0=58,hs=4,T0=30,B0=T0+120,H=B0+72;
 const n=DOX.parts.S[li].split(' ').length,sp=(W-14-X0)/n;
 const yT=d=>T0+(38-d)*hs, yB=d=>B0+(26-d)*hs;                  // treble top line F5, bass top line A3
 let s=`<svg viewBox="0 0 ${W} ${H}" class="dox-sys" role="img" aria-label="Line ${li+1}: ${DOX.lyrics[li].join(' ').replace(/- /g,'')}">`;
 for(const top of [T0,B0])for(let k=0;k<5;k++)s+=`<line class="sl" x1="6" x2="${W-6}" y1="${top+k*8}" y2="${top+k*8}"/>`;
 s+=`<line class="sl" x1="6" x2="6" y1="${T0}" y2="${B0+32}"/><line class="sl" x1="${W-6}" x2="${W-6}" y1="${T0}" y2="${B0+32}"/>`;
 if(li===3){const xb=X0+sp*8;s+=`<line class="sl" x1="${xb}" x2="${xb}" y1="${T0}" y2="${B0+32}"/><line class="sl thick" x1="${W-8.5}" x2="${W-8.5}" y1="${T0}" y2="${B0+32}"/>`}
 s+=`<text class="clef" x="9" y="${T0+27}">𝄞</text><text class="clef bass" x="10" y="${B0+20}">𝄢</text>`;
 s+=`<text class="acc" x="40" y="${yT(38)+4}">♯</text><text class="acc" x="40" y="${yB(24)+4}">♯</text>`;
 const head=(x,y,d,long,cls,ledger)=>{let o='';
   for(const L of ledger)o+=`<line class="sl" x1="${x-8}" x2="${x+8}" y1="${L}" y2="${L}"/>`;
   return o+`<ellipse class="nh ${cls}${long?' half':''}" cx="${x}" cy="${y}" rx="4.7" ry="3.4" transform="rotate(-20 ${x} ${y})"/>`};
 const stem=(x,y,up,cls)=>`<line class="stem ${cls}" x1="${up?x+4.3:x-4.3}" x2="${up?x+4.3:x-4.3}" y1="${y}" y2="${up?y-27:y+27}"/>`;
 const P={};for(const v of 'SATB')P[v]=DOX.parts[v][li].split(' ');
 for(let i=0;i<n;i++){const x=X0+sp*(i+.5),long=doxLong(li,i,n);
   // treble: soprano (stem up) + alto (stem down); bass: tenor (stem up) + bass (stem down)
   for(const [hi,lo,y,mid] of [['S','A',yT,28],['T','B',yB,28]]){
     const dh=doxStep(P[hi][i]),dl=doxStep(P[lo][i]);
     const led=d=>{const L=[];if(y===yT){for(let k=28;k>=d;k-=2)L.push(y(k));for(let k=40;k<=d;k+=2)L.push(y(k))}else{for(let k=28;k<=d;k+=2)L.push(y(k));for(let k=16;k>=d;k-=2)L.push(y(k))}return L};
     if(dh===dl)s+=head(x,y(dh),dh,long,`v-${hi} v-${lo}`,led(dh));
     else{s+=head(x,y(dh),dh,long,`v-${hi}`,led(dh));s+=head(x,y(dl),dl,long,`v-${lo}`,led(dl))}
     s+=stem(x,y(dh),true,`v-${hi}`)+stem(x,y(dl),false,`v-${lo}`)}
   const w=DOX.lyrics[li][i]||'';s+=`<text class="lyr" x="${x}" y="${T0+87}">${w}</text>`}
 return s+'</svg>'}

function doxParts(open,part,soft){
 const btn=v=>`<button type="button" class="btn small vbtn ${part===v?'on':''}" data-a="dox" data-v="${v}" aria-pressed="${part===v}">▶ ${DOX.names[v]}</button>`;
 return `<details class="dox-parts" ${open?'open':''} data-part="${part||''}"><summary>Sing it in four parts</summary>
 <p class="note">Pick your part to hear it loud, with the other three softly underneath. Soprano is ${DOX.hint.S}, alto is ${DOX.hint.A}, tenor is ${DOX.hint.T}, and bass is ${DOX.hint.B}.</p>
 <div class="tune">${['S','A','T','B'].map(btn).join('')}<button type="button" class="btn small vbtn ${part==='all'?'on':''}" data-a="dox" data-v="all" aria-pressed="${part==='all'}">▶ All four</button><button type="button" class="btn small ghost" data-a="doxStop">■ Stop</button></div>
 <label class="dox-soft"><input type="checkbox" id="doxSoft" ${soft?'checked':''}> Play the other parts softly</label>
 <div class="dox-score">${[0,1,2,3].map(doxSystem).join('')}</div>
 <p class="note">Top staff: soprano (stems up) and alto (stems down). Bottom staff: tenor (stems up) and bass (stems down). Tenor and bass are written for men’s voices; kids can sing any part an octave higher.</p></details>`}

// ---------- audio ----------
function doxClip(part,soft,synth){const b=.6,notes=[];let t=.1;
 for(let li=0;li<4;li++){const n=DOX.parts.S[li].split(' ').length;
  for(let i=0;i<n;i++){const beats=doxLong(li,i,n)?(li===3&&i===n-1?3:2):1;
   for(const v of 'SATB'){const vol=part==='all'?.24:(v===part?.5:(soft?.08:0));
     if(vol)notes.push([doxHz(DOX.parts[v][li].split(' ')[i]),t,b*beats-.05,vol])}
   t+=b*beats}
  t+=b}                                                      // a breath between lines
 return synth(notes,t+.4)}
