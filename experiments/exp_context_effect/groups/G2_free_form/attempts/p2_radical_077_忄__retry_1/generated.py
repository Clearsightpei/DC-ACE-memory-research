"""
p2_radical_077_忄  retry_1  (G2 free-form)

Fix per errata:
  Prior attempt made left dot a full 撇 (too long) and right side a
  竖 nub, so silhouette read as 什, not 忄.
  Form_catalog "点 as 忄 heart-radical side dot":
    - LEFT dot: SHORT ~35 px teardrop, thin→thick, angled ~50-60°
      down-right, sits ~(90, 130) LEFT of the 竖.
    - RIGHT dot: SHORT ~30 px 横-flick or 点 at ~(160, 125).
    - Central 竖: long vertical y≈70→250 with 顿 dab at TOP only.
    - NO hook at the bottom of the 竖.

Renders 300x300 white bg, black ink, using PIL brush-dabs.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush(x, y, r):
    """Filled circular brush dab of radius r at (x,y)."""
    draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def tapered_line(p0, p1, r_start, r_end, steps=None):
    """Draw a straight tapered stroke from p0 to p1, radius r_start->r_end."""
    x0, y0 = p0
    x1, y1 = p1
    dx = x1 - x0
    dy = y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(int(dist * 2), 8)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r_start + (r_end - r_start) * t
        brush(x, y, r)


# ------------------------------------------------------------------
# Stroke 1: central 竖 (long vertical)
# Top has a 顿 dab (start radius bigger), body ~ steady width,
# bottom NO hook — just a tiny press.
# ------------------------------------------------------------------
# Slight 顿 press at top -> steady body
top = (150, 72)
mid = (150, 160)
bot = (150, 252)

# Extra fat starting dab (顿笔)
brush(top[0], top[1], 8)
tapered_line(top, mid, r_start=7, r_end=6)
tapered_line(mid, bot, r_start=6, r_end=6)
# Tiny press at bottom (no hook)
brush(bot[0], bot[1], 6)

# ------------------------------------------------------------------
# Stroke 2: LEFT dot — short 35 px teardrop, thin -> thick,
# angled ~55 deg down-right, positioned so its center is near (90, 130).
# Start upper-left, end lower-right.
# ------------------------------------------------------------------
LEFT_LEN = 35
angle_left = math.radians(60)   # down-right
lx0 = 90 - (LEFT_LEN / 2) * math.cos(angle_left)
ly0 = 130 - (LEFT_LEN / 2) * math.sin(angle_left)
lx1 = 90 + (LEFT_LEN / 2) * math.cos(angle_left)
ly1 = 130 + (LEFT_LEN / 2) * math.sin(angle_left)
tapered_line((lx0, ly0), (lx1, ly1), r_start=2, r_end=7)
# heavy terminal press (thick end of teardrop)
brush(lx1, ly1, 7)

# ------------------------------------------------------------------
# Stroke 3: RIGHT dot — short 横-flick ~30 px starting near the 竖
# and flicking rightward+slightly down, at ~(160, 125).
# Thin at right end.
# ------------------------------------------------------------------
RIGHT_LEN = 32
# Start close to the 竖 (x ~ 158), end ~30 px to the right
rx0, ry0 = 158, 125
rx1, ry1 = rx0 + RIGHT_LEN, ry0 + 6   # slight downward slope
# Thick start (顿 press against the 竖), thin flick to the right
brush(rx0, ry0, 6)
tapered_line((rx0, ry0), (rx1, ry1), r_start=6, r_end=2)

# ------------------------------------------------------------------
img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_077_忄__retry_1/01_忄.png")
print("wrote 01_忄.png")
