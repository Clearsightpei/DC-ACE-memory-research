"""
Render 牛 (radical, 4 strokes) at 300x300 with PIL brush-dabs.

Stroke count / order (per label 牛 = 4画):
  1. 撇 (short throw-away)  — top-left area, upper-right start → lower-left tip
  2. 短横 (short horizontal) — meets 撇 tip / crosses just below top, then a bit right
  3. 长横 (long horizontal)  — middle band, longer than stroke 2
  4. 竖 (vertical, straight) — passes through top area down through both 横 to bottom

Key rules applied:
  * Principle 6 length-ratio discipline — bottom 横 clearly LONGER than upper 横.
  * Principle 3 crossings visible — 竖 clearly cuts through both 横; 撇 clearly
    starts left of the vertical and slants down-left away from the 竖.
  * Principle 4 hook discipline — 牛 has NO hook on the 竖 (that would be 千
    or 手 territory). Terminal is a blunt round press.
  * Standalone-scale discipline — modest 顿 dabs (r+1), not big balls; strokes
    fill canvas well.
"""

from PIL import Image, ImageDraw
import math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(p0, p1, r_start, r_end, steps=None):
    """Straight taper stroke via brush-dabs."""
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        length = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(length * 2.5))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=200, ease=1.0):
    """Quadratic Bezier taper stroke."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---- Layout anchors ----
# Center vertical column at x = 150
VX = 150

# Top 撇: starts near (165, 50), tips down-left toward (85, 135). Longer/steeper.
p_pie_start = (168, 50)
p_pie_ctrl = (140, 88)
p_pie_end = (88, 138)

# Short 横 (upper): starts at/near the 撇 tip, tilts up-right, ends past 竖.
h1_start = (95, 132)
h1_end = (210, 115)  # noticeable upward tilt

# Long 横 (middle): significantly longer, well below the upper 横.
h2_start = (50, 172)
h2_end = (265, 160)  # slight upward tilt

# Vertical 竖: starts high (near the top of 撇 area), through both 横 to bottom.
v_start = (VX, 72)
v_end = (VX, 272)


# ---- Draw in canonical order ----

# 1. 撇 — throw-away, thick→thin taper, modest 顿 start (standalone: r=6-8)
dab(*p_pie_start, r=6.5)  # 顿笔 — smaller than compound-scale
bezier_stroke(p_pie_start, p_pie_ctrl, p_pie_end,
              r_start=6.0, r_end=1.2, steps=240, ease=1.0)

# 2. Short 横 — thinner, plain endpoints (no visible ball at standalone termini)
stroke_line(h1_start, h1_end, r_start=4.2, r_end=4.2)
dab(*h1_end, r=4.6)  # very subtle terminal (r+0.4)

# 3. Long 横 — uniform, subtle 顿 at start, slightly firmer at end
dab(*h2_start, r=5.0)
stroke_line(h2_start, h2_end, r_start=4.2, r_end=4.4)
dab(*h2_end, r=5.0)  # subtle terminal press (not a ball)

# 4. 竖 — straight vertical, subtle 顿 start, blunt (not ball) terminal
dab(*v_start, r=5.0)  # 顿 start
stroke_line(v_start, v_end, r_start=4.2, r_end=4.2)
dab(*v_end, r=4.6)  # blunt round terminal (NO hook — 牛 not 千)


out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_106_牛/01_牛.png"
img.save(out_path)
print(f"Saved {out_path}")
