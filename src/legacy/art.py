import math, random
random.seed(4)
W,H=640,330
GROUND=300
def figure(x, beard=True, arms="up", lean=0, hair="short", glow=False):
    y=GROUND; hx=x+lean; hy=y-152
    o=[]
    if glow:
        for k in range(18):
            a=math.pi*(1.05+0.9*k/17)
            r1,r2=(38,70) if k%2==0 else (40,56)
            o.append(f'<path d="M{hx+r1*math.cos(a):.1f},{hy+8+r1*math.sin(a):.1f} L{hx+r2*math.cos(a):.1f},{hy+8+r2*math.sin(a):.1f}" fill="none" stroke-width="1.3"/>')
    # cloak/back robe
    o.append(f'<path d="M{x-17},{y-124} C{x-26},{y-90} {x-34},{y-40} {x-36},{y-6} Q{x},{y+2} {x+36},{y-6} C{x+34},{y-40} {x+26},{y-90} {x+17},{y-124} Q{x},{y-132} {x-17},{y-124} Z"/>')
    # robe folds
    for dx,top in [(-18,-70),(-6,-60),(8,-64),(20,-72)]:
        o.append(f'<path d="M{x+dx*0.6},{y+top} Q{x+dx*0.9+3},{y-30} {x+dx*1.1},{y-6}" fill="none" stroke-width="1.2"/>')
    # sash
    o.append(f'<path d="M{x-21},{y-86} Q{x},{y-80} {x+21},{y-86} L{x+22},{y-79} Q{x},{y-73} {x-22},{y-79} Z"/>')
    o.append(f'<path d="M{x+6},{y-78} L{x+2},{y-56} L{x+9},{y-57} Z"/>')
    # mantle diagonal over shoulder
    o.append(f'<path d="M{x-17},{y-122} C{x-6},{y-110} {x+10},{y-98} {x+21},{y-86}" fill="none" stroke-width="1.6"/>')
    # neckline
    o.append(f'<path d="M{hx-7},{y-129} Q{hx},{y-121} {hx+7},{y-129}" fill="none" stroke-width="1.4"/>')
    # arms
    if arms=="up":
        L=[(x-16,y-120),(x-36,y-150),(x-44,y-180)]; R=[(x+16,y-120),(x+36,y-150),(x+44,y-180)]
    elif arms=="open":
        L=[(x-16,y-120),(x-40,y-110),(x-58,y-122)]; R=[(x+16,y-120),(x+40,y-110),(x+58,y-122)]
    else: # one up one down
        L=[(x-16,y-120),(x-30,y-98),(x-34,y-76)]; R=[(x+16,y-120),(x+38,y-146),(x+46,y-176)]
    for P in (L,R):
        (ax,ay),(bx,by),(cx,cy)=P
        # sleeve as wide band
        nx,ny=-(cy-ay),(cx-ax); d=math.hypot(nx,ny); nx,ny=nx/d*7,ny/d*7
        o.append(f'<path d="M{ax-nx:.1f},{ay-ny:.1f} Q{bx-nx:.1f},{by-ny:.1f} {cx-nx*1.3:.1f},{cy-ny*1.3:.1f} L{cx+nx*1.3:.1f},{cy+ny*1.3:.1f} Q{bx+nx:.1f},{by+ny:.1f} {ax+nx:.1f},{ay+ny:.1f}"/>')
        ux,uy=(cx-bx),(cy-by); d=math.hypot(ux,uy); ux,uy=ux/d,uy/d
        hxp,hyp=cx+ux*8,cy+uy*8
        o.append(f'<ellipse cx="{hxp:.1f}" cy="{hyp:.1f}" rx="4.5" ry="6.5" transform="rotate({math.degrees(math.atan2(uy,ux))-90:.0f} {hxp:.1f} {hyp:.1f})"/>')
    # feet
    o.append(f'<path d="M{x-14},{y-3} q-9,0 -10,5 h14 z M{x+14},{y-3} q9,0 10,5 h-14 z"/>')
    # neck
    o.append(f'<path d="M{hx-5},{hy+11} V{y-128} M{hx+5},{hy+11} V{y-128}" fill="none"/>')
    # head
    o.append(f'<ellipse cx="{hx}" cy="{hy}" rx="11" ry="13.5"/>')
    o.append(f'<path d="M{hx-11},{hy+1} q-3,1 -1,5 M{hx+11},{hy+1} q3,1 1,5" fill="none" stroke-width="1.3"/>')
    if hair=="short":
        o.append(f'<path d="M{hx-11.5},{hy-1} C{hx-13},{hy-15} {hx-4},{hy-18} {hx+2},{hy-16} C{hx+10},{hy-16} {hx+13},{hy-8} {hx+11.5},{hy-1} C{hx+8},{hy-9} {hx-4},{hy-11} {hx-11.5},{hy-1} Z"/>')
    elif hair=="curly":
        o.append(''.join(f'<circle cx="{hx+11*math.cos(a):.1f}" cy="{hy-4+12*math.sin(a):.1f}" r="4"/>' for a in [math.pi*(1.05+0.9*k/6) for k in range(7)]))
    else: # head wrap
        o.append(f'<path d="M{hx-12},{hy-3} C{hx-14},{hy-20} {hx+14},{hy-20} {hx+12},{hy-3} Q{hx},{hy-8} {hx-12},{hy-3} Z"/><path d="M{hx-10},{hy-8} Q{hx},{hy-13} {hx+10},{hy-8}" fill="none" stroke-width="1.1"/>')
    # face
    o.append(f'<path d="M{hx-7},{hy-4} q3,-2 5,0 M{hx+2},{hy-4} q3,-2 5,0" fill="none" stroke-width="1.2"/>')
    o.append(f'<circle cx="{hx-4.5}" cy="{hy-1}" r="1.2" class="dot"/><circle cx="{hx+4.5}" cy="{hy-1}" r="1.2" class="dot"/>')
    o.append(f'<path d="M{hx},{hy-1} l-1.5,5 h2.5" fill="none" stroke-width="1.1"/>')
    if beard:
        o.append(f'<path d="M{hx-10.5},{hy+3} C{hx-10},{hy+18} {hx-3},{hy+23} {hx},{hy+24} C{hx+3},{hy+23} {hx+10},{hy+18} {hx+10.5},{hy+3} C{hx+6},{hy+10} {hx-6},{hy+10} {hx-10.5},{hy+3} Z"/>')
        o.append(f'<path d="M{hx-4},{hy+8} Q{hx},{hy+10} {hx+4},{hy+8}" fill="none" stroke-width="1.1"/>')
    else:
        o.append(f'<path d="M{hx-4},{hy+6} Q{hx},{hy+9} {hx+4},{hy+6}" fill="none" stroke-width="1.1"/>')
    return "\n".join(o)

def flame(x,h,w=22,lean=0):
    t=GROUND
    s=f'<path d="M{x-w},{t} C{x-w-6},{t-h*.35} {x-w*.3+lean*.3},{t-h*.55} {x-w*.4+lean*.5},{t-h*.75} C{x-w*.1+lean*.6},{t-h*.62} {x+lean*.2},{t-h*.7} {x+lean},{t-h} C{x+w*.4+lean*.6},{t-h*.7} {x+w*.2},{t-h*.55} {x+w*.55},{t-h*.62} C{x+w*.6},{t-h*.4} {x+w+6},{t-h*.3} {x+w},{t} Z"/>'
    s+=f'<path d="M{x-w*.45},{t} C{x-w*.6},{t-h*.25} {x-w*.1},{t-h*.35} {x+lean*.4},{t-h*.55} C{x+w*.15},{t-h*.35} {x+w*.6},{t-h*.25} {x+w*.45},{t} Z" fill="none" stroke-width="1.3"/>'
    return s

o=[]
# furnace wall: bricks
o.append(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" rx="10"/>')
bw,bh=48,22
for r,yy in enumerate(range(4,H-4,bh)):
    off=0 if r%2==0 else bw/2
    o.append(f'<path d="M4,{yy} H{W-4}" fill="none" stroke-width="1"/>')
    xx=4-off
    while xx<W:
        if xx>4: o.append(f'<path d="M{xx},{yy} V{min(yy+bh,H-4)}" fill="none" stroke-width="1"/>')
        xx+=bw
# arched opening
ax0,ax1,atop=70,W-70,40
cx=(ax0+ax1)/2; rx=(ax1-ax0)/2; ry=150; sy=atop+ry
o.append(f'<path d="M{ax0},{H-4} V{sy} A{rx},{ry} 0 0 1 {ax1},{sy} V{H-4} Z" />')
# voussoir ring
o.append(f'<path d="M{ax0-18},{H-4} V{sy} A{rx+18},{ry+18} 0 0 1 {ax1+18},{sy} V{H-4}" fill="none"/>')
for k in range(1,16):
    a=math.pi*(1+k/16)
    o.append(f'<path d="M{cx+rx*math.cos(a):.1f},{sy+ry*math.sin(a):.1f} L{cx+(rx+18)*math.cos(a):.1f},{sy+(ry+18)*math.sin(a):.1f}" fill="none" stroke-width="1.2"/>')
# floor
o.append(f'<path d="M{ax0},{GROUND} H{ax1}" fill="none"/>')
# back flames (behind figures)
for x,h,w,l in [(110,170,24,-6),(160,120,20,4),(240,95,18,-4),(400,100,18,5),(480,125,20,-4),(530,175,24,6),(320,70,16,0)]:
    o.append(flame(x,h,w,l))
o.append(figure(165,beard=True,arms="up",hair="short"))
o.append(figure(258,beard=False,arms="mixed",hair="curly"))
o.append(figure(350,beard=True,arms="up",hair="wrap"))
o.append(figure(468,beard=False,arms="open",hair="short",glow=True))
# front flames low
for x,h,w,l in [(95,80,20,3),(150,55,16,-3),(500,58,16,3),(552,85,20,-3)]:
    o.append(flame(x,h,w,l))
# untied ropes on floor
o.append('<path d="M205,296 c10,-8 20,6 30,-2 s16,-6 22,2" fill="none" stroke-width="1.6"/><path d="M392,296 c8,-7 18,5 26,-1 s14,-5 20,2" fill="none" stroke-width="1.6"/>')
svg=f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Coloring picture: Shadrach, Meshach, and Abednego walking unharmed in the fiery furnace with a fourth man, their ropes lying on the floor">
<g fill="#fff" stroke="#1c1c1a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
{chr(10).join(o)}
</g><style>.dot{{fill:#1c1c1a}}</style></svg>'''
open(__import__('sys').argv[1],'w').write(svg)
