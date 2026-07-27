# p3_char_0074_孑 — jié, 3 strokes.
# Similar to 子 but without the horizontal crossbar; the middle 横 is
# replaced by a short rising 提 on the right side.
# MMH stroke decomposition for 孑:
#   1. 横撇 (top): starts left, sweeps right and slightly up, then
#      the RIGHT end drops as a 撇 tail down-and-left.
#   2. 弯钩 (main descender): begins near where the 撇 tail ends
#      (mid-upper), curves down as a soft S, ends with an up-left hook
#      at the bottom.
#   3. 提 (rising short horizontal on the right): rising line from
#      lower-left of the shaft crossing the shaft up to the right edge.
# Revision 1: fixed 横撇 (tail on right, not left), tuned 弯钩 origin
# to sit just below the pie tail, softened 提 slope.

import os
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _var_line(draw, pts, w_start, w_end):
    n = len(pts) - 1
    for i in range(n):
        t0 = i / n if n else 0
        w = max(2, int(round(w_start + (w_end - w_start) * t0)))
        draw.line([pts[i], pts[i + 1]], fill="black", width=w)
    r0 = max(1, w_start // 2)
    x, y = pts[0]
    draw.ellipse([x - r0, y - r0, x + r0, y + r0], fill="black")
    rN = max(1, w_end // 2)
    x, y = pts[-1]
    draw.ellipse([x - rN, y - rN, x + rN, y + rN], fill="black")


def _bez_pts(p0, p1, p2, steps=24):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def _cubic_pts(p0, p1, p2, p3, steps=32):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0]
             + 3 * (1 - u) * u * u * p2[0] + u ** 3 * p3[0])
        y = ((1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1]
             + 3 * (1 - u) * u * u * p2[1] + u ** 3 * p3[1])
        out.append((x, y))
    return out


def draw_jie(draw, ox=0, oy=0, scale=1.0):
    # --- Stroke 1: 横撇 --------------------------------------------------
    # Horizontal portion from left to right, with slight upward tilt.
    h_left = (65 + ox, 88 + oy)
    h_right = (200 + ox, 78 + oy)
    _var_line(draw,
              [h_left, (105 + ox, 85 + oy), (155 + ox, 80 + oy), h_right],
              w_start=5, w_end=10)
    # Pie tail on the RIGHT end: drops down and to the left.
    pie_end = (150 + ox, 130 + oy)
    pie_ctrl1 = (200 + ox, 100 + oy)
    pie_ctrl2 = (175 + ox, 118 + oy)
    pie_pts = _cubic_pts(h_right, pie_ctrl1, pie_ctrl2, pie_end, steps=22)
    _var_line(draw, pie_pts, w_start=10, w_end=3)

    # --- Stroke 2: 弯钩 (curved shaft with up-left hook) ----------------
    # Starts near the tip of the pie tail; runs mostly vertical with a
    # slight belly to the right, ends near bottom-center with hook.
    top = (155 + ox, 118 + oy)
    shaft = _cubic_pts(top,
                       (180 + ox, 165 + oy),
                       (172 + ox, 215 + oy),
                       (155 + ox, 250 + oy),
                       steps=32)
    _var_line(draw, shaft, w_start=9, w_end=10)
    # Hook curling up-left.
    hook_end = (118 + ox, 238 + oy)
    hpts = _bez_pts(shaft[-1], (138 + ox, 252 + oy), hook_end, steps=14)
    _var_line(draw, hpts, w_start=10, w_end=3)

    # --- Stroke 3: 提 --------------------------------------------------
    # Rises from lower-left across the shaft to upper-right.
    ti_start = (95 + ox, 180 + oy)
    ti_end = (235 + ox, 152 + oy)
    _var_line(draw,
              [ti_start,
               (140 + ox, 172 + oy),
               (188 + ox, 160 + oy),
               ti_end],
              w_start=10, w_end=3)


draw_jie(draw)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_孑.png")
img.save(out_path)
print(f"Wrote {out_path}")
