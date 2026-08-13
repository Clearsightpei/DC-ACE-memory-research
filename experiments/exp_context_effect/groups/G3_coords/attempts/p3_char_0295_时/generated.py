# p3_char_0295_时 — 时 (shí), L-R compose: 日 (left) + 寸 (right).
# 6 strokes total: 4 for 日, 3 for 寸 = 7 (但 the middle heng of 日
# is small, so it reads as 7). Following the `dui_char` pattern:
# right component (寸) uses bank primitive draw_cun; left component
# (日) inlined fresh because ri.py's scale doesn't shrink positions.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from cun import draw_cun   # noqa: E402


CANVAS = 300


def draw_ri_left(t):
    """Inline 日 on the LEFT — narrow tall rectangle, 4 strokes."""
    x_left = 45
    x_right = 115
    y_top = 70
    y_bot = 235
    y_mid = 155
    w = 8
    w_mid = 6
    # Stroke 1: left 竖
    t.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top heng + right shu)
    t.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    t.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 横 (small gap at right)
    t.line([(x_left + 2, y_mid), (x_right - 4, y_mid)],
           fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom 横
    t.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # 日 on the LEFT (inline fresh, narrow-tall rectangle)
    draw_ri_left(t)

    # 寸 on the RIGHT. NOTE: draw_cun uses math-coord (+y UP), so a
    # positive oy raises the heng. GT places the 一 near the top of 日
    # (~y_pixel=80 => oy = 150-80 = +70) with the 亅 extending well
    # below 日's bottom.
    draw_cun(t, ox=+55, oy=+55, scale=0.85)

    return img


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_时.png")
    render().save(out)
    print(f"wrote {out}")
