import lisakovlib as lskv

lskv.init()

lskv.plane(len=25)

a = lskv.box('$m_1$', 0)
b = lskv.box('$m_2$', 10)
c = lskv.box('$m_3$', 20)

lskv.rope(a, b)
lskv.rope(b, c)

lskv.render()
