# p3_char_0488_俑 — 俑 (yǒng, "figurine")
# Structure: 亻 (left) + 甬 (right). 甬 = 龴 (top hat) + 用.
# Recipe: base off yong_char (亻 + 用). Shrink 用 and push it down;
# add a 龴 hat above (a 横撇 stroke sweeping right-to-left-down + a small
# starter 点 at the top). Bank primitives used as-is (no BANK_DEVIATION).

import os
import sys
from PIL import Image, ImageDraw

_BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from yong_use import draw_yong  # noqa: E402


def _tapered_line(draw, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_yong_char(D, ox=0, oy=0, scale=1.0):
    """俑 = 亻 + 甬. 甬 = 龴 hat + 用 (shrunken, pushed down)."""
    # 亻 on left — mirrors yong_char recipe, keep essentially same
    draw_ren_pang(D, ox=ox + (-65) * scale, oy=oy + 20 * scale,
                  scale=0.78 * scale)

    # 用 on right — shrunk and pushed down to leave room for the 龴 hat
    # bank draw_yong is centered at (150,150) w/ scale-about-center
    draw_yong(D, ox=ox + 45, oy=oy + 25, scale=0.60 * scale)

    # 龴 hat above 用. Two strokes forming a proper 横撇 + 点:
    # (a) main 横撇: short 横 going right, then turning down-left as 撇
    # (b) small 点 sitting on top of the 横撇's corner
    # 用 top edge after transform ~ y = 121; spans roughly x ∈ [130, 213].
    Y_HAT_TOP = 85
    Y_CORNER = 92
    Y_HAT_BOT = 120
    X_HAT_L = 135
    X_CORNER = 200
    X_HAT_R = 210

    # (a1) 横 part — short horizontal near the top-right of hat
    _tapered_line(D, (X_CORNER - 40, Y_HAT_TOP + 3),
                  (X_CORNER, Y_CORNER),
                  w0=int(6 * scale), w1=int(9 * scale), steps=18)
    # corner dot at the fold
    D.ellipse([X_CORNER - 5, Y_CORNER - 5, X_CORNER + 5, Y_CORNER + 5],
              fill=(0, 0, 0))
    # (a2) 撇 part — from corner down-and-left toward 用's top-left
    _tapered_line(D, (X_CORNER, Y_CORNER),
                  (X_HAT_L - 2, Y_HAT_BOT + 2),
                  w0=int(9 * scale), w1=max(1, int(3 * scale)), steps=24)

    # (b) small starter 点 at very top-right of the hat
    _tapered_line(D, (X_HAT_R - 4, Y_HAT_TOP - 8),
                  (X_HAT_R + 3, Y_HAT_TOP + 2),
                  w0=int(3 * scale), w1=int(7 * scale), steps=8)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_yong_char(D)
    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0488_俑/01_俑.png"
    img.save(out)
    print("saved", out)
