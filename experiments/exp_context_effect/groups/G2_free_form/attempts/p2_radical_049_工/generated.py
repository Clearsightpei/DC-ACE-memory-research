"""
p2_radical_049_工 — Drawer G2 attempt 1

工 (gong) is a 3-stroke radical:
  1. Top 横 (heng): short-ish horizontal, slight up-tilt.
  2. Middle 竖 (shu): vertical descender centered on the top 横 mid-point.
  3. Bottom 横: WIDER than top 横 (this is the character's signature),
     slight up-tilt, small terminal press on both ends.

Standalone-scale (per drawer_memory.md "Standalone vs compound"):
- Use small 顿-dabs (r+1) at endpoints, not r+2 balls.
- Fill the frame — top 横 at y~95, bottom 横 at y~215.
- Middle 竖 roughly centered horizontally, connecting top-mid to
  bottom-mid.
"""

from PIL import Image, ImageDraw

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- Stroke 1: top 横 (shorter horizontal) ---
# Slight up-tilt: left endpoint lower than right endpoint.
top_x0, top_y0 = 90, 100
top_x1, top_y1 = 210, 92
r_top = 5.0
# Initial 顿 dab
dab(top_x0, top_y0, r_top + 1.5)
line_dabs(top_x0, top_y0, top_x1, top_y1, r_top, r_top, steps=300)
# Terminal small press
dab(top_x1, top_y1, r_top + 1)

# --- Stroke 2: middle 竖 (vertical) ---
# Roughly centered at x=150; connects near top 横 mid to bottom 横 mid.
# Top 横 mid y ≈ 96; bottom 横 mid y ≈ 205. 竖 spans y=100→210.
mid_x = 150
mid_y0 = 100
mid_y1 = 208
r_mid = 5.0
dab(mid_x, mid_y0, r_mid + 1)  # small joining dab where it meets top 横
line_dabs(mid_x, mid_y0, mid_x, mid_y1, r_mid, r_mid, steps=300)
dab(mid_x, mid_y1, r_mid + 1)  # small joining dab at bottom join

# --- Stroke 3: bottom 横 (WIDER than top) ---
# Wider: spans roughly x=55→255. Slight up-tilt.
bot_x0, bot_y0 = 55, 220
bot_x1, bot_y1 = 255, 210
r_bot = 5.5
dab(bot_x0, bot_y0, r_bot + 1.5)  # 顿 at start
line_dabs(bot_x0, bot_y0, bot_x1, bot_y1, r_bot, r_bot, steps=400)
dab(bot_x1, bot_y1, r_bot + 1)

img.save("01_工.png")
print("Wrote 01_工.png")
