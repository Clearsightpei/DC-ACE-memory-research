"""Bank primitive: 支 (zhi, "branch" — 4 strokes: heng + shu + heng_pie + na).

Promoted from p2_radical_132_支 (G5 B3 PASS 2026-08-08). Composition =
十 (top) + 又 (bottom). Note: does NOT call draw_you() because MMH gives
different anchor spread for 又-inside-支 (top-heng is longer, pie tail
moved right). Appears in 支/枝/技/歧/etc.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from heng_pie import draw_heng_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhi_branch(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top heng (long)
    draw_heng(draw, _tx(87.6, 126.9, ox, oy, scale),
              _tx(207.4, 111.9, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2 shu (vertical of 十)
    draw_shu(draw, _tx(133.9, 55.1, ox, oy, scale),
             _tx(138.3, 173.7, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3 heng_pie (top of 又)
    s3h = _tx(87.6, 186.9, ox, oy, scale)
    draw_heng_pie(draw, s3h,
                  _tx(46.6, 292.7, ox, oy, scale),
                  apex_x=s3h[0] + 95 * scale,
                  corner_x=s3h[0] + 92 * scale)
    # s4 na (bottom sweep)
    draw_na(draw, _tx(92.6, 206.2, ox, oy, scale),
            _tx(279.5, 297.4, ox, oy, scale),
            bow_perp=int(12 * scale),
            w_head=max(2, int(4 * scale)),
            w_tail=max(2, int(12 * scale)), steps=90)
