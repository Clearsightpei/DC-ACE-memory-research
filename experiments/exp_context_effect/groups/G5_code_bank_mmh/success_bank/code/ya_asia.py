"""Bank primitive: 亚 (yà, 'Asia' — 6 strokes).

Promoted from p3_char_0234_亚 (G5 B8 PASS). Sibling of 业 (yi_ye.py) with
an added top-heng crown.

Recipe: P-A-006 stroke-primitive layer with MMH-verbatim anchors. All 5
joints are N-class (natural gap).

Reuse targets: 亚 (identity), 恶, 垩.
"""

from heng import draw_heng
from shu import draw_shu
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ya_asia(draw, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return _tx(x, y, ox, oy, scale)

    def w(v):
        return max(2, int(v * scale))

    # s1: top heng (crown)
    draw_heng(draw, T(78.8, 101.4), T(222.4, 92.9),
              width_head=w(8), width_tail=w(10))
    # s2: left tall vertical
    draw_shu(draw, T(108.4, 113.1), T(115.4, 267.5), width=w(7))
    # s3: right tall vertical
    draw_shu(draw, T(163.2, 104.6), T(165.8, 262.5), width=w(7))
    # s4: left outer dian (upper-left -> lower-right)
    draw_dian(draw, T(57.4, 176.1), T(89.9, 212.1),
              w_head=w(3), w_tail=w(7), bow=w(3), steps=40)
    # s5: right outer dian (upper-right -> lower-left)
    draw_dian(draw, T(226.2, 146.8), T(183.1, 206.2),
              w_head=w(3), w_tail=w(7), bow=w(3), steps=40)
    # s6: baseline heng (long, heaviest)
    draw_heng(draw, T(38.4, 276.0), T(266.0, 277.4),
              width_head=w(9), width_tail=w(11))
