"""
Render 仗 (weapon/rely-on) to a 300x300 PNG.

Composition: 亻 (left, tall-narrow ~35% width) + 丈 (right, ~60% width).
  Left 亻 (2 strokes): 撇 + 竖 -- reused from p3_char_0022 template,
  shifted left and scaled to occupy x=[35..115].
  Right 丈 (3 strokes):
    1) 横 -- short horizontal at top-right.
    2) 撇 -- long left-falling from just below the 横, sweeping to lower-left.
    3) 捺 -- long right-falling from an X-crossing near center-right,
       sweeping to lower-right (thick tail, calligraphic).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        seg = max(abs(dx), abs(dy))
        steps = max(int(seg) * 2, 8)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = w0 * (1 - t) + w1 * t
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============ LEFT: 亻 (person radical) =============
# 撇 -- steep left-position pie
pie_points = [
    (95, 60),
    (90, 85),
    (80, 115),
    (68, 145),
    (52, 175),
    (35, 200),
]
pie_widths = [5.0, 5.0, 4.5, 4.0, 3.2, 1.8]
brush_stroke(pie_points, pie_widths)

# tiny head curl
head_curl = [(95, 60), (100, 66), (97, 75)]
head_widths = [5.0, 3.8, 2.4]
brush_stroke(head_curl, head_widths)

# 竖 -- vertical drop
shu_points = [
    (82, 118),
    (82, 165),
    (82, 215),
    (82, 258),
]
shu_widths = [5.2, 5.2, 5.2, 5.0]
brush_stroke(shu_points, shu_widths)
d.ellipse((78, 115, 87, 124), fill="black")


# ============ RIGHT: 丈 =============
# 1) 横 -- short horizontal near top-right
heng_points = [
    (145, 82),
    (180, 80),
    (215, 78),
    (245, 78),
]
heng_widths = [4.0, 4.8, 4.8, 5.2]
brush_stroke(heng_points, heng_widths)
# small 顿 at right end
d.ellipse((242, 74, 252, 84), fill="black")

# 2) 撇 -- long left-falling from below 横 midpoint,
# curves gently down-left through the character body to bottom-left.
pie2_points = [
    (205, 80),   # head at 横 mid-right
    (198, 105),
    (188, 130),
    (172, 160),
    (150, 190),
    (125, 220),
    (100, 250),  # thin tail (deep into lower-left)
]
pie2_widths = [5.8, 5.4, 5.0, 4.4, 3.6, 2.6, 1.5]
brush_stroke(pie2_points, pie2_widths)

# 3) 捺 -- long right-falling forming X with 撇 around middle.
# Sweeps from upper-mid down to bottom-right corner, thick tail flick.
na_points = [
    (165, 115),  # cross start (thin, above 撇 midpoint)
    (180, 140),
    (200, 170),
    (225, 200),
    (250, 225),
    (272, 245),  # thick tail end
]
na_widths = [1.8, 3.0, 4.2, 5.4, 6.6, 5.0]
brush_stroke(na_points, na_widths)
# tail flick -- horizontal press-out at end
tail = [(272, 245), (288, 248)]
tail_w = [5.0, 1.8]
brush_stroke(tail, tail_w)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0177_仗/01_仗.png"
)
