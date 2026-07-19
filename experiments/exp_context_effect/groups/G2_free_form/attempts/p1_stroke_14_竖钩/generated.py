"""
p1_stroke_14_竖钩 (shu-gou, vertical-hook).

Shape: a straight vertical stroke (top -> bottom) with a short leftward-
and-upward hook flicking from the bottom endpoint. Rendered with PIL
brush-dabs per drawer_memory.md: uniform-width shu with a slight 顿
press at the top, a slightly-thickened joint at the bottom, then a
tapered hook flick up-and-left.

Canvas: 300x300, white bg, black ink.
Image coords: y grows DOWN.
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


# --- Primary vertical (竖) ---
# Centered horizontally around x = 150. Runs from near top to near bottom.
shu_top = (150, 55)
shu_bot = (150, 235)

# 顿笔 press at top: one larger dab before the ramp.
draw.ellipse((150 - 9, 55 - 8, 150 + 9, 55 + 8), fill="black")

# Uniform-ish vertical: start slightly thick, mild swell approaching
# the joint (per 折/钩 shoulder rule -> ramp up toward the corner).
dab_line(shu_top, shu_bot, r_start=7, r_end=8, steps=400)

# Joint press at the bottom of the vertical — the calligraphic 顿 that
# seats the hook onto the shu.
jx, jy = shu_bot
draw.ellipse((jx - 10, jy - 9, jx + 10, jy + 9), fill="black")

# --- Hook flick (钩) ---
# Flicks up-and-left from the joint. Short: ~28 px horizontal, ~22 px
# vertical rise. Tapers from joint-radius down to a sharp tip.
hook_start = (jx, jy)
hook_end = (jx - 30, jy - 24)
dab_line(hook_start, hook_end, r_start=9, r_end=1.2, steps=220)

img.save("01_竖钩.png")
print("Saved 01_竖钩.png (300x300)")
