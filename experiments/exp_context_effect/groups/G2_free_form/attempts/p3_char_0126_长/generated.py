"""
p3_char_0126_长 — 4 strokes.
Stroke order:
  1. 撇 (short, top-left) — small down-left flick
  2. 横 (long horizontal across middle)
  3. 竖提 (short vertical from below top-撇, ending with upward tick)
  4. 捺 (long down-right stroke from center descending to bottom-right)

Layout (300x300, math intuition on top-left origin, y grows DOWN):
- Top area ~y=90 for the small 撇
- Horizontal ~y=140 spanning x=60..230
- Vertical from ~y=95 to ~y=210 at x=100, then tick up-right to ~ (135,195)
- 捺 from (155,140) down-right to (245,255)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def brush_line(p0, p1, width=6):
    d.line([p0, p1], fill=INK, width=width)
    # round caps
    r = width // 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

def brush_poly(points, width=6):
    for i in range(len(points) - 1):
        brush_line(points[i], points[i + 1], width=width)

# Stroke 1: 撇 — small, meets top of the vertical (upper-left of char)
brush_line((122, 70), (95, 110), width=6)

# Stroke 2: 横 — long horizontal across middle
brush_line((45, 150), (245, 142), width=7)

# Stroke 3: 竖提 — vertical from top (touching 撇) down to bottom, then tick up-right
brush_poly([(95, 105), (95, 220)], width=7)
# tick (提) up-right
brush_line((95, 220), (145, 200), width=6)

# Stroke 4: 捺 — starts from upper-middle (near top of vertical/撇), sweeps down-right with flat tail
brush_poly([
    (135, 105),
    (165, 150),
    (195, 190),
    (225, 230),
    (255, 255),
], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0126_长/01_长.png")
print("saved")
