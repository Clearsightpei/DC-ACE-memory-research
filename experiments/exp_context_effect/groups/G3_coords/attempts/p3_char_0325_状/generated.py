"""
p3_char_0325_状 (zhuàng) — G3 attempt 1

Decomposition (from GT):
  - LEFT: 丬 (piece-left, ~3 strokes): short 点/pie top-left; short 提
    (rising tick) mid-left; long vertical 竖 down the shaft.
  - RIGHT: 犬 (dog) = 大 + 丶(dot) at upper-right.

Recipe:
  - Use bank #201 da_char as template for the RIGHT-side 大 (shifted
    right, moderately scaled). REJECT kiss_apex (per da_char lesson).
    Draw 犬's extra 丶 as a canonical upper-right leaning dot.
  - Draw 丬 inline as three thin strokes (P12 MMH weight).
Thin ~4px ink throughout to match MMH GT weight.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(points, w_head=4.5, w_tail=3.5):
    if len(points) < 2:
        return
    seg_len, total = [], 0.0
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        d = math.hypot(dx, dy)
        seg_len.append(d)
        total += d
    covered = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        L = seg_len[i]
        if L <= 0:
            continue
        steps = max(2, int(L * 2))
        for s in range(steps + 1):
            u_local = s / steps
            u_global = (covered + u_local * L) / max(1e-6, total)
            w = w_head * (1 - u_global) + w_tail * u_global
            x = x0 + (x1 - x0) * u_local
            y = y0 + (y1 - y0) * u_local
            _stamp(x, y, w / 2)
        covered += L


def cubic_pts(p0, p1, p2, p3, steps=80):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0]
             + 3 * (1 - u) * u ** 2 * p2[0] + u ** 3 * p3[0])
        y = ((1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1]
             + 3 * (1 - u) * u ** 2 * p2[1] + u ** 3 * p3[1])
        out.append((x, y))
    return out


# =========== LEFT SIDE: 丬 ===========
# Short pie/点 top-left (rises above shaft, curves down-left)
pie_top = [(85, 55), (80, 75), (68, 100)]
tapered_polyline(pie_top, w_head=4.5, w_tail=3.0)

# 提 (rising tick): from lower-left to upper-right, meets shaft
ti_seg = [(45, 175), (75, 165), (100, 152)]
tapered_polyline(ti_seg, w_head=5.0, w_tail=2.5)

# 竖 (long vertical shaft) — dominant left stroke, thin & straight
shu_seg = [(100, 60), (100, 275)]
tapered_polyline(shu_seg, w_head=4.0, w_tail=4.0)


# =========== RIGHT SIDE: 犬 (大 + dot) ===========
# Adapted from bank #201 da_char, shifted right, mildly compressed.
# Heng runs across the right half, slight up-tilt.
heng_left = (130, 158)
heng_right = (270, 148)
cross = (185, 152)  # pie/heng crossing pixel

# Pie: continuous curve, top above heng at (~185, 60), through cross,
# down to lower-left of the right half. Keep tail INSIDE right half
# (do not crowd 丬 shu). Reduce top-hook curl.
pie_top_start = (188, 62)
pie_head_ctrl = (192, 82)
pie_neck      = (184, 120)
pie_tail_ctrl = (165, 215)
pie_tail_end  = (150, 268)

# Na: separate stroke, starts at crossing, sweeps to lower-right.
na_head  = (cross[0] + 2, cross[1] + 2)
na_ctrl1 = (215, 205)
na_ctrl2 = (255, 245)
na_tail  = (280, 270)

# Render heng
tapered_polyline([heng_left, (198, 152), heng_right],
                 w_head=3.5, w_tail=4.0)

# Render pie in two arcs
seg_head = cubic_pts(pie_top_start, pie_head_ctrl,
                     (190, 108), pie_neck, steps=40)
seg_body = cubic_pts(pie_neck, (178, 150), pie_tail_ctrl,
                     pie_tail_end, steps=80)
tapered_polyline(seg_head, w_head=3.5, w_tail=4.3)
tapered_polyline(seg_body, w_head=4.3, w_tail=2.2)

# Render na
na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
tapered_polyline(na_seg, w_head=3.2, w_tail=4.6)

# Extra dot 丶 for 犬 — upper-right area, leaning down-right
dot_seg = [(238, 95), (252, 118)]
tapered_polyline(dot_seg, w_head=3.0, w_tail=5.5)


out_path = ("/Users/peilinwu/Documents/AI memory research/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0325_状/01_状.png")
img.save(out_path)
print(f"wrote {out_path}")
