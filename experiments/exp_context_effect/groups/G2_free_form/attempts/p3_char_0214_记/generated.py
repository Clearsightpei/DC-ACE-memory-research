"""
p3_char_0214_记 — 讠 (left) + 己 (right)

# SIGNATURE CHECK (from sibling_signature_checklist.md):
# 己: middle 横 FLOATS from BOTH walls -> shortened and clearly interior.
# Hook rule (TIER-0 B): 己's 竖弯钩 terminal flick goes UP-and-LEFT.

Revision 2: shorter floating middle 一, cleaner 讠 dot, unified 己 top.
"""
from PIL import Image, ImageDraw

W = H = 300
im = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(im)
INK = (0, 0, 0)
BW = 8

def line(pts, w=BW):
    d.line(pts, fill=INK, width=w, joint="curve")

# ------- LEFT: 讠 -------
# 点 (slanted dot, upper-left to lower-right)
line([(50, 70), (78, 92)], w=9)

# 横折提: horizontal -> down -> flick up-right
line([
    (38, 130),
    (95, 128),
    (78, 195),
    (108, 210),
])

# ------- RIGHT: 己 -------
# left wall x=135, right wall x=250
# Stroke 1: 横折 (top horizontal + turn down to middle)
line([
    (135, 88),
    (250, 85),
    (245, 155),
])

# Stroke 2: 一 middle horizontal — FLOATS clearly from both walls
line([
    (160, 158),
    (222, 158),
])

# Stroke 3: 竖 + 横 + 竖弯钩 all-in-one (left vertical, bottom horizontal, up-left hook)
line([
    (135, 88),   # top-left (continues visually from stroke 1 start)
    (133, 170),
    (135, 230),  # left vertical down
    (170, 250),  # curve into bottom
    (240, 250),  # bottom horizontal sweep
    (258, 235),  # turn up
    (248, 215),  # hook flick UP-and-LEFT
])

im.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0214_记/01_记.png")
print("saved 01_记.png")
