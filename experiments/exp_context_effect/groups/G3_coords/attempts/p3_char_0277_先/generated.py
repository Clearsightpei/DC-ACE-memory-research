# 先 (xian) — 6 strokes.
# Composition (top → bottom):
#   Top block (~upper 55% of canvas):
#     s1  短撇  short pie, top-left of top block
#     s2  短横  short heng, upper part of top block (baseline of the small nub)
#     s3  短竖  short vertical from s2 down to the long heng
#     s4  长横  long heng crossing s3, mid canvas
#   Bottom block (儿, lower 45%):
#     s5  长撇  long pie, left leg
#     s6  竖弯钩 right leg, curves and hooks up
#
# G3 principle P4: MMH GT strokes are near-uniform thin (~3-4px), not
# calligraphic tapered. We use uniform thin strokes here.
#
# Inline PIL rendering — no bank primitives called because 先's top
# doesn't map cleanly onto an existing bank entry, and inlining gives
# tighter GT match (v8 "trust GT" posture).

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
W_STROKE = 4  # uniform thin per P4 / P12

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def line(p0, p1, w=W_STROKE):
    d.line([p0, p1], fill="black", width=w)


def bezier(pts, w=W_STROKE, steps=80):
    # quadratic bezier through pts=[p0, p1_ctrl, p2]
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2
        d.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)


# --- Top block ---
# s1: short pie (upper-left of top nub)
bezier([(162, 52), (152, 68), (135, 88)])

# s2: short heng — top of the small "nub"
line((152, 82), (205, 78))

# s3: short vertical from under s2 down to the long heng
line((178, 82), (178, 138))

# s4: long heng crossing s3, mid canvas
line((78, 140), (250, 136))

# --- Bottom (儿) ---
# s5: long pie — left leg sweeping down-left
bezier([(155, 142), (110, 210), (52, 282)])

# s6: 竖弯钩 — smooth vertical→right sweep→hook, all in one bezier arc
# Segment A: vertical drop
line((205, 145), (205, 235))
# Segment B: smooth curve into base
bezier([(205, 235), (208, 278), (270, 275)])
# Segment C: hook flick up
line((270, 275), (272, 255))

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_先.png"))
