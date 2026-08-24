"""
p1_stroke_11_横折 (heng-zhe): horizontal-then-turn-90°-down.

Shape reasoning:
- 横 segment: left → right, slightly rising (calligraphic convention:
  横 tilts up 3–5°). Uniform width, small 顿笔 at start and slight
  press at the corner.
- 折 corner: sharp ~90° turn; the ink presses briefly before the turn
  (a small squared-off shoulder), then drops downward.
- 竖 segment: from the corner, straight down, roughly uniform width,
  ending with a small blunt press (this stroke is 横折, NOT 横折钩,
  so no upward hook flick at the bottom).

Uses PIL brush-dabs (from drawer_memory.md) for a smooth calligraphic
look. Canvas 300×300, white bg, black ink, image coords y grows DOWN.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- 横 segment (horizontal, slight upward tilt) ---
# Start at upper-left region; end near upper-right corner where the
# 折 will happen. Slight rise: end y a few px above start y.
heng_start = (55, 95)
heng_end = (235, 78)

# 顿笔 (initial press): one slightly larger dab at the start.
r0 = 7.5
draw.ellipse(
    (heng_start[0] - r0, heng_start[1] - r0,
     heng_start[0] + r0, heng_start[1] + r0),
    fill="black",
)

# Horizontal body: roughly uniform, tiny thickening toward corner
# (the 折 shoulder is a press, so ramp end radius up a touch).
dab_line(heng_start, heng_end, r_start=5.5, r_end=7.0, steps=400)

# --- 折 corner (squared shoulder) ---
# A small filled block just past heng_end to give the corner its
# distinctive squared-off calligraphic "shoulder" before dropping.
shoulder_cx, shoulder_cy = heng_end[0] + 2, heng_end[1] + 4
draw.ellipse(
    (shoulder_cx - 8, shoulder_cy - 8,
     shoulder_cx + 8, shoulder_cy + 8),
    fill="black",
)

# --- 竖 segment (drop down from corner) ---
# Straight down from just below the shoulder; roughly uniform width,
# ending with a modest blunt press (no upward hook flick).
shu_start = (heng_end[0] + 1, heng_end[1] + 6)
shu_end = (heng_end[0] + 1, 240)

dab_line(shu_start, shu_end, r_start=6.5, r_end=5.5, steps=400)

# Small blunt press at the bottom endpoint.
r_end_press = 6.5
draw.ellipse(
    (shu_end[0] - r_end_press, shu_end[1] - r_end_press,
     shu_end[0] + r_end_press, shu_end[1] + r_end_press),
    fill="black",
)

out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_11_横折/01_横折.png"
)
img.save(out_path)
print(f"saved {out_path} size={img.size}")
