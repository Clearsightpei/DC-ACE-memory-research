"""Render 亅 (character, Phase 3) to 300x300 PNG using PIL brush-dab technique.

GT observation:
- Vertical stroke positioned RIGHT of center (~x=180).
- Small entry curve at top (subtle downturn from the left, like a
  short 顿-with-arc start).
- Vertical descends straight, uniform width.
- Terminal is a leftward-flick HOOK at the bottom (nearly horizontal,
  going LEFT), not an up-left flick. Calligraphic 竖钩 as standalone.

Notes (form_catalog + drawer_memory):
- 亅 is a 竖钩. Hook is the identity — draw it explicitly (not as
  taper-loop afterthought). See "Draw the flick" rule.
- Standalone char, so it can occupy vertical center of canvas
  comfortably; use ~150 px vertical extent centered around y=155.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier(p0, p1, p2, r0, r1, steps=120):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Entry curve at top: small downward-right arc into top of vertical
# Simulates the calligraphic entry of a 竖钩 (a small "hooked in" start).
bezier((160, 72), (168, 72), (180, 82), 3.5, 6.0, steps=100)

# ---- Main vertical (竖) ----
# From top (180, 82) down to (180, 235). Uniform r=6.
line_taper((180, 82), (180, 235), 6.0, 6.0, steps=400)

# 顿 dab at top of vertical (subtle press)
dab(180, 82, 6.5)

# ---- Bottom hook: leftward flick (nearly horizontal) ----
# From (180, 235) going LEFT to (138, 240), tapering to sharp tip.
# Slight downward-then-flat curve for smooth curl.
bezier((180, 235), (172, 246), (138, 240), 6.5, 1.2, steps=140)

# Small joining dab at hook root to hide seam (per hook-base discipline:
# do NOT exceed segment radius — 7.0 ~ r+1 is tolerable at bend base,
# use conservatively).
dab(180, 235, 6.5)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0008_亅/01_亅.png"
)
print("saved")
