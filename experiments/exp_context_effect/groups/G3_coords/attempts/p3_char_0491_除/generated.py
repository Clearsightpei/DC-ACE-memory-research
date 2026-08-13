# BANK_DEVIATION
# skipped: none — no 阝 or 余 bank primitive fits directly.
# reason: 阝 in bank is only errata (no PASSed .py); 余 has no bank entry.
#         Inline fresh L-R composition following v8 "trust GT + inline" posture.
# fresh_component: fu_ear_for_LR_left (2-stroke 阝) + yu_余_for_LR_right (7-stroke)
#
# p3_char_0491_除 (chú) — L-R: 阝 (2 strokes, left) + 余 (7 strokes, right).
# GT observations:
#   Left 阝 sits in x ~ [45, 120]: small ear-loop upper, long shu descending.
#   Right 余 sits in x ~ [130, 285]: wide 人 roof at top, short heng under it,
#     central shu-gou dropping down, plus a short heng slightly wider,
#     and two small 点/撇+捺 at the base.
# 除 is 9 strokes total; L-R aspect roughly 40/60 (right side wider).

import os
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)


def bezier(draw, p0, p1, p2, w_head=6, w_tail=3, n=80,
           w_belly=None, belly_pos=0.7):
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if w_belly is not None:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        r = w / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def line_tap(draw, p0, p1, w0, w1, n=60):
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def polyline(draw, pts, width=5):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=width)


# =========================================================================
# LEFT: 阝 (2 strokes), based on p3_char_0146_队 recipe
# =========================================================================
# Ear-loop: single continuous 横撇弯钩, small closed-ish bump upper-left.
ear_pts = [
    (52, 100),   # top-left start
    (95, 92),    # top-right (heng slightly rising)
    (108, 115),  # small fold down-right
    (92, 135),   # coming back left-down
    (60, 142),   # returning to left column
    (55, 158),   # transition to shu column
]
polyline(d, ear_pts, width=5)

# Long shu (descender of 阝) — starts under the loop, drops to bottom
bezier(d,
       (55, 138), (56, 210), (58, 280),
       w_head=7, w_tail=4, n=60)

# =========================================================================
# RIGHT: 余 (7 strokes) — inline
# =========================================================================
# Layout: right block x ~ [130, 285], y ~ [45, 275].
# Apex of 人 at (~208, 55). Wide pie sweeping down-left, wide na down-right.

# Stroke 1: 撇 (pie) — from apex sweeping down-left, thins toward tail
bezier(d,
       (208, 55), (175, 100), (135, 155),
       w_head=8, w_tail=2, n=80)

# Stroke 2: 捺 (na) — from near-apex sweeping down-right, thickens belly then hook
bezier(d,
       (212, 60), (240, 105), (285, 155),
       w_head=3, w_tail=3, w_belly=11, belly_pos=0.8, n=80)

# Stroke 3: 横 (short heng, under the roof)
line_tap(d, (162, 158), (255, 158), 5, 5, n=60)

# Stroke 4: 横 (second, slightly longer heng further down — the crossbar of 十)
line_tap(d, (150, 195), (268, 195), 6, 5, n=60)

# Stroke 5: 竖钩 (central shu-gou) — vertical from between the two hengs down,
# with a small hook flick at bottom to the left.
line_tap(d, (208, 158), (208, 250), 6, 6, n=60)
# hook flick
line_tap(d, (208, 250), (194, 240), 6, 4, n=30)

# Stroke 6: 撇 (short pie, bottom-left of the shu — like 八 left leg)
bezier(d,
       (198, 205), (183, 225), (168, 250),
       w_head=5, w_tail=2, n=50)

# Stroke 7: 点 (dot, bottom-right of the shu — like 八 right leg)
bezier(d,
       (218, 205), (238, 225), (255, 250),
       w_head=3, w_tail=2, w_belly=7, belly_pos=0.75, n=50)


out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_除.png"))
print("saved")
