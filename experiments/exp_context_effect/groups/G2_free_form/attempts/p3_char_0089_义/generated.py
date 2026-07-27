"""
义 — 3 strokes: 点 (top-left), 撇 (down-left), 捺 (down-right).
The 撇 and 捺 form a wide X that crosses near the vertical middle.
Reference form_catalog "乂 as body-cross" (line 281): 撇+捺 crossing
near vertical middle; captures the 义 signature.
Small 点 sits above and slightly LEFT of the crossing point.

Layout (300x300):
  - 点: short slanted dash, upper-center-left, ~ (110,90)→(140,105)
  - 撇: from ~(155,110) sweeping down-left to ~(60,265), gentle bow
  - 捺: from ~(160,110) sweeping down-right to ~(255,265), thin→thick with foot
  - The two cross near (130, 210) — below middle, in the lower half
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLACK)


def stroke(points, widths):
    """Draw a variable-width stroke as a series of connected dabs."""
    n = len(points)
    # dense interpolation
    samples = []
    seg_count = 60
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        for s in range(seg_count):
            t = s / seg_count
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            samples.append((x, y, w))
    samples.append((points[-1][0], points[-1][1], widths[-1]))
    for x, y, w in samples:
        dab(x, y, w / 2)


# --- Stroke 1: 点 (top-left dot as short slanted dash) ---
# short thin→thick down-right flick, sits above and left of the X
stroke(
    [(105, 82), (122, 95), (140, 108)],
    [3.5, 5.5, 6.5],
)

# The 撇 and 捺 MUST CROSS to form the 义 X. Crossing point ~(155, 210).
# So: 撇 starts on the RIGHT side of the top (~x=195) and ends on LEFT (~x=55).
#     捺 starts on the LEFT side of the top (~x=115) and ends on RIGHT (~x=265).

# --- Stroke 2: 撇 (right-top down to lower-left, gentle bow, thick→thin) ---
stroke(
    [(195, 118), (175, 155), (150, 200), (110, 245), (70, 272)],
    [8.5, 8.0, 7.0, 5.0, 2.5],
)

# --- Stroke 3: 捺 (left-top down to lower-right, thin→thick, terminal foot) ---
# Passes THROUGH the 撇 around (155, 210)
stroke(
    [(115, 122), (140, 160), (170, 200), (215, 245), (255, 268)],
    [3.5, 5.0, 7.0, 9.0, 6.0],
)
# terminal foot — small horizontal press extending right
stroke(
    [(250, 268), (275, 270)],
    [6.5, 3.0],
)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0089_义/01_义.png"
)
print("saved")
