"""
受 (shòu) — 8 strokes. Structure: 爫 (claw top) + 冖 (cover) + 又 (bottom).

Layout on 300x300 canvas:
- Top band ~y=50-95   : 爫  (3 small ticks/dots forming a claw)
- Middle band ~y=110-135: 冖  (short horizontal with a right-side hook)
- Bottom half ~y=140-260: 又  (横撇 + 捺 crossing to form an X)

Hook rule: 冖's right-terminal hook flicks DOWN-and-LEFT (short flick
back into character body). 又's 捺 broadens to a flat foot at lower right.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_quad_dabs(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# -----------------------------------------------------------------------------
# TOP GROUP — 爫 (claw): 3 small strokes
# -----------------------------------------------------------------------------
# 1. small left 撇 tick (top-left of claw)
bezier_quad_dabs((105, 55), (98, 70), (92, 90), 3.0, 2.0, steps=150)

# 2. central short 撇/点 (a small tick angled down-left)
bezier_quad_dabs((150, 50), (144, 68), (138, 90), 3.0, 2.0, steps=150)

# 3. right 点 / short slanted stroke (top-right of claw)
bezier_quad_dabs((195, 55), (200, 72), (205, 92), 3.0, 2.5, steps=150)

# tiny connecting horizontal implied at top (small mark linking claw tops)
line_dabs(108, 62, 195, 60, 2.0, 2.0, steps=120)

# -----------------------------------------------------------------------------
# MIDDLE BAND — 冖 (cover): horizontal ending in a downward hook on the right,
# with a small left-side dot
# -----------------------------------------------------------------------------
# 4a. small left dot of the cover
dab(70, 120, 4.0)

# 4b. main horizontal of 冖 sweeping right, slight upward tilt
line_dabs(78, 122, 232, 116, 4.0, 4.5, steps=250)

# 4c. shoulder + hook flick (down-and-left back into body)
dab(232, 116, 5.5)
bezier_quad_dabs((232, 118), (238, 130), (228, 148), 5.0, 2.5, steps=150)

# -----------------------------------------------------------------------------
# BOTTOM GROUP — 又 (right hand): 横撇 + 捺
# -----------------------------------------------------------------------------
# Stroke: 横撇  (short slanted 横 + shoulder + long 撇 tail)
# 5a. short 横 across upper mid, slight upward tilt
line_dabs(85, 165, 205, 158, 4.5, 4.5, steps=200)

# 5b. shoulder 顿笔
dab(205, 158, 6.0)

# 5c. 撇 tail — long bowed sweep down-left, ends near lower-left
bezier_quad_dabs((205, 158), (145, 220), (65, 275), 5.0, 1.5, steps=400)

# Stroke: 捺  (thin -> thick, broad foot at lower right)
# Starts near the shoulder area, sweeps down-right with gentle curve.
bezier_quad_dabs((120, 175), (185, 225), (260, 270), 2.0, 7.0, steps=400)

# Broad terminal foot (捺 flat press)
for k in range(14):
    dab(260 + k * 0.6, 270 + k * 0.05, 7.0 - k * 0.4)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0411_受/01_受.png"
)
