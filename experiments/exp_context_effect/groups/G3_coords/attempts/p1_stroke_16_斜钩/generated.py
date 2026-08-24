"""
p1_stroke_16_斜钩 (xié gōu) — diagonal hook stroke.

Shape: a long stroke starting from upper-left area, slanting down and
slightly curving to the lower-right, ending with a small upward-left
hook (钩) at its tail. Appears in 我, 找, 戈, 成, 划.

Coordinate format (G3 mandate): plain numeric offsets, no anchors,
no cells, no joints. Uses PIL to write a 300x300 PNG directly.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Main diagonal body: upper-left -> lower-right, gently curved.
# Slight belly outward (down-left of the chord) to give calligraphic curve.
# Numeric control points chosen to fit 300x300 canvas.
p0 = (70, 55)       # start (top-left, slight in from edge)
p1 = (140, 140)     # mid-upper control (gentle curve)
p2 = (200, 215)     # mid-lower control
p3 = (245, 250)     # tail before hook (lower-right)

# Draw the curved body as a series of short segments (quadratic-ish),
# with a slight taper: start thin, thicken toward middle, thin toward tail.
def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

def bezier(pts, t):
    # De Casteljau for 4-pt cubic
    a = lerp(pts[0], pts[1], t)
    b = lerp(pts[1], pts[2], t)
    c = lerp(pts[2], pts[3], t)
    d = lerp(a, b, t)
    e = lerp(b, c, t)
    return lerp(d, e, t)

body = [p0, p1, p2, p3]
N = 80
prev = bezier(body, 0.0)
for i in range(1, N + 1):
    t = i / N
    cur = bezier(body, t)
    # width profile: 4 -> 8 -> 5 (thicker in belly)
    if t < 0.5:
        w = 4 + (t / 0.5) * 4       # 4 -> 8
    else:
        w = 8 - ((t - 0.5) / 0.5) * 3  # 8 -> 5
    draw.line([prev, cur], fill="black", width=int(round(w)))
    prev = cur

# The hook (钩): a short upward-left flick from the tail.
# 钩 for 斜钩 goes up and slightly left, short (~25-35 px).
hook_start = p3
hook_end = (215, 220)   # up and left of tail
# Draw hook with slight taper (thicker at joint, thinner at tip)
Nh = 20
prev = hook_start
for i in range(1, Nh + 1):
    t = i / Nh
    cur = lerp(hook_start, hook_end, t)
    w = 6 - t * 4  # 6 -> 2
    draw.line([prev, cur], fill="black", width=int(round(w)))
    prev = cur

# Round out the tail joint so the hook looks continuous with the body.
draw.ellipse([p3[0] - 5, p3[1] - 5, p3[0] + 5, p3[1] + 5], fill="black")

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_16_斜钩/01_斜钩.png"
img.save(out)
print(f"wrote {out}")
