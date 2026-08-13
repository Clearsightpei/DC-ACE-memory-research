"""Render 亞 (traditional form of 亚) at 300x300, white bg, black ink.

Structure per GT:
  - Top horizontal (narrower than base)
  - Left vertical descends from top-left, right vertical from top-right,
    both continuing down to the base line
  - Inside: two small "口"-like boxes (one left, one right) sitting on
    a middle cross-bar, with a short vertical column joining top and bottom
  - Bottom horizontal (widest, the base)
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(p1, p2, w=6):
    draw.line([p1, p2], fill=BLACK, width=w)
    r = w // 2
    for p in (p1, p2):
        draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=BLACK)

# ---- Overall frame anchors ----
TOP_Y = 55
BOT_Y = 250            # inner base (the frame's base line)
BASE_Y = 268           # the wide outer base horizontal
LEFT_X = 65
RIGHT_X = 240
MID_Y = 150            # middle cross-bar

# 1. TOP horizontal (~narrower than base)
line((85, TOP_Y), (225, TOP_Y+2), w=6)

# 2. LEFT vertical descending from top through to bottom of frame
line((LEFT_X, TOP_Y+3), (LEFT_X-8, BOT_Y), w=6)

# 3. RIGHT vertical descending from top through to bottom of frame
line((RIGHT_X, TOP_Y+3), (RIGHT_X+8, BOT_Y), w=6)

# 4. MIDDLE horizontal cross-bar (spans between the two verticals)
line((LEFT_X-4, MID_Y), (RIGHT_X+4, MID_Y), w=6)

# 5. Inner bottom horizontal (base of frame — sits above outer wide base)
line((LEFT_X-6, BOT_Y), (RIGHT_X+6, BOT_Y), w=6)

# ---- Inner motif: two little boxes on either side of a vertical column ----

# Central short vertical column (from top horizontal down to middle bar)
CX = 152
line((CX, TOP_Y+3), (CX, MID_Y), w=6)
# Central short vertical stem below middle bar to inner base
line((CX, MID_Y), (CX, BOT_Y), w=6)

# Left small box (口): sits between top and middle, hangs off center-left area
LB_L, LB_R = 95, 132
LB_T, LB_B = 92, 128
line((LB_L, LB_T), (LB_R, LB_T), w=5)     # top
line((LB_L, LB_T), (LB_L, LB_B), w=5)     # left
line((LB_L, LB_B), (LB_R, LB_B), w=5)     # bottom
line((LB_R, LB_T), (LB_R, LB_B), w=5)     # right

# Right small box (口)
RB_L, RB_R = 172, 210
RB_T, RB_B = 92, 128
line((RB_L, RB_T), (RB_R, RB_T), w=5)
line((RB_L, RB_T), (RB_L, RB_B), w=5)
line((RB_L, RB_B), (RB_R, RB_B), w=5)
line((RB_R, RB_T), (RB_R, RB_B), w=5)

# Lower-left small box
LB2_L, LB2_R = 95, 132
LB2_T, LB2_B = 172, 210
line((LB2_L, LB2_T), (LB2_R, LB2_T), w=5)
line((LB2_L, LB2_T), (LB2_L, LB2_B), w=5)
line((LB2_L, LB2_B), (LB2_R, LB2_B), w=5)
line((LB2_R, LB2_T), (LB2_R, LB2_B), w=5)

# Lower-right small box
RB2_L, RB2_R = 172, 210
RB2_T, RB2_B = 172, 210
line((RB2_L, RB2_T), (RB2_R, RB2_T), w=5)
line((RB2_L, RB2_T), (RB2_L, RB2_B), w=5)
line((RB2_L, RB2_B), (RB2_R, RB2_B), w=5)
line((RB2_R, RB2_T), (RB2_R, RB2_B), w=5)

# 6. OUTER BOTTOM base horizontal — widest stroke
line((35, BASE_Y), (270, BASE_Y+2), w=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0386_亞/01_亞.png")
print("saved 01_亞.png")
