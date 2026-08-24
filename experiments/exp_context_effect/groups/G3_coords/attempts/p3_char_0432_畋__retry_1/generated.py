# BANK_DEVIATION
# skipped: quan_dog_for_LR_right.py
# reason: 攵 has a short 撇+横 hat (not upper-right dot like 犬); different silhouette
# fresh_component: pu_attack_for_LR_right (攵 as right radical in L-R comp)

# TRAJECTORY DIFF (retry_1 of p3_char_0432_畋)
# GT: 田 (compact, left ~40%) + 攵 (right ~55%).
#   攵 = short 撇 (top-left of right slot), short 横 (crossing pie), then
#   long 撇 (from junction down-left) + long 捺 (from same junction down-right).
#   All strokes thin (~4-5px). 撇/捺 meet high, form a wide X spread over
#   the lower two-thirds.
# main FAIL: (1) 田 was full-canvas geometric block, too big — spilled far
#   left, overlapping with 攵 slot. (2) 攵 rendered as disconnected floating
#   dash + tiny stick figure at bottom — the four strokes never met at one
#   junction. Short pie/heng at top were mispositioned (way too small +
#   high), and long pie/na met at the very bottom instead of upper-middle.
# FIX: (a) use bank quan_tian_for_LR_left for 田 (proven B12 A-tier compact
#   form). (b) inline 攵 with EXPLICIT shared junction pixel that all four
#   strokes pass through, positioned at upper-middle of right slot; long
#   pie/na spread wide to bottom. Uniform thin ink.

# Q1 (errata): errata says "田 baked to canvas; 攵 novel" — use compact 田
#   from B12 bank (quan_tian_for_LR_left), inline fresh 攵.
# Q2 (form_catalog): apex-kiss / cross-shaft weld family — long pie + long
#   na share upper-middle junction; short pie + heng converge there too.
# Q3 (helpers): X-crossing pattern — but at this small scale I'll compute
#   the shared pixel inline rather than import kiss_apex, since I also need
#   the short pie/heng converging at the same point.

import os
import sys
import math
from PIL import Image, ImageDraw

_BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from quan_tian_for_LR_left import draw_quan_tian_for_LR_left  # noqa: E402


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


def draw_pu_attack_for_LR_right(d):
    """攵 in right L-R slot. Explicit shared upper-middle junction."""
    # Right slot ~ x in [150, 275]
    # Junction pixel where the long pie and long na cross:
    JX, JY = 200, 150

    # S1: short 撇 (top). Starts upper-right, curves down-left toward the
    # top-left region of the slot (above the junction).
    short_pie = _cubic_pts((225, 80), (215, 100), (200, 115), (180, 130),
                           steps=40)
    _tapered_polyline(d, short_pie, w_head=3.5, w_tail=4.5)

    # S2: short 横 (slightly rising). Crosses through/near the short 撇
    # tail area and extends right past the junction.
    heng = [(170, 128), (200, 122), (255, 115)]
    _tapered_polyline(d, heng, w_head=4.5, w_tail=3.8)

    # S3: long 撇 — from junction area, curves down-left to bottom-left of
    # slot. Two-cubic form for continuous curve.
    seg_head = _cubic_pts((JX + 5, JY - 5), (JX, JY + 10),
                          (JX - 10, JY + 30), (JX - 15, JY + 45), steps=30)
    seg_body = _cubic_pts((JX - 15, JY + 45), (JX - 25, JY + 70),
                          (JX - 40, JY + 100), (150, 275), steps=80)
    _tapered_polyline(d, seg_head, w_head=3.5, w_tail=4.8)
    _tapered_polyline(d, seg_body, w_head=4.8, w_tail=2.2)

    # S4: long 捺 — from junction area, sweeps down-right to bottom-right.
    na_seg = _cubic_pts((JX, JY), (JX + 25, JY + 40),
                        (JX + 50, JY + 80), (285, 265), steps=80)
    _tapered_polyline(d, na_seg, w_head=3.2, w_tail=5.5)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    # 田 on left (compact, B12 bank primitive)
    draw_quan_tian_for_LR_left(d)
    # 攵 on right (fresh)
    draw_pu_attack_for_LR_right(d)
    out = os.path.join(os.path.dirname(__file__), "01_畋.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
