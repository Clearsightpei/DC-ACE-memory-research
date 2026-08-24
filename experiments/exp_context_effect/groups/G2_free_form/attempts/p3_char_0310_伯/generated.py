"""
伯 (bó) — 7 strokes
Structure: 亻 (left, ~30% width) + 白 (right, ~65% width, 5 strokes)

Composed from prior PASSes:
  - 亻 pattern from p3_char_0022_亻 (steep pie + straight 竖)
  - 白 pattern from p3_char_0206_白 (short 撇 + box + inner 横 + bottom 横)

Layout on 300x300:
  - 亻 occupies x ~ 40..110, y ~ 55..250
  - 白 occupies x ~ 135..255, y ~ 65..260
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 8


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


# =========== LEFT: 亻 ============
# 撇 -- steep pie
pie_points = [(105, 58), (100, 85), (90, 115), (75, 150), (55, 185), (38, 215)]
pie_widths = [5.0, 5.0, 4.5, 4.0, 3.0, 1.5]
brush_stroke(pie_points, pie_widths)

# 竖 -- vertical drop, meets pie body
shu_points = [(92, 118), (92, 165), (92, 215), (92, 258)]
shu_widths = [5.0, 5.0, 5.0, 4.5]
brush_stroke(shu_points, shu_widths)
# small top 顿 dab
d.ellipse((88, 115, 97, 124), fill="black")


# =========== RIGHT: 白 ============
# short 撇 on top
d.line([(200, 60), (163, 108)], fill=INK, width=LW)

# Box coords
L, R = 155, 260
T, B = 105, 260

# 竖 -- left vertical of box
d.line([(L, T + 2), (L, B)], fill=INK, width=LW)

# 横折 -- top horizontal + right vertical
d.line([(L - 2, T), (R, T)], fill=INK, width=LW)
d.line([(R, T), (R, B)], fill=INK, width=LW)

# middle 横
MID_Y = T + (B - T) // 2 + 5
d.line([(L + 4, MID_Y), (R - 3, MID_Y)], fill=INK, width=LW)

# bottom 横
d.line([(L - 2, B), (R + 2, B)], fill=INK, width=LW)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0310_伯/01_伯.png"
)
print("saved")
