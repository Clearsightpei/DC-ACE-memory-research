"""Render 入 (radical) to a 300x300 PNG using PIL.

Revised to match GT more closely:
  1) 撇 (pie) — starts at ~(95,135) as a small hook, curves down-left
     to ~(80,245). Shorter than 捺; the top does NOT meet the 捺's top
     at a sharp peak (they cross with 捺 above).
  2) 捺 (na) — starts high at ~(135,100), curves down-right through
     ~(180,210) then bends toward horizontal ending near (245,250).
     Its top is higher than the 撇's top; it visually "covers" the
     junction with 撇 (they cross around (135, 160)).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, widths):
    n = len(points)
    samples_per_seg = 80
    dense = []
    dense_w = []
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        for s in range(samples_per_seg):
            t = s / samples_per_seg
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            dense.append((x, y))
            dense_w.append(w)
    dense.append(points[-1])
    dense_w.append(widths[-1])
    for (x, y), w in zip(dense, dense_w):
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ---------- Stroke 1: 撇 (pie) ----------
# Small hooked top (initial short right-curving nub in GT), then arcs
# down and slightly left, tapered tail. Top around (95, 135).
pie_points = [
    (108, 132),  # top hook-tip (slightly right of the main body)
    (98, 138),
    (92, 148),   # start of main body
    (92, 175),
    (90, 205),
    (85, 235),
    (80, 250),   # tail
]
pie_widths = [4, 6, 7, 7, 6, 5, 3]

stroke(pie_points, pie_widths)

# ---------- Stroke 2: 捺 (na) ----------
# Highest point of the character, well above the pie. Curves down-right
# then flattens toward horizontal at the tail.
na_points = [
    (135, 100),  # top apex (highest point)
    (150, 130),
    (170, 170),
    (190, 205),
    (210, 230),
    (230, 245),
    (250, 250),  # flat tail
    (258, 251),
]
na_widths = [5, 6, 8, 9, 10, 9, 6, 3]

stroke(na_points, na_widths)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_入.png")
img.save(out_path)
print(f"Wrote {out_path}")
