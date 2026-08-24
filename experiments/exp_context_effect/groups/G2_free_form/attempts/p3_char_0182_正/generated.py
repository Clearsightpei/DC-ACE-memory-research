"""
正 — 5 strokes:
  1. 横 (top, short-medium)
  2. 竖 (left, longest vertical, slightly slanted per GT)
  3. 横 (middle, short — starts from left 竖, stops before right 竖 in GT? actually meets right 竖)
  4. 竖 (right, short — from top 横 down to middle 横)
  5. 横 (bottom, LONGEST — clearly wider than top)

Silhouette: square-ish, but bottom 横 is the widest stroke.
Not in sibling-signature checklist. No hooks.

Revision v2: bottom 横 made clearly wider than top; slight rightward
slant to top 横; middle 横 doesn't quite reach right 竖 to look more
calligraphic (was too box-like in v1).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=7):
    d.line(pts, fill=BLACK, width=width)
    for (x, y) in [pts[0], pts[-1]]:
        r = width // 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# 1. Top 横 (short, slightly upward tilt to right per GT)
stroke([(100, 82), (215, 76)], width=7)

# 2. Left 竖 (longest — spans from just under top 横 down to just above bottom 横; slight left-lean)
stroke([(115, 85), (98, 240)], width=8)

# 3. Middle 横 (short — from left 竖 rightward past center, stops before right 竖)
stroke([(108, 158), (195, 156)], width=7)

# 4. Right 竖 (short — from top 横's right end down to middle 横 level)
stroke([(205, 86), (200, 160)], width=7)

# 5. Bottom 横 (LONGEST — clearly widest of all strokes)
stroke([(60, 246), (245, 242)], width=9)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0182_正/01_正.png")
