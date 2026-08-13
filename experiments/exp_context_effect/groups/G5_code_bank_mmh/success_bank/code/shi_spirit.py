"""Bank primitive: 礻 (shi, 'spirit' left-radical — 4 strokes:
dian + heng_pie + shu + dian).

Promoted from p2_radical_116_礻__retry_2 (G5 B4 R2 PASS, 2026-08-08).
HIGH reuse — appears in 社/礼/福/祝/神/视/祖/祥. Retry_1 was C due to
oversized right dot + shu too high; R2 recipe: mid-band crossbar +
centered shu with N-gap below crossbar + moderate right dot.

Left-position radical: callers typically embed with `(ox=-30, oy=0,
scale=0.9)` to shift right of canvas center for compound compositions
(this transform is a starting point; drawer may re-anchor per GT).
"""

from PIL import ImageDraw

from dian import draw_dian
from heng_pie import draw_heng_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shi_spirit(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top dian
    draw_dian(draw,
              _tx(131, 66, ox, oy, scale), _tx(163, 92, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(7 * scale)),
              bow=max(2, int(3 * scale)))
    # s2: heng_pie (mid-band crossbar sweeping down-left)
    draw_heng_pie(draw,
                  _tx(85, 148, ox, oy, scale), _tx(60, 245, ox, oy, scale))
    # s3: central shu (below crossbar with N-gap)
    draw_shu(draw,
             _tx(140, 193, ox, oy, scale), _tx(140, 292, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s4: right dian (moderate size, sits below-right of crossbar)
    draw_dian(draw,
              _tx(160, 188, ox, oy, scale), _tx(215, 245, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(7 * scale)),
              bow=max(2, int(4 * scale)))
