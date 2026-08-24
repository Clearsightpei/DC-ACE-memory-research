"""G1 attempt for p2_radical_005_一 — horizontal stroke (1画 radical)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Horizontal stroke 一: matches GT — roughly middle-lower band, slight taper,
# thicker "顿笔" at both ends.
# GT looks like: y ~ 175, from x~70 to x~230, subtle wedge ends.

x_left, x_right = 70, 230
y_left, y_right = 190, 185  # slight upward tilt to match GT

# Main body: thinner overall to match GT weight; small 顿笔 at ends.
n = 120
for i in range(n + 1):
    t = i / n
    x = x_left + (x_right - x_left) * t
    y = y_left + (y_right - y_left) * t
    if t < 0.05:
        r = 3.5 + (0.05 - t) * 40  # left 顿笔
    elif t > 0.95:
        r = 3.5 + (t - 0.95) * 50  # right 顿笔 (slightly heavier)
    else:
        r = 3.2
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_005_一/01_一.png")
print("wrote 01_一.png")
