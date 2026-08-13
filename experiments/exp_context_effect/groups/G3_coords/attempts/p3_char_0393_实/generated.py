# BANK_DEVIATION
# skipped: bao_gai_tou.py + da_char.py
# reason: bao_gai_tou mixes math-coord and raw-PIL-coord subprimitives and does not scale/shift consistently, and da_char.py is a module-level script hard-coded to full-canvas 大. Both need clean compression into the top/bottom halves of 实 with consistent PIL coords.
# fresh_component: mian_top_for_shi + da_bottom_for_shi
#
# 实 = 宀 (roof, top ~y=30-105) + 头-body (5 strokes)
#   Strokes (8 total):
#     1. 点 chimney dot on 宀
#     2. 横钩 roof of 宀
#     3. short left slash of 宀
#     4. 丶 left dot below roof
#     5. 丿 short right slash / dot
#     6. 一 main heng
#     7. 丿 continuous pie (above heng -> through crossing -> lower-left)
#     8. 乀 separate na (from crossing -> lower-right)
# Thin (~4-5 px) MMH weight per P12.

import os, math
from PIL import Image, ImageDraw

W, H = 300, 300


def _stamp(dr, x, y, r):
    dr.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(dr, points, w_head=4.5, w_tail=3.5):
    if len(points) < 2:
        return
    seg_len = []
    total = 0.0
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
            _stamp(dr, x, y, w / 2)
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


def draw_mian_top(dr):
    """宀 roof: chimney dot + horizontal-with-hook + left short slash."""
    # S1: chimney dot (short down-right stroke) at top
    seg = cubic_pts((146, 32), (150, 38), (154, 46), (158, 54), steps=20)
    tapered_polyline(dr, seg, w_head=3.5, w_tail=5.5)

    # S2: 横钩 roof — horizontal from left to right, then hook down-left at right end
    heng_left = (58, 82)
    heng_right = (238, 86)
    tapered_polyline(dr, [heng_left, (148, 84), heng_right],
                     w_head=3.8, w_tail=4.8)
    # hook: from right-end down and slightly left
    hook_pts = cubic_pts((238, 86), (236, 92), (232, 100), (226, 108),
                         steps=25)
    tapered_polyline(dr, hook_pts, w_head=4.5, w_tail=2.0)

    # S3: left short slash — down-right from roof-left area
    seg = cubic_pts((62, 78), (60, 88), (58, 100), (56, 112), steps=25)
    tapered_polyline(dr, seg, w_head=3.5, w_tail=4.5)


def draw_head_body(dr):
    """头-body: two small strokes + heng + pie + na."""
    # S4: left dot (丶) inside/below roof
    seg = cubic_pts((100, 126), (105, 134), (112, 142), (118, 148),
                    steps=20)
    tapered_polyline(dr, seg, w_head=3.0, w_tail=5.5)

    # S5: right short slanted stroke (like small 丿)
    seg = cubic_pts((202, 122), (198, 132), (192, 142), (184, 152),
                    steps=25)
    tapered_polyline(dr, seg, w_head=4.0, w_tail=2.8)

    # S6: main heng across middle-lower
    heng_left = (52, 185)
    heng_right = (248, 178)  # slight up-tilt
    tapered_polyline(dr, [heng_left, (150, 182), heng_right],
                     w_head=3.8, w_tail=4.8)

    # S7: pie — continuous curve, starts above heng, passes through
    # heng-midpoint crossing, sweeps to lower-left.
    cross = (156, 181)
    pie_top_start = (162, 152)
    pie_neck = (158, 175)
    pie_tail_ctrl = (100, 245)
    pie_tail_end = (62, 288)
    seg_head = cubic_pts(pie_top_start, (166, 160),
                         (160, 172), pie_neck, steps=30)
    seg_body = cubic_pts(pie_neck, (148, 200), pie_tail_ctrl,
                         pie_tail_end, steps=80)
    tapered_polyline(dr, seg_head, w_head=3.5, w_tail=4.5)
    tapered_polyline(dr, seg_body, w_head=4.5, w_tail=2.2)

    # S8: na — separate stroke starting at pie/heng crossing,
    # sweeping to lower-right.
    na_head = (cross[0] + 2, cross[1] + 2)
    na_ctrl1 = (190, 220)
    na_ctrl2 = (230, 260)
    na_tail = (258, 282)
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(dr, na_seg, w_head=3.2, w_tail=4.8)


img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
draw_mian_top(draw)
draw_head_body(draw)

out_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "01_实.png",
)
img.save(out_path)
print(f"wrote {out_path}")
