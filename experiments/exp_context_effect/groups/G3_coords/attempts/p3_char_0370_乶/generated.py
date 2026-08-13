# 乶 (Korean hanja) — composition: 甫 (top) + 丶 (top-right dot) + 乙 (bottom envelope)
# BANK_DEVIATION
# skipped: fu.py (top 甫 rendered inline for tight upper-left placement over 乙)
# reason: bank fu is scaffolded for standalone/left-position use; this composition
#         requires a compressed 甫 nested above a full-width 乙 envelope with a
#         top-right dot, which the frozen (ox,oy,scale) signature cannot reshape.
# fresh_component: fu_top_for_bol (compressed 甫 for 乶-style envelopes)

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from yi_radical import draw_yi_radical  # noqa: E402


def stamp_line(t, p0, p1, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    for s in range(steps + 1):
        u = s / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        t.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def draw_dot(t, cx, cy, w=8, h=12, angle_deg=30):
    # simple slanted dot 丶
    import math
    a = math.radians(angle_deg)
    for s in range(20):
        u = s / 19
        x = cx + math.cos(a) * (u - 0.5) * h
        y = cy + math.sin(a) * (u - 0.5) * h
        r = (w / 2.0) * (1 - abs(u - 0.6) * 0.6)
        t.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def draw_fu_top(t):
    """Compressed 甫: top horizontal, rectangle with vertical spine, small internal bars."""
    # Overall bounding box for the 甫 body: x in [70,175], y in [55,155]
    # Top horizontal (with left downward tick)
    stamp_line(t, (72, 60), (82, 55), 6, 6, steps=15)          # small left tick
    stamp_line(t, (78, 58), (176, 62), 7, 6, steps=60)         # top horizontal
    # Left vertical of box
    stamp_line(t, (88, 68), (86, 158), 6, 7, steps=60)
    # Right vertical of box (with hook down-left at bottom)
    stamp_line(t, (170, 70), (168, 150), 6, 7, steps=60)
    stamp_line(t, (168, 150), (156, 158), 7, 5, steps=20)      # tiny hook
    # Middle vertical spine (extends below box)
    stamp_line(t, (128, 45), (128, 175), 6, 8, steps=80)
    # Two internal horizontals inside the box
    stamp_line(t, (92, 92), (168, 94), 5, 5, steps=50)
    stamp_line(t, (92, 122), (168, 124), 5, 5, steps=50)


def draw_bol(t):
    # Top 甫
    draw_fu_top(t)
    # Top-right dot 丶
    draw_dot(t, cx=205, cy=60, w=10, h=18, angle_deg=45)
    # Bottom 乙 as envelope — shift down + slight scale down
    draw_yi_radical(t, ox=0, oy=40, scale=0.95)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_bol(t)
    out = os.path.join(_HERE, "01_乶.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
