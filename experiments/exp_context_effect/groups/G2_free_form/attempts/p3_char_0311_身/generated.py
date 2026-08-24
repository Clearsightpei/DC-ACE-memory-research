"""身 (shēn, body) — 7 strokes.

Structure (from GT):
1. Short 撇 at top-left (small tick above top of box)
2. 横折钩 — top horizontal + right vertical (forms the top-right of the box)
3. 横 — upper inner horizontal
4. 横 — lower inner horizontal
5. 横 — bottom closing horizontal (short, connects left post to bottom of right vert)
6. 竖 / 撇 short left post (the left side of the box)
7. Long 撇 — full body-crossing diagonal from mid-top down to lower-left,
   sweeping past the bottom of the box (this is the characteristic 身 stroke).

Notes from form_catalog: "撇 as body-crossing diagonal" — must overlap
and pass through the body, not stop early.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 6

def line(p1, p2, w=INK):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(points, w=INK):
    d.line(points, fill=BLACK, width=w, joint="curve")

# Box coordinates for the upper trunk of 身
# The character sits slightly high; long 撇 extends past bottom.
box_left  = 95
box_right = 195
box_top   = 75
box_mid1  = 120   # upper inner 横
box_mid2  = 160   # lower inner 横
box_bot   = 195   # bottom 横 (short, closes the trunk)

# 1) Short 撇 at top (small tick sitting on the top-left corner of the box,
#    slanting down-left and touching the box top)
poly([(130, 52), (118, 66), (108, 76)], w=5)

# 2) 横折钩 — top 横 across, then down the right side, ending with an up-left hook
#    Top 横 from (~box_left+8) to (box_right)
line((box_left + 5, box_top), (box_right, box_top), w=INK)
# Right 竖 down
line((box_right, box_top), (box_right + 2, box_bot + 5), w=INK)
# Small hook flick UP-and-LEFT at bottom of the right vertical
poly([(box_right + 2, box_bot + 5), (box_right - 8, box_bot - 2)], w=5)

# 3) Upper inner 横 (spans the box width, slightly shorter)
line((box_left + 8, box_mid1), (box_right - 4, box_mid1), w=5)

# 4) Lower inner 横
line((box_left + 8, box_mid2), (box_right - 4, box_mid2), w=5)

# 5) Bottom 横 that closes the trunk (short, near where left post ends)
line((box_left + 5, box_bot), (box_right - 4, box_bot), w=5)

# 6) Left post 竖 (from just under top 横 down to bottom 横)
line((box_left + 5, box_top + 2), (box_left + 8, box_bot), w=INK)

# 7) Long 撇 — the characteristic body-crossing diagonal.
#    Starts near top-center (above/inside the top 横), curves down-and-left,
#    sweeping past the bottom-left of the box.
poly([
    (185, 65),
    (175, 100),
    (155, 145),
    (125, 195),
    (90,  240),
    (55,  280),
], w=INK)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0311_身/01_身.png")
print("wrote 01_身.png")
