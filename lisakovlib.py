#
# lisakov lib
#
# it is a super lib, which is able
# to draw some standard things from physics
#

from math import sin, cos, pi
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import rcParams

floor_y = 0
hl = 1.5 # Hatch Length
ytt = 3 * 0.41 # y top text

# consts
LW = 3
EC = 'k'
COLOR = 'none'
TALIGN = 'center'
stderr = 2  # stderr file

objects = []

def todeg(_R):
    return 180 * _R / pi
def torad(_D):
    return pi * _D / 180

#
# die - noreturn print error function
#
def die(err):
    f = open(stderr, "wt")
    #f.write("Lisacov-lib: fatal error: %s\n" % err)
    f.write("Lisacov-lib: \033[1;31mfatal error: \033[0m%s\n" % err)
    exit(1)

#
# push_object - create an object and return a pointer to it
#
def push_object(name, x, y, width, height, angle):
    objects.append([name, x, y, width, height, angle])
    return len(objects) - 1


#
# init - initialize library
#
def init(fs=15):
    global ax
    rcParams['font.size'] = fs
    (_, ax) = plt.subplots()

#
# render - show printed objects
#
def render(x0=0, y0=0, x1=0, y1=0):
    for i in objects:
        if i[1] < x0:
            x0 = i[1]
        if i[2] - i[4] < y0:
            y0 = i[2] - i[4]
        if i[1] + i[3] > x1:
            x1 = i[1] + i[3]
        if i[2] > y1:
            y1 = i[2]

    x0 -= 1
    y0 -= 1
    x1 += 1
    y1 += 1

    plt.axis('off')

    ax.set_xlim([x0, x1])
    ax.set_ylim([y0, y1])
    ax.set_aspect('equal')

    plt.show()

#
# draw plane
#
def plane(x=0, y=0, len=0, angle=0, lw=LW, wide=3):
    reverse = False
    while(angle >= 180):
        angle -= 180
        reverse = True

    r = torad(angle)
    xlen = len * cos(r)
    ylen = len * sin(r)

    ax.plot([x, x + xlen], [y, y + ylen], 'k', lw=lw, zorder=1)

    if(reverse):
        plane = Rectangle((x, y), len, wide, \
            angle=angle, lw=0, ec=EC, hatch='///',facecolor=COLOR)
    else:
        plane = Rectangle((x + wide * sin(r), y - wide * cos(r)), len, wide, \
            angle=angle, lw=0, ec=EC, hatch='///',facecolor=COLOR)
    ax.add_patch(plane)

    return push_object('plane', x, y, len, lw + wide, angle)

#
# draw box
#
def box(text, x, lw=LW, xlen=5, ylen=3):
    m = Rectangle((x, floor_y), xlen, ylen, \
        linewidth=lw, ec=EC, facecolor=COLOR)
    ax.add_patch(m)
    ax.text(x + xlen / 2, ytt, text, ha=TALIGN)

    return push_object("m", x, ylen, x + xlen, floor_y, 0)

def rope(a, b, lw=LW):
    if(a >= len(objects) or b >= len(objects)):
        die("uncorrect objects")
    ax.plot([objects[a][3], objects[b][1]], \
        [(objects[a][4] + objects[a][2]) / 2, (objects[b][4] + objects[b][2]) / 2], \
        '-k', lw=lw)



#
# rest actions
#
def m2(x1=0, lw=3, bh = 3, bl = 5):
    Fl = 5
    ### Force (applied to m1)
    plt.arrow(x1+bl, bh/2, Fl, 0, fc='k', lw=lw,
            length_includes_head=True, head_width=.4)
#    ax.text(x1+bl+Fl, bh/2+1,'$\\vv{\hspace{-4pt}F\hspace{2pt}}$', ha='right')
