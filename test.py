import lisakovlib as lskv
from lisakovlib import margin, get_height

lskv.init()

lskv.plane(len=15)
w = lskv.wedge((1, 0), len=15)

m1 = lskv.box(margin(w, 0.1, 0, absolute=False), text="$m_1$", textpos=(-0.4, -0.2), ylen=1, xlen=2.5)
m2 = lskv.box(margin(w, 0.5, 0, absolute=False), text="$m_2$", textpos=(-0.4, -0.2), xlen=3)
m3 = lskv.box(margin(w, 0.8, 0, absolute=False), text="$m_3$", textpos=(-0.4, -0.2), xlen=3)

lskv.rope(m1, m2, m3)

lskv.arrow(margin(m3, y=get_height(m3) / 2), text='$F$', angle=90)

lskv.render(y1=10)
