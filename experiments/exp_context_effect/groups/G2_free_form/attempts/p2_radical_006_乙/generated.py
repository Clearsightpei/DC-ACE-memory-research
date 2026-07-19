"""Render 乙 as a single continuous 横折弯钩-like stroke.

Reference: GT shows a short top 横 that transitions via a subtle bend
into a bowed diagonal descent, then curves smoothly around into a long
rightward horizontal, terminating in a short upward hook on the right.

Rendering: PIL brush-dabs (thin-ish uniform radius so the whole stroke
reads as one continuous ink line, as in the GT).
"""
import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_quad(p0, p1, p2, r_start, r_end, steps=260):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


R = 5.0  # base ink radius — thin, uniform, matches GT hairline feel

# --- Beat 1: short top 横, gently arcing down at its right end -----------
# GT top is a shallow curve: starts around (95, 100), pushes right and
# slightly down to about (175, 108), where it begins to bend into the
# diagonal. Use a shallow Bezier for a soft, hand-drawn feel.
top_p0 = (80, 95)
top_p2 = (188, 105)
top_p1 = (130, 82)  # gentle upward bow like a shallow smile inverted
bezier_quad(top_p0, top_p1, top_p2, r_start=R + 1.5, r_end=R, steps=140)

# --- Beat 2: bowed diagonal descent (the "throat" of 乙) ------------------
# From end of top (178,108) curving down-and-left toward about (95, 210).
# The bow should be pulled toward the RIGHT (belly on the right / concave
# to the lower-left), giving 乙 its characteristic slightly-hollow throat.
throat_p0 = (188, 105)
throat_p2 = (85, 215)
throat_p1 = (195, 180)  # control pulled right → belly-on-right
bezier_quad(throat_p0, throat_p1, throat_p2, r_start=R, r_end=R, steps=220)

# --- Beat 3: smooth arc turning down-and-then-right, into bottom 横 -------
# Use the tangent-continuous LEFTWARD→right-horizontal variant:
#   x = x0 - R_arc*(1 - cos(t*pi/2)),  y = y0 + R_arc*sin(t*pi/2)
# Wait: we're going from a point where motion is heading down-and-left,
# and we need to end going purely rightward. Use the standard
# vertical→right-horizontal arc, starting from a synthetic point directly
# ABOVE the true bottom-left corner so the arc's tangent at t=0 matches
# the downward motion.
arc_x0, arc_y0 = 85, 215   # start at end of throat
R_arc = 36
arc_steps = 90
# Symmetric variant: descending-vertical → rightward-horizontal
# End point will be (arc_x0 + R_arc, arc_y0 + R_arc) = (127, 237)
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = arc_x0 + R_arc * (1 - math.cos(t * math.pi / 2))
    y = arc_y0 + R_arc * math.sin(t * math.pi / 2)
    dab(x, y, R)

arc_end = (arc_x0 + R_arc, arc_y0 + R_arc)  # (127, 237)

# --- Beat 4: long bottom 横 running rightward ------------------------------
bot_p0 = arc_end
bot_p2 = (240, 251)
bot_steps = 200
for i in range(bot_steps + 1):
    t = i / bot_steps
    x = bot_p0[0] + (bot_p2[0] - bot_p0[0]) * t
    y = bot_p0[1] + (bot_p2[1] - bot_p0[1]) * t
    dab(x, y, R)

# --- Terminal upward hook on the right -----------------------------------
# GT shows a short vertical stub rising up from the right end of the
# bottom 横. Straight up, ~28 px, mild taper.
hook_p0 = bot_p2
hook_len = 30
hook_steps = 80
for i in range(hook_steps + 1):
    t = i / hook_steps
    x = hook_p0[0]
    y = hook_p0[1] - hook_len * t
    r = R + 0.5 - (R + 0.5 - 2.2) * t  # taper slightly
    dab(x, y, r)

# Small terminal press at the very top of the hook (round-cap the tip)
dab(hook_p0[0], hook_p0[1] - hook_len, 2.4)

# 顿笔 at the start of the top 横 (subtle, standalone-scale)
dab(top_p0[0], top_p0[1], R + 1.0)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_006_乙/01_乙.png")
