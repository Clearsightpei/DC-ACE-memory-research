"""Render 着 (zhāo/zhe) at 300x300, black ink on white.

Structure:
- Top: 丷 (two short dots/slashes)
- Three horizontals of the 羊-ish upper component
- Long 撇 sweeping down-left through the middle
- 目 in the lower-right, tucked under the horizontals, right of the 撇
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def poly(pts, w=3):
    d.line(pts, fill="black", width=w, joint="curve")

# --- Top 丷 (two slashes) ---
poly([(115, 45), (128, 68)], w=3)   # left dot
poly([(178, 45), (165, 68)], w=3)   # right dot

# --- Horizontal 1 (top of 羊) ---
poly([(85, 90), (215, 90)], w=3)

# --- Horizontal 2 ---
poly([(95, 118), (208, 118)], w=3)

# --- Long 撇 (major diagonal, upper-right to lower-left) ---
poly([(205, 78), (185, 135), (140, 190), (95, 245), (60, 285)], w=4)

# --- Horizontal 3 (crosses the 撇, extends right) ---
poly([(110, 150), (240, 150)], w=3)

# --- 目 (lower-right rectangle) ---
box_l, box_r = 155, 235
box_t, box_b = 175, 275
# left vertical
poly([(box_l, box_t), (box_l, box_b)], w=3)
# right vertical
poly([(box_r, box_t), (box_r, box_b)], w=3)
# top
poly([(box_l, box_t), (box_r, box_t)], w=3)
# middle 1
poly([(box_l + 3, 208), (box_r - 3, 208)], w=2)
# middle 2
poly([(box_l + 3, 240), (box_r - 3, 240)], w=2)
# bottom
poly([(box_l, box_b), (box_r, box_b)], w=3)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_着.png"))
print("saved")
