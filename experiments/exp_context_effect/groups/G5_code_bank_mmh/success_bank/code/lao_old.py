"""Bank primitive: 老 (lǎo, "old") — 6 strokes.

Promoted from p3_char_0271_老 R1 (G5 B9 PASS 2026-08-09). VALIDATES
P-A-007 MEDIUM-tuning arm: main FAILed with default shu_wan_gou; R1
tuned bottom_extra=32, knee_ratio=0.72 per queue instruction, PASSed.

MEDIUM-REUSE: 耂-top pattern (老/考/耆/耊/孝). shu_wan_gou at bottom
with tail=241 needs bottom_extra tune to keep knee on-canvas.
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_lao_old(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # --- 耂 top ---
    # s1 short heng
    draw_heng(draw, _tx(94, 118, ox, oy, scale),
              _tx(188, 110, ox, oy, scale),
              width_head=6, width_tail=6)
    # s2 short vertical
    draw_shu(draw, _tx(133, 53, ox, oy, scale),
             _tx(138, 156, ox, oy, scale), width=6)
    # s3 long middle heng
    draw_heng(draw, _tx(28, 178, ox, oy, scale),
              _tx(273, 155, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s4 long pie
    draw_pie(draw, _tx(211, 73, ox, oy, scale),
             _tx(38, 273, ox, oy, scale),
             bow_perp=18, w_head=8, w_tail=3)
    # --- 匕 bottom ---
    # s5 short pie
    draw_pie(draw, _tx(226, 204, ox, oy, scale),
             _tx(140, 234, ox, oy, scale),
             bow_perp=-4, w_head=6, w_tail=3)
    # s6 shu_wan_gou — bottom_extra tuned for on-canvas knee
    draw_shu_wan_gou(draw, _tx(125, 193, ox, oy, scale),
                     _tx(232, 241, ox, oy, scale),
                     width=6, bottom_extra=32, knee_ratio=0.72)
