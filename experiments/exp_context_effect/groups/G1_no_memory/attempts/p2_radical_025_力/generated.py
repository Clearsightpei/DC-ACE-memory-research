"""G1 render for 力 (radical, 2 strokes).

Revised pass: widen the character, better balance, more diagonal 撇,
more clearly-curved 横折钩 with a definite hook flick at the bottom.

Strokes:
  1) 横折钩 (héng zhé gōu): horizontal top spanning most of the character
     width, then turn down and curve leftward, ending with a short
     upward hook.
  2) 撇 (piě): a long diagonal from below the top-horizontal near its
     left third, sweeping down-left to the lower-left corner.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
STROKE = 6


def line(p0, p1, w=STROKE):
    draw.line([p0, p1], fill=BLACK, width=w)
    r = w // 2
    for p in (p0, p1):
        draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=BLACK)


def polyline(pts, w=STROKE):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i+1], w)


# ---------- Stroke 1: 横折钩 ----------
# Top horizontal — wide, slight up-tilt to the right (calligraphic).
top_start = (95, 108)
top_end   = (205, 96)
# Small corner turn (顿) then long curved descent to lower-left,
# ending with an upward hook (钩).
corner    = (212, 108)
curve_pts = [
    corner,
    (212, 140),
    (206, 175),
    (192, 210),
    (170, 238),
    (148, 252),
]
# hook: flick up-left
hook_end = (135, 240)

polyline([top_start, top_end, corner], w=STROKE)
polyline(curve_pts, w=STROKE)
line(curve_pts[-1], hook_end, w=STROKE)


# ---------- Stroke 2: 撇 ----------
# Starts on the top horizontal at ~1/3 from the left, sweeps down-left
# with a slight curve, ending near the lower-left of the frame.
pie_start = (128, 118)
pie_c1    = (108, 165)
pie_c2    = (85,  210)
pie_end   = (60,  255)
polyline([pie_start, pie_c1, pie_c2, pie_end], w=STROKE)


# ---------- save ----------
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_力.png")
img.save(out_path)
print(f"Saved: {out_path}")
