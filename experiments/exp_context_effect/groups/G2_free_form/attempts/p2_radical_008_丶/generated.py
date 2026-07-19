"""Render p2_radical_008_丶 as a 300x300 PNG.

Observation from GT: The radical 丶 here is a thin curved stroke,
NOT the plump teardrop of Phase-1 丶 mastery. It sits in the upper-
middle of the canvas, starts at upper-left, curves down-and-right,
ending lower and slightly right. Very thin (~3-4 px), gentle bow with
belly on the lower-left side. Very slight thin->thicker taper toward
the tail (calligraphic dot form).

Rendered with PIL brush-dabs along a quadratic Bezier.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400, easing=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        te = t ** easing
        r = r_start + (r_end - r_start) * te
        dab(x, y, r)


# 丶 radical: thin gently-curved diagonal, upper-left to lower-right.
# GT shows a subtle bow, not a strong hook. Belly slightly on the
# lower-left (concave toward upper-right).
P0 = (122, 115)   # upper-left start
P2 = (182, 195)   # lower-right end
# Control point only slightly off the chord midpoint (~148,155) toward
# lower-left, so the bow is gentle rather than hook-like.
P1 = (140, 172)

# Thin throughout, essentially uniform with a tiny widening near tail.
bezier_stroke(P0, P1, P2, r_start=2.8, r_end=3.6, steps=500, easing=1.2)

# Very subtle terminal press (no ball)
dab(P2[0], P2[1], 4.0)

img.save("01_丶.png")
print("saved 01_丶.png")
