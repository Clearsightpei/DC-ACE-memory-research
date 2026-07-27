"""
p3_char_0003_乙 — the character 乙

乙 is a single continuous stroke: 横折弯钩 style but scaled to fill
canvas. Structure (observed from GT):
  1. Very short 横 at top, slight up-tilt, sitting upper-middle.
  2. Sharp 折 shoulder, direction change to down-left curve.
  3. Long 弯 body — sweeping curve from upper-middle down to the
     bottom-left area, then arcing rightward along the baseline.
  4. Short upward hook (钩) at the right end, flicking up.

Canvas 300x300, white bg, black ink. Image coords: y grows DOWN.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def stroke_line(x0, y0, x1, y1, r_start, r_end, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(80, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_cubic(p0, p1, p2, p3, r_start, r_end, steps=300):
    """Cubic Bezier via brush-dabs with tapered width."""
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = (omt**3) * p0[0] + 3 * (omt**2) * t * p1[0] + 3 * omt * (t**2) * p2[0] + (t**3) * p3[0]
        y = (omt**3) * p0[1] + 3 * (omt**2) * t * p1[1] + 3 * omt * (t**2) * p2[1] + (t**3) * p3[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


BASE_R = 4.5

# ---- Beat 1: 横 — short, slight up-tilt at top ----
# Top-横 sits around y=95, spans from about x=85 to x=155.
h_x0, h_y0 = 85, 100
h_x1, h_y1 = 155, 92    # slight up-tilt
dab(h_x0, h_y0, BASE_R + 2.0)         # 顿 dab at start
stroke_line(h_x0, h_y0, h_x1, h_y1, BASE_R, BASE_R + 0.3)

# ---- Beat 2: 折 shoulder-dab ----
dab(h_x1, h_y1, BASE_R + 2.2)

# ---- Beat 3+4: 竖 down-flare + 弯 big sweeping body ----
# From shoulder (155, 92), the stroke first drops nearly vertically for
# a short distance, then bellies out into a wide curve that sweeps
# down-left to the bottom-left corner area, then arcs rightward along
# the bottom to reach the right side.
#
# Using cubic Beziers to shape the wan body.
# Segment A: from shoulder down to a mid-point on the way to bottom-left.
#   p0 = (155, 92) — shoulder end
#   p1 = (155, 145) — pulls straight down first (short vertical feel)
#   p2 = (155, 210) — continues down, then curls leftward
#   p3 = (90, 250)  — bottom-left of the big sweep

bezier_cubic(
    (155, 92), (158, 150), (150, 215), (90, 250),
    r_start=BASE_R + 0.5, r_end=BASE_R + 0.7,
    steps=280,
)

# Segment B: from bottom-left sweep across the baseline to bottom-right.
#   p0 = (90, 250)
#   p1 = (110, 275)  — dips down slightly along baseline
#   p2 = (180, 275)
#   p3 = (225, 240)  — turns upward as we head toward the hook base

bezier_cubic(
    (90, 250), (110, 278), (185, 278), (230, 230),
    r_start=BASE_R + 0.7, r_end=BASE_R + 0.3,
    steps=260,
)

# ---- Beat 5: hook flick — short upward flick at right end ----
# From (230, 230), flick up (nearly straight up), taller flick for
# closer GT match.
hook_base = (230, 230)
# Small joining press at hook base
dab(hook_base[0], hook_base[1], BASE_R + 1.2)

flick_len = 62
flick_angle_deg = -95    # nearly straight up, very slight leftward lean
fa = math.radians(flick_angle_deg)
fx1 = hook_base[0] + flick_len * math.cos(fa)
fy1 = hook_base[1] + flick_len * math.sin(fa)
stroke_line(hook_base[0], hook_base[1], fx1, fy1, BASE_R + 0.3, 1.0, steps=180)

# Save
out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0003_乙/01_乙.png"
img.save(out)
print(f"Saved: {out}")
