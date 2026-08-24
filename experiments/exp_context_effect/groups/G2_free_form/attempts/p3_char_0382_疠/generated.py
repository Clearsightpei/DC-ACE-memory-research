"""Render 疠 (illness radical 疒 + 万 inside) to 300x300 PNG.

Structure:
  - 疒 (illness radical) wraps top-left of the character:
      1. Top short 点 dot (upper area)
      2. Short 横 horizontal (below the dot)
      3. Long 撇 sweeping down-left from the horizontal
      4. Two 点 dots stacked on the left of the 撇 (inside the frame)
  - 万 sits in the lower-right pocket, containing:
      5. 横 (horizontal top)
      6. 横折钩 (turn down and hook up-left)
      7. 撇 (from top-right, sweeping down-left through the box)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(pts, w0=9, w1=9, steps=40):
    """Draw a smooth poly-line, tapering width w0->w1 with dense dabs."""
    n = len(pts)
    if n < 2:
        return
    # Densify by linear interp between control points
    dense = []
    segs = n - 1
    per = max(6, steps // segs)
    for i in range(segs):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        for k in range(per):
            t = k / per
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    m = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / (m - 1)
        ww = w0 + (w1 - w0) * t
        r = max(1, ww / 2)
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# --- 疒 illness radical (upper-left frame) ---

# 1. Top dot (点)
brush_line([(120, 40), (135, 58)], w0=7, w1=11)

# 2. Short horizontal (横)
brush_line([(90, 78), (210, 72)], w0=7, w1=7)

# 3. Long 撇 — sweeps from left of horizontal down-left
brush_line([(95, 72), (85, 130), (60, 190), (30, 265)], w0=10, w1=3)

# 4. Two dots on the left inside the frame (两点)
brush_line([(75, 130), (95, 148)], w0=6, w1=10)
brush_line([(60, 170), (80, 188)], w0=6, w1=10)

# --- 万 (inside/lower-right pocket) ---

# 5. Top horizontal of 万
brush_line([(130, 118), (235, 112)], w0=7, w1=7)

# 6. 横折钩 — vertical descending with hook flick up-left
brush_line([(220, 112), (222, 135), (215, 210), (198, 258)], w0=8, w1=5)
# hook flick UP-and-LEFT
brush_line([(198, 258), (178, 245)], w0=6, w1=3)

# 7. 撇 inside 万 — from upper corner sweeping down-left
brush_line([(185, 140), (160, 205), (125, 268)], w0=9, w1=3)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0382_疠/01_疠.png")
