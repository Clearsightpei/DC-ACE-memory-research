# BANK_DEVIATION
# skipped: bai_char_for_top_stack.py, da_char.py
# reason: 皋 needs a 3-part vertical stack (白 / 大 / 十) inside 300px so each
#   component must be compressed further than either bank primitive supports;
#   inlining lets me control the y-bands cleanly.
# fresh_component: gao_char_stack (compact 白-top + 大-middle + 十-bottom stack)

"""
p3_char_0544_皋 — 皋 (gāo)

Decomposition (from GT):
  - TOP:    白 (short 撇 + rectangular ri-body with middle heng), y≈25..95
  - MIDDLE: 大 (heng + continuous pie + na from crossing), y≈100..180
  - BOTTOM: 十 (short heng + long shu going down to canvas bottom), y≈195..290

Thin ~4-5 px MMH-style ink throughout (P12).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(points, w_head=4.5, w_tail=3.5):
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


# -----------------------------------------------------------------------
# TOP: 白 (compact top-stack), y ≈ 25 .. 95
# -----------------------------------------------------------------------
def draw_bai_top(canvas, x_left=125, x_right=185, y_top=35, y_bot=100):
    y_mid = (y_top + y_bot) // 2
    w = 5
    # 短撇 above body
    canvas.line([(160, y_top - 18), (x_left + 3, y_top + 2)],
                fill=(0, 0, 0), width=4)
    # 竖 left
    canvas.line([(x_left, y_top), (x_left, y_bot)],
                fill=(0, 0, 0), width=w)
    # 横折 top + right 竖
    canvas.line([(x_left, y_top), (x_right, y_top + 2)],
                fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 2), (x_right, y_bot)],
                fill=(0, 0, 0), width=w)
    # middle 横
    canvas.line([(x_left + 3, y_mid), (x_right - 3, y_mid)],
                fill=(0, 0, 0), width=4)
    # bottom 横 (closes body)
    canvas.line([(x_left, y_bot), (x_right + 1, y_bot)],
                fill=(0, 0, 0), width=w)


draw_bai_top(draw)


# -----------------------------------------------------------------------
# MIDDLE: 大 (compressed), y ≈ 115 .. 200
# -----------------------------------------------------------------------
# heng
heng_left = (72, 140)
heng_right = (228, 136)
tapered_polyline([heng_left, (150, 138), heng_right],
                 w_head=3.6, w_tail=4.2)

# pie — one continuous curve from above heng down through crossing to lower-left
cross = (150, 138)
pie_top_start = (156, 105)
pie_neck = (150, 128)
pie_tail_ctrl = (105, 185)
pie_tail_end = (72, 208)
seg_head = cubic_pts(pie_top_start, (162, 118), (154, 122), pie_neck, steps=30)
seg_body = cubic_pts(pie_neck, (144, 145), pie_tail_ctrl, pie_tail_end, steps=70)
tapered_polyline(seg_head, w_head=3.4, w_tail=4.4)
tapered_polyline(seg_body, w_head=4.4, w_tail=2.4)

# na — separate stroke starting at the crossing on the heng
na_head = (cross[0] + 2, cross[1] + 2)
na_ctrl1 = (178, 165)
na_ctrl2 = (215, 195)
na_tail = (238, 210)
na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=70)
tapered_polyline(na_seg, w_head=3.0, w_tail=4.8)


# -----------------------------------------------------------------------
# BOTTOM: 十 (heng + long shu), y ≈ 220 .. 290
# -----------------------------------------------------------------------
# short heng across
draw.line([(60, 240), (240, 240)], fill=(0, 0, 0), width=5)
# long shu going straight down
draw.line([(150, 218), (150, 290)], fill=(0, 0, 0), width=5)


out_path = ("<REPO_ROOT>/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0544_皋/01_皋.png")
img.save(out_path)
print(f"wrote {out_path}")
