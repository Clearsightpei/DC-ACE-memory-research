"""p2_radical_123_韦 (wéi) — 4-stroke radical.

Revision 1 (self-check vs GT):
  - Top 横: GT shows a slight-arc bar upper-center, with the shaft
    tucked slightly under (not passing through it visibly). Keep.
  - Middle 横: GT places it around center; my prior render had it too
    high. Move down to y~+5.
  - Long 竖: extends from just under the top 横 down to below middle
    横 — but does NOT descend below the bottom 横折钩. Actually in
    GT the shaft ends near the base line, ~same y as hook end. OK,
    keep long tail.
  - Bottom 横折钩: GT's bottom section is a broad tapered horizontal
    from left-of-shaft to well-right-of-shaft, then a distinct fold
    down and a clear hook. Widen the horizontal span.
"""
import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

from _shared_helpers import (
    tapered_line,
    tapered_bezier,
    to_px,
)

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)


# --- 1) TOP short 横 with small right-side 顿笔 ----------------------
# From (-38, +92) slight bow to (+35, +85).
tapered_bezier(
    draw,
    p0=(-38, 92),
    p1=(-2, 87),
    p2=(35, 85),
    w_head=6,
    w_tail=9,
    n=36,
)
rx, ry = to_px(35, 85)
r = 4
draw.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(0, 0, 0))


# --- 2) MIDDLE 横 (longer, near center) -----------------------------
# From (-88, +8) to (+82, +12) — slight upward tilt.
tapered_line(
    draw,
    p0=(-88, 8),
    p1=(82, 12),
    w0=7,
    w1=9,
    n=44,
)


# --- 3) LONG 竖 (vertical shaft through top+middle, down to base) ---
# From (-3, +90) down to (-3, -118).
tapered_line(
    draw,
    p0=(-3, 90),
    p1=(-3, -118),
    w0=8,
    w1=9,
    n=44,
)


# --- 4) BOTTOM 横折钩 -----------------------------------------------
# 4a) bottom horizontal from (-78, -55) to (+70, -50)
tapered_line(
    draw,
    p0=(-78, -55),
    p1=(70, -50),
    w0=6,
    w1=9,
    n=40,
)

# 4b) corner 顿笔 blob at the fold
cx, cy = to_px(70, -50)
cr = 5
draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(0, 0, 0))

# 4c) vertical drop from (70, -50) to (66, -108) — slight inward lean
tapered_line(
    draw,
    p0=(70, -50),
    p1=(66, -108),
    w0=9,
    w1=8,
    n=36,
)

# 4d) hook: flick up-and-LEFT (inward) from (66, -108) to (38, -90).
tapered_line(
    draw,
    p0=(66, -108),
    p1=(38, -90),
    w0=8,
    w1=2,
    n=28,
)


out = os.path.join(HERE, "01_韦.png")
img.save(out)
print("wrote", out)
