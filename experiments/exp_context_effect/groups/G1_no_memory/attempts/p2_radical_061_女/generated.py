"""Render 女 (radical, 3 strokes) at 300x300 using PIL.

Stroke order (standard):
  1. 撇点 (piě-diǎn): starts upper-center, sweeps down-left as a piě,
                       then reverses into a short 点 slanting down-right.
                       The 点 tail sits below the horizontal on the right.
  2. 撇 (piě):         long diagonal from upper-right sweeping down-left,
                       crossing through stroke 1 and extending past the
                       horizontal to lower-left.
  3. 一 (héng):        long horizontal crossing near mid-height.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5


def line(p0, p1, width=LW):
    draw.line([p0, p1], fill=INK, width=width)
    r = width // 2
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def polyline(points, width=LW):
    for i in range(len(points) - 1):
        line(points[i], points[i + 1], width=width)


# ---------- Stroke 1: 撇点 (piě-diǎn) ----------
# Piě segment: from upper-center (155, 70) down-left to bend (108, 165).
# Then 点: bend down-right to end at (185, 215), tail below horizontal.
s1_a = (155, 70)
s1_b = (108, 165)
s1_c = (185, 215)
polyline([s1_a, s1_b, s1_c])

# ---------- Stroke 2: 撇 (long piě) ----------
# Long diagonal from upper-right (210, 105) sweeping down-LEFT through the
# center to lower-left corner (70, 250). This is the sweeping stroke that
# makes 女's characteristic slant.
s2_a = (210, 105)
s2_b = (70, 250)
line(s2_a, s2_b)

# ---------- Stroke 3: 一 (héng, horizontal) ----------
# Long horizontal crossing near mid-height.
s3_a = (45, 180)
s3_b = (270, 170)
line(s3_a, s3_b)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G1_no_memory/attempts/"
    "p2_radical_061_女/01_女.png"
)
