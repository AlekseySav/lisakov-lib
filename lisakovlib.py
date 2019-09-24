#
# School physics plot lib
#

from sys import stderr
from math import sin, cos, pi
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from matplotlib import rc, rcParams

# consts
LW = 3
EC = 'k'
COLOR = 'white'
TALIGN = 'center'

objects = []

def todeg(_R):
    return 180 * _R / pi
def torad(_D):
    return pi * _D / 180

#
# die - noreturn print error function
#
def die(err):
    #stderr.write("Lisakov-lib: fatal error: %s\n" % err)
    stderr.write("Lisakov-lib: \033[1;31mfatal error: \033[0m%s\n" % err)
    exit(1)

#
# push_object - create an object and return a pointer to it
#
def push_object(name, x, y, width, height, angle) -> int:
    objects.append([name, x, y, width, height, angle])
    return len(objects) - 1

#
# functions for work with objects
#
def get_type(i) -> str:
    if(i >= len(objects)):
        die("invalid object")
    return objects[i][0]
def get_x(i) -> int:
    if(i >= len(objects)):
        die("invalid object")
    return objects[i][1]
def get_y(i) -> int:
    if(i >= len(objects)):
        die("invalid object")
    return objects[i][2]
def get_width(i) -> int:
    if(i >= len(objects)):
        die("invalid object")
    return objects[i][3]
def get_height(i) -> int:
    if(i >= len(objects)):
        die("invalid object")
    return objects[i][4]
def get_angle(i) -> float:
    if(i >= len(objects)):
        die("invalid object")
    return objects[i][5]

#
# init - initialize library
#
def init(fs=15):
    global ax
    rcParams['font.size'] = fs
    rc('text', usetex=True)
    (_, ax) = plt.subplots()

#
# render - show printed objects
#
def render(x0=0, y0=0, x1=0, y1=0):
    for i in range(len(objects)):
        x = get_x(i)
        y = get_y(i)
        xlen = get_width(i)
        ylen = get_height(i)
        r = torad(get_angle(i))

        xlen = xlen * cos(r) + ylen * sin(r)
        ylen = ylen * cos(r) + xlen * sin(r)
        if x < x0:
            x0 = x
        if y - ylen < y0:
            y0 = y - ylen
        if x + xlen > x1:
            x1 = x + xlen
        if y > y1:
            y1 = y

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
# draws a plane
#
def plane(pos=(0, 0), len=0, angle=0, lw=LW, wide=1):
    x = pos[0]
    y = pos[1]
    if(pos.__len__() > 2):
        angle = pos[2]

    r = torad(angle)
    xlen = len * cos(r)
    ylen = len * sin(r)

    ax.plot([x, x + xlen], [y, y + ylen], 'k', lw=lw, zorder=2)
    x = x + wide * sin(r)
    y = y - wide * cos(r)
    plane = Rectangle((x, y), len, wide, \
        angle=angle, lw=0, ec=EC, hatch='///', color=COLOR, zorder=2)
    ax.add_patch(plane)

    return push_object('plane', x, y + wide, len, wide, angle)

#
# draws a box
#
def box(pos, text="", lw=LW, xlen=5, ylen=3, angle=0, textpos=(0, 0)):
    x = pos[0]
    y = pos[1]
    if(pos.__len__() > 2):
        angle = pos[2]

    m = Rectangle((x, y), xlen, ylen, \
        angle=angle, linewidth=lw, ec=EC, color=COLOR, zorder=3)
    ax.add_patch(m)

    r = torad(angle)

    ax.text(x + xlen * cos(r) / 2 + textpos[0], \
        y + (ylen * cos(r) + xlen * sin(r)) / 2 + textpos[1], text, \
            ha=TALIGN, zorder=3)

    return push_object("box", x, y + ylen, xlen, ylen, angle)

#
# draws an arrow and its naming
#
def arrow(pos, len=5, lw=LW, text="", angle=0, hw=0.3, textpos=(0, 0)):
    x = pos[0]
    y = pos[1]
    if(pos.__len__() > 2):
        angle += pos[2]

    r = torad(angle)
    xl = len * cos(r)
    yl = len * sin(r)

    plt.arrow(x, y, xl, yl, fc='k', lw=lw, head_width=hw)
    ax.text(x + xl + textpos[0], y + yl + 0.5 + textpos[1], text, ha='right')
    return push_object("arrow", x, y, len, lw, angle)

#
# draws a wedge
#
def wedge(pos, len=5, angle=0, wedge_angle=30, lw=LW):
    x = pos[0]
    y = pos[1]
    if(pos.__len__() > 2):
        angle = pos[2]

    r1 = torad(angle)
    r2 = torad(angle + wedge_angle)

    lx = len * cos(r2)

    x1 = x + cos(r1) * lx
    y1 = y + sin(r1) * lx

    x2 = x + cos(r2) * len
    y2 = y + sin(r2) * len

    plt.gca().add_patch(plt.Polygon([(x, y), (x1, y1), (x2, y2)], \
        color=COLOR, lw=lw, ls='-', ec='black'))
    return push_object("wedge", x, y2, abs(x - x2), abs(y - y2), angle + wedge_angle)

#
# function, used by library for rope
#
def rope2(a, b, lw=LW):
    if(a >= len(objects) or b >= len(objects)):
        die("uncorrect objects")
        
    acx = get_x(a) + (get_width(a) * cos(torad(get_angle(a))) + \
        get_height(a) * sin(torad(get_angle(a)))) / 2
 
    acy = get_y(a) - get_height(a) + (get_height(a) * cos(torad(get_angle(a))) + \
        get_width(a) * sin(torad(get_angle(a)))) / 2

    bcx = get_x(b) + (get_width(b) * cos(torad(get_angle(b))) + \
        get_height(b) * sin(torad(get_angle(b)))) / 2

    bcy = get_y(b) - get_height(b) + (get_height(b) * cos(torad(get_angle(b))) + \
        get_width(b) * sin(torad(get_angle(b)))) / 2

    ax.plot([acx, bcx], \
        [acy, bcy], \
        '-k', lw=lw, zorder=1)

#
# draw a line between each pair of objects
#
def rope(*L, lw=LW):
    for i in range(len(L) - 1):
        rope2(L[i], L[i + 1], lw=lw)

#
# convert coordinates:
# offset from object -> absolute coordinates
#
def margin(obj, x=0, y=0, absolute=True):
    x1 = get_x(obj)
    y1 = get_y(obj) - get_height(obj)
    angle = get_angle(obj)
    r = torad(angle)

    if(not absolute):
        x *= get_width(obj)
        y *= get_height(obj)


    x1 += x * cos(r)
    y1 += y * cos(r)
    x1 += y * sin(r)
    y1 += x * sin(r)
    
    if(angle):
        return (x1, y1, angle)
    return (x1, y1)
