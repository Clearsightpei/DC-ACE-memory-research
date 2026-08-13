# BANK_DEVIATION
# skipped: ren_pang.py, er_ren.py
# reason: bank ren_pang pie sweeps too far left for this narrow L-slot; 儿 needs
#         non-standard extra-long 竖弯钩 sweep to right edge that er_ren doesn't provide.
# fresh_component: mian_avoid_inline (⺈ + 口 + 儿-with-long-sweep) + thin_ren_inline
#
# p3_char_0494_俛 — 俛 = 亻 (left) + 免 (right).
# Inline PIL bezier, thin uniform lines per GT.

import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))


def bezier(pts, steps=60):
    n = len(pts) - 1
    out = []
    for i in range(steps + 1):
        t = i / steps
        if n == 2:
            x = (1 - t) ** 2 * pts[0][0] + 2 * (1 - t) * t * pts[1][0] + t * t * pts[2][0]
            y = (1 - t) ** 2 * pts[0][1] + 2 * (1 - t) * t * pts[1][1] + t * t * pts[2][1]
        elif n == 3:
            x = ((1 - t) ** 3 * pts[0][0] + 3 * (1 - t) ** 2 * t * pts[1][0]
                 + 3 * (1 - t) * t * t * pts[2][0] + t ** 3 * pts[3][0])
            y = ((1 - t) ** 3 * pts[0][1] + 3 * (1 - t) ** 2 * t * pts[1][1]
                 + 3 * (1 - t) * t * t * pts[2][1] + t ** 3 * pts[3][1])
        else:
            x = (1 - t) * pts[0][0] + t * pts[1][0]
            y = (1 - t) * pts[0][1] + t * pts[1][1]
        out.append((x, y))
    return out


def stroke(d, pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    W = 4

    # --- Left: 亻 (person radical) ---
    # Compact pie top-left, then shorter shu (vertical) mid-shaft.
    # Pie: from (95, 60) sweeping down-left to (48, 235).
    pie = bezier([(95, 60), (78, 130), (48, 235)], steps=70)
    stroke(d, pie, w=W)
    # Shu: from (~90, 115) straight down to (90, 265).
    stroke(d, [(90, 115), (90, 265)], w=W)

    # --- Right: 免 inline ---

    # (1) 撇 — short top-left slant (initial dot-like piece of ⺈).
    stroke(d, bezier([(178, 50), (168, 68), (155, 88)], steps=30), w=W)

    # (2) 横撇 — horizontal segment then folding down-left as pie (cap top of 免).
    # Horizontal top:
    stroke(d, [(160, 82), (232, 82)], w=W)
    # Fold down-left as long pie:
    stroke(d, bezier([(232, 82), (218, 115), (168, 155)], steps=50), w=W)

    # (3) 口 (rectangle body): four sides.
    # Left vertical:
    stroke(d, [(165, 148), (165, 200)], w=W)
    # Top horizontal:
    stroke(d, [(165, 148), (225, 148)], w=W)
    # Right vertical (heng-zhe right side):
    stroke(d, [(225, 148), (225, 200)], w=W)
    # Bottom horizontal:
    stroke(d, [(165, 200), (225, 200)], w=W)

    # (4) 撇 — left leg of 儿 (down-left sweep from bottom-left of 口).
    stroke(d, bezier([(170, 200), (155, 235), (128, 278)], steps=50), w=W)

    # (5) 竖弯钩 — right leg from bottom-right of 口, curving down then sweeping
    # far right with small upward hook (distinctive long tail in GT).
    swg = bezier([(220, 200), (222, 240), (245, 270), (280, 262)], steps=80)
    stroke(d, swg, w=W)
    # upward hook tip
    stroke(d, [(280, 262), (278, 250)], w=W)

    out = os.path.join(_HERE, "01_俛.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
