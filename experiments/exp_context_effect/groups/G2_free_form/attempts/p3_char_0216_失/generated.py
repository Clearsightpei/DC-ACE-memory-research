"""
失 (shī) — 5 strokes.
Stroke order:
  1. 撇 (short) — top little flick, right-of-center
  2. 横 — upper short horizontal
  3. 横 — middle long horizontal (widest)
  4. 撇 — long diagonal from top area down to bottom-left, slight curve
  5. 捺 — from center-mid down to bottom-right, widening
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=9):
    """Continuous stroke via connected line + endpoint dabs (round caps)."""
    d.line(pts, fill="black", width=width, joint="curve")
    r = width // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def tapered(pts, w_start, w_end):
    """Approximate a tapered stroke by drawing successive line segments
    with decreasing/increasing widths (denser sampling so no dotting)."""
    # densify
    n = 60
    xs = []
    for i in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        for k in range(n):
            t = k / n
            xs.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
    xs.append(pts[-1])
    m = len(xs)
    for i in range(m - 1):
        t = i / (m - 1)
        w = w_start + (w_end - w_start) * t
        r = w / 2
        x, y = xs[i]
        x2, y2 = xs[i + 1]
        d.line([(x, y), (x2, y2)], fill="black", width=max(1, int(round(w))))
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# 1. Top short 撇 — small flick pointing down and slightly left
tapered([(160, 55), (140, 92)], 8, 3)

# 2. Upper 横 — short horizontal
stroke([(122, 100), (198, 96)], width=8)

# 3. Middle 横 — long horizontal, widest, slight rise to right
stroke([(65, 152), (240, 148)], width=9)

# 4. Long 撇 — from top area down to bottom-left, smooth curve
tapered([(170, 62), (150, 130), (110, 200), (55, 275)], 10, 4)

# 5. 捺 — from where 撇 crosses middle 横, down-right, widening
tapered([(150, 165), (200, 220), (265, 275)], 5, 13)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0216_失/01_失.png")
print("saved")
