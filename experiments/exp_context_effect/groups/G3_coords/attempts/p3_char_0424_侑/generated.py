# BANK_DEVIATION
# skipped: you_have.py
# reason: draw_you_have has baked pixel coords for a centered full-canvas 有;
#         for 侑 (L-R) the 有 must compress into the right ~60% of canvas,
#         so I inline a shifted/scaled 有 recipe using the same yue bank.
# fresh_component: you_have_for_LR_right

# 侑 (yòu) — 亻 (left) + 有 (right). 8 strokes.
# Left: bank ren_pang (compressed).
# Right (有): inline top-横 + long 撇 + draw_yue tucked in crook.

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from yue import draw_yue, _tapered_line, _tapered_bezier  # noqa: E402


def draw_you_have_right(D):
    """Inline 有, positioned in the right ~60% of the 300x300 canvas."""
    # 1) top 横 — spans right side, slight up-slant to the right
    _tapered_line(D, (118, 102), (280, 90),
                  w0=6, w1=8, steps=28)
    D.ellipse([114, 98, 124, 108], fill=(0, 0, 0))
    D.ellipse([275, 86, 285, 96], fill=(0, 0, 0))

    # 2) long 撇 — starts near top-right of the heng, sweeps down-left
    p0 = (208, 70)
    p2 = (118, 275)
    ctrl = (165, 195)  # bow toward left
    _tapered_bezier(D, p0, ctrl, p2,
                    w0=10, w1=2, steps=64)
    D.ellipse([204, 66, 214, 76], fill=(0, 0, 0))

    # 3) 月 tucked inside the crook — small, right-bottom
    # draw_yue base is centered on (150,150); shift right ~65, down ~45,
    # scale 0.52 to fit compactly inside the crook.
    draw_yue(D, ox=65, oy=45, scale=0.52)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)

    # 亻 on left — smaller/compact so it stays in left ~30% of canvas.
    draw_ren_pang(D, ox=-70.0, oy=0.0, scale=0.70)

    # 有 on right — inlined (see BANK_DEVIATION note above).
    draw_you_have_right(D)

    out = os.path.join(os.path.dirname(__file__), "01_侑.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
