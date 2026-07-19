"""Render 入 (2-stroke radical) — RETRY #1.

Errata fix idea: prior attempt drew 撇 first at peak, 捺 attached just
below — but strokes still met visually at a single apex, reading as 人.
The distinguishing signature of 入 vs 人 is the OVERHANG: the 捺's
top-left tip must poke UP and to the LEFT of the 撇's start point.

Retry strategy (per errata note):
  1. Draw 捺 FIRST. Its head starts high on the upper-left (y ~ 60).
  2. Draw 撇 SECOND, starting at ~(150, 90) — a good 30 px BELOW and
     to the RIGHT of the 捺's top. The 撇's start is a 顿-press ON
     the 捺 body (which is diving down-right from higher up), so the
     upper-left tail of the 捺 sticks out above/left of the 撇 start.
  3. 捺: thin→thick, ending in broad flat foot lower-right.
  4. 撇: thick→thin, sweeping down-and-left, gentle bow.

This produces the clear "overhang" silhouette 入 needs.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(P0, P1, P2, r_start, r_end, steps=500, ease=1.0):
    """Quadratic Bezier stroke with tapered brush-dabs."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
        y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---- Stroke 1 (drawn first): 捺 (na) ----
# Starts HIGH on the upper-left area, runs down-and-right to a broad foot.
# The head sits noticeably above (~y=65) so its upper-left tip will
# overhang above the 撇's start point (y=95). Thinner-scale calligraphy
# to match GT — max radius ~7 (not 11).
Q0 = (118, 65)       # head, upper-left — HIGHER than 撇 start
Q2 = (250, 240)      # foot, lower-right
Q1 = (170, 150)      # control — belly on the lower-left of the chord
# 捺 has a sharp thin start (like a fine tip)
dab(Q0[0], Q0[1], 2.0)
bezier_stroke(Q0, Q1, Q2, r_start=2.0, r_end=8.0, steps=550, ease=0.85)
# Terminal foot (捺 press) — moderate, not huge
dab(Q2[0], Q2[1], 8.5)
# Slight extension of the foot for a flat terminal
for i in range(18):
    t = i / 18
    x = Q2[0] + t * 8
    y = Q2[1] + t * 1.5
    dab(x, y, 8.0 - t * 2.5)


# ---- Stroke 2 (drawn second): 撇 (pie) ----
# Starts on the 捺 body around (150, 95) — 30 px BELOW the 捺 head.
# The 捺's upper-left segment (from (118,65) down to ~(150,95)) remains
# visible ABOVE-AND-LEFT of the 撇 start — this is the OVERHANG signature.
# Small 顿 press only (r+1, not r+3) — no visible ball.
P0 = (150, 95)       # start on the 捺 body, below the 捺 head
P2 = (55, 250)       # tip, lower-left
P1 = (108, 170)      # control — gentle rightward bow (belly toward lower-left)
# Small 顿 press at start — sits on the 捺 body, hides seam without ball
dab(P0[0], P0[1], 6.0)
bezier_stroke(P0, P1, P2, r_start=6.5, r_end=1.8, steps=500, ease=1.25)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_030_入__retry_1/01_入.png"
)
print("wrote 01_入.png")
