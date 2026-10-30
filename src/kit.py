import os
HERE=os.path.dirname(os.path.abspath(__file__))
import math,random
src=open(os.path.join(HERE,'legacy','art.py')).read()
exec(src[src.index('def figure'):src.index('def flame')].replace('GROUND',"300"), globals())
def P(d,**k): return f'<path d="{d}"'+''.join(f' {a.replace("_","-")}="{v}"' for a,v in k.items())+'/>'
N='fill="none"'
def person(x,beard=False,arms="open",hair="short",s=1.0):
    if s==1: return figure(x,beard=beard,arms=arms,hair=hair)
    return f'<g transform="translate({x*(1-s):.1f},{300*(1-s):.1f}) scale({s})">{figure(x,beard=beard,arms=arms,hair=hair)}</g>'
def angel(x,s=1.0):
    w=f'<path d="M{x-14},176 C{x-60},120 {x-110},120 {x-96},150 C{x-110},170 {x-80},200 {x-18},206 Z"/><path d="M{x+14},176 C{x+60},120 {x+110},120 {x+96},150 C{x+110},170 {x+80},200 {x+18},206 Z"/>'
    for k in range(3): w+=f'<path d="M{x-30-k*18},{150+k*4} q-6,20 4,40 M{x+30+k*18},{150+k*4} q6,20 -4,40" fill="none" stroke-width="1.2"/>'
    g=w+figure(x,beard=False,arms="mixed",hair="curly")+f'<ellipse cx="{x}" cy="114" rx="13" ry="4" fill="none"/>'
    return g if s==1 else f'<g transform="translate({x*(1-s):.1f},{300*(1-s):.1f}) scale({s})">{g}</g>'
def star(x,y,r=8): return '<path d="M'+' L'.join(f'{x+(r if k%2==0 else r*.45)*math.sin(math.pi*k/5):.1f},{y-(r if k%2==0 else r*.45)*math.cos(math.pi*k/5):.1f}' for k in range(10))+' Z"/>'
def sun(x=560,y=60,r=24):
    s=f'<circle cx="{x}" cy="{y}" r="{r}"/>'
    for k in range(10):
        a=2*math.pi*k/10; s+=f'<path d="M{x+(r+6)*math.cos(a):.0f},{y+(r+6)*math.sin(a):.0f} L{x+(r+16)*math.cos(a):.0f},{y+(r+16)*math.sin(a):.0f}" fill="none" stroke-width="1.3"/>'
    return s
def moon(x=560,y=60): return f'<path d="M{x},{y} a22,22 0 1 0 24,28 a17,17 0 1 1 -24,-28 Z"/>'
def stars(n=20,seed=1,avoid=None):
    random.seed(seed); o=''
    for _ in range(n):
        x,y=random.randint(30,610),random.randint(24,150)
        if avoid and avoid[0]<x<avoid[1]: continue
        o+=star(x,y,random.choice([4,6,8]))
    return o
def cloud(x,y): return f'<path d="M{x},{y} q20,-24 46,-8 q24,-18 44,6 q-10,16 -40,10 q-24,12 -50,-8 Z"/>'
def hills(): return '<path d="M4,240 Q160,190 320,225 T636,210" fill="none" stroke-width="1.3"/>'
def mountains(): return '<path d="M4,230 L90,150 L170,215 L260,130 L360,220 L460,140 L560,210 L636,170" fill="none" stroke-width="1.4"/>'
def waves(y=270,x0=4,x1=636):
    o=''
    for r in range(3):
        d=f'M{x0},{y+r*12}'+''.join(f' q15,-8 30,0' for _ in range(int((x1-x0)/30)))
        o+=f'<path d="{d}" fill="none" stroke-width="1.5"/>'
    return o
def tent(x): return f'<path d="M{x-70},300 L{x},200 L{x+70},300 Z M{x},200 V300 M{x-20},300 L{x},250 L{x+20},300"/>'
def house(x): return f'<path d="M{x-65},300 V170 H{x+65} V300 Z M{x-75},172 L{x},120 L{x+75},172 Z M{x-15},300 V240 H{x+15} V300 M{x-51},200 h24 v24 h-24 Z M{x+27},200 h24 v24 h-24 Z"/>'
def stones(x,n=3):
    return ''.join(f'<ellipse cx="{x+i*34}" cy="{292-(i%2)*2}" rx="{18+(i%3)*6}" ry="{9+(i%2)*3}"/>' for i in range(n))
def crosses():
    o=''
    for (x,h,s) in [(200,150,.8),(320,190,1),(440,150,.8)]:
        top=300-h-40*s; o+=f'<rect x="{x-7*s:.0f}" y="{top:.0f}" width="{14*s:.0f}" height="{h:.0f}"/><rect x="{x-45*s:.0f}" y="{top+30*s:.0f}" width="{90*s:.0f}" height="{14*s:.0f}"/>'
    return o
def manger(x):
    return f'<path d="M{x-60},250 L{x+60},250 L{x+46},278 L{x-46},278 Z M{x-46},278 L{x-58},300 M{x+46},278 L{x+58},300 M{x-30},278 L{x-40},300 M{x+30},278 L{x+40},300"/>' + \
      ''.join(f'<path d="M{x-56+k*14},250 l6,-10" fill="none" stroke-width="1.2"/>' for k in range(9)) + \
      f'<ellipse cx="{x}" cy="240" rx="34" ry="13"/><circle cx="{x+30}" cy="232" r="11"/><path d="M{x-28},238 q20,-6 44,0 M{x-20},244 q20,-6 40,0" fill="none" stroke-width="1.1"/><circle cx="{x+27}" cy="231" r="1.2" class="dot"/><circle cx="{x+33}" cy="231" r="1.2" class="dot"/>'
def bigstar(x=320,y=60): return star(x,y,26)+''.join(f'<path d="M{x},{y+30} L{x+d},{y+90}" fill="none" stroke-width="1.2" stroke-dasharray="4 5"/>' for d in (-40,0,40))
def sheep(x,s=1):
    g=f'<g transform="translate({x},{300}) scale({s})">'
    g+='<path d="M-30,-14 q-6,-14 8,-18 q4,-14 18,-10 q10,-12 22,-2 q14,-4 16,10 q12,6 4,20 q4,12 -12,14 h-44 q-16,-2 -12,-14 Z"/>'
    g+='<ellipse cx="38" cy="-22" rx="11" ry="8"/><circle cx="41" cy="-24" r="1.3" class="dot"/><path d="M-18,0 v-0 M-18,2 v-6 M-6,2 v-6 M14,2 v-6 M26,2 v-6" fill="none" stroke-width="3"/>'
    return g+'</g>'
def ark(x=320):
    return f'<path d="M{x-180},230 H{x+180} L{x+150},280 H{x-150} Z M{x-90},230 V180 H{x+90} V230 M{x-100},182 L{x},150 L{x+100},182 Z"/>'+''.join(f'<rect x="{x-70+k*40}" y="196" width="18" height="16"/>' for k in range(4))+''.join(f'<path d="M{x-170+k*30},240 v34" fill="none" stroke-width="1"/>' for k in range(12))
def rainbow(x=320,y=230): return ''.join(f'<path d="M{x-250+k*16},{y} A{250-k*16},{170-k*14} 0 0 1 {x+250-k*16},{y}" fill="none"/>' for k in range(5))
def tree(x,h=120):
    return f'<path d="M{x-8},300 V{300-h*.55} H{x+8} V300"/><circle cx="{x}" cy="{300-h*.75}" r="{h*.28:.0f}"/><circle cx="{x-h*.2:.0f}" cy="{300-h*.6}" r="{h*.2:.0f}"/><circle cx="{x+h*.2:.0f}" cy="{300-h*.6}" r="{h*.2:.0f}"/>'
def tablets(x,y=200):
    o=''
    for dx in (-28,28):
        o+=f'<path d="M{x+dx-24},{y+70} V{y+14} a24,24 0 0 1 48,0 V{y+70} Z"/>'+''.join(f'<path d="M{x+dx-14},{y+22+k*10} h28" fill="none" stroke-width="1"/>' for k in range(4))
    return o
def bush(x):
    o=f'<path d="M{x-50},300 q-10,-40 20,-50 q0,-30 30,-30 q30,0 30,30 q30,10 20,50 Z"/>'
    for dx,h in [(-30,60),(0,90),(30,60),(-14,74),(16,74)]:
        o+=f'<path d="M{x+dx-10},{260} C{x+dx-14},{260-h*.5} {x+dx},{260-h*.7} {x+dx},{260-h} C{x+dx+2},{260-h*.7} {x+dx+14},{260-h*.5} {x+dx+10},260 Z"/>'
    return o
def basket(x):
    return f'<path d="M{x-60},268 Q{x},300 {x+60},268 L{x+50},252 H{x-50} Z"/>'+''.join(f'<path d="M{x-50+k*12},254 l4,22" fill="none" stroke-width="1"/>' for k in range(9))+f'<ellipse cx="{x}" cy="250" rx="26" ry="9"/><circle cx="{x+18}" cy="244" r="9"/>'+''.join(f'<path d="M{x-120+k*44},{290} q10,-30 4,-60 M{x-116+k*44},{250} q10,-6 16,4" fill="none" stroke-width="1.4"/>' for k in (0,1,5,6))
def wall(x0,x1,y=170):
    o=f'<path d="M{x0},300 V{y} H{x1} V300 Z"/>'
    for yy in range(y,300,20):
        off=0 if (yy//20)%2 else 20
        o+=f'<path d="M{x0},{yy} H{x1}" fill="none" stroke-width="1"/>'+''.join(f'<path d="M{xx},{yy} v20" fill="none" stroke-width="1"/>' for xx in range(x0+20+off,x1,40))
    o+=''.join(f'<path d="M{xx},{y} v-12 h12 v12" fill="none"/>' for xx in range(x0,x1-10,24))
    return o
def trumpet(x,y): return f'<path d="M{x},{y} L{x+60},{y-20} L{x+66},{y-34} L{x+74},{y-6} L{x+64},{y-12} L{x+2},{y+8} Z"/>'
def jar(x): return f'<path d="M{x-16},300 q-8,-30 4,-46 h24 q12,16 4,46 Z M{x-10},254 v-8 h20 v8"/><path d="M{x},246 q-8,-14 0,-26 q8,12 0,26 Z"/>'
def temple(x=320):
    o=f'<path d="M{x-150},300 V290 H{x+150} V300 M{x-140},290 V280 H{x+140} V290 M{x-150},170 L{x},120 L{x+150},170 Z M{x-150},170 H{x+150} V182 H{x-150} Z"/>'
    for k in range(6): o+=f'<path d="M{x-120+k*48},182 V280 h16 V182 Z"/>'
    return o
def scroll(x,y=240): return f'<path d="M{x-50},{y} H{x+50} V{y+40} H{x-50} Z"/><ellipse cx="{x-50}" cy="{y+20}" rx="8" ry="22"/><ellipse cx="{x+50}" cy="{y+20}" rx="8" ry="22"/>'+''.join(f'<path d="M{x-36},{y+8+k*8} h{60-(k%2)*16}" fill="none" stroke-width="1"/>' for k in range(4))
def table(x0,x1): return f'<path d="M{x0},244 H{x1} V258 H{x0} Z M{x0+20},258 V300 M{x1-20},258 V300"/>'
def candles(x,n=4,lit=4):
    o=''
    for i in range(n):
        cx=x+i*36; o+=f'<rect x="{cx}" y="250" width="16" height="44"/>'
        if i<lit: o+=f'<path d="M{cx+8},250 q-8,-12 0,-24 q8,12 0,24 Z"/>'
    return o+f'<path d="M{x-14},294 H{x+n*36}" fill="none"/>'
def wreath(x,lit=1):
    o=f'<ellipse cx="{x}" cy="270" rx="110" ry="26"/><ellipse cx="{x}" cy="270" rx="70" ry="14"/>'
    for k in range(14):
        a=2*math.pi*k/14; o+=f'<ellipse cx="{x+92*math.cos(a):.0f}" cy="{270+20*math.sin(a):.0f}" rx="10" ry="5" transform="rotate({math.degrees(a)+90:.0f} {x+92*math.cos(a):.0f} {270+20*math.sin(a):.0f})"/>'
    for i,(dx,dy) in enumerate([(-80,-6),(-26,-20),(26,-20),(80,-6)]):
        o+=f'<rect x="{x+dx-8}" y="{200+dy}" width="16" height="{66-dy*0}"/>'
        if i<lit: o+=f'<path d="M{x+dx},{200+dy} q-8,-12 0,-24 q8,12 0,24 Z"/>'
    o+=f'<rect x="{x-9}" y="176" width="18" height="86"/>' if lit>4 else ''
    if lit>4: o+=f'<path d="M{x},176 q-8,-12 0,-24 q8,12 0,24 Z"/>'
    return o
def throne(x): return f'<path d="M{x-40},300 V200 Q{x},170 {x+40},200 V300 M{x-40},250 H{x+40}"/>'
def harp(x): return f'<path d="M{x},300 L{x},180 Q{x+70},170 {x+60},300 Z" fill="none" stroke-width="3"/>'+''.join(f'<path d="M{x+k*10},{300} V{186-k*1}" fill="none" stroke-width="1"/>' for k in range(1,6))
def sling(x,y): return f'<path d="M{x},{y} q30,30 60,0" fill="none"/><circle cx="{x+30}" cy="{y+15}" r="7"/>'
def giant(x):
    return f'<g transform="translate({x*(1-1.5):.1f},{300*(1-1.5):.1f}) scale(1.5)">{figure(x,beard=True,arms="mixed",hair="wrap")}</g>'
def well(x): return f'<path d="M{x-40},300 V250 H{x+40} V300 M{x-40},250 Q{x},240 {x+40},250 M{x-34},250 V190 M{x+34},250 V190 M{x-44},190 H{x+44} L{x},166 Z"/>'+''.join(f'<path d="M{x-40},{262+k*12} H{x+40}" fill="none" stroke-width="1"/>' for k in range(3))
def bread(x):
    return ''.join(f'<ellipse cx="{x+i*30}" cy="{292-(i%2)*6}" rx="16" ry="9"/><path d="M{x+i*30-8},{288-(i%2)*6} l4,4 M{x+i*30},{286-(i%2)*6} l4,4" fill="none" stroke-width="1"/>' for i in range(4))
def flakes(n=40,seed=3):
    random.seed(seed); return ''.join(f'<circle cx="{random.randint(20,620)}" cy="{random.randint(30,230)}" r="2.5"/>' for _ in range(n))
def boat(x,y=258):
    return f'<path d="M{x-90},{y} H{x+90} L{x+66},{y+28} H{x-66} Z M{x},{y} V{y-110} L{x+60},{y-30} H{x} Z"/>'
def fish(x,y): return f'<path d="M{x},{y} q30,-20 60,0 q-30,20 -60,0 Z M{x+60},{y} l16,-12 v24 Z"/><circle cx="{x+14}" cy="{y-3}" r="1.6" class="dot"/>'
def bigfish(x=320,y=200):
    return f'<path d="M{x-160},{y} q160,-110 300,0 q-140,110 -300,0 Z M{x+140},{y} l50,-40 v80 Z"/><circle cx="{x-120}" cy="{y-12}" r="7"/><path d="M{x-150},{y+8} q20,10 40,0" fill="none"/>'+''.join(f'<path d="M{x-60+k*40},{y-40} q16,40 0,80" fill="none" stroke-width="1"/>' for k in range(4))
def palm(x): return f'<path d="M{x},300 Q{x+10},220 {x},160" fill="none" stroke-width="5"/>'+''.join(f'<path d="M{x},160 q{dx},{dy} {dx*2},{dy+30}" fill="none" stroke-width="3"/>' for dx,dy in [(-40,-20),(40,-20),(-30,-40),(30,-40),(0,-50)])
def donkey(x):
    return f'<path d="M{x-50},240 q0,-30 40,-30 h50 q20,0 26,-30 l10,-6 l6,10 q2,30 -18,46 v60 h-10 v-40 h-50 v40 h-10 v-40 q-20,0 -20,-10 Z"/><path d="M{x+64},180 l-4,-22 l10,16 M{x+76},176 l2,-22 l6,20" />'
def lamb(x): return sheep(x,0.8)
def crown(x,y): return f'<path d="M{x-24},{y+20} V{y} L{x-12},{y+10} L{x},{y-6} L{x+12},{y+10} L{x+24},{y} V{y+20} Z"/>'
def coat(x): return f'<path d="M{x-40},300 V200 L{x-20},180 H{x+20} L{x+40},200 V300 Z M{x-40},200 L{x-70},250 L{x-56},258 L{x-40},230 M{x+40},200 L{x+70},250 L{x+56},258 L{x+40},230"/>'+''.join(f'<path d="M{x-40},{214+k*18} H{x+40}" fill="none" stroke-width="1.2"/>' for k in range(5))
def pit(x): return f'<ellipse cx="{x}" cy="280" rx="70" ry="16"/><path d="M{x-70},280 V300 M{x+70},280 V300" fill="none"/>'+stones(x-90,1)+stones(x+70,1)
def bars(x0,x1): return f'<path d="M{x0},60 H{x1} V170 H{x0} Z"/>'+''.join(f'<path d="M{xx},60 V170" fill="none" stroke-width="4"/>' for xx in range(x0+16,x1,22))
def pyramids(): return '<path d="M380,300 L470,170 L560,300 Z M470,170 L480,300 M520,300 L590,200 L636,262" />'
def wheat(x0,x1): return ''.join(f'<path d="M{x},300 Q{x+4},250 {x+2},210" fill="none" stroke-width="1.3"/>'+''.join(f'<ellipse cx="{x-2}" cy="{214+i*7}" rx="2.6" ry="5" transform="rotate(-25 {x-2} {214+i*7})"/><ellipse cx="{x+6}" cy="{214+i*7}" rx="2.6" ry="5" transform="rotate(25 {x+6} {214+i*7})"/>' for i in range(4)) for x in range(x0,x1,16))
def altar(x): return f'<path d="M{x-50},300 V250 H{x+50} V300 Z"/>'+''.join(f'<path d="M{x-50},{262+k*12} H{x+50}" fill="none" stroke-width="1"/>' for k in range(3))+''.join(f'<path d="M{x+dx-12},250 C{x+dx-16},{250-h*.5} {x+dx},{250-h*.7} {x+dx},{250-h} C{x+dx+2},{250-h*.7} {x+dx+16},{250-h*.5} {x+dx+12},250 Z"/>' for dx,h in [(-26,50),(0,80),(26,50)])
def ram(x): return sheep(x,1)+f'<path d="M{x+30},{278} q-14,-14 -2,-22 q10,6 4,16" fill="none" stroke-width="2"/>'
def gift(x): return f'<rect x="{x-30}" y="250" width="60" height="50"/><path d="M{x-30},266 H{x+30} M{x},250 V300 M{x},250 q-20,-24 -26,-4 q10,6 26,4 q20,-24 26,-4 q-10,6 -26,4" fill="none"/>'
def window(x): return f'<path d="M{x},40 h120 v90 h-120 Z M{x+60},40 v90 M{x},85 h120" fill="none"/>'
def scene(*parts,label=""):
    body=''.join(parts)
    return f'<svg viewBox="0 0 640 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}"><g fill="#fff" stroke="#1c1c1a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"><rect x="4" y="4" width="632" height="322" rx="10"/>{body}<path d="M4,300 H636" fill="none"/></g><style>.dot{{fill:#1c1c1a}}</style></svg>'
