# p3_char_0355_块 — G3 drawer attempt
# Composition: 土 (提土旁 on left, use tu.py bank) + 夬 on right (inline fresh).
# The right 夬 has a 横折 top-box, a middle heng, and a pie/na X below the
# heng crossing — mirroring the 大-family recipe (v9 rerun) with na starting
# at the pie/heng crossing pixel.

import os
import sys
from PIL import Image, ImageDraw
import math

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from tu import draw_tu  # noqa: E402

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


# ---------------------------------------------------------------- helpers
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


# ---------------------------------------------------------------- LEFT: 土
# tu.py uses math-coords (center origin, +y up). Canonical bottom heng is
# ~210 px wide (200*1.05); at scale 0.40 → ~84 px, comfortably left-half.
# Shift left with ox=-80 so center of 土 sits at pixel x ≈ 70.
draw_tu(draw, ox=-80.0, oy=-5.0, scale=0.42)


# ---------------------------------------------------------------- RIGHT: 夬
# PIL pixel coords (y grows DOWN). 夬 occupies the right half, centered
# around x≈195. 4 strokes: 横折, 横, 撇, 捺.
#
# 横折 top-right corner sits high; its vertical descends TO the middle
# heng (not floating above it). Middle heng extends outside the box on
# both sides (per GT). Pie/na X-cross sits on middle heng.

# 1) 横折 — top short heng then turn down to middle-heng level (~y=150)
tapered_polyline([(175, 95), (210, 93), (245, 92)],
                 w_head=4.0, w_tail=4.5)
tapered_polyline([(244, 92), (243, 122), (242, 152)],
                 w_head=4.2, w_tail=3.8)

# 2) middle heng (extends past the box on both sides, slight up-right tilt)
tapered_polyline([(148, 155), (195, 150), (250, 147)],
                 w_head=3.5, w_tail=4.2)

# 3) 撇 — one continuous curve: head rises above the middle heng, passes
#    through the pie/heng crossing, sweeps to lower-left.
cross = (188, 152)
pie_top     = (198, 108)
pie_head_c  = (206, 125)
pie_neck    = (192, 145)
pie_tail_c1 = (170, 205)
pie_tail_c2 = (150, 240)
pie_tail    = (118, 275)

seg_head = cubic_pts(pie_top, pie_head_c, (196, 140), pie_neck, steps=40)
seg_body = cubic_pts(pie_neck, pie_tail_c1, pie_tail_c2, pie_tail, steps=80)
tapered_polyline(seg_head, w_head=3.3, w_tail=4.5)
tapered_polyline(seg_body, w_head=4.5, w_tail=2.2)

# 4) 捺 — separate stroke starting AT the crossing on middle heng
na_head  = (cross[0] + 2, cross[1] + 2)
na_ctrl1 = (225, 205)
na_ctrl2 = (265, 250)
na_tail  = (285, 275)
na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
tapered_polyline(na_seg, w_head=3.2, w_tail=4.8)


out_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "01_块.png",
)
img.save(out_path)
print(f"wrote {out_path}")
