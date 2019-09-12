import lisakovlib as lskv

lskv.init()

floor = lskv.plane(len=25)

a = lskv.box((0, 0), text="$m_1$")
b = lskv.box((10, 0))
c = lskv.box((20, 10), angle=170, text="$M$")

p = lskv.plane(pos=(20, 13), len=5, angle=180)

lskv.arrow((15, 1.5), text='$F_1$')

lskv.rope(a, b, c, p)

lskv.box(lskv.margin(c, y=1, x=0.8, absolute=False), text="$m$")

lskv.render()
