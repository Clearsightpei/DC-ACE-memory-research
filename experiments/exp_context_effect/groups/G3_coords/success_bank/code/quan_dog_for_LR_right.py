# quan_dog_for_LR_right.py — promoted from p3_char_0434_畎 (B12 main A verdict)
# Curator B12 (2026-08-04, position 601).
#
# 犬 (= 大 + 丶 upper-right dot) for the RIGHT slot of L-R compositions.
# Rendered inline in PIL pixel coords with an EXPLICIT SHARED X-CROSSING
# pixel that pie and na both pass through.
#
# ★ SIGNIFICANCE: This primitive was extracted from G3's FIRST-EVER A
# verdict (畎, after 600 items / 12 batches / 0 prior A). The 大-family
# is TERMINAL_FROZEN for full-canvas X-crossing (see 矢, 失, 人, 入, 大 —
# all C at R4). What made 犬 A-tier: the X-crossing was compressed INTO
# an L-R right slot (~55% canvas width), so the crossing occupies less
# pixel real-estate and the panel accepts thin-ink (~4-5px) at the join.
# See P-DEV4 in principle_bank.md for the codified pattern.
#
# Motivating context: 畎 (田 + 犬). Reuse targets:
# - 猷 (犬 as right radical after 酉)
# - Any 大-family right radical in L-R where the left occupies ~40% —
#   the compression is the mechanism, not the extra dot.
# - Consider adapting for 大 itself when it appears as a compact right
#   radical (奂-family), though the dot presence is what makes it 犬.
#
# Why fresh (v13 BANK_DEVIATION rationale): `da_char.py` bakes 大 at
# full canvas, does its own draw+save, and would collide with the left
# sibling if instantiated at its own coords.
#
# Signature: (d, x_slot_left=150, x_slot_right=275, cross_y=143,
#             pie_top=(218,78), na_tail=(285,260), dian_head=(245,82),
#             dian_tail=(268,118), w_thin=4.5)
# Caller controls slot boundaries; internal proportions match the 畎
# recipe. Default values produce the A-tier render.

import os
import math
from PIL import Image, ImageDraw


def _stamp(d, x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def _tapered_polyline(d, points, w_head=4.5, w_tail=3.5):
    if len(points) < 2:
        return
    seg_len, total = [], 0.0
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
            _stamp(d, x, y, w / 2)
        covered += L


def _cubic_pts(p0, p1, p2, p3, steps=80):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0]
             + 3 * (1 - u) * u ** 2 * p2[0] + u ** 3 * p3[0])
        y = ((1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1]
             + 3 * (1 - u) * u ** 2 * p2[1] + u ** 3 * p3[1])
        out.append((x, y))
    return out


def draw_quan_dog_for_LR_right(
    d,
    x_slot_left=150, x_slot_right=275, cross_y=143,
    pie_top=(218, 78), pie_neck=(216, 118),
    pie_tail_c=(175, 210), pie_tail=(148, 265),
    na_head_offset=(2, 2), na_ctrl1=(240, 190),
    na_ctrl2=(270, 230), na_tail=(285, 260),
    dian_head=(245, 82), dian_c1=(255, 95),
    dian_c2=(262, 108), dian_tail=(268, 118),
):
    """犬 for LR-right slot. cross_y is the y where pie and na both pass."""
    heng_left = (x_slot_left, cross_y + 2)
    heng_right = (x_slot_right, cross_y - 5)
    cross = ((x_slot_left + x_slot_right) // 2 + 15, cross_y)  # approx

    # S1: 横 (thin, slight taper across)
    _tapered_polyline(d, [heng_left, (cross[0] - 2, cross_y - 1), heng_right],
                      w_head=3.5, w_tail=4.2)

    # S2: 撇 — starts above heng, curves continuously through crossing to
    # bottom-left. Two-cubic form: head segment + body segment.
    seg_head = _cubic_pts(pie_top, (225, 95), (220, 108), pie_neck, steps=40)
    seg_body = _cubic_pts(pie_neck, (210, 145), pie_tail_c, pie_tail, steps=80)
    _tapered_polyline(d, seg_head, w_head=3.5, w_tail=4.5)
    _tapered_polyline(d, seg_body, w_head=4.5, w_tail=2.2)

    # S3: 捺 — from the crossing point, sweeps down-right
    na_head = (cross[0] + na_head_offset[0], cross[1] + na_head_offset[1])
    na_seg = _cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    _tapered_polyline(d, na_seg, w_head=3.2, w_tail=4.8)

    # S4: 丶 dian at upper-right — this is what makes 犬 (not 大)
    dian_seg = _cubic_pts(dian_head, dian_c1, dian_c2, dian_tail, steps=30)
    _tapered_polyline(d, dian_seg, w_head=3.0, w_tail=5.5)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_quan_dog_for_LR_right(d)
    out = os.path.join(os.path.dirname(__file__), "01_quan_dog_for_LR_right.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
