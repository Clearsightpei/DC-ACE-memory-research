"""Bank primitive: 宀 (mian, "roof" — 3 strokes: dian + dian + heng_zhe_short).

Promoted from p2_radical_060_宀__retry_2 (G5 B3 R2 PASS 2026-08-08).
VERY HIGH-REUSE top-position radical (家/字/客/它/宝/守/宁/宗/etc. — top-5
Phase-3 radical).

Retry_2 recipe: call bank draw_mi_cover (冖) for the left dian + roof
combined (they must be aligned!), then add a top dian above center.
This avoids the "scattered marks" defect of retry_1.
"""

from PIL import ImageDraw

from dian import draw_dian
from mi_cover import draw_mi_cover


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_mian_roof(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top center dian (compact tick)
    draw_dian(draw, _tx(140.0, 88.0, ox, oy, scale),
              _tx(162.0, 110.0, ox, oy, scale),
              w_head=3, w_tail=max(2, int(7 * scale)),
              bow=max(2, int(2 * scale)))
    # s2+s3: 冖 with a downshift so top dian has room above
    # Use draw_mi_cover directly (which composes left-dian + heng_zhe_short)
    draw_mi_cover(draw, ox=ox, oy=oy + 38.0 * scale, scale=1.02 * scale)
