"""Render 孓 (jué) — 3 strokes:
  1) 横撇弯钩 (top head + neck): short 横 then folds down into a bowed 撇 that
     hooks back — forms the "head" loop of the 子-family.
  2) 竖钩 (vertical hook): a mostly-vertical straight stroke that ends with
     a flick up-and-left at the bottom.
  3) 横 (middle cross-bar): long horizontal through the middle, tilted very
     slightly up to the right — this REPLACES the bottom 横 of 子 and is
     what distinguishes 孓 from 子.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier_pts(pts, n=80):
    """Cubic-ish Bezier via de Casteljau for arbitrary control-point count."""
    out = []
    m = len(pts) - 1
    for i in range(n + 1):
        t = i / n
        cur = list(pts)
        for k in range(m, 0, -1):
            cur = [(cur[j][0] * (1 - t) + cur[j + 1][0] * t,
                    cur[j][1] * (1 - t) + cur[j + 1][1] * t)
                   for j in range(k)]
        out.append(cur[0])
    return out

def stroke(pts, width_start, width_end, n=80):
    """Draw a Bezier stroke with linearly varying brush width via dabs."""
    curve = bezier_pts(pts, n)
    for i, (x, y) in enumerate(curve):
        t = i / max(1, len(curve) - 1)
        w = width_start * (1 - t) + width_end * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- Stroke 1: 横撇 top (head) ---
# Open shape: short 横 rising slightly, shoulder, then long bowed 撇
# sweeping down and to the LEFT. Not a closed loop.
stroke([(85, 90), (135, 82), (180, 78)], 7, 9)
# Shoulder + bowed 撇 down-left
stroke([(180, 78), (195, 92), (185, 118), (140, 135), (80, 138)],
       9, 4)

# --- Stroke 2: 竖钩 (vertical hook), slightly bowed left ---
stroke([(165, 105), (160, 150), (155, 210), (152, 245)], 8, 9)
# Hook flick up-and-left (prominent)
stroke([(152, 245), (135, 252), (115, 248), (100, 238)], 9, 3)

# --- Stroke 3: 横 (long middle cross-bar) ---
# Long horizontal through the middle, slightly bowed up.
stroke([(45, 200), (100, 194), (155, 192), (215, 194), (255, 198)], 7, 7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0076_孓/01_孓.png")
print("wrote 01_孓.png")
