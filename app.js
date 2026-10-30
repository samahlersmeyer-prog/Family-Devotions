(()=>{
const $=s=>document.querySelector(s);
const store={get(k){try{return JSON.parse(localStorage.getItem(k))}catch(e){return null}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
let DAYS=[],byDate={},done=store.get('done')||{},cur=null,tab='devotion',showAns=false;
let family=store.get('family')||[],log=store.get('log')||{},editFam=false,jFilter='';
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const saveLog=()=>{for(const d in log){for(const n in log[d]){const e=log[d][n];if(!e.h&&!e.l)delete log[d][n]}if(!Object.keys(log[d]).length)delete log[d]}store.set('log',log)};
const pad=n=>String(n).padStart(2,'0');
const iso=d=>`${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
const parse=s=>{const[y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d)};
const DOW=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const todayISO=iso(new Date());
function monday(s){const d=parse(s);const k=(d.getDay()+6)%7;d.setDate(d.getDate()-k);return d}
function pickStart(){const h=location.hash.slice(1);if(byDate[h])return h;if(byDate[todayISO])return todayISO;
  const future=DAYS.find(d=>d.date>=todayISO);return (future||DAYS[DAYS.length-1]).date}
function renderWeek(){const n=$('#days');n.innerHTML='';const m=monday(cur);
  for(let i=0;i<7;i++){const d=new Date(m);d.setDate(m.getDate()+i);const s=iso(d);const has=!!byDate[s];
    const b=document.createElement('button');b.type='button';b.disabled=!has;
    b.className=(s===todayISO?'is-today ':'')+(done[s]?'done':'');b.setAttribute('aria-pressed',s===cur);
    b.innerHTML=`<span class="d">${DOW[d.getDay()]}</span><span class="n">${d.getMonth()+1}/${d.getDate()}</span><span class="check" aria-hidden="true">✓</span>`;
    b.setAttribute('aria-label',`${DOW[d.getDay()]} ${MON[d.getMonth()]} ${d.getDate()}${has?': '+byDate[s].title:''}`);
    b.onclick=()=>go(s);n.appendChild(b)}
  const pm=new Date(m);pm.setDate(m.getDate()-1);const nm=new Date(m);nm.setDate(m.getDate()+7);
  $('#prevWeek').disabled=iso(pm)<DAYS[0].date;$('#nextWeek').disabled=iso(nm)>DAYS[DAYS.length-1].date}
function weekJump(dir){const m=monday(cur);m.setDate(m.getDate()+7*dir);for(let i=0;i<7;i++){const d=new Date(m);d.setDate(m.getDate()+i);if(byDate[iso(d)])return go(iso(d))}}
function go(s){cur=s;tab='devotion';showAns=false;history.replaceState(null,'','#'+s);render();scrollTo(0,0)}
function devotion(d){const v=d.verses.map(([n,t])=>`<sup>${n}</sup>${t}`).join(' ');
 return `<div class="steps">
 <section class="step"><h3>Invocation</h3><p>In the name of the Father and of the ✠ Son and of the Holy Spirit. Amen.</p><p>Lord Jesus, thank You for bringing us together tonight. Open our ears to hear Your Word. Amen.</p></section>
 <section class="step"><h3>Scripture</h3><p class="ref">${d.ref} · ESV</p><p class="scripture">${v}</p><p class="rub">Reader: ${d.reader}.</p></section>
 <section class="step"><h3>${d.story_title}</h3>${d.story.map(p=>`<p>${p}</p>`).join('')}</section>
 <section class="step"><h3>${d.teach_title}</h3><div class="teach">${d.teach.map(p=>`<p>${p}</p>`).join('')}</div></section>
 <section class="step"><h3>Questions</h3><ul class="qs">${d.q.map(([w,t])=>`<li><span class="who">${w}</span>${t}</li>`).join('')}</ul></section>
 <section class="step" id="hl"><h3>Highs and lows</h3>${hlBlock()}</section>
 <section class="step"><h3>Doxology</h3><p class="hymn">Praise God, from whom all blessings flow;<br>Praise Him, all creatures here below;<br>Praise Him above, ye heavenly host;<br>Praise Father, Son, and Holy Ghost. Amen.</p></section>
 <section class="step"><h3>Closing prayer</h3><p>${d.prayer} <span id="hlPrayer">${hlPrayer()}</span> ${d.ask} Watch over us tonight and let Your holy angels be with us. In Jesus’ name. Amen.</p><p>Pray the Lord’s Prayer together.</p></section>
 </div>`}
function kids(d){const k=d.kids;
 return `<div class="steps">
 <div class="toolbar"><button class="btn" id="ansBtn" type="button" aria-pressed="${showAns}">${showAns?'Hide answers':'Show answers'}</button><button class="btn primary" id="printKids" type="button">Print kids’ sheet</button></div>
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
function devoPrint(d){return `<div class="devo"><h1>${d.title}</h1><p class="r">${fmt(d.date)} · ${d.series}</p>
 <h2>Invocation</h2><p>In the name of the Father and of the ✠ Son and of the Holy Spirit. Amen.</p>
 <h2>Scripture: ${d.ref} (ESV)</h2><p>${d.verses.map(([n,t])=>`<sup>${n}</sup>${t}`).join(' ')}</p><p class="r">Reader: ${d.reader}.</p>
 <h2>${d.story_title}</h2>${d.story.map(p=>`<p>${p}</p>`).join('')}<h2>${d.teach_title}</h2>${d.teach.map(p=>`<p>${p}</p>`).join('')}
 <h2>Questions</h2>${d.q.map(([w,t])=>`<p><b>${w}:</b> ${t}</p>`).join('')}<h2>Highs and lows · Doxology</h2>
 <h2>Closing prayer</h2><p>${d.prayer} ${hlPrayer().replace(/<span class="blank">\(the (highs|lows)\)<\/span>/g,'______')} ${d.ask} Watch over us tonight and let Your holy angels be with us. In Jesus’ name. Amen.</p><p>Pray the Lord’s Prayer together.</p></div>`}
function fmt(s){const d=parse(s);return `${['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][d.getDay()]}, ${['January','February','March','April','May','June','July','August','September','October','November','December'][d.getMonth()]} ${d.getDate()}`}
function doPrint(html){$('#printArea').innerHTML=html;window.print()}
function famEditor(){return `<div class="fam"><p class="note">Who’s joining devotions? Add each person once. Names stay on this device only.</p>
 <div class="famlist">${family.map((n,i)=>`<span class="chip">${esc(n)} <button type="button" class="x" data-rm="${i}" aria-label="Remove ${esc(n)}">×</button></span>`).join('')}</div>
 <form id="famForm" class="famform"><label for="famName" class="sr">Name</label><input id="famName" maxlength="24" placeholder="Name" autocomplete="off"><button class="btn" type="submit">Add</button>${family.length?'<button class="btn" type="button" id="famDone">Done</button>':''}</form></div>`}
function hlBlock(){if(!family.length||editFam)return `<p>Everyone shares one high and one low, Mom and Dad included.</p>${famEditor()}`;
 const e=log[cur]||{};
 return `<p>Everyone shares one high and one low. Type them in and they’ll show up in the closing prayer.</p><div class="hlrows">${family.map((n,i)=>`<div class="hlrow"><span class="who">${esc(n)}</span>
 <label class="sr" for="h${i}">${esc(n)} high</label><input id="h${i}" data-n="${esc(n)}" data-k="h" placeholder="High ☀" value="${esc((e[n]||{}).h||'')}" maxlength="140">
 <label class="sr" for="l${i}">${esc(n)} low</label><input id="l${i}" data-n="${esc(n)}" data-k="l" placeholder="Low ☁" value="${esc((e[n]||{}).l||'')}" maxlength="140"></div>`).join('')}</div>
 <p class="note">Saved on this device. <button type="button" class="link" id="editFam">Edit family</button></p>`}
function hlPrayer(){const e=log[cur]||{};const hs=[],ls=[];
 family.forEach(n=>{const x=e[n];if(!x)return;if(x.h)hs.push(`<b>${esc(n)}</b>: ${esc(x.h)}`);if(x.l)ls.push(`<b>${esc(n)}</b>: ${esc(x.l)}`)});
 return (hs.length?`Thank You for ${hs.join('; ')}.`:`Thank You for <span class="blank">(the highs)</span>.`)+' '+(ls.length?`Please help with ${ls.join('; ')}.`:`Please help with <span class="blank">(the lows)</span>.`)}
function journal(){const dates=Object.keys(log).sort().reverse();const names=[...new Set(dates.flatMap(d=>Object.keys(log[d])))];
 const rows=dates.map(dt=>{const ents=Object.entries(log[dt]).filter(([n])=>!jFilter||n===jFilter);if(!ents.length)return '';
  return `<section class="step jday"><p class="ref"><button type="button" class="link" data-go="${dt}">${fmt(dt)}${byDate[dt]?' · '+esc(byDate[dt].title):''}</button></p>
  ${ents.map(([n,x])=>`<div class="jent"><span class="who">${esc(n)}</span>${x.h?`<p>☀ ${esc(x.h)}</p>`:''}${x.l?`<p class="${x.ok?'okd':''}">☁ ${esc(x.l)} <label class="ans-ck"><input type="checkbox" data-d="${dt}" data-n="${esc(n)}" ${x.ok?'checked':''}> God answered</label></p>`:''}</div>`).join('')}</section>`}).join('');
 return `<div class="steps"><div class="toolbar"><span class="note">Highs and lows from every night, newest first.</span></div>
 ${names.length>1?`<div class="bank">${['',...names].map(n=>`<button type="button" class="chip fbtn ${jFilter===n?'on':''}" data-f="${esc(n)}">${n?esc(n):'Everyone'}</button>`).join('')}</div>`:''}
 ${rows||'<section class="step"><p>No entries yet. Share highs and lows on the Devotion tab, and they’ll collect here for you to look back on.</p></section>'}
 <section class="step"><h3>Back up your journal</h3><p class="note">The journal lives only on this device. Save a backup now and then, or to move it to another phone.</p>
 <div class="nav" style="margin:0"><button class="btn" type="button" id="bk">Save backup</button><label class="btn" for="rs">Restore backup</label><input type="file" id="rs" accept=".json,application/json" class="sr"></div><p class="note" id="bkMsg"></p></section></div>`}
function wireJournal(m){
 m.querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>go(b.dataset.go));
 m.querySelectorAll('.fbtn').forEach(b=>b.onclick=()=>{jFilter=b.dataset.f;render()});
 m.querySelectorAll('.ans-ck input').forEach(c=>c.onchange=()=>{const x=log[c.dataset.d][c.dataset.n];x.ok=c.checked;saveLog();c.closest('p').classList.toggle('okd',c.checked)});
 const bk=$('#bk');if(bk)bk.onclick=()=>{const blob=new Blob([JSON.stringify({family,log,done},null,1)],{type:'application/json'});const u=URL.createObjectURL(blob);const a=document.createElement('a');a.href=u;a.download=`devotions-journal-${todayISO}.json`;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),1000);$('#bkMsg').textContent='Backup saved to your downloads.'};
 const rs=$('#rs');if(rs)rs.onchange=()=>{const f=rs.files[0];if(!f)return;f.text().then(t=>{const j=JSON.parse(t);if(!j.log)throw 0;
   for(const d in j.log){log[d]=Object.assign(log[d]||{},j.log[d])}family=[...new Set([...family,...(j.family||[])])];Object.assign(done,j.done||{});
   store.set('family',family);saveLog();store.set('done',done);render();$('#bkMsg').textContent='Backup restored.'}).catch(()=>{$('#bkMsg').textContent='That file isn’t a journal backup. Pick the .json file you saved.'})}}
function wireHL(m){
 const ff=$('#famForm');if(ff)ff.onsubmit=e=>{e.preventDefault();const v=$('#famName').value.trim();if(v&&!family.includes(v)){family.push(v);store.set('family',family)}editFam=true;render();const n=$('#famName');if(n)n.focus()};
 m.querySelectorAll('[data-rm]').forEach(b=>b.onclick=()=>{family.splice(+b.dataset.rm,1);store.set('family',family);render()});
 const fd=$('#famDone');if(fd)fd.onclick=()=>{editFam=false;render()};
 const ef=$('#editFam');if(ef)ef.onclick=()=>{editFam=true;render()};
 m.querySelectorAll('.hlrow input').forEach(inp=>inp.oninput=()=>{const n=inp.dataset.n;log[cur]=log[cur]||{};log[cur][n]=log[cur][n]||{};log[cur][n][inp.dataset.k]=inp.value;saveLog();const p=$('#hlPrayer');if(p)p.innerHTML=hlPrayer()});
}
function render(){const d=byDate[cur];renderWeek();const m=$('#main');
 m.innerHTML=`<div class="hero"><span class="eyebrow">${cur===todayISO?'TONIGHT · ':''}${fmt(cur).toUpperCase()}</span><h2>${d.title}</h2>
 <div class="meta"><span class="chip">${d.series}</span><span class="chip">${d.ref}</span></div></div>
 <div class="tabs" role="tablist"><button class="tab" role="tab" aria-selected="${tab==='devotion'}" data-t="devotion">Devotion</button><button class="tab" role="tab" aria-selected="${tab==='kids'}" data-t="kids">Kids’ page</button><button class="tab" role="tab" aria-selected="${tab==='journal'}" data-t="journal">Journal</button></div>
 ${tab==='devotion'?devotion(d):tab==='kids'?kids(d):journal()}
 <div class="nav"><button class="btn" id="prev" type="button">‹ Previous</button>
 <button class="btn primary ${done[cur]?'is-done':''}" id="doneBtn" type="button">${done[cur]?'Done ✓':'Mark as done'}</button>
 <button class="btn" id="next" type="button">Next ›</button></div>
 ${tab==='devotion'?'<p style="text-align:center"><button class="btn" id="printDevo" type="button">Print devotion</button></p>':''}
 <footer>Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), copyright © 2001 by Crossway, a publishing ministry of Good News Publishers. Used by permission. All rights reserved.</footer>`;
 const i=DAYS.findIndex(x=>x.date===cur);
 $('#prev').disabled=i===0;$('#next').disabled=i===DAYS.length-1;
 $('#prev').onclick=()=>go(DAYS[i-1].date);$('#next').onclick=()=>go(DAYS[i+1].date);
 $('#doneBtn').onclick=()=>{done[cur]=!done[cur];store.set('done',done);render()};
 m.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{tab=t.dataset.t;render()});
 const ab=$('#ansBtn');if(ab)ab.onclick=()=>{showAns=!showAns;render()};
 const pk=$('#printKids');if(pk)pk.onclick=()=>doPrint(sheet(d));
 const pd=$('#printDevo');if(pd)pd.onclick=()=>doPrint(devoPrint(d));
 wireHL(m);wireJournal(m);
 const ws=$('#ws');if(ws)ws.addEventListener('click',e=>{if(e.target.tagName==='TD')e.target.classList.toggle('on')});
}
$('#todayBtn').onclick=()=>go(byDate[todayISO]?todayISO:pickStart());
$('#prevWeek').onclick=()=>weekJump(-1);$('#nextWeek').onclick=()=>weekJump(1);
fetch('days.json').then(r=>r.json()).then(j=>{DAYS=j;DAYS.forEach(d=>byDate[d.date]=d);cur=pickStart();render()})
 .catch(()=>{$('#main').innerHTML='<p class="note">Couldn’t load the devotions. Check your connection and refresh.</p>'});
})();
