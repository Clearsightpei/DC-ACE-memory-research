"""Bank primitive: 讠 (yan, speech-radical simplified — 2 strokes: dian + heng_zhe_ti).

Promoted from p2_radical_035_讠__retry_2 (G5 B3 R2 PASS 2026-08-08).
VERY HIGH-REUSE left-position radical (说/话/记/让/请/词/许/该/etc. — one of
the top-5 most common Phase-3 radicals).

Reference geometry places 讠 in the LEFT third of a full-width character
(dian near x=95-140, s2 body around x=55-130). When used as sub-component,
scale ~0.60-0.70 and shift right so it occupies just the left ~30% of the
enclosing character.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng_zhe_ti import draw_heng_zhe_ti


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yan_speech(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: dian at upper left
    draw_dian(draw, _tx(95, 55, ox, oy, scale),
              _tx(140, 100, ox, oy, scale),
              w_head=3, w_tail=max(2, int(10 * scale)),
              bow=max(2, int(4 * scale)), steps=48)
    # s2: heng_zhe_ti compound (horizontal + corner + descend + rising ti)
    draw_heng_zhe_ti(draw,
                     head=_tx(55, 140, ox, oy, scale),
                     tail=_tx(130, 232, ox, oy, scale),
                     corner=_tx(116, 154, ox, oy, scale),
                     descend_mid=_tx(95, 195, ox, oy, scale),
                     ti_head=_tx(65, 240, ox, oy, scale),
                     width=max(2, int(6 * scale)))
