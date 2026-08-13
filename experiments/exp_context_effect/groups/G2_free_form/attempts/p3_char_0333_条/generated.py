"""
条 (tiáo) — 7 strokes
Structure: 夂 on top (3 strokes: 撇, 横撇/横折, 捺)
           木 on bottom (4 strokes: 横, 竖, 撇, 捺)
The two 捺 dominate — top 捺 sweeps down-right diagonally,
木's 横 sits under the top 捺's crossing, 木's 竖 drops from
the horizontal, then 撇/捺 splay outward.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

def bezier(p0, p1, p2, width=6, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t*t * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t*t * p2[1]
        pts.append((x, y))
    d.line(pts, fill="black", width=width, joint="curve")

# ---------- Top: 夂 (occupies roughly y=35..175) ----------
# Stroke 1: 撇 — starts upper-middle, curves down-left, long
bezier((180, 40), (145, 100), (70, 175), width=6)

# Stroke 2: 横撇 (short horizontal then flick down-left)
line([(160, 80), (215, 80)], width=6)
bezier((215, 80), (205, 100), (170, 130), width=6)

# Stroke 3: 捺 (top) — big diagonal sweep down-right, crossing stroke 1
bezier((150, 105), (200, 150), (260, 195), width=7)

# ---------- Bottom: 木 (compressed, y=175..275) ----------
# Stroke 4: 横 — horizontal, sits under the 夂 crossing
line([(55, 200), (245, 200)], width=6)

# Stroke 5: 竖 — vertical from horizontal down through
line([(150, 185), (150, 285)], width=6)

# Stroke 6: 撇 — small, from vertical top area curving down-left
bezier((150, 210), (115, 245), (70, 285), width=6)

# Stroke 7: 捺 — small, sweeping down-right
bezier((150, 210), (190, 245), (240, 285), width=7)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_条.png"))
print("saved")
