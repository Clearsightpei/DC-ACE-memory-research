"""
G1 (no-memory control) — p1_stroke_24_横撇弯钩
Compound stroke: 横 (horizontal) + 撇 (left-falling) + 弯 (curve) + 钩 (hook).
This is the stroke that appears in characters like 及, 阝(右耳旁), 队, 阴, 阳.

Rendered cold from label + description; no memory, no GT PNG for strokes.
Output: 300x300 PNG, white background, black ink.
"""

import os
from PIL import Image, ImageDraw

SIZE = 300
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(OUT_DIR, "01_横撇弯钩.png")


def draw_thick_polyline(draw, points, width):
    """Draw a polyline with rounded joins by stroking segments + circles at joints."""
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill="black", width=width)
    r = width // 2
    for x, y in points:
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def bezier(p0, p1, p2, steps=40):
    """Quadratic Bezier from p0 to p2 via control p1, returns list of (x,y)."""
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def main():
    img = Image.new("RGB", (SIZE, SIZE), "white")
    draw = ImageDraw.Draw(img)

    stroke_w = 14

    # 横撇弯钩 has 4 phases, drawn as a single continuous stroke:
    #
    #   1. 横 (heng): short horizontal top segment, going right.
    #   2. 撇 (pie): sharp turn down-left (like the 横撇 combo).
    #   3. 弯 (wan): curves back to the right and down (belly of the stroke).
    #   4. 钩 (gou): small upward hook at the bottom-right end.
    #
    # Reference silhouette matches the right side of 及 / the right-ear 阝.

    # ---- 1) 横 (short horizontal top) ----
    heng_start = (70, 75)
    heng_end = (215, 75)
    draw.line([heng_start, heng_end], fill="black", width=stroke_w)

    # ---- 2) 撇 (turn sharply down-left from heng_end) ----
    # Nearly straight, tilted down-left, ending around lower-left region.
    pie_start = heng_end
    pie_end = (100, 175)
    draw.line([pie_start, pie_end], fill="black", width=stroke_w)

    # ---- 3) 弯 (curve): sweep from pie_end down and to the right ----
    # Quadratic bezier so the belly bulges downward.
    wan_start = pie_end
    wan_ctrl = (135, 260)          # control point pulls curve down
    wan_end = (215, 235)           # ends lower-right
    wan_pts = bezier(wan_start, wan_ctrl, wan_end, steps=60)
    draw_thick_polyline(draw, [(int(x), int(y)) for x, y in wan_pts], stroke_w)

    # ---- 4) 钩 (hook): short upward flick from wan_end ----
    gou_start = wan_end
    gou_end = (230, 195)
    draw.line([gou_start, gou_end], fill="black", width=stroke_w)

    # Round the joints so the compound stroke reads as one continuous ink flow.
    r = stroke_w // 2
    for jx, jy in [heng_start, heng_end, pie_end, wan_end, gou_end]:
        draw.ellipse([jx - r, jy - r, jx + r, jy + r], fill="black")

    img.save(OUT_PATH)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
