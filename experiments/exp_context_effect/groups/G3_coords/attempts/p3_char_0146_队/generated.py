# p3_char_0146_队 (duì) — 4-stroke: 阝 (left ear = 横折折折 loop + shu descender)
#                                     + 人 (pie + na, right side)
# G3 approach: inline fresh. 阝 is in errata (fail mode: force-fit).
# GT shows: left side small closed-ish loop (ear) + long shu going down,
#           right side wide 人 with high apex, pie down-left, na down-right.
import os
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)


def bezier_stroke(draw, p0, p1, p2, w_head=6, w_tail=2, n=60,
                  w_belly=None, belly_pos=1.0):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def polyline_stroke(draw, pts, width=4):
    # simple constant-width polyline for the ear-loop
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=width)


# --- 阝 (left ear): the "ear" is one continuous 横折折折 that makes a
# small closed bump at upper-left; then a long shu descends.
# GT shows ear roughly in canvas x=[50,115], y=[85,180]; shu tails to y=270.

# Ear: single continuous 横折折折 with softer corners (rounded loop),
# smaller and tucked more to the left.
ear_pts = [
    (58, 108),   # start top-left
    (98, 100),   # top-right (heng slightly rising)
    (108, 120),  # small fold down
    (95, 140),   # coming back left-down
    (68, 148),   # returning to left column
    (62, 165),   # transition to shu column
]
polyline_stroke(d, ear_pts, width=5)

# Shu (long descender of 阝) starting from bottom-left of loop
bezier_stroke(d,
              (62, 148), (62, 210), (65, 278),
              w_head=6, w_tail=3, n=60)

# --- 人 (right side): apex higher, pie shorter, na wider.
# Pie: from apex sweeping to lower-left, curved
bezier_stroke(d,
              (198, 85), (170, 165), (140, 258),
              w_head=6, w_tail=1, n=60)

# Na: from apex sweeping to lower-right, widening at belly
bezier_stroke(d,
              (198, 85), (238, 170), (285, 258),
              w_head=3, w_tail=3, w_belly=10, belly_pos=0.75, n=60)


out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_队.png"))
