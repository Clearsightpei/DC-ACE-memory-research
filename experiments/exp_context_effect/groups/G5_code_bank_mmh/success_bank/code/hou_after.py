"""Bank primitive: 后 (hòu, 'after' — 6 strokes).

Promoted from p3_char_0235_后 (G5 B8 PASS). 厂-body (spine + arm) + 口 bottom.

Recipe: P-A-006 stroke-primitive layer + inline 口 (kept as heng_zhe open
frame + 3 explicit strokes for the flat 口 aspect).

Reuse targets: 后, 逅, 垢, 姤.
"""

from pie import draw_pie
from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _thin_line(draw, head, tail, width):
    draw.line([head, tail], fill='black', width=width)
    r = width / 2 + 1
    hx, hy = head; tx, ty = tail
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')
    draw.ellipse([tx - r, ty - r, tx + r, ty + r], fill='black')


def draw_hou_after(draw, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return _tx(x, y, ox, oy, scale)

    def w(v):
        return max(2, int(v * scale))

    # s1: short top pie
    draw_pie(draw, T(208.3, 81.2), T(105.5, 116.0),
             bow_perp=6, w_head=w(6), w_tail=w(3))
    # s2: long left pie (spine of 厂)
    draw_pie(draw, T(79.7, 106.1), T(19.3, 280.7),
             bow_perp=10, w_head=w(9), w_tail=w(3))
    # s3: middle heng (arm of 厂)
    draw_heng(draw, T(97.9, 164.9), T(255.8, 151.2),
              width_head=w(7), width_tail=w(8))
    # s4: 口 left shu
    _thin_line(draw, T(98.7, 213.3), T(121.9, 295.3), w(7))
    # s5: 口 heng_zhe (open top+right)
    s5_head = T(115.7, 214.5)
    s5_tail = T(200.1, 261.3)
    corner = (s5_tail[0], s5_head[1] + 2 * scale)
    _thin_line(draw, s5_head, corner, w(7))
    _thin_line(draw, corner, s5_tail, w(7))
    # s6: 口 bottom heng
    draw_heng(draw, T(128.3, 284.5), T(223.8, 274.8),
              width_head=w(7), width_tail=w(8))
