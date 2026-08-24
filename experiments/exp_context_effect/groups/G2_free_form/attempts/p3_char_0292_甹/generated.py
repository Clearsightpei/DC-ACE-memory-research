"""
Render 甹 (ping) — composed of 由 (top) + 丂-like bottom.
Structure from GT:
  - Top: 由-shape (rectangle with vertical cross bar, vertical extends
    slightly ABOVE the rectangle top).
  - Bottom: a long horizontal, then a 横折弯钩-style sweep dropping down
    and curling back with an UP-and-LEFT terminal flick.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
BR = 6  # brush


def line(p0, p1, w=BR):
    d.line([p0, p1], fill=BLACK, width=w)


def stroke(pts, w=BR):
    d.line(pts, fill=BLACK, width=w, joint="curve")


# ---- TOP: 由 ------------------------------------------------------
# The vertical of 由 protrudes ABOVE the rectangle (like a stem)
# Rectangle roughly centered horizontally, top half of canvas.
rect_left, rect_right = 100, 200
rect_top, rect_bottom = 55, 155

# vertical stem: from y=30 (above rect) down to y=155 (rect bottom)
line((150, 30), (150, 155), w=BR)

# left vertical (of 由)
line((rect_left, rect_top), (rect_left, rect_bottom), w=BR)

# right vertical + hook at bottom-right (like 横折)
line((rect_right, rect_top), (rect_right, rect_bottom), w=BR)

# top horizontal (rect_top)
line((rect_left, rect_top), (rect_right, rect_top), w=BR)

# middle horizontal (inside 由 — the cross bar)
line((rect_left, 105), (rect_right, 105), w=BR)

# bottom horizontal of the 由 rectangle
line((rect_left, rect_bottom), (rect_right, rect_bottom), w=BR)

# ---- BOTTOM: long 横 + 横折弯钩 sweep -----------------------------
# Long horizontal below the rectangle, extending wider than 由
h_left, h_right = 55, 245
h_y = 185
line((h_left, h_y), (h_right, h_y), w=BR)

# 横折弯钩: starts from right side of horizontal, drops down and curves
# Sketch as a smooth polyline: down-right diagonal, then curve leftward,
# then hook up-left at the terminal.
hook_pts = [
    (h_right - 10, h_y + 2),   # start (just under the right end of long 横)
    (225, 210),
    (215, 235),
    (195, 255),
    (165, 268),
    (135, 265),
    (120, 258),  # terminal — flick up-and-left
]
stroke(hook_pts, w=BR)

# Small terminal flick up-and-left
line((120, 258), (108, 250), w=BR)

img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0292_甹/01_甹.png"
)
print("saved")
