"""Bank primitive: 龹 (juán) — 6 strokes.

Promoted from p3_char_0284_龹 (G5 B9 A verdict 2026-08-09). NOVEL top-radical
that appears in 龸/巻/眷/券/勝 family. Structure: 2 opposing short dots
(dian) + 2 stacked hengs + 1 long central bowed pie (bent to weld both
P joints) + 1 right na. RARE-REUSE but structural template for the
"top-radical with central spine crossing two hengs" family.

Key A-recipe insight: s5 (central pie) is bent as a cubic bezier so it
passes through both P-joint centers (s3.mid, s4.mid). Straight chord
would miss both crossings — this is the A-recipe geometry.
"""

from PIL import ImageDraw

from heng import draw_heng
from na import draw_na
from dian import draw_dian


def _bezier3(p0, p1, p2, p3, n=100):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _draw_bent_pie(d, head, tail, ctrls, w_head=8, w_tail=2):
    pts = _bezier3(head, ctrls[0], ctrls[1], tail, n=110)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_juan_yong(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: short left dian
    draw_dian(draw, _tx(93.5, 90.5, ox, oy, scale),
              _tx(115.7, 111.0, ox, oy, scale),
              w_head=3, w_tail=7, bow=2, steps=32)
    # s2: short right dian
    draw_dian(draw, _tx(191.0, 68.3, ox, oy, scale),
              _tx(169.3, 106.6, ox, oy, scale),
              w_head=3, w_tail=7, bow=3, steps=32)
    # s3: upper heng
    draw_heng(draw, _tx(90.5, 138.9, ox, oy, scale),
              _tx(198.9, 125.4, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s4: lower heng
    draw_heng(draw, _tx(58.0, 180.2, ox, oy, scale),
              _tx(241.4, 163.5, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s5: long central BENT pie — bezier through joint band (A-recipe geometry)
    _draw_bent_pie(draw,
                   _tx(135.9, 56.0, ox, oy, scale),
                   _tx(38.4, 259.0, ox, oy, scale),
                   ctrls=[_tx(150, 130, ox, oy, scale),
                          _tx(100, 200, ox, oy, scale)],
                   w_head=max(2, int(8 * scale)),
                   w_tail=max(2, int(2 * scale)))
    # s6: right na
    draw_na(draw, _tx(168.2, 172.0, ox, oy, scale),
            _tx(285.4, 237.0, ox, oy, scale),
            bow_perp=14, w_head=4, w_tail=11, steps=80)
