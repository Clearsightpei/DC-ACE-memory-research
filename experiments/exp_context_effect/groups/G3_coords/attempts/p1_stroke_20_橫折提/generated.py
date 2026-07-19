"""
p1_stroke_20_橫折提 — compound stroke: 横 (horizontal) + 折 (turn down) + 提 (rising).
Coordinate-based drawing using PIL. Output: 300x300 PNG, white bg, black ink.

Stroke path (image coords, y grows down):
  1) 横 (horizontal): (60, 100) -> (215, 95)  slight upward tilt, ends with small dun
  2) 折 (short vertical drop): (215, 95) -> (205, 165)  slight leftward slant
  3) 提 (rising stroke): (205, 165) -> (255, 130)  short upward-right, tapered end
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke_line(p0, p1, w0, w1, steps=60):
    """Draw a tapered line by stamping circles from width w0 to w1."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (w0 + (w1 - w0) * t) / 2.0
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# 1) 横 — horizontal, slight upward tilt, thick with slight taper, ending dun (thicker)
stroke_line((60, 102), (210, 96), w0=9, w1=11, steps=80)
# small dun (顿笔) at end of 横 — a slightly larger stamp
d.ellipse([210 - 8, 96 - 8, 210 + 8, 96 + 8], fill=BLACK)

# 2) 折 — the corner turn: short vertical drop, slightly leaning left, thick top -> slimmer bottom
stroke_line((214, 92), (204, 168), w0=12, w1=9, steps=60)

# 3) 提 — rising stroke: from bottom of 折, tapered from thick to fine, going up-right
stroke_line((204, 168), (258, 130), w0=11, w1=2, steps=80)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_20_橫折提/01_橫折提.png"
img.save(out_path)
print(f"saved {out_path}")
