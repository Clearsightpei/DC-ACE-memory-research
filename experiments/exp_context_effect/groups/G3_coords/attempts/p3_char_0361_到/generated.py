# p3_char_0361_到 (dào, "to arrive") — 8 strokes.
# Structure: 至 (left, 6 strokes) + 刂 (right, 2 strokes).
#
# Left 至 breakdown (top→bottom):
#   1. top 横 — spans upper part of left half
#   2. 撇折 (short pie folding down-right, forming 厶 upper stroke)
#   3. 点 (small dot to the right of the fold)
#   4. middle 横 (top heng of 土)
#   5. 竖 (of 土)
#   6. bottom 横 (widest heng at base)
#
# Right 刂 breakdown:
#   7. short 竖 (upper right)
#   8. long 竖钩 (tall vertical with a small hook at bottom-left)
#
# Rendering approach: thin uniform lines matching GT (main-curriculum
# PNG shows ~3-5px strokes). Direct PIL for clarity — the composition
# is left(至)+right(刂) with 至 not being a mastered bank primitive.
# 刂 bank exists (dao_pang.py) but its turtle-based signature and
# scaling don't compose cleanly with the PIL-inline 至 half; using
# a PIL inline for 刂 too, patterned on yi_mow.py's right half.

import os
from PIL import Image, ImageDraw


def _tapered_line(draw, p0, p1, w0, w1, steps=32):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _dot(draw, cx, cy, r=4):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))


def draw_dao(draw):
    # ---- LEFT: 至 ----
    # 1. top 横 — slight rightward-tilt possible; keep flat
    _tapered_line(draw, (45, 62), (170, 60), 4, 4, steps=40)

    # 2. 撇折 — compact ㄙ-like shape. Pie down-left then short right fold.
    _tapered_line(draw, (102, 72), (75, 112), 4, 3, steps=24)
    _tapered_line(draw, (75, 112), (118, 118), 4, 4, steps=20)

    # 3. 点 — small dot near the right/top of the fold zone
    _dot(draw, 132, 95, r=5)

    # 4. middle 横 (top of 土)
    _tapered_line(draw, (60, 145), (162, 145), 4, 4, steps=36)

    # 5. 竖 of 土 — passes through bottom heng
    _tapered_line(draw, (112, 145), (112, 228), 4, 4, steps=32)

    # 6. bottom 横 — widest, longer than the top hengs
    _tapered_line(draw, (25, 228), (185, 228), 4, 5, steps=52)

    # ---- RIGHT: 刂 ----
    # 7. short 竖 — upper right
    _tapered_line(draw, (207, 82), (207, 165), 3, 4, steps=28)

    # 8. long 竖钩 — tall vertical with hook flick at bottom-left
    _tapered_line(draw, (258, 55), (252, 255), 4, 4, steps=42)
    # hook: from bottom, flick to lower-left
    _tapered_line(draw, (252, 255), (232, 245), 4, 1, steps=14)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_dao(draw)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_到.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
