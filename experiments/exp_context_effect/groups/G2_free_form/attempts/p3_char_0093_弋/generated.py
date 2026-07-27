"""
p3_char_0093_弋 — 3 strokes: 横 (mid horizontal), 斜钩 (long slant hook down-right), 点 (upper-right dot).
Memory references:
 - drawer_memory row 437: 斜钩 Bezier P0=(95,55)→P2=(245,245), ctrl=(125,195); hook flick ~-110°
 - form_catalog: compact upper radicals — silhouette-first
 - Beat count = 3. Draw the flick (explicit final beat).
GT observation: 横 is short-ish, roughly through middle; 斜钩 starts near top-left,
belly bows to lower-left, and the terminal hook flicks upward off the bottom-right.
点 sits at the upper-right area, small teardrop tilting down-right.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier(p0, p1, p2, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts

def stroke(pts, width_seq):
    # brush-dab along the path with per-point width
    for (x, y), w in zip(pts, width_seq):
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def taper_widths(n, w_start, w_end):
    return [w_start + (w_end - w_start) * i / (n - 1) for i in range(n)]

# ---- Stroke 1: 斜钩 (draw first as the primary body-defining stroke) ----
# Long S-curve from upper-left area sweeping to lower-right, belly toward lower-left.
p0 = (110, 90)
ctrl = (135, 200)
p2 = (240, 245)
pts = bezier(p0, ctrl, p2, n=80)
widths = taper_widths(len(pts), 8, 10)
stroke(pts, widths)

# terminal hook flick: from (240,245) up-and-right (angle ~ -30° from horiz, short)
import math
hook_len = 28
hook_angle = math.radians(-35)  # up-right
hx = 240 + hook_len * math.cos(hook_angle)
hy = 245 + hook_len * math.sin(hook_angle)
hook_pts = [(240 + (hx - 240) * t, 245 + (hy - 245) * t) for t in [i/20 for i in range(21)]]
stroke(hook_pts, taper_widths(len(hook_pts), 10, 3))

# ---- Stroke 2: 横 (short horizontal crossing the 斜钩 near the middle) ----
# Crosses the 斜钩 body around y≈155; extends left of body, ends just past the body
h_start = (65, 158)
h_end = (215, 148)  # slight up-tilt
n = 40
h_pts = [(h_start[0] + (h_end[0] - h_start[0]) * i/n, h_start[1] + (h_end[1] - h_start[1]) * i/n) for i in range(n + 1)]
stroke(h_pts, taper_widths(len(h_pts), 7, 8))
# small terminal press dab
d.ellipse((215 - 5, 148 - 5, 215 + 5, 148 + 5), fill="black")

# ---- Stroke 3: 点 (dot at upper right, tilted like a teardrop pointing down-right) ----
# Small angled teardrop from (200,75) toward (225,100)
dp0 = (200, 75)
dp1 = (215, 82)
dp2 = (228, 100)
dpts = bezier(dp0, dp1, dp2, n=25)
dwidths = taper_widths(len(dpts), 4, 10)
stroke(dpts, dwidths)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0093_弋/01_弋.png")
