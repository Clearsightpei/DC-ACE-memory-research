"""Draw 表 (biao - surface/outer) at 300x300, black ink on white.
Structure: 龶-like top (three horizontals + vertical) over 衣-like bottom (long horizontal + pie + na + inner strokes).
Uses PIL with slight brush-taper via multi-width stacked lines.
"""
from PIL import Image, ImageDraw
import math, os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, widths=None, base=8):
    """Draw stroke as polyline with variable width segments."""
    if widths is None:
        widths = [base]*len(points)
    for i in range(len(points)-1):
        x1,y1 = points[i]
        x2,y2 = points[i+1]
        w = int((widths[i]+widths[i+1])/2)
        d.line([(x1,y1),(x2,y2)], fill="black", width=w)
        # end cap
        d.ellipse([x2-w//2, y2-w//2, x2+w//2, y2+w//2], fill="black")
        d.ellipse([x1-w//2, y1-w//2, x1+w//2, y1+w//2], fill="black")

# --- TOP: 龶 shape (three horizontals + central vertical hooking) ---
# horizontal 1 (top short)
stroke([(115,55),(175,58)], [7,9])
# vertical descending down through middle
stroke([(150,50),(150,120)], [8,9])
# horizontal 2 (middle, wider)
stroke([(100,90),(200,92)], [8,10])
# horizontal 3 (longer, sits above the big横)
stroke([(95,120),(215,122)], [8,10])
# Big long horizontal (spans wide - marks middle)
stroke([(60,155),(240,158)], [10,12])

# --- BOTTOM: 衣-bottom (𧘇 shape) ---
# left 撇 (long pie sweeping down-left from just under the big horizontal)
stroke([(145,158),(120,200),(80,258)], [10,9,7])
# right 捺 (na) - swoops down-right from top-middle
stroke([(155,158),(195,205),(248,260)], [9,11,13])
# small internal 撇 in the middle (little pie)
stroke([(175,195),(158,225)], [8,7])
# small hook/竖 inside right (like a mini 乚)
stroke([(190,215),(185,245),(200,255)], [7,7,6])

out_dir = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0391_表"
os.makedirs(out_dir, exist_ok=True)
img.save(os.path.join(out_dir, "01_表.png"))
print("saved")
