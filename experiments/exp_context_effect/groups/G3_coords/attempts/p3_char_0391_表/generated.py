# BANK_DEVIATION
# skipped: (no 衣/表 primitive in bank)
# reason: 表 is a Phase-3 char with no direct bank entry; top (龶-like: 3 hengs + shu) and bottom (衣 variant with 撇+竖提+撇+捺) both need fresh render — bank has 一, 长, 太 pieces but no clean 衣.
# fresh_component: biao_char (freshly inlined 龶-top + 衣-bottom)
"""表 (biǎo) — fresh PIL render.

Structure (8 strokes, from GT):
  Top 龶 block:
    1. short heng (upper)
    2. mid heng (a bit longer)
    3. bottom-of-top heng (widest)
    4. vertical shu passing through all three hengs
  Bottom 衣 variant:
    5. long left pie starting near top-right of horizontals sweeping down-left
    6. short right pie (small tick)
    7. dian / hook under center
    8. long na sweeping down-right
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")
    # round endcaps
    r = width // 2
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def bezier(p0, p1, p2, n=40):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out

# ---- TOP 龶 block ----
# heng 1 (short top)
stroke([(115, 70), (175, 68)], width=6)
# heng 2 (mid)
stroke([(95, 108), (200, 105)], width=6)
# heng 3 (widest, bottom of top block)
stroke([(70, 148), (225, 145)], width=7)
# vertical shu passing through top
stroke([(145, 55), (147, 150)], width=6)

# ---- BOTTOM 衣 variant ----
# long pie: starts near top-right of bottom block, sweeps down-left
stroke(bezier((155, 148), (110, 210), (55, 275)), width=6)

# short pie tick (right side, just below the wide heng)
stroke([(195, 158), (180, 180)], width=5)

# central dian/small hook (under center of bottom-heng)
stroke(bezier((140, 175), (135, 210), (155, 260)), width=6)
# little hook tail on the central stroke
stroke([(155, 258), (170, 250)], width=5)

# long na: sweeps from mid-right down to lower-right
stroke(bezier((170, 190), (200, 235), (260, 275)), width=7)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_表.png")
img.save(out_path)
print("saved", out_path)
