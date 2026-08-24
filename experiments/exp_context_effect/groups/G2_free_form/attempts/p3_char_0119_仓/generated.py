"""
仓 (cāng) — 仓-structure: 亽 top (人 + 一) + 巳-body pocket with inner 口

Strokes:
  1. 撇 — from apex (150,55) down-left, long curved to (35, 240)
  2. 捺 — from apex down-right, thick foot ending around (240, 210)
  3. 短横 — short horizontal under apex around y=125
  4. 横折钩 + inner 口 — bottom body pocket with hook up-left
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke_polyline(pts, width=9):
    draw.line(pts, fill=BLACK, width=width, joint="curve")


def taper_line(pts, w_start=4, w_end=12):
    n = len(pts) - 1
    for i in range(n):
        t = i / max(1, n - 1)
        w = int(round(w_start + (w_end - w_start) * t))
        draw.line([pts[i], pts[i + 1]], fill=BLACK, width=w)


def dab(xy, r=5):
    x, y = xy
    draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Stroke 1: 撇 (long left diagonal from apex, curving) ---
apex = (150, 55)
pie_pts = [
    apex, (140, 85), (125, 115), (105, 150),
    (85, 185), (60, 220), (40, 245)
]
# taper: thick near apex, thin at tail
taper_line(pie_pts, w_start=10, w_end=4)
dab(apex, r=6)

# --- Stroke 2: 捺 (down-right from apex, thick foot) ---
# End closer to bottom body's right edge, not past it
na_pts = [(155, 60), (175, 90), (195, 125), (215, 165), (230, 200), (245, 215)]
taper_line(na_pts, w_start=4, w_end=13)
# tail flick outward
draw.line([na_pts[-1], (263, 215)], fill=BLACK, width=11)

# --- Stroke 3: 短横 under apex ---
stroke_polyline([(112, 128), (188, 126)], width=8)
dab((112, 128), r=5)

# --- Stroke 4a: 横折钩 (outer bottom body) ---
# top of pocket around y=160, from x=95 to x=210
# then folds down along right wall to y=250
# then hooks up-left to (185, 235)
top = [(95, 158), (208, 158)]
right = [(208, 158), (212, 205), (212, 250)]
hook = [(212, 250), (198, 246), (183, 232)]

stroke_polyline(top, width=9)
dab((95, 158), r=5)
stroke_polyline(right, width=9)
stroke_polyline(hook, width=9)

# --- Stroke 4b: inner 口 (small pocket inside the bottom body) ---
# small rectangle around (120, 190) - (180, 235)
ix0, iy0, ix1, iy1 = 122, 188, 182, 232
stroke_polyline([(ix0, iy0), (ix1, iy0)], width=6)  # top
stroke_polyline([(ix0, iy0), (ix0, iy1)], width=6)  # left
stroke_polyline([(ix0, iy1), (ix1, iy1)], width=6)  # bottom
stroke_polyline([(ix1, iy0), (ix1, iy1)], width=6)  # right

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0119_仓/01_仓.png"
)
print("saved 01_仓.png")
