# BANK_DEVIATION
# skipped: tou_radical.py, kou.py
# reason: 高 needs a very small top-口 (~40% width) and a wide bottom 冂-frame
#   enclosing another 口; bank primitives are sized for standalone use and
#   don't compose cleanly into 高's 3-tier vertical stack at these proportions.
# fresh_component: gao_char_inline (亠 + small_kou + 冋-frame with inner_kou)
#
# 高 (gao, "tall") — 10 strokes.
# Layout (top→bottom, PIL pixel coords, top-left origin):
#   1) 点 (dot) — top center
#   2) 一 (heng lid) — wide, below dot
#   3-5) 口 (small mouth, upper middle)
#   6) 冂 left 竖
#   7) 冂 top-right 横折钩 (with small hook)
#   8-10) inner 口 (bottom)

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_高.png")


def _line(draw, pts, w=4):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)


def _bez(p0, p1, p2, steps=24):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def draw_gao(draw):
    W = 4

    # --- 1) 点 (dot) — small tilted stroke, top center, clearly above lid ---
    dot_pts = _bez((150, 18), (154, 30), (161, 42), 12)
    _line(draw, dot_pts, W + 1)

    # --- 2) 一 (heng lid) — wide horizontal below dot ---
    _line(draw, [(55, 62), (245, 60)], W)

    # --- 3-5) small 口 (upper mouth), sits between lid and frame ---
    # left shu
    _line(draw, [(112, 78), (112, 118)], W)
    # top+right 横折 (with tiny corner)
    _line(draw, [(112, 78), (188, 78), (188, 118)], W)
    # bottom heng
    _line(draw, [(112, 118), (188, 118)], W)

    # --- 6) 冂 left 竖 (long left vertical of frame) ---
    _line(draw, [(62, 138), (62, 272)], W)

    # --- 7) 冂 top-right 横折钩 ---
    # top heng
    _line(draw, [(62, 138), (238, 136)], W)
    # right shu going down
    _line(draw, [(238, 136), (240, 262)], W)
    # small hook at bottom-right (kicking left, more pronounced)
    hook_pts = _bez((240, 262), (228, 270), (212, 265), 12)
    _line(draw, hook_pts, W)

    # --- 8-10) inner 口 (bottom mouth) ---
    # left shu
    _line(draw, [(95, 178), (95, 244)], W)
    # top+right 横折
    _line(draw, [(95, 178), (205, 178), (205, 244)], W)
    # bottom heng
    _line(draw, [(95, 244), (205, 244)], W)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_gao(draw)
    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
