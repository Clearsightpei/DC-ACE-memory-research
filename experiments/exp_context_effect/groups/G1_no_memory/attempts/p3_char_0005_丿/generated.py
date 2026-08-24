"""Render 丿 (p3_char_0005) to 300x300 PNG matching GT layout.

GT shows two strokes:
  - A long left-falling stroke 丿 (piě) on the left half, curving from upper-mid
    down toward lower-left.
  - A short diagonal stroke on the upper-right, sloping down-left.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width=6):
    # draw a polyline with rounded joints
    draw.line(points, fill=INK, width=width, joint="curve")
    # end caps
    r = width // 2
    for (x, y) in (points[0], points[-1]):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# ---- Stroke 1: long piě 丿 on left ----
# Curves noticeably leftward, tapering downward. Starts near (150, 75),
# stays mostly vertical near the top, then bows outward to lower-left ending
# near (70, 275). Sampled to get a smooth concave-right arc.
piě = [
    (150, 78),
    (147, 100),
    (142, 125),
    (135, 150),
    (127, 175),
    (117, 200),
    (105, 222),
    (92, 245),
    (78, 268),
    (70, 280),
]
stroke(piě, width=7)

# ---- Stroke 2: short diagonal on upper-right ----
# From upper-right (215, 105) sloping down-left to (170, 135).
short = [
    (215, 105),
    (200, 115),
    (185, 125),
    (170, 138),
]
stroke(short, width=6)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0005_丿/01_丿.png"
img.save(out)
print("wrote", out)
