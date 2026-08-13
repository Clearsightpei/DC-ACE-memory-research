"""
定 (dìng) — 8 strokes: 宀 (roof: 点, 点, 横钩) + 疋 (top横, 竖, 横, 撇, 捺)
G2 approach: PIL with brush-dab stroke primitives per drawer_memory.md.
Hook flick: 横钩 terminal flicks DOWN-LEFT (into body), per TIER-0.B.
"""
from PIL import Image, ImageDraw
import math

W = 300
img = Image.new("RGB", (W, W), "white")
d = ImageDraw.Draw(img)

def dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def stroke(pts, width=6, taper_end=None):
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        d.line((x0, y0, x1, y1), fill="black", width=width)
    for x, y in pts:
        dab(x, y, width // 2)
    if taper_end:
        x, y = pts[-1]
        dab(x, y, taper_end)

# --- 宀 roof ---
# 1. Top dot (点)
stroke([(150, 40), (156, 55)], width=7, taper_end=5)

# 2. Left dot (点) of 宀
stroke([(85, 65), (78, 85)], width=7, taper_end=5)

# 3. 横钩 — horizontal that turns down into a small hook at right
# Horizontal segment then a short down-left flick
horiz = [(80, 85), (220, 82)]
stroke(horiz, width=7)
# hook: from (220,82) go down-left short
stroke([(220, 82), (215, 105)], width=7, taper_end=4)

# --- 疋 body ---
# 4. Top horizontal of 疋 (short)
stroke([(125, 145), (190, 143)], width=7, taper_end=4)

# 5. Short vertical (竖) from left end of top horizontal down
stroke([(128, 143), (128, 180)], width=7, taper_end=4)

# 6. Longer horizontal below (the 一)
stroke([(100, 195), (210, 192)], width=7, taper_end=4)

# 7. 撇 — left-falling from top of 疋 body down to lower-left
stroke([(150, 200), (130, 230), (95, 265)], width=7, taper_end=3)

# 8. 捺 — right-falling; wide sweep then a long horizontal flick to the right (定's tail)
capts = [(160, 205), (185, 235), (210, 258)]
for i in range(len(capts) - 1):
    x0, y0 = capts[i]
    x1, y1 = capts[i + 1]
    w = 8 if i == 0 else 10
    d.line((x0, y0, x1, y1), fill="black", width=w)
# terminal long horizontal flick to right (characteristic of 定)
d.line((210, 258, 265, 260), fill="black", width=7)
dab(265, 260, 3)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0381_定/01_定.png")
print("saved")
