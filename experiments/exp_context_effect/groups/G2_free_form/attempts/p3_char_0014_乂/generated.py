"""
乂 (yi) — two crossing strokes forming an X-like shape.
GT observation:
  - 撇 (left-falling): starts upper-right ~(200, 55), curves down-left
    to lower-left ~(65, 260). Long sweeping arc with slight rightward
    bow, thick→thin taper.
  - 捺 (right-falling): starts upper-left ~(90, 90), curves down-right
    to lower-right ~(235, 260). Thin→thick taper with broad flat foot.
  - The two strokes cross at roughly the visual center (~150, 165).
  - 撇 is drawn FIRST in traditional stroke order.
Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def bezier_points(p0, p1, p2, n=80):
    """Quadratic Bezier."""
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_tapered_stroke(draw_obj, points, w_start, w_end):
    """Draw a stroke with linearly-tapered width along the path via
    stacked dabs (circles)."""
    n = len(points)
    for i, (x, y) in enumerate(points):
        t = i / (n - 1)
        w = w_start * (1 - t) + w_end * t
        r = w / 2.0
        draw_obj.ellipse(
            [x - r, y - r, x + r, y + r], fill="black"
        )


# 撇 — start upper-right, sweep down-left with a PRONOUNCED rightward
# bow (curves like a comma). Thick→thin taper. The GT shows a small
# hooked head at the top (a tiny 顿 that curls slightly).
pie_start = (198, 62)
pie_ctrl = (175, 145)   # control point well to the right of midline → strong bow
pie_end = (58, 268)
pie_pts = bezier_points(pie_start, pie_ctrl, pie_end, n=120)
draw_tapered_stroke(draw, pie_pts, w_start=9, w_end=3)
# Tiny head-curl on 撇 (the GT's little top flick).
draw.ellipse([pie_start[0] - 5, pie_start[1] - 4,
              pie_start[0] + 5, pie_start[1] + 4], fill="black")

# 捺 — start upper-left, sweep down-right with a VISIBLE downward bow
# (control point pulled down-and-right of midline). Thin→thick with a
# broad foot at the bottom-right.
na_start = (85, 95)
na_ctrl = (130, 195)    # control below midline → belly curves downward
na_end = (240, 258)
na_pts = bezier_points(na_start, na_ctrl, na_end, n=120)
draw_tapered_stroke(draw, na_pts, w_start=3, w_end=11)

# Broad terminal press on 捺's foot.
foot_x, foot_y = na_end
draw.ellipse(
    [foot_x - 8, foot_y - 6, foot_x + 8, foot_y + 6], fill="black"
)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0014_乂/01_乂.png"
)
print("Saved 01_乂.png")
