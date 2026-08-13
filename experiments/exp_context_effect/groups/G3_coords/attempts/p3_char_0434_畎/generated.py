# p3_char_0434_畎 — 畎 (quǎn), 9 strokes.
# Structure: L-R composition. Left = 田 (5 strokes: box+cross). Right = 犬 (4 strokes: 大 + 丶 upper-right).
#
# BANK_DEVIATION
# skipped: bi_field_over_ji.py (baked full-canvas 田) and da_char.py (baked full-canvas 大 with own draw+save)
# reason: 田 must compress into left ~40% of canvas; 犬 (=大+dot) must occupy right ~55% and shift right.
#         Both bank entries are hard-coded at ~full canvas and would collide if instantiated at their own coords.
# fresh_component: quan_tian_for_LR_left (compressed 田) + quan_dog_for_LR_right (犬 = 大 + upper-right dian)

import os
import math
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畎.png")

W, H = 300, 300
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)


def _stamp(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(points, w_head=4.5, w_tail=3.5):
    if len(points) < 2:
        return
    seg_len = []
    total = 0.0
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        L = math.hypot(dx, dy)
        seg_len.append(L)
        total += L
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


# ---------- LEFT: 田 (compressed for L-R left slot) ----------
x_left, x_right = 30, 125
y_top,  y_bot   = 100, 220
x_mid = (x_left + x_right) // 2
y_mid = (y_top + y_bot) // 2

w  = 5   # thin MMH weight
wm = 4

# S1 left 竖
d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
# S2 横折 (top + right)
d.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
# S3 middle 竖
d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
# S4 middle 横
d.line([(x_left + 2, y_mid), (x_right - 2, y_mid)], fill=(0, 0, 0), width=wm)
# S5 bottom 横
d.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)


# ---------- RIGHT: 犬 = 大 + 丶 upper-right ----------
# 大 in right slot: heng across, pie curving down-left, na down-right.
heng_left  = (150, 145)
heng_right = (275, 138)
cross      = (215, 143)   # apex/crossing on heng

# S6: 横 (thin, tapered)
tapered_polyline([heng_left, (213, 142), heng_right], w_head=3.5, w_tail=4.2)

# S7: 撇 — starts above heng, continuous curve through crossing, down-left
pie_top    = (218, 78)
pie_neck   = (216, 118)
pie_tail_c = (175, 210)
pie_tail   = (148, 265)

seg_head = cubic_pts(pie_top, (225, 95), (220, 108), pie_neck, steps=40)
seg_body = cubic_pts(pie_neck, (210, 145), pie_tail_c, pie_tail, steps=80)
tapered_polyline(seg_head, w_head=3.5, w_tail=4.5)
tapered_polyline(seg_body, w_head=4.5, w_tail=2.2)

# S8: 捺 — from the crossing point, sweeps down-right
na_head  = (cross[0] + 2, cross[1] + 2)
na_ctrl1 = (240, 190)
na_ctrl2 = (270, 230)
na_tail  = (285, 260)
na_seg   = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
tapered_polyline(na_seg, w_head=3.2, w_tail=4.8)

# S9: 丶 dian at upper-right of 大 (that's what makes 犬)
dian_seg = cubic_pts((245, 82), (255, 95), (262, 108), (268, 118), steps=30)
tapered_polyline(dian_seg, w_head=3.0, w_tail=5.5)


img.save(_OUT)
print("wrote", _OUT)
