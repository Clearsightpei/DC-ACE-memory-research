# p2_radical_120_瓦 — G3 coord-bank attempt (revision 2)
# 4 strokes: 一 (top heng), 丿 (left pie), 乙 (横折弯钩 envelope), 丶 (inner dian)
# Math coords: center origin (150,150), +y up.
#
# Revision notes vs first attempt:
#  - top heng shifted UP slightly and made shorter (matches GT proportion)
#  - 丿 given a more diagonal slant (down-and-left with softer bow), starting
#    UNDER the left tip of the heng (not attached), ending much lower-left
#  - 乙 envelope bottom sweep extended further right and rises higher toward
#    tail; hook flick made more visible pointing up-and-slightly-inward
#  - dian repositioned into upper-mid area, made a touch larger

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from _shared_helpers import (
    to_px, tapered_bezier, tapered_line, variant_pie, variant_dian,
)

img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

# ---- Stroke 1: 一 (top heng) — short horizontal, upper area
# Spans roughly x=-40..+42 at y ~ +70
tapered_line(draw, (-40, 70), (42, 72), 7, 9)
# 顿笔 corner blob at the right tip (start of 乙)
rx, ry = to_px(42, 72)
draw.ellipse([rx - 4, ry - 4, rx + 4, ry + 4], fill=(0, 0, 0))

# ---- Stroke 2: 丿 (left pie) — diagonal down-and-left, softer scoop
# Starts just below the left tip of the top heng, sweeps down to lower-left
# form_catalog 丿 row: shallow slope, soft curl, thinner
variant_pie(draw,
            head=(-42, 62),
            tail=(-88, -105),
            bow_perp=-14.0,
            w_head=8.0, w_tail=1.5, n=56)

# ---- Stroke 3: 乙 (横折弯钩) — big envelope on the right.
# Starts at right end of top heng (~(42,68)), descends vertically-ish,
# curves along the bottom, hooks up at bottom-right.
#
# (a) vertical descent turning at the bottom-left of the envelope
tapered_bezier(draw,
               p0=(42, 68),
               p1=(30, -20),
               p2=(-5, -95),
               w_head=9, w_tail=8, n=48)

# (b) bottom sweep to the right, rising slightly
tapered_bezier(draw,
               p0=(-5, -95),
               p1=(35, -108),
               p2=(72, -85),
               w_head=8, w_tail=7, n=40)

# (c) hook: tapered flick up-and-slightly-left from the tail
tapered_line(draw, (72, -85), (60, -55), 8, 2)

# ---- Stroke 4: 丶 (dian) — inside the envelope, upper-middle area
# thin head upper-left → thick tail lower-right
variant_dian(draw,
             head=(-8, 20),
             tail=(18, -12),
             w_head=3.0, w_tail=11.0, bow_perp=-2.5, n=32)

out = os.path.join(os.path.dirname(__file__), "01_瓦.png")
img.save(out)
print(f"wrote {out}")
