# 亦 (yi, "also") — 6 strokes
# Structure: 点 (top), 一 (horizontal), then 4-part lower group:
#   撇 (left arm), 竖 (short center), 竖钩/short-shu (mid-right), 点 (right dot)
# GT shows thin uniform lines (MMH style). Trust GT — draw thin, no calligraphic taper.

from PIL import Image, ImageDraw
import os, math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 4  # thin line width per GT

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def curve(pts, w=LW):
    # simple polyline through points
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# 1) top 点 — short slash top-center, going down-right
line((150, 60), (162, 78))

# 2) 一 (horizontal) — long, slightly wavy, spans wide
# GT shows a gently arced horizontal
curve([(55, 118), (105, 112), (170, 110), (230, 115), (250, 120)])

# 3) 撇 (left arm) — starts near left-center of the horizontal, sweeps down-left with curve
curve([(105, 130), (95, 165), (80, 205), (65, 245)])

# 4) 短竖 (tiny center vertical nub) — just below horizontal, short
line((140, 130), (139, 165))

# 5) 竖钩 (mid-right vertical with hook curving left at bottom)
curve([(180, 135), (178, 175), (172, 215), (160, 245), (145, 255)])

# 6) 点 (right dot) — long diagonal sweeping down-right
curve([(215, 145), (230, 180), (245, 215), (255, 245)])

out_path = os.path.join(os.path.dirname(__file__), "01_亦.png")
img.save(out_path)
print(f"saved {out_path}")
