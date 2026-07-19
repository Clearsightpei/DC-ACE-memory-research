"""
p2_radical_078_幺 (3画 radical)

Structural decomposition (from GT visual inspection + memory):
  幺 = 撇折 (small, top) + 撇折 (larger, middle) + 点 (bottom-right)

The two 撇折 stack vertically, each one an angle: a short bowed 撇
(upper-right → lower-left) meeting a short rightward 横 at a shoulder
dab (memory: "撇折 family — 撇 tip → shoulder-dab → short 横 rightward").
The second 撇折 sits below the first and is bigger. A small teardrop 点
closes at the lower-right.

Renderer: PIL brush-dabs (memory-preferred). 300x300 white, black ink.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400):
    """Quadratic Bezier stroke with linearly interpolated radius."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def line_stroke(p0, p1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def pie_zhe(pie_p0, pie_ctrl, pie_p2, heng_end, r_pie_start=7, r_pie_end=3.5, r_heng=4):
    """Render a 撇折: bowed 撇 → shoulder-dab at tip → short 横 rightward.
    Memory: "撇折: 撇 primary + shoulder-dab at tip + short 横 rightward
    with slight up-tilt + terminal press"."""
    # Start press (顿笔) on 撇
    dab(pie_p0[0], pie_p0[1], r_pie_start + 1)
    # Bowed 撇 (upper-right → lower-left), thick → thin
    bezier_stroke(pie_p0, pie_ctrl, pie_p2, r_pie_start, r_pie_end, steps=300)
    # Shoulder dab at joint
    dab(pie_p2[0], pie_p2[1], r_pie_end + 2)
    # Short 横 rightward from tip to heng_end
    line_stroke(pie_p2, heng_end, r_heng, r_heng, steps=200)
    # Terminal small press at 横 end
    dab(heng_end[0], heng_end[1], r_heng + 1)


# --- Stroke 1: TOP 撇折 (small) ---
# Small size, sits in upper portion (~y 55-105)
# 撇 throws from upper-right (~155, 55) down-left to (~120, 100)
# Then short 横 rightward to (~165, 98) with slight up-tilt
pie_zhe(
    pie_p0=(158, 58),
    pie_ctrl=(148, 78),
    pie_p2=(118, 100),
    heng_end=(168, 96),
    r_pie_start=6,
    r_pie_end=3,
    r_heng=3.5,
)

# --- Stroke 2: MIDDLE 撇折 (larger) ---
# Bigger, sits in middle-lower portion, offset slightly left/down
# 撇 throws from upper-right (~170, 115) down-left to (~90, 195)
# Then 横 rightward to (~175, 190) - the "belly" of the character
pie_zhe(
    pie_p0=(175, 115),
    pie_ctrl=(155, 155),
    pie_p2=(88, 195),
    heng_end=(178, 188),
    r_pie_start=8,
    r_pie_end=3.5,
    r_heng=4,
)

# --- Stroke 3: 点 (teardrop dot) at bottom-right ---
# Short teardrop, thin → thick, going down-right
# Memory: "点: short teardrop, thin→thick, ~30-50 px long"
def teardrop(p0, p1, r0=2, r1=8, steps=200):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** 1.4  # easing for taper
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    # Terminal press
    dab(p1[0], p1[1], r1 + 1)


teardrop((160, 215), (200, 258), r0=2, r1=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_078_幺/01_幺.png")
print("saved 01_幺.png")
