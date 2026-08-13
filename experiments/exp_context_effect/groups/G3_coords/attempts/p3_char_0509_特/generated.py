# BANK_DEVIATION
# skipped: niu.py (turtle-based; cannot cleanly mix with PIL right side)
# reason: right side uses PIL/pixel tu_cun_stacked_for_LR_right; the L-R
#         compound needs left 牜 rendered in matching PIL pixel style so
#         stroke widths and offsets stay coherent. Bank's niu.py is turtle
#         with hardcoded canvas-center offsets that won't nest into a
#         compressed L-column slot.
# fresh_component: niu_pil_for_LR_left (left-column 牜 variant of 牛,
#         shorter, shu extended slightly, matches PIL width profile)

import os
import sys

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from tu_cun_stacked_for_LR_right import draw_tu_cun_stacked  # noqa: E402

CANVAS = 300
CX = CY = CANVAS // 2


def _to_px(x, y):
    return (CX + x, CY - y)


def _line_stroke(d, p0, p1, w_head, w_tail, n=25):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        cur = (x, y)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r],
                      fill=(0, 0, 0))
        prev = cur


def draw_niu_left(d, x0=-85):
    """牛/牜 left-column variant, 4 strokes:
       1. 撇 top-left descending
       2. 短横 (short) upper, meeting near pie
       3. 长横 (long) middle
       4. 竖 vertical, goes down to bottom (no bottom heng — L-col style)
    """
    # 1. 撇 — starts high near center, descends to lower-left
    _line_stroke(d, _to_px(x0 + 20, 90), _to_px(x0 - 30, 35),
                 w_head=6, w_tail=3, n=25)
    # 2. 短横 — near top, on right of pie
    _line_stroke(d, _to_px(x0 + 5, 60), _to_px(x0 + 50, 60),
                 w_head=4, w_tail=4, n=20)
    # 3. 长横 — middle, wider
    _line_stroke(d, _to_px(x0 - 30, 5), _to_px(x0 + 50, 5),
                 w_head=5, w_tail=5, n=30)
    # 4. 竖 — vertical through center, long, goes to bottom
    _line_stroke(d, _to_px(x0 + 10, 70), _to_px(x0 + 10, -90),
                 w_head=5, w_tail=5, n=35)


def draw():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    # Left 牜
    draw_niu_left(d, x0=-85)
    # Right 寺 — shift right so its shu center at x = 40 + ox lands ~x=+55
    draw_tu_cun_stacked(d, ox=+15)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_特.png")
    img.save(out)
    return out


if __name__ == "__main__":
    print(draw())
