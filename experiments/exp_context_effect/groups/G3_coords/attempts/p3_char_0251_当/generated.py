"""当 (dāng) — Phase 3 character. G3 fresh render.

Structure (from GT):
  Top group ~y40-95:
    - left dot 丶 slanting down-left  (upper-left of center)
    - middle short 竖 (vertical)
    - right 撇/dot slanting down-left from top-right
  Middle:
    - long 横 spanning ~x60-240 at y~140
  Bottom 彐-like enclosure:
    - top 横折 (opens the enclosure from left, turns down on right)
    - middle 横 (inside)
    - bottom 横 (closes enclosure, longer)
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def tapered(p0, p1, w0, w1, steps=40):
    """Draw a tapered line from p0 to p1 with width w0->w1."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t = i / (steps - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

def bow(p0, p1, ctrl, w0, w1, steps=60):
    """Quadratic bezier tapered."""
    x0, y0 = p0
    x1, y1 = p1
    cx, cy = ctrl
    for i in range(steps):
        t = i / (steps - 1)
        u = 1 - t
        x = u*u*x0 + 2*u*t*cx + t*t*x1
        y = u*u*y0 + 2*u*t*cy + t*t*y1
        w = w0 + (w1 - w0) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# --- Top group: 丷 with middle vertical (like 小 top) ---
# Left dot: slants down-LEFT
tapered((130, 45), (105, 88), 3, 8)
# Middle short vertical (竖)
tapered((150, 40), (150, 95), 6, 5)
# Right dot: slants down-LEFT (like 撇 short)
tapered((195, 45), (170, 88), 8, 3)

# --- Middle 横 (long horizontal) ---
tapered((55, 138), (240, 140), 5, 5)
# small hook/dot at right end
d.ellipse((236, 135, 246, 145), fill=BLACK)

# --- Bottom 彐 enclosure ---
# Top of enclosure: 横折 — horizontal then turn down (right side vertical)
# Horizontal part
tapered((70, 175), (222, 175), 5, 6)
# Turn down (right vertical, forms right side of box)
tapered((222, 175), (222, 262), 6, 5)

# Middle horizontal (inside)
tapered((85, 215), (215, 215), 4, 4)

# Bottom horizontal (closes box), slightly longer, extends past right
tapered((60, 262), (228, 262), 5, 5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_当.png"))
print("saved", os.path.join(out_dir, "01_当.png"))
