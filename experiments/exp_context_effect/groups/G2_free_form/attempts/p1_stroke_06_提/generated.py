"""
p1_stroke_06_提 (rising stroke / ti)

提 (tí) — the "rising" stroke:
  - Starts at lower-left, ends at upper-right.
  - Begins with a small "press" (顿笔) giving a thicker head,
    then tapers to a sharp point at the upper-right tip.
  - Angle is roughly 25–35 degrees above horizontal.

Rendered with PIL by stacking small circular "brush dabs" along a
line from (start) to (end), with radius decreasing linearly from
r_start (thicker) to r_end (near-zero) to get the taper.

Output: 300x300 white background, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Stroke endpoints in image coords (origin top-left, y grows DOWN).
# Lower-left start, upper-right end.
x0, y0 = 70, 215   # lower-left (thick head)
x1, y1 = 240, 110  # upper-right (sharp tip)

# Brush taper: thick at start, near-zero at tip.
r_start = 11.0
r_end   = 1.0

# Small "press" (顿笔) at the head: add a slightly larger dab
# at the very beginning to suggest the initial pressure.
head_press_r = 13.0
draw.ellipse(
    (x0 - head_press_r, y0 - head_press_r,
     x0 + head_press_r, y0 + head_press_r),
    fill="black",
)

# Stamp dabs along the stroke.
n_steps = 400
for i in range(n_steps + 1):
    t = i / n_steps
    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * t
    r = r_start + (r_end - r_start) * t
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Confirm size and save.
assert img.size == (300, 300)
out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_06_提/01_提.png"
)
img.save(out_path)
print(f"Saved {out_path} size={img.size}")
