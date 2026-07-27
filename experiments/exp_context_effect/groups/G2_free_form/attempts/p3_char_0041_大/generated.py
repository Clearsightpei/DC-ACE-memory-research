"""Render 大 (p3_char_0041) — 一 + 人.

Structure from GT + form_catalog:
  - 一 (horizontal), spans mid-upper area, meets both diagonals
  - 撇 (pie), starts near top-center, sweeps down-left through 一
  - 捺 (na), starts at same apex, sweeps down-right through 一,
    ends thick with flat foot
Sibling bit (form_catalog): 大 = 一 + 人 (no interior 点, no upper-right 点).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def brush_stroke(points, widths):
    """Draw a variable-width stroke by dabbing circles along interpolated path."""
    if len(points) < 2:
        return
    # Densify: for each segment, walk in small steps
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        dx, dy = x1 - x0, y1 - y0
        seg_len = max(1.0, (dx * dx + dy * dy) ** 0.5)
        steps = int(seg_len) + 1
        for s in range(steps + 1):
            t = s / steps
            x = x0 + t * dx
            y = y0 + t * dy
            w = w0 + t * (w1 - w0)
            r = max(1, w / 2)
            draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# --- 1. 一 (horizontal) ---
# Wide horizontal, slight up-tilt then flat, thicker at both ends
one_pts = [(50, 148), (100, 142), (185, 138), (250, 140)]
one_ws  = [10, 8, 8, 11]
brush_stroke(one_pts, one_ws)

# --- 2. 撇 (pie): starts as a short stub ABOVE 一, then long sweep down-left ---
# Upper stub at (150, 78) descending mostly vertically to (145, 140) then curving out
pie_pts = [
    (152, 76),
    (149, 100),
    (146, 125),
    (144, 145),   # crossing point on 一
    (130, 185),
    (105, 225),
    (75, 268),
]
pie_ws = [9, 9, 9, 8, 7, 6, 4]  # tapers thin at tail
brush_stroke(pie_pts, pie_ws)

# --- 3. 捺 (na): from apex down-right, thin→thick with broad foot ---
# Starts thin at apex, crosses 一 near (162, 143), broadens to a flat foot at (245, 260)
na_pts = [
    (150, 88),
    (156, 115),
    (162, 143),
    (183, 180),
    (208, 218),
    (235, 252),
    (250, 262),
]
na_ws = [4, 6, 8, 10, 12, 14, 15]  # thickens toward foot
brush_stroke(na_pts, na_ws)

# Broad flat terminal foot for 捺 (extend rightward horizontally)
fx, fy = 250, 262
draw.ellipse([fx - 6, fy - 4, fx + 10, fy + 4], fill="black")

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0041_大/01_大.png")
print("saved")
