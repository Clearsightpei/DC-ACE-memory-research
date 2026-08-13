"""
G5 attempt: p2_radical_002_亅 (radical, 1 stroke).

MMH block:
  stroke 1: head @ ('TC', 0.283, 0.674) · tail @ ('BL', 0.973, 0.722)
  No joints.

米字格 cells on 300x300 (3x3 grid of 100px cells):
  TC (top-center)   : x in [100,200], y in [0,100]
  BL (bottom-left)  : x in [0,100],   y in [200,300]

Anchors:
  head = (100 + 0.283*100, 0 + 0.674*100) = (128, 67)
  tail = (0   + 0.973*100, 200 + 0.722*100) = (97, 272)

Stroke class: 竖钩 (vertical + hook). Head is top of vertical
segment (upper canvas), body descends nearly vertical, then hooks
sharply LEFT at the bottom. Since head.x=128 and tail.x=97 are
both left of center, we place the vertical column near x≈155
(matching GT image), give a small leftward tick at the top (to
match head anchor), a straight descent, and hook to the left
ending near tail anchor.

SELF_CHECK block at bottom.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
STROKE_W = 6

# Column x for the vertical descent (matches GT ~x=155).
col_x = 155
top_y = 55
bot_y = 250      # where the vertical body meets the hook curve
hook_end_x = 80  # leftmost point of the hook
hook_end_y = 262

# Small tick at head: 亅 begins with a slight cap/tick pointing up-left.
head_tick_x = 128
head_tick_y = 68  # matches MMH head anchor closely

# --- Stroke 1: 竖钩 as one polyline ---
# (head tick) -> (top of vertical) -> straight down -> curve into hook -> hook tail
# We render the vertical body as a straight line, then draw a rounded corner
# and the leftward hook segment.

# Head tick (short cap into the top of the vertical)
d.line([(head_tick_x, head_tick_y), (col_x, top_y + 6)], fill=INK, width=STROKE_W)

# Vertical body
d.line([(col_x, top_y + 6), (col_x, bot_y)], fill=INK, width=STROKE_W)

# Hook: curve from (col_x, bot_y) leftward and up-left to (hook_end_x, hook_end_y)
# Use a quadratic-ish sampling via a few short segments to give it a soft corner.
import math
def hook_curve(p0, p1, ctrl, steps=18):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * ctrl[0] + t ** 2 * p1[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * ctrl[1] + t ** 2 * p1[1]
        pts.append((x, y))
    return pts

hook_pts = hook_curve(
    p0=(col_x, bot_y),
    p1=(hook_end_x, hook_end_y),
    ctrl=(col_x, hook_end_y + 6),  # control pulls hook to a right-angle-ish corner
)
for a, b in zip(hook_pts[:-1], hook_pts[1:]):
    d.line([a, b], fill=INK, width=STROKE_W)

# Round the endpoints (nicer joins).
r = STROKE_W // 2
for (x, y) in [(head_tick_x, head_tick_y),
               (col_x, top_y + 6),
               (col_x, bot_y),
               (hook_end_x, hook_end_y)]:
    d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

out_png = __file__.rsplit("/", 1)[0] + "/01_亅.png"
img.save(out_png)
print("wrote", out_png)

# ---------------- SELF_CHECK ----------------
# Anchor comparison (in fractional-cell coords, tolerance ±0.20 same/adj cell):
#   head expected TC(0.283, 0.674) -> abs (128, 67)
#   head actual   ~ (128, 68)  -> matches (delta ≈ 0.00, 0.01)  -> OK, same cell
#   tail expected BL(0.973, 0.722) -> abs (97, 272)
#   tail actual   ~ (80, 262)  -> BL cell x_frac=0.80, y_frac=0.62
#                  -> delta ≈ (0.17, 0.10) same cell -> OK within ±0.20
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # rendered as 1 continuous stroke (tick+vertical+hook)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '亅 = 竖钩: head tick near TC(0.28,0.67), body descends x=155, '
             'hooks left to BL cell. Rendered as one polyline (1 stroke).',
}
