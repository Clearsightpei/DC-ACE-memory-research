"""Render 太 (p3_char_0128) — 大 + interior 点.

# SIGNATURE CHECK (per sibling_signature_checklist.md):
#   target = 太
#   bit = 一 + 撇+捺 sharing apex ON the 一, PLUS interior 点 between the legs
#         (contrast 大: no dot; 犬: dot upper-right ABOVE the 一)
#   flick = none (no hook strokes)

Structure (reuses p3_char_0041_大 body, adds one dot):
  1. 一 (horizontal) spanning mid-upper area
  2. 撇 (pie), sweeps down-left through 一
  3. 捺 (na), sweeps down-right through 一, thick foot
  4. 点 (dian) — small interior teardrop below the 一, tucked between
     the descending 撇 and 捺 (GT shows it in the lower crotch area).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    """Draw a variable-width stroke by dabbing circles along interpolated path."""
    if len(points) < 2:
        return
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
one_pts = [(50, 148), (100, 142), (185, 138), (250, 140)]
one_ws  = [10, 8, 8, 11]
brush_stroke(one_pts, one_ws)

# --- 2. 撇 (pie): short stub above 一, then long sweep down-left ---
pie_pts = [
    (152, 76),
    (149, 100),
    (146, 125),
    (144, 145),   # crossing point on 一
    (130, 185),
    (105, 225),
    (75, 268),
]
pie_ws = [9, 9, 9, 8, 7, 6, 4]
brush_stroke(pie_pts, pie_ws)

# --- 3. 捺 (na): from apex down-right, thin→thick with broad foot ---
na_pts = [
    (150, 88),
    (156, 115),
    (162, 143),
    (183, 180),
    (208, 218),
    (235, 252),
    (250, 262),
]
na_ws = [4, 6, 8, 10, 12, 14, 15]
brush_stroke(na_pts, na_ws)

# Broad flat terminal foot for 捺
fx, fy = 250, 262
draw.ellipse([fx - 6, fy - 4, fx + 10, fy + 4], fill="black")

# --- 4. 点 (interior dot): between the descending 撇 and 捺, below the 一 ---
# GT shows a small teardrop in the lower crotch, roughly x≈150-165, y≈225-245.
# Render as a short slanting dot going down-right (typical 点 direction).
dot_pts = [
    (148, 218),
    (155, 228),
    (163, 238),
]
dot_ws = [5, 8, 10]
brush_stroke(dot_pts, dot_ws)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0128_太/01_太.png"
img.save(out)
print("saved", out)
