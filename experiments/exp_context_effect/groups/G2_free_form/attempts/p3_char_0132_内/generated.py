"""
p3_char_0132_内 — 4 strokes.

Revision 1: fix interior 人 (make strokes clearly meet at apex),
make right wall extend below with a proper hook.

Strokes:
  1. 竖 — left wall, from (80, 62) descending to (72, 250).
  2. 横折钩 — top 横, corner, right wall descending to bottom, hook up-left.
  3. 撇 — interior: from apex (~145, 105) sweeps down-left to (~78, 215).
  4. 捺-becomes-hook — starts at same apex (~145, 105), sweeps down-right
     to (~178, 200), then flicks slightly up (small hook).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

def dab(x, y, r=4):
    d.ellipse([x-r, y-r, x+r, y+r], fill="black")

# --- Stroke 1: 竖 (left wall) ---
dab(80, 62, r=5)
line([(80, 62), (74, 250)], width=7)
# slight terminal press
dab(74, 250, r=4)

# --- Stroke 2: 横折钩 ---
# top 横 slight up-tilt
line([(80, 62), (228, 58)], width=7)
# shoulder
dab(230, 62, r=6)
# right wall
line([(230, 62), (222, 258)], width=7)
# hook up-left
line([(222, 258), (204, 246)], width=6)

# --- Interior 人 apex point ---
APEX = (145, 105)
dab(APEX[0], APEX[1], r=4)

# --- Stroke 3: 撇 (down-left) ---
撇_pts = [APEX, (130, 130), (112, 158), (94, 190), (78, 218)]
line(撇_pts, width=6)

# --- Stroke 4: right leg (short 捺-with-hook) ---
# From apex, sweeps down-right, thickens toward end, tiny up-left flick
leg_pts = [APEX, (155, 135), (168, 165), (178, 195)]
line(leg_pts, width=6)
# thicker terminal
d.ellipse([173, 190, 185, 202], fill="black")
# tiny hook flick up-left
line([(180, 200), (172, 194)], width=4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0132_内/01_内.png")
print("wrote 01_内.png")
