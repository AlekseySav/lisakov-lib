import lisakovlib as lskv
from lisakovlib import margin, get_height

lskv.init()

lskv.plane(len=15)
w = lskv.wedge((1, 0), len=15)

lskv.box(margin(w, 0.3, 0, absolute=False), text="$m_2$", textpos=(-0.4, -0.2))

lskv.render(y1=10)
