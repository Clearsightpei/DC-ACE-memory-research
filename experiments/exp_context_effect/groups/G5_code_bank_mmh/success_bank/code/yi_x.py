"""Bank primitive: 义 (yi, "righteousness" — 3 strokes: dian + pie + na).

Promoted from p3_char_0089_义__retry_1 (G5 B6, 2026-08-08). **First A verdict from
retry channel** — retry succeeded where B5 main got only C. See B6 postmortem
in sandbox.md and A-recipe extension P-A-005 in principle_bank.md.

A-recipe factors that made this work (missing in main C attempt):
  - dian rendered as proper tapered dot (w_head=3, w_tail=9) at MMH-anchored
    upper-left position (not thin tick drifting to center).
  - pie called with NEGATIVE bow so its mid-belly pushes DOWN-RIGHT toward BC
    (crossing anchor with na), instead of straight diagonal that misses cross.
  - na called with positive bow + strong tail-thickening (w_head=4, w_tail=12),
    mid-belly meets pie near BC anchor → welded crossing.

Signature: (draw, ox=0, oy=0, scale=1.0). Baked from MMH anchors on 300×300.

Reuse targets: 仪 (人+义), 议 (讠+义), 艺 (艹+乙+义-derivative);
also composition base for L-R chars with 义 as right radical.
"""

from PIL import ImageDraw

from dian import draw_dian
from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yi_x(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: dian (upper-left, tapered down-right)
    draw_dian(draw,
              _tx(97.6, 109.9, ox, oy, scale),
              _tx(132.1, 138.0, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(9 * scale)),
              bow=3)
    # s2: pie (upper-right → lower-left), NEGATIVE bow to force cross at BC
    draw_pie(draw,
             _tx(172.3, 101.7, ox, oy, scale),
             _tx(41.6, 284.2, ox, oy, scale),
             bow_perp=-45,
             w_head=max(2, int(10 * scale)),
             w_tail=max(2, int(3 * scale)),
             steps=80)
    # s3: na (middle-left → lower-right), positive bow, strong tail-thickening
    draw_na(draw,
            _tx(71.2, 163.5, ox, oy, scale),
            _tx(278.0, 291.2, ox, oy, scale),
            bow_perp=20,
            w_head=max(2, int(4 * scale)),
            w_tail=max(2, int(12 * scale)),
            steps=80)
