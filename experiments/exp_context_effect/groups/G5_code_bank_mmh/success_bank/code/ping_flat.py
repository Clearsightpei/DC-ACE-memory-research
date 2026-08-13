"""Bank primitive: 平 (ping, "flat/even" — 5 strokes:
short-top-heng + dian + pie + long-middle-heng + long-shu).

Promoted from p3_char_0176_平 (G5 B6 PASS, 2026-08-08). Shu tail clamped
to y=298 (canvas edge) — MMH tail was BC(0.474, 1.117) → y=311 out of canvas.

Reuse targets: 评 (讠+平), 坪 (土+平), 苹 (艹+平), 秤 (禾+平).

Signature: (draw, ox=0, oy=0, scale=1.0).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ping(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top short heng
    draw_heng(draw,
              _tx(99, 77, ox, oy, scale), _tx(204, 65, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s2: left small dian
    draw_dian(draw,
              _tx(79, 112, ox, oy, scale), _tx(106, 146, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(7 * scale)), bow=3)
    # s3: right small pie
    draw_pie(draw,
             _tx(202, 94, ox, oy, scale), _tx(175, 144, ox, oy, scale),
             bow_perp=6, w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(3 * scale)))
    # s4: long middle heng (main horizontal beam)
    draw_heng(draw,
              _tx(36, 188, ox, oy, scale), _tx(273, 174, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(12 * scale)))
    # s5: long central shu (clamped to y=298)
    draw_shu(draw,
             _tx(136, 87, ox, oy, scale), _tx(147, 298, ox, oy, scale),
             width=max(2, int(8 * scale)))
