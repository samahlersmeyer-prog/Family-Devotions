import math,re
import os
HERE=os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else HERE
src=open(os.path.join(HERE,'art.py')).read()
exec(src[src.index('def figure'):src.index('def flame')].replace('GROUND',"300"), globals())
def wrap(o,label):
    return f'<svg viewBox="0 0 640 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}"><g fill="#fff" stroke="#1c1c1a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">{"".join(o)}</g><style>.dot{{fill:#1c1c1a}}</style></svg>'
def kid(x,beard=False,arms="open",hair="short",s=0.7):
    return f'<g transform="translate({x*(1-s):.1f},{300*(1-s):.1f}) scale({s})">{figure(x,beard=beard,arms=arms,hair=hair)}</g>'
mon=re.search(r'<svg.*?</svg>',open(os.path.join(HERE,'mon.svg')).read(),re.S).group(0)
# Tue: church door
t=['<rect x="4" y="4" width="632" height="322" rx="10"/>']
for yy in range(4,300,26):
    off=0 if (yy//26)%2 else 30
    t.append(f'<path d="M4,{yy} H636" fill="none" stroke-width="1"/>')
    for xx in range(4-off,640,60):
        if xx>4: t.append(f'<path d="M{xx},{yy} V{yy+26}" fill="none" stroke-width="1"/>')
t.append('<path d="M330,300 V120 A110,110 0 0 1 550,120 V300 Z"/><path d="M314,300 V120 A126,126 0 0 1 566,120 V300" fill="none"/>')
for xx in range(358,550,28): t.append(f'<path d="M{xx},300 V{120-math.sqrt(max(0,110**2-(xx-440)**2))+6:.0f}" fill="none" stroke-width="1.2"/>')
t.append('<path d="M330,150 H550 M330,250 H550" fill="none" stroke-width="3"/>')
t.append('<circle cx="520" cy="210" r="8"/><path d="M520,218 v14" fill="none"/>')
t.append('<path d="M372,142 L436,140 L438,226 L374,228 Z"/>')
for k in range(8): t.append(f'<path d="M382,{154+k*9} H{428-(k%3)*6}" fill="none" stroke-width="1"/>')
t.append('<text x="380" y="152" style="font:700 9px sans-serif;fill:#1c1c1a;stroke:none">95</text><circle cx="405" cy="146" r="2" class="dot"/>')
t.append(figure(230,beard=False,arms="mixed",hair="short"))
t.append('<path d="M272,126 l18,-26 M282,92 l20,12 l-6,8 l-20,-12 Z"/>')
t.append('<path d="M4,300 H636" fill="none"/>')
tue=wrap(t,"Coloring picture: Martin Luther nailing the 95 Theses to the church door")
# Wed: Worms
w=['<rect x="4" y="4" width="632" height="322" rx="10"/>','<path d="M4,300 H636" fill="none"/>']
for xx in (60,580): w.append(f'<path d="M{xx-18},300 V60 H{xx+18} V300 M{xx-24},60 H{xx+24} M{xx-24},300 H{xx+24}" />')
w.append('<path d="M120,40 Q320,90 520,40" fill="none"/><path d="M120,40 V70 M520,40 V70" fill="none"/>')
w.append('<path d="M330,230 H600 V244 H330 Z M346,244 V300 M584,244 V300" />')
import random; random.seed(3)
for i,xx in enumerate(range(350,580,30)):
    h=12+(i%3)*8
    for k in range(3 if i%2 else 2): w.append(f'<rect x="{xx}" y="{230-(k+1)*10}" width="{24-(k%2)*4}" height="9" rx="1.5"/>')
w.append('<path d="M450,160 h60 v70 h-60 Z M444,160 h72 l-6,-16 h-60 Z"/>')
w.append('<path d="M462,144 l6,-14 l6,10 l6,-14 l6,14 l6,-10 l6,14 Z"/>')
w.append(figure(220,beard=False,arms="open",hair="short"))
w.append('<path d="M140,96 q60,-30 120,0" fill="none" stroke-width="1.3" stroke-dasharray="4 4"/>')
wed=wrap(w,"Coloring picture: Martin Luther standing before the emperor and a table of his books")
# Thu: Wartburg
c=['<rect x="4" y="4" width="632" height="322" rx="10"/>','<path d="M4,250 Q160,170 330,200 T636,210 V326 H4 Z" />']
c.append('<path d="M250,200 V120 H420 V200 Z"/>')
for xx in range(250,420,20): c.append(f'<path d="M{xx},120 v-12 h10 v12" fill="none"/>')
c.append('<path d="M420,200 V70 H470 V200 Z"/>')
for xx in range(420,470,12): c.append(f'<path d="M{xx},70 v-10 h6 v10" fill="none"/>')
for (x,y) in [(275,140),(310,140),(345,140),(380,140),(437,90),(437,130)]: c.append(f'<path d="M{x},{y+20} V{y+6} a6,6 0 0 1 12,0 V{y+20} Z"/>')
c.append('<path d="M320,200 V176 a14,14 0 0 1 28,0 V200" />')
c.append('<path d="M60,60 a20,20 0 1 0 22,26 a16,16 0 1 1 -22,-26 Z"/>')
for (x,y) in [(140,50),(200,80),(540,40),(590,90),(500,110)]: c.append(f'<path d="M{x},{y-6} v12 M{x-6},{y} h12" fill="none" stroke-width="1.3"/>')
c.append('<path d="M120,300 H300 L290,262 H130 Z"/><path d="M160,262 L210,246 L260,262 L210,270 Z M210,246 V270" />')
for k in range(3): c.append(f'<path d="M{170+k*6},{258-k*2} l30,-8 M{220},{250+k*5} l30,8" fill="none" stroke-width="1"/>')
c.append('<rect x="100" y="238" width="12" height="24"/><path d="M106,238 q-6,-10 0,-18 q6,8 0,18" />')
thu=wrap(c,"Coloring picture: Wartburg Castle at night with Luther's candle and open Bible")
# Fri: family at table
f=['<rect x="4" y="4" width="632" height="322" rx="10"/>','<path d="M4,300 H636" fill="none"/>',
'<path d="M470,40 h120 v90 h-120 Z M530,40 v90 M470,85 h120" fill="none"/>']
f.append(figure(120,beard=True,arms="open",hair="short"))
f.append(figure(520,beard=False,arms="open",hair="wrap"))
f.append(kid(240,hair="curly")); f.append(kid(320,hair="short")); f.append(kid(400,hair="wrap"))
f.append('<path d="M150,244 H490 V258 H150 Z M170,258 V300 M470,258 V300" />')
f.append('<path d="M290,244 L320,232 L350,244 L320,250 Z M320,232 V250"/>')
f.append('<rect x="372" y="222" width="10" height="22"/><path d="M377,222 q-6,-10 0,-18 q6,8 0,18"/>')
fri=wrap(f,"Coloring picture: a family gathered around the table with a Bible and a candle")
PICS=[mon,tue,wed,thu,fri]
