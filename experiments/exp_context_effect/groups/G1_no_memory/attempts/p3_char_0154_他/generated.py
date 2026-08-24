"""Render 他 (tā) at 300x300, white bg, black ink.
Structure: 亻 (person radical, left) + 也 (right, 3 strokes).
也 strokes: (1) 横折钩 top-outer, (2) 竖 inner-left, (3) 竖弯钩 sweeping bottom-right.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 4

def line(pts, w=TH):
    d.line(pts, fill=INK, width=w, joint="curve")

# ---------- 亻 (left radical) ----------
# Stroke 1: 撇 (diagonal from upper-right down to lower-left)
line([(100, 80), (60, 210)], w=TH)
# Stroke 2: 竖 (vertical, from mid of 撇 down)
line([(85, 130), (85, 250)], w=TH)

# ---------- 也 (right) ----------
# Stroke 1: 横折钩 — starts as horizontal at top, turns down, small hook at bottom-left
# Top horizontal
line([(140, 115), (240, 110)], w=TH)
# Vertical down from right end
line([(240, 110), (240, 215)], w=TH)
# Small hook (钩) pointing left at bottom
line([(240, 215), (222, 205)], w=TH)

# Stroke 2: 竖 — inner-left vertical, starts higher than the top horizontal, crosses through
line([(160, 90), (160, 205)], w=TH)

# Stroke 3: 竖弯钩 — starts near top center-inside, goes down, sweeps right along bottom, then rises (钩)
pts = []
# vertical descent
for y in range(130, 235, 3):
    pts.append((195, y))
# curve sweeping right along bottom
cx, cy = 195, 235
r = 40
# arc from ~180deg (left of center) down to ~350deg (right, slightly above baseline)
for a in range(90, 5, -4):
    rad = math.radians(a)
    x = cx + r * math.cos(math.radians(180 - a) + math.pi) * 0  # placeholder
# Simpler: parametric arc from (195,235) sweeping right and up
# Use quadratic-like curve via sampling
arc_pts = []
# start of curve
x0, y0 = 195, 235
# end of curve (right side, above baseline)
x1, y1 = 265, 205
# midpoint control (down-right corner)
cxm, cym = 235, 260
for t_i in range(0, 21):
    t = t_i / 20.0
    # quadratic bezier
    x = (1-t)**2 * x0 + 2*(1-t)*t * cxm + t**2 * x1
    y = (1-t)**2 * y0 + 2*(1-t)*t * cym + t**2 * y1
    arc_pts.append((x, y))
pts.extend(arc_pts)
# 钩 rising upward at end
pts.append((x1, y1 - 20))
line(pts, w=TH)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0154_他/01_他.png"
img.save(out_path)
print(f"saved {out_path}")
