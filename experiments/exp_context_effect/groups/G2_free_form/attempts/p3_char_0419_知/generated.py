"""知 = 矢 (left) + 口 (right)
矢 strokes: 丿(短撇), 一(短横), 一(长横), 丿(撇), 丶(捺-变点)
口 strokes: 丨, 横折, 一
Left half compressed; right 口 sits mid-right, slightly below top.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6

def stroke(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

def bezier(p0, p1, p2, n=40, width=LW):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    stroke(pts, width=width)

# ----- 矢 (left half, occupies ~x 30-155) -----
# 1. 短撇 (top): small flick from upper-mid downward-left
bezier((110, 55), (100, 65), (75, 90), width=6)

# 2. 短横 (upper short horizontal, under the 撇)
stroke([(70, 105), (145, 105)], width=6)

# 3. 长横 (longer horizontal, middle band, crosses the vertical line)
stroke([(40, 155), (165, 150)], width=6)

# 4. 长撇 (main slanting stroke, from near top-mid diagonally down-left)
bezier((115, 130), (95, 195), (45, 265), width=7)

# 5. 捺 (bottom-right diagonal to the right, thickens toward tail)
bezier((105, 190), (135, 235), (170, 260), width=7)

# ----- 口 (right half, ~x 180-270, y 100-210) -----
x0, y0, x1, y1 = 180, 105, 270, 205
# left vertical (丨)
stroke([(x0, y0 + 5), (x0, y1)], width=6)
# top horizontal + right vertical (横折)
stroke([(x0 - 2, y0), (x1, y0)], width=6)
stroke([(x1, y0), (x1, y1 - 3)], width=6)
# bottom horizontal (一)
stroke([(x0 - 2, y1), (x1 + 3, y1)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0419_知/01_知.png")
