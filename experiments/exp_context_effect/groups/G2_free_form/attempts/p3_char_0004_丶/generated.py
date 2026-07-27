"""
p3_char_0004_丶 — the standalone 丶 (dian/dot) character.

GT observation: a single teardrop-form stroke, thin at the upper-left
start, thickening toward the lower-right end, with a slight curve
(concave-down bow). Positioned near center of the 300x300 canvas,
roughly (130,120) → (185,200), length ~90px.

Approach: draw with PIL by stepping along a quadratic Bezier and
stamping filled circles whose radius grows linearly from thin at t=0
to thick at t=1 — the classic brush-dab technique for teardrop strokes.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Quadratic Bezier control points for a slight down-right curve.
# Start upper-left (thin), control biased right of the midpoint to give
# the concave-down bow visible in the GT, end lower-right (thick).
P0 = (135, 118)   # thin start
P1 = (150, 155)   # control — pulls the curve toward the right/down
P2 = (188, 202)   # thick terminal

def bez(t, p0, p1, p2):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y

# Brush radius grows from ~1.5 (hairline) to ~7 (broad terminal dab).
R_START = 1.5
R_END = 7.0

N = 240
for i in range(N + 1):
    t = i / N
    x, y = bez(t, P0, P1, P2)
    r = R_START + (R_END - R_START) * t
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Small extra terminal press for a clean rounded foot.
tx, ty = P2
draw.ellipse((tx - R_END, ty - R_END, tx + R_END, ty + R_END), fill="black")

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0004_丶/01_丶.png")
