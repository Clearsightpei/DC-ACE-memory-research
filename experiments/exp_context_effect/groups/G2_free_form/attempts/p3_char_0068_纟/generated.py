"""
纟 (silk radical) — 3 strokes:
  1. Top 撇折  — short 撇 (down-left) then 折 (up-right), forming a small hook/loop
  2. Middle 撇折 — same shape, below, slightly wider
  3. Bottom 提  — long rising diagonal from lower-left to upper-right
Layout is vertical, narrow (left-radical scaling). Centered around x=150.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(p0, p1, width_start, width_end, steps=40):
    """Draw a tapered line by dabbing circles of interpolated radius."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = width_start + (width_end - width_start) * t
        r = w / 2.0
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def dot(x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ---- Stroke 1: top 撇折 ----
# 撇: short down-left curve
brush_line((155, 70), (130, 105), 5, 5)
# tiny shoulder dab
dot(130, 105, 4)
# 折: up-right rising line, slightly angled up
brush_line((130, 105), (165, 118), 5, 4)
dot(165, 118, 3)

# ---- Stroke 2: middle 撇折 ----
# 撇 (a bit wider than top)
brush_line((150, 138), (118, 175), 5, 5)
dot(118, 175, 4)
# 折
brush_line((118, 175), (172, 190), 5, 4)
dot(172, 190, 3)

# ---- Stroke 3: bottom 提 (long rising diagonal) ----
# Starts thick at lower-left, tapers to thin at upper-right
brush_line((95, 245), (205, 215), 7, 3)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0068_纟/01_纟.png"
)
