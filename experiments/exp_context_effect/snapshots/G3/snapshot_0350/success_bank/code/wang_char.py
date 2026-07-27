# wang_char.py — 亡 (wáng), 3 strokes: dian (top-right) + long 横 + inline 竖折.
# PASSed at p3_char_0052_亡 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402


def draw_wang_char(t, ox=0, oy=0, scale=1.0):
    draw_dian(t, ox=ox + 10 * scale, oy=oy + 65 * scale, scale=0.55 * scale)
    draw_heng(t, ox=ox + 0, oy=oy + 20 * scale, scale=1.15 * scale)
    # Inline 竖折 sized to 亡 proportions.
    ink = max(2, int(round(10 * scale)))

    def P(mx, my):
        return (150 + ox + mx * scale, 150 - oy - my * scale)
    x_left, y_top, y_bot, x_right = -95, 15, -95, 95
    t.line([P(x_left, y_top), P(x_left, y_bot)], fill=(0, 0, 0), width=ink)
    t.line([P(x_left, y_bot), P(x_right, y_bot)], fill=(0, 0, 0), width=ink)
    r = ink // 2 + 1
    for pt in [(x_left, y_bot), (x_left, y_top), (x_right, y_bot)]:
        cx, cy = P(*pt)
        t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
