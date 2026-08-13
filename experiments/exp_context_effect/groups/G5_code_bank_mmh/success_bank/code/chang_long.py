"""Bank primitive: 长 (chang, 'long' — 4 strokes: pie(top-right) + heng +
shu-ti(left) + na).

Promoted from p2_radical_088_长__retry_2 (G5 B4 R2 PASS, 2026-08-08).
HIGH reuse — 长 appears in 张/帐/涨/胀/账. The R2 recipe uses PIL
polylines directly for the 竖提 (compound s3 with rising hook) — no
bank primitive covers 竖提 cleanly.

Retry_2 fixed both main and retry_1 FAIL modes:
  - slimmer strokes (~7-8 px, not 15)
  - long wide horizontal
  - proper 竖提 with rising up-right flick at bottom
  - na starting inside the vertical, sweeping to BR
"""

from PIL import ImageDraw


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_chang_long(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    w_stroke = max(2, int(8 * scale))
    black = (0, 0, 0)

    # s1: pie (top-right → center)
    p1 = [_tx(198, 60, ox, oy, scale),
          _tx(172, 92, ox, oy, scale),
          _tx(150, 128, ox, oy, scale)]
    draw.line(p1, fill=black, width=w_stroke, joint='curve')

    # s2: long horizontal (mid-band)
    p2 = [_tx(32, 168, ox, oy, scale),
          _tx(150, 160, ox, oy, scale),
          _tx(272, 155, ox, oy, scale)]
    draw.line(p2, fill=black, width=w_stroke, joint='curve')

    # s3: 竖提 (left vertical with rising hook at bottom)
    p3 = [_tx(100, 52, ox, oy, scale),
          _tx(105, 130, ox, oy, scale),
          _tx(110, 205, ox, oy, scale),
          _tx(118, 245, ox, oy, scale),
          _tx(170, 218, ox, oy, scale)]
    draw.line(p3, fill=black, width=w_stroke, joint='curve')

    # s4: na (from inner-mid down to BR)
    p4 = [_tx(112, 160, ox, oy, scale),
          _tx(165, 195, ox, oy, scale),
          _tx(215, 225, ox, oy, scale),
          _tx(268, 252, ox, oy, scale)]
    draw.line(p4, fill=black, width=max(2, int(9 * scale)), joint='curve')
    # taper tail
    draw.line([_tx(268, 252, ox, oy, scale), _tx(282, 256, ox, oy, scale)],
              fill=black, width=max(2, int(4 * scale)))
