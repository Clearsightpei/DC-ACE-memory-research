"""処 (chu) — 5 strokes. Revised pass 2.

Structure per GT: outer 几 envelope wrapping inner 夂 in upper-left.
Stroke order:
  1. Small top 撇 (夂 header) — short diagonal upper-center
  2. 横撇 of 夂 — horizontal then diagonal descending
  3. Long 捺 of 夂 — sweeping down-right through the envelope
  4. Left 撇 of 几 — starts upper-mid, descends to bottom-left
  5. 横折弯钩 of 几 — top-right shoulder, down, right-curving hook

Widths uniform ~5-6 px (GT is thin uniform line).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 夂 (inner, upper-left) ----
# Stroke 1: short 撇 at top
line([(130, 55), (105, 90)], width=5)

# Stroke 2: 横撇 (short heng, then pie down-left)
line([(85, 90), (160, 90)], width=5)         # heng
line([(160, 90), (145, 105), (110, 150)], width=5)  # pie down

# Stroke 3: long 捺 of 夂 — from mid-upper region sweeping to lower-right
line([(125, 105), (155, 155), (195, 210), (240, 260)], width=5)

# ---- 几 (outer envelope) ----
# Stroke 4: left 撇 of 几 — starts upper (near stroke 2 area), curves down to bottom-left
line([(105, 100), (95, 165), (75, 225), (55, 275)], width=5)

# Stroke 5: 横折弯钩 — top horizontal starts near where 4 starts, extends right
# then down and curves right into a hook
line([(150, 105), (245, 105)], width=5)                       # top heng
line([(245, 105), (250, 175), (250, 230)], width=5)           # down
line([(250, 230), (255, 260), (275, 275)], width=5)           # curve out
line([(275, 275), (275, 260)], width=5)                       # small hook up

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_処.png"))
print("wrote 01_処.png")
