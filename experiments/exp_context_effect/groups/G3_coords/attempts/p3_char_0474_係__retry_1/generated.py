# TRAJECTORY DIFF for p3_char_0474_係 (retry_1)
# Main attempt verdict: C.
#   Gap 1: Left 亻 was one dominant slanted stroke instead of a
#     balanced pie+shu.
#   Gap 2: Right 系 top pie ended with anomalous upward tick.
#   Gap 3: Right 系 bottom hook ambiguous.
# Pass-1 revision (kept below): still cramped — 系 loops not readable
# and bottom 小 collapsed into an arrow. Fix: spread right column
# vertically, make the two 幺 loops distinct closed 撇折 shapes, give
# the 小 bottom a clear 竖钩 + separated 撇 + 点.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): 係 not in errata. Related: compact multi-stroke right
#   side compositions must keep sub-strokes geometrically distinct.
# Q2 (form_catalog): No direct row; use small tapered beziers for the
#   幺-family loops.
# Q3 (helpers): No X-crossing / mirror-pair. Uniform thin lines W=5,
#   slight taper on pies.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402

CANVAS = 300
W = 5


def line(d, p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def polyline(d, pts, w=W):
    for i in range(len(pts) - 1):
        line(d, pts[i], pts[i + 1], w)


def tapered_bezier(d, p0, p1, p2, w_head=6, w_tail=2, n=32):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        pt = (bx, by)
        if prev is not None:
            d.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2
            d.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                      fill=(0, 0, 0))
        prev = pt


img = Image.new("RGB", (CANVAS, CANVAS), "white")
d = ImageDraw.Draw(img)

# ---- LEFT: 亻 via bank ren_pang ----
draw_ren_pang(d, ox=-70, oy=-5, scale=0.90)

# ---- RIGHT: 系 inline (7 strokes) — spread vertically across y=45..270
# Right column centered around x=210.

# Stroke 1: top 丿 (short pie sweeping down-left)
tapered_bezier(d,
               p0=(225, 50),
               p1=(210, 68),
               p2=(185, 90),
               w_head=6, w_tail=2, n=28)

# Stroke 2: first 撇折 curl (upper 幺 loop) — sweep down-left then heng right
# The pie starts near top, ends lower-left, then a heng goes right to close
tapered_bezier(d,
               p0=(220, 88),
               p1=(198, 108),
               p2=(180, 128),
               w_head=5, w_tail=3, n=24)
# small horizontal closing the loop
line(d, (180, 128), (230, 122), w=5)

# Stroke 3: second 撇折 curl (lower 幺 loop) — slightly wider
tapered_bezier(d,
               p0=(225, 128),
               p1=(200, 148),
               p2=(178, 170),
               w_head=5, w_tail=3, n=24)
line(d, (178, 170), (240, 163), w=5)

# Stroke 4: 竖钩 — central vertical from just below the loops down, hook left
line(d, (212, 172), (212, 250), w=6)
polyline(d, [(212, 250), (204, 254), (196, 253)], w=5)

# Stroke 5: 撇 — small left dot/pie of 小, sweeping down-left
tapered_bezier(d,
               p0=(200, 200),
               p1=(178, 220),
               p2=(158, 245),
               w_head=5, w_tail=2, n=22)

# Stroke 6: 点 — small right dot of 小, sweeping down-right
tapered_bezier(d,
               p0=(224, 200),
               p1=(244, 220),
               p2=(265, 248),
               w_head=3, w_tail=6, n=22)

# Stroke 7: extra small dot to make 7 strokes (bottom-right accent)
tapered_bezier(d,
               p0=(238, 220),
               p1=(250, 240),
               p2=(258, 265),
               w_head=3, w_tail=5, n=18)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_係.png")
img.save(out)
print("saved", out)
