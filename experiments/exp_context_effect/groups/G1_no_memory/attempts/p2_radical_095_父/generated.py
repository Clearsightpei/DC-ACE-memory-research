"""Render 父 (radical, 4 strokes) at 300x300, white bg, black ink.

Revision 1: matched more closely to GT.
  - Upper two "eyebrow" strokes: shorter, wider apart, angled inward,
    clearly detached from the lower X.
  - Lower X: long 撇 (upper-right to lower-left) crosses a long 捺
    (upper-left to lower-right). Crossing sits at roughly the vertical
    middle of the character.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def tapered_stroke(points, w_start=4, w_end=10, steps=60):
    seglens = []
    total = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        d = math.hypot(x1 - x0, y1 - y0)
        seglens.append(d)
        total += d

    def sample(t):
        target = t * total
        acc = 0.0
        for i, d in enumerate(seglens):
            if acc + d >= target or i == len(seglens) - 1:
                u = 0 if d == 0 else (target - acc) / d
                x0, y0 = points[i]
                x1, y1 = points[i + 1]
                return (x0 + u * (x1 - x0), y0 + u * (y1 - y0))
            acc += d
        return points[-1]

    prev = sample(0.0)
    for i in range(1, steps + 1):
        t = i / steps
        cur = sample(t)
        w = w_start + (w_end - w_start) * ((i - 0.5) / steps)
        w = max(2, int(round(w)))
        draw.line([prev, cur], fill="black", width=w)
        r = w // 2
        draw.ellipse((cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r), fill="black")
        prev = cur


# ----- Stroke 1: upper-left short 撇 -----
# A short, gently curving stroke going from upper area sweeping down-left.
# Placed in the LEFT-UPPER quadrant. Detached from lower X.
tapered_stroke(
    [(120, 85), (110, 100), (98, 115), (88, 128)],
    w_start=7, w_end=3, steps=30,
)

# ----- Stroke 2: upper-right short stroke (short curved dot) -----
# Short curving stroke, RIGHT-UPPER quadrant. Slight curve down-left.
tapered_stroke(
    [(200, 85), (195, 100), (188, 115), (180, 128)],
    w_start=4, w_end=7, steps=30,
)

# ----- Stroke 3: long 撇 (upper-right -> lower-left) -----
# The rightward "hook-of-撇": begins near top-right of lower assembly,
# arcs down-left through the middle, tapers to fine tail bottom-left.
tapered_stroke(
    [(210, 130), (185, 160), (150, 190), (110, 220), (75, 245)],
    w_start=9, w_end=3, steps=70,
)

# ----- Stroke 4: long 捺 (upper-left -> lower-right) -----
# Begins fine at upper-left, thickens through the middle,
# broad flat foot at lower-right.
tapered_stroke(
    [(105, 135), (135, 165), (170, 195), (205, 220), (235, 235)],
    w_start=3, w_end=11, steps=70,
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_095_父/01_父.png"
)
print("wrote 01_父.png")
