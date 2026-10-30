import math
import os
HERE=os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else HERE
src=open(os.path.join(HERE,'art.py')).read()
exec(src[src.index('def figure'):src.index('def flame')].replace('GROUND',"300"), globals())
def wrap(o,label): return f'<svg viewBox="0 0 640 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}"><g fill="#fff" stroke="#1c1c1a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">{"".join(o)}</g><style>.dot{{fill:#1c1c1a}}</style></svg>'
B='<rect x="4" y="4" width="632" height="322" rx="10"/>'; G='<path d="M4,300 H636" fill="none"/>'
def star(x,y,r=8): return '<path d="'+'M'+' L'.join(f'{x+(r if k%2==0 else r*.45)*math.sin(math.pi*k/5):.1f},{y-(r if k%2==0 else r*.45)*math.cos(math.pi*k/5):.1f}' for k in range(10))+' Z"/>'
# Mon: prodigal son
m=[B,'<path d="M4,230 Q200,180 420,215 T636,200" fill="none" stroke-width="1.2"/>',
'<path d="M470,300 V170 H600 V300 Z M460,172 L535,120 L610,172 Z M520,300 V240 H550 V300 M484,200 h24 v24 h-24 Z M562,200 h24 v24 h-24 Z"/>',
figure(250,beard=True,arms="open",hair="short"),figure(340,beard=False,arms="open",hair="curly"),G,
'<path d="M120,300 q4,-20 8,0 M140,300 q4,-14 8,0" fill="none"/>','<circle cx="90" cy="70" r="24"/>']
# Tue: Abraham stars
t=[B,figure(220,beard=True,arms="up",hair="wrap"),G,'<path d="M430,300 L500,200 L570,300 Z M500,200 V300 M480,300 L500,250 L520,300" />']
import random; random.seed(5)
for _ in range(26):
    x,y=random.randint(30,610),random.randint(24,170)
    if not (150<x<300 and y>60): t.append(star(x,y,random.choice([5,7,9])))
t.append('<path d="M560,60 a22,22 0 1 0 24,28 a17,17 0 1 1 -24,-28 Z"/>')
# Wed: wilderness
w=[B,'<path d="M4,230 L90,150 L170,215 L260,130 L360,220 L460,140 L560,210 L636,170" fill="none" stroke-width="1.4"/>',
figure(250,beard=True,arms="mixed",hair="short"),G,'<circle cx="560" cy="60" r="26"/>']
for (x,y,rx,ry) in [(380,290,30,14),(430,292,22,10),(470,288,34,16),(120,292,26,11),(80,290,18,9)]: w.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}"/>')
w.append('<path d="M560,300 v-50 m0,18 h-16 v-14 m16,6 h14 v-18" fill="none" stroke-width="5"/>')
# Thu: three crosses
c=[B,'<path d="M4,300 Q320,170 636,300" />']
for (x,h,s) in [(200,150,.8),(320,190,1),(440,150,.8)]:
    top=300-h-40*s
    c.append(f'<rect x="{x-7*s:.0f}" y="{top:.0f}" width="{14*s:.0f}" height="{h:.0f}" /><rect x="{x-45*s:.0f}" y="{top+30*s:.0f}" width="{90*s:.0f}" height="{14*s:.0f}"/>')
c.append('<circle cx="320" cy="62" r="34" fill="none" stroke-dasharray="3 6"/>')
for k in range(12):
    a=2*math.pi*k/12; c.append(f'<path d="M{320+44*math.cos(a):.0f},{62+44*math.sin(a):.0f} L{320+58*math.cos(a):.0f},{62+58*math.sin(a):.0f}" fill="none" stroke-width="1.3"/>')
c.append('<path d="M60,90 q20,-24 46,-8 q24,-18 44,6 q-10,16 -40,10 q-24,12 -50,-8 Z M500,80 q20,-24 46,-8 q24,-18 44,6 q-10,16 -40,10 q-24,12 -50,-8 Z"/>')
# Fri: mighty fortress + candles
f=[B,'<path d="M4,300 Q160,210 330,230 T636,250 V326 H4 Z"/>','<path d="M200,230 V120 H380 V230 Z"/>']
for xx in range(200,380,20): f.append(f'<path d="M{xx},120 v-12 h10 v12" fill="none"/>')
for tx in (170,380):
    f.append(f'<path d="M{tx},240 V90 H{tx+50} V240 Z"/>')
    for xx in range(tx,tx+50,12): f.append(f'<path d="M{xx},90 v-10 h6 v10" fill="none"/>')
f.append('<path d="M195,80 V40 l26,10 l-26,10" /><path d="M405,80 V40 l26,10 l-26,10"/>')
f.append('<path d="M262,230 V196 a28,28 0 0 1 56,0 V230 Z M290,168 v62" />')
for (x,y) in [(230,150),(345,150),(185,120),(398,120)]: f.append(f'<path d="M{x},{y+20} V{y+6} a6,6 0 0 1 12,0 V{y+20} Z"/>')
for x in (470,510,550,590):
    f.append(f'<rect x="{x}" y="250" width="16" height="44"/><path d="M{x+8},250 q-8,-12 0,-24 q8,12 0,24 Z"/>')
f.append('<path d="M455,294 H620" fill="none"/>')
for (x,y) in [(60,40),(110,70),(480,40),(600,80)]: f.append(f'<path d="M{x},{y-6} v12 M{x-6},{y} h12" fill="none" stroke-width="1.3"/>')
PICS=[wrap(m,"Coloring picture: the father running to welcome his lost son home"),wrap(t,"Coloring picture: Abraham looking up at a sky full of stars"),
wrap(w,"Coloring picture: Jesus in the wilderness beside a pile of stones"),wrap(c,"Coloring picture: three crosses on a hill"),
wrap(f,"Coloring picture: a mighty fortress on a hill with All Saints' candles")]
