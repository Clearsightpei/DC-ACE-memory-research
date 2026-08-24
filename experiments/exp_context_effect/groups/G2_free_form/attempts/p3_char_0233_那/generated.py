"""Render 那 (nà) at 300x300, PIL.

Structure (6-7 strokes total):
Left component (尹-like, occupies left ~55% of canvas):
  1. Top horizontal (short)
  2. Second horizontal (through vertical)
  3. Bottom horizontal (base, slightly longer)
  4. Vertical / long 撇 sweeping down-left from top
Right component 阝 (right ear, occupies right ~35%):
  5. 横撇弯钩 (ear-loop starting top, curving)
  6. Vertical, long, extending well below baseline
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def stroke(pts, w=7):
    d.line(pts, fill=BLACK, width=w, joint="curve")
    # dab endpoints for calligraphic feel
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill=BLACK)


# ---------- LEFT COMPONENT (尹-like) ----------
# Top horizontal
stroke([(55, 90), (155, 82)], w=7)
# Second horizontal
stroke([(45, 140), (170, 138)], w=7)
# Bottom horizontal (base)
stroke([(50, 195), (155, 195)], w=7)
# Long 撇 — from upper right of left comp sweeping down-left
# passes through the horizontals like a vertical then curves out
pts_pie = [(140, 60), (135, 110), (125, 160), (110, 210), (85, 250), (55, 275)]
stroke(pts_pie, w=8)

# ---------- RIGHT COMPONENT 阝 (right ear) ----------
# 横撇弯钩 — starts top-right, sharp turn down, arcs into a small closed loop
# Larger ear-loop, more pronounced.
ear = [
    (200, 78),
    (250, 88),
    (255, 130),
    (240, 160),
    (215, 172),
    (198, 170),
]
stroke(ear, w=8)
# terminal flick UP-and-LEFT into character body (hook rule from memory)
d.line([(198, 170), (215, 155)], fill=BLACK, width=7)

# Vertical of 阝 — from top of ear, straight down, extending well below baseline
vpts = [(210, 82), (214, 150), (218, 220), (222, 278)]
stroke(vpts, w=9)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0233_那/01_那.png"
)
print("saved")
