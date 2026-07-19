"""
夊 (sui) - 3-stroke radical.
Canonical strokes: 撇 + 横撇 + 捺 (or equivalently a top small curl,
a middle 撇, and a long sweeping 捺).

Rendering interpretation from GT:
  1. Top curl (小 横撇) -- short 横 then a short curved 撇 tail
  2. Middle 撇 -- from upper area, curves down-left across the 捺
  3. Long 捺 -- from near top-center, sweeps down-right, thickens
     near the end, extending well past the 撇's endpoint x

Revision notes vs pass 1:
  - Slimmed top 横撇 (smaller shoulder dab, thinner tail)
  - Reduced 撇 start-顿 dab from r=10 to r=7 (matches standalone
    scale-up discipline)
  - Made 捺 taper start even thinner and extend a bit further right
  - Ensured the 撇 clearly crosses the 捺 in the middle
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        steps = int(max(60, math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    x0, y0 = p0
    xc, yc = p1
    x1, y1 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x1
        y = u * u * y0 + 2 * u * t * yc + t * t * y1
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Stroke 1: 横撇 (top curl) ---
# Very short 横 going slightly up-right
p1a = (138, 80)
p1b = (172, 75)
line_dabs(p1a, p1b, 4.5, 5.5)
# Small shoulder dab (r+2 at real corner)
dab(*p1b, 7)
# Short bowed 撇 tail curving down-left
bezier_dabs(p1b, (165, 100), (135, 130), 5.5, 1.5, steps=180)

# --- Stroke 2: 撇 (main middle stroke) ---
# From upper-right of the top curl, sweep down-left across the 捺 path.
# Start-顿 dab is modest (r=7) per standalone discipline.
dab(180, 92, 7)
bezier_dabs((180, 92), (145, 175), (78, 240), 7.0, 1.5, steps=280)

# --- Stroke 3: 捺 (long press-down) ---
# Starts near the top-center, arcs down-right, crossing the 撇 near
# the middle of the canvas, then thickens toward a broad terminal
# press-foot at the lower-right.
def na_stroke(p0, p1, p2, r0, r_peak, r_end, steps=350):
    x0, y0 = p0
    xc, yc = p1
    x1, y1 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x1
        y = u * u * y0 + 2 * u * t * yc + t * t * y1
        # thin start; ramp to peak thickness at t=0.85; slight
        # narrowing at very end (foot tip)
        if t < 0.85:
            r = r0 + (r_peak - r0) * (t / 0.85)
        else:
            r = r_peak + (r_end - r_peak) * ((t - 0.85) / 0.15)
        dab(x, y, r)


na_stroke((152, 112), (180, 200), (275, 258), 1.6, 11.0, 4.5, steps=380)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_084_夊/01_夊.png"
)
print("saved")
