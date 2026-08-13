"""
冱 = 冫 (left) + 互 (right).
Left: two-dot ice radical, compressed to left column.
Right: 互 - top 横, two interlocking 横折 forming middle, bottom 横 spanning.
GT trace: 冫 dots occupy left ~x40-90; 互 spans x100-260, y50-260.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def brush_stroke(pts, widths):
    n = len(pts)
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        steps = max(20, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2
            draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


# =============== LEFT: 冫 (ice radical, compressed) ===============
# Upper dot - short curve slanting down-right
upper_pts = [(45, 105), (55, 115), (65, 128), (72, 138)]
upper_widths = [3, 6, 8, 5]
brush_stroke(upper_pts, upper_widths)

# Lower stroke - curved down-left flick, longer
lower_pts = [(72, 175), (66, 190), (58, 210), (50, 230), (44, 245)]
lower_widths = [4, 7, 9, 8, 4]
brush_stroke(lower_pts, lower_widths)


# =============== RIGHT: 互 ===============
# Stroke 1: top 横 (top horizontal spanning right area)
top_h = [(105, 75), (170, 73), (240, 72), (260, 74)]
top_widths = [5, 7, 7, 6]
brush_stroke(top_h, top_widths)

# Stroke 2: 竖折 forming top-left of middle - down from top-left, then right toward middle
# Terminates around x=210, y=160 (not spanning full width) - interlocking style
s2_pts = [(115, 88), (115, 130), (117, 160), (155, 160), (200, 160), (215, 160)]
s2_widths = [6, 6, 6, 6, 6, 6]
brush_stroke(s2_pts, s2_widths)

# Stroke 3: 横折 forming bottom-right of middle - starts from left-mid, goes right then down
# Starts around x=145 (not from far-left), goes right to right edge, then down to bottom
s3_pts = [(148, 175), (185, 175), (220, 175), (240, 175), (240, 210), (240, 240)]
s3_widths = [6, 6, 6, 6, 6, 6]
brush_stroke(s3_pts, s3_widths)

# Stroke 4: bottom 横 (bottom horizontal spanning)
bot_h = [(100, 250), (170, 252), (240, 253), (265, 251)]
bot_widths = [5, 7, 7, 6]
brush_stroke(bot_h, bot_widths)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0286_冱/01_冱.png")
print("Saved 01_冱.png")
