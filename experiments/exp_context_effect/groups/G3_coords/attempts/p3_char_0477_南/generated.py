# BANK_DEVIATION
# skipped: (no direct bank entry for 南 or its 冂+inner composition)
# reason: 南 is a unique composite (top 十 + wide 冂-envelope + inner 半-like);
#         no bank primitive matches the envelope shape or the inner cluster,
#         so inline fresh render aligned to GT is cleaner than forcing a scale.
# fresh_component: nan_char_inline (top-cross + wide-envelope + inner 半-cluster)

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, width=6):
    d.line([p0, p1], fill="black", width=width)

def curve_hook(points, width=6):
    # polyline with joined segments
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill="black", width=width)

W_MAIN = 7

# --- Top: short 一 + short 丨 (the "十" on top of the envelope) ---
# short top heng
line((118, 60), (182, 60), width=W_MAIN)
# short shu going down through the heng, ending near the top of the envelope
line((150, 45), (150, 105), width=W_MAIN)

# --- Wide top heng (envelope's roof - actually a wide heng above the frame) ---
# Wide horizontal spanning most of the width, positioned above the box
line((55, 108), (245, 108), width=W_MAIN)

# --- The 冂 envelope (left 竖 + top-right corner going down with hook) ---
# Left vertical: 竖 going down from the top-heng to bottom
# In 南, the left is a 竖 (straight down)
line((72, 118), (72, 268), width=W_MAIN)

# Right side: 横折钩 (horizontal-turn-vertical with hook at bottom-left)
# starts from top just under the wide heng, goes right a bit then turns down, then hooks left
curve_hook([(72, 118), (228, 118), (228, 262), (212, 262)], width=W_MAIN)
# Actually the wide heng already provides the top; the 横折钩 in 南 starts at top-right
# Let me redo: draw right-side vertical with hook
line((228, 118), (228, 268), width=W_MAIN)
# hook at bottom (small tick left)
line((228, 268), (212, 258), width=W_MAIN)

# --- Inside cluster: 丷 (two small dots/strokes) + 干-like (heng + vertical) ---
# Two small mirror dots near the top interior
# left dot (short pie-like)
curve_hook([(105, 140), (98, 158)], width=6)
# right dot (short na-like)
curve_hook([(195, 140), (202, 158)], width=6)

# Inner heng (medium width)
line((95, 185), (205, 185), width=W_MAIN)
# second inner heng
line((110, 220), (205, 220), width=W_MAIN)
# inner vertical (going from just below top dots down through both hengs)
line((150, 160), (150, 258), width=W_MAIN)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_南.png")
img.save(out_path)
print(f"saved: {out_path}")
