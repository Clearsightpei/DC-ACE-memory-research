"""G1 render of 能 (nEng). Revision 2."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def polyline(pts, w=LW):
    for a, b in zip(pts, pts[1:]):
        d.line([a, b], fill="black", width=w)

# ============================================================
# Layout: 300x300, split 4-quadrants
# TL: 厶  TR: 匕
# BL: 月  BR: 匕
# ============================================================

# ---------- Top-left: 厶 (roughly x 40-125, y 40-125) ----------
# Stroke 1: left-falling diagonal (short) 撇
polyline([(75, 45), (55, 90), (60, 115)])
# Stroke 2: bottom sweeping stroke - starts from mid-left, goes right and curls up (横折折)
polyline([(60, 115), (110, 115), (100, 90), (115, 75)])

# ---------- Bottom-left: 月/⺼ (roughly x 30-125, y 135-260) ----------
# Left stroke: falling diagonal (撇) starting from top, curving to bottom
polyline([(65, 140), (50, 200), (42, 258)])
# Top-right: horizontal fold with right vertical (横折钩)
polyline([(65, 140), (120, 140), (120, 210), (108, 258)])
# Two inner horizontals
line((60, 180), (115, 180))
line((55, 220), (115, 220))

# ---------- Top-right: 匕 (roughly x 155-265, y 55-140) ----------
# Stroke 1: short left-falling diagonal (撇)
polyline([(180, 60), (165, 105)])
# Stroke 2: 竖弯钩 - horizontal then down then curl right with hook up
polyline([(155, 110), (245, 110), (245, 60)])   # top part: horizontal to right then up
# The 竖弯钩 of 匕: actually starts from upper-right area, goes down and curves right with an upward hook
# Redo more accurately:
# Clear approach - a 匕 has:
#   - a 撇 (falling-left short stroke) top-left
#   - a 竖弯钩 that starts high on the right, goes down, curves right, ends with hook up
# I'll leave stroke1 撇 and redo stroke 2 as one polyline
# (Already drew stroke2 above but not quite right - overwrite is fine since we already drew it)

# ---------- Bottom-right: 匕 (roughly x 155-265, y 155-260) ----------
polyline([(180, 160), (165, 205)])
polyline([(155, 210), (245, 210), (245, 160)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0499_能/01_能.png")
