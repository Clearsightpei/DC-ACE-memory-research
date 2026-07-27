"""
发 (fā) — 5 strokes, character.

Structure from GT observation:
  1. Short 撇 near top-left (small flick going down-left).
  2. Long 撇 starting mid-top area, curving down to bottom-left.
  3. 横折折/curve stroke: goes right from mid-left, drops, angles down-left
     (the "eyebrow" over the long strokes; in 发 this is the top-right hook
     shape that crosses the long 撇).
  4. Dot 点 upper-right (a short slash).
  5. Long 捺 sweeping from center down to bottom-right.

No siblings on the checklist. No hook in this glyph (per GT tracing).
Draw with PIL Bezier sampling and stroke-width tapering approximated by
overdrawing.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)


def bezier(p0, p1, p2, p3, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    # end-caps
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill="black")


# Stroke 1: short 撇 top-left — small down-left flick
s1 = bezier((100, 80), (92, 95), (82, 108), (72, 120), steps=40)
stroke(s1, width=5)

# Stroke 2: long 撇 — starts near top-middle, curves down to bottom-left
s2 = bezier((150, 70), (125, 140), (95, 200), (55, 265), steps=60)
stroke(s2, width=6)

# Stroke 3: 横折折 — starts from upper-left area, arcs across the top-right,
# then bends down-and-left crossing through the long 撇 in the middle
s3a = bezier((85, 130), (140, 115), (195, 120), (225, 140), steps=50)
stroke(s3a, width=6)
s3b = bezier((225, 140), (205, 160), (180, 180), (150, 200), steps=40)
stroke(s3b, width=6)

# Stroke 4: dot 点 upper right — short slash
s4 = bezier((215, 85), (222, 95), (230, 108), (238, 122), steps=25)
stroke(s4, width=6)

# Stroke 5: long 捺 — starts near center where stroke 3 ends and long 撇 crosses,
# sweeps down-right to bottom-right corner
s5 = bezier((145, 175), (180, 210), (215, 240), (260, 268), steps=60)
stroke(s5, width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0170_发/01_发.png")
print("saved")
