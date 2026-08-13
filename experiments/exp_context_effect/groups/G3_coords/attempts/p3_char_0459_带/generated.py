# BANK_DEVIATION
# skipped: (no 巾/帅/带-family bank entry exists)
# reason: 带 top-with-three-uprights and bottom 巾 have no matching bank primitive; inlining fresh.
# fresh_component: dai_top_three_uprights, jin_frame_bottom
"""
带 (dai) — belt/carry.
Structure decomposition (top-to-bottom):
  Top zone: three short vertical strokes crossed by a long heng, with
            a small left "ear" (short pie/dian) and a small right hook.
  Middle: 冖 cover (dian + heng-gou).
  Bottom: 巾 frame (left shu, top-right heng-shu-gou, center shu extending
          below the frame).
Rendered fresh with PIL lines; ~10 strokes total.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5    # main stroke width
LW_S = 4  # small stroke width

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

def polyline(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)

# ---- TOP: three short uprights crossing a long heng ----
# Long horizontal (heng) across the top
line((35, 85), (265, 85), w=LW)

# Three short verticals crossing THROUGH the heng (extend above and slightly below)
line((95, 40),  (95, 108),  w=LW_S)   # left upright
line((150, 32), (150, 112), w=LW)     # center upright (slightly taller)
line((205, 40), (205, 108), w=LW_S)   # right upright

# Small left "ear" — short pie descending from left end of heng
polyline([(40, 88), (28, 112)], w=LW_S)

# Small right "ear" — small heng-zhe/hook curling down at right end
polyline([(260, 85), (272, 95), (258, 118)], w=LW_S)

# ---- MIDDLE: 冖 (mi cover) ----
# Left dian (short down-stroke)
polyline([(72, 118), (80, 138)], w=LW_S)

# heng-gou: long horizontal + right-side hook downward
polyline([(78, 140), (232, 140), (223, 158)], w=LW)

# ---- BOTTOM: 巾 frame ----
# Left shu — vertical on the left side, from just under the cover
line((92, 145), (92, 240), w=LW)

# Right shu-gou — right side of frame, ends with a short hook to the left
polyline([(215, 158), (215, 240), (198, 233)], w=LW)

# Bottom of the 冂 frame? No — 巾 has no bottom horizontal.
# Center shu — the defining vertical of 巾/带, extends well below the frame
line((150, 140), (150, 278), w=LW)

# Save
import os
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_带.png"))
print("wrote 01_带.png")
