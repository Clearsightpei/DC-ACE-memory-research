"""
Render 子 (p3_char_0049_子) at 300x300 with PIL.

Structure (3 strokes):
1. 横撇 (top): short horizontal to the right, then a shoulder turn
   diagonally down-left to form the head hook of 子.
2. 弯钩 (middle): vertical spine starting near the shoulder of stroke 1,
   descending straight then curving slightly and ending with an
   up-left hook flick at the bottom.
3. 横 (bottom of visual middle): a long horizontal cross-bar that
   crosses the vertical spine around the middle of the character.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=8):
    """Draw a smooth stroke through points with round joints/ends."""
    d.line(points, fill=BLACK, width=width, joint="curve")
    # round caps
    for (x, y) in (points[0], points[-1]):
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def dab(cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLACK)


# --- Stroke 1: 横撇 (top head) ---
# Short 横 from left to right along the top, then shoulder turns
# and 撇 goes down-left, extending past the spine.
horizontal_start = (90, 88)
shoulder = (215, 78)          # small upward tilt on the 横
pie_end = (125, 145)          # 撇 flicks down-left, past the spine
# 横 part
stroke([horizontal_start, shoulder], width=8)
# small shoulder dab (顿) at the corner
dab(shoulder[0], shoulder[1], 7)
# 撇 part (longer down-left flick)
stroke([shoulder, (185, 105), (155, 125), pie_end], width=8)

# --- Stroke 2: 弯钩 (vertical hook forming spine) ---
# Starts near the shoulder / top of the head area, descends mostly
# straight, curves slightly and hooks up-left at the bottom.
spine_top = (170, 105)
spine_points = [
    spine_top,
    (168, 145),
    (168, 185),
    (170, 220),
    (165, 245),   # begin curve
    (145, 258),   # bottom of curve
    (120, 253),   # hook flick up-left
    (105, 240),
]
stroke(spine_points, width=9)
# small 顿 at very top of spine
dab(spine_top[0], spine_top[1], 5)

# --- Stroke 3: 横 (cross bar) ---
# Long horizontal near the vertical middle, crossing the spine.
hbar_start = (55, 170)
hbar_end = (250, 168)
stroke([hbar_start, (150, 171), hbar_end], width=8)
# small terminal dabs
dab(hbar_start[0], hbar_start[1], 5)
dab(hbar_end[0], hbar_end[1], 6)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0049_子/01_子.png"
)
