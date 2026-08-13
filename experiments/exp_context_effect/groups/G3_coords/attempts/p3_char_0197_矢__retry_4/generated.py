# TRAJECTORY DIFF for p3_char_0197_矢 (retry 4)
#
# GT: canvas-filling 矢 (~40..270 x-span, ~30..280 y-span). Five strokes:
#   (1) short top pie (upper-left, tilt down-left)
#   (2) short top heng (upper, from pie's tail rightward)
#   (3) long middle heng (main crossbar, spans ~40..270)
#   (4) long pie from middle-heng-center down to bottom-left
#   (5) long na from middle-heng-center down to bottom-right
#
# Prior attempts (main, r1, r2, r3): ALL small (~90..230 range,
# only ~140px wide). Bottom pie+na apex sat ABOVE the middle heng
# (X-cross fault). Top pie disconnected from top heng.
#
# Fixes this attempt:
#   (a) SIZE up — top heng width, middle heng width to match GT.
#   (b) Bottom pie + na APEX exactly on middle heng center (y = heng_y).
#   (c) Long pie/na extend nearly to bottom (y ~ 280).
#   (d) Top pie tail connects to top heng's left end.
#
# BANK_DEVIATION
# skipped: (any pie/heng/na primitives)
# reason: prior 4 attempts using per-primitive coords ended up small and
#   with apex above the heng; inline direct-coord render to control size
#   and apex-on-heng exactly.
# fresh_component: shi_inline_r4

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")

def taper_line(p0, p1, w0, w1, steps=40):
    # simple tapered line: draw several ellipses/lines along path
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = w / 2.0
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# ---- (1) top pie: short slash upper-left ----
# From (135, 40) down-left to (108, 78)
taper_line((135, 40), (108, 78), 5, 8, steps=30)

# ---- (2) top short heng: from ~ (108, 78) to (188, 72) ----
stroke([(105, 82), (192, 74)], width=7)

# ---- (3) long middle heng: main crossbar ----
# spans ~ (35, 148) to (270, 140) — slightly rising
heng_y_left = 152
heng_y_right = 138
stroke([(35, heng_y_left), (270, heng_y_right)], width=8)

# APEX on middle heng at x=150, y=~145
apex_x, apex_y = 150, 145

# ---- (4) long pie: from apex down to bottom-left, curving ----
# start at (apex, on heng), curve outward down-left
pie_pts = [
    (apex_x, apex_y),
    (apex_x - 15, apex_y + 30),
    (apex_x - 40, apex_y + 70),
    (apex_x - 70, apex_y + 105),
    (45, 275),
]
stroke(pie_pts, width=8)

# ---- (5) long na: from apex down to bottom-right, widening ----
# taper heavier na
na_start = (apex_x, apex_y)
na_end = (280, 285)
# use taper
taper_line(na_start, na_end, 5, 13, steps=60)

# save
out = os.path.join(os.path.dirname(__file__), "01_矢.png")
img.save(out)
print("wrote", out)
