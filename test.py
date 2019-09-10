import lisakovlib as lskv

lskv.init()

lskv.floor(start=-20, end=20)

a = lskv.m('$m_1$', 10)
b = lskv.m('$m_2$', 0)
c = lskv.m('$m_3$', -10)

lskv.rope(a, b)
lskv.rope(b, c)

lskv.render(start=-10, end=10)
