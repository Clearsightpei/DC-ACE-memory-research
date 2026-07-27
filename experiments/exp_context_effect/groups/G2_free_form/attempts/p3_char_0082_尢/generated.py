"""Render 尢 (3 strokes) at 300x300, white bg, black ink.

Strokes (per GT + form_catalog "leg-pair splay" + "撇 + 竖弯钩 as leg-pair"):
  1. 撇 (short top-left flick) — small down-left flick from around (140,55) to (110,95)
  2. 横 (top bar) — long, slightly rising, from (60,110) to (215,100)
  3. 竖弯钩 (right leg) — starts near right end of the 横 (~195,90), descends,
     curves rightward at baseline, hooks up-left.
  The 撇-body on the left descends after crossing the 横 further down to (~65,255)
  — actually GT shows the top short flick + a longer body-crossing 撇 IS ONE STROKE
  going from top-right area down-left through the bar. Re-read: 尢 is 3 strokes:
   横 + 撇 (long, through the bar) + 竖弯钩.
Re-mapped:
  1. 横 — bar y≈110, x 60..215
  2. 撇 — starts top around (150,55), passes through the bar, ends lower-left (65,260)
  3. 竖弯钩 — starts near (195,90), goes down to (~195,220), curves right to (~245,255), hooks up-left
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def brush_line(draw, pts, widths):
    """Draw a variable-width polyline by stroking segments with a circular brush at each sample."""
    # pts: list of (x,y); widths: list of radii per point (same length)
    # Fill circles between samples so lines look continuous.
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(1, int(dist * 2))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = w0 + (w1 - w0) * t
            draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

def sample_bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts

# --- Stroke 1: 横 (top bar, slight upward tilt to the right) ---
heng_pts = [(58, 118), (140, 110), (215, 105)]
heng_widths = [6, 5.5, 4.5]
brush_line(d, heng_pts, heng_widths)

# --- Stroke 2: 撇 (throw down-left, starting from top-right of the bar area,
#     passing through the bar, curving to lower-left) ---
pie = sample_bezier((150, 85), (115, 160), (55, 265), n=60)
pie_widths = [4 + 2 * (1 - i / (len(pie) - 1)) for i in range(len(pie))]  # thicker at top
# Taper the tip a bit
pie_widths = [max(1.5, w) for w in pie_widths]
brush_line(d, pie, pie_widths)

# --- Stroke 3: 竖弯钩 — starts near right end of the bar, descends,
#     curves rightward at baseline, hooks up-left ---
# Segment A: vertical descent
seg_a = sample_bezier((195, 100), (200, 170), (205, 225), n=40)
# Segment B: curve rightward
seg_b = sample_bezier((205, 225), (220, 260), (255, 265), n=30)
# Segment C: hook up-left
seg_c = [(255, 265), (255, 248), (243, 240)]

full = seg_a + seg_b[1:] + seg_c[1:]
# Widths: uniform-ish, slight swell in curve, taper at hook tip
widths = []
n = len(full)
for i in range(n):
    if i < len(seg_a):
        widths.append(5.0)
    elif i < len(seg_a) + len(seg_b) - 1:
        widths.append(5.5)
    else:
        # hook taper
        k = (i - (len(seg_a) + len(seg_b) - 1)) / max(1, len(seg_c) - 1)
        widths.append(5.5 - 3.5 * k)

brush_line(d, full, widths)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0082_尢/01_尢.png")
