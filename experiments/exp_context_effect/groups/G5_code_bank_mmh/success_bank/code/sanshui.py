"""Bank primitive: 氵 (sanshui, "three-water" left-radical — 3 strokes: dian + dian + ti).

Promoted from p2_radical_069_氵 (G5 B2 PASS 2026-08-08). VERY HIGH-REUSE:
appears in 河/海/江/清/游/汉/洗/汽/... (arguably the single most-frequent
left-radical). Ends with a rising ti that welds into the character body.
"""

from PIL import ImageDraw

from dian import draw_dian
from ti import draw_ti


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_sanshui(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 — top dian: head (119.5, 77.1) → tail (162.9, 110.4)
    draw_dian(draw, _tx(119.5, 77.1, ox, oy, scale),
              _tx(162.9, 110.4, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(9 * scale)),
              bow=max(2, int(4 * scale)))
    # s2 — middle dian: head (92.9, 139.5) → tail (131.2, 168.8)
    draw_dian(draw, _tx(92.9, 139.5, ox, oy, scale),
              _tx(131.2, 168.8, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(9 * scale)),
              bow=max(2, int(4 * scale)))
    # s3 — bottom ti: head (116.6, 294.4) → tail (174.3, 190.1)
    draw_ti(draw, _tx(116.6, 294.4, ox, oy, scale),
            _tx(174.3, 190.1, ox, oy, scale),
            w_head=max(3, int(10 * scale)),
            w_tail=max(1, int(2 * scale)))
