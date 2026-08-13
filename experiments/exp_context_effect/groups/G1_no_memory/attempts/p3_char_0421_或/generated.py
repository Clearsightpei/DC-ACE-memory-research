"""Render 或 to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=BLACK, width=w)

def poly(points, w=LW):
    d.line(points, fill=BLACK, width=w, joint="curve")

# 或 layout:
#  - 一 top horizontal spanning middle-upper
#  - 口 (small mouth) on the left, below the horizontal
#  - 戈 wrapping the right: short 撇 upper-left, long 斜钩 diagonal with hook, dot upper-right
#  - long 横 base underneath 口 (also part of 戈's structure)

# --- top horizontal 一 (part of 戈 upper) ---
poly([(70, 110), (215, 100)], LW)

# --- short 撇 (left-falling) at top ---
poly([(115, 85), (95, 115)], LW)

# --- long 斜钩 (main diagonal of 戈) with terminal hook ---
# starts near top, sweeps down-right in a slight curve, ends with small upward hook
poly([(170, 80), (185, 130), (205, 175), (225, 220), (240, 250), (255, 240)], LW)

# --- dot 点 upper right ---
poly([(230, 90), (250, 108)], LW)

# --- 口 (mouth) bottom-left ---
# top edge
poly([(75, 150), (140, 148)], LW)
# left vertical
poly([(78, 150), (80, 210)], LW)
# right vertical (with slight inward)
poly([(140, 148), (138, 210)], LW)
# bottom of mouth
poly([(80, 210), (140, 208)], LW)

# --- long base horizontal underneath (extends across) ---
poly([(55, 240), (215, 232)], LW)

out = Path(__file__).parent / "01_或.png"
img.save(out)
print(f"Saved {out}")
