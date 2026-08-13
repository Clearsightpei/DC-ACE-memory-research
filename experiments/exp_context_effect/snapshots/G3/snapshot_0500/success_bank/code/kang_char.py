# p3_char_0250_伉 (kàng) — 亻 (left) + 亢 (right = 亠 top + 几 bottom).
# Approach: reuse zhang_ren's tall-亻 recipe for the left; on the right compose
# tou_radical (亠) placed above draw_ji (几), similar to how 亢 decomposes.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402
from ji import draw_ji  # noqa: E402
from tou_radical import draw_tou_radical  # noqa: E402


_CANVAS = 300


def _to_pixel(mx, my, canvas=_CANVAS):
    return canvas / 2 + mx, canvas / 2 - my


def _draw_tall_ren_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """亻 tuned for compound-character composition — tall shu."""
    draw_pie(t, ox=ox + (-8) * scale, oy=oy + 25 * scale, scale=0.85 * scale)
    top_x, top_y = _to_pixel(ox + 5 * scale, oy + 30 * scale)
    bot_x, bot_y = _to_pixel(ox + 5 * scale, oy + (-85) * scale)
    thickness = max(1, int(round(9 * scale)))
    t.line([(top_x, top_y), (bot_x, bot_y)], fill=(0, 0, 0), width=thickness)


def draw_kang_char(t, ox=0.0, oy=0.0, scale=1.0):
    """伉 = 亻 (left) + 亢 (right, where 亢 = 亠 above + 几 below)."""
    # Left: 亻 — compact so it sits within character height
    _draw_tall_ren_pang(t, ox=ox - 75.0 * scale, oy=oy + 5.0 * scale, scale=0.85 * scale)

    # Right side: 亢 = 亠 + 几
    # 几 sits in the lower/middle of the right slot
    draw_ji(t, ox=ox + 35.0 * scale, oy=oy - 30.0 * scale, scale=0.85 * scale)

    # 亠 on top of the 几 — dian + heng lid
    draw_tou_radical(t, ox=ox + 35.0 * scale, oy=oy + 60.0 * scale, scale=0.80 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_kang_char(t)
    out_path = os.path.join(os.path.dirname(__file__), "01_伉.png")
    img.save(out_path)
    print(f"wrote {out_path}")
