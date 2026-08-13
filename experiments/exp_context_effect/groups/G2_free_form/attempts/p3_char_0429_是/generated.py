"""是 (shi) — 9 strokes.
Composition: 日 on top + 疋-like bottom (横, 竖, 横, 撇, 捺).

Stroke plan:
 1. 竖 left side of 日
 2. 横折 top+right of 日
 3. 横 middle of 日
 4. 横 bottom of 日 (close the box)
 5. 横 (wide, below 日)
 6. 竖 short vertical from row 5 down
 7. 短横 mid horizontal on the vertical
 8. 撇 down-left long from stroke-7 area
 9. 捺 down-right long from stroke-7 area

# SIGNATURE CHECK: none of the sibling-risk labels apply for 是 as a
# whole; 日 as a component is not in the sibling checklist.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
WT = 6  # base stroke width

def line(p1, p2, w=WT):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(points, w=WT):
    d.line(points, fill=BLACK, width=w, joint="curve")

# ---- 日 (top) — roughly x in [110, 190], y in [45, 120] ----
# 1. 竖 (left of 日)
line((113, 48), (113, 122), w=WT)
# 2. 横折 (top + right)
poly([(113, 48), (188, 48), (188, 122)], w=WT)
# 3. 横 (middle)
line((114, 86), (187, 86), w=WT-1)
# 4. 横 (bottom close)
line((113, 122), (188, 122), w=WT)

# ---- 疋-like bottom ----
# 5. 横 wide horizontal (below 日, slight upward tilt to right)
line((60, 152), (240, 148), w=WT)

# 6. 竖 short vertical dropping from row 5 (slightly left of center to
#    match GT — the small 口-top of 龰 sits left-of-middle)
line((135, 152), (135, 200), w=WT)

# 7. 短横 mid-horizontal (small crossbar, narrow — forms 龰-top box)
line((135, 200), (185, 200), w=WT)

# 8. 撇 — long sweeping diagonal, starts high on the vertical and
#    sweeps down-left far past the bottom-left of the frame
poly([(135, 175), (120, 210), (100, 245), (70, 278)], w=WT)

# 9. 捺 — long diagonal sweeping down-right with a thickening tail
poly([(155, 205), (180, 230), (210, 255), (245, 275)], w=WT+2)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0429_是/01_是.png")
print("saved")
