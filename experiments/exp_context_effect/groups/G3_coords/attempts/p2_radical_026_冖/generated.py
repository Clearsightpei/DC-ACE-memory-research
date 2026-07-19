# p2_radical_026_冖 — 秃宝盖 (bald cover)
#
# Composition: a small 点 (left dot) + a 横钩 (horizontal top-bar ending
# in a short downward-left hook at the right end).
#
# GT observation (300x300):
#   - Small pie-shaped dot near (95, 115) sloping down-right, tail ~(105, 130).
#   - Horizontal bar from ~(105, 120) to ~(230, 120), thin and lightly
#     curved (very slightly bowed upward mid-bar).
#   - Hook flicks down-left from right end ~(230, 120) ending near (215, 155).
#   - Whole radical sits in the upper-middle of the canvas (~y=110–160).
#
# TR-compliance notes:
#   - The bank's heng_gou primitive gave TOO-heavy widths (13 px + 9 px blob)
#     for a small radical use; on the first render it dominated the canvas.
#   - TR5 says: if a primitive doesn't fit the composition without extreme
#     transforms, INLINE the recipe. Widths are hard-coded in heng_gou, not
#     scale-friendly for a radical usage, so I inline a thinner variant here.
#   - The 点 primitive scales cleanly — reuse it via draw_dian with a
#     shrink-and-shift transform.

import os
import sys
from PIL import Image, ImageDraw

# Make success_bank/code importable for the 点 primitive
BANK_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "success_bank", "code",
)
sys.path.insert(0, BANK_DIR)

from dian import draw_dian  # noqa: E402


def draw_inlined_henggou(draw, x0, y0, x1, y1, w_start=6, w_end=9,
                        hook_dx=-16, hook_dy=30, blob_r=6, hook_w_start=9):
    """Inlined 横钩: horizontal tapered bar from (x0,y0) to (x1,y1),
    顿笔 blob at right end, hook flicking down-left to (x1+hook_dx, y1+hook_dy).
    Thinner than the bank primitive — sized for a radical, not a stroke study.
    """
    steps = 24
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = int(w_start + (w_end - w_start) * t0)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=max(1, w))

    # 顿笔 blob at right end
    draw.ellipse([x1 - blob_r, y1 - blob_r, x1 + blob_r, y1 + blob_r], fill="black")

    # Hook: short tapered line from just past the blob, angling down-left
    hx0 = x1 + 1
    hy0 = y1 + 1
    hx1 = x1 + hook_dx
    hy1 = y1 + hook_dy
    hsteps = 14
    for i in range(hsteps):
        t0 = i / hsteps
        t1 = (i + 1) / hsteps
        xa = hx0 + (hx1 - hx0) * t0
        ya = hy0 + (hy1 - hy0) * t0
        xb = hx0 + (hx1 - hx0) * t1
        yb = hy0 + (hy1 - hy0) * t1
        w = max(1, int(hook_w_start - (hook_w_start - 1) * t0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)


def main():
    W = H = 300
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: 点 (small dot at upper-left) ---
    # 点 primitive: math coords (canvas center = (150,150) in PIL); head at
    # (-15,+25)*scale, tail at (+18,-20)*scale.
    # Target dot: head PIL (95,110), tail PIL (110,130). Center ~ (100,120).
    # With scale=0.5: head at (-7.5,+12.5) math -> PIL (142.5,137.5) relative
    #   to nothing; tail at (+9,-10) math -> (159,160).
    #   Default center of dot (avg endpoints) = (150.75, 148.75) in PIL.
    # We want center at (100, 120). So:
    #   ox_math = 100 - 150 = -50
    #   oy_math = 150 - 120 = +30
    # scale=0.5 → head ends up at approximately (150-50-7.5, 150-30-12.5)? Let me
    # recompute properly: head_math_final = (ox+(-15*scale), oy+(25*scale))
    #   = (-50-7.5, 30+12.5) = (-57.5, 42.5) math -> PIL (92.5, 107.5). Good.
    # tail_math_final = (-50+9, 30-10) = (-41, 20) math -> PIL (109, 130). Good.
    draw_dian(draw, ox=-50, oy=30, scale=0.5)

    # --- Stroke 2: 横钩 (inlined — thin bar + short hook) ---
    # Bar from (108, 120) to (230, 120), then hook down-left to ~(216, 152).
    # Slight downward slope (2 px) to feel 横-like.
    # Widths: 6 -> 9 (thinner than the bank primitive which is 9->13).
    draw_inlined_henggou(
        draw,
        x0=108, y0=118,
        x1=230, y1=122,
        w_start=6, w_end=9,
        hook_dx=-14, hook_dy=30,
        blob_r=6, hook_w_start=9,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_冖.png")
    img.save(out)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
