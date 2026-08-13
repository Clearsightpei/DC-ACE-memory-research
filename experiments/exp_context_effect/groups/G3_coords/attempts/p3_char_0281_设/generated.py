# p3_char_0281_设 (shè). L-R compose: 讠 (left, ~30% width) + 殳 (right, ~65%).
# 6 strokes total: 讠 = 点 + 横折提 (2); 殳 = top compound (2) + 又 (2).
# Fresh render with tapered_line/bezier helpers, thin widths per P12.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import to_px, tapered_line, tapered_bezier  # noqa: E402

CANVAS = 300


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # ==================== LEFT: 讠 (yan_pang) ====================
    # Occupies roughly x = -120..-40. Vertical center around y = 0.

    # Stroke 1: 点 (top-left dot). Short diagonal from upper-left to lower-right.
    tapered_line(d, (-110, 80), (-95, 60), 3, 7, n=20)

    # Stroke 2: 横折提 (yan body).
    # Segment A: heng — short horizontal from (-110, 30) → (-55, 30)
    tapered_line(d, (-110, 30), (-55, 30), 5, 5, n=20)
    # Segment B: fold — down-left curve from (-55, 30) → (-100, -45)
    tapered_bezier(d, (-55, 30), (-85, -10), (-100, -45), 5, 4, n=32)
    # Segment C: ti — short lift up-right from (-100, -45) → (-45, -25)
    tapered_line(d, (-100, -45), (-45, -25), 6, 2, n=20)

    # ==================== RIGHT: 殳 (shu) ====================
    # Occupies roughly x = -20..+110. Two-decker: top piece + 又 below.

    # Stroke 3: 撇 (top-left small pie of 殳). Short slanting stroke.
    tapered_bezier(d, (+5, 85), (-10, 65), (-25, 45), 6, 3, n=28)

    # Stroke 4: 横折弯 (top-right compound of 殳): heng then down then small hook.
    tapered_line(d, (-20, 78), (+80, 78), 5, 5, n=22)
    tapered_bezier(d, (+80, 78), (+80, 30), (+55, 18), 5, 4, n=28)

    # Stroke 5: 横撇 of 又 (crossing X). heng then pie down-left.
    # apex/joint at (+40, 10). Pie ends around (-40, -70).
    tapered_line(d, (-30, 10), (+40, 10), 5, 5, n=20)
    APEX = (+40, 10)
    tapered_bezier(d, APEX, (+10, -25), (-40, -70), 5, 3, n=32)

    # Stroke 6: 捺 of 又. Starts from shared joint (+40, 10) sweeping down-right.
    tapered_bezier(d, APEX, (+65, -25), (+110, -85), 4, 11, n=40)

    return img


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_设.png")
    render().save(out)
    print(f"wrote {out}")
