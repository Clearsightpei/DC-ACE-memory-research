"""p3_char_0193_癶 (bo, "back to back") — G3 attempt.

癶 = two mirror halves, "back to back" radical.
Left half: short 撇 (top mark) + long 撇 curving down-left.
Right half: short 撇/挑 (top mark) + long 捺 flaring down-right, with a
small 点 on the shoulder of the 捺.

GT PNG shows thin, hand-drawn-looking strokes. Under v8 we trust GT
over bank primitives, so inline PIL rendering with modest widths.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=5):
    """Draw a smooth polyline with rounded joins/caps."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill="black")


def curve(p0, p1, p2, steps=30, width=5):
    """Quadratic bezier as polyline."""
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    stroke(pts, width=width)


def draw_bo(d):
    # -------- LEFT HALF --------
    # Short 撇/heng at top-left (slanted small mark, like a rising then dipping)
    stroke([(115, 95), (95, 115)], width=5)

    # Long 撇: from upper-middle, curving down and left to lower-left
    curve((130, 100), (95, 170), (55, 240), width=6)

    # -------- RIGHT HALF --------
    # Small 点 above (the tiny dot on top-right)
    stroke([(180, 100), (172, 115)], width=5)

    # Short 挑 / heng-pie at top-right (below the dot)
    stroke([(165, 130), (200, 115)], width=5)

    # Long 捺: from just below the short mark, curving down and right
    curve((175, 130), (215, 195), (260, 240), width=6)


draw_bo(d)

out = os.path.join(os.path.dirname(__file__), "01_癶.png")
img.save(out)
print("wrote", out)
