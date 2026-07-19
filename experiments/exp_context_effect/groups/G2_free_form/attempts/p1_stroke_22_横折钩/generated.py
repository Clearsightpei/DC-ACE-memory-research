"""
p1_stroke_22_横折钩 — 横折 + 钩 flick at bottom of the 竖.

Structure (image coords, y grows DOWN, 300x300 canvas):
  1) 横 primary: slight up-tilt, uniform r~5, small 顿-dabs at start & end
     start=(55, 100), end=(220, 88)
  2) Shoulder 顿-dab at the corner (~r+3) at (220, 88)
  3) 竖 secondary: straight down from (215, 90) to (208, 235),
     uniform r~5, ramp-up near bottom is minor (hook takes over)
  4) 钩 flick: from bottom endpoint of 竖 (208, 235),
     up-and-left to (168, 205); taper thick->thin (r 6 -> 1.2)

Techniques: brush-dab (linearly-varying-radius filled ellipses).
Memory reference:
- 横折 (batch-1 PASS): 横 slight up-tilt + shoulder-dab + 竖 straight down.
- 竖钩 (batch-1 PASS): hook flicks up-and-left from bottom.
- 横折钩 = 横折 body + 钩 flick appended at bottom of the 竖.
"""

from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(draw, p0, p1, r0, r1, steps=None):
    """Brush-dab straight segment with linearly varying radius."""
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        steps = max(60, int(length * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def press_dab(draw, p, r):
    x, y = p
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- 1) 横 primary: (55, 100) -> (220, 88), slight up-tilt, uniform r=5
heng_start = (55, 100)
heng_end = (220, 88)
press_dab(draw, heng_start, 7)          # 顿 dab at start
dab_line(draw, heng_start, heng_end, 5, 5.5)  # slight ramp-up toward corner

# --- 2) Shoulder 顿 dab at the corner
shoulder = (220, 88)
press_dab(draw, shoulder, 8)

# --- 3) 竖 secondary: (215, 90) -> (208, 235), essentially straight down
shu_start = (215, 90)
shu_end = (208, 235)
dab_line(draw, shu_start, shu_end, 6, 5.5)

# --- 4) 钩 flick: up-and-left from bottom of 竖
hook_start = shu_end
hook_end = (168, 205)   # up-and-left, ~40-45 px flick
# Joining dab at start of hook to hide seam
press_dab(draw, hook_start, 6.5)
dab_line(draw, hook_start, hook_end, 6, 1.2)

# Save
out = Path(__file__).parent / "01_横折钩.png"
img.save(out)
print(f"Saved {out}")
