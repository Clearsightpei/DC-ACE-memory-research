# 有 (yǒu, "have"), 6 strokes.
# Structure: 𠂇 (top 横 + long 撇) on the outside; 月 tucked inside the crook.
# Reference: yue.py (draw_yue) for the inner 月; top 横 + long 撇 inline.

import sys, os
BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from yue import draw_yue, _tapered_line, _tapered_bezier


def draw_you_have(D):
    # 1) Top 横 — spans across the character, slight upward slant to the right
    _tapered_line(D, (48, 92), (232, 78),
                  w0=6, w1=8, steps=28)
    # small starter cap
    D.ellipse([44, 88, 55, 98], fill=(0, 0, 0))
    # ending accent
    D.ellipse([227, 74, 237, 84], fill=(0, 0, 0))

    # 2) Long 撇 — starts near the top-right of the heng, sweeps down-left
    p0 = (155, 55)
    p2 = (35, 275)
    ctrl = (120, 180)  # bow toward left
    _tapered_bezier(D, p0, ctrl, p2,
                    w0=11, w1=2, steps=64)
    D.ellipse([151, 51, 162, 62], fill=(0, 0, 0))

    # 3) 月 tucked inside the crook — small, right-bottom
    # yue.py base is centered on (150, 150) with X_TOP_LEFT=128, X_RIGHT=200,
    # Y_TOP=55, Y_HOOK=250. We want the 月 to sit at ~x_center=170, y_center=180
    # and be a bit smaller (scale 0.65).
    draw_yue(D, ox=20, oy=32, scale=0.62)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_you_have(D)
    out = os.path.join(
        os.path.dirname(__file__), "01_有.png"
    )
    img.save(out)
    print("wrote", out)
