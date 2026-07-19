"""
亻 (p2_radical_029_亻) — 2画 radical "人字旁" (single-person radical).

Structure (per GT PNG):
- Stroke 1: 撇 (throw-away) — starts upper-right, curves down-and-left with
  a rightward belly (concave-left). Long, thick→thin taper, sharp tip in
  the lower-left region.
- Stroke 2: 竖 (vertical) — starts at (or just below) the midpoint of the
  撇, drops straight down. Blunt terminal (no hook flick — this is a plain
  竖, not 竖钩).

Renderer: PIL brush-dabs (per drawer_memory.md general technique). 300×300
white canvas, black ink.

Standalone-scale discipline (per memory):
- Curvature more pronounced (Bezier ctrl pulled ~50 px off chord midpoint).
- Smaller 顿-dab at start (r=8, not r=12).
- Plain endpoint at 撇 tip and 竖 base (no r+2 balls at standalone termini).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    """Quadratic Bezier with linearly (or eased) tapering radius."""
    for i in range(steps + 1):
        t = i / steps
        # Bezier position
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def line_stroke(p0, p1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------------- Stroke 1: 撇 (throw-away) ----------------
# Upper-right start, sweeping down-and-left. Belly on the right side
# (concave-left). Long stroke because 亻 is dominant top-half in the GT.
pie_p0 = (180, 60)     # upper-right start
pie_p2 = (75, 225)     # lower-left tip
pie_ctrl = (170, 130)  # control point pulled toward interior (right side)

# 顿笔 dab at start (small for standalone)
dab(pie_p0[0], pie_p0[1], 8)
bezier_stroke(pie_p0, pie_ctrl, pie_p2, r_start=8.5, r_end=1.5,
              steps=500, ease=1.3)

# ---------------- Stroke 2: 竖 (vertical) ----------------
# Starts at the midpoint of the 撇 (roughly halfway down the curve),
# drops straight down. Blunt terminal (no hook — this is 亻, not 亻with hook).
shu_top = (160, 130)   # sits under/right of 撇 midpoint
shu_bot = (160, 250)   # drops straight down

# 顿笔 dab at start (small joining dab where it meets 撇)
dab(shu_top[0], shu_top[1], 6.5)
line_stroke(shu_top, shu_bot, r_start=5.5, r_end=5.5, steps=250)
# Small terminal press (plain, r+1 not r+2 for standalone)
dab(shu_bot[0], shu_bot[1], 6.5)

# ---------------- Save ----------------
out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_029_亻/01_亻.png"
img.save(out)
print(f"Saved {out}")
