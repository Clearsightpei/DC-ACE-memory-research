"""往 (wǎng) — 8 strokes, left-right compound.
Left: 彳 (double-person radical, 3 strokes)
  1. 撇 (short upper flick)
  2. 撇 (longer middle flick)
  3. 竖 (long vertical drop)
Right: 主 (5 strokes)
  4. 丶 dot on top (tapered diagonal)
  5. 横 top horizontal (short)
  6. 横 middle horizontal (shortest)
  7. 竖 vertical through the horizontals
  8. 横 bottom horizontal (longest)

Proportions ~ left 35% / right 65%. Left compressed narrow.
Right 主's bottom 横 is widest.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    d.line(pts, fill="black", width=width, joint="curve")

def taper_stroke(pts, w_start=3, w_end=9):
    """Tapered brush stroke via dabs."""
    dense = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for s in range(steps + 1):
            t = s / max(steps, 1)
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    n = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(n - 1, 1)
        r = w_start + (w_end - w_start) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---------- LEFT: 彳 ----------
# 1. Upper 撇 - short flick from top
stroke([(80, 75), (70, 92), (55, 112)], width=7)

# 2. Middle 撇 - longer sweep
stroke([(95, 115), (75, 140), (50, 170)], width=8)

# 3. 竖 - long vertical drop
stroke([(88, 148), (85, 245)], width=9)

# ---------- RIGHT: 主 ----------
# 4. 丶 dot on top (tapered)
taper_stroke([(190, 55), (208, 82)], w_start=2, w_end=6)

# 5. 横 top horizontal (short)
stroke([(150, 108), (250, 105)], width=7)

# 6. 横 middle horizontal (shortest)
stroke([(165, 168), (240, 166)], width=7)

# 7. 竖 vertical through the three horizontals
stroke([(200, 105), (200, 245)], width=9)

# 8. 横 bottom horizontal (longest)
stroke([(135, 248), (200, 245), (275, 250)], width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0399_往/01_往.png")
print("wrote 01_往.png")
