"""Render 成 (chéng, 'become') as a 300x300 PNG.

Structure (from GT):
- Top short 横 slanting upward with a small tail
- Long 撇 from upper-middle going down-left to lower-left
- Inner middle: small horizontal + short vertical (like top of 厂/口 fragment)
- Big 斜钩: arcs from upper-right, through center, down to bottom-right,
  then a strong upward hook flick
- Small 撇 crossing the 斜钩 near the top
- Small 点 at top-right above the hook arc
"""

from PIL import Image, ImageDraw
import math
import os


def draw_cheng(draw):
    # Top short heng (slightly rising to the right, upper region)
    # anchor: (80, 90) → (170, 78)
    draw.line([(80, 92), (172, 80)], fill='black', width=5)

    # Long pie (left arm) — start near top-middle, sweep down-left
    # bezier via 3 waypoints
    pie_pts = []
    for i in range(60):
        t = i / 59.0
        # Cubic-ish: start (118, 78), through (100, 160), end (60, 270)
        x0, y0 = 118, 78
        x1, y1 = 100, 165
        x2, y2 = 60, 275
        # Quadratic Bezier
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        pie_pts.append((x, y))
    for i in range(len(pie_pts) - 1):
        draw.line([pie_pts[i], pie_pts[i + 1]], fill='black', width=5)

    # Inner short heng (middle horizontal, below the top) — shorter
    draw.line([(100, 148), (170, 138)], fill='black', width=5)

    # Inner small pocket: short vertical / pie then a bottom heng
    inner_pts = []
    for i in range(24):
        t = i / 23.0
        x0, y0 = 100, 148
        x1, y1 = 95, 185
        x2, y2 = 110, 218
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        inner_pts.append((x, y))
    for i in range(len(inner_pts) - 1):
        draw.line([inner_pts[i], inner_pts[i + 1]], fill='black', width=5)

    # Inner bottom small stroke closing pocket
    draw.line([(108, 215), (168, 208)], fill='black', width=4)

    # Big 斜钩 (xie gou) — from upper-right down through middle to lower-right
    # then a strong flick up. Use two-segment bezier for a pronounced belly.
    xg_pts = []
    for i in range(100):
        t = i / 99.0
        # Cubic Bezier for stronger belly and better shape
        x0, y0 = 152, 88
        x1, y1 = 175, 180
        x2, y2 = 215, 245
        x3, y3 = 258, 268
        x = ((1 - t) ** 3 * x0
             + 3 * (1 - t) ** 2 * t * x1
             + 3 * (1 - t) * t ** 2 * x2
             + t ** 3 * x3)
        y = ((1 - t) ** 3 * y0
             + 3 * (1 - t) ** 2 * t * y1
             + 3 * (1 - t) * t ** 2 * y2
             + t ** 3 * y3)
        xg_pts.append((x, y))
    for i in range(len(xg_pts) - 1):
        draw.line([xg_pts[i], xg_pts[i + 1]], fill='black', width=6)
    # Strong hook flick upward at end
    hk_pts = []
    for i in range(30):
        t = i / 29.0
        x0, y0 = 258, 268
        x1, y1 = 272, 250
        x2, y2 = 278, 218
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        hk_pts.append((x, y))
    for i in range(len(hk_pts) - 1):
        draw.line([hk_pts[i], hk_pts[i + 1]], fill='black', width=5)

    # Small 撇 crossing top of 斜钩 (short slash upper-right area) —
    # like a short pie going down-right from around the top
    draw.line([(175, 100), (215, 122)], fill='black', width=5)

    # Small 点 (dot) at top-right above the hook
    draw.ellipse([(203, 78), (219, 96)], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_cheng(draw)
    out = os.path.join(os.path.dirname(__file__), '01_成.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
