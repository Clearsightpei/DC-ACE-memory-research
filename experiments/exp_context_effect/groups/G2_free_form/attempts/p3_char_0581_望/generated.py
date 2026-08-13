"""
望 (wàng) — 11 strokes
Structure: top-left 亡 (3 strokes: 点/短横, 竖折), top-right 月 (4 strokes),
bottom 王 (4 strokes). Actually more properly:
  top-left: 亡 (点 + 横 + 竖折) — 3 strokes
  top-right: 月 (撇 + 横折钩 + 横 + 横) — 4 strokes
  bottom: 王 (横 + 横 + 竖 + 横) — 4 strokes
Total = 11.

Applying calligraphic-weight 4-move: tapered strokes for 撇/点,
components touch, hook flicks up-and-left.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(points, widths):
    """Draw a stroke with per-point interpolated width via ellipses."""
    if len(widths) == 2:
        w0, w1 = widths
        widths = [w0 + (w1 - w0) * i / max(1, len(points) - 1) for i in range(len(points))]
    # sample line segments densely so tapered ellipses overlap
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        r0 = widths[i] / 2
        r1 = widths[i + 1] / 2
        steps = max(2, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = r0 + (r1 - r0) * t
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line(p0, p1, w=5):
    stroke([p0, p1], [w, w])


# ============ TOP-LEFT: 亡 ============
# 亡 has 3 strokes: 点 (dot at top), 横 (short horizontal), 竖折 (vertical then turn right)
# Positioned in top-left quadrant; 竖折 horizontal stays within left half
# 点 (top dot)
stroke([(50, 45), (68, 58)], [3, 7])
# 横 (short horizontal) — top of 亡
stroke([(30, 75), (115, 72)], [5, 5])
# 竖折 (vertical down then horizontal right — stays within left half)
stroke([(55, 78), (55, 128)], [5, 5])
stroke([(55, 128), (105, 126)], [5, 5])

# ============ TOP-RIGHT: 月 ============
# 月 — narrow tall rectangle on right side
# 撇 — left side, curving, tapered
stroke([(155, 55), (145, 90), (130, 135)], [7, 5, 2])
# 横折钩 — top 横, then down 竖, then hook up-and-left
stroke([(160, 60), (240, 55)], [5, 6])  # top 横
stroke([(240, 55), (233, 138)], [6, 6])  # right 竖
# hook flicks UP-and-LEFT
stroke([(233, 138), (215, 128)], [6, 2])
# inner 横 (2 shorter horizontals inside)
stroke([(158, 90), (228, 88)], [4, 4])
stroke([(155, 115), (230, 113)], [4, 4])

# ============ BOTTOM: 王 ============
# 王 has 4 strokes: 横, 横, 竖, 横 (bottom is longest)
# Positioned in bottom, touching top row
# top 横
stroke([(75, 165), (210, 163)], [5, 5])
# middle 横 (shorter)
stroke([(95, 205), (190, 203)], [5, 5])
# 竖 (vertical through middle)
stroke([(143, 165), (143, 250)], [5, 5])
# bottom 横 (longest)
stroke([(50, 250), (240, 248)], [6, 6])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0581_望/01_望.png")
