import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib import rc, rcParams

def atan(x): 
    return np.degrees(np.arctan(x))

floor_y = 0
hl = 1.5 # Hatch Length
Fl = 5 # Force Length
lwc=2.5
ytt = 3 * 0.41 # y top text

# consts
LW = 3
EC = 'k'
COLOR = 'none'
TALIGN = 'center'
stderr = 2  # stderr file

objects = []

def init(fs=15):
    global ax

    rcParams['font.size'] = fs
    # rcParams['text.latex.preview'] = True
    # rc('axes', linewidth=1.5)
    # rc('text', usetex=True)
    # rc('text.latex', preamble=r'\usepackage{esvect}')
    (_, ax) = plt.subplots()
    # nil.subplots_adjust(left=0.05, bottom=0.15, right=0.95, top=0.95)
    
    # rcParams['hatch.linewidth']=lw/2

def render(start=-10, end=10):
    bl = 5
    bh = 3

#
# this is works for now, but have to be corrected
#

    # Table Plane
    tx0 = start - 1 # Table X0
    tx = end + bl + Fl + 1 # Table X_fin
    
    # Plot setup
    plt.axis('off')
    ax.set_xticks([]) #even if not shown need to set for correct bbox_inches
    ax.set_yticks([])

    ax.set_xlim([tx0, tx])
    ax.set_ylim([-hl,  bh*1.05])
    ax.set_aspect('equal')

    plt.show()

def die(err):
    print("Lisacov-lib panic: %s" % err, file=stderr)
    exit(1)

def floor(start=-20, end=10):
    ax.plot([start, end], [floor_y, floor_y], 'k', lw=LW,zorder=1)
    plane = Rectangle((start, floor_y), end - start, -hl, \
        lw=0, ec=EC, hatch='///',facecolor=COLOR) 
    ax.add_patch(plane)

    objects.append(("floor", start, floor_y, end, floor_y))
    return len(objects) - 1

def m(text, x, lw=LW, xlen=5, ylen=3):
    m = Rectangle((x, floor_y), xlen, ylen, \
        linewidth=lw, ec=EC, facecolor=COLOR)
    ax.add_patch(m)
    ax.text(x + xlen / 2, ytt, text, ha=TALIGN)

    objects.append(("m", x, floor_y, x + xlen, floor_y + ylen))
    return len(objects) - 1

def rope(a, b, lw=LW):
    if(a >= len(objects) or b >= len(objects)):
        die("uncorrect objects")
    a_len = objects[a][4] - objects[a][2]
    b_len = objects[b][4] - objects[b][2]
    ax.plot([objects[a][1], objects[b][3]], [a_len / 2, b_len / 2], 'k-', lw=lw)



#
# rest actions
#
def m2(x1=0, lw=3, bh = 3, bl = 5):
    x2 = -8.5
    x3 = x2*2
    ### m2
    m2 = Rectangle((x2, floor_y), bl, bh,
        linewidth=lw, ec='k', facecolor='none')
    ax.add_patch(m2)
    ax.text(x2+bl/2, ytt, '$m_2$', ha='center')

    ### m3
    m3 = Rectangle((x3, floor_y), bl, bh,
        linewidth=lw, ec='k', facecolor='none')
    ax.add_patch(m3)
    ax.text(x3+bl/2, ytt, '$m_3$', ha='center')

    ### Rope 1-2
    ax.plot([x1,x2+bl], [bh/2, bh/2], 'k-', lw=lwc)
    ### Rope 2-3
    ax.plot([x2,x3+bl], [bh/2, bh/2], 'k-', lw=lwc)

    ### Force (applied to m1)
    plt.arrow(x1+bl, bh/2, Fl, 0, fc='k', lw=lw,
            length_includes_head=True, head_width=.4)
    ax.text(x1+bl+Fl, bh/2+1,'$\\vv{\hspace{-4pt}F\hspace{2pt}}$', ha='right')




